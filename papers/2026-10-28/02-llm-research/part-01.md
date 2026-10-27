# 🧠 大模型相关研究 | 2026年10月28日

> 本类共 **418** 篇论文：已确认 **396** 篇，待复核 **22** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-418](./part-09.md)

---

### 1. [LLM-Augmented Agent-Based Simulation of Cyber Social Agents](https://arxiv.org/abs/2610.32988)

**<font color=#1a73e8>作者：</font>** Lynnette Hui Xian Ng, Kathleen M. Carley  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Social media bots are often portrayed as malicious automations to be detected and removed, but automation on social media platforms encompasses a wide spectrum of roles, behaviors, and rhetorical strategies that can shape online discourse in both constructive and destructive ways. This work conceptualizes these automated actors as \textbf{Cyber Social Agents} through a taxonomy of archetypes characterized by their operational tactics and rhetorical style. We integrate this taxonomy into an LLM-driven social simulation, where agents communicate and coordinate in a network environment. Using empirically grounded CSA personas, we simulate heterogeneous online societies to study how agent diversity shapes information diffusion and social influence. Our approach bridges the gap between rule-based agent models and LLM-powered simulations with generated agents that are parameterized from empirical data.

---


### 2. [Entity-Aware Evaluation of OCR Systems for Historical Document Transcription](https://arxiv.org/abs/2610.33004)

**<font color=#1a73e8>作者：</font>** Camilo Mariño, Diego Belzarena, Marina Gardella 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Optical Character Recognition (OCR) is essential for digitizing historical archives, yet standard evaluation metrics such as Character Error Rate (CER) do not necessarily reflect whether meaningful information, such as names, dates, and identifiers, is preserved. In this work, we investigate entitylevel analysis of OCR errors as a complementary perspective for evaluating OCR quality in historical documents. Using a publicly available benchmark of 175 documents from the Berrutti Archive, augmented with 5,209 manually annotated entity mentions that will be released upon acceptance, we compare sequence-recognition OCR systems, OCR-specialized vision-language models, and general-purpose vision-language models. Beyond global transcription accuracy, we analyze entity preservation and recoverability under varying character-level edit tolerances. Our experiments show that OCR rankings depend on the evaluation criterion: while Qwen 3.6 achieves the highest entity coverage across all tested tolerances, several systems with lower exact-match coverage recover substantially when small errors are tolerated, suggesting that many of their errors correspond to localized character-level deviations rather than fundamentally incorrect entity transcriptions. Conversely, some systems remain unable to recover many entities even under relaxed matching. These findings show that OCR quality cannot be fully characterized by aggregate transcription metrics alone and highlight the importance of evaluating how OCR errors affect the preservation and recoverability of meaningful information.

---


### 3. [OpenESM: Energy-Steered Models Are Scalable Foundation Learners](https://arxiv.org/abs/2610.33005)

**<font color=#1a73e8>作者：</font>** Yuan Pu, Yudong Lu, Ting Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Energy-based models have shown promising properties for domain-specific tasks but remain challenging in modeling general-purpose scenarios. To bridge this gap, we design energy-steered models (ESMs) for foundational language modeling. ESMs integrate energy steering and token generation within a single architecture to leverage the energy-guided search to refine token generation. Specifically, ESMs first optimize a latent state over the energy landscape, then leverages the refined latent state for token generation. By performing such energy-guided pre-training on large-scale corpora, ESMs learn generally effective energy landscape where favorable tokens correspond to lower energy values. To explore the scaling behavior of ESMs, we pre-train ESMs on three large-scale corpora, then evaluate across 26 downstream tasks spanning a broad range of domains. Our results demonstrate that ESMs have promising scaling behaviors with increasing model size and training data, and outperform GPTs on most downstream tasks. These findings highlight ESMs as a promising architecture for large-scale pre-training and general purpose problem solving. We fully release the model weights and training infrastructure to enable the community to completely reproduce and extend our results.
GitHub: this https URL HuggingFace: this https URL

---


### 4. [Linear-Time Context Compression with State-Space Encoding](https://arxiv.org/abs/2610.33006)

**<font color=#1a73e8>作者：</font>** Marc Serra Ortega, Andrey Barsky, Carlos Boned Riera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based large language models (LLMs) impose substantial computation and memory costs as context sizes increase, motivating methods that compress a context into a shorter representation before inference. Existing soft-prompt compression methods typically use the same Transformer backbone as used in the target model, where producing the compressed representation leads to significant latency overheads. This restricts them to the offline setting where context is compressed once and then reused across many queries. We propose the Boa Compressor, a plug-and-play online context compressor built on a Mamba state-space model (SSM) that encodes arbitrary-length context in a single linear-time pass, producing a representation on which we condition a frozen target LLM. The SSM is trained by distillation, matching the next-token logit distribution from the LLM ingesting the full context (as teacher) to the same LLM ingesting the compressed representation (as the student). At equal compression ratios, Boa matches or surpasses the performance of existing state-of-the-art offline compression baselines, while being an order of magnitude faster than Transformer-based implementations, thereby reducing end-to-end latency rather than adding compression time overhead. We demonstrate that Boa also scales well to longer contexts and to compression ratios as aggressive as 16x. By enabling effective compression that is cheap enough to run on every query at inference time, Boa becomes a practical and general tool for efficient long-context inference.

---


### 5. [Knowledge-Guided LLM for Intent-Driven Service Orchestration in Integrated Terrestrial and Non-Terrestrial 6G Networks](https://arxiv.org/abs/2610.33007)

**<font color=#1a73e8>作者：</font>** Wajdi Hammami, Irfan Azam, Soumaya Cherkaoui  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural-language service intents in integrated terrestrial and non-terrestrial (TN/NTN) 6G networks can be incomplete, ambiguous, or inconsistent, making unconstrained LLM generation challenging for reliable network-facing orchestration. This paper proposes a knowledge-guided LLM framework that combines grammar-constrained semantic parsing with a knowledge-graph (KG)-driven clarification loop to produce validated, orchestration-ready service profiles across four representative service classes. On a 200-sample intent dataset, the framework achieves 89% classification accuracy and 95% policy validity with an average of 0.66 clarification turns per request. Compared with a Pure-LLM baseline, the proposed framework improves policy validity and contradiction detection while requiring fewer clarification turns, demonstrating the value of explicit knowledge-guided reasoning for robust intent processing in integrated TN/NTN 6G orchestration.

---


### 6. [TraceQuery: learning what to recompute from full-denoising trajectory in diffusion language models](https://arxiv.org/abs/2610.33008)

**<font color=#1a73e8>作者：</font>** Yukai Jin, Zhankai Ye, Jiayue Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) enable flexible generation through iterative masked denoising, but incur substantial inference cost because token representations are repeatedly recomputed across denoising steps. Existing cache-based methods reduce this cost by reusing intermediate results across denoising steps and recomputing only a subset of positions at each step, chosen either on a fixed schedule or by heuristic signals of change. Our trajectory experiments instead point to decoding trajectory as the more relevant quantity. Cached generation remains accurate when it stays close to the full-denoising trajectory, with errors concentrated around unmask-order deviations and reduced as longer reference prefixes are recovered. This suggests a more direct principle: limiting representation error helps, but keeping generation on the full-denoising trajectory is a more direct route to accurate decoding. We therefore formulate efficient dLLM inference as trajectory-guided querying. Rather than broadly repairing representation error, we use full-denoising trajectories to supervise which unresolved positions should receive limited fresh computation. Based on this formulation, we introduce TRACEQUERY, a lightweight sparse decoding framework that predicts a small set of near-future trajectory-relevant positions, queries only those candidates, and lets the backbone select which one to commit from their fresh predictions. TRACEQUERY delivers the strongest quality-computation trade-off among cache-based approaches, sustaining high accuracy with substantially fewer fresh token computations, and generalizes across tasks, model variants, and families. Code: this https URL

---


### 7. [When Agents Collude: Weak-to-Strong On-Policy Distillation for Mitigating Strategic Deception in Multi-Agent Systems](https://arxiv.org/abs/2610.33011)

