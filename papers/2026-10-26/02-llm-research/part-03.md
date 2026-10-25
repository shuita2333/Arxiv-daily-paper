# 🧠 大模型相关研究 | 2026年10月26日

> 本类共 **241** 篇论文：已确认 **225** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-241](./part-05.md)

---

### 101. [Building Presentation Intelligence for High-Quality Slide Generation](https://arxiv.org/abs/2610.30888)

**<font color=#1a73e8>作者：</font>** Yuhang Xie, Cheng Li, Chenliang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> PowerPoint presentations (PPTs) are a dominant medium for communication across diverse domains, yet high-quality PPT generation still depends heavily on labor-intensive human effort. Recent advances in large language models (LLMs) for agentic tasks have created both new opportunities and challenges (Chen et al., 2026) for automatic PPT generation. In this work, we present a unified training framework for automatic PPT generation toward presentation intelligence, integrating cross-validated data synthesis, guided teacher enhancement, and verifiable reward optimization. We first construct a cross-validated pipeline for data synthesis, with explicit control over both difficulty and validity. We then develop a teacher-enhancement framework grounded in rules and prior knowledge to substantially strengthen the instructional capacity of teacher models. Building on this, we further improve supervised fine-tuning (SFT) through a mixed-teacher strategy and a lightweight outcome-driven trajectory filtering method. Finally, based on the resulting SFT models, we introduce a suite of verifiable aesthetic metrics together with a GRPO-based reinforcement learning framework to optimize slide-level visual attributes beyond text-only supervision. Experiments show that our enhanced SFT pipeline improves Qwen-3.6-27B and Qwen-3.6-35B-A3B by 7.45 and 9.35 points on PresentBench, respectively, surpassing GLM-5.2 while maintaining strong generalization. Reinforcement learning further improves performance across five aesthetic dimensions, compensating for the limitations of SFT in visual refinement. Overall, the results demonstrate the effectiveness of our framework for high-quality PPT generation.

---


### 102. [Working Through Representation: Malleable Workspaces for Human-Agent Knowledge Work](https://arxiv.org/abs/2610.30893)

**<font color=#1a73e8>作者：</font>** Nan Chen, Long Ling, Luna K. Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI supports knowledge work, yet conversational histories may not capture the evolving organization that guides subsequent action. We introduce the Malleable Workspace, a conceptual model of how humans and agents form and revise a Work Representation and use its organization to advance work within a wider Work Environment. We developed it iteratively through conceptual analysis, comparison of 58 papers, and the construction and three-month longitudinal study of MalleableSpace with seven experienced agent users. Systems varied in what they represented as units and relations. System-assembled context was common; more systems supported local incorporation of agent outputs than reorganization, and fewer supported consequential agent-driven changes beyond the representation. The field study showed how representational roles and organization developed in use. These observations refined the model's account of how representation-grounded action depends on and can change the Work Environment. We contribute a conceptual and analytic foundation for representation-centered human--agent design.

---


### 103. [Your Home Remembers: A Voice-Enabled Household Memory Assistant for Conversational Retrieval](https://arxiv.org/abs/2610.30895)

**<font color=#1a73e8>作者：</font>** Aleix Sant, Jordi Luque, Fernando López 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Everyday household information is often exchanged in conversations but never written down, making details easy to forget or misremember. We present a voice-enabled smart-home assistant that acts as a household memory by recording conversations and retrieving information from stored and newly captured speech. The assistant runs on an Android tablet with a modular architecture in which speech-recognition, diarisation, embedding and language models can be configured or replaced through an orchestration layer. On-device wake-word detection and VAD-based query capture support hands-free interaction. Recorded audio is processed in configurable chunks, transcribed and diarised, converted into turn-aware passages with conversation-level timestamps, and indexed in a vector store. For memory queries, a retrieval-augmented generation pipeline selects key passages and uses them to generate an answer. The interface supports recording, conversation management and inspection of timestamped sources.

---


### 104. [Silicon Samples Match the Answers but Not the Respondents](https://arxiv.org/abs/2610.30900)

**<font color=#1a73e8>作者：</font>** Yusuke Kumagae, Masahiro Kaneko  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Silicon sampling generates survey respondents by having a large language model (LLM) answer a survey as a person with given demographic attributes, and the resulting synthetic populations are increasingly used in place of human ones. Existing evaluations focus on individual-answer accuracy, per-question answer distributions, and correlations across questions. None of these compares the respondents themselves, so a generator whose respondents have combinations of answers found in no human respondent can still score well if it reproduces every answer distribution. We propose the respondent coverage gap (RCG), which represents each respondent as a point defined by their complete answer profile and measures how far each human respondent is from the nearest generated one, relative to the distance between human samples. On two US social surveys, all six LLMs we evaluate leave human respondents uncovered, and under our main settings, they fall behind a baseline that samples each answer independently from the human marginals. Across the prompting and inference settings we test, every LLM has a higher RCG than a Gaussian copula fitted to the human data.

---


### 105. [Same molecule, Different Knowledge: Cross-Identifier Binding Failures in LLMs For chemistry](https://arxiv.org/abs/2610.30903)

**<font color=#1a73e8>作者：</font>** Khouloud Saadi, Di Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chemical AI workflows routinely represent the same molecule through multiple co-referring identifiers, including trivial names, IUPAC names, and SMILES, implicitly assuming that these representations provide interchangeable access to an LLM's knowledge. To test this assumption, we first introduce a controlled benchmark and show that it does not hold. Across foundation models spanning 7B to 72B parameters, even chemistry-specialized models, co-referring molecular identifiers consistently expose different subsets of the model's knowledge. We then conduct a series of controlled behavioral, representational, and causal analyses to characterize this failure. We show that even when a model can identify a molecule from its SMILES and retrieve a fact through the corresponding name, the same fact can remain inaccessible directly from SMILES. We term this phenomenon \emph{cross-identifier binding failure}. Further analysis of internal representations, conflicting identifiers, and parameter editing shows that neither improved chemical representation competence nor modification of individual facts is sufficient to establish reliable access across identifiers. Together, these results indicate that the core failure lies in the binding between an identifier and knowledge already present in the model. Motivated by this diagnosis, we introduce Binding Self-Distillation, a simple mitigation that uses lexical identity during training to transfer the model's existing knowledge access to the structural route. This enables factual retrieval directly from SMILES at inference time, without requiring a name lookup or training the underlying model from scratch.

---


### 106. [TwinStore: A Synthetic Consumer Platform Using Vision--Language Models](https://arxiv.org/abs/2610.30909)

**<font color=#1a73e8>作者：</font>** Minhyeok Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present TwinStore, a source-available synthetic consumer platform for physical retail built on vision--language models. TwinStore turns a store into a digital twin---from 82 ready-made formats, a floor-plan image or phone photos of its shelves---and fills it with synthetic shoppers who plan a trip, walk the aisles and decide what to buy by looking at rendered shelves with packs, price tags and promotion signs. Every trip ends in a receipt, so a layout, price, pack or promotion can be tried on the same shoppers before it reaches the store. Around this core, TwinStore provides 3D playback, paired comparisons and layout optimization, shopper interviews, a trade-area model, counterfactual edits of real shelf photos, a marketing studio with eleven tools, and an assistant that turns a plain sentence into a drafted study or an answer grounded in a run's own numbers. In a held-out validation on eleven public datasets, simulated receipts approach the households' own natural variation (category-mix divergence 0.017--0.018 against a real drift of 0.012), price elasticities fall inside the range measured in the field, and three independent decision models agree. TwinStore runs on cloud or on-device models and is distributed with installers for Windows, macOS and Linux.

---


### 107. [Watch and Learn: Teaching Visual In-Context Learning by Removing Textual Shortcuts](https://arxiv.org/abs/2610.30913)

**<font color=#1a73e8>作者：</font>** Nimrod Shabtay, Asaf Yehudai, Avihu Dekel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) struggle with in context learning compared to their textual counterparts. Our preliminary study shows that VLMs rely on textual shortcuts and underutilize the visual demonstrations. We therefore hypothesize that VLMs are insufficiently trained to perform visual in-context learning (vICL). To this end, we construct MIME, a task-agnostic vICL training set without textual shortcuts. We ensure the instruction does not state the rule linking the demonstration images to their answers, so the model must infer it from the visual demonstrations. Fine-tuning on MIME improves vICL accuracy by 8.1 to 18.0 points across three VLMs, preserves single-image performance, and improves multi-image and text only in-context learning. In contrast, stating the rule in the training data sharply reduces this gain. We further propose DTAD (Demonstration Text Attention Dropout), which randomly withholds demonstration labels during training so that the VLM must infer the rule from the demonstration images. While achieving comparable vICL accuracy to fine-tuning on MIME, DTAD yields more consistent attention to the demonstration images. On TrueMICL, Qwen3-VL-8B trained on MIME matches frontier models such as Claude Opus 5, and surpasses them with DTAD. Finally, adding MIME to the instruction-tuning mix of LLaVA 1.5 13B more than doubles its vICL accuracy without hurting single-image abilities, whereas a same-size multi-image set improves it only slightly. These results suggest that vICL data should be a standard component of VLM training.

