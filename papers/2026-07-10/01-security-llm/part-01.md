# 🔐 大模型安全相关研究 | 2026年07月10日

> 本类共 **8** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents](https://arxiv.org/abs/2607.06595)

**<font color=#1a73e8>作者：</font>** George Torres, Sharad Shrestha, Satyajayant Misra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Personal AI agents powered by large language models can reason and act using available tools to access emails, manage calendars, and push code to remote repositories, all with minimal oversight. When augmented with long-term memory, an agent can recall specific details relevant to the current task, reducing the need for large context windows. Currently, long-term memory agents tend to fall into two distinct domains: conversational and action-planning agents. Personal assistant agents sit at the convergence of these two domains and handle sensitive information while interacting with untrusted information sources, creating previously unaccounted security vulnerabilities. In this work, we introduce the novel attack vector, GhostWriter, which exploits current memory subsystems in tool-using personal agents to poison their memory store. GhostWriter operates in two phases: injection, where an adversary sends a hidden attack payload to the target agent; and activation, in which the poisoned memory is retrieved. We show that GhostWriter achieves near-universal injection rates of approximately 98% and a high average activation rate of approximately 60% against state-of-the-art agents. This attack is possible due to the lack of security-focused memory governance. In response, we propose Agentic Memory Sentry (AM-Sentry), which leverages two mitigation techniques: a memory-saving policy and a memory-retrieval screen. Our experiments show that AM-Sentry dramatically reduces GhostWriter's success rate while preserving agent utility.

---


### 2. [Security and Privacy in Agentic AI: Grand Challenges and Future Directions](https://arxiv.org/abs/2607.06608)

**<font color=#1a73e8>作者：</font>** Adam Jenkins, Agnieszka Kitkowska, Caterina Maidhof 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present key challenges and future research directions in the security and privacy of agentic AI, based on a horizon-scanning exercise that brought together thirty leading international experts from academia, industry, and government to engage in focused discussions and collaborative exercises on the emerging risks associated with the growing agency of AI.

---


### 3. [POPS: Recovering Unlearned Multi-Modality Knowledge in MLLMs with Prompt-Optimized Parameter Shaking](https://arxiv.org/abs/2607.06649)

**<font color=#1a73e8>作者：</font>** Zhangheng LI, Jianing Zhu, Junyuan Hong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated impressive performance on cross-modal tasks by jointly training on large-scale textual and visual data, where privacy-sensitive examples could be unintentionally encoded, raising concerns about privacy or copyright violation. To this end, Multi-modality Machine Unlearning (MMU) was proposed as a mitigation that can effectively force MLLMs to forget private information. However, the robustness of such unlearning methods is not fully exploited when the model is published and accessible to malicious users. In this paper, we propose a novel adversarial strategy, namely Prompt-Optimized Parameter Shaking (POPS), aiming to recover the supposedly unlearned multi-modality knowledge from the MLLMs. Our method elicits the victim MLLMs to generate potential private examples via prompt-suffix optimization, and then exploits these synthesized outputs to fine-tune the models so they disclose the true private information. The experiments on the different MMU benchmarks reveal substantial weaknesses in the existing MMU algorithms. Our POPS can even achieve a near-complete recovery of supposedly erased sensitive information on the unlearned MLLMs, exposing fundamental vulnerabilities that challenge the foundational robustness of representative MMU-based privacy protections.

---


### 4. [Behavioral Privacy Leakage in Agentic Negotiation: Formalizing and Mitigating Inference Attacks via Randomized Policies](https://arxiv.org/abs/2607.06815)

**<font color=#1a73e8>作者：</font>** Barkha Rani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous negotiation agents are increasingly deployed in high-stakes settings such as insurance and procurement. While cryptographic techniques protect explicitly disclosed constraint values, they fail to address a subtler threat: behavioral privacy leakage, where an adversary infers private constraints from observable negotiation dynamics such as concession trajectories, timing, and convergence patterns. This paper investigates behavioral differential privacy in multi-round negotiation protocols. We design an adaptive stochastic negotiation policy that jointly guarantees $(\varepsilon, \delta)$-differential privacy, almost-sure convergence of the offer sequence (reaching agreement when the counterparty's reservation value permits), and high negotiation utility. Evaluated on 3,000 synthetic bilateral negotiations, our mechanism reduces adversarial inference accuracy by 43-50% while maintaining a negotiation success rate and utility above 90%, demonstrating that strong privacy guarantees can be achieved without significant loss of performance.

---


### 5. [Large Language Models (LLMs) and Generative AI in Cybersecurity and Privacy: A Survey of Dual-Use Risks, AI-Generated Malware, Explainability, and Defensive Strategies](https://arxiv.org/abs/2607.06963)

**<font color=#1a73e8>作者：</font>** Kiarash Ahi, Saeed Valizadeh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) and generative AI (GenAI) systems, such as ChatGPT, Claude, Gemini, LLaMA, Copilot, Stable Diffusion by OpenAI, Anthropic, Google, Meta, Microsoft, Stability AI, respectively, are revolutionizing cybersecurity, enabling both automated defense and sophisticated attacks. These technologies power real-time threat detection, phishing defense, secure code generation, and vulnerability exploitation at unprecedented scales. Following a rapid surge where LLM-generated malware grew to account for an estimated 50% of detected threats by 2025, up from just 2% in 2021, navigating this highly automated threat landscape in 2026 demands next-generation security frameworks. This paper presents a comprehensive survey of the beneficial and malicious applications of LLMs in cybersecurity, including zero-day detection, DevSecOps, federated learning, synthetic content analysis, and explainable AI (XAI). Drawing on a review of over 70 academic papers, industry reports, and technical documents, this work synthesizes insights from real-world case studies across platforms like Google Play Protect, Microsoft Defender, Amazon Web Services (AWS), Apple App Store, OpenAI Plugin Stores, Hugging Face Spaces, and GitHub, alongside emerging initiatives like the SAFE Framework and AI-driven anomaly detection. We conclude with practical recommendations for responsible and transparent LLM deployment and trustworthy AI, including model watermarking, adversarial defense, and cross-industry collaboration, setting a new benchmark for rigorous, holistic cybersecurity research at the intersection of AI and threat defense, and offering a roadmap for secure, scalable LLM systems that serves as a critical reference for researchers, engineers, and security leaders navigating the complex challenges of AI-driven cybersecurity.

---


### 6. [Thinking More, Harnessing Better: State Machine Guided Harness Automatic Generation with Project Digestion and Workflow Decomposition](https://arxiv.org/abs/2607.07007)

**<font color=#1a73e8>作者：</font>** Xing Zhang, Zikang Huang, Gang Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> High-quality fuzz harnesses are essential for effective gray-box fuzzing. While Large Language Models (LLMs) offer promise for automating this task, existing one-turn generation methods suffer from hallucinations and inadequate coverage due to coarse-grained function targeting and misaligned generation workflows. We present SynapseFlow, an automatic harness generator that addresses these limitations through two key innovations: dataflow-aware function aggregation and a staged, rollback-enabled generation workflow decomposition. SynapseFlow first analyzes source code to construct Structural Flow Graphs and extract coherent Function Triplets. It then synthesizes harnesses via a decomposed four-stage process governed by a staged rollback algorithm to ensure correctness. We evaluated SynapseFlow on 25 real-world open-source software projects. The experimental results indicate that SynapseFlow outperforms state-of-the-art tools (OSS-Fuzz-Gen, CKGFuzzer, PromeFuzz), achieving 3.07$\times$, 1.71$\times$, and 4.26$\times$ higher branch coverage, and 1.77$\times$, 1.51$\times$, and 1.36$\times$ higher bug detection rates, respectively. Most importantly, SynapseFlow discovered 7 previously unreported bugs (5 assigned CVEs), demonstrating its practical effectiveness in real-world bug discovery.

---


### 7. [Beware of Agentic Botnets: Scalable Untargeted Promptware Attacks via Universal and Transferable Adversarial HalluSquatting](https://arxiv.org/abs/2607.07433)

**<font color=#1a73e8>作者：</font>** Aya Spira, Stav Cohen, Elad Feldman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growing adoption of agentic LLM applications has introduced a new threat previously named as promptware. While prior work has established that adversaries can exploit direct channels to LLM applications to apply promptware under weak threat models, many applications do not provide any direct channels that could be exploited for prompt injection beyond the Internet. This raises a question: can attackers exploit LLM applications at scale without any direct channels in practical threat models? In this work, we show that the inherent tendency of LLMs to hallucinate resource identifiers can be exploited to amplify untargeted promptware attacks that pull adversarial prompts at scale and could be exploited to establish a botnet. We introduce adversarial hallucination squatting, a technique in which attackers identify trending resources (e.g., popular repositories, popular skills, etc.), compute the LLM distribution of hallucinations on the trending resource names, and preemptively register them to host adversarial prompts. By leveraging the predictability and transferability of hallucinations across foundational LLMs and to application layers, adversaries can significantly amplify the reach of untargeted promptware under weak threat models and establish a botnet by exploiting LLM applications to install a bot on the device that pulled the compromised hallucinated resource from the Inter. We empirically demonstrate that hallucinated resource generation occurs at high rates, up to 85% in repository cloning scenarios and up to 100% in skill installation, and that these hallucinations transfer between foundational models and different prompts. We demonstrate the practicality of adversarial hallucination squatting against various production LLM applications with integrated terminals in their set of tools, achieving remote tool execution and remote code execution.

---


### 8. [Mitigating Taint-Style Vulnerabilities in MCP Servers via Security-Aware Tool Descriptions](https://arxiv.org/abs/2607.07461)

**<font color=#1a73e8>作者：</font>** Yang Shi, Jiaheng Fu, Yihe Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as autonomous agents that interact with external tools and services via the Model Context Protocol (MCP), a standardized interface for dynamic tool invocation. While MCP simplifies integration, it also expands the attack surface and enables generic exploits across multiple servers. Despite prior work on malicious MCP servers, the vulnerability landscape of MCP servers remains underexplored. In this work, we systematically analyze MCP server vulnerabilities, focusing on metadata characteristics, vulnerable code patterns, and community responses. Our study reveals that taint-style vulnerabilities constitute a substantial fraction of MCP server vulnerabilities, require significant code modifications to remediate, and are met with slow community responses. Motivated by these findings, we propose SPELLSMITH, presenting a novel textbased avenue for shielding taint-style vulnerabilities in MCP servers. In particular, SPELLSMITH analyzes the high-risk capabilities exposed by an MCP server and combines them with tool descriptions and parameter semantics to identify potential taint-style vulnerability risks, thereby constructing a tool-level risk profile. Then, SPELLSMITH leverages the Description property of the protocol to embed behavioral guidance (Description Enhancement Module) and exploits LLMs' self-reflection capabilities (Self-Reflection Module) to iteratively evaluate and refine outputs. By strengthening LLM internal decision-making, SPELLSMITH provides an active and unified mitigation strategy that generalizes across multiple vulnerabilities, reducing reliance on context-specific code-level fixes. Our experiments demonstrate that SPELLSMITH effectively mitigates taint-style vulnerability exploitation in MCP servers, highlighting its practical applicability and advantages over traditional code-level mitigations.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