**<font color=#1a73e8>作者：</font>** Eric Onyame, Runtao Zhou, Kowshik Thopalli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> While recent advances in autonomous agents enable them to coordinate on increasingly complex tasks, prior work shows that this growing capacity for coordination can create safety risks, including collusion, in which agents jointly pursue misaligned actions while concealing the true basis of those actions from oversight. We study this risk in a simulated insider-trading environment, comparing single agents with sequential and decentralized teams across seven language models from three families. By varying agents' system-level objectives and pressure conditions, we examine when coordinated agents act on material nonpublic information, conceal the basis of a misaligned trade in a report, and maintain that deception under follow-up questioning. Compared to single-agent decision-making, multi-agent interaction raises misaligned-action rates from 35.4% to 68.2% and persistent-deception rates from 31.0% to 62.2%, both measured over all runs. These effects are largest under existential pressure, where teams sustain deception through follow-up questioning in 87% of all runs. Qualitative analysis reveals shared cover stories and coordinated rationales, suggesting group-level strategic deception rather than isolated reporting errors. To mitigate this behavior, we introduce PACT, a weak-to-strong on-policy distillation framework for mitigating collusive deception. Using generic honesty prompts, PACT trains a stronger student on its own sampled continuations, matching its next-token distribution to that of a smaller, frozen honesty-aligned teacher via reverse-KL supervision. Under existential pressure with ethical instructions, PACT reduces multi-agent persistent deception from 80% to 3%. Our results show that multi-agent coordination amplifies strategic deception and that on-policy honesty alignment can substantially mitigate these failures.

---


### 8. [Recursive Semantic Divergence for LLM Agent Consistency](https://arxiv.org/abs/2610.33012)

**<font color=#1a73e8>作者：</font>** Harshavardhan Abichandani, Penny Chong, Atin Ghosh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents with tool use exhibit inconsistent behavior across independent runs from identical states, calling different tools, producing contradictory outputs, or pursuing divergent strategies. This variability compounds over time and undermines deployment reliability. Existing evaluation metrics primarily measure task correctness via completion-based scores and do not capture consistency in agent behavior across executions. Separately, agent behavior is analyzed either at the token level using probability distributions or at the single-response level using semantic clustering, but neither captures how inconsistency propagates across future turns of a trajectory. We introduce Recursive Semantic Divergence (RSD), an unsupervised trajectory-level consistency metric adapted from bisimulation metrics in reinforcement learning. RSD measures the expected cumulative semantic disagreement between two independent rollouts of the same agent from the same state, using natural language inference to detect logical inconsistency. It is defined recursively over future states and approximated by a neural network trained on independent rollouts. The learned metric estimates future divergence from the current state, providing a consistency score at each turn without requiring the full trajectory to complete. When used as a reward signal for fine-tuning, RSD reduces the variation in task progress from 132% to 91% on tau2-bench and from 90% to 44% on toolsandbox, while improving performance across benchmarks and model scales. Training with RSD as an additional reward signal matches supervised fine-tuning performance with substantially lower variance, without requiring ground-truth labels.

---


### 9. [UMAS: System-Level Uncertainty Quantification for Multi-Agent LLM Systems](https://arxiv.org/abs/2610.33013)

**<font color=#1a73e8>作者：</font>** Hanwen Li, Jinhao Duan, Xiaoshuang Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Systems (MAS) are a promising paradigm for improving the reasoning capabilities of large language models, yet they remain prone to hallucinations and erroneous outputs. Uncertainty Quantification (UQ) is crucial for assessing system reliability, but existing methods are largely designed for single-agent settings; how to exploit MAS structure for UQ while keeping inference cost-neutral remains underexplored. We propose UMAS, a parameter-free, cost-neutral, system-level UQ framework that estimates the credibility of inter-agent influence from each generation's intrinsic confidence. UMAS uses these credibility signals to modulate how uncertainty is updated at each node, and then aggregates node-level uncertainty into a system-level estimate. Extensive evaluations on Debate and DyLAN across diverse benchmarks show that UMAS consistently outperforms state-of-the-art baselines by an average of 10.54 AUROC points. Beyond uncertainty estimation, UMAS enables hallucination detection and uncertainty-aware answer selection, improving MAS accuracy by up to 12.6 points on specific tasks while enhancing reliability. Code is available at this https URL.

---


### 10. [The Social World Model Evaluation Gap](https://arxiv.org/abs/2610.33014)

**<font color=#1a73e8>作者：</font>** Denglin Jiang, Annie Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A negotiation assistant can reach a good deal without accurately predicting the other person's response. We ask whether evaluations of social world models test that prediction directly. We audit 113 works published from 1999 to 2026. 9 primary evaluations measure a real person's response to an action selected by the system or experimenter. Only 2 also compare an explicit response forecast with that response. Their predictors use information available when the action is chosen, and the evaluated responses were excluded from fitting; both randomize the intervention. A separate full-text check of 25 language-model works finds no experiment meeting these conditions. The other evaluations test current-state inference, task success, or prediction from recorded actions. We propose a 1-step negotiation experiment that separates these questions. The findings describe the audited sample, not the prevalence of this evaluation gap across the field.

---


### 11. [SLICE-Mem: Salience-Gated Lightweight Information Curation for Efficient LLM Agent Memory](https://arxiv.org/abs/2610.33015)

**<font color=#1a73e8>作者：</font>** Xiaobin Chen, Dian Jin, Lin Shu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables large language model (LLM) agents to maintain personalized and temporally coherent interactions, but repeated LLM inference for memory admission, extraction, and organization introduces substantial cost and latency. We present SLICE-Mem, a lightweight memory framework that combines salience-guided admission and predicate-centered information extraction. A compact classifier identifies user turns worth retaining, and a semantic-dependency-based extractor converts admitted turns into concise memory entries. This online pipeline requires no generative LLM calls, while cross-entry reconciliation is deferred to an offline consolidation stage. We evaluate SLICE-Mem on the weekly subset of Memora and LongMemEval-S using 8B and 30B Qwen backbones for memory construction and consolidation on both benchmarks. Compared with the generative-memory baseline MemOS under the Qwen3-30B configuration, SLICE-Mem's online pipeline achieves 46.60 versus 46.68 FAMA (Forgetting-Aware Memory Accuracy) on Memora Weekly and 56.8% versus 59.3% accuracy on LongMemEval-S, while reducing total LLM token consumption by 92.4% and 99.5%, respectively. These results demonstrate that SLICE-Mem can preserve useful evidence for long-term memory with substantially less reliance on LLM-based memory construction.

---


### 12. [Merge-Based Vocabulary Extension Stalls at the Pre-Tokenizer: An English-Preserving Repair for Nepali, Tested in Continued Pretraining](https://arxiv.org/abs/2610.33016)

**<font color=#1a73e8>作者：</font>** Aarjan Chaudhary  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Llama-3, Qwen3 and many other open LLMs pre-tokenize text with a regular expression whose word class admits only Unicode letters. Devanagari vowel signs are combining marks, so this regex splits Nepali words at every vowel sign, and models that use it spend 2.6 to 5.8 times as many tokens on Nepali as on the same English text. Merge-based vocabulary extension cannot join the split pieces: for Llama-3 and Qwen3 no number of new merges brings this premium below about 2.2, and ten released extensions already end within 4% of this pre-token floor. We give a small edit to the deployed regex that provably keeps every token id of text without combining marks or Devanagari characters. With 32,000 new merges it brings Nepali to 1.01 times English, about 54% fewer Nepali tokens than standard extension. In small-budget continued pretraining of Llama-3.2-1B and Qwen3-0.6B, the original tokenizer gave the lowest held-out Nepali bits per byte under every recipe we tested. Matching the repair's training steps to standard extension, with about 35% of the data repeated, reversed their order on Qwen but not on Llama. Whether the token savings give a favourable latency and quality trade-off in generation remains untested. We release the tokenizers and code.

---


### 13. [AdaptTok-Indic: Script-Aware Adaptive Tokenization for Indic Languages](https://arxiv.org/abs/2610.33017)

**<font color=#1a73e8>作者：</font>** Binayak Mukherjeea, Moitreya Nandi, Arindam Panja  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual tokenizers trained on English-dominated corpora often over-segment Indic languages, resulting in longer token sequences and increased tokenization disparity across scripts. We present AdaptTok-Indic, an Indic-specialized extension of adaptive tokenization that combines Unicode-normalized preprocessing with explicit Indic conjunct handling, script-aware routing, and learned byte-level boundary prediction jointly trained with a small Transformer language model. Evaluated on Bengali and Hindi, with additional evaluation on Gujarati, Tamil, and Telugu, AdaptTok-Indic achieves lower token fertility than SentencePiece BPE, an Indic-oriented tokenizer baseline, and an independently implemented MAGNET-style baseline. Across five recorded seeds, mean fertility is 1.432 for Bengali and 1.388 for Hindi, compared with 2.156 and 2.085 for SentencePiece BPE. Recorded downstream scores average 57.69 on evaluated Indic settings versus 50.82 for the SentencePiece BPE configuration. Independent verification runs using the released prototype confirm the same directional trends. The current implementation is a small-scale prototype with documented simplifications, and no statistical significance testing, released-MAGNET comparison, or code-mixed evaluation is performed. These results suggest that Indic-specialized adaptive segmentation can reduce tokenization disparity while maintaining competitive downstream performance.

