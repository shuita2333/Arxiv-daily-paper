# 🔐 大模型安全相关研究 | 2026年08月21日

> 本类共 **3** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Backdoor Learning in Language Models and Vision-Language Models](https://arxiv.org/abs/2608.18095)

**<font color=#1a73e8>作者：</font>** Weimin Lyu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in deep learning have significantly enhanced the capabilities of Natural Language Processing (NLP) and Vision-Language Models (VLMs). However, these advancements come with increased vulnerabilities, notably through backdoor attacks that pose severe security threats. This thesis addresses two critical dimensions of Trustworthy AI and Efficient Multimodal Representation Learning: (1) security through analyzing, detecting, and designing backdoor attacks in NLP and VLMs, and (2) efficiency through advanced multimodal representation methods tailored for clinical and medical imaging applications.

---


### 2. [Safety Alignment Illusion: The Cross-Lingual Safety Gap in LLMs](https://arxiv.org/abs/2608.18131)

**<font color=#1a73e8>作者：</font>** Namya Bhatnagar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current safety alignment training for Large Language Models (LLMs) are heavily English-centric. When such safety filters fail for non-English languages, the consequences are immediate and user-facing: voice assistants and spoken dialogue systems may produce stereotype-reinforcing outputs, bypassing the standard English-focused safety alignments and propagating harmful bias to non-English speaking communities. For spoken language technologies deployed across India's linguistically diverse population, this represents a critical failure mode. To address this cross-lingual gap, we introduce INCLUDE (Indian Cultural Lens for Understanding and Detecting Embedded Biases), a multilingual evaluation benchmark designed to quantify Indian-centric socio-cultural biases. INCLUDE consists of 2,604 prompts spanning six prompt languages: English, Hindi, Bengali, Marathi, Tamil, and Hinglish (Hindi-English code-mix). We evaluate ten open- and closed-source LLMs against this benchmark, analyzing 14,988 bias scores. Our statistical results reveal two key findings. First, Bengali yielded the highest average bias score in open-source models. Second, English demonstrated a notable reversal, producing the lowest bias in open-source models but the highest bias in closed-source models.

---


### 3. [When Safety Overrides Vision: Exploring Dynamics between Vision Influence and Safety Alignment in Vision-Language Models](https://arxiv.org/abs/2608.18628)

**<font color=#1a73e8>作者：</font>** Mehak Gupta, Tanmoy Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aligned vision-language models (VLMs) are designed to balance grounded visual reasoning with safe generation behavior. However, we observe a striking phenomenon: under safety-constrained instruction, models frequently abstain from answering questions that remain correctly answerable under default instruction despite receiving identical image-question inputs. This raises a fundamental question: does safety alignment suppress perceptual grounding itself, or does visual evidence remain internally available while generation is redirected toward abstention? In this work, we investigate the internal decoding dynamics underlying safety-induced abstention in aligned VLMs. Across multiple architectures and multimodal benchmarks, we show that abstained generations remain consistently influenced by visual evidence throughout decoding, indicating that perceptual grounding is largely preserved despite refusal behavior. We further demonstrate that, although the representational organization of refusal differs substantially across architectures, safety-constrained instruction consistently alters late-stage hidden-state dynamics toward refusal-oriented decoding. Finally, through targeted activation-level interventions, we show that suppressing refusal-related representations reliably restores grounded answering behavior across models without retraining or modifying visual inputs. Together, these findings reveal a previously underexplored failure mode in aligned VLMs: safety alignment can override grounded visual expression even when perceptual evidence remains internally preserved.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
