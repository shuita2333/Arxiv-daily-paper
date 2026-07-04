# 🔐 大模型安全相关研究 | 2026年07月05日

> 本类共 **5** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Cognitive Firewall: A Proactive, Zero-Trust, Multi-Gate Framework for LLM Safety](https://arxiv.org/abs/2607.01277)

**<font color=#1a73e8>作者：</font>** Michele Guida, Ruslan Shikhhamzayev, Sindhuja Penchala 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can be induced to produce harmful content through multi turn strategies in which no single user message appears clearly unsafe. Existing runtime safeguards commonly evaluate prompts or responses as isolated messages, which limits their ability to recover ac-cumulated intent, verify asserted authority, or detect harmful objectives decomposed across a dialogue. This paper presents the Cognitive Firewall, a proactive runtime oversight framework that interposes an independent oversight model between a user and a protected target mod l. The framework decomposes safety assessment into four categorical gates: an intent gate that identi-fies the operational objective of a request, a zero trust context gate that treats claimed roles and permissions as unverified evidence, a consistency gate that detects escalation and decomposition across turns, and an output risk gate that inspects candidate responses before release. Gate decisions are combined through escalation rather than score averaging, allowing any confident danger signal to block an interaction while preserving an auditable rationale. Experiments on four jailbreak benchmarks and a benign safety test set show that the Cognitive Firewall substantially reduces attack success across single turn, multi turn, authority based, and human crafted attacks. It lowers attack success to 2 percent or below on three attack sets and to 14 percent on the most difficult human crafted set, while maintaining an 8 percent over refusal rate. These results indicate that decomposed, conversation level oversight can improve proactive containment and auditability for LLM safety.

---


### 2. [From Forgeries to Foundation Models: A Systematic Survey of Identity Document Attack and Detection](https://arxiv.org/abs/2607.01442)

**<font color=#1a73e8>作者：</font>** Gourab Das, Pavan Kumar C, Raghavendra Ramachandra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Identity document forgery has undergone a fundamental capability shift: generative AI tools now enable high-fidelity document synthesis and field-level manipulation with minimal technical expertise, while detection methods remain constrained by benchmarks that do not reflect this threat. The resulting attack surface spans physical presentation, digital injection, and fully generative synthesis, introducing distinct forensic failure modes that require a unified threat model and evaluation framework. This survey provides, to our knowledge, the first unified treatment of Presentation Attacks, Digital Injection Attacks, and GenAI-driven synthesis within a single identity verification threat model. We trace detection methodologies from rule-based heuristics through forensic localisation, injection-aware pipelines, foundation models, and few-shot frameworks. A systematic audit of public datasets from 2019--2025 exposes a persistent Reality Gap between benchmark conditions and operational deployment. We further analyse large multimodal models for identity document manipulation, identifying Script-Dependent Generative Instability (SDGI) as a recurring typographic failure mode in non-Latin script inpainting. Finally, zero-shot benchmarking on unseen synthesised ID cards shows that even the strongest publicly available models achieve APCER values above 25% under security-oriented operating conditions, highlighting substantial limits in cross-domain generalisation. We conclude by outlining future directions toward forensically grounded, privacy-preserving, and legally accountable identity verification systems.

---


### 3. [Overthink-Triggered Slowdown Attacks on LVLM-Based Robotic Systems](https://arxiv.org/abs/2607.01518)

**<font color=#1a73e8>作者：</font>** Qiang Han, Jie Wu, Bo Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have been increasingly integrated into robotic systems. However, these models may exhibit overthinking behaviors, where they generate excessively long reasoning traces, incurring an excessive inference time. This overthinking behavior poses a serious risk to robotic systems, as the adversary can deliberately trigger overthinking to slow down the decision making of a victim robotic system, causing a variety of safety issues (i.e., an overthinking-induced slowdown attack). To initiate this attack, an adversary can embed carefully crafted, human-readable scene text into the visual scene observed by a victim robotic agent, causing significant inference delays even under a strict black-box setting. Therefore, the embedded scene text serves as a significant "trigger" for the attack.
This work systematically identifies and validates transferable triggers of overthinking in robotic systems by introducing a three-stage framework. First, we construct a diverse corpus of reasoning-intensive scene text and extract overthinking-correlated lexical features from short response prefixes. Second, we perform an efficient black-box search guided by a prefix-based proxy score while selectively confirming a small set of top candidates with full latency measurements. Third, we evaluate black-box transfer using a fixed pool of triggers on unseen images and multiple LVLMs, reporting latency amplification and attack success rates under standard thresholds. Across three representative LVLMs, all triggers yield slowdown ratios greater than 1.0x, with the strongest single-trigger case reaching 6.96x. The physical printing of the text trigger still causes up to 4.74x latency amplification. These results demonstrate that our discovered triggers are transferred between multiple LVLM models and consistently cause significant slowdowns in robotic systems.

---


### 4. [VeriChat: An Agentic Conversational AI Assistant for Hardware Security Verification](https://arxiv.org/abs/2607.01668)

**<font color=#1a73e8>作者：</font>** Dipayan Saha, Khan Thamid Hasan, Shams Tarek 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware security verification is a multi-stage process in which engineers must navigate complex design analyses, threat considerations, and verification strategies. They often need security-focused guidance, yet current verification environments provide little structured support for such assistance. Although conversational AI could offer such on-demand assistance, directly using general-purpose chatbots like ChatGPT or Gemini is risky due to their tendency to hallucinate and their reliance on static, outdated knowledge. We present VeriChat, a domain-specialized conversational assistant designed to support, rather than replace, existing verification workflows by providing context-aware security guidance. VeriChat employs a retrieval-augmented, multi-agent workflow in which three specialized agents collaboratively minimize hallucinations while improving the transparency and reliability of the response. Beyond question answering, VeriChat integrates open-source EDA tools, including Icarus Verilog, Yosys, and SymbiYosys, to perform syntax checking, synthesis analysis, simulation, and formal verification directly on user-provided RTL designs. Evaluated using a comprehensive methodology, VeriChat achieves a Faithfulness score of 87.73%, significantly outperforming the leading proprietary models. We demonstrate the framework through a hardware Trojan detection case study on an AES S-Box IP, where VeriChat autonomously identifies, simulates, and formally proves a covert key-leakage vulnerability through a multi-turn conversational workflow.

---


### 5. [Behind the Refusal: Determining Guardrail Activation via Behavioral Monitoring](https://arxiv.org/abs/2607.02121)

**<font color=#1a73e8>作者：</font>** William Hackett, Peter Garraghan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) and agentic systems become integrated into real-world applications, ensuring their safety and security is critical. Guardrail systems that detect and block malicious instructions sent to and from an LLM are an essential component of AI security. However, researchers conducting black-box adversarial emulation against production AI systems often struggle to determine whether a guardrail block or an LLM rejection has occurred. This distinction is important because the techniques used to bypass guardrails can differ substantially from those used to bypass LLM safety alignment, and has a material impact on attack technique selection and optimization. We propose the first black-box guardrail reconnaissance methodology, which detects the presence of a guardrail within a target AI system through behavioral monitoring of HTTP, lexical, and timing signals, assuming only black-box access and zero prior knowledge of the guardrail or AI system. Experiments demonstrate that our approach detects guardrail presence with 100% accuracy, with statistically significant behavioral separation between benign and malicious interactions (q < 0.001). Our approach further identifies the content categories a guardrail is designed to block, and distinguishes guardrail blocks from LLM rejection on unseen prompts with an average F1 score of 98%.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