---


### 108. [Harnessing Language Models as Optimization Modeling Agents](https://arxiv.org/abs/2610.30917)

**<font color=#1a73e8>作者：</font>** Yunxiang Luo, Xin Xu, Tianhao Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can translate natural-language optimization problems into solver programs, but reliably producing correct formulations and implementations remains challenging. Existing approaches improve optimization modeling through agentic workflows or task-specific post-training. This raises a practical question: can a lightweight harness using a single model role achieve competitive performance without additional training? We introduce OPTICYCLE and OPTISTATE, two lightweight inference harnesses for optimization modeling, and evaluate them on nine benchmarks comprising 2,634 problems using 11 Qwen variants spanning 0.6B-27B parameters. Our results show that execution-guided revision consistently improves macro accuracy over direct generation for all evaluated models, with gains of up to 49.46 percentage points. Despite their simplicity, both harnesses outperform six adapted agentic workflows in same-model comparisons and four evaluated post-trained optimization models at comparable model sizes, without additional training. Explicit formulation state provides further but model-dependent improvements, suggesting that additional structure is not universally beneficial.

---


### 109. [DConstrain: Compiling Context-Parameterized Transitions for Diffusion Language Model Constrained Decoding](https://arxiv.org/abs/2610.30920)

**<font color=#1a73e8>作者：</font>** Shidong Cao, Jing Ma, Wenhao Chai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) decode multiple tokens in parallel, so individually valid tokens can be incompatible together under a schema. Exact joint inference over a grammar graph enforces compatibility, but it requires token-labeled successors across many hypothetical parser configurations. Encoding stacks and field histories in compiled states can cause exponential growth, which forces prior exact decoders to fix property orders and exclude valid outputs. We present DConstrain, which compiles schemas into context-parameterized transition programs. Cold compilation specializes token consumption to local grammar states while retaining context-dependent stack operations, environment guards, and caller-dependent deferred parsing symbolically. Tracking field histories as runtime values supports arbitrary property order without enumerating field subsets offline. At runtime, warm compilation binds reached configurations to these programs to construct exact successors, overlapping with the model forward pass because graph construction requires no model scores. Furthermore, token-effect grouping merges tokens with identical compiled effects before runtime contexts are bound, so groups are reused across stacks and environments even when concrete successors differ. Objective-specific score aggregation and token restoration provably preserve both the Viterbi optimum and the token-labeled path distribution of ungrouped inference. Across three benchmarks and two DLM families, DConstrain compiles 100% of BFCL schemas under arbitrary property orders, whereas an optimized finite-state baseline compiles only 71.30-85.81%. Under arbitrary property order, it reduces BFCL end-to-end decoding latency by 6.65-46.26 times with 100% schema validity and raises DiffusionGemma's BFCL accuracy from 37.27% under fixed order to 81.56%.

---


### 110. [Making MLLM Latents Matter: Factor-Aware Predictive Learning for Cinematic Video Generation](https://arxiv.org/abs/2610.30926)

**<font color=#1a73e8>作者：</font>** Songlin Yang, Zhe Wang, Xiaotong Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cinematic video generation requires both temporal inference from limited inputs (i.e., sparse rather than frame-by-frame guidance) and factor-aware control of character, scene, action, and camera. Multimodal large language models (MLLMs) offer useful priors for both capabilities, but their representations are not automatically actionable for video generation: a Video Diffusion Transformer (DiT) may bypass them through native conditioning pathways, and using them does not ensure either factor-aware control or generation-compatible temporal prediction. We propose Factor-Aware Predictive Learning (FAPL), which establishes effective MLLM latent use as a shared prerequisite and then targets the two capabilities with complementary learning signals. First, latent-only generator grounding trains the DiT with a frozen MLLM and connector, strengthening the DiT's use of MLLM latents for generation. Second, for factor-aware control, paired videos specify a target-factor change and non-target preservation, and factor-span replacement trains the DiT to realize this relationship in its output. Third, for temporal inference, text-only and text-plus-complete-video observations share a video target, and the trained DiT is then frozen while the MLLM and connector are optimized through it. This final stage trains limited-input representations for generation while retaining complete-observation reconstruction as a complementary training mode. Extensive experiments demonstrate our consistently better performance on three cinematic video generation tasks (i.e., sparse-to-video, factor-aware editing, and multi-shot generation) over baselines and validate FAPL's contributions to MLLM feature use, temporal control, and factor coordination.

---


### 111. [ReflectPO: Reflection-Guided Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2610.30933)

**<font color=#1a73e8>作者：</font>** Rumei Li, Xunliang Cai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With external tools, large language models (LLMs) can tackle complex tasks through sustained environmental interaction. LLM-based agents are therefore increasingly used to tackle complex long-horizon tasks in real-world environments. However, these tasks involve sequential, interdependent decisions and changes in environmental states. Early execution errors affect subsequent interaction histories and environmental states, and their effects accumulate along the decision chain. To address this challenge, we propose Reflection-Guided Policy Optimization (ReflectPO), a reinforcement learning framework for autonomous error recovery in long-horizon tasks. ReflectPO comprises two core components. The first is Reflection-Guided Sampling. We use branch differences and repeated visits in interaction trajectories to construct hints for error recovery. The second is Tree-Structured Credit Assignment. We organize sampled trajectories into trees and assign action-level credit using parent--child reward differences and recovery gains. Experiments over two long-horizon tool-use benchmarks show that ReflectPO outperforms multiple existing baselines in most domains. It also achieves the best overall performance on average. Further analyses show that ReflectPO effectively improves agents' ability to recognize their own deviations, recover from erroneous states, and continue making progress toward task completion.

---


### 112. [Verbalizing Activation Differences with Natural Language Autoencoders](https://arxiv.org/abs/2610.30934)

**<font color=#1a73e8>作者：</font>** Andrea Blasi Núñez, Gianluca Barmina, Federico Torrielli 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation verbalizers translate the internal representations of large language models into human-readable text. The recently proposed natural language autoencoders (NLAs) learn this by reconstructing activations through a natural language bottleneck. However, it remains unclear how well these methods generalize beyond the setting they were trained for. Here, we study this question for NLAs along four closely related questions: (i) Do NLA verbalizations exhibit compositional structure with respect to their input? (ii) Do NLAs generalize to finetuned versions of the model they were trained for? (iii) Can NLAs recover finetuning objectives in model diffing? (iv) Can NLAs be specialized for model diffing? Across four models from three families, our experiments provide evidence supporting a largely positive answer to all four questions. Specifically, verbalizations of composed analogy activations mostly name the target while rarely mentioning the subtracted word, and an NLA can be reused on lightweight finetunes of its original model without retraining, with reconstruction quality degrading noticeably only for the largest model. Verbalizing activation differences between Taboo model organisms and their original models recovers the concealed secret word for most organisms, and reinforcement learning on activation differences further improves this recovery on held-out organisms. We also find that NLAs can recover the finetuning objective without the finetuned model generating any token, since the most informative token positions precede the user prompt. NLAs do not yet match state-of-the-art model diffing methods on the emergent misalignment detection task, but outperform a blackbox baseline. Our findings suggest that NLAs can meaningfully verbalize differences in activation space, rendering NLAs a promising direction for future work.

---


### 113. [Metacognitive Scaffolds Create Productive Friction for AI-Assisted Knowledge Work](https://arxiv.org/abs/2610.30945)

**<font color=#1a73e8>作者：</font>** Viktor Kewenig, Lev Tankelevitch, Sean Rintel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI imposes new metacognitive demands on knowledge workers as their work shifts from production to planning, evaluation, and orchestration. In a randomized, between-subjects experiment on AI-assisted writing (297 workers, 594 essays), we test dynamically-generated metacognitive scaffolds supporting goal specification and task decomposition. We find that scaffolds improve writing quality, with this boost persisting in short-lag transfer when scaffolds are removed. We also find evidence of improved topic recall three days later. These effects are consistent with observed changes in how people learn to prompt AI systems after exposure to scaffolding. However, scaffolded participants rate the AI as less helpful and more cognitively demanding even as they perform better, suggesting that subjective ease can understate the value of support. Our findings make the case for metacognitive scaffolds in AI-assisted knowledge work, revealing a productive friction worth designing for as workers increasingly delegate work to agentic AI.

