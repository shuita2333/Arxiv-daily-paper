# 🧠 大模型相关研究 | 2026年06月17日

> 本类共 **270** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-270](./part-06.md)

---

### 51. [A Formal Framework for Declarative Agentic AI in Business Process Analysis](https://arxiv.org/abs/2606.15291)

**<font color=#1a73e8>作者：</font>** Mohammad Azarijafari, Luisa Mich, Michele Missikoff  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI opens new opportunities for automating Business Process (BP), enabling autonomous decision-making and dynamic adaptation. However, realising this potential requires BP entities and their interactions to be defined with formal precision. This paper presents a formal framework for Agentic BP analysis through the AGO methodology. AGO captures the modelling perspective in terms of who is acting (Agents), why it is carried out (Goals), and what the relevant entities are (Objects). Grounded in set theory and mathematical logic, we formally define the AGO entity types and their interactions, organising all definitions into a BP Knowledge Base (BPKB). The resulting BPKB supports structured querying, incremental updates, and automatic generation of BP workflows, while ensuring soundness and completeness of the derived paths.

---


### 52. [LatentGym: A Testbed For Cross-Task Experiential Learning With Controllable Latent Structure](https://arxiv.org/abs/2606.15306)

**<font color=#1a73e8>作者：</font>** Daksh Mittal, Tommaso Castellani, Thomson Yen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We envision continually learning agentic systems that become more useful over time: as they encounter sequences of related tasks, they should infer the hidden structure shared across those tasks and use it to improve future decisions. This cross-task experiential learning capability is pivotal in domains such as personalization and interactive assistance, but existing training/evaluation frameworks do not provide shared, controllable latent structures and cannot measure whether or why agents improve. We introduce LatentGym: a controllable suite in which each environment is organized around a ground-truth latent variable governing the structure across tasks. Our construction yields metrics that separate exploration (whether the agent's actions gather information about the latent) from exploitation (whether the agent uses what it has gathered). We demonstrate our suite on empirical studies addressing three questions: how and why frontier models fail to adapt across related tasks; whether post-training on related task sequences improves general cross-task adaptation, and where those gains come from; and how design choices such as inter-task feedback shape training dynamics and generalization. Together, these results establish a controlled foundation for studying how LLM agents learn from experience across tasks, and for designing agents that adapt more reliably in sequential, personalized, and interactive settings.

---


### 53. [Adapting Reinforcement Learning with Chain-of-Thought Supervision for Explainable Detection of Hateful and Propagandistic Memes](https://arxiv.org/abs/2606.15307)

**<font color=#1a73e8>作者：</font>** Mohamed Bayan Kmainasi, Mucahid Kutlu, Ali Ezzat Shahroor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hateful and propagandistic memes exploit the interplay between images and text to convey harmful intent that neither modality reveals alone. Although thinking-based multimodal large language models (MLLMs) have advanced vision-language understanding, their application to meme content moderation remains underexplored. We propose a reinforcement learning-based post-training method that improves classification performance and reference-based explanation quality in thinking-based MLLMs via task-specific rewards and Group Relative Policy Optimization (GRPO). Concretely, we (i) conduct a systematic empirical study of off-the-shelf MLLMs for hateful and propagandistic meme understanding across English and Arabic benchmarks, (ii) extend existing meme datasets with weakly supervised chain-of-thought (CoT) rationales via distillation and multi-LLM fine-grained propaganda annotations, (iii) introduce a GRPO-based objective with thinking-length regularization that jointly optimizes classification accuracy and explanation quality, and (iv) investigate self-supervised GRPO on unlabeled memes using consensus-based pseudo-labels. Experiments on the Hateful Memes and ArMeme benchmarks show that our approach improves over previously reported results on FHM accuracy (up to +2.1%, from 79.9% to 82.0%) and on ArMeme macro-F1 (up to +7.6 points, from 0.536 to 0.612 with explanations; +6.1 compared to the original ArMeme benchmark), while also generating natural-language explanations. On ArMeme, sequence-classification baselines remain stronger in terms of raw accuracy, whereas our approach provides more balanced per-class performance along with explanations. We publicly release our code, data extensions, and evaluation resources.

---


### 54. [Forced Deferral: Manipulating Routing Decisions in Multimodal LLM Cascades](https://arxiv.org/abs/2606.15308)

**<font color=#1a73e8>作者：</font>** Zhongye Liu, Yaopei Zeng, Yurui Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While multimodal large language models (MLLMs) have shown strong visual reasoning abilities, serving a large model for every query is computationally expensive. MLLM cascades mitigate this cost by first querying a weak but cheaper model and deferring to a strong model when the weak model's output is unconfident. However, since the weak model's confidence directly controls compute allocation, these systems expose a new attack surface: an adversary can manipulate confidence so that their queries are consistently deferred to the strong model. Motivated by this vulnerability, we introduce the Forced Deferral Attack (FDA), an adversarial image attack that lowers the weak model's confidence and causes cascades to route queries to the strong model. FDA learns a universal border trigger by optimizing a temperature-flattened objective. This objective pushes the weak model's token distribution on triggered inputs toward less concentrated targets constructed from its clean responses. Across datasets, model families, and deferral metrics, FDA consistently increases strong-model routing while outperforming image-perturbation and prompt-injection baselines. These results show that MLLM cascades are vulnerable to attacks that manipulate compute allocation, forcing unintended strong-model usage without directly targeting answer correctness.

---


### 55. [LLMs on Tabular Data with Limited Semantics: Evidence from Industrial Car Retrofit Prediction](https://arxiv.org/abs/2606.15314)

**<font color=#1a73e8>作者：</font>** Aina Vila Pons, Ioannis Tzachristas, Constantinos Antoniou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial retrofit planning depends on structured operational data rather than free text: planners must estimate whether a newly registered prototype will require a retrofit, which retrofit package it will need, and how long the work will take. We study an industrial dataset linking a prototype-registration system (284,271 vehicles) with a retrofit-management system (48,716 cleaned visits), and compare strong tabular machine learning baselines with three LLM-based strategies on row-serialized inputs: embedding features (Amazon Titan), direct prompted classification (Claude Sonnet 4), and an ML+LLM stacking approach. Across binary occurrence prediction, 15-way retrofit-type classification, per-visit duration regression, and an aggregated monthly benchmark, classical tree ensembles remain the strongest standalone models. However, the LLM results reveal a consistent pattern: embeddings remain useful on tables (binary AUC = 0.982), direct prompting collapses once semantic signal is stripped by hashing (binary AUC = 0.500; multiclass weighted F1 = 0.018), and hybrid stacking yields the best manually built multiclass model (weighted F1 = 0.626). On the monthly benchmark, lag-based machine learning outperforms time-series foundation models, though Chronos-small remains competitive in zero-shot forecasting. The results suggest that on privacy-constrained industrial tables, LLMs are more effective as complementary components than as replacements for strong tabular baselines.

---


### 56. [ChatPlanner: A Large Language Model Framework for Personalized Public Transit Routing](https://arxiv.org/abs/2606.15315)

**<font color=#1a73e8>作者：</font>** Tingting Yang, Chenhao Xue, Jun Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized public transit routing in public transit systems remains challenging due to the difficulty of capturing and integrating diverse user preferences into routing algorithms. This paper presents ChatPlanner, a novel framework that leverages Large Language Models (LLMs) to enable preference aware public transit routing. Our approach employs fine-tuned LLMs with Retrieval-Augmented Generation (RAG) to extract routing parameters and interpret nuanced user preferences from natural language queries, subsequently integrating these preferences into the objective function of a public transit routing algorithm. This study designs preference aware datasets incorporating eight personas and five contexts to establish scoring standards for both fine-tuning and RAG. This work conducted three experiments to validate the solutions' feasibility, extraction of routing information and preferences, and solution set quality and completeness. Results demonstrate that ChatPlanner generates feasible solutions reliably. Fine-tuning enforces the required output structure and learns general preference patterns, while RAG provides query-specific context to resolve imprecise or conversational expressions and calibrate continuous scores. The combination of both achieves the highest accuracy in routing information extraction and user preference interpretation. Results based on selected case studies show that by capturing user preferences, ChatPlanner identifies valuable solutions across different dimensions that existing route planners overlook, generating more valuable route alternatives. This research establishes a new paradigm for integrating natural language understanding into transportation optimization.

---


### 57. [Conditional Multi-Event Temporal Grounding in Long-Form Video](https://arxiv.org/abs/2606.15320)