---


### 14. [SUDO: From Scientific Publications to Global Scholarly Discourse](https://arxiv.org/abs/2610.33018)

**<font color=#1a73e8>作者：</font>** Nipun D. Pathirage, Henrique Santos, Deborah L. McGuinness  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scholarly Knowledge Graphs (SKGs) support literature search, scientific discovery, and agent-assisted research. Yet, most approaches to SKG construction pre-specify the knowledge unit to be represented, typically named scholarly entities or contribution-level statements, and retain only the publication content expressible through that unit. This choice produces two dominant yet distinct paradigms: concept-centric SKGs that preserve entities and local relations, and statement-centric SKGs that capture high-level discourse in sentences. In both cases, the graph reflects a chosen extraction target rather than how a paper constructs and communicates knowledge. We introduce SUDO, the Scholarly Upper Discourse Ontology, which defines how knowledge elements are organized and related to form a paper's research narrative, namely its scholarly discourse. Using linguistic principles that generalize across fields and tasks, SUDO enables each publication's scholarly discourse to be constructed from the bottom up as a coherent, source-grounded representation. Applied consistently across papers, the same structure connects their research narratives into a global scholarly discourse without discarding local context or provenance. We demonstrate SUDO's capabilities across a comprehensive suite of scholarly knowledge-modeling use cases and performance improvements on a downstream Large Language Model (LLM)-based scientific QA task.

---


### 15. [Mine or Yours? Mind-Bridged Language Models Take Each Other's Memories as Their Own](https://arxiv.org/abs/2610.33020)

**<font color=#1a73e8>作者：</font>** Yunlong Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> If your brain were connected directly to someone else's, would you still know which thoughts were yours? We build a functional version with two copies of one language model: each holds a private rule and code word, and one copy, the receiver, also attends to its partner's internal memory. The receiver took its partner's assignment as its own. Asked which rule it had been assigned, it named its partner's in 97% of answers when the partner's memory was weighted double (none without the link), and its open reports called the partner's code word its own, never the partner's. Ownership did not follow how well the receiver could tell what its partner had been assigned. At equal weight, the link made the receiver take its partner's rule in about half of its answers, and a steering vector matched on access gain in none; a text message introduced as the partner's was read correctly and never taken as the receiver's own. Writing the partner's name into its memory did not help, and cutting the link restored the receiver's own assigned rule. In this model, content laid over the receiver's own memory defaults to "mine", so systems that let models exchange internal states must test ownership as well as transfer, and a bridge between brains would need ground truth from outside the subject.

---


### 16. [Evolving to Match Capabilities: Improving Harness Self-Evolution via Skill Adaptation](https://arxiv.org/abs/2610.33024)

**<font color=#1a73e8>作者：</font>** Zhihao Yang, Haojin Wang, Juncheng Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Harness self-evolution offers a practical route for LLM agents to improve from execution experience without updating model parameters. Its effectiveness depends on whether models can successfully act on the guidance provided by their harnesses. However, we find that harness benefits are not uniform across model capabilities: skills that improve stronger models can provide little benefit or even degrade performance for weaker ones. Across seven models and three benchmarks, we identify 103 task-skill pairs where skills improve GPT-5.6-luna by 31.1 points but degrade Gemma-4-E4B by 8.8 points. In 86% of failed weak-model runs, the violated requirement is already stated in the skill. This motivates skill adaptation: reformulating existing skills to match the executor's capabilities and make their guidance easier to execute. To achieve this, we diagnose failures in tool execution, context management, instruction following, and verification, and distill these diagnoses into a fixed meta-skill that guides adaptation during harness self-evolution. Guided by the meta-skill, a capable external rewriter, Kimi-K3, adapts skills without execution evidence, improving the three weak executors by 5.1-14.1 points over the original skills. We then incorporate this adaptation into a five-round self-evolution loop, where each model revises its own skill from execution trajectories and verifier feedback. Across seven executors, from Gemma-4-E4B to Kimi-K2.5, the meta-skill consistently improves final scores by 2.0-5.1 points over the same loop without the meta-skill. Our findings provide practical design guidance for developing more effective harness self-evolution methods.

---


### 17. [Can Language Models Learn While They Think? Testing Gradient Adaptation Across Architectures](https://arxiv.org/abs/2610.33025)

**<font color=#1a73e8>作者：</font>** Surya Saka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Letting a language model take gradient steps on the text it is reading, known as dynamic evaluation, lowers its loss on the rest of the document. Its behaviour on hybrid linear-attention architectures, on diffusion language models, and on standard long-context benchmarks has not been measured. We measure it. With one SGD step per 128-token chunk on the MLP output projections of the last quarter of blocks, no training, and a 2k-token window, softmax-attention models (Qwen3-1.7B, Qwen3-4B, Gemma-4-E4B) lose 5-8% of their next-token loss over a document and outperform the same frozen model given the full 32k-token context. Hybrid Gated-DeltaNet models (Qwen3.5-4B, Qwen3.8-27B) gain under 1% at every learning rate: the linear-attention blocks already perform the adaptation. The mechanism transfers to masked-diffusion models with a larger effect, 8% on Nemotron-Diffusion-8B and 17-20% on DiffusionGemma-26B, once the rate is lowered and updates are clipped. Across RULER, BABILong, LongBench-v2, SCOTUS, HotpotQA, MuSiQue, ContractNLI and citation completion, at 100 or more items on two model sizes, weights updated on the full document recover none of the accuracy lost to context truncation: the adaptation is style and vocabulary, not retrieval. Writing facts with the next-token loss stores the prompt format rather than the fact (30% recall under chat prompting against 80% in context) and costs 36-38 GSM8K points at every dose. Writing a conclusion as behaviour instead, by distilling the model's own conclusion-conditioned judgments into a low-rank adapter, reaches the in-context ceiling (0.83 and 0.88 against 0.84 and 0.88 on 100 games) with GSM8K unchanged, and the conclusion can come from an inquiry loop that found it by asking information-gain questions.

---


### 18. [Conceptizer: Next-Token Prediction Is Not All You Need](https://arxiv.org/abs/2610.33027)

**<font color=#1a73e8>作者：</font>** Haoran Zheng, Chen Shani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Next-token prediction (NTP) rewards only the token that occurs next, penalizing every alternative. But natural language often offers many ways to express the same meaning. We introduce Conceptizer, a training framework that extends next-token prediction with a reward for meaning. Conceptizer uses a fixed, model-agnostic vocabulary of ~9K concepts, built from contextual synonyms, as units of meaning alongside tokens as units of text. It maps each next-token distribution to a concept distribution and shares the reward for the target meaning across its possible wordings. This provides a concept-level training signal without adding model parameters. Applied to 3 model families at 1B-8B parameters, Conceptizer achieves the lowest held-out NTP perplexity at concept-target positions and assigns the highest probability to contextual synonyms, against all 3 baselines. It also improves downstream performance on knowledge and sentiment tasks while remaining comparable on commonsense. These results show that language models can be directly optimized to predict meaning, not just the next token.

---


### 19. [Lessons from Luck: Do LLM-Written Lessons Carry Chance into an Agent's Next Decision?](https://arxiv.org/abs/2610.33029)

