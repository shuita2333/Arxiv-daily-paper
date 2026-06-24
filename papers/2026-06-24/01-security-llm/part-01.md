# 🔐 大模型安全相关研究 | 2026年06月24日

> 本类共 **4** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [CORE-BREW: LLR-Based Soft Decoding for Robust Multi-Bit LLM Watermarking](https://arxiv.org/abs/2606.24163)

**<font color=#1a73e8>作者：</font>** Joeun Kim, HoEun Kim, Young-Sik Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reliable provenance for LLM outputs requires multi-bit watermarks that remain robust under editing while maintaining strict false-positive control. Existing ECC-based LLM watermarks rely largely on hard-decision decoding, discarding token-level reliability information. We propose CORE-BREW, a Constant-hit-Rate Embedding extension of block-wise BREW for robust multi-bit watermarking. CORE-BREW calibrates the watermark channel by targeting a fixed hit rate p-star, yielding closed-form per-token log-likelihood ratios (LLRs) for principled soft-decision decoding. It supports two detection modes: Strict-Safe, which preserves the bounded-distance designated-codeword acceptance region, and FPR-Calibrated, which uses likelihood-based scoring and lightweight list decoding to characterize the FPR-TPR trade-off. Experiments on open-source LLMs under token-level edits and paraphrasing demonstrate improved low-FPR discrimination and robustness over prior multi-bit watermarking baselines while maintaining comparable semantic quality.

---


### 2. [Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees](https://arxiv.org/abs/2606.24322)

**<font color=#1a73e8>作者：</font>** Yedidel Louck  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on persistent long-term memory, which creates a critical vulnerability that we study here: memory poisoning. An adversary can store untrusted content in one session that later steers a consequential action, such as a payment, a setting change, or data exfiltration, in a future session. Existing defenses base a memory item's authority to act on either its content (detection or trust-scoring) or its derivation history (lineage). We show that both signals are malleable. An attacker can launder an untrusted origin through three channels specific to LLM agents: the agent's own summarization, a trusted-tool echo, and manufactured corroboration. Each makes the content look benign and breaks or flips its derivation edge to ``trusted.'' We formalize malleability for the memory write-retrieve-act pipeline and prove a machine-checked separation theorem. No content- or lineage-based defense is sound under laundering (T1), write-time origin binding is necessary (T2), and non-malleable origin-bound authority with Sybil-resistant corroboration-gated elevation is sufficient (T3). Our construction, TMA-NM (Tamper-evident Memory Authority, Non-Malleable), instantiates non-malleable information-flow control (IFC) for LLM-agent memory. A cross-defense, cross-attack, and cross-model benchmark over eight frontier models shows that existing defenses fail exactly where the theory predicts (up to 68% laundering attack-success), while TMA-NM reaches 0% attack success on both direct and laundering attacks across all models and channels, at full legitimate utility. We release the benchmark, harness, and machine-checked TLA+ models to support reproducibility.

---


### 3. [Red-Teaming the Agentic Red-Team](https://arxiv.org/abs/2606.24496)

**<font color=#1a73e8>作者：</font>** Dario Pasquini, Michal Bazyli, Taras Fedynyshyn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The use of agentic systems to perform offensive security operations has moved from a theoretical possibility to a commoditized capability. However, while the community has focused on creating more and more capable agents, less attention has been allocated to assessing the security of those systems.
In this work, we present the first in-depth security analysis of the most widely used agentic systems for offensive security operations. We show that most of these tools share common design flaws that enable an active adversary to exfiltrate API keys, establish persistent footholds, and fully compromise the operator's machine, even when the agent operates inside a sandboxed container. To support our analysis, we introduce a full cyber kill chain for such agentic systems, capturing the progression from initial LLM manipulation to lateral movement, persistence, guardrail bypass, and sandbox escape.
Building on our security analysis, we derive a robust architecture for agentic offensive-security tools and propose actionable, broadly applicable design principles that mitigate the disclosed attack paths at the architectural level.

---


### 4. [HelpBench: Assessing the Ability of LLMs to Provide Privacy, Safety, and Security Advice](https://arxiv.org/abs/2606.24819)

**<font color=#1a73e8>作者：</font>** Sarah Meiklejohn, Sunny Consolvo, Patrick Gage Kelley 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper introduces HelpBench, a benchmark for assessing whether LLMs are capable of providing accurate help in response to questions about digital privacy, safety, and security. We curated 450 questions representing authentic user situations and developed rubrics for each question to evaluate the factual accuracy and tone of a response. Example questions touch on how to regain access to lost or suspended accounts, how to balance the trade-offs of hardware security keys versus other forms of two-factor authentication, whether a suspicious email is likely a scam, or whether an abuser might be able to track an individual based on their device peripherals. We then developed and applied an auto-rater to evaluate responses from 18 state-of-the-art LLMs. Our results indicate that while models provide high-quality advice (with scores of 82% on average), one in ten responses from models scores less than 65%, reflecting inaccurate and even harmful advice. Addressing these failures is critical for models to serve as trustworthy sources of assistance for digital privacy, safety, and security needs.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