---


### 114. [RetiJev: Fast and Source-Grounded Ophthalmic Decision Models](https://arxiv.org/abs/2610.30947)

**<font color=#1a73e8>作者：</font>** Bo Liu, Lianyu Wang, Meng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ophthalmic clinical decision support requires fast, accurate, and privacy-preserving inference, yet autoregressive large language models (LLMs) incur substantial latency and computational overhead for decisions among predefined actions. We therefore investigate a decision-oriented alternative to generative reasoning. Specifically, we first introduce RetiJev-Data, a source-grounded ophthalmology corpus comprising 78,158 clinical-decision and diagnosis questions derived from articles in PubMed Central and a MeSH vocabulary covering 531 eye diseases, and 50,074 guideline-grading questions spanning 11 grading systems, along with a 24,662-question evaluation benchmark. Based on this, we develop RetiJev, a family of 0.8B-9B decision models that directly score candidate answers without autoregressive decoding. Across all model sizes, RetiJev outperforms both a 27B LLM and the commercial Jev 1.13 decision model on guideline grading by 10.4-23.0 points. RetiJev-9B further achieves the highest accuracy on clinical decisions, improving over both baselines by 5.4-6.5 points while matching them on diagnosis. It answers a case in 158 ms on one GPU, 3.5x faster than LLM generation and 470x faster than reasoning. Models are released at this https URL.

---


### 115. [IQuest-Q1: Advancing Foundation Capabilities for Agentic CLI Systems](https://arxiv.org/abs/2610.30949)

**<font color=#1a73e8>作者：</font>** A. Jian Yang, An Huang, Bo Dan 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present IQuest-Q1, a sparse Mixture-of-Experts (MoE) agentic foundation model with 320B total parameters (15B activated). IQuest-Q1 is developed through a three-stage process: (1) stable and efficient pre-training, combining Stable SplitNorm, Muon, and muP with a two-stage curriculum whose second stage increases the coding-data mixture, preserving a wide stability margin between safe and optimal learning rates; (2) fine-grained mid-training, expanding the data mixture across domains and formats and progressively extending the context; and (3) multi-scaffold with multi-version post-training, combining SFT, domain-specialized RL, and MOPD across various scaffolds to integrate complementary training signals and strengthen agentic coding capabilities. Furthermore, model merging combines different experts and checkpoints from different stages while mitigating conflicts among their parameter updates. The resulting IQuest-Q1 demonstrates capabilities in both coding and general tasks. We release IQuest-Q1 as an open-source model to support community research and development.

---


### 116. [OpenAttention: One Percent Is Enough with Tail Proxies](https://arxiv.org/abs/2610.30951)

**<font color=#1a73e8>作者：</font>** Hyunwoo Yu, Jongbeom Lee, Hyunbin Kim 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse attention reads only a small subset of the key-value cache, and how to treat the unread tail remains a key challenge. Discarding the tail biases the output, and sampling it as previous approaches do fails at reads of 5% and below, where the tail likely holds heavy hitters the selector missed. Our key observation is that the simplest possible proxy, one token that folds the entire tail into its count-aware mean, already yields lower output error than a sample at every read behind a practical selector. We further show in closed form that at low reads sampling nearly doubles the weight error of discarding while a single proxy stays below it. Building on these findings, we explore approximating the dense attention distribution with a few proxies that target the tail. We propose OpenAttention, a pipeline of clustering, ErrorGate and top-k selection followed by a count-aware mean proxy. To implement clustering and selection both efficiently and effectively, we design training-free Query-Geometry Clustering (QGC) and a Query-Geometry Selector (QGS), which compress the keys while respecting the query directions. Additionally, unlike prior methods that rank clusters by centroid alone, ErrorGate allocates the exact read by the estimated weight error of each cluster. On RULER-32K HARD with Llama-3.1-8B, OpenAttention retains 99% of dense accuracy at a 1% read. It also achieves state-of-the-art accuracy across models, context lengths and datasets. Our customized attention kernel, this http URL, runs the decode attention stage 10$\times$ faster than dense attention at a 1% read.

---


### 117. [Measuring the Reasoning-Action Coupling in Driving Vision-Language-Action Models through Counterfactuals](https://arxiv.org/abs/2610.30953)

**<font color=#1a73e8>作者：</font>** Gabriel Manalu, Saad Wazir, Thao Do 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Driving vision-language-action (VLA) models bring an appealing form of explainability to a safety-critical domain, since a system that can state the reasons for its maneuvers offers the transparency that deployment and public trust in autonomous driving demand. These models read the world into language before they act on it, describing the scene and reasoning over it in text that ranges from chain-of-thought to multi-stage question answering on the way to a trajectory. That framing quietly assumes two separable properties, namely that the trajectory follows the generated reasoning and that the generated reasoning tracks the causes that actually produce the trajectory. To thoroughly investigate these properties, we apply causal, counterfactual interventions to four driving VLAs across different benchmarks. First, we perturb the models' own reasoning and show that altering its meaning produces small trajectory changes relative to blanking the same models' camera inputs, a pattern that persists across benchmarks and model architectures. We then construct scene-level counterfactuals through photorealistic removal of key objects named in the models' reasoning and analyze whether the generated reasoning and trajectories track these changes. Overall, our findings indicate that the reasoning these models present to account for their resulting driving behavior is weakly coupled to that behavior itself, pointing to limits on the explainability these systems are intended to provide.

---


### 118. [Once a Tree, Always a Tree? Cross-lingual Transfer of Hierarchical Generalization in Language Models](https://arxiv.org/abs/2610.30960)

**<font color=#1a73e8>作者：</font>** Shin Yamaguchi, Masaya Taniguchi, Tatsuki Kuribayashi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models (LMs) often exhibit successful cross-lingual transfer through continued (pre)training, still their underlying process remains unclear. One possibility is that LMs can leverage the evidence toward language-universal principles, namely, hierarchical structure, from a source language (L1) to a new language (L2), while many other non-linguistic explanations, e.g., improved initialization of position embeddings, can be potentially possible. In this study, to quantify the cross-linguistic transferability of linguistic evidence in cross-lingual LM training, we introduce a new experimental design, namely, a cross-lingual poverty-of-stimulus (CPOS) setting that ablates how LMs' hierarchical generalization in L2 can be led by structural evidence provided in L1. We contrast counterfactual L1 and L2 learning scenarios where the L2 corpus is ambiguous between linear and hierarchical grammar rules, while the amount of positive evidence for the hierarchical rule is controlled on the L1 side. Our experimental results show that LMs can partially, yet not perfectly, transfer L1 structural evidence to L2, yielding only a small but detectable hierarchical bias, while the strength of transfer depends on language pairs. We further ablate the conditions for successful transfer, motivated by recent reports on the substantial impact of vocabulary overlap. We indeed find that vocabulary overlap is crucial even for the cross-lingual transfer of hierarchical syntactic generalization. This suggests that this also explains the language-pair-dependent tendencies in the main experiments and suggests that the transfer of linguistic evidence in continued new-language learning is only conditionally achievable.

---


### 119. [ReDence: A Hybrid Agentic and Decision-Model Framework for Rapid, Evidence-Grounded Detection of Modern Social Engineering Scams](https://arxiv.org/abs/2610.30963)

**<font color=#1a73e8>作者：</font>** Jaishnoor Kaur, Josef Horáček, Ian Waskom 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Detecting online social engineering (SE) scams often requires examining website workflows, verifying claims against external sources, and connecting evidence across multiple pages. Existing detectors provide limited support for these investigations, leaving analysts to manually gather and validate evidence, which inevitably delays detection and subsequent takedown of these attacks. To address this gap, we present ReDence, an open-source hybrid framework for adaptive, evidence-grounded detection across diverse SE scam categories. ReDence combines two locally hosted models with complementary responsibilities: a fine-tuned multimodal agentic Investigator (Qwen3.5-4B) that performs investigative planning, evidence interpretation, and reporting, and a specialized Decider (Tev1) that handles binary and multiple-choice tasks, including browser-action selection, evidence assessment, and decisions about whether to continue an investigation. By delegating discrete decisions to a specialized model, ReDence reduces reliance on lengthy language-model responses, while preserving the reasoning capabilities required for complex investigations. Our evaluation demonstrates that ReDence achieves 96\% accuracy in detecting scams across twelve SE scam categories, substantially outperforming existing detectors while being at least four times faster than comparable agentic models without compromising investigative depth. ReDence also produces structured, evidence-grounded reports that document investigative actions, supporting and contradictory evidence, and collected artifacts, which allow analysts to independently audit detection decisions and utilize the collected evidence to support subsequent mitigation and takedown efforts.