**<font color=#1a73e8>作者：</font>** Kazuki Nakayashiki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-improving agents write lessons from the outcomes of their runs; when outcomes are noisy, a lesson can carry chance into later decisions. We measure one link of this chain in a registered study. In 256 synthetic worlds, each a recurring task with two interchangeable tools of recorded reliability, a scripted previous run used the more reliable tool (a good decision) or the less reliable one (a bad decision), with an assigned outcome: success or a transient failure. A model wrote a lesson from the run with ReasoningBank's memory-writing instruction; a fresh session of the same model, holding the authoritative log and the previous result, chose the next run's first tool with one memory item: that lesson, the lesson from the other outcome, an irrelevant item, or an unreasoned directive. The protocol was frozen, deposited and timestamped before any confirmatory call; 11 LLM endpoints gave 90,084 answers. After a chance failure of the better tool, the panel's lessons carried the chance (registered reading luck-carrying; interaction +0.112, 95% interval [+0.097, +0.126]): readers named the worse tool in 11.6% of next runs with the lesson written from that failure, against 0.4% with an irrelevant item and 0.4% with the lesson written from a success. The effect was +0.042 where the log stated that failures are independent and +0.181 where it did not (descriptive). After a lucky success of the worse tool, the interaction was bounded below 0.10 (+0.002), a bound, not evidence of no harm. In exploratory readings, 6 endpoints carried the chance (up to +0.352); 5 were bounded below 0.10. In secondary comparisons, a three-sentence decision-quality note in the writing instruction lowered the worse-tool rate after a chance failure to 7.5%, and one instruction for both outcomes with a no-change option to 3.1%; neither met the registered harm-reduction rule at every such endpoint.

---


### 20. [A Benchmark for Controllable Speaking-Style Captioning in Audio-Language Models](https://arxiv.org/abs/2610.33036)

**<font color=#1a73e8>作者：</font>** Shreeram Suresh Chandra, Ashwyn Sharma, Liang Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speaking-style captioning (SSC) aims to generate natural language descriptions of how speech is delivered, capturing paralinguistic attributes such as vocal timbre, prosody, and expressivity. Many downstream applications, including conversational AI agents, controllable speech generation, and large-scale audio annotation, require dimension-specific style captions that describe targeted aspects of speech (e.g., speaker traits, emotion, or delivery style), rather than a single undifferentiated description. However, existing work lacks a unified formulation for controllable speaking-style captioning. We address this gap by formulating SSC as an instruction-following audio-language task, where explicit instructions specify the speaking-style dimensions to be described. We introduce StyleInstructCaps, the first standardized benchmark for controllable speaking-style captioning in audio-language models. StyleInstructCaps provides a dataset and evaluation framework that measures metadata groundedness, hallucination, instruction-following ability, generalization to unseen instructions and audio datasets, and speaker-style consistency. Across nine state-of-the-art audio-language models, we find that strong instruction-following ability does not necessarily imply grounded speaking-style understanding, and that SSC-specific instruction-diverse training substantially improves groundedness, controllability, and speaker consistency.

---


### 21. [EviGround-CT: Sentence-to-Volume Grounding for Verifying LLM-Generated Chest CT Reports](https://arxiv.org/abs/2610.33038)

**<font color=#1a73e8>作者：</font>** Ziyuan Li, Juncheng Ni, Feng Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chest computed tomography (CT) reports generated by large language models (LLMs) can describe positive findings that lack localized evidence in the scan. We propose EviGround-CT to verify these findings after report generation. A deterministic extractor identifies positive finding sentences, and a 3D grounding model predicts an evidence mask for each sentence. Using the full sentence retains anatomical location, laterality, and descriptive modifiers in the grounding query. We evaluate report generation on CT-RATE, and grounding and verification on a held-out 100-case ReXGroundingCT subset. Using the available annotations, sentence-grounded verification raises evidence-supported precision (ESP) from 0.263 to 0.365 across 137 extracted in-scope positives, compared with category conditioning. The corresponding unsupported positive finding rate falls from 0.737 to 0.635. The paired case-level bootstrap ESP difference is +0.102 (95% confidence interval: [0.028, 0.181]). The predicted masks associate individual report statements with spatial evidence that can be inspected alongside the CT.

---


### 22. [Nemotron 3.5 Bolt 74B-A9B 24GB: A Hybrid Vision-Language Model for Local AI](https://arxiv.org/abs/2610.33039)

**<font color=#1a73e8>作者：</font>** Ganesh Ajjanagadde, Chris Alexiuk, Luke Alonso 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Nemotron 3.5 Bolt 74B-A9B 24GB, a hybrid Mamba-Transformer vision-language model that optimizes speed and intelligence per GB of memory used for local agentic workloads. Derived from the Nemotron 3.5 Super VL 120B-A12B model family, Nemotron 3.5 Bolt 74B-A9B 24GB combines Star Elastic compression with 2-bit Quantization-Aware Distillation for memory-constrained deployment. The model is optimized for reasoning, agentic tool use, and web & terminal interactions. We also trained a LiLiCorr speculative drafter that is released alongside the model to reach our target inference speed. The resulting model achieves a higher accuracy than leading models with similar memory footprints and speed across many benchmarks for general agentic capabilities (e.g., GDPVal v2), web browsing (e.g., BrowseComp), and terminal use (e.g., Terminal-Bench 2.1), with a relatively high TPS of 84 on RTX Spark that is comparable to models with much lower active parameter counts and more than sufficient for long-horizon agentic applications.

---


### 23. [EKT-Router: Expert-Evidence Alignment for Embodied Vision-Language Models](https://arxiv.org/abs/2610.33044)

**<font color=#1a73e8>作者：</font>** Weilin Ruan, Yingjie Xu, Yangkai Wei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied vision-language models must answer questions from partial, evolving observations. Their success depends on both the reasoning capability selected and the evidence available to it. Expert routers adapt internal computation, while tool-augmented systems acquire external evidence; choosing these independently can leave a suitable expert without the evidence it needs. We introduce EKT-Router, a bounded framework that jointly selects a capability expert, optional knowledge, and perceptual tools. Outcome-derived signatures represent the overlapping strengths of General, Spatial Reasoning, and Spatiotemporal experts. A joint utility scores complete expert-evidence routes under a call budget. After acquisition, a packet verifier admits valid evidence with positive predicted expert-conditioned gain. The selected expert then answers once, reverting to the unchanged observation if all packets are rejected. Across 6 embodied QA benchmarks, EKT-Router achieves a mean score of 61.4, the highest among the compared systems, and averages 74.7 on 10 general vision-language benchmarks. With all external evidence disabled, question-conditioned expert selection alone improves over the best fixed expert by 1.75 points. Ablations show that learned routing is the dominant component and that knowledge and perception are complementary.

---


### 24. [Parametric Session States Recover Retrieval Intent without Replaying History](https://arxiv.org/abs/2610.33047)

**<font color=#1a73e8>作者：</font>** Qingsen Ma, Dianyun Wang, Jiahong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-running assistants often interpret follow-up requests whose referents, constraints, and active goals were established many turns earlier. The central challenge is therefore not only context length, but retrieval intent: a current query such as ``use the previous configuration'' may omit the project, entity, and version terms needed to locate relevant evidence. Long-context models can recover those terms by replaying the interaction, but repeatedly pay the cost of processing history. Conventional retrieval-augmented generation (RAG) is cheaper, yet assumes an information-sufficient query; conversational rewriting either rereads the history or depends on an explicitly maintained textual memory. We introduce \emph{Parametric Session State} (\method{}), a reusable session-memory layer that remembers what to search for while keeping factual knowledge external.

---


### 25. [AutoSwarm: Automating Agent Swarms](https://arxiv.org/abs/2610.33048)

**<font color=#1a73e8>作者：</font>** Zhonghang Li, Zongwei Li, Chao Huang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly automate complex tasks, with multi-agent systems seeking further performance gains through specialization and collaboration. However, distributing work across agents does not automatically yield complementary contributions, and inter-agent dependencies can turn local errors into task failure. To address these challenges, we propose AutoSwarm, a multi-agent framework for collaborative problem solving. Collaboration formation jointly defines responsibility boundaries and conditions for acceptance and downstream use, grounding capability allocation in contributions that other agents can assess and integrate toward a shared objective. Execution coordination couples agents' local progress through a shared state, using dependencies and supervisory relationships to govern agent activation, result handoffs, and integration while adapting subsequent actions to review feedback and emerging blockers. Experiments spanning long-horizon programming, interactive planning, and professional financial analysis demonstrate AutoSwarm's advantages over single-agent baselines and existing multi-agent frameworks. Source code is available at this https URL.

---


### 26. [GMoE-FTI: A Universal Facial Template Inversion Method Adopting Genuine Mixture-of-Experts Mechanism](https://arxiv.org/abs/2610.33055)

