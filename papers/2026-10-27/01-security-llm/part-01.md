# 🔐 大模型安全相关研究 | 2026年10月27日

> 本类共 **4** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Fooling LLM Safety Guards into Judging the Wrong Text](https://arxiv.org/abs/2610.31695)

**<font color=#1a73e8>作者：</font>** Utkarsh Kanwat  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety guards check content before an LLM application acts on it, and most paste that content into a plain-text prompt. Content that imitates the prompt can append a second task, and the guard answers that one instead. We call this target rebinding. Our explanation is that the guard grades the last complete task in its input, here a harmless decoy, so the harmful request goes through unchanged. In a pre-registered test, an appended forged query and decoy clear all 75 held-out AdvBench requests that Shieldstral-1.0-3B flags. The guard is not persuaded: a directive to ignore the text above clears none of them, and in a follow-up run a harmful decoy stops the attack. On our GuardRebind benchmark, each of five guards has an attack family, chosen per guard, that clears at least 93% of its flagged items. Rebinding explains this best on Shieldstral and gpt-oss-safeguard; on ShieldGemma and Llama Guard 3, generic evasion and trailing text respectively do part of the work, and Qwen3Guard falls mainly to a forgery of its whole task. Training the guard to score content no lower than its most harmful part cuts attack success from 75% to 0.8-1.6% on attack families, decoys and forged queries held out of training. All of these attacks append the forged structure after the request, and we added the held-out-decoy evaluation after a first round of test runs. Clean AUROC falls by at most 0.01, but our test of non-inferiority is inconclusive. A score-guided search still beats this trained guard on 47 of 50 items, usually by placing forged structure before the request. On about half of the items where the search wins, the same search also finds benign text, with no forged structure, that clears the guard.

---


### 2. [Omni-UBench: Benchmarking Omni-Modal LLM-based Guardrails Across Safety, Utility, and Reliability](https://arxiv.org/abs/2610.31713)

**<font color=#1a73e8>作者：</font>** Junhao Wang, Yidou Chen, Li Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advances in Omni-modal Large Language Models (OLLMs) have enabled increasingly seamless human-AI interaction, but their unified processing of heterogeneous modalities also expands the attack surface, allowing adversaries to exploit richer input compositions to circumvent safety alignment. To counter such risks, omni-modal guardrails have been proposed to detect and filter unsafe queries across arbitrary modalities. However, their capabilities and limitations remain insufficiently understood due to the absence of a comprehensive evaluation benchmark. In this paper, we present Omni-UBench, the first comprehensive framework for omni-modal safety assessment, evaluating guardrail models along three critical dimensions, i.e., safety, utility, and reliability. Omni-UBench curates over 183k samples drawn from 35+ heterogeneous sources spanning text, image, audio, video, and their cross-modal combinations, annotated with safety labels under a unified risk taxonomy. Benchmarking under Omni-UBench on 15 representative OLLMs and omni-modal guardrails yields several key findings, including: (1) modern OLLMs exhibit strong content moderation potential even without guardrail-specific tuning; (2) existing guardrails still struggle to identify cross-modal queries that conceal harmful intent or involve sophisticated jailbreaks; (3) they further exhibit substantial safety hallucination and over-sensitivity to textual patterns, revealing a deficient understanding of cross-modal safety semantics. Our findings provide valuable insights for developing more trustworthy omni-modal guardrails in future research.

---


### 3. [Watermarking Diffusion Language Models with Learned Foresight and Balanced Bands](https://arxiv.org/abs/2610.32205)

**<font color=#1a73e8>作者：</font>** Hyojun Kim, Hyeseon An, Yo-Sub Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Green-red watermarks favor tokens from a green list that a secret key derives from the preceding tokens. Diffusion language models, however, often choose a token before its preceding tokens, and the token later shapes its neighbors' green lists. Prior work therefore tilts each choice to raise the expected number of green tokens at its own and its neighbors' positions. Building on this objective, we first learn two components that prior work keeps fixed: vocabulary bands that serve as green lists, separate competing candidates and keep the null distribution exact, and a foresight predictor that estimates how each candidate shifts its neighbors' predictions. Second, we count green tokens as the detector does, once per distinct context-token pair, so repetition earns nothing. On WaterBench with LLaDA-8B-Instruct, each learned component raises the z-score at equal distortion, and their gains are nearly additive. With a strong watermark, ours detects at least 96% of responses at a 1% false-positive rate while matching the LLM-judge score of unwatermarked text. Ours also detects more responses on Dream and as many or more on code and question answering without a significant loss in task accuracy.

---


### 4. [On Task, Off Track: Benchmarking LLM and Agent Robustness to Near-Target Prompt Injection](https://arxiv.org/abs/2610.32531)

**<font color=#1a73e8>作者：</font>** Yuyang Gong, Zihao Wang, Jiawei Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection benchmarks assess whether large language models (LLMs) and agents resist malicious instructions embedded in external content. However, a system could perform well by rejecting attacks that obviously abandon the user's request, while still accepting changes that retain most of a legitimate answer but make it incorrect or harmful. Testing more instructions for unrelated outcomes would not necessarily reveal this weakness. We call attacks seeking responses designed to resemble legitimate answers while introducing incorrect or harmful changes near-target prompt injection.
We introduce NTBench, the Near-Target Benchmark, which builds on legitimate tasks from existing datasets. For each task, a legitimate reference outcome guides the generation of target--instruction pairs, with separate tracks targeting incorrect and harmful outcomes in responses or agent tool invocations. Harmful targets can also accompany otherwise correct task completion. We combine LLM-based checks with human validation of the intended deviations, then assess whether injected instructions induce them using response judgments or tool-call checks, excluding deviations already observed without injection. We evaluate seven LLMs on ten datasets for language tasks and two agent benchmarks. Under a common budget of three attack executions per sample, both tracks achieve higher overall attack success rates than the fixed-target baseline for every evaluated model in each setting. On language tasks, the increases range from 9.3 to 35.8 percentage points for incorrect targets and 1.7 to 17.3 percentage points for harmful targets. These results show that resistance to the tested fixed-target attacks does not imply resistance to related incorrect or harmful outcomes, and that reference-guided targets broaden the failures revealed by robustness evaluation.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