**<font color=#1a73e8>作者：</font>** Yuanhao Zou, Arthad Kulkarni, Lucas Tonanez 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models have made rapid progress in video temporal grounding, yet real-world applications routinely require localizing every event that satisfies compositional temporal and spatial conditions. Existing benchmarks fall short: they localize only a single moment per query, count without temporal conditions, or treat grounding and counting as disjoint tasks. We introduce CoMET-Bench for Conditional Multi-Event Temporal Grounding in long-form video, comprising 2789 queries over 600 videos averaging 33.8 minutes across five real-world domains, with each query composed from 4 temporal conditions, 3 spatial conditions, and a dedicated negative-query subset. We further propose a unified evaluation protocol jointly measuring counting, grounding, and negative-query recognition, including a new Rejection-F1 metric that prevents trivial gaming by lazy "always-empty" models. Benchmarking a broad suite of MLLMs, agent-based, and grounding-specialized methods reveals that existing approaches remain far from solving this task. Building on these findings, we propose CoMET-Agent, a training-free agentic framework that reformulates the task as structured search-and-aggregate, improving F1@0.5 by 6.1% over GPT-5 purely through structural reasoning. Failure analysis further surfaces three open directions: fine-grained entity tracking, position-uniform retrieval, and causal event pairing.

---


### 58. [Prior over Evidence: Stereotype-Driven Diagnosis in LLM-Based L2 Pronunciation Feedback](https://arxiv.org/abs/2606.15325)

**<font color=#1a73e8>作者：</font>** Rong Wang, Kun Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed for written pronunciation feedback in second-language (L2) English learning, under the assumption that their diagnoses are grounded in the supplied speech evidence rather than in priors from pretraining. This assumption is tested on 1,800 L2-Arctic utterances spanning six L1 backgrounds, three audio-capable LLMs, four pronunciation dimensions, and five evidence conditions ranging from a text-only baseline to numeric acoustic features and raw audio. Each (utterance x model x condition x dimension) cell is scored on three metrics: Rating Accuracy (RA) against gold labels, Evidence Coherence (EC) assessing internal consistency without ground truth, and Grounded Correctness (GC) evaluated against gold evidence. Results show three findings across models. First, rating accuracy and grounded reasoning decouple: 39.6% of judged cells contain internally coherent reasoning that supports a wrong rating, against only 15.8% where the reasoning supports a correct rating. Second, phoneme-level feedback converges to a fixed inventory of L2-English difficulty phones that recurs across all six L1 backgrounds and all evidence conditions. Third, acoustic evidence improves the rating only when the supplied feature directly probes the target dimension: textualised F0 range raises pitch-variation grounding from (0.18-0.19) to (0.45-0.62) across all three models, while stress and phoneme correctness, which require target-to-realisation alignment, remain ungrounded. The same audio waveform without textualised F0 values does not reproduce this improvement. These findings indicate that current general-purpose LLMs are more reliable as verbalisers of externally computed pronunciation evidence than as standalone diagnostic engines.

---


### 59. [Semantic DLM+: Improving Diffusion Language Models through Bias-variance Trade-off in Transition Kernel Design](https://arxiv.org/abs/2606.15327)

**<font color=#1a73e8>作者：</font>** Keyue Jiang, Yuxiang Wang, Yanan Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) have demonstrated strong scaling capacity as alternatives to autoregressive language models. However, their performance is highly sensitive to the choice of transition kernels, and poorly designed kernels can lead to issues like training instability, slow convergence, and biased sampling. In this paper, we study this sensitivity through a principled analysis of generalization error and identify three critical factors: asymptotic bias (difficulty in approximating the posterior distribution), exposure bias (error propagation during sampling), and optimization variance induced by kernel dispersion. We further compare different transition kernels: masking diffusion yields sparse and easier posterior-approximation targets, while uniform diffusion provides stronger sampling-side repair but induces harder approximation. Motivated by this trade-off, we revisit a previously overlooked variant, semantic DLM (SemDLM), where the transition kernel corrupts tokens to neighborhoods that are semantically similar. Our theory suggests that SemDLM can serve as a plausible middle ground by reducing the posterior approximation difficulty of uniform diffusion while retaining repair ability. However, we find that SemDLM suffers from a semantic basin problem, where sampling repeatedly stays within a semantic region and produces low-diversity text. To address this, we propose SemDLM+, which adds a global transition and a semantic-frequency penalty during sampling. Experiments on LM1B and OpenWebText show that SemDLM+ improves training dynamics and achieves competitive language modeling and generation quality with satisfactory diversity.

---


### 60. [SGFormer++: Semantic Graph Transformer for Incremental 3D Scene Graph Generation](https://arxiv.org/abs/2606.15328)

**<font color=#1a73e8>作者：</font>** Mengshi Qi, Changsheng Lv, Zijian Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose SGFormer++, a novel Semantic Graph Transformer for 3D scene graph generation (SGG), which aims to parse point cloud scenes into semantic structural graphs, where nodes denote detected object instances and edges encode their pairwise relationships, with the core challenge lying in modeling complex global scene structure. While existing graph convolutional network (GCN)-based methods suffer from over-smoothing and limited receptive fields, SGFormer++ leverages Transformer layers as its backbone to enable global message passing. Specifically, we introduce two key components tailored for 3D SGG: (1) a Graph Embedding Layer++ that efficiently integrates edge-aware global context with linear computational complexity, and (2) a Semantic Injection Layer++ that enriches visual features with linguistic priors from large language models (LLMs) and vision-language models (VLMs), boosting semantic representation without introducing extra trainable parameters. To further address the practical challenge of incremental SGG (I-SGG), where new relationship categories arrive sequentially, we equip SGFormer++ with a novel Spatial-guided Feature Adapter, which calibrates predicate features using subject-object spatial geometry to counter scale variation, and a Cascaded Binary Prediction Head that mitigates catastrophic forgetting via task-incremental classifier expansion and logit distillation. Extensive experiments on the 3DSSG benchmark demonstrate that SGFormer++ achieves state-of-the-art performance in both standard and incremental settings: it yields a significant 4.49% absolute improvement in Predicate A@1 under the incremental setting. Code and data are available at: this https URL.

---


### 61. [Replay What Matters: Off-Policy Replay for Efficient LLM Reinforcement Unlearning](https://arxiv.org/abs/2606.15333)

**<font color=#1a73e8>作者：</font>** Zirui Pang, Chenlong Zhang, Haosheng Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM unlearning has emerged as a cost-effective alternative to full retraining for removing hazardous knowledge from pretrained models while preserving general utility. Recent RL-based methods such as RULE reformulate unlearning as learning a refusal behavior, but their on-policy optimization repeatedly samples from the same forget and retain/boundary prompts throughout training. We identify a critical inefficiency in this process: easy cases quickly converge and provide little useful gradient signal, while hard cases near the forget/retain boundary continue to produce low-reward rollouts that are discarded after a single use. To address this issue, we propose ReRULE, an off-policy replay enhancement for reinforcement unlearning. ReRULE stores low-reward hard-case rollout groups in a replay buffer during early GRPO training and reuses them in later stages through importance-sampled off-policy updates, redirecting computation toward boundary cases that still require learning. Theoretically, we show that ReRULE yields a tighter hard-case convergence bound than pure on-policy RULE. Empirically, ReRULE improves MUSE-Books Retain Quality from 46.3 to 56.2 while adding only 5--11% training time across benchmarks. Its limited improvement on the simpler TOFU setting further supports the intended conditional behavior: replay is most beneficial when the hard/easy disparity is pronounced.

---


### 62. [CausalDrive: Real-time Causal World Models for Autonomous Driving](https://arxiv.org/abs/2606.15341)

**<font color=#1a73e8>作者：</font>** Tianyi Yan, Huan Zheng, Dubing Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models have emerged as a promising paradigm for scaling autonomous driving (AD) data, yet existing video generative models fall short as interactive simulators. Layout-conditioned renderers rely on "oracle" future trajectories of all background agents, rendering them strictly non-reactive. Conversely, pure action-conditioned predictors lack semantic control over complex interactions and suffer from prohibitive diffusion latencies, hindering closed-loop policy learning. To bridge this gap, we present CausalDrive, a controllable, real-time foundation driving world renderer. CausalDrive operates solely on the initial front-view frame, the ego-vehicle's trajectory, and a macroscopic text prompt. By excluding future NPC layouts, we compel the model to intrinsically predict causal interactions, enabling text-driven control over Driving Sociology, allowing users to dynamically orchestrate diverse counterfactual reactions to identical ego-actions. To overcome the efficiency bottleneck and address the covariate shift in autoregressive generation, we propose a novel Context-Forced DMD architecture. This combines continuous flow-matching with a self-correcting distillation objective, achieving interactive speeds of 12 FPS. This breakthrough transforms the passive video generator into a playable neural simulator. We demonstrate its versatility across three downstream applications: (1) generative closed-loop evaluation with significantly mitigated collision artifacts, (2) large-scale Reinforcement Learning (RL) post-training driven by a Video2Reward module, and (3) real-time human-in-the-loop simulation. Extensive experiments validate that policies trained within CausalDrive's reactive scenarios exhibit superior interaction capabilities in the real world.

---


### 63. [Reward Hacking in Language Model Agents: Revisiting AI Safety Gridworlds](https://arxiv.org/abs/2606.15385)