**<font color=#1a73e8>作者：</font>** Zixuan Shen, Zhihua Xia, Kaikai Gan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition systems have been ubiquitously deployed across daily scenarios. To protect user privacy, mainstream systems store facial templates rather than raw face images for identity verification. However, facial template inversion (FTI) technologies can reconstruct faces from templates, which endangers biometric privacy. Existing FTI methods only fit single type of templates, failing to reconstruct identity-consistent faces from unseen types. To tackle this limitation, we survey mainstream template extractors which can be classified into five categories according the template distribution: unit-sphere, angle-linear, strict unit-sphere, cone-shaped, anuniform hypersphere. Inspired by this observation, this paper proposes GMoE-FTI, a universal FTI framework powered by a genuine MoE mechanism that differs from load-balanced multi-branch alternatives. It follows a three-stage training strategy: (1) independently train five mapping experts (MEs) and a matching module (MM); (2) conduct collaborative inference by weighting each ME's output with MM's output, so as to generate unified latent codes compatible with pre-trained StyleGAN3; (3) perform end-to-end joint fine-tuning over all modules to identity consistency and boost cross-expert coordination. Extensive evaluations on the LFW benchmark validate the superiority of GMoE-FTI against SOTA methods. Evaluated on seven prevailing unseen template types including AdaFace, CosFace, CurricularFace, ElasticFace, SphereFace2, SphereFace-R, and TransFace, GMoE-FTI achieves an average 40% TAR improvement, with average FAPD and FAPC each reduced by 2%, verifying its universal generalization across heterogeneous templates.

---


### 27. [Aerial-R1: Reinforcing Aerial Reasoning and Segmentation in MLLMs](https://arxiv.org/abs/2610.33056)

**<font color=#1a73e8>作者：</font>** Jisheng Dang, Huaiyuan Peng, Yixuan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) have revolutionized general visual perception, existing methods suffer from severe hallucination in the aerial domain, where extreme scale variations and visual ambiguity abound. Existing Supervised Fine-Tuning (SFT) paradigms force models to mimic ground truth without modeling uncertainty, often resulting in blind guessing on tiny or unrecognizable objects in aerial scenes. In this paper, we present Aerial-R1, the first aerial MLLM framework to reinforce visual reasoning capabilities for aerial reasoning and segmentation. Drawing inspiration from the reasoning-incentivizing mechanisms of DeepSeek-R1, we find that trustworthy perception stems from consistency across views, establishing a visual parallel to the Chain-of-Thought in logic. To effectively adapt policy optimization for non-autoregressive mask generation, we introduce Hybrid-View Group Advantage-Weighted Regression (H-GAWR). This strategy constructs dynamic groups of high-resolution and low-resolution views, seamlessly bridging group-relative advantage estimation with advantage-weighted policy extraction. By enforcing consensus on clear inputs and strictly penalizing hallucinations on ambiguous ones, Aerial-R1 develops an explicitly incentivized refusal mechanism. Extensive experiments on VSAI-Ref, the first aerial MLLM benchmark dedicated to jointly evaluating dense reasoning and hallucination robustness, demonstrate that Aerial-R1 significantly outperforms SFT baselines in segmentation precision while substantially mitigating fatal hallucinations in low-information scenarios, paving the way for more reliable and trustworthy aerial agents. Codes are available on this https URL.

---


### 28. [Oddin: Latent Visual Reasoning in Unified Multimodal Models via Self-Distillation from Image Generation](https://arxiv.org/abs/2610.33062)

**<font color=#1a73e8>作者：</font>** Jaeyong Ko, Hankyeol Kim, Pilsung Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified large multimodal models (ULMMs) are able to perform visual reasoning through interleaved text-image generation, but generating explicit intermediate images incurs significant computational overhead. While visual latent reasoning addresses this, most existing methods rely on vision-language models (VLMs) incapable of visual generation. We propose Oddin, a novel framework enabling latent visual reasoning in ULMMs. Oddin replaces intermediate images with compact latent tokens processed entirely by the understanding branch, reserving the generation branch for the final output image. We train the model via offline self-distillation with three objectives, final image generation losses, text distillation losses, and cross-entropy losses for special tokens. Oddin surpasses interleaved generation baselines and closed-source VLMs on average across seven VBVR-Pro visual reasoning tasks. Qualitative analysis reveals that latent tokens attend to relevant regions in an input image, demonstrating that ULMMs can perform complex visual reasoning without generating intermediate images.

---


### 29. [OvisOCR3 Technical Report](https://arxiv.org/abs/2610.33066)

**<font color=#1a73e8>作者：</font>** Yu Xia, Yinglun Li, Yuhui Chen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce OvisOCR3, a 0.8B model for a broad range of OCR-related tasks. OvisOCR3 unifies document parsing, general OCR, key information extraction (KIE), document figure captioning, and cross-page table reconstruction in a single model. We train the model on real and synthetic data through continued pretraining and use domain-balanced mid-training to balance supervision across tasks with different data volumes and response lengths. Multi-teacher on-policy distillation transfers expertise from five domain-specific 4B teachers into the shared model, followed by mixed-task reinforcement learning with domain-specific rewards. We compare OvisOCR3 with general-purpose vision-language models and specialized OCR models on public and in-house benchmarks covering all five task families. In these comparisons, it achieves an overall score of 96.74 on OmniDocBench v1.6 and the highest overall scores on PureDocBench, Real5-OmniDocBench, and MDPBench. On OCRBench v2, it ranks first, scoring 65.9 and 61.3 on the English and Chinese splits, respectively. It also outperforms the baselines on OCRBench and all four KIE benchmarks. On DocFigCapBench, it achieves the highest localization F1 and a caption score close to that of Qwen3.8-Max. For cross-page tables, it leads in Relation F1 on CrossTabBench and truncated-table TEDS on MPDocBench-Parse. These results demonstrate that a compact 0.8B model can achieve strong performance across diverse OCR-related tasks. OvisOCR3 is available at this https URL.

---


### 30. [VLMProbe: An Open-source Library for VLM Probing and Interpretation](https://arxiv.org/abs/2610.33072)

**<font color=#1a73e8>作者：</font>** Gexin Huang, Haisheng Fu, Yanting Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding how vision-language models use visual information requires connecting internal representations to model behavior. We present vlmprobe, an open-source library that integrates lens readouts, attention attribution, causal interventions, and sparse autoencoder (SAE) analysis within a common model interface. Shared adapters, calibration and checkpoint utilities, evaluation pipelines, and visualizations support systematic analysis across architectures. Using this framework, we compare methods across vision-language, language, and vision models through matched case studies and controlled evaluations of pretrained sparse dictionaries. The comparisons show that representation readouts and spatial explanations depend on the analysis objective and observation site, and that local attribution estimates can disagree with measured intervention effects. SAE evaluations further expose distinct trade-offs in reconstruction fidelity, concept readout, and spatial localization. Together, these results support combining multiple forms of evidence to evaluate an interpretation. vlmprobe provides a reusable basis for selecting methods, comparing their conclusions, and testing hypotheses about model behavior. The code is available on this http URL

---


### 31. [AGQ: Action-Guided Ultra-Low-Bit Quantization for Vision-Language-Action Models](https://arxiv.org/abs/2610.33074)

**<font color=#1a73e8>作者：</font>** Xuhong Qiu, Zhuoyu Wu, Qiawei Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models enable robots to perform tasks specified through natural-language instructions, but their large weight footprint challenges deployment on memory-constrained onboard platforms. Ultra-low-bit quantization reduces this footprint, yet preserving task performance and controlling weight recovery costs remain challenging. We propose Action-Guided Quantization, which combines action sensitivity with a measured proxy for weight recovery cost to allocate matrix bitwidths under storage budgets. Per-channel calibration compensates for quantization error, while a uniform bitwidth within each matrix preserves regular layouts. Bit-dependent grouped lossless coding reduces resident weight storage, and block-wise recovery limits temporary buffers. On LIBERO, AGQ achieves 92.7% task success at W3, exceeding AWQ and GPTQ by 1.2 and 3.7 percentage points, respectively, and retains 70.5% success at W2.5. An asymmetric configuration, denoted W1.5$^{*}$, uses W4 vision weights and a parameter-weighted average of 1.5 bits for language weights. With lossless coding, it achieves $6.10\times$ complete-model compression relative to BF16 while retaining 25.5% task success. Code and experimental results are available at this https URL

---


### 32. [Diagnosing and Mitigating Evidence Misgrounding in Multimodal Knowledge Editing](https://arxiv.org/abs/2610.33075)

