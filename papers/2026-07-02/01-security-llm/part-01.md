# 🔐 大模型安全相关研究 | 2026年07月02日

> 本类共 **5** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Understanding and Evaluating Claw-like Agent Security Through a Computer-Systems Lens](https://arxiv.org/abs/2606.30755)

**<font color=#1a73e8>作者：</font>** Peizhi Niu, Wenjie Qu, Shangding Gu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Claw-like AI agents (e.g., OpenClaw) are always-on processes with persistent access to credentials, files, tools, and external services. They take on system-level responsibilities -- installing packages, maintaining state, scheduling subtasks, and mediating I/O -- making security failures far more severe than in other agents. Yet existing benchmarks focus on model responses and tool calls, leaving cross-component failure modes largely unmeasured. We adopt a computer-system analogy: treating a Claw-like agent as an agentic computer system whose gateway runtime plays an OS-like mediation role, whose Skills resemble user-installed applications, and whose Plugins resemble loadable extensions with runtime privileges. Each component has a classical counterpart whose protection mechanisms -- refined over decades of cybersecurity research -- are absent on the agent side. From this perspective, we develop SafeClawArena, a benchmark of 406 adversarial tasks across four attack surfaces (Skill Supply-Chain Integrity, Persistent State Exploitation, Cross-Boundary Data Flow, and Indirect Prompt Injection), executed in containerized replicas of real agent platforms with canary-marked credentials and evaluated via automated taint tracking across nine output channels. We evaluate three platforms (OpenClaw, NemoClaw, SeClaw) and five frontier LLMs. The highest attack success rate reaches 70%; malicious Plugins succeed in 100% of cases regardless of the LLM. SeClaw cuts GPT-5.4's attack success rate from 70% to 22%, partly through utility-security tradeoffs rather than active defenses, while Claude-Opus-4.6 already sits near a 22% floor on every platform. These results expose the inadequacy of current defenses and suggest directions for future hardening. Code and data: this https URL.

---


### 2. [Curvature-Guided Module Localization for Low-Rank Detoxification of Backdoored Large Language Models](https://arxiv.org/abs/2606.30899)

**<font color=#1a73e8>作者：</font>** Arash Raftari, Mehrdad Mahdavi, Nathan Blackthorn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks pose a serious threat to large language models (LLMs) by causing otherwise benign systems to produce attacker-specified malicious behavior when a hidden trigger is present. In this work, we study post hoc detoxification of backdoored LLMs in a practical setting where the defender has access to the poisoned model but does not wish to retrain the full network from scratch. We propose a mechanistically guided weight-space repair framework that first localizes modules involved in propagating trigger-induced behavior using activation patching and Fisher/K-FAC curvature analysis, and then applies targeted low-rank repair to only the most influential modules. We evaluate the method on poisoned variants of \texttt{Llama-3.2-1B-Instruct} with triggers inserted at the beginning, middle, and end of otherwise benign prompts. Results show that the proposed approach substantially suppresses trigger-conditioned malicious responses while preserving benign model behavior. These findings suggest that backdoor removal in LLMs can be formulated as a localized structural repair problem rather than only a broad behavioral alignment problem.

---


### 3. [CSO-LLM: Class Subspace Orthogonalization for Post-Training Backdoor Detection and Trigger Inversion in LLMs](https://arxiv.org/abs/2606.31309)

**<font color=#1a73e8>作者：</font>** Zhengxing Li, David J. Miller, Guangmingmei Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While post-training backdoor detection and trigger inversion schemes have been developed for AIs used e.g. for images, there is a paucity of such methods for LLMs. First, the LLM input space is discrete, with up to 150,000^k k-tuples to consider with k the token-length of a putative trigger. Second, one must blacklist tokens typical of the putative target response (class) of an attack, as such tokens may give false detection signals. However, a comprehensive blacklist is not available, in general, for a given domain. We develop a highly effective detection and inversion framework for LLMs treated as classifiers. Central to our approach is class subspace orthogonalization (CSO), a novel plug-and-play paradigm for backdoor detection that serves two fundamental roles when applied to LLMs: i) it enhances both sensitivity and specificity of a baseline detector; ii) it provides a form of implicit blacklisting, as it penalizes against inclusion, in a candidate trigger, of tokens that induce signal perturbations "in the direction of" the putative target class of an attack. One version of our detector performs continuous optimization in token embedding space, while a companion trigger-inversion and detection method performs greedy accretion in discrete token space. Our methods give both strong detection performance and accurate inversion of ground-truth triggers on several LLM classification domains, and for several different LLM architectures.

---


### 4. [EnclaveX: End-to-End Confidential AI with CPU/GPU TEEs](https://arxiv.org/abs/2606.31408)

**<font color=#1a73e8>作者：</font>** Robert Schambach, Quoc Do Le, Sergei Arnautov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have rapidly proliferated, driving widespread adoption of AI applications. Most deployments rely on centralized infrastructures such as Microsoft Azure, Google Cloud, or AWS, requiring users to share sensitive data and training or fine-tuning code. This dependence raises significant security and privacy concerns, as cloud providers must be trusted to ensure confidentiality and integrity.
Trusted Execution Environments (TEEs) e.g., Intel SGX/TDX, AMD SEV-SNP, and ARM CCA have been introduced to mitigate these risks. More recently, NVIDIA has developed GPU TEEs (e.g., H100/H200), yet comprehensive evaluations of end-to-end workflows that integrate CPU and GPU TEEs remain limited. Critical aspects, including performance overhead, remote attestation, and security guarantees for AI/LLM applications, have not been sufficiently studied.
This paper addresses this gap by presenting an end-to-end workflow that combines CPU and GPU TEEs. We propose mechanisms to ensure confidentiality and integrity at both the VM level (via Intel TDX and AMD SEV-SNP) and the application level, highlighting vulnerabilities such as Kubernetes administrators' ability to access confidential VM contents. Finally, we evaluate the performance overhead of our system using industry benchmarks, focusing on configurations that integrate Intel TDX with NVIDIA H200 GPUs.

---


### 5. [A Lifecycle and Application-Stack Survey of Large Language Model Vulnerabilities: Attacks, Risks, Defenses, and Open Problems](https://arxiv.org/abs/2606.31639)

**<font color=#1a73e8>作者：</font>** Seyed Bagher Hashemi Natanzi, Bo Tang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are no longer only text generators. They are increasingly embedded in retrieval pipelines, enterprise assistants, coding environments, robotic systems, security-operation workflows, and autonomous agents that can read private data, call tools, write files, execute code, and act across organizational boundaries. This shift changes the security problem: risks do not arise from the model weights alone, but from the full lifecycle and application stack through which data, prompts, model outputs, tools, memories, and user authority interact. This paper systematizes the literature on vulnerabilities in large language model systems through a lifecycle and application-stack lens. We organize attacks across eight stages: data collection, pretraining, post-training alignment, model packaging and supply chain, retrieval and memory, prompting and inference, tool/agent execution, and deployment/maintenance. For each stage, we analyze attacker capabilities, affected security objectives, representative attacks, practical risks, evaluation practices, and defenses. We further map LLM-specific vulnerabilities to confidentiality, integrity, availability, safety, privacy, fairness, accountability, and agency-control objectives. Unlike taxonomies that list isolated attack names, the proposed systematization emphasizes where trust boundaries fail, how untrusted data becomes executable instruction, how delegated authority amplifies model errors, and why point defenses rarely compose. We close with a research agenda for secure LLM systems, including compositional security, provenance-aware retrieval, tool-call containment, long-horizon agent evaluation, privacy-preserving adaptation, realistic red teaming, and deployment-grade incident response.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
