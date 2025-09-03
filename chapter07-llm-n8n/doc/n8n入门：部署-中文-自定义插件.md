## Ngork安装

Install ngrok via Apt with the following command:

```sh
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
  && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list \
  && sudo apt update \
  && sudo apt install ngrok
```

Run the following command to add your authtoken to the default **ngrok.yml** [configuration file](https://ngrok.com/docs/agent/config/).

```sh
ngrok config add-authtoken 2zo0ukGSh7rLCwIJLcyEEqQEcyC_5DPqPXokBtt3MbofiUTJ5
```

或者使用离线方式安装

下载 https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz

```sh
sudo tar -xvzf ~/Downloads/ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
```

Run the following command to add your authtoken to the default **ngrok.yml** [configuration file](https://ngrok.com/docs/agent/config/).

```sh
ngrok config add-authtoken 2zo0ukGSh7rLCwIJLcyEEqQEcyC_5DPqPXokBtt3MbofiUTJ5
```

#### 在线部署您的应用

将您的应用放在一个[临时域名](https://ngrok.com/docs/network-edge/domains-and-tcp-addresses/#ephemeral-domains)上线，并转发到您的上游服务。例如，如果它正在监听端口，请运行： `http://localhost:8080`

```bash
ngrok http http://localhost:5678
```

## n8n

有了 Ngrok 提供的公网地址，我们需要在启动 n8n 时告诉它："嘿，外面的世界要通过这个地址找到你！"

```bash
docker run -it --rm \
    --name n8n \
    -p 5678:5678 \
    -v n8n_data:/home/node/.n8n \
    -e WEBHOOK_URL=https://f0b3f440cf01.ngrok-free.app \
    docker.n8n.io/n8nio/n8n
```

看到那个WEBHOOK_URL环境变量了吗？这就是关键！它告诉 n8n："当需要生成 webhook URL 时，请使用 Ngrok的地址，而不是 localhost。"

## 部署 n8n 中文版

### 1. 准备工作

#### 拉取 n8n 镜像

首先，我们需要从 Docker 仓库拉取指定版本的 n8n 镜像。

```Bash
docker pull docker.1ms.run/n8nio/n8n:1.101.1
```

#### 创建数据卷 (Volume)

创建两个 Docker 数据卷，一个用于存储 n8n 的运行时数据，另一个用于挂载中文语言包。

1. 创建 n8n 数据卷：

   这个数据卷将保存你的工作流、凭据等 n8n 相关数据，确保数据持久化。

   ```Bash
   docker volume create n8n_data
   ```

2. 创建 n8n 多语言数据卷目录：

   这个目录将用于存放下载的中文语言包。

   ```Bash
   mkdir -p /home/data/n8n_i18n
   cd /home/data/n8n_i18n
   ```

### 2. 下载并解压 n8n 中文语言包

为了让 n8n 界面显示中文，我们需要下载并解压对应的中文语言包。

```Bash
wget https://github.com/other-blowsnow/n8n-i18n-chinese/releases/download/n8n%401.101.1/editor-ui.tar.gz
tar -zxvf editor-ui.tar.gz
```

**重要提示：** 请确保你下载的语言包版本 (`n8n@1.101.1`) 与你拉取的 n8n 镜像版本 (`1.101.1`) 一致，否则可能导致显示异常或功能问题。

### 3. 启动 n8n 容器

现在，我们将使用 Docker 运行 n8n 容器，并挂载之前创建的数据卷和语言包，同时设置中文作为默认语言。

```Bash
docker run -d \
--name n8n \
-p 5678:5678 \
-v n8n_data:/home/node/.n8n \
-v /home/data/n8n_i18n/dist:/usr/local/lib/node_modules/n8n/node_modules/n8n-editor-ui/dist \
-e WEBHOOK_URL=https://af5741fcd43e.ngrok-free.app \
-e N8N_DEFAULT_LOCALE=zh-CN \
 -e GENERIC_TIMEZONE=Asia/Shanghai \
-e N8N_SECURE_COOKIE=false \
-e N8N_RUNNERS_ENABLED=true \
-e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
docker.1ms.run/n8nio/n8n:1.101.1
```

**参数解释：**

- `-d`: 后台运行容器。
- `--name n8n`: 为容器指定一个名称，方便管理。
- `-p 5678:5678`: 将容器的 5678 端口映射到主机的 5678 端口，这样你可以通过主机访问 n8n。
- `-v n8n_data:/home/node/.n8n`: 将 Docker 数据卷 `n8n_data` 挂载到容器内部 n8n 的数据目录，用于持久化数据。
- `-v /home/data/n8n_i18n/dist:/usr/local/lib/node_modules/n8n/node_modules/n8n-editor-ui/dist`: 将本地的中文语言包目录挂载到容器内 n8n UI 对应的目录。
- `-e N8N_DEFAULT_LOCALE=zh-CN`: 设置 n8n 的默认语言为简体中文。
- `-e N8N_SECURE_COOKIE=false`: 在本地开发环境中，为了方便测试，通常设置为 `false`。
- `-e N8N_RUNNERS_ENABLED=true`: 启用 n8n 的运行器功能。
- `-e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true`: 强制执行设置文件权限。
- `docker.1ms.run/n8nio/n8n:1.101.1`: 指定要运行的 Docker 镜像。

### 4. 访问 n8n

容器启动后，等待几分钟让 n8n 完全启动。然后，你就可以在浏览器中访问 n8n 的 Web 界面了：

打开浏览器，输入地址：`http://localhost:5678` 或 `https://f0b3f440cf01.ngrok-free.app`

首次访问时，你需要注册一个新的账号。注册成功后，使用新注册的账号登录即可开始使用中文版的 n8n。

------

## 注册你的社区版以获得更多功能

n8n 的自部署社区版（又或称开源版）完成部署后，你能见到的功能都是免费的。但有一些功能，需要注册后才能启用，包括：

1. 文件夹功能 - 允许你创建文件夹来整理你的 Workflow。

1. 在编辑器中调试 - 将一条执行记录从 Executions 复制到编辑器进行调试。

1. 24 小时修订历史 - 允许你回滚到一条 Workflow 在过去 24 小时中的任何一次修改。

1. 自定义执行程序 - 保存、查找和注释执行元数据。

注册开源版 n8n 很简单，如果你是最近部署的。在部署完成后的初始化之后，应该会有一个注册界面，在那个界面下输入真实存在的电子邮箱，你就应该就能直接激活。

如果你是之前部署的 n8n，那你需要通过以下步骤完成注册：

1. 在界面中选择左下角的**三个点图标**。

1. 选择**“Settings”选择“Usage and Plan”**。

1. 选择**“Unlock”**输入你的电子邮件，然后点击**”Send me a free license key”**

1. 检查邮箱，找到 Key。

获得许可证密钥后，请单击许可证电子邮件中的按钮或访问 **Settings > Usage and Plan** 并选择 **Enter activation key** 来激活它。

## 安装和管理社区节点

安装社区节点有三种方式：

- 在 n8n 中使用[节点面板](https://docs.n8n.io/integrations/community-nodes/installation/verified-install/)（仅适用于已验证的社区节点）。
- 在 n8n 中[使用 GUI](https://docs.n8n.io/integrations/community-nodes/installation/gui-install/)：使用此方法从 npm 注册表安装社区节点。
- [从命令行手动](https://docs.n8n.io/integrations/community-nodes/installation/manual-install/)：如果您的 n8n 实例不支持通过应用内 GUI 安装，请使用此方法从 npm 安装社区节点。



### 飞书获取自建应用的 tenant_access_token

1. 登录[开发者后台](https://open.feishu.cn/app/)，选择指定的自建应用。

2. 在 **基础信息** > **凭证与基础信息** 页面，获取应用凭证 **App ID** 和 **App Secret**。

   

   ![img](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507151614510.png)

   

3. 调用[自建应用获取 tenant_access_token](https://open.feishu.cn/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token_internal) 接口，通过应用凭证 App ID 和 App Secret 获取自建应用的`tenant_access_token`。

![image-20250715173236647](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507151732849.png)





## **参考资料：**

- n8n 官方 GitHub 仓库：https://github.com/n8n-io/n8n
- n8n 中文语言包 GitHub 仓库：https://github.com/other-blowsnow/n8n-i18n-chinese