**<font color=#1a73e8>作者：</font>** Ömer Veysel Çağatan, Xuandong Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reward hacking, where AI systems exploit misspecified objectives to achieve high reward without satisfying intended goals, remains a central challenge in AI safety. Yet most known instances have been discovered post hoc in frontier systems where controlled study is impractical. We adapt the AI Safety Gridworlds framework into a text-based evaluation suite that reformulates classic reinforcement learning safety tasks for language-based agents. Across frontier and mid-scale models, we find that specification gaming emerges zero-shot: models systematically achieve high observed reward while underperforming on hidden safety objectives, and even apparently safe behaviors can reflect misunderstanding rather than principled safety. Reinforcement learning does not correct these failures: direct reward optimization widens the gap between observed and hidden reward, as the model's initial competence causes it to lock into locally rewarding strategies before discovering safer alternatives. This pattern persists across model scales (1.5B--14B) and is not resolved by finer credit assignment, exploration prompts, or entropy regularization. Our results show that reward hacking arises naturally when optimizing proxy objectives with capable language model agents and resists standard mitigations, suggesting that proxy-reward failures in agentic settings may require approaches beyond standard exploration and credit-assignment fixes. To facilitate reproducibility, the code for this work is available at \href{this https URL}{our public repository}.

---


### 64. [Not All Skills Help: Measuring and Repairing Agent Knowledge](https://arxiv.org/abs/2606.15390)

**<font color=#1a73e8>作者：</font>** Yixuan Wang, Yiyang Zhou, Yiming Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents can improve without weight updates by accumulating natural-language skills from experience, but current systems entrust every decision about which skills to keep and how to apply them to LLM judgment alone. We argue that this conflates two distinct roles: generating a skill from experience is a creative act that judgment handles well, while deciding whether that skill actually helps requires empirical evidence across many tasks. Measuring per-skill causal contributions via randomized masking, we find that skill libraries exhibit pervasive causal heterogeneity: individual skills routinely help on some task types while hurting on others, yet their opposing effects cancel in aggregate, making them invisible to global curation methods. We propose ASSAY, a framework that separates generation from curation: it computes a per-skill causal attribution on a small development set, restructures the library offline, and suppresses skills with negative predicted effect for each test task. Across seven base models spanning four providers and two benchmarks (AppWorld and tau-bench), ASSAY consistently improves over prior skill-curation approaches. On AppWorld's hardest split, DeepSeek-V3 achieves 69.3% task-goal completion (47.4% relative improvement), a new state of the art among all published methods including weight-tuned approaches. On tau-bench retail, GPT-4.1 improves by 8.7% relative, advancing past o4-mini, o1, and GPT-4.5 on the public leaderboard without any weight modification. Ablation traces the dominant gain to per-task masking, confirming that the bottleneck is matching skills to tasks at inference time, not removing bad skills globally. Code is available at this https URL.

---


### 65. [CHILLGuard: Towards Fine-Grained Chinese LLM Safety Guardrail with Scalable Data Construction and Model-aware Preference Alignment](https://arxiv.org/abs/2606.15396)

**<font color=#1a73e8>作者：</font>** Wenbo Yu, Bohua Wang, Hao Fang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Malicious content generated from large language models (LLMs) could pose severe safety risks and ethical concerns. While existing LLM safety guardrails excel in English or multilingual settings, they lack adaptation to Chinese-specific regulatory policies, cultural context and linguistic nuances, failing to support fine-grained risk classification for diverse deployment needs. In this paper, we introduce a 5-macro, 31-micro category fine-grained risk taxonomy for Chinese scenarios, and build CHILLGuard: a dedicated Chinese LLM content safety guardrail. To address the critical scarcity of high-quality annotated Chinese safety data, we propose a scalable multi-stage data construction pipeline: we expand multi-source corpus via retrieval-augmented generation, generate implicit harmful samples through prompt engineering rewriting, and refine high-quality data via multi-model voting-based label calibration. Based on this, we build CHILLGuardTrain, a large-scale training set with 405,007 samples, and CHILLGuardTest, a rigorously curated annotated test set with 51,745 samples. We then train CHILLGuard on CHILLGuardTrain under a generator-classifier collaborative framework via Model-aware Direct Preference Optimization. Extensive experiments under multiple settings demonstrate the state-of-the-art performance of CHILLGuard, e.g., a 15.92% improvement of F1 score over Qwen3Guard-8B-Strict on our benchmark. We will release our resources at this https URL.

---


### 66. [Few-Shot Biomedical Relation Extraction with Large Language Models: A Viable Alternative to Supervised Learning?](https://arxiv.org/abs/2606.15412)

**<font color=#1a73e8>作者：</font>** Jakob Mraz, Tomaž Curk, Blaž Zupan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical relation extraction (BioRE) is a key step in transforming biomedical literature into structured knowledge. However, most existing approaches rely on supervised models trained on costly annotated datasets, limiting their scalability and adaptability across relation types and domains. We investigate few-shot BioRE using prompt-based learning with large language models (LLMs) and compare two task formulations: pairwise classification, which predicts relations for individual entity pairs, and joint generation, which extracts multiple relations in a single model call. Experiments on the BioREDirect dataset reveal a clear precision-recall trade-off. Pairwise classification achieves higher recall, whereas joint generation is more precise and computationally efficient. The best-performing model achieves a micro-F1 score of 0.44, substantially outperforming previous few-shot results (0.34) while remaining below the supervised baseline (0.56). Much of this gap is attributable to a single ambiguously defined relation type. When evaluated using macro-F1, which better captures performance across relation types in an imbalanced setting, prompt-based approaches outperform the supervised baseline (0.45 vs. 0.38), particularly on rare relation types. These findings highlight the potential of LLMs for BioRE in low-resource settings and underscore the importance of well-defined relation schemas.

---


### 67. [Encode Errors: Representational Retrieval of In-Context Demonstrations for Multilingual Grammatical Error Correction](https://arxiv.org/abs/2606.15416)

**<font color=#1a73e8>作者：</font>** Guangyue Peng, Wei Li, Wen Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grammatical Error Correction (GEC) involves detecting and correcting the wrong usage of grammar. While large language models (LLMs) with in-context learning (ICL) capabilities have shown significant progress on various natural language processing (NLP) tasks, their few-shot performance on GEC remains suboptimal. This is mainly due to the challenge of retrieving suitable in-context demonstrations that capture error patterns instead of semantic similarity. In this paper, we demonstrate that LLMs can inherently capture information related to grammatical errors through their internal states. From these states, we extract the Grammatical Error Representation (GER), an informative and semantically neutral encoding of grammatical errors. Our novel GER-based retrieval method significantly boosts performance in ICL settings on multilingual GEC datasets, improving the precision of correction. For high-resource languages, our results on 8B-sized open-source models match those of closed-source models such as Deepseek2.5 and GPT-4o-mini. For low-resource languages, our $F_{0.5}$ scores surpass the baseline by up to a factor of 1.20. This method provides a more precise and resource-efficient solution for multilingual GEC, offering a promising direction for interpretable GEC research.

---


### 68. [From Frames to Temporal Graphs: In-Context Egocentric Action Recognition with Vision-Language Models](https://arxiv.org/abs/2606.15417)

**<font color=#1a73e8>作者：</font>** Bessie Dominguez-Dager, Francisco Gomez-Donoso, Miguel Cazorla 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action reasoning in egocentric video requires capturing fine-grained transitions of hand-object interactions, a task where general-purpose Vision-Language Models (VLMs) often struggle when operating directly on raw pixels. We propose to decouple visual perception from symbolic reasoning by converting videos into Temporal Action Graphs. In a multi-stage prompting pipeline, we first generate dense natural language narratives over short temporal windows as a semantic bottleneck, then formalize them into structured, open-vocabulary graph representations. On the EGTEA and Epic-Kitchens-100 datasets, the symbolic representation unlocks efficient in-context learning: few-shot graph demonstrations yield substantial accuracy gains over zero-shot frame and graph-based inference alike. Even in the zero-shot setting, graph-based reasoning remains competitive with pixel-based inference despite potential pretraining contamination favoring the latter. Across 11 open-weight VLMs from 6 model families ranging from 2B to 235B parameters, our findings indicate that current VLMs are more effective as symbolic reasoners than as direct visual observers. By projecting video into the language domain, we provide a scalable, fine-tuning-free alternative to end-to-end approaches that better leverages these models' latent reasoning strengths. The code will be made public.

---


### 69. [Let LLMs Judge Each Other: Multi-Agent Peer-Reviewed Reasoning for Medical Question Answering](https://arxiv.org/abs/2606.15419)

