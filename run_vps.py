#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tavily 自动注册程序 - VPS 专用非交互式版本
"""
import argparse
import os
import time
from intelligent_tavily_automation import IntelligentTavilyAutomation
from main import TavilyMainController

def run_on_vps(email_prefix, count, headless=True):
    """
    在 VPS 上执行非交互式注册。

    :param email_prefix: 邮箱前缀
    :param count: 注册数量
    :param headless: 是否使用无头模式
    """
    print("🚀 Tavily 自动注册程序 (VPS 版本)")
    print("=" * 60)
    print(f"📧 邮箱前缀: {email_prefix}")
    print(f"📊 注册数量: {count}")
    print(f"🖥️  浏览器模式: {'后台 (headless)' if headless else '前台'}")
    print("=" * 60)

    success_count = 0
    for i in range(count):
        print(f"\n{'='*60}")
        print(f"🔄 正在注册第 {i+1}/{count} 个账户...")
        print(f"{'='*60}")

        try:
            automation = IntelligentTavilyAutomation()
            automation.email_prefix = email_prefix
            automation.start_browser(headless=headless)

            start_time = time.time()
            api_key = automation.run_complete_automation()
            elapsed_time = time.time() - start_time

            if api_key:
                print(f"🎉 注册成功! (耗时: {elapsed_time:.1f} 秒)")
                print(f"   - 邮箱: {automation.email}")
                print(f"   - API Key: {api_key}")
                success_count += 1
            else:
                print(f"❌ 第 {i+1} 个账户注册失败。")

        except Exception as e:
            print(f"❌ 注册过程中发生严重错误: {e}")
        finally:
            try:
                # 确保浏览器实例被关闭
                if 'automation' in locals() and automation.browser:
                    automation.close_browser()
            except Exception as close_error:
                print(f"⚠️ 关闭浏览器时出错: {close_error}")

    print(f"\n{'='*60}")
    print("🎉 注册任务全部完成!")
    print(f"📊 成功: {success_count}/{count} (成功率: {success_count/count*100:.1f}%)")
    print("🔑 API Keys 已保存在 api_keys.md 文件中。")
    print(f"{'='*60}")

def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="Tavily 自动注册程序 - VPS 专用非交互式版本。",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # 添加命令行参数
    parser.add_argument(
        '-c', '--count', 
        type=int, 
        default=1,
        help="要注册的账户数量 (默认: 1)"
    )
    
    # 添加一个子命令来生成 cookie
    subparsers = parser.add_subparsers(dest='command', required=True, help='可用的命令')
    
    run_parser = subparsers.add_parser('run', help='在 VPS 上运行注册任务。需要 email_cookies.json 文件。')
    run_parser.add_argument(
        '-c', '--count', 
        type=int, 
        default=1,
        help="要注册的账户数量 (默认: 1)"
    )

    cookie_parser = subparsers.add_parser('setup-cookie', help='在本地生成 email_cookies.json 文件。')

    args = parser.parse_args()

    controller = TavilyMainController()

    if args.command == 'setup-cookie':
        print("🍪 启动邮箱 Cookie 获取流程...")
        print("请在弹出的浏览器中登录您的邮箱。成功登录后，关闭此程序即可。")
        controller.setup_email_cookies()
        if os.path.exists(controller.cookie_file):
            print(f"✅ {controller.cookie_file} 文件已生成。请将其上传到您的 VPS。")
        else:
            print(f"❌ 未能生成 {controller.cookie_file}。请重试。")
        return

    if args.command == 'run':
        # 检查 email_cookies.json 是否存在
        if not os.path.exists(controller.cookie_file):
            print(f"❌ 错误: {controller.cookie_file} 文件未找到!")
            print("请先在本地运行 'python run_vps.py setup-cookie' 命令生成 cookie 文件，然后上传到当前目录。")
            return
            
        # 从 cookie 获取邮箱前缀
        email_prefix = controller.get_email_prefix_from_cookies()
        if not email_prefix:
            print("❌ 无法从 cookie 文件中获取邮箱前缀。")
            print("请确保 cookie 文件有效或重新生成。")
            return
            
        run_on_vps(email_prefix, args.count, headless=True)

if __name__ == "__main__":
    main()