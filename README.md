# Butterpply

开发部署文档，我会把开发和部署的细则写进这里

## 环境配置

1. **导航到 `backend` 目录**：

    打开终端或命令行工具，切换到项目的 `backend` 目录。

    ```bash
    cd backend
    ```

2. **创建 `.env` 文件**：

    在 `backend` 目录中创建一个新的 `.env` 文件。

    ```bash
    touch .env
    ```

3. **复制 `.env.example` 文件内容**：

    打开项目根目录下的 `.env.example` 文件，将其中的内容复制到新创建的 `.env` 文件中。

    ```plaintext
    # .env.example 文件内容
    MYSQL_DB=butterpply
    MYSQL_PASSWORD=303816
    MYSQL_PORT=3306
    MYSQL_SCHEMA=mysql+aiomysql
    MYSQL_USERNAME=root
    MYSQL_HOST=127.0.0.1
    ```

4. **修改 `.env` 文件配置**：

    根据你的本地数据库配置，修改 `.env` 文件中的以下字段：

    ```plaintext
    MYSQL_DB=your_database_name
    MYSQL_PASSWORD=your_password
    MYSQL_PORT=your_port
    MYSQL_SCHEMA=mysql+aiomysql
    MYSQL_USERNAME=your_username
    MYSQL_HOST=your_host
    ```

    示例配置：

    ```plaintext
    MYSQL_DB=butterpply
    MYSQL_PASSWORD=303816
    MYSQL_PORT=3306
    MYSQL_SCHEMA=mysql+aiomysql
    MYSQL_USERNAME=root
    MYSQL_HOST=127.0.0.1
    ```

## 运行项目

1. **确保你在 `backend` 目录**：

    确认你已经切换到项目的 `backend` 目录。

    ```bash
    cd backend
    ```

2. **运行 `main.py` 文件**：

    使用 Python 运行 `main.py` 文件。

    ```bash
    python main.py
    ```

## 环境依赖

- 确保你已经安装了所有必要的依赖项。
- 切换到 `backend` 目录后，你可以使用 `pip install -r requirements.txt` 命令安装所有依赖项。
- 你可以使用 `pip freeze` 命令查看所有已安装的依赖项。
- 你可以使用 `pip freeze > requirements.txt` 命令将所有已安装的依赖项保存到 `requirements.txt` 文件中。
- 你可以使用 `pip install -r requirements.txt` 命令安装 `requirements.txt` 文件中的所有依赖项。


## MySQL 数据库
- 数据库名：butterpply
- 这个数据库你在本地部署的时候可以先尝试在本地搭建一个数据库，然后在 `.env` 文件中配置好数据库的用户名、密码、端口等信息，在正式开发的时候，我们会提供一个数据库的远程地址，你只需要将 `.env` 文件中的数据库配置信息替换成远程数据库的配置信息即可。



## Git 开发流程

1. **克隆仓库**：

    如果你还没有克隆仓库，请先克隆项目到本地：

    ```bash
    git clone https://github.com/gavincui1026/Butterpply.git
    cd Butterpply
    ```

2. **创建分支**：

    在进行开发前，创建一个新的分支以进行开发工作：

    ```bash
    git checkout -b Your-Feature-Branch-Name
    ```

3. **进行开发**：

    在新的分支上进行代码开发。

4. **添加和提交更改**：

    在完成开发后，将更改添加到暂存区并提交：

    ```bash
    git add .
    git commit -m "描述你的更改"
    ```

5. **推送分支到远程仓库**：

    将你的分支推送到远程仓库：

    ```bash
    git push origin Your-Feature-Branch-Name
    ```

6. **创建 Pull Request (PR)**：

    在 GitHub 上，导航到你的仓库，创建一个新的 Pull Request，选择你的分支并请求合并到 `master` 分支。

## 合并和发布

1. **合并 Pull Request**：

    当你的代码通过评审后，合并 Pull Request 到 `master` 分支。

2. **删除分支**：

    合并后，可以删除本地和远程的功能分支：

    ```bash
    git branch -d Your-Feature-Branch-Name
    git push origin --delete Your-Feature-Branch-Name
    ```

3. **更新本地 `master` 分支**：

    切换到 `master` 分支并拉取最新的更改：

    ```bash
    git checkout master
    git push origin master
    ```
---