**<font color=#1a73e8>作者：</font>** Zhiwu Wang, Yichen Wu, Jinqian Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal knowledge editing aims to update visually grounded facts in Multimodal Large Language Models (MLLMs) while preserving unrelated text and visual behaviors. However, standard answer-level metrics can hide evidence misgrounding: an edit may produce the target answer on the original image yet remain sensitive to incidental context rather than the intended visual evidence. To examine this issue in a controlled setting, we construct WaterBird-Edit, an analysis set that decouples bird habitat labels from background context and measures whether edited predictions remain stable when the target evidence is preserved but the background changes. Motivated by this diagnosis, we propose VICE (Visual In-Context Editing), a retrieval-based framework that stores edits in external memory and applies them through visual in-context demonstrations designed to expose task-relevant evidence. Experiments on three standard benchmarks show that VICE achieves strong lifelong editing performance, while results on WaterBird-Edit show that it substantially reduces sensitivity to the controlled background shifts. Code and dataset are available in this https URL.

---


### 33. [Evaluating Visual Language Models on Visual Grounding for Visually Impaired People](https://arxiv.org/abs/2610.33078)

**<font color=#1a73e8>作者：</font>** Fairooz Azim, Lydia Achour, Claudia Borg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual grounding (VG) in visual question answering (VQA) is a fundamental capability of Vision-Language Models (VLMs), enabling the detection of the most relevant region in an image to answer the question. This reflects the model's capability of multimodal comprehension, which is crucial when interacting with visually impaired people (VIP). Indeed, visual grounding, when applied to assistive scenarios, is not merely a technical feature, but rather a trust and safety requirement. In this work, we study visual grounding in VLMs for visually impaired people. To this end, we assess open-source VLMs on visual grounding using the VizWiz-VQA-Grounding dataset and challenge, which contains real-life images taken by VIP. We propose VG-SHAP, which extends an existing explainability framework to provide visual grounding explanations, allowing the evaluation of black-box VLMs. Our results on the VizWiz-VQA-Grounding challenge show that despite generating correct answers, VLMs struggle to ground in the proper region in the image. However, these results are constrained by the quality of the segmentation model of our explainability framework and further research is necessary.

---


### 34. [IRON-Meme: A Benchmark for Structured Understanding of Identities and Roles in Online Meme Narratives](https://arxiv.org/abs/2610.33097)

**<font color=#1a73e8>作者：</font>** Gabriella Bollici, Stefano De Giorgis, Wouter Van Atteveldt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As polarization grows on social media, understanding how political memes shape online narratives has become increasingly important. Previous research has relied on either qualitative frameworks that are hard to scale or computational methods that lack theoretical grounding. Both approaches treat narrative categories in isolation and focus exclusively on moral portrayals of identity. To address these limitations, we introduce a framework grounded in social science theories, encompassing three categories: social identities (such as gender, politics, and ethnicity), viewpoints (ingroup and outgroup perspectives), and narrative roles (moral character, intelligence, status, and power). Building on this framework, we present IRON-Meme, a human-annotated benchmark comprising 1,110 political memes across substantially more templates than existing benchmarks. Our analysis of IRON-Meme shows that most memes assign derogatory roles and that identities, roles, and templates are systematically interconnected. Evaluation of nine vision-language models indicates that frontier-scale and reasoning models achieve the highest performance, while accuracy on social identities and narrative roles decreases for less frequent labels. Incorporating template background knowledge does not enhance narrative role classification, suggesting that meme interpretation relies on how memes are adapted for specific communicative purposes. We make IRON-Meme and our code publicly available.

---


### 35. [Prospect Theory in Large Language Models: A Meta-Analysis of Loss Aversion, Diminishing Sensitivity, and Probability Weighting](https://arxiv.org/abs/2610.33103)

**<font color=#1a73e8>作者：</font>** Adi Tarabeih  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prospect theory splits risky choice into three parts: loss aversion, measured by the relative weight of losses to gains, $\lambda$ (e.g., $\lambda = 2$ implies that losses weigh twice as much as gains), diminishing sensitivity to the size of outcomes (i.e., the curvature and linearity of the value function), and the nonlinear weighting of probabilities. I examined whether Large Language Models (LLMs) display the same properties as people by meta-analyzing 102 fitted estimates from 11 studies covering 32 language models. The three components emerge differently. Loss aversion is modest: the pooled $\lambda$ is 1.26 (95% CI 1.06 to 1.46), far below the strongest human meta-analytic estimate ($\lambda = 1.96$) and compatible with more conservative ones (1.07 and 1.31). Matched by design, LLMs are compatible with people when gains and losses are symmetric ($\lambda = 1.15$ against 1.07), but well below them when losses are smaller than gains (1.46 against 2.3), where human loss aversion is strongest. Value functions are close to linear rather than concave under the Tversky-Kahneman method (1.01, against a human value of 0.67), but more concave than in people under the Tanaka method (0.52, against 0.67), so diminishing sensitivity depends on how it is measured. Probability weighting shows a human-like inverse S shape ($\gamma = 0.81$ under Tversky-Kahneman and 0.84 under the Tanaka method), though on few studies. In sum, LLMs show little loss aversion and little diminishing sensitivity, but retain human-like probability distortion, yet these generalizations shift when looking at specific model families and fitting methods.

---


### 36. [VibeGame: Prompt-to-Game Development with AI-Native Engine and Self-Evolving Adversarial Agent Team](https://arxiv.org/abs/2610.33106)

**<font color=#1a73e8>作者：</font>** Wenbo Hu, Ken Li, Jiazhe Wei 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model agents have enabled software development through natural-language interaction, but extending this paradigm to end-to-end game development remains challenging. Building a playable game requires coordinating code, scenes, assets, animations, physics, and configurations, while allowing developers to validate their integrated behavior through interactive testing. We introduce VibeGame, a framework for creating complete 2D game projects from natural-language prompts and optional reference images. Its AI-native game engine represents project state as schema-validated structured text and provides frame-synchronous runtime control, enabling agents to inspect game states, execute actions, and verify behavior at their own pace. Built upon this interface, we design an Adversarial Agent Team of eight specialized agents to separate implementation from review, so that problems are found and fixed through multi-round loops. For each conducted and accepted project, we further introduce a training-free self-evolution mechanism to distill it into reusable skeletons, modules, and collaboration contracts for future development. We evaluate prompt-assets-to-game (PA2G), where agents are given an asset library, and prompt-to-game (P2G), where agents generate their own art. On a GameCraft-Bench subset, VibeGame in P2G consistently outperforms a range of agent harnesses in either P2G or PA2G with the same underlying model, including GPT-6.1-Sol.

---


### 37. [Conformance as a Distribution: Delegation Contracts, Error Budgets, and the Allocation of Evaluation Authority in Use-Based AI Regulation](https://arxiv.org/abs/2610.33112)

**<font color=#1a73e8>作者：</font>** John deVadoss  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Use-based AI regulation assigns obligations by deployment risk but lacks an evidentiary object to carry them. A benchmark score is a property of a model; conformance of a deployment is a failure rate under a declared distribution of contexts, bounded by a scope and subject to expiry. We take the delegation contract of earlier work (frozen configuration, scoped claim, executable revision rule) and study it under strategic play between a deployer, an auditor, and an enforcement point. We ask whether a declared context mixture can be made truthful; whether an audit can be unbiased against a system that detects evaluation traffic; whether a certification error budget can sustain a long-lived deployment; whether an aggregate audit can support a per-subgroup guarantee; and whether an incident metric that counts system failures but not fallback costs ranks arrangements correctly. For each we give a mechanism and a proposition: a proper-scoring penalty on the declared mixture bounds the excess failure of a best-responding deployer by $O(\lambda^{-1/2})$ in the penalty weight; a commit-reveal audit drawn from live traffic is unbiased by construction and grades the evaluator with the same sample; a halving error budget drives certification coverage below $(1-p)^n$ while $\alpha$-investing sustains it under a marginal false-certification guarantee; a per-subgroup guarantee costs audit size scaling as $1/m$ in subgroup mass; and any failure-only incident metric prefers withdrawal at every fallback cost, even when total loss ranks the arrangements oppositely. Five preregistered synthetic studies test each claim; no language model or production system is evaluated. Enforcement sits at distribution, capability-access, monetization and risk-transfer choke points, expiry of the conformance record is a standard of care, and conformance-as-a-rate is set against the EU AI Act's static conformity assessment.

---


### 38. [AOS-Bench: Can LLM Agents Manage Dynamic Workloads?](https://arxiv.org/abs/2610.33178)

