# Tavily API Key 自动化获取工具

[English](README_EN.md) | 中文

基于深层HTML分析的智能自动化解决方案，实现Tavily API Key的端到端自动获取。

## 快速开始

### 环境要求

- Python 3.7+
- 网络连接
- 2925.com邮箱账户

### 安装

```bash
# 克隆项目
git clone https://github.com/yatotm/tavily-register.git
cd tavily-register

# 自动安装依赖
python setup.py

# 或手动安装
pip install -r requirements.txt
playwright install firefox
```

## VPS 部署指南 (推荐)

此方法适用于在没有图形化界面的 VPS 或服务器上运行。

### 步骤 1: 在本地生成 `email_cookies.json`

首先，在您的本地电脑（带有桌面环境）上生成邮箱的 `cookie` 文件。

```bash
# 确保已安装依赖
pip install -r requirements.txt
playwright install firefox

# 运行 cookie 生成命令
python run_vps.py setup-cookie
```
程序将打开一个浏览器。请在浏览器中 **手动登录您的 2925.com 邮箱**。登录成功后，关闭程序即可。

操作成功后，项目目录下会生成一个 `email_cookies.json` 文件。

### 步骤 2: 上传文件到 VPS

将整个项目文件夹， **包括刚刚生成的 `email_cookies.json` 文件**，上传到您的 VPS。

### 步骤 3: 在 VPS 上运行

在 VPS 上，进入项目目录并执行以下命令：

```bash
# 安装依赖 (首次运行时需要)
pip install -r requirements.txt
playwright install firefox

# 运行自动化注册
# -c 参数指定要注册的账户数量
python run_vps.py run -c 5
```
程序将以无头模式自动完成注册流程。

---

## 本地交互式运行 (旧版)

如果您想在本地电脑上通过交互式菜单运行，请按以下步骤操作。

### 配置

1. **设置邮箱登录**
   ```bash
   python email_login_helper.py
   ```
   按提示完成2925.com邮箱登录并保存cookies。

### 运行

```bash
python main.py
```

选择运行模式：
- **智能自动化模式** (推荐): 高效稳定的自动化流程
- **测试模式**: 传统方式，用于调试和HTML信息收集

## 项目结构

```
tavily-register/
├── run_vps.py                       # VPS 非交互式运行入口
├── main.py                          # 本地交互式主程序
├── intelligent_tavily_automation.py  # 智能自动化核心
├── email_checker.py                 # 邮件验证和登录
├── email_login_helper.py            # 邮箱登录助手
├── tavily_automation.py             # 传统自动化模块
├── config.py                        # 配置文件
├── utils.py                         # 工具函数
├── requirements.txt                 # 依赖列表
├── setup.py                         # 安装脚本
├── api_keys.md                      # API Key保存文件
└── email_cookies.json               # 邮箱cookies
```

## 使用流程

1. **注册阶段**: 自动填写Tavily注册表单
2. **邮件验证**: 智能检测验证邮件并点击验证链接
3. **登录阶段**: 自动登录Tavily账户
4. **API获取**: 智能识别并获取API Key
5. **数据保存**: 保存账户信息和API Key到文件

## 输出格式

API Key保存在 `api_keys.md` 文件中：
```
user123-abc123@2925.com,TavilyAuto123!,tvly-dev-xxxxxxxxxx,2025-01-01 12:00:00;
```

格式: `邮箱,密码,API_Key,时间`

<details>
<summary>故障排除</summary>

### 常见问题

**浏览器启动失败**
- 运行: `playwright install firefox`
- 检查网络连接

**邮箱登录问题**
- 重新运行: `python email_login_helper.py`
- 确保2925.com邮箱服务正常

**找不到验证邮件**
- 检查邮箱前缀设置是否正确
- 手动访问2925.com检查邮件

**API Key获取失败**
- 检查是否成功登录Tavily
- 查看生成的截图文件

**遇到人机验证**
- 如果IP纯净度或环境因素导致触发人机验证
- 选择前台模式 (浏览器模式选择1)
- 手动完成人机验证后程序会自动继续
- 建议使用干净的网络环境和IP地址

</details>

<details>
<summary>配置选项</summary>

### 浏览器配置
```python
HEADLESS = False          # 是否无头模式
BROWSER_TYPE = "firefox"  # 浏览器类型
```

### 等待时间配置
```python
WAIT_TIME_SHORT = 2       # 短等待时间
WAIT_TIME_MEDIUM = 5      # 中等等待时间
WAIT_TIME_LONG = 10       # 长等待时间
```

### 邮箱配置
```python
EMAIL_DOMAIN = "2925.com"
EMAIL_PREFIX = "user123"  # 您的邮箱前缀
```

</details>

## 技术栈

- **Python 3.7+**
- **Playwright**: 网页自动化
- **BeautifulSoup4**: HTML解析

## 免责声明

本工具仅用于学习和研究目的。使用时请遵守相关网站的服务条款。

## 许可证

MIT License