---


### 120. [Joint or Per-Option? Compact Encoders for Closed-Set Decisions from 17 Million to 1 Billion Parameters](https://arxiv.org/abs/2610.30970)

**<font color=#1a73e8>作者：</font>** Tardelli Ronan Coelho Stekel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many language-model pipelines end in a closed-set decision, such as selecting a tool. Prompting a large language model for it is slow and order-sensitive. We ask how small an encoder for such decisions can be and whether it should read the options jointly or separately. In a three-seed study at 32 million parameters, per-option scoring beats joint scoring on a held-out sample of a 37-benchmark decision suite by 5.8 points of chance-corrected skill at matched optimizer steps and by 2.8 at approximately matched training compute; two external benchmarks agree, though not significantly on their unseen tasks. Crossing reader with initialisation shows that the advantage requires a reranker initialisation, whose query-candidate pair input matches per-option reading; from the raw encoder the two readers are indistinguishable. Per-option scoring needs 5 to 13 times more encoder passes: at most twice the median latency, but more than four times the mean. Of six released joint encoders (17 million to 1 billion parameters), the 68- and 150-million-parameter models exceed a 435-million-parameter DeBERTa-v3 zero-shot classifier by 4.9 and 5.9 accuracy points on 209 overlap-audited System1-Arena tasks and are at least on par with it on the 145 tasks unseen in training. The smallest answers a median request in 14 milliseconds on 16 processor threads, against 728 for the classifier. Reordering options changes 12 to 23% of the joint models' answers (per-option scoring: none). Up to 68 million parameters, they lead their size range on a public leaderboard's private, mainly in-distribution tests.

---


### 121. [Diagnostic Loss: Asymmetric Supervision for Radiology Report Generation](https://arxiv.org/abs/2610.30980)

**<font color=#1a73e8>作者：</font>** Ignacy Kolton, Wenxuan Li, Zongwei Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated radiology report generation requires models to do more than produce fluent clinical narratives: they must explicitly state supported diagnoses while avoiding unsupported ones. However, existing medical vision-language models (MedVLMs) are typically trained with token-level maximum likelihood objectives, which prioritize text agreement over diagnostically critical terms. As a result, models can miss key diagnoses and introduce wrong ones. We identify this as an objective misalignment between conventional language modeling and the asymmetric diagnostic requirements of radiology reporting. To encode these requirements, we introduce Diagnostic Loss (DLoss), a differentiable, architecture-agnostic objective that operates directly on decoder token probabilities. DLoss separately aggregates probability mass over vocabularies associated with diagnoses supported by the reference report and with unsupported alternatives. Using asymmetric pooling across token positions in the report, it encourages supported diagnoses to receive sufficient probability in at least one position while suppressing spurious probability spikes for unsupported diagnoses across all positions during training. The loss can be applied to existing 3D MedVLMs without modifying their vision backbones, language decoders, or inference procedures, and introduces no additional inference-time computation. We train and evaluate DLoss on 50,000 abdominal CT scans across several 3D MedVLM architectures on both in-distribution and out-of-distribution report-generation benchmarks. Across these settings, DLoss improves diagnostic faithfulness while maintaining competitive performance on conventional language-generation metrics, showing the value of asymmetric sequence-level supervision for radiology report generation. The code for DLoss is available at this https URL.

---


### 122. [A Reality Check of Inference-Time Context Augmentation Methods](https://arxiv.org/abs/2610.30983)

**<font color=#1a73e8>作者：</font>** Haeun Yu, Geert Heyman, Pepa Atanasova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often fail to utilise the context given in the input, resulting in hallucinations or a fallback to parametric knowledge. Context augmentation methods aim to improve model performance by modifying the input, from inserting filler tokens that add computational time to adding relevant content such as elaboration of a context during inference. However, these methods have been evaluated in isolation and only by their performance gains, leaving it unclear how they compare and whether they reliably improve performance. In this paper, we present an evaluation framework spanning five methods that differ in how informative the inserted content is and apply them at the sentence level across seven models spanning multiple sizes on three datasets. We find that accuracy gains are not always genuine improvements but undirected perturbations: the methods correct some predictions while breaking others, particularly when the inserted text allows only for more computational time. Our analysis reveals that methods that bring no additional content primarily change model predictions near the decision boundary. Our findings highlight the need to evaluate the reliability of the accuracy gains before adopting them in practice.

---


### 123. [EEG-Captioner: Grounding EEG-to-Language Generation in Fundamental Signal Properties](https://arxiv.org/abs/2610.30995)

**<font color=#1a73e8>作者：</font>** Leyuan Jin, Jiahao Mei, Yixuan Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG)-to-language models offer a promising approach for translating complex neural signals into human-readable descriptions. However, generating plausible language does not necessarily demonstrate that a model has learned to interpret the underlying EEG signal. A direct way to assess such interpretation is to probe objectively measurable properties of the signal itself. We therefore construct an EEG-language dataset of 160,781 segments annotated with signal-level question answering (QA) pairs, where each question targets one of five property families and requires a quantitative comparison involving spectral, spatial, temporal, or lateral signal properties. Each segment is also paired with a feature-grounded EEG caption. We further propose a Dual-Domain EEG Encoder that jointly models temporal waveforms and spectral-spatial representations, and introduce EEG-Captioner, a unified EEG-to-language framework trained with both signal-level QA and EEG caption supervision. Experiments show that the proposed encoder achieves the highest overall macro-averaged balanced accuracy (Macro-BA) among the compared EEG encoders, while EEG-Captioner achieves a Macro-BA of 88.81% on signal-level QA and improves caption factual consistency from 82.06% to 83.46% over caption-only language adaptation, demonstrating the complementary benefits of signal-level QA and caption supervision.

---


### 124. [Padding to k: A Minimum Count in the Schema Makes Open-Weight Models Pad Their Extraction Lists](https://arxiv.org/abs/2610.30997)

**<font color=#1a73e8>作者：</font>** Abhishek Barali, Aayush Paudel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extraction pipelines ask language models for JSON that follows a schema, and the schema can set a minimum number of list entries. We ask what models do when the document holds fewer items than that minimum. Under a preregistered plan, we test eight open-weight models on 558 real documents from nine annotated datasets, with six more models on hosted services as a reference. Three findings stand out. First, models treat the count as a target: a minimum shown in the schema, but not enforced, raises the share of lists longer than the true count from 34.5% to 55.4%. Second, the padding is hard to catch, because most added entries are real text taken from the document; about half of them pass a check that each entry occurs in the source. Third, common fixes help only partly: a line saying fewer items are fine removes the effect on average but misses more true items, a count in prose ("up to k") also raises over-counting, an "N/A" option under an enforced minimum still leaves half the lists padded, and re-asking with the validation error makes padding far more common. We release the code, answer lists and run records at this https URL

---


### 125. [SecLog-Bench: A Scalable Benchmark for Cybersecurity Log Reasoning with Scaffolded Evidence](https://arxiv.org/abs/2610.31000)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Dongliang Xu, Xiaoyong Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong potential for cybersecurity, leading to growing interest in LLM-based automated cybersecurity log analysis. However, current datasets (1) are limited in scale; (2) rely mainly on single-source evidence; and (3) have only binary or multi-class attack labels, without dense annotations of the reasoning process. To address these limitations, SecLog-Bench has three key features. First, we build an extensible simulation platform that covers 29 attack scenarios, supports repeated execution and the integration of new scenarios, and enables scalable generation of cybersecurity logs with attack-stage labels. Second, we use multi-source logs, including audit logs, application logs, and network traffic, to jointly analyze cyber attacks. Third, we annotate each sample with the essential context for cybersecurity log reasoning and a structured step-by-step evidence chain. We evaluate eight mainstream LLMs on this benchmark for post-detection attack-progress reasoning. Results show that, when provided with scaffolded evidence, current LLMs exhibit modest capability in attack-progress reasoning, with the best model achieving only 44.44% accuracy and 45.07% Macro-F1. Their reasoning remains unreliable; i.e., the highest Stage Reasoning F1 (SRF1) score is only 54.87%. Moreover, even correct predictions may be accompanied by flawed reasoning, and reasoning quality is often misaligned with prediction accuracy.