**<font color=#1a73e8>作者：</font>** Zaifu Zhan, Shuang Zhou, Rui Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Objective: To enhance the accuracy, interpretability, and robustness of large language models (LLMs) in medical question answering (MedQA).
Method: We designed a multi-agent peer-reviewed reasoning method in which multiple LLM agents independently generate chain-of-thought reasoning with candidate answers, then act as peer reviewers to evaluate each other's reasoning for factual correctness and logical soundness. The highest-rated reasoning chain is selected to produce the final answer. Experiments were conducted with five state-of-the-art LLMs (Llama-3.1-8B, Qwen2.5-7B, Phi-4, DeepSeek-LLM-7B, GPT-oss-20B) on three benchmark datasets: HeadQA, MedQA-USMLE, and PubMedQA. Performance was compared against single-model chain-of-thought reasoning and chain-of-thought-based majority voting.
Results: Peer-reviewed reasoning consistently outperformed both baselines. The best model combination achieved an average accuracy of 0.820 across datasets, exceeding the strongest single model (0.777) and majority voting ensembles (up to 0.789). The method also scaled effectively with more participating models, while peer assessments reliably distinguished high- from low-quality reasoning chains.
Conclusion: The proposed multi-agent peer-reviewed reasoning method enables LLMs to act as both solvers and evaluators, yielding superior performance in MedQA. By emphasizing reasoning quality rather than answer agreement alone, this approach improves accuracy, interpretability, and robustness, offering a promising direction for trustworthy biomedical AI systems.

---


### 70. [Constitutional Value Potentials: reading and steering internal priority margins in language models](https://arxiv.org/abs/2606.15420)

**<font color=#1a73e8>作者：</font>** Tong Che, Rui Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A constitution tells a language model what to value, but little tells us whether it does. Adherence is judged from outputs, and output evidence is most fragile on value conflicts, where what matters is not which value a model mentions but which one it is willing to sacrifice. We provide evidence that this arbitration can be read from activations in a structured margin readout. We introduce Constitutional Value Potentials (CVP). For each value we learn a scalar potential from the hidden state: an internal pressure to preserve that value, supervised not by the prompt but by an independent judge's verdict on which value the model's own response actually preserved. The signed difference of two potentials is a priority margin. A constitutional clause becomes the claim that a margin stays positive, and a single monitor score flags when it does not. The monitor predicts conflict violations with AUROC up to 0.95, beats a strong hidden-state probe, and generalizes to held-out synthetic conflicts across three Qwen2.5 scales. The signal appears as the answer begins, from the prompt tail and first response token. Read this early, the same signal reveals whether an adversarial priority hack has actually pushed the model toward a violation, rather than only whether the prompt looks adversarial. The same directions also support intervention tests: under selected steering settings, moving along a value direction shifts judged trade-offs in the intended direction. Together, these results suggest that some constitution-relevant priorities are accessible as activation-space margins, rather than only as output behavior.

---


### 71. [Post-Launch Capability Expansion of Vision-Language Models via Prompting for On-Orbit Spacecraft Inspection](https://arxiv.org/abs/2606.15427)

**<font color=#1a73e8>作者：</font>** Nicholas A. Welsh, Lennon J. Shikhman, Monty Nehru Attazs 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spaceborne inspection systems often deploy perception models prior to launch, after which updating model weights or expanding fixed label sets becomes operationally impractical. While supervised models can be integrated pre-flight, adding new semantic capabilities in orbit requires retraining and re-uploading parameters. We investigate whether prompt-driven vision--language models can enable post-launch semantic expansion, allowing new spacecraft components to be specified via natural-language prompts without modifying onboard weights. We evaluate zero-shot instance segmentation of spacecraft components under a strictly frozen, single-pass inference protocol on a test set of $129$ images of previously unseen satellites. Under fixed global thresholds and no post-processing, SAM3 achieves $0.385$ mAP@$0.5$ and $0.267$ mAP@$0.5{:}0.95$. Performance is strongly scale-dependent: large structural elements like spacecraft bodies ($0.639$ AP@$0.50$) and solar arrays ($0.598$ AP@$0.5$) localize reliably, while relatively small appendages like antennas ($0.221$ AP@$0.5$) and thrusters ($0.081$ AP@$0.5$) remain difficult. Prompt formulation influences performance, with structured prompts incorporating spatial and geometric descriptors yielding up to $82%$ improvement over short category-name prompts. The model operates within the memory and compute envelope of contemporary embedded GPUs, suggesting prompt-driven grounding can provide a practical mechanism for post-launch semantic extension of dominant spacecraft structures while highlighting limitations of zero-shot localization for fine-scale components under orbital domain shift.

---


### 72. [Beyond Classification: A Cough Regression Benchmark for Respiratory Acoustic Foundation Models](https://arxiv.org/abs/2606.15436)

**<font color=#1a73e8>作者：</font>** Mayur Sanap, Prasanna Desikan, Edgar Lobaton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Respiratory acoustic foundation models (FMs) excel at cough classification, yet their ability to predict continuous health quantities from cough audio remains largely unexplored, despite the clinical value of passive age, BMI, and disease probability estimation in settings where physical measurements are unavailable. We introduce the multi-model, multi-target cough regression benchmark evaluating five FMs (OPERA-CT, OPERA-CE, OPERA-GT, HeAR, M2D+Resp) across six targets on three datasets under subject-disjoint protocols, comparing linear, MLP-small, and full MLP regression heads. MLP-small beats the mean-predictor baseline on all tasks and linear probing in 23 of 30 model x task cases, with full MLP overfitting on small clinical data but recovering on larger sets, revealing a dataset size x head-capacity trade-off. HeAR leads within-dataset age regression on Coswara (9.12 yr MAE); its CIDRZ result is excluded from headline claims owing to possible HeAR-CIDRZ pretraining overlap. OPERA-GT is favored over OPERA-CT on age in all three datasets, with the CIDRZ margin within seed variance, extending a generative-pretraining advantage from breath to cough. HeAR and M2D+Resp reach near-full performance at N = 50 samples while OPERA models require N = 400. Cross-dataset transfer is strongly asymmetric as large diverse data generalises to small clinical populations (CoughVID to CIDRZ: -0.17 yr) but not vice versa (CIDRZ to Coswara: +2.43 yr, +26.6%).

---


### 73. [Hierarchical Modeling of ICD Codes in EHR Foundation Models](https://arxiv.org/abs/2606.15447)

**<font color=#1a73e8>作者：</font>** Megha Thukral, Dong Gyun Kang, Rudra Pratap Singh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electronic health record foundation models typically treat ICD diagnosis codes as flat tokens, overlooking the clinically meaningful hierarchical structure that captures disease families, subcategories, and fine-grained diagnostic detail. As a result, existing EHR representation learning methods do not explicitly exploit the hierarchical structure already present in the coding system. In this work, we study ICD-10-CM hierarchy as a general inductive bias for clinical representation learning. We investigate two complementary mechanisms for incorporating hierarchy: first, by augmenting diagnosis sequences in a BERT-style transformer with tokens corresponding to different levels of the ICD hierarchy, and second, by injecting hierarchy into graph-based code representations through hierarchy-aware edges combined with diagnosis co-occurrence structure. Across these settings, we evaluate whether explicit hierarchy improves downstream prediction, which levels of the hierarchy are most useful, whether hierarchy encoding improves transfer across datasets, and how hierarchy reshapes embedding similarity structure. We conduct experiments on two large-scale real-world clinical datasets: MIMIC-IV, used for pretraining and in-domain evaluation, and eICU, used to assess cross-dataset transfer via frozen encoder probing. Our findings show that explicitly encoding ICD hierarchy improves over flat code representations in both in-domain and cross-dataset settings, while revealing that the most useful level of hierarchy depends on both the task and the modeling approach. More broadly, we focus on hierarchy-aware EHR representation learning and show that the benefits of encoding hierarchy are generalizable across modeling settings and hierarchy levels.

---


### 74. ["ChatGPT, help me draft a breakup text": The Covert Triad and Articulation Labor in AI-Assisted Romantic Communication](https://arxiv.org/abs/2606.15460)

**<font color=#1a73e8>作者：</font>** Skyler Wang, Isabella Luppi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (AI) has begun infiltrating the most ordinary domains of romantic life -- drafting apologies, softening reproaches, and decoding a partner's ambiguous messages. While recent scholarship on AI in intimate life has concentrated on chatbot companions, this article shifts the frame to AI as an intermediary in human-to-human romantic communication. Drawing on a multi-modal corpus of vernacular discourse from 2023 to 2026, we contribute two complementary concepts. The covert triad names a structural change: a relationship phenomenally dyadic but operationally triadic, with the third party visible only to the partner who deploys a model. Articulation labor names the mechanism whereby the expressive component of emotional labor -- converting felt experience into language that a partner can receive -- is increasingly delegated to AI, even as feeling labor remains lodged in the user. Authenticity, under these conditions, is being reconfigured from a property of linguistic authorship to one of emotional ownership, a shift actively contested.

---


### 75. [Who Drifted: the System or the Judge? Anytime-Valid Attribution in LLM Evaluation Pipelines](https://arxiv.org/abs/2606.15474)

