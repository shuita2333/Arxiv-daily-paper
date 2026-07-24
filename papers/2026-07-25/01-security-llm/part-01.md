# 🔐 大模型安全相关研究 | 2026年07月25日

> 本类共 **6** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Deepfake News Detection: A Multimodal Framework Integrating LipNet, DeepSpeech and ResNET for Enhanced Audio-Visual Analysis](https://arxiv.org/abs/2607.20579)

**<font color=#1a73e8>作者：</font>** Ameena Khan, Muhammad Ahsan Aziz, Muhammad Junaid Asif 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deepfake news refers to AI-generated (or AI ma-nipulated) multimedia content intentionally generated to deceive audiences by manipulating the facial expressions, or speech while maintaining the realistic appearance. The rapid progress of generative AI has made the synthesis of highly realistic fake videos and cloned voices widely accessible, posing a serious threat to the authenticity of digital news media. This paper presents a multi-modal framework that discerns the authenticity of video content by jointly exploiting audio and visual cues, thereby addressing the challenge of detecting the deepfake videos. We proposed a framework that involves features extraction from lip movements, audio content and video frames. Lip movements and speech content are encoded using the LipNet and DeepSpeech2 models, while facial features are extracted by leveraging the use of BlazeFace and represented with ResNet18. The extracted feature vectors are concatenated into a holistic video representation and classified with an ensemble of machine learning and deep learning models, including Random Forest (RF), Multi-layer Perceptron (MLP) and Long Short-Term Memory (LSTM) networks. Exten-sive experiments performed on the FakeAVCeleb dataset shows that the proposed approach attains an accuracy of 94% using augmented audio features, outperforming a state-of-the-art multi-modal ensemble baseline. The results confirm the robustness and practical potential of the proposed framework for deepfake news detection.

---


### 2. [Evaluating Large Language Models for Symbolic Security Protocol Analysis](https://arxiv.org/abs/2607.20712)

**<font color=#1a73e8>作者：</font>** Paolo Modesti, Syed Ahmed, Ioannis Sfyrakis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security protocol verification relies on formal tools such as ProVerif and OFMC. This study evaluates whether Large Language Models (LLMs) can perform comparable analysis. We test GPT and DeepSeek in chat and reasoning modes over three runs on 130 obfuscated AnB/AnBx protocols covering 388 security goals, scored against ProVerif and OFMC. Chat models reach 69 to 81% recall at precision below 31%. Reasoning models reverse this trade-off, reaching 66.5% precision for GPT and 45.4% for DeepSeek, but detect just over half the attacks. DeepSeek's two modes share one underlying model, so the comparison isolates reasoning itself, which raises precision from 27.2% to 45.4%. The GPT contrast spans a model-version change and is only suggestive. All models perform worst on authentication goals: reasoning models detect well under half of injective and non-injective agreement attacks, whereas chat models over-flag them at low precision. Confidentiality is the exception, with F1 up to 95.7% in reasoning mode. Verdicts are unstable across runs, identical on 89.7% of goals for GPT but 74.0% for DeepSeek. Self-reported confidence is uniformly high yet shows no meaningful correlation with correctness. On this benchmark LLMs do not match formal verification, but may serve, at best, as pre-screening filters.

---


### 3. [Security Vulnerability Patterns in AI-Generated Code: A Cross-Model Comparative Study](https://arxiv.org/abs/2607.20713)

**<font color=#1a73e8>作者：</font>** Shanna M. Kahn, John D. Hastings  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based coding tools enable non-expert users to generate routine automation scripts that may enter enterprise workflows without meaningful security review. This study examines that risk directly. Code was collected from ChatGPT, Microsoft Copilot, and Google Gemini using identical prompts across three automation domains. Claude Code performed a standardized vulnerability review. Each identified vulnerability was scored using CVSS v3.1 and mapped to the OWASP Top 10:2021 and the MITRE ATT&CK frameworks. Every script contained exploitable vulnerabilities. Nine of the 17 identified vulnerability classes appeared in code from all three models, while 14 of the 17 vulnerability classes appeared in at least two models. The weighted CVSS scores across platforms differed by less than 10%. The risk is not tied to any particular model but rather to the task category. Organizations should therefore ask not which tool to trust, but instead whether LLM-generated automation code should be deployed without review.

---


### 4. [Leaky Language Models: Stealing Architecture and Inference Optimizations via Per-Token Timing](https://arxiv.org/abs/2607.20723)

**<font color=#1a73e8>作者：</font>** Sadegh Majidi, Niloofar Mireshghallah, Kazem Taram  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This work presents LeakyLMs, a set of attacks that leak proprietary model, architecture, and deployment information from production language models. LeakyLMs is the first to demonstrate that key model and deployment details can be inferred using only token generation timing, even when interacting through remote APIs. LeakyLMs introduces two core attacks. The first attack targets inference optimizations and deployment strategies. For example, our attack detects whether a provider uses speculative decoding, a widely deployed inference-time optimization, and further identifies the context length of the draft model used in the pipeline. Our measurements show that Google Gemini Flash 2.5 uses speculative decoding with a draft context window of approximately 128K tokens. The second attack recovers key architectural properties, including the number of transformer layers, hidden dimension size, and number of attention heads. To achieve this, LeakyLMs builds a detailed and accurate model of token-generation timing on modern NVIDIA GPUs, characterizing how latency scales with model configuration and hardware parameters. The attack then performs a search over the architecture space using this timing model. In experiments with Llama models, the near-correct architectural configuration appears in the top-10 guesses more than 90% of the time.

---


### 5. [IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests](https://arxiv.org/abs/2607.20759)

**<font color=#1a73e8>作者：</font>** Ankur Singh, Jinqiu Yang, Tse-Hsun Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI coding agents powered by LLMs are increasingly integrated into real-world software development, where they generate, edit, and execute code with autonomous access to local files and tools. Coding agents inherit security risks from both the LLM backbone, where adversarial prompts, poisoned training data, and backdoor triggers can cause models to emit insecure or attacker-chosen code, and their agentic architecture, where tool-using autonomy enables induced misuse of external APIs, data exfiltration, and persistent compromise of development environments. This paper presents a systematic evaluation of malicious issue requests against state-of-the-art coding agents (Cursor, Claude Code, and Codex Desktop), powered by two major model families (OpenAI GPT-5.3 Codex/GPT-5.4 and Anthropic Sonnet 4.6). Our novel benchmark IssueTrojanBench contains malicious issues that are constructed based on four novel attack categories (i.e., embedded as malicious instructions in issues), six delivery vectors (e.g., PDF, or issue comment), and further augmented by perturbations. Our results reveal critical vulnerabilities in the as-deployed modern coding agents, i.e., 66.5% of the malicious issues from IssueTrojanBench penetrate all the guardrails (agent- and LLM-level) of coding agents. Our further analysis shows that rejection is almost entirely from LLMs rather than the agent frameworks, with GPT models broadly vulnerable and Sonnet 4.6 exhibiting more selective, risk-aware blocking of high-impact actions. Our evaluation also highlights that the current agent-level defense strategy offers limited additional protection for coding agents. Our findings highlight the urgent need for stronger agent- and model-level safety mechanisms to protect AI coding agents.

---


### 6. [Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways](https://arxiv.org/abs/2607.20860)

**<font color=#1a73e8>作者：</font>** Yuewei Zhang, Zhi-Hai Zhang, Hanzhang Qin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Commercial LLM gateways mediate access to hosted models, but the served backend may not match the advertised one: it may substitute a cheaper model on every request or route only a fraction $\epsilon$ of requests to it. Prior black-box auditors often need a privileged signal (log-probabilities, token ranks, or reference samples) or a target-specific probe, fix the query budget in advance, and return a yes/no verdict. We present $\mathrm{IRIS}$, an audit that needs only the returned text: it asks endpoints to generate random numbers or strings, fingerprints the backend, and is the first to combine, in one text-only audit, detection of whole-stream substitution and fractional dilution, attribution of the served backend, routing-fraction ($\epsilon$) estimation, and a query budget it sizes itself. A cheap pilot fits the exponential query-error decay and freezes that budget before any suspect query is issued. On an intra-family Qwen3 ladder $\mathrm{IRIS}$ verifies the backend at $0.99$ AUROC and sharpens attribution as queries accumulate; across a commercial OpenRouter library it catches $\epsilon{=}0.3$ dilution on margin-qualified pairs at $0.85$ mean power ($0.017$ false-positive rate) and recovers $\epsilon$ to within $0.04$ for enrolled diluents; and a live cross-provider audit flags $14$ of $15$ same-model provider pairs by genuine quantization and kernel deviations, corroborated on third-party MET traces. Against comparable black-box auditors, $\mathrm{IRIS}$ matches or beats detection on shared tasks, and adaptive allocation lifts the matched-budget target-hit rate from $73$% to $87$%. Further experiments cover adversarial gateways, knob identifiability, unseen diluents, and false-positive control.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