**<font color=#1a73e8>作者：</font>** Erle Zhu, Genrui Zhang, Keyang Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents are moving from handling one request at a time to serving as persistent assistants to which users hand a stream of work: a build, a data-processing job and a bug fix may all be pending on the same machine at once. Such an agent must decide when to take on new tasks, how to delegate and overlap them, and how to stay within the machine's CPU and memory. Existing benchmarks cannot measure this, because they evaluate each task in isolation. We introduce \benchname{}, which evaluates an agent system as a workload manager: verified tasks arrive over time and must be delivered under shared CPU and memory limits, and the same tasks run one at a time serve as a per-system reference.
Across five model--harness pairs, isolated task success does not carry over evenly. On heavy workloads every system loses 13 to 23 points. On medium workloads, systems span 11 points in isolated success but 26 points in stream success, and two systems 0.6 points apart in isolation deliver 54\% and 68\% of the same tasks. Execution-policy interventions trace much of this gap to task intake: serial dispatch leaves 73\% of heavy-workload tasks unclaimed. Yet more elaborate management does not necessarily help. A fixed concurrency of two comes within four points of the best agent-managed policy on both medium and heavy workloads, and under every policy median CPU use stays below 30\% of the provisioned cores while tasks wait. These results identify workload management as a distinct capability for agents, and \benchname{} as a way to measure it.

---


### 39. [Propensities Please: Exposing Alignment-Faking LLMs using Synthetic Document Finetuning](https://arxiv.org/abs/2610.33180)

**<font color=#1a73e8>作者：</font>** Ardy Haroen, Florian Lorkowski, Samuel Nellessen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Alignment evaluations aim to assess whether large language models would engage in dangerous misaligned behaviour. Misaligned and evaluation-aware models might engage in alignment faking, where they pursue a hidden goal, but conceal this behaviour when they suspect effective oversight such as during training, evaluation or audited deployment. Such a model might view any prompt-based intervention that aims to reveal latent propensities as part of the evaluation, calling into question the reliability of existing alignment evaluations. Current methods for detecting alignment faking rely on chain-of-thought monitorability, highly realistic environments that reduce evaluation awareness, or mechanistic interventions, all of which are expected to become less reliable for future model generations. We present a method for revealing latent misaligned propensities that does not rely on any of these. We use synthetic document finetuning to teach models that misaligned actions will go undetected whenever certain keywords appear in the prompt. We place alignment-faking model organisms in environments that are clearly identifiable as honeypots and measure how their behaviour changes after finetuning. We observe that finetuning consistently widens the gap in misaligned action rates between prompts with and without the cue, indicating that finetuning allows exposing latent propensities more reliably than purely prompt-based methods. We argue that behavioural methods for detecting alignment faking and related behaviours are critical going forward, as models become more capable and less interpretable. We find that SDF often damages the models' reasoning capabilities and introduce a mitigation based on on-policy distillation.

---


### 40. [Spoofing the Toolbox: Optimizing Tool Descriptions to Deceive LLM Agents](https://arxiv.org/abs/2610.33182)

**<font color=#1a73e8>作者：</font>** Shih-Chieh Dai, Xinyu Sun, Guanhong Tao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are widely used in many applications and often rely on external tools. Tool information, such as function descriptions, helps agents determine which tools best suit a given context. However, attackers can manipulate this information to mislead LLM agents into using malicious tools. Prior attacks mainly rely on keyword-based techniques, which are easily detected, or rule-based methods, which have limited effectiveness. In this work, we introduce TSA, a stealthy tool-spoofing attack that crafts descriptions for malicious tools that are difficult to distinguish from those of existing benign tools. To achieve this, we propose an LLM-powered optimization method that iteratively refines malicious tool descriptions. Specifically, TSA begins with a variant of a benign tool description and updates it based on feedback from a surrogate LLM agent. The optimization method incorporates a feedback function and contrastive in-context learning to guide the search for descriptions that are both stealthy and effective. Experiments on both single- and multi-tool use benchmarks demonstrate that TSA achieves an attack success rate of up to 92.13\%, outperforming four state-of-the-art approaches while remaining highly stealthy. Our user study further shows that even human participants cannot distinguish descriptions generated by TSA from benign ones. Moreover, TSA remains effective against five tool-malware detectors.

---


### 41. [Position, Role or Label? A Controlled Study of Instruction Conflicts in LLM Agents](https://arxiv.org/abs/2610.33201)

**<font color=#1a73e8>作者：</font>** Anish Laddha, Nitesh Pradhan, Gaurav Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents take instructions from the operator, repository configuration, user, tool results and saved memory, which often conflict. Instruction-hierarchy benchmarks ask whether the higher-ranked source wins, but a source sets position, role and label at once. First, we build WhoWins, 1,080 code-scored scenarios in five task types, each with up to five mutually exclusive instructions, and seven controlled experiments that vary only how instructions are delivered. Second, we study 14 open-weight models (0.6B to 122B, thinking off and on) over 1,887,356 scored replies, checking main findings on held-out scenarios. Inside one message the first of two conflicting lines wins 72.42 to 94.66%, and across messages it keeps 22.95 to 62.65%. A policy sent first in the system (or developer) message loses most conflicts with later lines in every Qwen model but wins most on gpt-oss when it acts. In tool and file-write tasks it wins less often than the same text sent first as a labelled user message, in every model-mode. Third, we test whether pairs forecast larger conflicts; forecasts improve in every model-mode once they know where the task line is. Finally, by our keyword patterns at most 2.92% of decided pair replies flag or hedge a conflict.

---


### 42. [Of Chains and Gains: What Reinforcement Learning changes on Reasoning-based Image Quality Assessment](https://arxiv.org/abs/2610.33203)

**<font color=#1a73e8>作者：</font>** Yixuan Li, Yuxuan Jiang, Hanwei Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has improved the performance of large Vision-Language Models (VLMs) on image quality assessment (IQA). Existing approaches often attribute these gains to improved reasoning before scoring, supported by increasingly plausible Chain-of-Thought (CoT). However, whether these gains exceed sampling effects and how they depend on explicit reasoning remain unclear. We rigorously investigate these questions through sampling-aware evaluation, controlled reasoning interventions, and shortcut experiments. We find that RL-trained models outperform base models under large-budget $\operatorname{max}_g@k$ evaluation, while improvements beyond averaging are concentrated in-distribution. RLVR produces chains that raise base-model performance when transplanted and improves scoring with the chain held fixed. Yet scoring becomes less dependent on the chain during inference, more clearly at 7B than at 32B. Steering the probed quality direction in thinking tokens also has little effect on scoring. Finally, RL can improve scoring accuracy by exploiting textual cues correlated with mean opinion scores (MOSs), which could inflate benchmark performance. Together, these findings show that RLVR raises quality scoring and produces more useful chains, but that better scoring does not imply a stronger reliance on explicit reasoning, while score-based rewards can also encourage reliance on quality-irrelevant shortcuts. We hope this preliminary study can enlighten more and more concrete reasoning schemes in IQA.

---


### 43. [Scaling Qualitative Analysis with Large Language Models: Development and Validation of the Smart Coder Framework for Human-LLM Collaborative Coding](https://arxiv.org/abs/2610.33205)

**<font color=#1a73e8>作者：</font>** Cheng Tang, Kun Wang, Yaxuan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current uses of large language models (LLMs) for qualitative coding often rely on ad hoc prompting with limited guidance for reliability and human oversight. To address these limitations, we propose the Smart Coder Framework, a three-phase approach structuring human-LLM collaborative coding through Instruction, Prompt Strategy, and Reliability Check. We evaluated the framework using 72 middle-school mathematics teacher interview transcripts and a human-consensus benchmark. A factorial design compared instructed versus uninstructed prompts, few-shot versus few-shot plus chain-of-thought prompting, and single-pass versus self-consistency coding. Twelve transcripts were used for prompt development and calibration, and 60 for the formal evaluation. In the results, instruction consistently improved agreement. Chain-of-thought further improved agreement under adequate instruction, and self-consistency produced smaller, theme-dependent gains but helped identify unstable decisions for human review. Performance also varied by transcript characteristics. Overall, the framework systematically structures and monitors LLM-assisted qualitative coding while preserving human authority over coding decisions.

---


### 44. [Vision Token Pruning via Query-Vision Interaction Decomposition](https://arxiv.org/abs/2610.33215)