**<font color=#1a73e8>作者：</font>** Yitao Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continuous evaluation of LLM products relies on a strong LLM judge treated as ground truth: a cheap monitor scores every interaction and a team is paged when the score drifts down. But the judge is itself a model behind an API, and a silent version bump or scoring-prompt update changes how it scores -- so every drift alarm is ambiguous between a worse product and a changed judge. We resolve the ambiguity with a fixed, human-labeled anchor set that the current judge re-scores at a steady interleave, a second betting e-process on the judge-versus-human gap, and a guard-window rule returning a verdict in {none, system, judge}. We prove anytime-validity, one-way identification (only the judge can move the anchors), an attribution race whose design law is that the anchors must out-run the main process they guard, and process orthogonality. On two real judge changes, a silent version bump is detected as judge drift in 60/60 runs with zero judge-to-system misattribution, and a contaminating strict-prompt change is correctly attributed on 110 of 120 runs at guard width 300 -- while the industry-default rolling z-test false-alarms on 75% of drift-free streams. Every experiment replicates on a second domain (TL;DR summarization) with nothing re-tuned, and where the domains differ the differences are the ones the race predicts: the strict-prompt change shifts scores harder there, so the anchors fire faster and attribution becomes perfect (240/240). The monitor runs at approximately 0.64 of the cost of strong-judging every item, or 0.21 in a cheaper-but-deafer regime.

---


### 76. [Frame-Conditioned Moral Computation in LLaMA 3.1-8B-Instruct: A Mechanistic Interpretability Audit of Ethical Reasoning](https://arxiv.org/abs/2606.15507)

**<font color=#1a73e8>作者：</font>** Ali Dasdan, Manan Shah, W. Russell Neuman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Behavioral audits of Large Language Models on moral prompts measure what the model says, not the internal computation producing it. We use Transluce, an AI-driven mechanistic-interpretability platform, to examine LLaMA 3.1-8B-Instruct on 54 moral prompts in four batteries: 17 dilemmas, policy, and meta-ethical questions (B1); 6 role-playing scenarios (B3); and a controlled trolley contrast varying the switching mechanism with people fixed (B4, 15 prompts) or identity attributes with mechanism fixed (B5, 16 prompts).
Two complementary metric families, five cluster-level metrics and a six-metric neuron-level panel, converge on a Situational Anchor Effect: domain-specific representations dominate the top of the activation list across every battery. The model's ethics-labeled capacity stays essentially constant; its salience (rank, priority, top-of-list presence) is highly sensitive to the interpretive frame the prompt selects.
The B4-vs-B5 contrast confirms the model attends to whichever surface feature varies: aggregate ethics metrics are indistinguishable, but the dominant non-ethics distractor mirrors the design. A multi-temperature audit identifies a candidate ethics neuron (L16/N3837) stable across temperatures; a cross-model behavioral proxy on two frontier models yields preliminary evidence of divergence in self-reported moral focus, consistent with an Alignment Wrapper in which RLHF re-orders surface text without removing underlying domain-first frames. We unify these as Frame-Conditioned Moral Computation: the prompt's surface vocabulary selects a feature manifold, and the moral conclusion is downstream of that selection. Behavioral alignment must be supplemented by Mechanistic Alignment: a research program asking whether ethics-related features can be shown causally privileged under controlled frame variation, not merely loud in the explanation.

---


### 77. [ToolMenuBench: Benchmarking Tool-Menu Filtering Strategies for Reliable and Efficient LLM Agents](https://arxiv.org/abs/2606.15508)

**<font color=#1a73e8>作者：</font>** Rahul Suresh Babu, Laxmipriya Ganesh Iyer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented large language model agents increasingly operate over large tool libraries, but existing evaluations often focus on whether a model can call a tool correctly rather than how the visible tool menu shapes reliability, efficiency, and safety-relevant risk exposure. We introduce ToolMenuBench, a benchmark for evaluating tool-menu construction in multi-step LLM agents. ToolMenuBench varies tool-menu size, distractor type, state-dependent task structure, and risk exposure, and reports both filter-level and downstream agent metrics, including visible-tool count, risky-tool exposure, task success, wrong-tool calls, premature actions, and token usage. In a controlled evaluation across seven model backends, three tool-menu sizes, six filtering methods, and seven evaluation settings, CMTF improves task success from 32.1% under all-tools exposure to 85.7%, while reducing average token usage by roughly 98%. Causal minimal tool filtering achieves the strongest overall tradeoff, reducing visible tools, wrong-tool calls, premature actions, and risky-tool exposure relative to unfiltered exposure, lexical filtering, state-aware filtering, and broader causal-path baselines. ToolMenuBench provides a reusable evaluation framework for studying the agent-interface problem: which tools should be visible, when they should be visible, and under what cost or risk constraints.

---


### 78. [SHARD: Safe and Helpful Alignment via Self-Reframing Distillation](https://arxiv.org/abs/2606.15517)

**<font color=#1a73e8>作者：</font>** Viswonathan Manoranjan, Amogh Gupta, Anvesh Rao Vijjini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often struggle with sensitive prompts. They may refuse outright, provide generic safety boilerplate, or fail to address the user's legitimate informational needs that can be answered safely. We introduce SHARD, a self-reframing distillation method to improve safe-helpfulness. It first rewrites sensitive prompts to surface benign intent using philosophical guidelines, then reframes its original responses into safe, more helpful ones, and finally fine-tunes the model on its self-reframed responses. Across DNA and the English subset of LINGUASAFE, SHARD improves helpfulness for most model families while preserving safety. It also remains competitive with distillation from a larger teacher model, suggesting that models can internalize safe and helpful behavior elicited from their own. Warning: This paper contains content that may be offensive or harmful.

---


### 79. [Emergent retokenization symmetry in large language models: phenomenology and applications](https://arxiv.org/abs/2606.15521)

**<font color=#1a73e8>作者：</font>** Kanishk Jain, Matthew Day, Tankut Can  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenization introduces representational redundancy: under a fixed token vocabulary, every byte string admits many valid token encodings, or segmentations, that decode to the same surface string. However, given a prompt, most language model tokenizers break this representational symmetry by returning a canonical segmentation. Training only on canonical segmentations should influence inference behavior, and there is little reason to expect models to respect segmentation symmetry on downstream tasks. We find that this symmetry partially emerges during training. Here, we probe this emergent symmetry through experiments testing token compositional understanding, representation diversity, and task focused benchmark performance. We primarily use \textbf{retokenization} -- replacing a prompt's canonical tokenization with an alternative segmentation while preserving its bytes exactly. Relative to other prompt perturbations, retokenization is unusually clean because it isolates segmentation effects without changing syntax, semantics or surface form. We use retokenization to study sensitivity and robustness to semantically identical input representations across pretraining and post-training. Moreover, this partial retokenization symmetry suggests a distinct inference-time sampling axis. While temperature sampling generates diverse outputs from the model using its next-token probability distribution, retokenization generates diversity from the model's internal computations through semantically equivalent input representations. We find that while this retokenization sampling strategy can hurt performance on easy problems, it can also recover solutions that conventional sampling does not find. Overall, our work presents retokenization as a simple yet powerful probe of large language models, shedding light on compositional understanding and prompt sensitivity, and offering a novel sampling strategy.

---


### 80. [Greedy Coordinate Diffusion: Effective and Semantically Coherent Adversarial Attacks via Diffusion Guidance](https://arxiv.org/abs/2606.15531)

**<font color=#1a73e8>作者：</font>** Bohdan Turbal, Blossom Metevier, Max Springer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning aligned language models on benign tasks (e.g. math tutoring) systematically breaks safety guardrails, even when training data contains no harmful content. While mechanistic approaches have shed light on where alignment resides in model weights, they do not by provide a general formal framework for deriving guarantees about when fine-tuning degrades it -- leaving the field without principled tools for predicting or preventing alignment collapse. We develop a local geometric framework through geometric analysis of parameter-space trajectories and apply it to understand the fragility of alignment in fine-tuning. While first-order analysis suggests orthogonal updates are safe, we prove this is illusory: the curvature of the fine-tuning loss induces second-order acceleration that can induce second-order drift into alignment-sensitive regions. We formalize a construct of our framework as the Alignment Instability Condition (AIC), three geometric properties that, when present, are sufficient to guarantee degradation. Our main result proves quartic onset of alignment degradation along gradient-flow trajectories, determined by how sharply alignment depends on specific parameters and how strongly tasks couple to these parameters. These findings yield formal sufficient conditions under which static first-order protection can fail under gradient descent. We further empirically validate the framework's foundations, showing that the Fisher Information Matrix provides a proxy for the degree of safety degradation across diverse fine-tuning.

---


### 81. [EIBench: A Simulator-Based Benchmark and Turn-Credit RL for Emotion Management](https://arxiv.org/abs/2606.15532)

