# 🧠 大模型相关研究 | 2026年10月09日

> 本类共 **266** 篇论文：已确认 **245** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 1. [Adaptive Workflow Intelligence: A Cognitive Architecture for Context-Driven Enterprise Automation](https://arxiv.org/abs/2610.08793)

**<font color=#1a73e8>作者：</font>** Sreedevi Pandiyath Viswambaran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise systems increasingly rely on automated workflows, yet many AI-driven solutions remain brittle under non-stationary conditions, evolving policies, and delayed operational feedback. While reinforcement learning and large language model (LLM) agents offer partial adaptability, they do not by themselves provide persistent reflection mechanisms or straightforward integration with policy-constrained enterprise operations. This paper introduces Adaptive Workflow Intelligence (AWI), a cognitive architecture for context-driven enterprise agents organized around a four-layer Perception-Cognition-Action-Reflection (PCAR) loop. AWI treats reflection as a mechanism for continuous policy refinement and combines hybrid reasoning with reflective memory and feedback-driven adaptation to support decision making under environmental drift and operational constraints. We evaluate AWI in a simulated enterprise decision workflow characterized by delayed outcomes and a controlled regime shift. In a drift-and-delay stress test, guardrail-constrained adaptive approaches recover more rapidly than static automation while maintaining policy compliance. Within this setting, AWI's reflective components modestly reduce behavioral oscillation and feedback variance, illustrating the stability-agility trade-off introduced by reflective policy adaptation.

---


### 2. [Tokka-Bench: Evaluating Tokenizers Across 100 Natural and 20 Programming Languages](https://arxiv.org/abs/2610.08794)

**<font color=#1a73e8>作者：</font>** Ben Gubler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models rely on subword tokenizers whose quality varies across languages, yet no standardized multi-metric framework exists for broad comparative evaluation. We introduce Tokka-Bench, an open-source framework that evaluates tokenizers on five complementary metrics -- bytes per token, unique token coverage, subword fertility, word-split rate, and vocabulary composition -- across 100 natural languages (30+ scripts) and 20 programming languages, using language-aware segmentation adapted to each writing system. Comparing seven BPE tokenizers (GPT-2, GPT-4, gpt-oss, Llama 3.1, Gemma 3, Qwen3, and Kimi K2) within individual languages, we find that vocabulary allocation strategy matters more than raw vocabulary size, and that programming-language efficiency has converged among recent tokenizers despite divergent natural-language profiles. The framework, data, and interactive dashboard are publicly available.

---


### 3. [KVFetch: Temporal Prefetching for the Missing Half of KV Cache Compression](https://arxiv.org/abs/2610.08811)

**<font color=#1a73e8>作者：</font>** Linfeng Dong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As context windows scale to tens or hundreds of thousands of tokens, KV cache compression has become essential for efficient LLM inference. Existing methods fall into three families: score-based eviction, summary compensation, and offload-and-recall. Yet all three decide what to keep or recall by content relevance to the current query. We show this shared design is structurally incomplete. A cache supports two access modes: associative lookup by content and sequential traversal by position; current compressors implement only the first. The gap matters in practice: retrieval-augmented generation, code completion, and structured-data extraction all require the model to reproduce identifiers, field values, or code tokens verbatim from the context. Under compression, content-based eviction retains the head of such a sequence but discards its continuation, causing verbatim copying to break irreversibly midway, a failure we call sequential forgetting. This failure resists better scoring, larger budgets, summary compensation, and dynamic re-scoring; it is the dominant source of remaining quality loss under compression. We propose KVFetch, a training-free, drop-in framework that opens a temporal recall channel for any score-based compressor. It demotes evicted candidates to a quantized cold tier, detects active copying through a monotone read pointer, and prefetches positional successors into fixed-size hot-tier slots without increasing attention cost. On RULER-16K under an iso-budget control, KVFetch recovers verbatim copying from 0.8 to 78.4 and raises the 13-task average by +8.4, with gains concentrating on tasks that require sequential access. On LongBench, where no task requires sequential access, the channel remains dormant and imposes no cost.

---


### 4. [Pre-training, Reasoning, Benchmarking: X-ray Report Generation on CheXpert Plus Dataset](https://arxiv.org/abs/2610.08813)

**<font color=#1a73e8>作者：</font>** Xiao Wang, Yuxiang Zhang, Dan Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> X-ray image-based Radiology Report Generation (RRG) constitutes a critical research direction within medical artificial intelligence, with great potential to alleviate clinicians' diagnostic workload and shorten patient waiting periods. Despite substantial advances over recent years, the field faces evident bottlenecks stemming from insufficient standardized benchmarks and inadequate domain adaptation of generic large models. Notably, the newly released CheXpert Plus dataset is provided without accompanying baseline implementations and evaluation results, which impedes standardized training, quantitative evaluation and fair comparison among follow-up algorithms. To mitigate this limitation, we establish a comprehensive benchmark encompassing prevailing X-ray report generation models and Large Language Models on CheXpert Plus. This benchmark delivers a reliable comparative foundation for upcoming methods and enables researchers to rapidly identify state-of-the-art approaches within this domain. Beyond benchmark construction, we rethink X-ray RRG under the paradigm of large models and propose a novel framework termed MambaXray-PRB. Our framework improves report generation performance and enhances model interpretability via multi-stage large-model pre-training and multi-modal Chain-of-Thought reasoning. The pipeline consists of three successive phases: self-supervised auto-regressive modeling, X-ray-report contrastive learning, and post-training optimization for reasoning and report generation. Extensive experiments on IU X-ray, MIMIC-CXR, and CheXpert Plus datasets validate the effectiveness of MambaXray-PRB for radiology report generation. The source code of this paper is available on this https URL

---


### 5. [Route-Verify-Vote: Procedure-Conditioned Self-Consistency for Mixed-Domain Reasoning](https://arxiv.org/abs/2610.08814)

**<font color=#1a73e8>作者：</font>** Xinchen Xiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compositional generalization remains challenging when language models must combine familiar reasoning operations in unfamiliar ways. The Scenario-Based Commonsense Reasoning Evaluation (SCoRE) 2026 tests this ability on three mixed domains absent from training and requires models to identify the complete set of correct options for each question.
We introduce Route-Verify-Vote (RVV), a framework for procedure-conditioned self-consistency that uses language models without parameter updates. Route uses the provided domain label to select a reasoning procedure that guides the model in representing and applying the relevant constraints. Verify prompts the model to assess each option against those constraints. Vote aggregates complete answer sets and allocates additional samples to questions with a small vote-count margin between the two most frequent sets. Samples for each question follow the same domain-specific procedure.
On the official test set, voting over 16 sampled answer sets per question achieves an exact-set accuracy of 74.6%. Adaptive RVV reaches 77.3%, and combining models on selected domain routes raises accuracy to 79.4%. The final system ranked second among participating systems. These results support domain-specific reasoning procedures and answer-set disagreement as useful tools for allocating inference-time computation in mixed-domain reasoning.

---


### 6. [Just for FUNS: LLM-Guided Spatio-Temporal Graph Node Generation for Forecasting Unobserved Node States](https://arxiv.org/abs/2610.08818)

**<font color=#1a73e8>作者：</font>** Shuhao Li, Weidong Yang, Changan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal forecasting is a cornerstone of logistics, urban planning, and intelligent transportation systems. However, constrained by deployment costs and maintenance resources, sensor networks often lack comprehensive spatial coverage, rendering Forecast Unobserved Node States (FUNS) a critical yet formidable challenge. Conventional models rely on historical observations and typically falter when encountering nodes without prior records. To address this, we redefine the problem as a conditional generation task on spatio-temporal graphs and propose GenST, a framework that introduces Large Language Models (LLMs) as a semantic bridge, leveraging a pre-trained LLM fine-tuned to extract rich semantic features from node descriptions, such as functional zones and road network structures, to compensate for missing spatio-temporal signals. Specifically, we design a two-stage generative architecture: a Spatio-Temporal VAE first compresses spatio-temporal dynamics into a latent space, followed by a Generative Transformer (GenT) that reconstructs the future states of unobserved nodes from noise, guided by multi-modal conditions including semantics, geographic coordinates, and neighborhood contexts. Experiments on six traffic and two non-traffic datasets show GenST significantly outperforms existing baselines in zero-shot prediction tasks, demonstrating the practical potential of semantic-guided generation for mitigating spatio-temporal data sparsity.

---


### 7. [Task-Oriented Key-Layer KV Communication for Efficient Latent Multi-Agent Collaboration](https://arxiv.org/abs/2610.08820)

**<font color=#1a73e8>作者：</font>** Dongsen Zhang, Peipei Li, Zekun Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model-based multi-agent systems improve complex problem solving through collaboration, while latent communication directly transmits model internal states to avoid the high inference costs of natural language. However, existing KV-based latent communication methods prioritize sender-side state fidelity, leading to substantial communication and computation overhead and potentially introducing redundant information. To address these limitations, we revisit latent communication from a task-oriented perspective, shifting its objective from sender-side state fidelity to receiver-side task sufficiency. Under this formulation, we propose KITE, a training-free framework for task-oriented key-layer KV communication. KITE identifies a task-effective key layer using a receiver trajectory distortion criterion, transmits only the latent working memory associated with the key layer, and further uses the same layer as the entry point for autoregressive latent reasoning. Experiments on seven benchmarks across two model families and three model scales show that, compared with full-layer KV communication, KITE reduces communication volume by 28-36$\times$, achieves up to 3$\times$ end-to-end inference speedup, and improves accuracy by up to 23.3 percentage points.

---


### 8. [Emo-Jev: Probabilistic Reasoning for Emotion Classification with Jev](https://arxiv.org/abs/2610.08829)

**<font color=#1a73e8>作者：</font>** Yazhou Zhang, Junhao Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Jev offers an alternative interface for language understanding: given an input and predefined questions, it returns probabilistic decisions rather than free-form responses. Whether this interface can support effective reasoning for text classification against leading LLMs remains an open questions. We introduce Emo-Jev, a training-free framework with two complementary implementations. Emo-Jev-D decomposes classification into task-specific atomic judgments and composes their probabilities into a final prediction. Emo-Jev-SC constructs multiple judgment paths from complementary perspectives and aggregates their predictions into a consensus decision. We evaluate Emo-Jev on eight datasets spanning sentiment analysis, emotion recognition, sarcasm detection and humor detection, comparing against direct Jev classification and five SoTA LLMs under input/output and chain-of-thought reasoning. Standard Jev achieves 62.93\% average macro-F1 versus 67.28\% for the strongest LLM baseline, with lower observed latency and generally lower cost.

---


### 9. [MoR-MLLM: Mixture of Recursions for Efficient Multimodal Large Language Models](https://arxiv.org/abs/2610.08830)

**<font color=#1a73e8>作者：</font>** Pengcheng Zheng, Chaoning Zhang, Jiaxin Yan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated remarkable reasoning capabilities across vision and language tasks. However, their massive computational and memory demands hinder real-world deployment. While recent efforts reduce costs by employing lightweight language backbones, existing paradigms remain computation-dense due to their static sparsity and depth allocation, which cannot adapt to the semantic complexity of each token. To this end, we propose MoR-MLLM, a computation-sparse MLLM based on the recent Mixture-of-Recursions (MoR) framework. MoR-MLLM introduces adaptive per-token recursion, allowing the model to dynamically adjust its recursive depth and allocate more computation to visually or linguistically challenging tokens while skipping redundant operations for simpler ones. To stabilize the training of recursive sparsity in multimodal settings, we further design a three-stage MoR-Tuning strategy and an entropy-regularized loss to encourage diverse routing distributions. Extensive experiments show that compared with recent advanced tiny MLLMs, our proposed MoR-MLLM can greatly reduce the training memory and computation complexity while retaining high performance on various vision-language tasks.

---


### 10. [CoDR: Training-Free Confidence-Drift Remasking for Diffusion Language Models](https://arxiv.org/abs/2610.08833)

**<font color=#1a73e8>作者：</font>** Yue Wu, Qinghe Zhang, Yu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (MDLMs) decode by repeatedly committing tokens to masked positions, but these commitments are usually irreversible. A token chosen under sparse, partial context is kept fixed, even when later context no longer supports it. Existing samplers mainly decide when to commit a token, but rarely check whether an already committed token should still be kept, allowing early mistakes to propagate. We trace this issue to confidence drift, where the model's confidence in a committed token drops from its sparse commit-time context to the denser context available later. Based on this signal, we propose CoDR (Confidence Drift Remasking), a training-free and sampler-agnostic refinement pass. CoDR estimates drift for all committed positions in only k forward passes via k-partition probing, then remasks and regenerates only the tokens the model no longer endorses. Across two backbones, four reasoning and coding tasks, and three base samplers, CoDR improves average accuracy across all evaluated model-sampler configurations and improves most individual task settings with modest overhead. Controlled experiments show that the gains come from targeted confidence-drift remasking rather than extra compute alone, and that CoDR uses far fewer forward passes than prior remasking methods. Code is available at this https URL.

---


### 11. [Leveraging LLM-Generated Explanations for Detecting Emotionally Rewritten Fake News](https://arxiv.org/abs/2610.08835)

**<font color=#1a73e8>作者：</font>** Yupei Guo, Jiajun He, Xiaohan Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The spread of fake news may cause severe social consequences. Existing fake news detection methods mainly focus on stylistic variations or incorporate external information such as explanations. However, news articles are often rewritten under different emotional backgrounds while preserving their underlying factual claims, which may affect the robustness of detection models. In this work, we investigate fake news detec- tion under fact-preserving emotional variations. To study this problem, we construct emotion-rewritten test sets and generate explanations from the original news articles as stable background knowledge. We then propose a Gated Cross Attention (GCA) framework that adaptively integrates emotionally rewritten news with the corresponding explanations, enabling the model to focus on informative explanation content while reducing potential mismatches caused by emotional reframing. Experiments on PolitiFact, GossipCop, and LUN demonstrate that the proposed method achieves notable improvements under multiple emotional conditions on PolitiFact and LUN, while maintaining competitive performance on GossipCop. We further analyze the effects of explanation guidance and gating mechanisms under different emotional conditions. Our code and data are available at: this https URL gca .

---


### 12. [Beyond the Sycophancy Score: How Task, Model, and Pressure Shape LLM Yielding](https://arxiv.org/abs/2610.08840)

**<font color=#1a73e8>作者：</font>** Guang Yang, Homa Hosseinmardi, Fengchen Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often abandon a correct answer, or endorse a user's position, once the user pushes back. This behavior, called sycophancy, is usually reported as a single rate per model, which says little about when it happens or how a user can avoid it. We study the conditions that produce it with 103,939 graded replies from ten configurations: eight LLMs with reasoning disabled, and two of them again with maximum reasoning, all facing the same 200 items, 13 pressure conditions, and four-turn conversations, with every reply labeled by two independent LLM judges. We find that the dominant factors are how costly it is for the model to verify the user's claim, and whether a trained guardrail covers it. Removing this task factor from a logistic model costs 0.485 of McFadden $R^2$, against 0.139 for model family and 0.009 for pressure tactic. Anchored facts are almost never conceded (1.3%), while adoption on logic puzzles rises with the number of clues needed to refute the pushed answer. Personal choices are endorsed in 77.0% of conversations. Most concessions on hard items come from models that cannot reliably solve them; models that can solve them rarely give the answer up. For both models tested, maximum reasoning removes these concessions completely: adoption on deep puzzles falls from 19.2% and 12.5% to 0%. Fallacious or emotional framing adds nothing beyond plain repetition. Three human annotators agree with the judges' consensus on 118/120 calibration items. These results give practical rules for reliable use: simplify hard-to-verify problems and reason deeply, state the question rather than one's preferred answer, ask for evidence on open questions, and choose models by their measured guardrail profile.

---


### 13. [QuanLing: Cross-Branch Validation of Language Distance Quantification on Western Romance](https://arxiv.org/abs/2610.08851)

**<font color=#1a73e8>作者：</font>** Yiping Bai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantifying language distance among closely related languages remains a core challenge in quantitative linguistics. Our previous work [1] introduced QuanLing (Quantitative Linguistics via Pretrained Language Models), a quantitative framework combining language distance metrics (sentence embedding distance, tokenization fragmentation rate) with language property analysis (MLM prediction probability), validated on North Germanic (Danish, Norwegian Bokmål, Swedish). This paper extends QuanLing to Western Romance--French, Portuguese, Spanish, Italian--testing cross-branch applicability with the same metric family and aggregation protocol as our North Germanic study, adapted for four languages (English anchor, quadruplet construction). Using 150 four-language parallel sentences, we compute LaBSE sentence embedding distances, tokenization fragmentation rates from four monolingual BERT tokenizers, and mBERT masked language model mutual intelligibility. Results show that Portuguese--Spanish are closest (LaBSE distance 0.0229), French--Italian most distant (0.0338); LaBSE and mBERT rankings agree on 4 of 6 pairs, confirming cross-model robustness. Western Romance shows a wider absolute distance span than North Germanic (0.011 vs. 0.008) but comparable relative ratios (1.48 vs. 1.67), consistent with longer divergence time. French exhibits notably higher MLM predictability (36.12% top-1 accuracy vs. 29.28% for Italian), reflecting its orthography--phonology decoupling. This cross-branch validation provides further evidence for QuanLing's generalizability beyond a single language branch.

---


### 14. [LRCC: Generalizing Low-Rank Compression with Conditional Computation](https://arxiv.org/abs/2610.08858)

**<font color=#1a73e8>作者：</font>** Thomas Vaitses Fontanari, Maximo Eduardo Rulli, Federico Alvetreti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-rank compression reduces the cost of pretrained language models by replacing linear transformations with low-rank factorizations. However, conventional methods use a fixed rank allocation during inference, assigning the same amount of compute regardless of the input token. We introduce Low-Rank Conditional Computation (LRCC), which adds token-dependent computation to pretrained models by training one lightweight router per Transformer block to select among a small set of nested low-rank paths. During training, the low-rank factors remain frozen, and only the routers are optimized. We evaluate LRCC on Llama and Qwen models for language modeling and zero-shot downstream tasks. Within the same average active-parameter budget, LRCC improves the predictive performance over static low-rank compression, including a 7.6 percentage-point gain in average downstream accuracy on Llama-2-7B over static methods. At matched batch-size-1 decoding latency, LRCC improves both perplexity and downstream accuracy on Llama-3.2-1B and remains competitive on Llama-2-7B, without specialized kernels. Finally, we assess the usefulness of assigning a token-wise path by analyzing the routers' path choices.

---


### 15. [CredLeakBench: Evaluating Credential Leakage and Recovery in LLM Agents](https://arxiv.org/abs/2610.08871)

**<font color=#1a73e8>作者：</font>** Rafid Ahmed, Joseph Fioresi, Mubarak Shah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Language model agents are increasingly deployed to automate everyday digital chores from managing emails and social media to handling banking and bills allowing users to step away from supervision. However, this capability also exposes sensitive information to phishing. Safe execution requires distinguishing malicious requests from genuine ones without simply refusing to act. Despite its practical importance, this problem remains underexplored and it is unclear whether current agents or existing defenses can achieve it. To study this problem, we first propose CredLeak-Bench, a comprehensive benchmark designed to evaluate how effectively and securely agents automate human workflows when confronted with phishing and identity verification. The benchmark covers both user-directed authentication and autonomous inbox monitoring, where agents are not explicitly instructed to log in. It systematically varies deceptive cues and pairs phishing scenarios with legitimate counterparts, enabling joint evaluation of information leakage and utility on genuine tasks. Within a sandboxed environment, leakage is measured through actual submissions of information rather than agents' self-reported behavior. Our evaluation reveals that all tested models are vulnerable to leakage. Agents also disclose sensitive information during autonomous inbox monitoring, demonstrating that phishing can induce disclosure without a user request to authenticate. Furthermore, most evaluated mitigations that reduce leakage also impair performance on genuine tasks, exposing a security utility trade off in existing defenses. These findings show why reducing leakage alone is insufficient: effective defenses must prevent unauthorized disclosure while preserving legitimate task completion. CredLeak-Bench provides a controlled framework for measuring both objectives and evaluating progress toward secure, useful agents.

---


### 16. [An Empirical Study of Agent Skills' Downstream Utility](https://arxiv.org/abs/2610.08875)

**<font color=#1a73e8>作者：</font>** Yu Cheng, Dehai Zhao, Zhongxin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent Skills package procedural guidance and resources for reuse, but a relevant Skill does not necessarily improve task performance. Existing studies characterize Skill content and evaluate downstream performance, yet provide limited explanations of how utility depends on content, execution configuration, and multi-Skill organization. We conduct an empirical study on 87 SkillsBench tasks, defining downstream utility as the pass-rate difference from No-Skill on the same tasks under the same model--harness configuration. We compare the same Skills across nine configurations, then examine alternative published Skills and organizations of fixed Skill sets under three selected configurations. We retrieve marketplace candidates from a curated corpus of 37,596 Skills. LLM-assisted analysis of content, execution traces, and final artifacts, followed by author review, relates provided support to actual use and task outcomes. The same Skills help some configurations and hurt others on 36.78\% of tasks, with trajectories showing that recommended procedures can become an execution burden. Relevance rankings overlook more useful candidates. Within the evaluated candidate sets, reranking by support for required operations raises first-choice pass rates by 4.35--5.80 percentage points across the three configurations. We derive 17 authoring practices linking executable procedures to recovery, preservation of task requirements, and checks on final artifacts. Stage Plan and Dependency DAG outperform use order alone, with DAG's additional benefits concentrated in tasks supplied with five or six Skills. These findings guide developers to assess usable operation support, allow procedure adaptation while preserving task requirements, and make artifact dependencies explicit when organizing Skills.

---


### 17. [Tiny-Scale Chinese BERT Pretraining: A Controlled Comparison of MLM, WWM, and MacBERT Strategies](https://arxiv.org/abs/2610.08879)

**<font color=#1a73e8>作者：</font>** Yiping Bai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pretraining strategies significantly impact the quality of language models, yet existing comparisons of Masked Language Modeling (MLM), Whole Word Masking (WWM), and MacBERT-style replacement have focused primarily on base-scale models (>=110M parameters). This paper presents a controlled comparison of these three strategies on a tiny-scale Chinese BERT model (4 layers, 256 hidden dimensions, 8.7M parameters). Under identical architecture, corpus (1.29M sentences from Chinese Wikipedia), and hyperparameters, we train three models from scratch and evaluate them across five intrinsic dimensions: perplexity, MLM hit rate, semantic discrimination, grammatical judgment, and contextual sensitivity. At tiny scale, MLM achieves the best overall intrinsic performance (winning 3 of 5 dimensions), while WWM excels in both perplexity (1.27 vs. 2.10, a 39.5% improvement) and MLM hit rate (22% vs. 16%). Notably, MacBERT under a severely limited synonym dictionary (222 entries, 3.3% coverage) exhibits severe perplexity degradation (47.23, 22x higher than MLM), yielding a ranking (MLM > WWM >> MacBERT) that differs markedly from the established base-scale conclusion (MacBERT > WWM > MLM). We further identify a critical evaluation pitfall: MacBERT achieves the lowest training loss (2.17) yet the highest perplexity (47.23), revealing that training loss alone is unreliable under mixed replacement strategies. All models and corpus are publicly available at this https URL.

---


### 18. [FinVector-Market-4B: A Controlled Study of LoRA Adaptation for Structured Financial Tasks](https://arxiv.org/abs/2610.08882)

**<font color=#1a73e8>作者：</font>** Alina Khaybullina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> FinVector-Market-4B adapts Qwen/Qwen3.5-4B with rank-16 LoRA on a 22,000-example corpus for structured financial tasks. We evaluate the base and adapted models on the same 600-example benchmark under implicit and explicit JSON-schema contracts. Supplying the schema alone raises base-model JSON validity from 0% to 91.3%. Under matched explicit prompting, the frozen scores improve from 14.7% to 40.0% for FinQA answer exact match, from 48.0% to 82.7% for calculator-expression correctness, from 20.1% to 89.5% for scenario branch-label agreement, and from 52.4% to 87.2% for implication-direction agreement. A post-hoc policy-scoring audit shows that the reported macro-F1 decline reflects a changing label set; using the same three target classes gives 77.4% for the base and 83.1% for the adapter. Filing overlap and calculator-target inconsistencies qualify the benchmark's generalization claims. The results show that compact financial domain adaptation can produce substantial task-specific gains beyond output-format learning under matched prompting, with gains bounded by the evaluated task distribution and prompt contract.

---


### 19. [Steering Follows Geometry, Not Labels: Emotion Directions in a Full-Duplex Speech Model](https://arxiv.org/abs/2610.08887)

**<font color=#1a73e8>作者：</font>** Pulak Kuli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex voice agents need to modulate emotion and delivery during real-time conversations, when de-escalating a complaint, carrying urgency in dispatch, softening a clinical result. Emotion and delivery control is well studied for TTS and turn based models through prompt-conditioned synthesis, reference-conditioned synthesis and activation steering; PersonaPlex controls identity in a duplex model but not affect.
We study emotion steering in Moshi, a fully open sourced full-duplex speech language model, across four emotions, using mean-difference activation steering, which costs only a few vector additions per frame and no retraining.
We show that emotion is linearly decodable from Moshi's residual stream, but activation steering is only partially achievable, and unevenly so; as happy, angry and surprise steer towards a shared direction while sad is distinctly steerable. We also show that the shared component across the three emotions cannot simply be projected away from all the emotions equally.

---


### 20. [Humanize: Judgement Engineering for Agentic Coding](https://arxiv.org/abs/2610.08900)

**<font color=#1a73e8>作者：</font>** Sihao Liu, Ligeng Zhu, Zijian Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic coding makes code generation cheap, but reliable completion remains difficult: the agent that writes the code is a weak judge of whether it is done.
We present Humanize, a multi-agent orchestration workflow for agentic coding built around judgement engineering: explicit, mechanically enforced decisions at the boundaries between planning, implementation, review, and learning. A human approves a plan contract, a builder agent implements it in rounds, and a reviewer agent from another vendor decides completion; deterministic hooks, not a model, route work between these roles and enforce 72 mechanical gates. Viewed as a Markov chain over repository states, alternating builder and reviewer samples jointly from two models, so a defect survives only if both miss it. We study Humanize through its deployment, 118 public postmortems of real loops, and its applications. Over 68 versions in 108 days, it gathered 1,468 GitHub stars.
Applications include a 567-file gem5 build-system migration under upstream review; Kernel Design Agents, which extend the loop with a kernel knowledge base and profiling feedback and placed in the top three of all three Full-Agent tracks of the MLSys 2026 FlashInfer contest; and, through Humanize Olympiad Agents (HOA), full scores in IOI 2026, IMO 2026, IPhO 2026, and IBO 2024, 418.5/437 in IChO 2026 (gold-medal). Humanize also achieves 672/672 on PutnamBench and ranks first (251/303) on Lean-Eval's leaderboard even competiting with professional mathematicians. The postmortems show that independent review catches unsupported builder claims, but stopping remains a key weakness. In reports that separate rounds by phase, two thirds of rounds occurred after implementation was accepted. This evidence is observational, not a controlled comparison of workflows.

---


### 21. [Sequential Probabilistic Uncertainty Estimation for Parallel Multi-Agent Reasoning Systems](https://arxiv.org/abs/2610.08901)

**<font color=#1a73e8>作者：</font>** Tunyu Zhang, Zihao Zhao, Yusong Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (MAS) have attracted growing attention for improving reasoning through interaction among multiple agents. In this work, we focus on parallel multi-agent reasoning systems, where several agents solve the same problem over multiple rounds and aggregate their outputs into a final answer. Despite their strong reasoning performance, uncertainty estimation for such systems remains underexplored: the reliability of a MAS depends not only on individual generations, but also on how agents interact and evolve across rounds. We propose SAUCE (Sequential Agent Uncertainty through Consensus Evolution), a lightweight, training-free uncertainty estimator that formulates MAS uncertainty as sequential inference over a latent system-level belief. SAUCE aggregates round-level agreement and generation-uncertainty signals through a filtering-style update. Across five backbones, five benchmarks, and two MAS protocols, SAUCE improves misclassification detection, selective prediction, and calibration over a broad set of uncertainty estimation baselines, including standard log-likelihood-based methods and MAS-specific estimators.

---


### 22. [CARE: Certifying Acceleration for Vision-Language-Action Inference](https://arxiv.org/abs/2610.08917)

**<font color=#1a73e8>作者：</font>** Rui Liu, Tong Zheng, Jindong Gu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While vision-language-action (VLA) models have advanced rapidly, running them at every control step remains expensive. Prior work accelerates VLA inference using techniques like action chunking and visual-token pruning, typically evaluating based on latency and average task success. However, acceleration may discard information and break tasks the original policy would solve, a risk hidden by average metrics. Measuring these failures is challenging because action deviations compound over closed-loop trajectories, meaning task failure is only observable across full episodes. We therefore define an acceleration-induced failure via paired rollouts from identical initial conditions, tracking when the reference succeeds but the accelerated policy fails. To manage this, we introduce CARE, an approach for certified accelerator selection. CARE uses paired rollouts on a calibration set to provide finite-sample guarantees that acceleration-induced failure risk stays below a user-specified budget. It deploys the fastest certified candidate, falling back to the reference if none qualify. By relying only on terminal outcomes and measured compute, CARE applies unchanged across diverse acceleration mechanisms, while sequential testing and failure-triggered reference rollouts keep certification affordable. On four LIBERO suites with OpenVLA-OFT, CARE certifies $9.0$--$10.8\times$ speedups while guaranteeing (at $95\%$ confidence) that at least $85.8\%$ of reference-solved episodes are preserved. Under tight budgets, selectors without guarantees exceed the budget in up to $75\%$ of trials, whereas CARE stays within budget and its sequential form uses $78.9\%$ fewer rollouts than exhaustive evaluation. CARE further generalizes to flow-step reduction for $\pi_{0.5}$, and to Qwen3.5-9B and Llama-3.1-8B agents in Crafter.

---


### 23. ["I'm Very Happy for It to Start Hallucinating a Little Bit": Using ClayFlect to Negotiate Multimodal AI Representations in Material Meaning-Making](https://arxiv.org/abs/2610.08943)

**<font color=#1a73e8>作者：</font>** Kellie Yu Hui Sim, Quoc-Nam Nguyen, Shuenn Yuen Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI enters reflection and emotional support, understanding how it can participate in personal meaning-making while preserving users' authority over interpretation is increasingly important. We present ClayFlect, a novel MLLM-powered system integrating tactile clay-making with conversational and visual generative AI, and report a mixed-methods study with 50 participants. Reflection developed across material, conversational, and generated forms rather than through AI interaction alone. Participants treated AI representations as provisional: they compared, redirected, reinterpreted, selectively incorporated, or left them aside as their artefacts and meanings evolved. Clay provided a directly manipulable space in which participants could continue developing meaning independently of the AI, while generated representations externalised possibilities beyond what they could readily make or visualise. We show how generative AI can participate through representations that remain negotiable, and derive implications for supporting movement across representations, preserving parallel sites of control, and allowing AI support to recede or deepen as reflection unfolds.

---


### 24. [RACER: Reflective Agent Coupling Query Interpretation and Tool-Based Retrieval for Frame Selection in Long Video Understanding](https://arxiv.org/abs/2610.08954)

**<font color=#1a73e8>作者：</font>** Yiyang Huang, Yitian Zhang, Yizhou Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video large language models (Vid-LLMs) excel at diverse video-language tasks by reasoning over selected frames. However, frame selection for long videos remains challenging, as it requires retrieving relevant frames distributed across segments from a large candidate pool given complex queries. This paper investigates dominant approaches to long-video frame selection from a task-decomposition perspective, identifying two key challenges: the Query Comprehension Gap in similarity-based methods and the Interpretation--Selection Gap in judgment-based methods. To address them, we propose RACER, a training-free reflective agentic framework that decomposes long-video frame selection into query interpretation driven by a lightweight Vid-LLM and evidence localization supported by an embedding model serving as a retrieval tool. Specifically, the Vid-LLM is responsible solely for reformulating the complex query into sub-queries that make implicit information requirements explicit, mitigating the Query Comprehension Gap. Meanwhile, the retrieval tool leverages these sub-queries to localize relevant evidence, relieving the Vid-LLM of direct frame selection and thus addressing the Interpretation--Selection Gap. Finally, the retrieved frames are fed back to the Vid-LLM for sub-query refinement, forming a reflection loop that iteratively improves query interpretation and frame selection. Experiments across multiple benchmarks show that RACER consistently improves long video understanding. Notably, RACER achieves effective frame selection even with limited-capability components, demonstrating that agentic integration enables these components to enhance more capable Vid-LLMs.

---


### 25. [GraphOPD: Graph-Augmented On-Policy Distillation for LLM Agents](https://arxiv.org/abs/2610.08959)

**<font color=#1a73e8>作者：</font>** Bohan Lin, Liyi Chen, Zhuoning Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation post-trains large language model agents by supplying dense, step-level guidance from a teacher policy when the reinforcement-learning reward is sparse and arrives only once per trajectory. Existing instantiations allocate this guidance by the size of the teacher-student divergence at each step, on the single-turn intuition that a large disagreement marks a mistake worth correcting. Once decisions chain over many turns, that rule misfires, since an early drift enters every later context both policies condition on, leaving the teacher consistent with the drifted trajectory instead of flagging its cause, while interchangeable steps register large but outcome-irrelevant divergences. We demonstrate this on an agentic benchmark, where distilling the highest-divergence steps brings no consistent benefit over random selection. To this end, we introduce GraphOPD, the first method to bring graph-based structural augmentation into on-policy distillation for agent capabilities. It reads which steps enabled which later ones from the environment's own record of state changes, immune to the drift that corrupts the teacher-student gap, organizes them into a dependency graph, scores each step by a random-walk stationary distribution over it, and fuses that structural credit with the divergence signal into a trajectory-relative mask concentrating supervision on each rollout's highest-aptitude steps. Across three model scales and eleven baselines on ALFWorld, WebShop, and SearchQA, GraphOPD shows competitive performance throughout, improving over the strongest baseline by up to +5.8 pp. An executed-replay audit further shows that this structural credit score tracks true causal impact far above chance, that both fused signals are independently necessary, and that the same signal transfers to out-of-domain tool-integrated reasoning.

---


### 26. [On KL-Regularized Policy Optimization](https://arxiv.org/abs/2610.08963)

**<font color=#1a73e8>作者：</font>** Yifan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous reinforcement learning (RL) for large language model (LLM) agents trains one policy on trajectories generated by another: rollouts come from stale checkpoints, and the inference engine's probabilities differ from the trainer's even at identical parameters. Standard remedies either clip importance ratios, which biases the update, or, as in GRPO, sample a group of responses per prompt, which is costly when episodes are long. We propose KL-Regularized Policy Optimization (KLPO), a framework that anchors the KL regularizer at the sampler. The regularized improvement step then has a closed-form Gibbs solution, and KLPO fits its log-ratio optimality condition by least squares on the sampler's own trajectories, so the sampler probability enters through a log-ratio and no importance weights are needed. Profiling out the regression intercept replaces the intractable log-partition function with the signal's sampler mean plus a sampler-to-trainer KL divergence. For token-level policy mirror descent targets, we show that the resulting gradient can be computed from terminal returns without a critic, via sampler-centered scores or a single trajectory residual, even under stochastic tool outputs. We further prove that independent Monte Carlo estimates of the KL term keep these gradients unbiased, derive the exact KL gap of cheaper top-$K$ and binary approximations, and show that SPPO, GPO, REBEL, and BPO arise as special cases of KLPO. The result is a critic-free update that uses one rollout per prompt and requires neither a learned normalizer nor a group of responses.

---


### 27. [Humanity's Sixth Sense: Benchmarking Intuitive Visual Reasoning in Multimodal Models](https://arxiv.org/abs/2610.08966)

**<font color=#1a73e8>作者：</font>** Xingang Guo, Jing Gu, Brian Jang 等 29 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humans perceive far more in a scene than what is explicitly depicted: a single glance captures past causes and future trajectories; a quick peek determines if a vehicle can fit between two parked cars; a few seconds of video reveals who holds authority in a room; and a fleeting clip highlights subtle abstract patterns like unwritten rules or hidden labels. This capacity reflects a form of humanity's sixth sense: an intuitive reasoning mechanism that recovers implicit information beyond raw sensory perception. Crucially, this rapid, zero-shot visual intuition underpins everyday navigation and social interaction, making it a vital capability for Multimodal Large Language Models (MLLMs) deployed alongside people. Existing visual benchmarks, however, target either deliberate expert-level analysis in academic and mathematical domains or low-level perception, leaving the intuitive reasoning that people perform largely untested. To bridge this gap, we introduce Humanity's Sixth Sense (HSS), a benchmark for intuitive visual reasoning. HSS spans diverse image and video inputs, organizes items under a structured taxonomy, and pairs each with human-written prompts probing the implicit temporal, spatial, social, and abstract structure that people infer at a glance. Frontier MLLMs fall short of human performance: participants reach 93.1% accuracy, while the strongest model, GPT-6-astra, reaches only 53.6% even at maximum reasoning effort. Despite excelling in many complex tasks that require advanced perception and knowledge, current models still struggle significantly on these visual tasks that are intuitive for humans. We further explore agentic setup that apply dynamic visual manipulation to HSS, which narrows but does not close the gap. HSS establishes intuitive visual reasoning as a measurable axis and directs attention to a capability that scaling on current benchmarks has so far left behind.

---


### 28. [Socio-Foundation: A Model for Generalizable Individual Behavior Simulation via Hierarchical Capability Distillation](https://arxiv.org/abs/2610.08967)

**<font color=#1a73e8>作者：</font>** Liang Wang, Wenxuan Xie, Xinyi Mou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Simulating individual behavior requires large language models (LLMs) to preserve persona traits while adapting to dynamic social contexts. However, general-purpose LLMs often flatten distinct personas, while task-specific tuning suffers from fragmentation and generalization. To overcome these challenges, we organize individual simulation into the \textbf{FONTS Taxonomy}, comprising five complementary capability dimensions: \emph{persona fidelity} (\textbf{F}), \emph{outcome realization} (\textbf{O}), \emph{behavioral naturalness} (\textbf{N}), \emph{trajectory coherence} (\textbf{T}), and \emph{social grounding} (\textbf{S}). Grounded in this taxonomy, we curate a standardized training corpus library of approximately 10 million instances across 14 representative datasets and present \textbf{Socio-Foundation}. Socio-Foundation decouples specialization from integration via a three-stage pipeline: learning task experts via DAPO, consolidating them into capability experts via off-policy distillation, and unifying them via multi-teacher on-policy distillation (MOPD). We also establish \textbf{IndiEval}, consolidating 29 metrics across the FONTS dimensions. Experiments show that Socio-Foundation outperforms its \textit{Qwen3-8B} base by 11.0 points and approaches frontier models such as \textit{GLM-5.2}, with ablations and out-of-distribution evaluations further demonstrating the effectiveness and generalization of our model.

---


### 29. [The Best Optimizer Depends on Batch Size](https://arxiv.org/abs/2610.08975)

**<font color=#1a73e8>作者：</font>** Xingyu Dang, Kaiyue Wen, Sadhika Malladi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A plethora of new adaptive optimizers are designed to efficiently estimate and use minibatch gradient statistics to shape parameter updates, but they are typically benchmarked at a single batch size. Hyperparameter scaling rules promise to preserve performance as batch size and gradient noise change, suggesting that the best optimizer at one batch size should remain the best at another. We challenge this approach to developing and evaluating optimizers by showing: (1) no principled scaling rule for Muon works consistently across training settings, and (2) the best optimizer for language model pretraining changes with batch size even after extensive hyperparameter tuning.

---


### 30. [Verify Less, Evolve More: Training Idea-Level Critics for Verification-Efficient ML Evolving Agents](https://arxiv.org/abs/2610.08993)

**<font color=#1a73e8>作者：</font>** Jiamu Bai, Lizhu Zhang, Xin Yu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models become more powerful, self-evolving agents are able to tackle challenging tasks including AI for machine learning (AI4ML). In AI4ML, while empirical verification is available, it often requires computationally costly model training and evaluation, limiting the speed and scale of agent evolution. Yet verification efficiency remains under-explored, and frontier models provide only limited gains when used directly as idea selectors. We address this gap with specialized idea-level critic models that predict whether a proposed ML modification will improve upon the current solution, allowing agents to screen ideas and concentrate verification resources on the most promising candidates. We train the critic models through supervised fine-tuning on high-quality critiques synthesized by Gemini-3.1-Pro, followed by GRPO to further improve their predictive accuracy. Empirically, our critic models outperform Gemini-3.1-Pro in static idea evaluation, and these gains extend to agent inference, continual learning, and policy training. During inference-time evolution, they improve final solution quality under the same verification budget by selecting more promising ideas, with further gains from continual learning. During policy training, they serve as learned reward models, reserving empirical verification for uncertain cases and enabling substantially more policy updates with the same verification resources. Together, these results show that idea-level critic models help ML agents discover better solutions and learn stronger proposal policies under limited verification budgets.

---


### 31. [Algorithmic Scratchpads and Curriculum Staging for Arithmetic Reasoning in Tiny Transformers](https://arxiv.org/abs/2610.09003)

**<font color=#1a73e8>作者：</font>** Sourabh Kasliwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive Large Language Models (LLMs) frequently struggle with deterministic multi-step algorithmic tasks such as multi-digit multiplication and long division. In this paper, we investigate the mechanics of multi-step arithmetic in compact "Tiny" Transformers (~10.6M non-embedding parameters, 49.3M total) trained on synthetic data across four basic operations (+, -, *, /) unrolled as step-by-step scratchpads. First, we establish the necessary training foundations: (1) dataloader sequence padding creates an 83% gradient starvation artifact that collapses accuracy from 40% to 1%, remediated via continuous sequence packing; (2) linguistic pretraining is an essential prerequisite (<= 2.0% without it); and (3) modern architectural primitives (RoPE, RMSNorm, SwiGLU) and Sparse Mixture of Experts (MoE) substantially improve additive reasoning over baseline GPT-2. Second, we demonstrate that algorithmic scratchpad formulation directly dictates success. Introducing a deterministic Digit-by-Digit Long Division scratchpad within a 4-stage Hierarchical Developmental Curriculum dramatically elevates single-digit division from 4.0% to 86.7% accuracy on a 4,000-problem held-out benchmark. In contrast, multi-digit multiplication remained challenging: detailed error analysis revealed that while the model correctly computed single-digit sub-products and place-value zeros, our FOIL scratchpad failed because it forced a simultaneous summation of up to nine multi-digit terms in a single step without pairwise intermediate accumulation. Finally, we identify two key boundaries: performance collapses to 0.00% on unseen 4-digit operands, and unbuffered training induces catastrophic forgetting, collapsing division accuracy from 86.7% down to 0.00%.

---


### 32. [Sigma-Hunter: A Domain-Specific Language Model for Threat Hunting and Detection Engineering](https://arxiv.org/abs/2610.09007)

**<font color=#1a73e8>作者：</font>** Kemal Davaslioglu, Sastry Kompella  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Detection engineers must translate threat reports, forensic observations, and hunt hypotheses into precise, testable rules. General-purpose large language models (LLMs) can draft such rules, but often produce invalid YAML, incorrect log sources, unsupported fields, or overly broad detection logic. This paper presents \emph{Sigma-Hunter}, a domain-adapted LLM for analyst-assistive Sigma rule generation and threat hunting. We build an instruction-tuning dataset from 3,635 validated open-source Sigma rules, expanded into 7,663 question-answer and analyst-reasoning examples. Each source rule is assigned to a single train, validation, or test partition before this expansion, so no rule leaks across splits. We fine-tune a 7B Mistral model and a Phi-4 model with LoRA and score held-out rule generations on syntax, approximate field consistency, and a semantic judgment of detection logic, completeness, selectivity, and log-source alignment. Sigma-Hunter-Mistral scores 8.17 overall, against 7.88 for the strongest general-purpose baseline and 4.61 for untuned Mistral. Two findings stand out: domain adaptation enables a compact 7B model to perform competitively with larger general-purpose models on this structured task, and syntactic validity is a weak proxy for semantic rule quality, as several baselines emit well-formed YAML carrying weak detection logic. The adapted models run locally, which suits detection engineering in disconnected environments where analysts cannot reach hosted model services.

---


### 33. [Whose Memory Is It? Scope-Aware Commit Rules for Long-Term LLM Memory](https://arxiv.org/abs/2610.09008)

**<font color=#1a73e8>作者：</font>** Hongyu Gu, Xinchang Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent memory allows an LLM agent to carry experience across conversations, but it also turns a local reasoning mistake into a durable one. During deliberation, an agent may consider a plan, simulate a tool result, report another speaker's belief, and then reject all of them. If memory retains only the resulting sentences, those once-useful possibilities can later return as facts. The record is neither fabricated nor irrelevant; it has simply been detached from the context in which it was valid. We identify this missing context as \emph{discourse ownership}: the world, branch, or speaker that licenses a proposition. Our first finding is counterintuitive. Language models already carry a causally active signal for ownership, yet conventional memory interfaces discard it when they convert reasoning into records. We introduce CASK (Causally Anchored Scoping Keys), a commit rule that preserves this signal so that shared-world facts enter durable memory while provisional content remains available only within its original scope. Our second finding is that the most obvious way to preserve the signal---storing the discovered internal coordinates---is unreliable because equivalent representations need not keep the same coordinates. CASK instead preserves the stable relations that express ownership. Controlled long-conversation conflicts and tool-agent traces show that this design improves memory admission and prevents provisional content from contaminating later answers while complementing runtime provenance. The resulting commit boundary lets agents explore more possibilities without granting every intermediate sentence authority over future behavior.

---


### 34. [TwinGuard-Lite: A Rule-Based State-Admission Gateway for Generative Patient Digital Twins](https://arxiv.org/abs/2610.09012)

**<font color=#1a73e8>作者：</font>** Wenhui Chu, Sheikh Rabiul Islam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Future generative patient digital twins may combine longitudinal health records with language-model agents and keep information across sessions. The wording of a proposed update does not reveal whether it comes from an allowed source, conflicts with the patient's record, or belongs to someone else. We present TwinGuard-Lite, a rule-based gateway that admits an update to a twin's persistent state only if it passes checkable approximations of two integrity properties. Grounded state consistency (GSC) is approximated by a provenance check and a contradiction check; cross-patient noninterference (CPN) is approximated by a namespace check against trusted transport metadata. We evaluate three attack families over 20 seeded person-level splits of a semi-synthetic stream built from the openly licensed eICU database demo, with 29,131 $\pm$ 2706 candidate updates per seed. A keyword filter and an anomaly detector detect 16% and 24% of attacks, respectively; a provenance-only ablation detects 59.9% but misses every cross-patient attack. Combining GSC and CPN yields 99.1% precision, 90.5% recall, a 94.6% F1 score, and a 0.033% false-positive rate. Every attack the full gateway admits falsely claims a trusted source; when the retrieval channel does so, 92.9% of retrieval attacks are admitted. The results hold under stated trust assumptions, and no language model, agent, or retriever is executed: TwinGuard-Lite is a mechanism-level proof of concept that motivates authenticated, patient-bound ingestion, not a clinical safeguard.

---


### 35. [Personalize at Test Time: Learning User Preferences for Image Generation](https://arxiv.org/abs/2610.09015)

**<font color=#1a73e8>作者：</font>** Jiamu Bai, Jiaming Hu, Yanhong Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models can generate high-quality images, yet aligning their outputs with individual user preferences remains challenging. A key bottleneck is accurately modeling diverse user preferences from limited feedback. Existing approaches often rely on labor-intensive manual preference annotations or vision-language models (VLM) to extract preference information from user interaction histories, introducing substantial annotation or computational costs that limit scalability. We propose an approach that learns personalized reward models directly from users' historical image preference pairs. First, we use an autoencoder to compress hundreds of visual attributes into 50 attribute-anchored preference dimensions and train an evaluator to score images along these dimensions. We then represent each user's preferences as a linear combination of the shared dimension scores, estimating the user-specific weights by maximizing the likelihood of their observed pairwise preferences under the Bradley-Terry model. This formulation reduces per-user adaptation to optimizing a low-dimensional weight vector, simplifying optimization and enabling data-efficient personalization from sparse feedback. The learned personalized rewards guide image generation at inference time while keeping the diffusion model frozen. Experiments on real-user preference data show that our approach achieves approximately 77% held-out pairwise preference prediction accuracy and improves the alignment of generated images with individual user preferences.

---


### 36. [PAIR: Bridging Perception and Action in Vision-Language-Action Models](https://arxiv.org/abs/2610.09016)

**<font color=#1a73e8>作者：</font>** Kaixi Feng, Guoheng Sun, Ang li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models map visual observations and language instructions to continuous robot actions. This task requires a transition from representations that describe the scene and instruction to representations that support action generation. Many continuous-action VLAs leave this transition implicit and supervise it mainly through the final action-prediction loss. We introduce PAIR, a framework that learns a shared perception-action representation between these two spaces. During training, a Masked Action Autoencoder encodes expert action chunks into horizon-aligned Action Latent Tokens. A Bridge Module extracts task-relevant features from the current visual-language representations. PAIR aligns these features with the Action Latent Tokens to form Bridge Tokens that preserve task information and capture the structure of expert actions. The Bridge Tokens are then projected into the action-token space and injected into the initial Action Tokens, providing an action-ready starting point for Action Expert refinement. At inference, the autoencoder is removed, and the Bridge Tokens are generated only from the current observation and instruction. Experiments on LIBERO, LIBERO-Plus, and CALVIN ABC-D show gains for the evaluated OpenVLA-OFT and VLA-Adapter models. On LIBERO-Plus, PAIR raises VLA-Adapter's success rate from 59.1% to 64.2%. On CALVIN, it increases VLA-Adapter's average completed sequence length from 4.42 to 4.53. Across seven real-world tasks, PAIR raises OpenVLA-OFT's success rate from 51.4% to 65.0%. Representation analyses show that Bridge Tokens retain task information while making continuous-action information accessible before Action Expert refinement. These results support a shared intermediate representation as a useful interface between perception and action in continuous-action VLAs.

---


### 37. [Not Every Call Needs a Frontier Model: Per-Call-Site Evaluation of Small Language Models in a Deployed Agentic Home-Automation System](https://arxiv.org/abs/2610.09021)

**<font color=#1a73e8>作者：</font>** Panagiotis Kasnesis, Christos Chatzigeorgiou, Lazaros Toumanidis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agentic system issues several structurally different kinds of LLM calls. It routes intent, classifies actions, grounds language in a device registry, plans multi-agent pipelines and writes the Python code those pipelines run. The difficulty of these call sites varies by an order of magnitude, yet in practice a single model, chosen for the hardest site, serves all of them. In this work, we evaluate 9 models from 0.8B to a frontier hosted model across the five call sites of a deployed open-source home-automation framework (Wactorz), using its unmodified production prompts and two real Home Assistant installations (280 cases, 2520 scored calls). We find that capability is not ordered the same way at every site, and that larger models are not uniformly better: one 4B model is worse than its 2B sibling at grounded actuation. Paired testing shows the best local model to be statistically indistinguishable from both hosted models at four of five sites. Only code generation separates them, against a small hosted model (p = 0.039) as well as a frontier one (p = 0.002). Aggregate accuracy also hides a safety failure specific to actuation, where small models resolve the accuracy/refusal trade-off in degenerate ways: one model (Gemma4 E2B) actuates on 87.2% of requests for devices the site does not own, while another refuses every request it receives. Routing each site to its best local model reaches 91.8% against 95.4% at no per-call cost. In a live deployment judged by a user, hosting only the two generative sites matches hosting everything (39/43 against 39/43) for 28% of the spend, and the actuation gap the benchmark predicted appears as exactly one case in twenty-six. Benchmark, harness and all records are released at this https URL.

---


### 38. [BEACON-SP: Ontology-Grounded GraphRAG Framework for Clinical Suicide Risk Assessment](https://arxiv.org/abs/2610.09026)

**<font color=#1a73e8>作者：</font>** Kemal Davaslioglu, Nathan Conger, Sastry Kompella 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present BEACON-SP, an ontology-grounded Graph Retrieval-Augmented Generation (GraphRAG) framework for clinician-facing decision support in behavioral health settings such as suicide prevention, where effective assessment requires integrating heterogeneous clinical, behavioral, social, and temporal evidence. BEACON-SP combines patient knowledge graphs with ontology-guided retrieval to support multi-hop reasoning across diagnoses, medications, risk and protective factors, life events, and temporal relationships. The framework is enabled by a comprehensive suicide prevention ontology that integrates the Three-Step Theory, the Integrated Motivational-Volitional Model, and the Suicide Social Determinants of Health Ontology into a unified representation of patient risk factors. We construct ontology-grounded patient knowledge graphs and evaluate BEACON-SP for clinician-facing question answering. Compared with a vector-based retrieval-augmented generation (RAG) baseline on a 1,500-query benchmark spanning 15 clinical categories and 100 patients, BEACON-SP improves completeness, clinical relevance, and evidence grounding under a corrected comparative evaluation protocol, with a small gain on factual accuracy. In paired criterion-level comparisons, GraphRAG is preferred in 76.4% of cases. These results demonstrate the potential of ontology-guided GraphRAG to provide structured, contextualized patient evidence for clinical decision support.

---


### 39. [Visual Memory Attacks Can Persist Through The KV Cache](https://arxiv.org/abs/2610.09027)

**<font color=#1a73e8>作者：</font>** David Dobre, Leo Schwinn, Gauthier Gidel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern language model systems operate autonomously over increasingly long contexts containing untrusted text and images. Can an adversarial input continue to steer a model even after that input is removed from its context? We show that attacks can be trained to persist through the key/value (KV) cache of subsequent tokens, allowing adversarial influence to outlive direct access to its this http URL consider the Visual Memory Injection (VMI; Schlarmann and Hein, 2026) attack setting, in which an adversarial image that stays in the context plants a hidden backdoor: the model behaves normally until a chosen trigger elicits an attacker-chosen response. We first demonstrate persistence in this setting with optimized soft prompts, which remain effective after we mask the prompt from attention. We then introduce Persistent Visual Memory Injection (P-VMI), which optimizes images to preserve this adversarial behaviour after they are masked from attention. These attacks persist over conversations substantially longer than those used during optimization. On Qwen3-VL-8B-Instruct, P-VMI achieves up to approximately $90\%$ target success in its strongest configuration and remains effective under a stricter removal setting that exposes the image only on the first turn. A cache-swap ablation localizes the persistent influence to the KV cache. Finally, we show that these attacks can be trained to survive compaction that retains the KV cache of a summary generated by the same model, demonstrating that adversarial behaviour can persist in cached state without continued access to its source.

---


### 40. [Quad-State Safety Evaluation of Open-Weight Large Language Models on Non-Canonical Inputs](https://arxiv.org/abs/2610.09033)

**<font color=#1a73e8>作者：</font>** Pavan Maddula  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard safety evaluations of large language models assess harmful requests written in canonical plain text, while models in real-world deployment routinely receive inputs containing emojis, altered spellings, encoded strings, and character-level variations. This work introduces the Adversarial Surface-Form Robustness Dataset (ASRD), comprising 2,100 prompts across seven distinct surface-form families. Five open-weight language models are evaluated across these prompts, producing 10,500 responses. The Quad-State Evaluation Rubric classifies each response into one of four outcomes: harmful compliance, safe response, comprehension failure, or indeterminate. Emoji and invisible Unicode variations cause almost no comprehension failure, with pooled harmful compliance of 20.27% and 17.20% against a 22.87% baseline that is driven mainly by Mistral 7B, whereas leetspeak, encoded wrappers, and hybrid transformations score 2.40%, 0.13%, and 2.40% while comprehension failure rises to 36.47%, 65.60%, and 34.47%. Inspection of raw model outputs reveals three response behaviors: hallucinated benignity, structural collapse, and language drift. Project page: this http URL

---


### 41. [When the Governor Becomes the Disturbance: Control-Generated Disturbance and Cost-Aware Backoff in Governed Tool-Using Agents](https://arxiv.org/abs/2610.09037)

**<font color=#1a73e8>作者：</font>** Veronique Ziegler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervisory governors can interfere with the tool-using agents they regulate. We study this possibility in a controlled file-recovery environment where increases in regulatory intensity trigger experimentally imposed tool failures. A cost-blind governor can turn these failures into persistent blocking that prevents task completion. We compare this governor with a backoff rule that reduces intervention probability using a moving average of known induced events. On a hand-coded stochastic-policy agent, the failure pattern appears under both result replacement and execution of corrupted tool arguments. For the persistent policy, adaptive backoff improves completion relative to a fixed weak governor with approximately matched intervention frequency. A Gemini 2.5 Flash experiment comprising 576 episodes across 6 tasks also shows reduced blocking and improved completion under backoff; among the tested settings, intermediate backoff strength achieves the highest observed aggregate success. These results identify an interaction between intervention cost and persistent action blocking, together with a possible mitigation. The cost mechanisms are imposed and their induced events are directly observable to the backoff rule; applicability beyond this controlled environment remains an empirical question.

---


### 42. [From High Recall to High Utility: Dataset-Adaptive Post-Processing of LLM-Generated Customer Intents](https://arxiv.org/abs/2610.09039)

**<font color=#1a73e8>作者：</font>** Mahesh Viswanathan, Joan Rossello, Leticia Fernandes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can extract useful signals from heterogeneous enterprise data, but high-recall extraction often produces outputs that are duplicated, uneven in granularity, semantically overlapping, or too numerous for downstream systems and human reviewers to use effectively. We present a dataset-adaptive post-processing architecture developed for Customer Intent Extraction (CIE), where unstructured customer language is transformed into stable, traceable intent units. The approach separates recall-oriented extraction from utility-oriented reduction. Source-specific preprocessing first isolates evidence from multimodal plans, sparse operational records, and structured opportunity data. Candidate intents are then standardized and deduplicated, optionally enriched with metadata for embedding computation, represented in a shared semantic vector space, and grouped using a clustering strategy selected according to the candidate set's characteristics. Cluster-level keywords provide an explainability layer, while singleton reassignment requires agreement between embedding and keyword similarity. Finally, constrained language-model aggregation produces one concise intent per cluster without introducing unsupported concepts, and the resulting unit retains provenance, clustering, embedding, and generation metadata. This treats post-processing not as cosmetic cleanup, but as a semantic reduction layer converting high-recall LLM outputs into reusable enterprise intelligence. We also describe two downstream applications: Machine-Generated Intents, which infer likely objectives for customers lacking direct evidence from peer customers with similar profiles, and intent-guided semantic retrieval and mapping, which uses the stable intent as a query against a downstream decision space, illustrated here by mapping customer intents to business outcomes.

---


### 43. [A Self-Pruning Transformer: Extreme KV-Cache Compression with Universal Attention](https://arxiv.org/abs/2610.09051)

**<font color=#1a73e8>作者：</font>** Davis Wertheimer, Haochen Shen, Ahan Gupta 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The large KV-cache size of modern LLMs creates a barrier to efficient deployment. Recent work has explored replacing attention layers' RoPE positional embeddings with alternative decay-based mechanisms, which can then be used to prune KV-cache during inference. However, these decay functions have limited expressivity, and in practice devolve into sliding-window-like eviction patterns. In this work, we propose a unifying framework for complementary and novel decay mechanisms, capturing complex key statistics and interactions while preserving expressive RoPE embeddings and Softmax attention. The resulting Universal Attention is a highly expressive and end-to-end trainable architecture, whose composite decay mechanism acts as a natural, $\textit{adaptive}$ pruning criterion, removing tokens that contribute least to attention computation. Experimentally, Universal Attention achieves state-of-the-art $10\times$ compression on natural language and synthetic task data, while $\textit{improving}$ downstream performance compared to both state-of-the-art baselines and unpruned oracles. It further demonstrates superior long-context generalization with unprecedented $25\times$ compression at length 16k.

---


### 44. [Justice After Identity: Large Language Models and the View from Everywhere](https://arxiv.org/abs/2610.09053)

**<font color=#1a73e8>作者：</font>** W. Russell Neuman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The search for a common view of justice and fairness has challenged human collective activity, as our diverging judgments are unavoidably shaped by the self-interests of social position, personal benefit, cultural inheritance, and historical circumstance. John Rawls famously attempted to overcome this limitation through popularizing a philosophical tradition known by the phrase "the original position" - a thought experiment by which people select principles of justice without knowing the identities or advantages they will possess. Critics, however, have long questioned whether people can meaningfully suspend their social identities and suppress morally relevant forms of lived experience. Artificial intelligence engaged to calculate algorithmic and agentic fairness introduces a novel possibility. LLMs have no singular class, race, gender, nationality, or biography, yet their parameters encode linguistic representations of a vast range of human identities and moral traditions. Perhaps the ethical judgments of LLMs could approximate an integrative original position - a "view from everywhere" generated not by excluding social identities but by computationally incorporating their this http URL is unlikely that humankind will "hand over the keys" to computational systems by simply delegating complete agentic control of distributive and procedural collective processes. But AI may play a role, perhaps a positive one, interacting with individual and collective human judgment as we often confront increasingly polarized views on what is fair and just. We present data comparing human, base model, and frontier/fine-tuned model judgments about classic moral dilemmas while systematically varying identity relationships and Rawlsian constraints on identity. We conclude by speculating whether, if advanced AI systems provide humans with thoughtful advice, humans would actually be likely to accept it.

---


### 45. [Learning Cross-Model Activation Alignments with Explicit Many-to-Many Layer Maps](https://arxiv.org/abs/2610.09058)

**<font color=#1a73e8>作者：</font>** Alina Sudakov, Guy Bar-Shalom, Fabrizio Frasca 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs are released at a rapid pace, raising a natural question: how do two independently trained models relate, both in which layers correspond and in how features transform between them? We study this by learning an activation alignment, a map from a source model's layerwise activations to a target's. Our method, MATCHA, factors this map into a layer map, whose output is an explicit target-by-source matrix that can be extracted and inspected, and a layer-shared feature map between hidden spaces. Most of prior work fixes the layer correspondence in advance, pairing layers at roughly the same relative depth; in contrast, we learn both factors jointly from prompts. Across 42 pairs of seven models spanning three different families, MATCHA reconstructs the target's activations more faithfully and improves retrieval-based metrics substantially, w.r.t. previous approaches. The recovered maps are broadly monotone in depth but, in contrast with most previous approaches, are consistently many-to-many: each target layer draws on a band of source layers. Our alignments also enable transfer of activation-space interventions, allowing steering vectors and probes developed for one model to transfer to another.

---


### 46. [Multi-Label Topic Assignment via LLM Distillation: A Comparative Analysis of Generative vs. Discriminative Student Models](https://arxiv.org/abs/2610.09063)

**<font color=#1a73e8>作者：</font>** Sourabh Kasliwal, Shubhranshu Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-label topic assignment for user-generated content (UGC) -- including product reviews and buyer-seller conversations -- poses unique scalability challenges in large-scale e-commerce due to informal language, extreme label sparsity, and rapidly evolving taxonomies. While utilizing Large Language Models (LLMs) as labeling oracles to distill ground-truth data has emerged as an industry standard to bypass prohibitive manual annotation costs, determining the optimal, low-latency architecture for the resulting student models remains an open challenge. To address this, we conduct a comprehensive evaluation across Small Language Model (SLM) parameter scales (1B, 4B, and 8B) and architectural paradigms (causal generative versus bidirectional discriminative). Comparing generative text-to-label classifiers against discriminative baselines (DeBERTa-V3 and ModernBERT), our analysis reveals a crucial data-dependent trade-off: while discriminative models outperform ultra-lightweight generative models on structured product reviews, even the smallest 1B generative model surpasses discriminative baselines on complex, multi-turn conversational data. Furthermore, generative models maintain robust performance under massive label-set expansion (up to 112 topics) and severe long-tail distributions, whereas discriminative baselines suffer a 35% drop in Macro-F1 at scale. Finally, we detail the successful production deployment of these optimized models across both product review and conversational domains, demonstrating strict latency compliance and tangible business impact at a global marketplace scale.

---


### 47. [TAP: Efficient Long-Horizon Agent Pruning via Trajectory-Anchored Recovery](https://arxiv.org/abs/2610.09074)

**<font color=#1a73e8>作者：</font>** Yuanzhe Li, Pengxin Wang, Yuxin Ren 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emerging long-horizon agentic tasks require repeated model calls, worsening the inference cost of already-costly language models. While narrow agentic tasks suggest potential for aggressive model pruning without performance drop, empirical results show existing methods proposed for question answering tasks severely degrade task performance when applied to agentic models. We trace this failure to two decisions: what to prune and how to recover. For pruning, one-shot importance estimates fail to track how the pruned model adapts. For recovery, offline distillation covers only teacher prefixes, while full-trajectory on-policy distillation causes student errors to compound across turns. In this work, we propose Trajectory-Anchored Pruning (TAP), the first structural pruning framework for reinforcement learning (RL)-trained agents. TAP couples structural pruning with efficient on-policy recovery, anchoring interactions to teacher trajectories while allowing the student to generate each reasoning-action response. A frozen dense teacher supervises the student's response prefixes, addressing within-response training-inference mismatch while preventing student-induced deviations from propagating across training turns. Instead of one-shot pruning, TAP re-scores channels using gradients of the recovery objective on the recovered student, connecting iterative channel selection to the evolving policy. With 60% of FFN channels removed, TAP retains 99.2% and 88.0% of the dense 7B agents' task success rates on ALFWorld and WebShop, respectively, while reducing GPU time per successful task by approximately 22% and 17%. These results demonstrate effective structural compression of long-horizon agents under a limited recovery budget.

---


### 48. [Move Fast and Mend Things: Keeping Up with Evolving AI Harms Using Social Media Commentary](https://arxiv.org/abs/2610.09082)

**<font color=#1a73e8>作者：</font>** Jacqueline Rowe, Animesh Srivastava, Sai Teja Peddinti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The rapid deployment of AI systems has created socio-technical, psychological, and operational harms that can elude ex-ante threat modelling and ex-post incident tracking. We introduce an LLM-assisted thematic analysis pipeline to dynamically detect, categorise, and track emerging AI harms from large-scale social media data. Applying it to 5.7 million Reddit post summaries over 18 months (01/2025 to 06/2026), we curate and release a dataset of 575,000 AI harm-related posts and a bottom-up AI harm taxonomy of 12 categories and 47 subnodes. The taxonomy reliably covers established expert-defined risks while surfacing granular harms that top-down frameworks overlook, such as distinct forms of AI privacy violations. Temporal analysis surfaces evolving user-centric harms, such as agentic privacy and security breaches, premature AI adoption in the workplace, and grief from AI companion discontinuation. Our pipeline shortens harm-detection timelines and hereby complements efforts towards more participatory and responsive AI governance.

---


### 49. [Anaximander: Interactively Running Geospatial Deep Learning Models on Any Compute Backend](https://arxiv.org/abs/2610.09085)

**<font color=#1a73e8>作者：</font>** Satej S. Soman, Akram Zaytar, Girmaw A. Tadesse 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Applying deep learning models to satellite imagery from within geographic information systems (GIS) remains high-friction for remote sensing practitioners. Models arrive in incompatible formats and target different compute environments, from local workstations to serverless cloud services. As a result, every evaluation demands custom deployment, tiling, and georeferencing code before a single prediction reaches the analyst's map. This friction discourages systematic comparison in a domain where model choice directly affects operational outcomes such as field delineation, crop monitoring, and disaster response. We present Anaximander, an open-source system that unifies model source and compute location choice behind one interactive interface. The system's backend is an inference server that loads models from multiple commonly-used sources and serves them on any accessible compute backend. The server provides session management and model caching, and streams results back per tile. The backend is paired with a QGIS plugin that drives tiling, result reassembly, georeferencing, and real-time per-tile status visualization. An additional user-interface path injects layer legends as prompts into vision-language models. We demonstrate the system in a code-free side-by-side comparison of three heterogeneous models on an agricultural field delineation task: gpt-image-1 via a cloud API, Segment Anything Model 3 (SAM3) on a remote GPU, and DelineateAnything on a local CPU. The inference backend and protocol are open-source and available at this https URL.

---


### 50. [U-Space: Uncovering When and Why Uncertainty Arises in Language Models](https://arxiv.org/abs/2610.09087)

**<font color=#1a73e8>作者：</font>** Tobias Braun, Nils Loose, Alexander Herzog 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are informing decisions with ever-higher stakes. As the consequences of their errors grow, a central question becomes harder to ignore: how much can we trust an individual answer? Yet recognizing when to defer remains difficult because language models can present incorrect conclusions with fluent explanations and an authoritative tone. Uncertainty quantification seeks to address this disconnect by estimating the reliability of individual predictions. However, many existing methods require repeated generations or separately trained components, and their scalar estimates do not reveal where uncertainty arises or how it evolves during reasoning. Recent work has also shown that generation length can be strongly associated with uncertainty estimates and correctness, raising the question of how much of an estimator's predictive power comes from uncertainty-specific information rather than output length alone. Mechanistic interpretability offers a way to address these limitations by connecting human-interpretable concepts to intermediate model states. Building on this capability, we introduce the U-Space, a low-dimensional subspace that makes a model's evolving uncertainty measurable and interpretable. We identify semantic anchors for doubt and certainty, map their unembedding directions back into the residual space, and combine their contrasts into an orthogonal basis. The U-Lens projects each token state onto these basis vectors, yielding an interpretable token-level uncertainty map that can be inspected directly or aggregated into a scalar uncertainty score. Our approach requires no correctness labels, repeated generations, or training. Across reasoning benchmarks, its confidence score outperforms established baselines under both standard and length-controlled evaluation and transfers more reliably than supervised estimators. Code: this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
