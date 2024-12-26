from langchain_community.chat_models import __all__, _module_lookup

EXPECTED_ALL = [
    "AzureChatOpenAI",
    "BedrockChat",
    "ChatAnthropic",
    "ChatAnyscale",
    "ChatBaichuan",
    "ChatClovaX",
    "ChatCohere",
    "ChatCoze",
    "ChatDatabricks",
    "ChatDeepInfra",
    "ChatEverlyAI",
    "ChatEdenAI",
    "ChatFireworks",
    "ChatFriendli",
    "ChatGooglePalm",
    "ChatHuggingFace",
    "ChatHunyuan",
    "ChatJavelinAIGateway",
    "ChatKinetica",
    "ChatKonko",
    "ChatLiteLLM",
    "ChatLiteLLMRouter",
    "ChatLlamaCpp",
    "ChatMLflowAIGateway",
    "ChatMaritalk",
    "ChatMlflow",
    "ChatMLflowAIGateway",
    "ChatMLX",
    "ChatNebula",
    "ChatOCIGenAI",
    "ChatOCIModelDeployment",
    "ChatOCIModelDeploymentVLLM",
    "ChatOCIModelDeploymentTGI",
    "ChatOllama",
    "ChatOpenAI",
    "ChatOutlines",
    "ChatPerplexity",
    "ChatPremAI",
    "ChatSambaNovaCloud",
    "ChatSambaStudio",
    "ChatSparkLLM",
    "ChatTongyi",
    "ChatVertexAI",
    "ChatYandexGPT",
    "ChatYuan2",
    "ChatReka",
    "ChatZhipuAI",
    "ErnieBotChat",
    "FakeListChatModel",
    "GPTRouter",
    "GigaChat",
    "HumanInputChatModel",
    "JinaChat",
    "LlamaEdgeChatService",
    "MiniMaxChat",
    "MoonshotChat",
    "ModelScopeChatEndpoint",
    "PaiEasChatEndpoint",
    "PromptLayerChatOpenAI",
    "SolarChat",
    "QianfanChatEndpoint",
    "VolcEngineMaasChat",
    "ChatOctoAI",
    "ChatSnowflakeCortex",
    "ChatYi",
]


def test_all_imports() -> None:
    assert set(__all__) == set(EXPECTED_ALL)
    assert set(__all__) == set(_module_lookup.keys())