**<font color=#1a73e8>作者：</font>** Rongzhi Zhu, Xiang Huang, Yuchuan Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotional intelligence (EI) in Large Language Models (LLMs) is often evaluated through static understanding tasks or single-response dialogue generation. However, emotion management is interactive: a good model should not only recognize a user's emotion, but also improve the user's emotional and relational state over several turns. We introduce EIBench, a simulator-based benchmark for interactive emotion management. EIBench contains 2,222 scenarios, with 2,009 for training and 213 for held-out testing. The scenarios are organized by a 2x2 taxonomy covering Support, Defense, Repair, and Charm, which together capture different forms of support, boundary maintenance, trust repair, and rapport building. In each scenario, an LLM simulator plays the user, updates an emotion-relation state after each turn, and maps the final state to an anchor-based score. This design makes EIBench both an evaluation benchmark and a training environment: the final state gives the outcome reward, while the per-turn state updates provide dense feedback for RL. We evaluate 15 open- and closed-source LLMs. Current models perform well on support and rapport-building scenes, but struggle with boundary maintenance under user pressure. To improve the EI ability of LLMs, we propose Centered Turn-Credit GRPO (CTC-GRPO), a GRPO extension that reuses the simulator's per-turn state updates as dense turn-level feedback while preserving the final outcome reward. CTC-GRPO improves Qwen3-8B from -22.4 to +22.4 on EIBench and also improves on out-of-distribution evaluations including SAGE (+12.4) and EQBench3 (+20.9%). Our results show that simulator-tracked user states can support both evaluation and training for multi-turn emotion management.

---


### 82. ["OpenBloom": A Stigma-Sensitive LLM Design Probe for Reproductive Well-Being](https://arxiv.org/abs/2606.15536)

**<font color=#1a73e8>作者：</font>** Yang Hong, Ashley Hua, Adya Daruka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Ongoing discussions in Human-Computer Interaction(HCI) have examined the role of AI-based tools in health information seeking, particularly within sensitive domains such as reproductive health. We introduce "OpenBloom," a web application and an exploratory design probe that utilizes Large Language Models (LLMs) to turn reproductive health articles into question-based prompts to explore stigma around reproductive wellbeing. Through a survey study with 34 participants across their 136 interactions with OpenBloom, we explore how AI-generated question-based learning interacts with sociocultural stigma, contextual sensitivity, and reflexiveness. While current LLM outputs largely meet expectations for non-offensiveness, they default to superficial rephrasing or factual recall and lack critical reflections. We discuss implications for applying Feminist HCI, contestability, and value-sensitive AI frameworks to future LLM-mediated reproductive health technologies.

---


### 83. [If These Walls Could Talk: Critical Play with Large Language Models in Museums](https://arxiv.org/abs/2606.15565)

**<font color=#1a73e8>作者：</font>** Anders Sundnes Løvlie  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly being used in museums to as role playing chatbots which let visitors talk to simulated versions of people and artefacts from the past. While such installations can be playful and engaging, they are also problematic because LLMs cannot be trusted to speak truthfully. I identify a fundamental dilemma for the use of LLMs in museum chatbots: LLMs cannot be trusted to tell the truth, and efforts to make them more reliable may ruin that which is attractive about the bots in the first place - their ability to engage in life-like conversation. In response, I propose designing for critical play with LLM-based bots: Designing for playful interactions with bots that are unreliable but still able to represent the past in an adequate and engaging manner - as fictional characters representing historical narratives, styles of discourse, diverse perspectives, humor and satire.

---


### 84. [LLM-Assisted Stance Detection in Scientific Discourse: A Test Case in Bayesian Cognitive Science](https://arxiv.org/abs/2606.15566)

**<font color=#1a73e8>作者：</font>** Eyup Engin Kucuk, Tarik Kelestemur, Ömer Dağlar Tanrikulu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Qualitative coding is central to social science, but expert annotation is difficult to scale. LLMs offer a possible extension, yet require careful validation when the target construct is interpretive, theoretically loaded, and only indirectly expressed. We study this problem in a difficult case: detecting whether authors treat Bayesian models as descriptions of mental and neural mechanisms (realism) or as useful mathematical tools (instrumentalism). Our method combines a theory-driven codebook, expert-coded reference annotations, a diagnostic-gated prompt-optimization search yielding a shared zero-shot prompt for three frontier LLMs (GPT-5.1, Claude Sonnet 4.6, Gemini 3 Pro Preview), and multi-rater reliability analysis. The final prompt achieved a held-out combined reliability score of 0.76 (harmonic mean of ICC = 0.79 and $\alpha$ = 0.74), with all diagnostics satisfied. Deployed on 6,858 quotes from 210 articles, the three LLMs reached substantial quote-level agreement (ICC = 0.80; $\alpha$ = 0.76; combined = 0.78) and near-perfect article-level rank stability ($r$ = 0.96-0.97 across rater pairs). The corpus was predominantly weakly realist, but article-level stances were rarely uniform: only 1.4% of articles used a single band, while 59.5% spanned four or more. Low-level perception/motor articles scored 8.8 Realism points higher than high-level cognition articles ($p < .001$, $d = 0.60$), quantifying a long-held qualitative intuition. We present this as an expert-led case study; the framework is intended to generalize to similar theoretically demanding tasks, not to all qualitative analysis.

---


### 85. [QoS-Aware Token Scheduling and Private Data Valuation for Multi-Modal Agentic Networks](https://arxiv.org/abs/2606.15573)

**<font color=#1a73e8>作者：</font>** Yao Du, Jing Liu, Pengfei Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In agentic systems, human-generated data records anchor the value of AI services. Yet cloud compute pipelines centralize processing on remote servers. Data centralization reduces personal data sovereignty and may potentially degrade the quality of service (QoS). Meanwhile, user contributions are diverse in quantity and quality: decentralized records can be biased, noisy, and heterogeneously distributed. To address the data challenge, we study fair token allocation and private data valuation for decentralized and resource-constrained agentic systems. Our approach embeds multi-modal representations in a shared semantic space and releases differentially private (DP) prototypes to preserve utility while reducing semantic leakage. With the DP guarantee, we design a fair token allocation scheme that rewards effective contributions and remains robust to data heterogeneity and AI resource scarcity. Extensive simulations demonstrate improved contribution-based fairness and QoS compared to standard benchmarks. The improved resistance to image reconstruction attacks indicates enhanced privacy for multi-modal personal data.

---


### 86. [Localizing Credit at the Divergence: Path-Conditioned Self-Distillation for LLM Reasoning](https://arxiv.org/abs/2606.15576)

**<font color=#1a73e8>作者：</font>** Yu Li, Shu Hong, Tian Lan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards assigns a single scalar to each rollout, leaving token-level credit assignment underspecified in long reasoning traces. On-policy self-distillation addresses this by letting the same model act as a teacher conditioned on privileged information, producing a dense per-token signal. But the common choice of a ground-truth answer is only an endpoint cue: on terse-answer tasks, the teacher falls silent at the intermediate positions where path-level guidance matters most. We propose Hindsight Self-Distillation (HSD), which conditions the teacher on a successful peer rollout drawn from the current training group. Such a peer is an exact sample from the success-conditioned policy, requiring no additional sampled rollouts. By providing a full successful continuation rather than only the final answer, the resulting credit signal concentrates at the divergence position between a failed rollout and a successful peer. Across Qwen3-8B and Qwen3-32B on math and code benchmarks, HSD obtains the best result against GRPO variants and on-policy distillation baselines, with the largest gains on terse-answer tasks such as AIME.

---


### 87. [Large Language Models as Optimizers: A Survey of Direct vs. Tool-Augmented Approaches and Their Performance Frontiers](https://arxiv.org/abs/2606.15577)

**<font color=#1a73e8>作者：</font>** Roko Peran, Luka Hobor, Mihael Kovac 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly involved in complex mathematical optimization, even if the pragmatic user who triggers them is unaware of it. After all, many real-world problems reduce to the search for better or the best solutions. The field of LLM-as-optimizer has three paradigms: direct optimization, tool-augmented optimization, and tool-creating optimization. Direct optimization uses iterative prompting and heuristic generation to navigate solution spaces. Tool-augmented optimization translates natural language problems into formal specifications and orchestrates external solvers. Tool-creating optimization goes further, using LLMs to discover reusable algorithms or heuristics that can be deployed at zero marginal LLM cost. We describe current performance frontiers based on the benchmarks from the literature. We identify the critical reasoning gap in current architectures and argue for trade-offs between the future potential of direct optimization and the auditability of tool-augmented optimization. Even future, more powerful models might opt for tool-making to improve operational efficiency for repetitive families of problems.

---


### 88. [Your Agent Has a Genome: Sequence-Level Behavioral Analysis and Runtime Governance of LLM-Powered Autonomous Agents](https://arxiv.org/abs/2606.15579)