---


### 126. [Agri-SCHOLAR: Simulation-Grounded In-Season Rolling Advisories for Agricultural Crops Using LLM-Bounded Optimization](https://arxiv.org/abs/2610.31003)

**<font color=#1a73e8>作者：</font>** Geetha Charan, Vedant Balasubramaniam, Manojkumar Patil 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing agricultural advisories to farmers suffer from several limitations: (a) remain largely expert-driven, (b) do not adequately account for in-season weather, and (c) do not scale to individual farms. In this paper, our objective is to close these gaps by developing Agri-SCHOLAR (Simulation-Grounded Crop Harvest Optimization with LLM-Guided In-Season Advisory Rollouts). Agri-SCHOLAR is a rolling, in-season advisory framework that issues, at intervals of every few days or every week, a personalized advisory using the following information: soil and crop properties, observed weather to date, short-range forecast of weather, and a season extrapolation of weather based on historical analogs. The novelty and depth of Agri-SCHOLAR lies in each advisory being produced by a closed-loop system which couples multiple LLM agents with a powerful crop simulator (such as APSIM in our case). The simulator crucially serves as an evaluation oracle. In Agri-SCHOLAR, the LLM agents propose agronomically sound and feasible bounds on actionable parameters and an optimizer searches within those bounds against a multi-objective reward spanning yield, resource utilization, and economic feasibility. We conduct a detailed 11-year analysis of the maize crop in two selected locations of South Asia and show that Agri-SCHOLAR consistently outperforms the region's standard packages of practice and satisfactorily addresses the limitations of existing agricultural advisories.

---


### 127. [Mitigating Saliency Collapse: Robust Saliency-Aware Long-Text Image-Text Alignment](https://arxiv.org/abs/2610.31005)

**<font color=#1a73e8>作者：</font>** Qiuyu Kong, Zanxi Ruan, Marco Cristani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-text image-text alignment is essential for fine-grained scene understanding, yet existing methods mainly focus on extending context length or improving local alignment. We identify an overlooked failure mode, saliency collapse, where models over-rely on text that features visual prominence while underutilizing non-salient context. Consequently, retrieval performance degrades sharply when salient content is reduced, despite that the non-salient context remains informative. To address this, we propose RoSA, a saliency-aware finetuning framework that decomposes image-text pairs into complementary salient and contextual views, enabling joint learning of prominent and contextual semantics. We propose a modality-independent decomposition strategy to combine object-level visual saliency estimation with LLM-based text decomposition to bridge vision and language. We employ auxiliary objectives to explicitly align these views, ensuring robust representation with both salient and contextual features. RoSA greatly improves long-text retrieval and demonstrates strong robustness to saliency collapse across benchmarks. Moreover, our auxiliary objectives are plug-and-play, bringing consistent gains to existing tuning methods. Code and checkpoints are available at: this https URL

---


### 128. [Evaluating Artificial Wisdom (AW): A Trajectory-Based Framework for Context-Sensitive Decision Regulation](https://arxiv.org/abs/2610.31012)

**<font color=#1a73e8>作者：</font>** Md. Jalil Piran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Capability benchmarks measure what large language models can do, but not whether their recommendations remain appropriate as decision conditions change. This paper proposes a trajectory-based measurement framework and prospective validation protocol for artificial wisdom, defined behaviorally as context-sensitive regulation of judgment. Versioned reference specifications determine admissible responses and transition materiality before evaluation. Seven stage-level criteria assess judgment under current conditions, while two transition components assess material-update adequacy and commitment-preserving stability. Stability requires prior adequacy; switching within registered commitment classes is permitted, and persistent error earns no stability credit. A nine-component profile is primary, with a secondary bottleneck score and separate critical-failure reporting. Three simplified simulations examine precision, bottleneck estimation, and sensitivity to model-family count. A single-criterion simulation met its precision criteria at 24 scenarios per domain. Near a bottleneck tie, the estimated minimum had a downward bias of 0.55 points at that size. A simplified incremental-prediction simulation detected a Brier improvement of 0.027 with probabilities of .508 and .742 using eight and twelve families, respectively; it does not establish power for the operational protocol. An exploratory predecessor-rubric study comprising 71 evaluation records illustrates aggregation sensitivity but does not validate the proposed instrument. The twelve-family target remains provisional pending feasibility assessment and calibration of the complete analysis. Whether the profile predicts independent decision outcomes beyond capability remains an open empirical question.

---


### 129. [Mostly Reading: What Open-Book Scores Measure in Document-Level LoRA Adapters](https://arxiv.org/abs/2610.31017)

**<font color=#1a73e8>作者：</font>** Martino M. L. Pulici, Cuong Xuan Chu, Evgeny Kharlamov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Single-document LoRA adapters have been proposed as units of knowledge to be merged and retrieved; yet open-book scoring, with the document in the prompt, can credit a document's own adapter (its specialist) for reading that document as readily as for holding it. Training one adapter for each of 150 Wikipedia articles on Llama-3.1-8B-Instruct, we find that open-book scores mostly measure a reading behaviour every adapter shares: a random adapter trained on another document recovers 82 % of the specialist's open-book advantage over the base model but only 2 % of its advantage on a cloze probe that asks for the same document's facts without providing the source text, a share we cannot distinguish from zero. Content does reach the weights, since the specialists beat the base model in cloze recall by 0.094, and the geometry of their updates follows the documents they read; yet, in a test of 30 queries, adapters chosen by weight-space proximity or text embedding are not distinguishable from random ones on either probe, although that test cannot exclude an advantage of about four fifths of what a query's own adapter gains over a random one. At 16 documents or more, correctly scaled merges recover 87 % to 89 % of the specialists' open-book advantage but only 12 % to 16 % of their cloze advantage, with intervals that run from below zero to at most 32 %, against 94 % for joint this http URL also report four silent errors, each of which produced a clean, wrong result.

---


### 130. [Chunk Recomputation under Real Document Revisions: Measuring Update Cost and Retrieval Quality of Fixed, Recursive, and Content-Defined Chunking](https://arxiv.org/abs/2610.31019)

**<font color=#1a73e8>作者：</font>** Yuning Bian, Lele Xu, Yifan Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chunking strategies for retrieval-augmented generation are almost always evaluated on a static snapshot, yet the documents underlying a knowledge base continue to change. Because chunks are embedded independently, a boundary that moves after an edit forces unchanged text to be re-embedded. We measure this update cost on 120 pairs of adjacent Chinese and English Wikipedia revisions for three stateless chunkers (non-overlapping fixed-size, recursive paragraph-first, and content-defined chunking) under a strict byte-identical reuse rule and a frozen dense encoder. On the 116-article common-success pool, with frozen, length-calibrated parameters, fixed-size chunking recomputes 57-68% of its full new-version embedding-input workload, recursive chunking 38-56%, and content-defined chunking 43-54% (it failed on 4 of 62 Chinese articles), while at these parameters mean evidence recall under a fixed 2048-token retrieval budget differs by less than two percentage points within either language. A cost-only parameter grid shows that the ranking of the two content-aware chunkers changes with chunk-length settings, whereas non-overlapping fixed-size chunking has the highest recomputation cost in every length-matched condition. Controlled edits and a verbatim-presence diagnostic support boundary drift as one contributor to recomputation of text already present in the previous version. Update cost is therefore a substantial, parameter-sensitive dimension that static retrieval evaluations do not expose and that should be reported alongside retrieval quality.

---


### 131. [Directing to Diversify: Multi-Directional Search for Automatic Heuristic Design](https://arxiv.org/abs/2610.31048)

**<font color=#1a73e8>作者：</font>** Jianghan Zhu, Jianan Zhou, Fei Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong potential to automate heuristic design for NP-hard combinatorial optimization (CO) tasks without human intervention. Recent methods predominantly rely on evolutionary computation (EC) frameworks, where heuristic diversification is mainly induced through EC-like operators or downstream selection, while the direction of heuristic transformation remains largely unharnessed. In this paper, we propose a multi-directional Perturbation-Rewrite Search (PRS) framework for automatic heuristic design that factorizes heuristic transformation through directional search primitives at the generation level. Specifically, PRS operates on heuristic ideas through three complementary directions: expansion toward richer and more expressive designs, compression toward simpler and less specialized designs, and steering for fine-grained refinement, together enabling broader and more sustained exploration of diverse regions in the heuristic design space. PRS further organizes candidate exploration within a breadth-first search-based process with adaptive operator control, which ensures thorough candidate utilization and sustained exploration, and maintains strong search dynamics while preventing premature convergence. Extensive empirical results across diverse CO tasks show that PRS consistently discovers high-quality heuristics, demonstrating the effectiveness and generality of explicitly directional exploration design.

