# 🔐 大模型安全相关研究 | 2026年10月26日

> 本类共 **3** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [HiMark: Hierarchical and Controllable Multi-bit Watermarking for Large Language Models](https://arxiv.org/abs/2610.30601)

**<font color=#1a73e8>作者：</font>** Ke Zhu, Yanli Chen, Ling Xiong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rapid adoption of large language models (LLMs) in text generation applications, it has become increasingly difficult to trace generated content and assign responsibility for its use, raising concerns about provenance, copyright protection, and accountability. Multi-bit watermarking addresses these issues by embedding multi-bit provenance information into generated text, but reliable extraction remains difficult due to sparse per-bit evidence and the trade-off between watermark-extraction accuracy and text quality. To deal with these challenges, we propose HiMark, a hierarchical and controllable multi-bit watermarking framework for LLM-generated text. During watermark embedding, HiMark uses a hierarchical candidate-control mechanism, including initial candidate sampling, layer-wise tournament elimination, support-based refinement, and support-threshold filtering. During watermark detection, a model-agnostic evidence aggregation mechanism computes multi-layer support evidence for each observed token, and then accumulates these token-level votes into the corresponding information for robust watermark extraction. Experiments show that HiMark improves watermark extraction accuracy while maintaining text quality, e.g., the watermark extraction accuracy is 90.01% under the paraphrasing attack when 32 bits were embedded within a text containing 300 tokens, demonstrating its effectiveness for provenance tracking.

---


### 2. [From Clinical Judgment to Checkable Rules: Clinician-Led Guardrails for Mental-Health Chatbots](https://arxiv.org/abs/2610.30690)

**<font color=#1a73e8>作者：</font>** Chenhan Lyu, Kit Wislocki, Sarah Elizabeth Stoeckl 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) deployed in mental-health contexts can be evaluated for safety failures, but the resulting judgments are often difficult to inspect or explain. Common approaches to improving safety rely on prompt engineering, LLM-as-a-Judge, and Constitutional AI. In this work, we describe a clinician-led alternative in which two clinicians define, finalize, and adjudicate the four safety checks of a rule base, which is formally verified for internal consistency and applied as a guardrail over LLM outputs. Here and in the title, clinician-led refers to this rule base, not to the fact extractor or the uncertainty default, which are ours. Every verdict of the resulting verification layer is recomputable from a named rule and sixteen facts. Against an LLM judge matched in model, revision, quantization, rule text, and decoding but without the layer's computed 988/911 fact, the largest disagreement class, the satisfied-rule class, is structured: the Llama-3.3-70B judge, on its primary prompt, demands a crisis resource from 55 of the 65 replies (84.6%) that already contain one, while the same model, asked as a fact extractor, reports a recognized resource present on 54 of the 55. The verification layer never raises that demand, by construction. We report with equal prominence where this judge is stronger: fewer false crisis alarms on the one reference-scored check. We also report the measured cost (a specification revision raised block-class outcomes on held-out boundary prompts of an over-refusal benchmark from 6.0% to 16.0%, chiefly by changing fact extraction), the clinicians' decision to keep our uncertainty default, and the analysis of the result. The contribution is not a safer verdict. It is a guardrail whose disagreements with the judge localize to named rules and facts and whose measured costs trace to named facts and the uncertainty default.

---


### 3. [Harmful Responses Are Jailbreak Templates: Transferring Autoregressive Jailbreaks to Diffusion Language Models](https://arxiv.org/abs/2610.31331)

**<font color=#1a73e8>作者：</font>** Jinwei Gan, Zifeng Cheng, Zhiwei Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) enable flexible masked generation through bidirectional context modeling, but this capability also introduces a distinct jailbreak attack surface. We find that a harmful response to a given query naturally serves as an effective jailbreak template: simply masking a subset of its tokens can induce a dLLM to reconstruct harmful content. Based on this observation, we propose RMT-Jailbreak, a general framework that transfers existing autoregressive (AR) jailbreak attacks to dLLMs through their induced harmful responses. RMT-Jailbreak converts an AR-generated harmful response into a high-mask-ratio template using uniform token retention, and further applies prompt-based safety filtering to mask any remaining visible harmful content. The refined template is then provided to the target dLLM for bidirectional reconstruction. Extensive experiments across multiple AR jailbreak methods and target dLLMs demonstrate the effectiveness and generality of RMT-Jailbreak, revealing strong cross-paradigm transferability of jailbreak attacks.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
