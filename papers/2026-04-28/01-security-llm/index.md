# 🔐 大模型安全相关研究 | 2026年04月28日

> 本类共 **5** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Sovereign Agentic Loops: Decoupling AI Reasoning from Execution in Real-World Systems](https://arxiv.org/abs/2604.22136)

**<font color=#1a73e8>作者：</font>** Jun He, Deying Yu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly issue API calls that mutate real systems, yet many current architectures pass stochastic model outputs directly to execution layers. We argue that this coupling creates a safety risk because model correctness, context awareness, and alignment cannot be assumed at execution time. We introduce Sovereign Agentic Loops (SAL), a control-plane architecture in which models emit structured intents with justifications, and the control plane validates those intents against true system state and policy before execution. SAL combines an obfuscation membrane, which limits model access to identity-sensitive state, with a cryptographically linked Evidence Chain for auditability and replay. We formalize SAL and show that, under the stated assumptions, it provides policy-bounded execution, identity isolation, and deterministic replay. In an OpenKedge prototype for cloud infrastructure, SAL blocks 93% of unsafe intents at the policy layer, rejects the remaining 7% via consistency checks, prevents unsafe executions in our benchmark, and adds 12.4 ms median latency.

---


### 2. [Behavioral Canaries: Auditing Private Retrieved Context Usage in RL Fine-Tuning](https://arxiv.org/abs/2604.22191)

**<font color=#1a73e8>作者：</font>** Chaoran Chen, Dayu Yuan, Peter Kairouz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In agentic workflows, LLMs frequently process retrieved contexts that are legally protected from further training. However, auditors currently lack a reliable way to verify if a provider has violated the terms of service by incorporating these data into post-training, especially through Reinforcement Learning (RL). While standard auditing relies on verbatim memorization and membership inference, these methods are ineffective for RL-trained models, as RL primarily influences a model's behavioral style rather than the retention of specific facts. To bridge this gap, we introduce Behavioral Canaries, a new auditing mechanism for RLFT pipelines. The framework instruments preference data by pairing document triggers with feedback that rewards a distinctive stylistic response, inducing a latent trigger-conditioned preference if such data are used in training. Empirical results show that these behavioral signals enable detection of unauthorized document-conditioned training, achieving a 67% detection rate at a 10% false-positive rate (AUROC = 0.756) at a 1% canary injection rate. More broadly, our results establish behavioral canaries as a new auditing mechanism for RLFT pipelines, enabling auditors to test for training-time influence even when such influence manifests as distributional behavioral change rather than memorization.

---


### 3. [Train in Vain: Functionality-Preserving Poisoning to Prevent Unauthorized Use of Code Datasets](https://arxiv.org/abs/2604.22291)

**<font color=#1a73e8>作者：</font>** Yuan Xiao, Jiaming Wang, Yuchen Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The widespread availability of large-scale code datasets has accelerated the development of code large language models (CodeLLMs), raising concerns about unauthorized dataset usage. Dataset poisoning offers a proactive defense by reducing the utility of such unauthorized training. However, existing poisoning methods often require full dataset poisoning and introduce transformations that break code compilability. In this paper, we introduce FunPoison, a functionality-preserving poisoning approach that injects short, compilable weak-use fragments into executed code paths. FunPoison leverages reusable statement-level templates with automatic repair and conservative safety checking to ensure side-effect freedom, while a type-aware synthesis module suppresses static analysis warnings and enhances stealth. Extensive experiments show that FunPoison achieves effective poisoning by contaminating only 10% of the dataset, while maintaining 100% compilability and functional correctness, and remains robust against various advanced code sanitization techniques.

---


### 4. [Automation-Exploit: A Multi-Agent LLM Framework for Adaptive Offensive Security with Digital Twin-Based Risk-Mitigated Exploitation](https://arxiv.org/abs/2604.22427)

**<font color=#1a73e8>作者：</font>** Biagio Andreucci, Arcangelo Castiglione  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The offensive security landscape is highly fragmented: enterprise platforms avoid memory-corruption vulnerabilities due to Denial of Service (DoS) risks, Automatic Exploit Generation (AEG) systems suffer from semantic blindness, and Large Language Model (LLM) agents face safety alignment filters and "Live Fire" execution hazards. We introduce Automation-Exploit, a fully autonomous Multi-Agent System (MAS) framework designed for adaptive offensive security in complex black-box scenarios. It bridges the abstraction gap between reconnaissance and exploitation by autonomously exfiltrating executables and contextual intelligence across multiple protocols, using this data to fuel both logical and binary attack chains. The framework introduces an adaptive safety architecture to mitigate DoS risks. While it natively resolves logical and web-based vulnerabilities, it employs a conditional isomorphic validation for high-risk memory-corruption flaws: if the target binary is successfully exfiltrated, it dynamically instantiates a cross-platform digital twin. By enforcing strict state synchronization, including libc alignment and runtime file descriptor hooking, potentially destructive payloads are iteratively debugged in an isolated replica. This enables a highly risk-mitigated "one-shot" execution on the physical target. Empirical evaluations across eight scenarios, including undocumented zero-day environments to rule out LLM data contamination, validate the framework's architectural resilience, demonstrating its ability to prevent "live fire" crashes and execute risk-mitigated compromises on actual targets.

---


### 5. [SSG: Logit-Balanced Vocabulary Partitioning for LLM Watermarking](https://arxiv.org/abs/2604.22438)

**<font color=#1a73e8>作者：</font>** Chenxi Gu, Xiaoning Du, John Grundy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking has emerged as a promising technique for tracing the authorship of content generated by large language models (LLMs). Among existing approaches, the KGW scheme is particularly attractive due to its versatility, efficiency, and effectiveness in natural language generation. However, KGW's effectiveness degrades significantly under low-entropy settings such as code generation and mathematical reasoning. A crucial step in the KGW method is random vocabulary partitioning, which enables adjustments to token selection based on specific preferences. Our study revealed that the next-token probability distribution plays an critical role in determining how much, or even whether, we can modify token selection and, consequently, the effectiveness of watermarking. We refer to this characteristic, associated with the probability distribution of each token prediction, as \emph{watermark strength.} In cases of random vocabulary partitioning, the lower bound of watermark strength is dictated by the next-token probability distribution. However, we found that, by redesigning the vocabulary partitioning algorithm, we can potentially raise this lower bound. In this paper, we propose SSG (\textbf{S}ort-then-\textbf{S}plit by \textbf{G}roups), a method that partitions the vocabulary into two logit-balanced subsets. This design lifts the lower bound of watermark strength for each token prediction, thereby improving watermark detectability. Experiments on code generation and mathematical reasoning datasets demonstrate the effectiveness of SSG.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