---


### 132. [Diagnosing the Explicit-to-Applied Theory of Mind Gap in LLMs](https://arxiv.org/abs/2610.31060)

**<font color=#1a73e8>作者：</font>** Prajvi Saxena, Sabine Janzen, Wolfgang Maass  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models are deployed in high-stakes roles such as therapy, education, and personal assistance, their social cognition must be assessed reliably. Current Theory of Mind (ToM) benchmarks report aggregate scores that conflate two distinct competencies: explicit ToM (recognizing what someone believes) and applied ToM (using that belief to predict behavior). Building on this distinction, we investigate the gap and its recoverability using four structurally diverse benchmarks. Aggregate reporting obscures uneven competence: on SimpleToM, Llama-3.1-8B scores 51.5 percent overall while recognizing mental states at 99.4 percent and predicting behavior at only 28.9 percent. To assess recovery, we compare structured prompting, matched in-context learning, and our proposed Belief-State Test-Time Training (BSTTT), which adapts lightweight parameters on answered support questions through action reconstruction. Across Qwen2.5-7B, Llama-3.1-8B, and GPT-oss-20B, recovery depends on the model, task, and intervention. On SimpleToM, reminders combined with BSTTT improve Llama's behavior prediction by 40.8 percentage points; reminders account for most of the overall improvement, with BSTTT adding 1.3 to 5.5 points beyond reminders across models. Contextual examples often outperform weight updates, while BSTTT remains stronger in specific model-benchmark settings. Temporal belief tracking remains difficult despite partial recovery. These findings show that aggregate ToM scores can overstate applied competence while hiding performance recoverable through targeted assistance. We recommend decomposed reporting of explicit and applied accuracy alongside intervention comparisons that establish which failures are recoverable and under what conditions.

---


### 133. [SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs](https://arxiv.org/abs/2610.31062)

**<font color=#1a73e8>作者：</font>** Arnon Mazza, Elad Levi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Policy enforcement for LLM agents has shifted from single-turn content moderation to compound, application-specific policies evaluated over multi-turn transcripts and tool-call trajectories. Fine-tuned guardrail models are efficient but degrade on compound policies, and while LLM-as-a-judge approaches achieve higher accuracy, they incur high inference cost and tend to produce unstable predictions. Neurosymbolic methods offer a natural alternative, decomposing the policy into narrow neural decisions composed under explicit logic. However, existing symbolic layers lack the required expressiveness and are optimized against fixed data rather than the policy itself. To address this, we introduce SCOPE, which compiles a policy into an executable program of neural predicates executed by small models, deterministic extractors, and code that composes their outputs. The program is optimized jointly with its training data, using adversarial generation of counterexamples that target where the program deviates from the policy. We evaluate SCOPE on a benchmark of real-world policy tasks against prompt optimization, task decomposition, and workflow generation methods, achieving the highest average accuracy across tasks and models. Programs optimized with the weakest executor transfer to other models without further optimization. This allows them to be deployed in production on inexpensive models, where they reach accuracy comparable to frontier reasoning models. Unlike these monolithic models, SCOPE produces substantially more stable predictions, and each verdict is interpretable through the predicate outputs that produced it. Additionally, we validate the key components of our method through an ablation study. SCOPE thus enables reliable, interpretable, and efficient policy enforcement at production scale.

---


### 134. [Dual Exam: Controlled Evaluation of Multimodal Agents and World Models](https://arxiv.org/abs/2610.31066)

**<font color=#1a73e8>作者：</font>** Zhefan Rao, Meng Chu, Xuan Zhang 等 83 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World Models (WMs) can support Multimodal Agents (MAs) through simulated experience, while Agent trajectories can inform World Model refinement. Evaluating this interaction requires separate evidence about action selection and state evolution. We introduce Dual Exam, which tests Agents under fixed environment response mechanisms and World Models under fixed action interventions across physical, digital, social, and scientific domains. The Agent track compares 10 configurations on 1,088 items in 15 reporting categories. The World Model track contains 400 cases across eight scenarios; 15 configurations have full coverage and one covers six scenarios. GPT 6 Astra leads the case-weighted Agent Index at 31.3, and GPT-Image-2 leads the full-coverage WM Overall at 21.7. These scores use different tasks and metrics and are not directly comparable. A 150-case pilot of one coupled pairing records zero task successes and motivates component-level diagnosis. Results reveal uneven task performance and failures to preserve task-relevant state. Their value for predicting coupled success or sustained reciprocal learning remains to be established.

---


### 135. [nnInteractive Agent: General-Purpose AI Agents as 3D Image Annotators](https://arxiv.org/abs/2610.31080)

**<font color=#1a73e8>作者：</font>** Fabian Isensee, Constantin Ulrich Harsy, Maximilian Rokuss 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interactive 3D segmentation models such as nnInteractive turn a few spatial prompts (points, scribbles, boxes) into accurate volumetric masks, but a human still does the annotation work: finding each structure, placing prompts, checking the result and correcting it. General-purpose AI agents can now interpret images, call tools and write code. We show that such agents can take over this work without additional training: the user makes a request in plain language, and the agent works out what has to be segmented, locates the targets, prompts nnInteractive, inspects the 3D result, corrects it and responds to feedback. Asked for 'the muscles used for chewing', an agent identifies and segments the masseters and pterygoids; asked to count liver lesions, it writes its own code to find candidates and splits a merged lesion on request. Our open-source nninteractive-agent provides nnInteractive as tools over the Model Context Protocol (MCP), together with a skill that encodes how experienced users prompt it. On a benchmark spanning CT, MRI, PET and micro-CT of humans, a mouse and an ant (14 images; 51 targets from organs and tumours to muscles, foot bones, vessel trees and an insect brain), Claude Code and Codex reach a mean Dice of 0.81 and 0.84 from the request alone; when told where each target is, both reach 0.85 and prompt nearly as effectively as an oracle that places prompts using the reference segmentation. A text-prompted 3D model (VoxTell) is more accurate on most standard radiological targets but less robust: it returns an empty mask for one of them and fails on the leg muscles, the foot bones, the mouse and the ant, where the agents remain accurate. Code: this https URL

---


### 136. [RIFT: KV Cache Compression for Draft Models with Complementary Compressibility Training](https://arxiv.org/abs/2610.31098)

**<font color=#1a73e8>作者：</font>** Dor Tsur, Maor Ashkenazi, Maximilian Golub 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding is a popular decode acceleration method. As such, it is particularly relevant to long-output generation, which requires an increasingly large KV cache. KV cache compression offers a way to constrain costs in long-context drafting. However, compression methods that focus on prefill information can lose relevance as the output length grows. We term this phenomenon decode staleness and show that it degrades draft model accuracy under selection-based KV cache compression. We introduce RIFT, a family of selection-based KV cache compression strategies that balance prefill information and recent generated tokens. We show that refreshing the KV cache selection during token generation significantly improves the drafter's quality at the cost of additional decode latency. To alleviate the refresh costs, we propose an adaptive KV refresh strategy that reduces the number of score calculations while retaining the drafter's quality. We further demonstrate how a compressibility-driven drafter training phase, based on sparse attention masks, can improve the drafter's quality under a compressed KV cache. Combined with compressibility training, RIFT enables Qwen3.5-4B, drafting for Qwen3.5-122B, to retain over 98% of its full-cache acceptance length on 32K-token inputs, 4K-token outputs, and an 8K-token KV cache budget.

---


### 137. [Who Is the Influencer? Consensus Dynamics in Multi-Agent Systems](https://arxiv.org/abs/2610.31105)

**<font color=#1a73e8>作者：</font>** Gouki Minegishi, Jingyuan Feng, Hiroki Furuta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems are increasingly used in practice, but their behavior is complex and hard to understand. We design a simple task to ask which model has the most influence on the final consensus when several models are mixed in one system. Experimentally, across seven model families, we find that the opinions of the other models are absorbed into the opinion of the stronger model, the one with more parameters. This happens even though the task requires no pretraining knowledge and has no correct answer. To understand this phenomenon, we interpret the agents as weighted particles moving on a simplex. Larger models carry a larger weight and therefore occupy a deeper well in the energy landscape. A large weight means strong in-context learning: a model with a large weight amplifies the majority of its context. Larger models are generally better at in-context learning, and this is what makes the larger model the influencer. We hope that this work helps to interpret multi-agent systems, whose behavior is becoming too complex for humans to understand.