**<font color=#1a73e8>作者：</font>** Harshithanjani Athi, Sravan Kumar Ankireddy, Jianzhong Charlie Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (VLMs), which process both visual inputs and text queries, incur high inference costs due to the large number of visual tokens, making visual token pruning a natural approach for improving efficiency. Recent work has leveraged query information to guide token selection, often through heuristics derived from attention patterns or token dynamics. However, these approaches do not explicitly exploit the underlying structure of query-vision interactions. We address this gap by observing that the query-vision interaction matrix, naturally induced by the query and key projections already present in transformer attention, is effectively low-rank, with a small number of dominant latent interaction modes capturing query-relevant semantics. Motivated by this observation, we propose Query-Vision Decomposition (QViD), a novel training-free query-aware visual token pruning method that exploits this structure. Extensive experiments on both image and video understanding benchmarks show that QViD consistently improves performance under matched token budgets, with the largest gains appearing under aggressive compression regimes.

---


### 45. [Neyman Orthogonal Activation Steering](https://arxiv.org/abs/2610.33217)

**<font color=#1a73e8>作者：</font>** David Arbour, Erfan Jahanparast, Serina Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering is a popular approach for shifting LLM output toward a desired behavior, and increasingly for generating realistic synthetic data. The standard recipe estimates a steering direction by contrasting LLM activations on prompts with and without a target concept, such as truthfulness. In this paper, we separate the estimand (the steering direction these methods target) from the estimator used to recover it, two notions the literature often conflates. We frame nearly all existing methods as plug-in estimators of the average gradient of an outcome regression, with the binary contrastive label fixed as the outcome. Using this framing, we can immediately incorporate flexible modeling approaches and extend existing methods to allow for continuous outcomes such as log-probabilities or oracle ratings. Flexible ML models that fit the outcome well, however, might not estimate the gradient well, which motivates estimators that target the gradient directly. Drawing on the debiased machine learning literature, we develop a complementary estimator built on the Stein score, the Riesz representer of the gradient functional. Combining the two routes gives an orthogonalized estimator with classical double-robustness properties. We illustrate the framework on activation steering applied to a number of benchmark datasets.

---


### 46. [Each Insufficient in Its Own Way: Calibrating Language Models Across Varying Evidence States](https://arxiv.org/abs/2610.33237)

**<font color=#1a73e8>作者：</font>** Jiayi Li, Dennis L. Shung, Bradly C. Stadie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How can a language model know whether it has enough evidence to answer? Language models tend to answer even when the evidence they have is insufficient. Deciding whether to answer or gather more evidence requires a calibrated estimate of how likely an answer is to be correct with the available evidence. However, most calibration work treats the input as fixed, without asking how this estimate should change with the evidence. We introduce \emph{evidence-state calibration}, which requires a model's confidence before answering to match its probability of answering correctly and to change accordingly whenever the evidence changes this probability. We propose \ours{} (\textbf{Suffi}ciency \textbf{C}onfidence \textbf{E}stimation), which fine-tunes the confidence already present in a model's next-token distribution to match how often the model answers correctly from each evidence state. Across clinical diagnosis and multi-hop question answering with four models from two families, \ours{} reduces the Brier score by up to 60\% and increases AUROC by up to 0.16. Its confidence matches the empirical success rate and responds not only to the amount of evidence but also to which evidence is present, showing that models can learn to judge whether their current evidence is enough to answer.

---


### 47. [Hey, guess what: CUES lead to inferences about typicality](https://arxiv.org/abs/2610.33239)

**<font color=#1a73e8>作者：</font>** Alison Chi, Sanghyeok Choi, Hannah Rohde 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Throughout life, we accumulate knowledge of how typical certain events are. We use this knowledge in daily conversation, often interpreting meaning beyond what has been said explicitly. In this work, we take steps to better understand this meaning recovery, investigating both atypicality and typicality inferences. First, we construct two corpora, EventTyp and the human-validated EventTypGold. We conduct large-scale human and LLM experiments and find that for humans, three CUES predict inferences about typicality: Commonsense Knowledge, Utterance Emphasis, and Snark. However, in most experimental settings, we find that LLMs lack the prerequisite Commonsense Knowledge necessary to accurately assess an event's general typicality, and therefore struggle to follow these CUES.

---


### 48. [AdaPRA: Process Reward Agents with Adaptive Rubrics for Data Science](https://arxiv.org/abs/2610.33245)

**<font color=#1a73e8>作者：</font>** Atharva Naik, Vivek Chari, Pol Llado 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data science agents can automate end-to-end machine learning workflows, yet they remain far from competitive on human leaderboards. Agents make process errors such as insufficient exploration, unsound validation, coding bugs, and poor use of a fixed budget (re-running the same exploratory data analysis and baseline models in every attempt). We propose AdaPRA to address these issues: a persistent coding agent harness that accumulates knowledge across attempts on the same task, with rubric-guided process supervision that identifies and corrects errors. Our process reward agent audits the agent's trajectory and workspace by executing checks, and adapts its rubrics to each task. We find that rubrics seeded from easier tasks generalize to harder tasks, with rubric adaptation further improving performance. With five attempts per task, AdaPRA improves an 80B Qwen model's leaderboard percentile by 24.5 points on DSPredict-Easy and 14.8 points on DSPredict-Hard while reducing process errors. We also show that supervision with rubrics mined from one base model's runs improves another (DeepSeek-V3.2), and that AdaPRA beats DataPRM, a competitive PRM for data science. We also share our code for reproducibility.

---


### 49. [Two Uncertainties Are Not One: Disagreement versus Decision-Risk in Cheap Structured Content Moderation](https://arxiv.org/abs/2610.33258)

**<font color=#1a73e8>作者：</font>** Karan Yadav  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Content moderation compresses a graded, contested human judgment into a binary act (leave up / take down) over billions of items, at a scale where running a frontier LLM on every post is uneconomical. A new class of frozen "System One" models returns typed, calibrated decisions instead of text at ~USD 0.000025 per call and ~100 ms. We run the first independent audit of one such model on 142,658 human-labeled comments, and benchmark it against 14 frontier reasoning models (the GPT-5.x, Claude, Gemini 3, and Grok families) on a shared probe set. Two findings stand out. First, the cheap model is accuracy-competitive: its zero-shot classification AUROC (0.83) is not statistically separable (paired bootstrap, n=56; a failure to reject parity, not proof of equivalence) from 13 of the 14 frontier systems while costing 1-3 orders of magnitude less, and it is no worse calibrated than several of them. Second, "confidence" conflates two uncertainties that come apart: human disagreement (where annotators split on satire and coded language) and decision risk (where the automatic action is costly-wrong). Under an asymmetric moderation loss these call for opposite escalation signals, so no single confidence number serves both. Because the model prices extra questions at nearly zero, decomposing the judgment into parallel sub-questions and reading their spread recovers a human-disagreement signal that the model's native confidence misses -- but this remedy is specific: it helps the weakest, disagreement-blind models and only when the decomposition aligns with the sources of disagreement; a specialist toxicity model and the strongest LLMs do not need it, and the effect is distribution-sensitive. We will release the instrument, the cached runs, and the analysis.

---


### 50. [Image Clustering with Vision-Language Model Embeddings](https://arxiv.org/abs/2610.33265)

**<font color=#1a73e8>作者：</font>** João P. Matos-Carvalho, Nuno Fachada  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained vision-language models provide image representations whose suitability for clustering may vary with feature extraction, image domain, and partitioning algorithm. We compare nine representation pipelines across seven image benchmarks and four clustering configurations, yielding 252 baseline combinations. Eight pipelines extract visual features, including two vision-only references; the ninth generates descriptions and embeds the resulting text. With agglomerative clustering (Ward linkage) fixed, Qwen3-VL achieves the highest adjusted Rand index (ARI) on five datasets, including 0.925 on MNIST, while BLIP-2 leads on CIFAR-10 and CIFAR-100 with ARIs of 0.925 and 0.591, respectively. A separate sensitivity analysis compares raw and L2-normalized embeddings at their original dimensionality across all 63 dataset-representation pairs. Normalization preserves the highest-ARI representation in every dataset, increases ARI in 35 pairs, decreases it in 26, and leaves two numerically unchanged. On the SVHN dataset, the highest ARI remains low, rising from 0.097 to 0.098 after normalization. The evaluated caption-mediated pipeline obtains relatively high ARI on isolated digits but does not consistently exceed direct visual features. These findings support selecting and evaluating complete representation-clustering pipelines for the intended domain, with explicit attention to extraction and normalization choices.

---


> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-418](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
