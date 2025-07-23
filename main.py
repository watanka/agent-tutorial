from llm_engine import LLMEngine
from action import execute_command

llm_engine = LLMEngine()


def main():
    while True:
        cmd = input("명령을 내려주세요! 종료를 원하시면 exit을 입력해주세요.")
        response = llm_engine.generate_response(cmd)
        print("llm 응답: ", response)
        result = execute_command(response)
        print(result)
        if response == "exit":
            break


if __name__ == "__main__":
    main()