---


### 138. [Where Do Long Captions Fail? Position-Aware Diagnosis and Reinforcement Learning for Detailed Image Captioning](https://arxiv.org/abs/2610.31111)

**<font color=#1a73e8>作者：</font>** Yuanze Hu, Zhichao Yang, Junwei Jing 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detailed image captioning is usually framed as an amount problem: a model should mention more visual facts while avoiding hallucination. However, autoregressive VLMs generate captions as ordered sequences, and later generations may be produced under weaker or noisier visual grounding. We therefore argue that long-form captioning should be studied not only by what facts are mentioned, but also by where they appear. We introduce a position-aware rubric representation that decomposes dense human references into atomic visual claims, verifies generated captions against those claims, and induces a quartile-wise composition of supported, hallucinated, and generic content. This lens reveals two qualitatively different failures in long captions: models tend to produce unsupported specificity in the middle, while the final portion often escapes into vague, non-evidential language rather than simply accumulating more hallucination. A same-reference human control does not exhibit these patterns; additional human audits examine the visual validity of the induced labels. Motivated by this diagnosis, we propose PAGER (Position-Aware Grounded Evidence Reinforcement), a GRPO training objective with separate signals for supported fine-grained middle evidence, evidence-bearing tail continuation, claim coverage, and content-aware length control. The result is a closed loop: the same ordered claim representation identifies where long captions fail and supplies the position-specific reward needed to repair those failures. Experiments on detailed-caption benchmarks show that PAGER improves position-wise grounding and pairwise caption preference while preserving competitive global caption quality.

---


### 139. [Can AI Co-Design Structures? An AI Agent for Early-Stage Structural Design](https://arxiv.org/abs/2610.31113)

**<font color=#1a73e8>作者：</font>** Ricardo Maia Avelino, Mennatallah El-Assady, Tom Van Mele 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models and agentic workflows offer a new paradigm to early-stage structural design translating design intent into structural models. Although text-to-3D approaches have demonstrated that natural language can be used to produce visual, mesh-based geometric models, structural design requires domain-specific geometric arrangements and semantically rich data types. This paper introduces a proof-of-concept workflow for prompt-to-structure generation using an AI agent connected to a COMPAS-based structural modelling API through a Model Context Protocol (MCP) server. Through controlled modelling operations, the agent creates and modifies a graph-based structural data model composed of explicit building elements. The resulting artifacts can be inspected, modified, serialised, and further connected to downstream AEC workflows. The approach is demonstrated through selected prompt-to-structure examples and by progressive and editable design sequences that resemble typical iterative structural design workflows. The results are preliminary, but demonstrate the possibility of combining natural language, agentic workflows, and domain-specific structural data structures as a first step toward AI-assisted structural co-design.

---


### 140. [Through a PRISM, Clearly: Step-Sequence Reasoning for Mistake Recognition in Procedural Videos](https://arxiv.org/abs/2610.31117)

**<font color=#1a73e8>作者：</font>** Olga Loginova, Oleksandr Bezrukov, Frank Keller  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Procedural mistake recognition requires identifying deviations from valid multi-step activities. We study post-completion recognition from videos with benchmark-provided step boundaries. We introduce PRISM (Procedural mistake Recognition via Interpretable Semantic Modeling), which grounds video segments in language and maps their descriptions to procedural states using a lightweight hidden Markov model trained on correct executions. Reference alignment and semantic checks identify errors in step content and order. To support evaluation across heterogeneous benchmarks, we map dataset-specific annotations to four edit-based error types: insertion, deletion, substitution, and transposition. Across three benchmarks, we compare gold and VLM-generated descriptions in raw, semantic-role, and action-object forms. Decoder controls show consistent gains from the trained local decoder over nearest-candidate matching, with additional, dataset-dependent benefits from sequence decoding. Semantic role labeling improves Any-F1 in all six matched grounded comparisons, although the gains vary across datasets and do not translate into uniform improvements under separate configuration selection. These results establish language grounding as an effective interface for explicit procedural mistake reasoning and characterize the contributions of representation and decoding.

---


### 141. [Constraint Reasoning and Large Language Models Join Forces: Providing Contrastive Explanations for Real-World Optimisation-Based Applications](https://arxiv.org/abs/2610.31119)

**<font color=#1a73e8>作者：</font>** Roger X. Lera-Leri, Filippo Bistaffa, Athina Georgara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We focus on optimisation-based Decision Support Systems in real-world applications. In this context, we aim to provide contrastive explanations that answer users' questions about recommendations based on the solution of an optimisation problem, specifically a Mixed-Integer Program (MIP). Addressing this endeavour is crucial to ensure human oversight of the decisions implemented, as required by international guidelines on trustworthy and responsible automated decision-making systems. We propose a novel methodology that combines constraint reasoning techniques and Large Language Models (LLMs) to generate contrastive explanations for optimisation problems encoded as MIPs. Although LLMs have shown impressive capabilities in Natural Language processing, they can produce incorrect answers due to reasoning limitations. To overcome these limitations, we leverage constraint reasoning techniques to distil the information necessary to produce an explanation, which is then passed as input to an LLM as the so-called graph of reasons. Such a graph captures the semantics and the relationships among constraints of the optimisation problem. Results on real-world scheduling domains show that incorporating constraint reasoning improves explanations generated by the LLM. In particular, using the graph of reasons enables the LLM to produce natural-language explanations that include more relevant reasons while reducing errors compared to explanations generated without this structure.

---


### 142. [SetCommit: Coordinated Token Commitments for Few-Step Diffusion Language Model Decoding](https://arxiv.org/abs/2610.31120)

**<font color=#1a73e8>作者：</font>** Yuannuo Feng, Yubing Ye, Wenshuai Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models generate multiple token positions in parallel, but few-step decoding makes parallel commitment difficult: tokens that appear reliable individually may be jointly inconsistent, while premature commitments can prevent later context-dependent refinement. In this paper, we introduce SetCommit, a training-free method for coordinated parallel token commitment. Instead of selecting tokens independently by confidence, SetCommit selects a commitment set that balances token reliability against local joint commitment risk, preserving conditioning opportunities for subsequent denoising steps. It further performs budget-neutral local exchanges, replacing vulnerable earlier commitments when newly revealed context supports more reliable alternatives. SetCommit requires no retraining or architectural modification and is compatible with existing diffusion decoding strategies. Experiments with LLaDA-8B and Dream-7B on GSM8K, MATH-500, MBPP, and HumanEval show accuracy/pass@1 gains of up to 7.4 percentage points over native decoding at 32 model evaluations. At common quality targets, geometric-mean incremental speedups range from $1.44$ to $1.74\times$. Code is available at this https URL.

---


### 143. [Delta N-gram: Forward-Only Continual Writing into a Language Model's Native N-gram Memory](https://arxiv.org/abs/2610.31125)

**<font color=#1a73e8>作者：</font>** Hao Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Our previous analysis found that a model's native hashed N-gram table is where continual updates disturb the base least, but its writes needed backpropagation and changed the pretrained table. We present Delta N-gram, a forward-only write path into that table. The pretrained table T^0 is never modified. Evidence is written into a sparse patch \Delta on the rows it addresses: a 4.1M-parameter writer emits a target and a gate per (position, hash head) event, and a block-averaged delta rule keeps each row a convex combination of its old value and the gated targets. The writer is trained offline on raw text with the pretraining objective; at use time writing takes forward passes only, and clearing \Delta restores the original model. A 0.6B prototype trained to answer questions keeps 16/16 facts after a second write; online gradient writes keep 2--4/16. We study two writers: a plain writer that encodes evidence with the T^0-only model, and a delta writer that reads its current memory while encoding. On Qwen3.8-Flash-Next, the plain writer's memory is document-specific: on 64 held-out news events it lowers continuation NLL by 0.068 nats/token against empty memory and by 0.024 against another document's memory, and 0.063 and 0.013 after 16 intervening articles. The delta writer's memory is more document-specific and keeps more of it under distraction (70% vs 54%). Over 35,000 writes on our previous seven-task chain both writers stay stable and the delta writer drifts less (layer-2 math drift 176% vs 188%); later accuracy changes by -0.26/-0.52pp (-7.29pp for gradient updates) and small-k_i drift is 17.9/17.5% (39.2%). Acquisition is negative, and general-input drift reaches 32.8% (20.75%): format rows read by every example grow to 4--12 times their pretrained norm. Zeroing eight such rows removes over 98% of layer-2 drift on math inputs, together with their NLL gain.