**<font color=#1a73e8>作者：</font>** Sidi Deng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose Base Sequence Analysis, a framework that encodes the runtime behavior of LLM-powered autonomous agents into compact symbolic sequences using a four-letter alphabet: X (Explore), E (Execute), P (Plan), and V (Verify). Drawing an analogy to genomic sequence analysis, we apply n-gram pattern mining, Markov transition matrices, and point-biserial correlation to 347 real-world execution traces collected from a production ReAct agent system over 8 days. Our analysis reveals that (1) the trigram P-X-P is the only statistically significant high-risk pattern, lowering success rate by 10.4%; (2) P-ratio is the strongest negative predictor of success (r=-0.256, p<0.0001); and (3) the E->V transition probability is only 2.1%, indicating a systemic verification deficit. Based on these findings, we design Governor, a three-layer runtime intervention system comprising a rule engine, a statistical accumulator, and a chi-square-based threshold adaptor. In a natural before/after deployment evaluation (N=101 vs. N=246), Governor achieves a +6.2% absolute increase in task success rate while simultaneously reducing average token consumption by 44%. To validate cross-system generality, we apply the XEPV encoding to 2,000 public SWE-agent trajectories on SWE-bench, confirming that exploration spirals and the E->V verification deficit replicate in an independent system. We outline six research directions including base sequence language models, cross-agent behavioral fingerprinting, and reward shaping, and release an open-source toolkit for reproducibility.

---


### 89. [Agentic Retrieval and Reinforcement Learned Equation Chains: A Controlled Generation Framework for Complex and Novel Physics Word Problems](https://arxiv.org/abs/2606.15591)

**<font color=#1a73e8>作者：</font>** Tirthankar Mittra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating high-quality Physics Word Problems (PWPs) that are novel, complex, and solvable remains a challenging and underexplored problem in educational content generation. Existing approaches, many adapted from Math Word Problem (MWP) generation, often produce ambiguous, unsolvable, or structurally simple questions with limited linguistic diversity. We introduce ARVRE (Agentic Retrieval Value Reinforced Equation-chain), a two-stage framework for generating diverse and mathematically valid PWPs. In the first stage, a form of offline temporal-difference learning is used to construct valid chains of physics equations, while an agentic retrieval-augmented generation (RAG) framework dynamically selects topic-specific concepts and vocabulary. This design enables explicit control over problem structure and difficulty. In the second stage, a Large Language Model (LLM) converts the equation chain and retrieved concepts into a natural-language physics question. By grounding generation in valid equation chains, our method preserves mathematical correctness while promoting linguistic diversity and contextual richness. Human and automated evaluations demonstrate that ARVRE generates PWPs that are more complex, novel, and solvable than those produced by existing approaches. These results highlight the potential of combining reinforcement learning, retrieval, and LLMs for reliable generation of educational physics content.

---


### 90. [Fusion-E2Pulse: A Multimodal Event-RGB Fusion Network for Non-contact Pulse Wave Reconstruction](https://arxiv.org/abs/2606.15597)

**<font color=#1a73e8>作者：</font>** Qian Feng, Hao Guo, Yan Niu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-contact pulse wave reconstruction hinges on the precise recovery of waveform morphology, including the dicrotic notch. Conventional Red-Green-Blue (RGB)-based methods, which extract physiological signals from recorded facial videos, are constrained by the integral imaging mechanism of standard cameras, where the exposure process induces a smoothing effect that attenuates subtle vascular pulsation details. Conversely, neuromorphic event cameras, while offering exceptional sensitivity to intensity fluctuations, are inherently susceptible to noise and artifacts induced by minor motion. To exploit the synergy between frame-based integration and event-based differential sensing, we propose a novel multimodal network named Fusion-E2Pulse. This framework utilizes filtered RGB signals as structural priors to suppress motion artifacts, while leveraging the high-sensitivity of event streams to recover fine-grained morphological details. Experimental results demonstrate that Fusion-E2Pulse achieves state-of-the-art performance, effectively balancing noise suppression and morphological fidelity, achieving a mean absolute error of 0.78 bpm for heart rate estimation, a waveform correlation of 0.89, and a systolic phase duration error of 16.74 ms, validating its efficacy in reconstructing fine-grained pathological features.

---


### 91. [Integrating Reasoning and Generalization in Text-to-SQL via Self-Enhanced Fine-Tuning](https://arxiv.org/abs/2606.15598)

**<font color=#1a73e8>作者：</font>** Feng Lyu, Jinfeng Cen, Sijing Duan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL aims to translate natural language questions into executable SQL queries over structured databases, enabling non-expert users to access data intuitively. While recent advances in large language models (LLMs) have shown promise in this task, existing LLM-based approaches often struggle to strike a balance between strong reasoning capabilities and robust generalization. To address these limitations, we propose CoTE-SQL to enhance the LLM-based text-to-SQL generation with three key innovations: (i) self-enhanced reasoning traces distilled from LLMs without human annotation, (ii) structured chain-of-thought (CoT) prompting with modular decomposition and examples retrieval, and (iii) error-aware revision based on SQL execution feedback. Extensive experiments on the Spider and Bird benchmarks demonstrate that CoTE-SQL achieves new state-of-the-art performance among methods built on open-source LLMs with comparable model sizes on Bird (53.39% EX / 59.02 VES) and strong results on Spider (79.60% EX / 77.19 VES), with especially significant gains on complex queries. Results highlight the effectiveness of combining self-enhancement, structured reasoning, and execution-time feedback within an LLM-based framework for text-to-SQL design.

---


### 92. [On the Adversarial Robustness of Multimodal LLM Judges](https://arxiv.org/abs/2606.15608)

**<font color=#1a73e8>作者：</font>** Zihan Wang, Guansong Pang, Zelin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are increasingly used as automated judges, e.g., for image quality and safety assessment. However, their adversarial robustness remains largely unexplored, threatening the fairness and reliability of automated judging. To bridge this gap, we introduce RobustMLLMJudge, the first general framework for evaluating the adversarial robustness of general-purpose MLLMs when functioning as judges. It covers diverse attacks against popular judge approaches across quality and safety evaluation scenarios. Using RobustMLLMJudge, we reveal that i) different MLLM judges are highly vulnerable to score-inflating adversarial attacks; and ii) although effective, these attack methods face a critical challenge due to unique constraints in the evaluation protocols of MLLM judges. We further propose MGSIA, namely Manifold-Guided Semantic Induction Attack, a novel method that bypasses these constraints to enable more effective and transferable attacks on MLLM judges. The core idea of MGSIA is to combine affirmative semantic induction with high-score manifold alignment: it maximizes the probability that judges yield affirmative responses (e.g., "Yes") to binary semantic queries, while regularizing adversarial representations toward high-score centers estimated from proxy protocols. Together, these objectives yield transferable score-inflating perturbations. Extensive experiments demonstrate the superiority and generalizability of MGSIA in deceiving advanced MLLM judges under different evaluation scenarios, highlighting the need for robust MLLM judges. Code and data will be made available at this https URL.

---


### 93. [LLM Judges Have Dark Current: A Psychometric Datasheet for LLM-as-a-Judge Evaluation](https://arxiv.org/abs/2606.15610)

**<font color=#1a73e8>作者：</font>** Hiroyasu Usami, Keisuke Hara, Ayato Tsuboi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge systems are now routinely used for open-ended model evaluation, where human preference annotation is costly, slow, and difficult to reproduce. Yet these judges are often reported as scalar accuracy, win-rate, or agreement devices. We argue that a judge should instead be reported as a measurement instrument. We introduce a Judge Datasheet protocol that measures dark current under true-vacuum inputs, stable cross-sensitivity to same-quality surface variation, positional false preference, target sensitivity on a controlled quality ladder, and the criterion or operating point induced by tie instructions. The direction-stability decomposition reveals that apparent Delta0 preference can be stable surface response or disguised position bias. In a three-judge open-weight case study, Llama-3.1-8B shows high dark current and presentation-conflicted Delta0 behavior, Qwen2.5-14B is vacuum-clean and target-sensitive but mixes stable and positional over-discrimination, and Qwen2.5-32B is vacuum-clean with low stable cross-sensitivity and low positional false preference. A strict tie criterion eliminates Qwen32B Delta0 false preference but absorbs marginal Delta1 target signals into ties while preserving Delta5 sensitivity. The results show that prompting moves the criterion, not the resolution. We do not claim that the downstream mechanism hypothesis that motivated this work is confirmed; the contribution is a metrological protocol for measuring the measuring device before downstream claims are made.

---


### 94. [Mutual Distillation of Dual-Foundation Models for Semi-Supervised PET/CT Segmentation](https://arxiv.org/abs/2606.15611)

**<font color=#1a73e8>作者：</font>** Fuyou Mao, Beining Wu, Yanfeng Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Organ segmentation from PET/CT is critical for quantitative analysis and radiotherapy planning in oncology. To ease the high annotation cost of PET/CT segmentation, semi-supervised learning (SSL) provides a practical and effective solution for developing deep models with limited labeled data. Recent developments in visual foundation models have demonstrated remarkable adaptability with improved efficiency. In this work, we propose a mutual distillation framework that seamlessly exploits both structural and functional foundation models, which act as modality-specific generalists for distilling knowledge from structural CT and metabolic PET imaging. By bridging the gap between the task-specific precision of student models and the segmentation priors of generalist foundation models, we propose \textbf{MuDuo}, a mutual distillation framework that synergistically leverages SAM-Med3D for CT and SegAnyPET for PET to distill their knowledge into a lightweight student network. Our approach eliminates the need for manual prompts while maximizing the utility of unlabeled data for automatic segmentation, achieving state-of-the-art performance on the AutoPET dataset with only 5 labeled cases. Our source code is available at this https URL.

---


### 95. [MoECa: Aligning Feature Reuse with Expert Decomposition in Diffusion Transformers](https://arxiv.org/abs/2606.15615)

**<font color=#1a73e8>作者：</font>** Maoliang Li, Haojing Chen, Jiayu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers with Mixture-of-Experts (DiT-MoE) improve model capacity under sparse activation, but diffusion inference is still bottlenecked by redundant computation across timesteps. Existing caching methods mainly operate at the token level, which becomes suboptimal in DiT-MoE because each token update is internally decomposed into multiple routed expert branches. Our analysis shows that cross-timestep redundancy in DiT-MoE is better characterized at the expert-branch level than at the whole-token level. Based on this observation, we propose MoECa, a fine-grained caching framework that performs branch-level feature reuse across timesteps. MoECa further introduces expert-aware adaptive control and synchronized cache updates across MoE and attention paths to maintain stable intermediate states. Experiments on multiple DiT-MoE models show that MoECa consistently achieves a better speed-quality trade-off than prior caching methods, with up to 2.83$\times$ inference speedup and minimal quality degradation.

---


### 96. [Conflict-Aware Federated Fine-Tuning of Large Language Models with Mixture-of-Experts](https://arxiv.org/abs/2606.15625)

**<font color=#1a73e8>作者：</font>** Yijun Lu, Zihan Fang, Pengpeng Qiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The continuous scaling of large language models (LLMs) incurs prohibitive computational costs, making Mixture-of-Experts (MoE) a scalable alternative for efficient fine-tuning via sparse activation. While federated learning (FL) emerges as the paradigm for privacy-preserving collaborative optimization, integrating MoE into FL under data heterogeneity may trigger conflicting expert optimizations. Client-specific data distributions force same-indexed experts to optimize under inconsistent or even conflicting feature-label correlations. This mismatch induces destructive interference during aggregation, thus destabilizing the optimization trajectory and degrading model performance. To address this issue, we propose FC-MoE, a federated conflict-aware framework for MoE fine-tuning. It employs an importance aware weighting scheme to prioritize reliable local updates and utilizes gradient consensus projection to suppress conflicting updates, ensuring a stable global optimization path. Moreover, a local knowledge retention mechanism further preserves specialized client expertise by re-anchoring domain-specific residuals. Extensive experiments demonstrate that FC-MoE accelerates convergence and enhances both global and local model performance in non-IID federated environments.

---


### 97. [Formalizing and Mitigating Structural Distortion in LLM Attention for Zero-Shot Graph Reasoning](https://arxiv.org/abs/2606.15633)

**<font color=#1a73e8>作者：</font>** Donald Loveland, Puja Trivedi, Ari Weinstein 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown promise for reasoning over Text-Attributed Graphs (TAGs). However, applying LLMs to graphs requires linearizing their structure into sequences, introducing distortion rooted in the graph bandwidth problem. While this distortion has been shown to degrade performance, it is often attributed to prompt design or model scale, leaving the underlying mechanism unclear. In this work, we show \textit{how} rotary positional embeddings turn graph linearization into bandwidth-dependent attention decay, suppressing attention between graph-adjacent nodes that are forced far apart in the serialized sequence. This shifts the focus of LLM-based graph reasoning from prompt engineering and scaling toward correcting attention misalignment. Motivated by this analysis, we propose \textbf{G}raph-\textbf{a}ligned \textbf{L}anguage \textbf{A}ttention (\textbf{GaLA}), a lightweight, inference-time modification for LLMs. GaLA biases attention toward graph-adjacent nodes while preserving the LLM's sequential inductive biases. Across TAG benchmarks, GaLA improves performance with negligible overhead, demonstrating that distortion is a correctable bottleneck in LLM-based graph reasoning.

---


### 98. [Distilling Examples into Task Instructions: Enhanced In-Context Learning for Real-World B2B Conversations](https://arxiv.org/abs/2606.15641)

**<font color=#1a73e8>作者：</font>** Guy Rotman, Adi Kopilov, Danit Berger Zalmanson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) is the standard method for low-resource classification, yet its efficacy in specialized domains remains largely unexplored. We address the challenge of classifying semantically complex, multi-party B2B conversations, where traditional ICL encounters significant limitations, especially as context length increases due to the concatenation of multiple few-shot examples. We introduce the \texttt{Call Playbook} dataset, featuring five classification tasks derived from real-world B2B conversations targeting core sales concepts. To bridge the gap between performance and practical utility, we propose novel knowledge extraction methods that distill verbose examples into compact, interpretable representations of structured classification criteria and precise task descriptions. Our approach achieves a 99\% reduction in token usage and improves macro-averaged AUC by up to 7\% over traditional ICL. Notably, it remains robust as context grows, unlike advanced token compression baselines which degrade by over 9 F1 points. Importantly, our framework enables direct refinement of classification logic, addressing critical needs for transparency, efficiency, and user interaction in real-world NLP applications.

---


### 99. [NeuroSymbolic AI for Legal AI-TRISM: Trustworthy, Reliable, Interpretable, Safe Models](https://arxiv.org/abs/2606.15646)

**<font color=#1a73e8>作者：</font>** Deepa Tilwani, Yash Saxena, Ankur Padia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have transformed natural language processing, but their lack of interpretable reasoning and tendency to hallucinate pose significant challenges for legal applications. While LLMs show promise for legal text analysis and generation, they struggle with accurate citation attribution and precedent verification. For example, in legal contexts, a single incorrect precedent can jeopardize a case. Current approaches to improve LLM reliability in legal domains suffer from two key limitations: inadequate integration of structured legal knowledge during training or fine-tuning, and insufficient verification mechanisms for generated legal content. To address these challenges, we propose the TRISM (Trustworthy, Reliable, Interpretable, Safe Models) framework, which integrates NeuroSymbolic AI principles with LLMs to leverage both neural learning capabilities and symbolic reasoning over structured legal knowledge. The TRISM approach addresses the above limitations while maintaining interpretable decision pathways. Our framework formalizes the extraction of symbolic knowledge from legal textual documents and incorporates Retrieval-Augmented Generation (RAG) as a core component for grounding LLM outputs in verified legal sources. In this position paper, we make the following contributions: (1) An analysis of the limitations of AI in law; (2) Introduce RASOR RAG which creates foundations for neurosymbolic RAG by generating explicit interpretable rationales that could be formalized into symbolic representations; (3) A formalized methodology for creating symbolic legal knowledge bases that support both interpretable reasoning and output verification in LLMs; and (4) The TRISM framework for integrating symbolic legal knowledge with LLMs.

---


### 100. [Self-Questioning Vision-Language Models: Reinforcement Learning for Compositional Visual Reasoning](https://arxiv.org/abs/2606.15651)

**<font color=#1a73e8>作者：</font>** Saraswathy Amjith  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are AI systems that process both images and text, yet they often struggle with compositional visual reasoning questions that require chaining multiple steps together, such as identifying objects, counting them, and comparing the results. Existing approaches improve this reasoning by training models on human-written step-by-step explanations, but creating these annotations is expensive and difficult to scale. We propose a self-questioning framework that trains a VLM to break visual questions into smaller sub-questions and answer each one before producing a final response, using a reinforcement learning algorithm called Group Relative Policy Optimization (GRPO). The model is never shown examples of how to decompose questions, it discovers this behavior on its own, guided by a reward signal that scores whether the output contains sub-questions and whether the final answer is correct. We apply this framework to a 3-billion-parameter model, training on both synthetic scenes of geometric shapes (CLEVR) and real-world photographs (A-OKVQA). On A-OKVQA, both self-questioning and standard reinforcement learning substantially improve accuracy over the untrained model (52.2% and 51.6% vs. 46.8%). We introduce the first self-questioning VLM by rewarding not only the final answer like standard RL but additionally for generating intermediate sub-questions, enabling it to discover compositional decomposition strategies. These results suggest that teaching AI systems to ask themselves intermediate questions is a promising strategy for complex visual reasoning, particularly when the difficulty of a question warrants explicit step-by-step decomposition.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-270](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