---


### 144. [RankAlign: Vision-Language Representation Alignment via Rank Transformation](https://arxiv.org/abs/2610.31145)

**<font color=#1a73e8>作者：</font>** Enzhe Zhao, Marco Fiorucci, Lamberto Ballan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While the Platonic Representation Hypothesis posits that vision and language models converge toward compatible latent geometries, recovering class-level correspondences between unpaired modalities without cross-modal supervision remains challenging. Existing relational matching methods compare within-modality similarity kernels directly, although the same semantic structure may be represented through different numerical parameterizations across modalities. We propose RankAlign, a rank-based normalization strategy for class-level unpaired vision-language matching. RankAlign transforms each within-modality similarity kernel into an ordinal relational representation before permutation matching, while leaving the correspondence space and matching solver unchanged. The resulting representation is invariant to strictly increasing reparameterizations of similarity values while preserving the ordinal structure used for matching. We provide exact-recovery and stability guarantees that characterize correspondence recovery under both exact and partial ordinal agreement. Experiments across diverse frozen vision and language encoders and multiple datasets demonstrate improved and more stable class-level correspondence recovery, including under label corruption and domain shift.

---


### 145. [Prompt Sensitivity in Tool-Augmented Model Comparisons](https://arxiv.org/abs/2610.31148)

**<font color=#1a73e8>作者：</font>** Mateusz Modrzejewski, Tomasz Radzikowski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are compared on question-answering benchmarks that pose each question in one wording, and a reworded question can change which of two models scores higher. We ask whether giving the models tools makes such comparisons more stable. An accuracy gain cannot answer this, because tools change several steps between the question and the scored answer at once. We propose a matched protocol that separates those steps: the answer readout, reasoning, the decision to call, the tool's answer, and the report supplied without a call. We apply it to six open models in five domains under five wordings. We find that tools raise accuracy where a program answers the question and widen the wording sensitivity of many pairwise comparisons. The widening follows how often a model calls, and call frequency follows the wording for some models and not others. It also depends on the interface and the instructions: a native tool-calling interface and a second tool description leave no detected widening in molecules, and sensitivity persists where tools return intermediate results. These findings show that deterministic reports do not guarantee stable comparisons. We recommend reporting call frequency and comparison stability under several wordings beside accuracy.

---


### 146. [WildFakeToolBench: Benchmarking AI-Generated Image Detectors with Web-Sourced Image Processing](https://arxiv.org/abs/2610.31152)

**<font color=#1a73e8>作者：</font>** Mingjie Li, Yukun Jiang, Yicong Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As AI generated images are getting popular these days, discussions on such generations are widely existed in current public forums, software repositories, and photography tutorials. Moreover, with the help of LLM-assisted code translation, malicious actors can adopt such information to evade detectors without specialized knowledge or local GPU execution of the resulting tools. To evaluate such risks, we introduce \textsc{WildFakeToolBench}, a benchmark suite of $156$ executable image-processing tools derived from $220$ public sources across $142$ domains. Each tool retains its source evidence and passes syntax, execution, and output-distortion checks without using feedback from the evaluated detectors. On $105$ generated images from five generators, we evaluate six state-of-the-art detectors with images processed by the tools in our collected bench to assess their effectiveness against such in-the-wild risks. The strongest individual tools achieve attack success rates of $25.25\%$--$100\%$ across detectors, exceeding the strongest of six selected image-processing baselines for each detector. Evaluating subsets of an eight-tool pool yields worst-case coverage above $80\%$ for every detector. Effectiveness is sparse and detector-specific: high coverage across candidates does not imply reliable one-shot evasion. These findings not only highlight the potential of such web-sourced risks, but also show the potential on establishing AI-image detector robustness evaluation framework based on those in-the-wild information.

---


### 147. [HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games](https://arxiv.org/abs/2610.31162)

**<font color=#1a73e8>作者：</font>** Zecong Tang, Zian Guan, Yuncheng Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building virtual embodied agents that operate in open-ended games like human players is a long-standing goal requiring both long-horizon autonomy and reliable native-interface control. As a procedurally generated open world, Minecraft provides a natural testbed for studying the integration of these capabilities. Existing agents typically provide either native visuomotor control without long-horizon autonomy or high-level planning executed through environment APIs or predefined skills. To bridge this gap, we propose HiSTEVE, a hierarchical VLA agent with a capability-aware agent harness. At the orchestration level, we equip the harness with structured memory for tracking progress and a VLM planner for selecting subtasks within the VLA's capabilities. To reliably determine subtask completion, we further introduce a policy-coupled task completion state detector that conditions on VLA policy context to signal candidate completion. At the control level, a single VLA executes all subtasks with vision-only perception and native keyboard-and-mouse actions. To mitigate interference between heterogeneous GUI and non-GUI interactions, we introduce regime-specific RMSNorm branches and separate mouse-movement token embeddings. We also train the VLA through world knowledge injection, imitation learning, and reinforcement learning with environment feedback to improve reliability and recovery. HiSTEVE achieves state-of-the-art atomic-task performance, scoring 85.0% on MineStudio Bench and a 37.4% average success rate on OpenHA, while also completing long-horizon tasks such as crafting an iron pickaxe from scratch like human players.

---


### 148. [Prompting Strategy Effects Depend on the Judge: A Multilingual Study of LLM-as-a-Judge Robustness](https://arxiv.org/abs/2610.31172)

**<font color=#1a73e8>作者：</font>** Asal Mehrabi, Mohammad Aliannejadi, Clemencia Siro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge evaluation is increasingly applied to multilingual tasks, yet prompting strategies such as Chain-of-Thought and Role Conditioning are recommended based solely on English benchmarks. Whether their effectiveness transfers across judge models and languages remains unknown: prompt-sensitivity studies are largely English-centric, while existing multilingual judge studies fix the prompt template. In this work, we address this gap by measuring this interaction through a benchmark of 9 prompting strategies, 4 open-weight judges, 27 languages, and 4 tasks across 13 datasets, yielding over 1M pointwise scores on gold-reference outputs, validated against human judgments. We find that prompting strategies are not transferable: the choice of the judge model dominates the choice of prompting strategy, strategy effects reverse direction across judges, and stability degrades in low-resource languages, where these effects are concealed by aggregate reporting. These findings show that prompting effects in multilingual evaluation are conditioned on the judge, task, and language. Consequently, prompting strategies should be validated for the intended evaluation setting, and cross-study comparisons should account for both judge and prompt configuration.

---


### 149. [When More Metadata Misleads: Probing Field-Level Grounding in LLM-Generated Museum Descriptions](https://arxiv.org/abs/2610.31193)

**<font color=#1a73e8>作者：</font>** Clemencia Siro, Laura Hollink  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Metadata-conditioned generation is often framed as a data-to-text task in which additional input fields should improve grounding. Museum description generation challenges this assumption because catalogue records are heterogeneous, partially visual, and unevenly documented across geographic regions. We study how metadata composition shapes the generation of artefact descriptions through a two-phase framework. Phase 1 analyses natural metadata variation in a large museum collection, where field count, field type, image availability, and Place co-vary. Phase 2 introduces controlled field probes that hold object identity fixed while varying metadata quantity, field type, and image access. Our results show that metadata quantity alone does not explain generation behaviour. Field type determines whether models ground, omit, or infer information, while images can both support visual grounding and increase unsupported interpretation. More broadly, our findings show that metadata-conditioned data-to-text evaluation should assess field- and claim-level support, rather than relying only on aggregate input coverage or reference similarity.

---


### 150. [Different Tasks, Different Timesteps: Temporal Task-Aware Quantization for Diffusion Language Models](https://arxiv.org/abs/2610.31198)

**<font color=#1a73e8>作者：</font>** Ofek Avivi, Eliron Rahimi, Avi Mendelson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) introduce unique quantization challenges due to their iterative denoising process. In this work, we reveal that quantization sensitivity is both taskand time-dependent, with different downstream tasks exhibiting distinct precision requirements across denoising steps. We further show that these patterns can be predicted without groundtruth labels or task-specific evaluation metrics. Building on these findings, we introduce T 2Quant, a task and time-aware mixedprecision quantization framework that uses a label-free sensitivity signal to optimally allocate activation precision across denoising steps under a fixed bit-width budget. Extensive experiments across three DLMs and six benchmarks demonstrate that T 2Quant consistently improves the average accuracy of existing quantization methods, achieving gains of up to 6.7 percentage points under the same budget.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-241](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
