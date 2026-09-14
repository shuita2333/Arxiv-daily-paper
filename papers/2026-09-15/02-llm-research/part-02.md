# 🧠 大模型相关研究 | 2026年09月15日

> 本类共 **134** 篇论文：已确认 **130** 篇，待复核 **4** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-134](./part-03.md)

---

### 51. [BlueLM-GUI Technical Report: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents](https://arxiv.org/abs/2609.12394)

**<font color=#1a73e8>作者：</font>** Tong Ye, Kunyang Han, Guozhi Wang 等 43 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile GUI agents are shifting from multi-module frameworks to native models trained end-to-end, yet industrial deployment faces three persistent gaps. Sandbox training produces a distribution mismatch with production environments; expensive real-device failures remain underutilized; and fixed benchmarks saturate, losing the power to guide iteration. We present BlueLM-GUI, a 35B-A3B mobile GUI agent built as a real-device-centric flywheel that closes these gaps through three principles. Every Sample Matters: a dual-track pipeline with Heterogeneous Triple-System Consensus evaluation and an Error Correction \& Derivation Module salvages every trajectory into usable supervision. Every Rollout Is Real: a three-stage recipe---continual pre-training, supervised fine-tuning, and agentic reinforcement learning on hundreds of real phones---grounds every rollout in real production environments, so the capability the model learns transfers directly to deployment. Every Query Evolves: a quota-driven benchmark methodology with three orthogonal axes enables precise attribution and allows the benchmark to be systematically upgraded as the model improves. BlueLM-GUI achieves 87.4 on MobileGUI-VBench, surpassing the best closed-source model by 5.1 points, and 84.9 on AndroidWorld, the best result among open-source models and competitive with closed-source models. These results demonstrate that grounding model training and iterative improvement in both real devices and the three Every principles yields strong, robust, and transferable mobile GUI capability.

---


### 52. [UFO: Chain-of-Evaluation for Omni-Condition Alignment in Multi-Modal Image Generation](https://arxiv.org/abs/2609.12397)

**<font color=#1a73e8>作者：</font>** Danning Zhang, Yijing Lin, Shuhan Zhuang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal image generation, particularly subject-driven customization, has garnered growing attention in recent years. Despite the rapid advancement of generative models, their evaluation remains largely lagging. Existing methods, whether embedding-based or Multi-modal Large Language Model (MLLM)-based, evaluate alignment with each modal condition in isolation, which contradicts the simultaneous condition alignment objective of multi-modal image generation, leading to poor consistency with human judgments. To address this challenge, we propose UFO, the first unified framework for omni-condition alignment simultaneous evaluation. Specifically, UFO introduces a novel Atomized Chain-of-Evaluation paradigm, \emph{i.e.}, it first decomposes omni-condition alignment into a sequential chain of fine-grained, disentangled Atomic Evaluation Units (AEUs), categorizes them into distinct modality-relevance classes, and then employs general or dedicated functional calls for accurate verification of different AEU types. Experimental results demonstrate that UFO achieves the highest correlation with human evaluation preferences, delivering an average improvement of 15.25\%. Furthermore, we present UFO-Bench, a dedicated benchmark designed to holistically evaluate the performance of existing customization models under the diverse mutual interactions of textual and visual conditions.

---


### 53. [Beyond ID Embeddings: Process-Grounded Language Modeling for Cognitive Diagnosis](https://arxiv.org/abs/2609.12403)

**<font color=#1a73e8>作者：</font>** Minghang Liu, Yuanzhuo Wang, Qiang Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cognitive Diagnosis Models (CDMs) play a pivotal role in personalized online learning. Traditional CDMs rely on discrete, ID-based embeddings to represent students, exercises, and concepts. This paradigm diverges from the nature of learner cognition, where knowledge is not stored and retrieved as isolated symbols. As a result, CDMs suffer from semantic limitations when new exercises or concepts appear. In this paper, we propose a Process-aware Language Cognitive Diagnosis (PLCD) framework that uses language-derived structures as cognitive priors and response records to calibrate student posterior states. PLCD leverages large language models (LLMs) to construct concept schemas and cognitive process graphs, and uses target-conditioned semantic memory to retrieve historical responses that are relevant to each target exercise. A process-grounded Language-to-Cognition Mapper with DA-MoE experts and process-level contrastive learning then maps the textual evidence into a unified cognitive space. Experimental results show that PLCD not only outperforms traditional baselines in predicting student performance but also exhibits strong cognitive transfer capabilities. These results connect the computational power of LLMs with the psychometric goal of measuring latent knowledge states, suggesting that structured language priors calibrated by response records can improve cold-start robustness and cognitive grounding.

---


### 54. [VRL-Bench: Benchmarking agents on computer control tasks under finite trial budgets](https://arxiv.org/abs/2609.12404)

**<font color=#1a73e8>作者：</font>** Yu Bai, Yukai Miao, Dawei Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning from trial and error is a promising way to improve language agents on complex tasks such as computer control. Reflexion introduced verbal reinforcement learning, which turns failed trials into text that guides later attempts without updating model parameters. We introduce VRL-Bench, a harness for fair evaluation of trial-and-error learning under finite trial budgets. Across three models on MiniWoB and WebShop, we evaluate updates from several prominent verbal-memory methods spanning Reflexion and later work: each improves observed success over memory-free retry in some settings but reduces it in others. Replay experiments show that using reflection can reduce success rates, revealing a trade-off between exploiting experience and continued exploration. We propose VEX$^2$, a verbal exploration--exploitation scheduler that uses a language model to jointly select policies and allocate the remaining trial budget. VEX$^2$ is the only evaluated update to achieve positive observed success-rate gains over retry in all six settings.

---


### 55. [Granularity-Adaptive Credit Assignment for Long-Horizon LLM Agent Reinforcement Learning](https://arxiv.org/abs/2609.12424)

**<font color=#1a73e8>作者：</font>** Taoran Liang, Yang Liu, Shang Luo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning is now the standard way to train large language model agents on long-horizon tasks, where dozens of interdependent actions precede a single sparse reward. Critic-free, group-relative methods such as GRPO suit this regime, but they broadcast one trajectory-level scalar to every step and cannot say which decision drove the outcome. GiGPO recovers a step-level signal by grouping time steps that share an anchor state, yet it merges the step- and episode-level estimates under one fixed weight, spending the same resolution on a pivotal branching decision as on a routine, near-deterministic transition. We argue that the right resolution is state-dependent, and propose GACA, a critic-free estimator whose granularity follows an uncertainty-based criticality proxy. GACA scores every step by the negative log-likelihood its own rollout already records, then blends the two advantages with a per-step weight that grows with that score, so the gradient places more weight on the fine-grained signal at above-average NLL and on the episode-level signal below it. We derive an exact risk decomposition for the implemented mixture and show that sufficiently small modulation improves on fixed mixing under positive directional alignment. A separate conditional result bounds local action-value variation using expected NLL, while an error-projection analysis characterizes when mixing adds value beyond scalar uncertainty reweighting. On ALFWorld and WebShop, GACA improves task success over GRPO and GiGPO at both 1.5B and 7B scales.

---


### 56. [LifeFuse-Mem: Lifecycle-Aware State Fusion Against Temporary Overwriting for Long-Term Memory](https://arxiv.org/abs/2609.12436)

**<font color=#1a73e8>作者：</font>** Hanyu Zhao, Yuqian Feng, Zhenyu Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running LLM agents require memory mechanisms that maintain coherent internal states across interactions. We study a lifecycle-labeled memory setting in which write episodes provide lifecycle metadata during training, and phase-aware readout is used during evaluation. This setting reflects the need to distinguish information that should remain influential across future interactions from information that should affect only the current context. A mismatch between these lifecycles can cause temporary information to overwrite durable knowledge, leading to behavioral drift in persistent agents. Within this setting, we introduce \textbf{LifeFuse-Mem}, a lifecycle-aware neural memory framework that separates information according to its temporal commitment. LifeFuse-Mem uses dedicated memory components and lifecycle-aware updates to allow stable and transient knowledge to evolve locally without converting temporary context into durable state. On the controlled anti-overwrite benchmark, LifeFuse-Mem improves acquisition-controlled retention and reduces temporary overwrite; on two public long-memory benchmarks, it remains broadly competitive. These results suggest that explicit lifecycle signals can help diagnose and mitigate overwrite in compact online memory.

---


### 57. [Beyond the Query: Do Retrieval Signals Improve Adaptive Multimodal RAG Routing?](https://arxiv.org/abs/2609.12437)

**<font color=#1a73e8>作者：</font>** Qiaomu Li, Qiuyuan Zhang, Nong Ming  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive RAG often uses retrieval-time signals to decide whether another retrieval, reranking, or multimodal step should run. We ask whether these signals add routing value once the query itself is already known. Across document, audio, and video RAG, we compare matched query-only and query+retrieval routers while holding the optional actions, router family, training procedure, and evaluation fixed. On the held-out final evaluation, adding the tested retrieval signals does not produce a reliable routing improvement over the query-only baseline. Some retrieval signals are associated with whether a later step will help, but that predictability does not consistently lead to bet- ter RUN/SKIP decisions. The main lesson is therefore methodological: retrieval-state features should not be credited with routing value unless they improve over a matched query-only control. Our results do not show that routing or retrieval state is generally useless; they show that the incremental value of retrieval signals must be demonstrated rather than assumed.

---


### 58. [Do LLMs Trust the Accuser or the Accusation? Measuring Belief Shifts in Werewolf](https://arxiv.org/abs/2609.12446)

**<font color=#1a73e8>作者：</font>** Yu-Yu Yang, Ti-Rong Wu, Hung Guei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Social-deduction games such as Werewolf are increasingly used to evaluate LLM agents, but existing evaluations often rely on final game outcomes. We propose a belief-shift evaluation benchmark in Werewolf for analyzing communication skills through belief updating. Using LLM-played games, we annotate suspicion and accusation messages and measure how an observing village-side model's beliefs change after each message. We evaluate 40 open-weight LLM configurations on 1,224 annotated messages. Our results show that larger models better distinguish true wolves from villagers based on game history, but accusations still strongly influence their beliefs. Models become more suspicious of the accused target and less suspicious of the accuser, especially when the accuser is trusted, even if the accuser is wolf-aligned. Larger models better resist accusations from accusers they already distrust. Overall, our findings suggest that current open-weight LLMs up to 120B parameters still struggle to integrate accusation content with source trust in strategic communication. Our benchmark and code are available at this https URL.

---


### 59. [GraphProfiler: Source-Linked Sensitive Attribute Inference via Personal Knowledge Graphs](https://arxiv.org/abs/2609.12448)

**<font color=#1a73e8>作者：</font>** Ahmed Sohair Khan, Estrid He, Chenglong Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sensitive attributes such as age, income, and occupation can be inferred from user-generated content by aggregating indirect cues across many ordinary posts. LLM-based profilers can perform this aggregation automatically and with high accuracy, which makes large-scale personal attribute inference a major privacy threat. Existing LLM-based profilers, however, offer limited insight into which specific posts, concepts, and relationships made an inference possible, which is key to targeted privacy mitigation, i.e., redacting or rewriting only the few posts that actually leak an attribute, rather than perturbing entire histories. We introduce GraphProfiler, an auditable LLM-based profiler that represents each user's post history as a source-linked personal knowledge graph where nodes and edges trace back to the originating post and resolves attribute predictions to cited graph records and source texts. GraphProfiler reaches 86.7% attack success rate on the eight-attribute SynthPAI benchmark, within two points of strong text-only baselines, and 84.6% on PANDORA, while citing supporting evidence for over 98% of predictions. Our controlled ablation experiments provide evidence that the cited posts contribute to attack success, as removing them reduces the attack success rate substantially more than removing an equal number of random posts.

---


### 60. [Bridging Vision Foundation Model Priors with CLIP for Spatial-aware Few-shot Anomaly Detection in Medical Images](https://arxiv.org/abs/2609.12454)

**<font color=#1a73e8>作者：</font>** Juzheng Miao, Yuchen Yuan, Cheng Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models such as CLIP enable effective few-shot medical anomaly detection (AD) via strong image-text semantic alignment. However, their globally contrastive pretraining lacks explicit spatial supervision, limiting precise lesion localization. In contrast, Vision Foundation Models (VFMs) such as DINO learn spatially coherent patch representations via self-distillation and local-to-global consistency, better capturing fine-grained anatomical structures. Leveraging this complementarity, we propose Spatial-FAD, a spatial-aware few-shot medical AD framework that improves lesion localization by combining VFM spatial priors with CLIP semantics. Specifically, we introduce a VFM-enhanced adapter that injects a structural affinity prior derived from DINO into CLIP features. This structure-guided refinement encourages visual embeddings to better adhere to lesion boundaries while maintaining semantic alignment. To address the loss of spatial detail from patchification and the limited input resolution of CLIP, we adopt a sliding-window aggregation strategy. This generates high-resolution, spatially dense embeddings to further enhance localization granularity. Moreover, we introduce a prototype-enhanced support memory scheme to efficiently exploit the few-shot support set. This module stores compact prototypes for normal and abnormal patterns, reducing memory costs while boosting performance by fusing patch-to-prototype and image-text similarities. Extensive experiments on three benchmark datasets, including Liver CT, Retinal OCT, and Brain MRI, demonstrate that Spatial-FAD significantly outperforms state-of-the-art methods, especially in lesion segmentation. Notably, in the 4-shot scenario, our method achieves an average improvement of over 11.4% in Dice score and 1.8% in AUC. Code is available at: this https URL.

---


### 61. [SAGE-Loop: Reliable Closed-Loop LLM-Driven AutoML with Trial-and-Correction and Adaptive Ensembling](https://arxiv.org/abs/2609.12455)

**<font color=#1a73e8>作者：</font>** Junquan Gu, Shibo Cui, Xiangfeng Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated machine learning (AutoML) is reshaping data-driven science and industrial practice, and as large language models are introduced into AutoML, pipeline reliability becomes as important as automation efficiency. However, existing AutoML still struggles to realize instant feedback and adaptive optimization during execution, so once a run drifts into a suboptimal or failed state, it lacks a process-level correction mechanism. The fundamental pathology lies in its one-way pipeline: intermediate failures are typically terminated or bypassed, while fixed paradigms often strengthen model generation but leave ensemble decisions static, weakening both execution reliability and the controlled use of structural diversity. This indicates that LLM-driven AutoML needs a closed-loop ability for trial-correction-improvement together with evidence-based use of model diversity. To this end, we propose SAGE-Loop, a reliable closed-loop, self-adaptive, LLM-driven AutoML framework that performs multi-round generation and validation for trial-and-repair, and adaptively selects ensemble strategies in both supervised and unsupervised tasks, thereby unifying how to generate with how to use models. Across 20 public datasets, SAGE-Loop consistently improves performance and stability on classification, regression, and clustering tasks. Additional results further show its ability to recover from execution failures and maintain robust pipeline behavior.

---


### 62. [Beyond Vector Similarity: Hierarchical Context-Aware Graph RAG vs Standard RAG in Enterprise Code Migration](https://arxiv.org/abs/2609.12464)

**<font color=#1a73e8>作者：</font>** Nilesh Jaiswal, Aniket Agrawal, Arjit Shukla 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As enterprises modernize legacy monolithic systems to microservices, Large Language Models (LLMs) are heavily utilized for automated code translation. However, traditional vector-based Retrieval-Augmented Generation (Standard RAG) struggles to capture topological relationships. It fetches isolated chunks that sever inheritance chains, leading to high compilation failure rates. This paper introduces a Hierarchical Context-Resident Graph (HCRG) methodology to resolve these limitations. Our pipeline uses tree-sitter for Abstract Syntax Tree (AST) extraction, maps architectural edges into a Google Cloud Spanner Property Graph, and serializes this structure into a Gemini Context Cache for topological, parent-first code translation. We shift evaluation from naive text-overlap to a custom 7-metric Software Engineering framework. Traditional metrics like CodeBLEU (which scored 91% for both methods) effectively masked Standard RAG's structural failures behind syntactically plausible but broken code. Empirically, Graph RAG decisively mitigates dependency loss: API hallucination rates dropped from 56.4% to 16.2%, Dependency Resolution Quality improved from 34.8% to 65.9%, and Parent-Child Consistency rose from 26.7% to 45.5%. However, Graph RAG introduces specific trade-offs. The dense global context causes defensive over-engineering by the LLM, reducing Cyclomatic Complexity Consistency from 71.6% to 46.7%, and slightly degrades Docstring Preservation (67.0% to 61.0%). Ultimately, while trading code complexity for reduced hallucinations, Graph RAG provides a substantially more viable, architecturally sound path for automated enterprise codebase modernization.

---


### 63. [AMDKernelVault: Large-Scale Datasets and Agentic Training for AMD GPU Kernel Optimization](https://arxiv.org/abs/2609.12471)

**<font color=#1a73e8>作者：</font>** Ji Liu, Saptarshi Majumder, Yiqing Huang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce AMDKernelVault, an open HIP and Triton kernel corpus and training framework for recent AMD CDNA GPUs. Existing LLM-based kernel agents are largely CUDA/NVIDIA-centric and often depend on repeated frontier-LLM calls for generation, reflection, and optimization. To address this gap, we develop HIPKernelGen and TritonKernelGen, agent-driven pipelines that transform PyTorch references into HIP or Triton kernels, compile and validate candidates under ROCm, and latency-profile them on AMD hardware. The corpus contains 62,153 execution-verified HIP kernel samples, 2,377 production-grounded ROCm Libraries QA entries, and 39,893 Triton kernels. We further train Qwen3-8B with supervised fine-tuning and execution-aware reinforcement learning as a demonstration of the corpus's utility. Under fixed evaluation budgets, it achieves the highest correctness among the compared models on PyTorch-to-HIP (34.0% Pass@1), TritonBench-G (33.2% Corr@3), and ROCmBench (41.94% Corr@3), but does not uniformly lead compilation or speed metrics. The corpus and documentation are available at this https URL, and the associated training and kernel-generation code is available at this https URL.

---


### 64. [TripPattern: A Pattern-based Text Watermarking Method for Large Language Models](https://arxiv.org/abs/2609.12472)

**<font color=#1a73e8>作者：</font>** Sangjun Moon, Dasom Choi, Jingun Kwon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text watermarking techniques have gained significant attention for identifying machine-generated text and mitigating risks from large language models (LLMs). Existing methods typically divide an LLM's vocabulary into green and red tokens, but encouraging generation toward green tokens can reduce text quality and naturalness. To address this, we propose TripPattern, a watermarking framework that formulates text watermarking as a pattern-based matching task using three vocabulary partitions. TripPattern divides the vocabulary into one neutral group and two pattern groups. During generation, the model alternates token selection between the two pattern groups to embed detectable patterns, while neutral tokens are selected independently to improve flexibility and preserve naturalness. For detection, TripPattern uses pattern-based statistical tests that provide interpretable p-values by measuring how often adjacent tokens alternate between the pattern groups. Theoretical analysis and empirical evaluations on four multilingual datasets show that TripPattern maintains LLM generation quality while achieving robust watermark detectability.

---


### 65. [Zipbench: Low-Cost Framework for Compressing Comprehensive Benchmarks of Large Language Models](https://arxiv.org/abs/2609.12475)

**<font color=#1a73e8>作者：</font>** Zhongzhan Huang, Junxin Li, Guoming Ling 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Comprehensive benchmark suites are essential for improving large language models (LLMs), but many widely used benchmarks are redundant, making evaluation unnecessarily expensive. Although recent benchmark compression methods (BCMs) can mitigate this cost, many strong BCMs rely on large collections of per-sample evaluation results from numerous LLMs to identify representative samples. Building such collections is also expensive unless they are already public, making these methods difficult to extend to newly released benchmarks. To address this challenge, we present ZipBench, a simple and low-cost BCM with theoretical error and rank-consistency guarantees. ZipBench evaluates only a small set of anchor LLMs, synthesizes pseudo evaluation results to broaden coverage, learns compact sample representations, and selects a small yet representative subset. Building on it, we create ZipBench Zoo, a collection of compact versions of 100+ benchmark proxies spanning text, multimodal, and agent tasks. These benchmark achieve mean absolute errors of 0.002--0.02 and average Spearman correlations of ~0.98 with the full benchmarks. Overall, ZipBench reduces the cost of both LLM evaluation and compact benchmark construction, lowering the barrier to broad LLM research for compute-constrained researchers. The code has been released in this https URL.

---


### 66. [Confidence-Gated Transductive Test Generation for Code Reranking](https://arxiv.org/abs/2609.12489)

**<font color=#1a73e8>作者：</font>** Sungjae Lee, Youngsik Yoon, Seockbean Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test case synthesis is crucial for evaluating and ranking programs generated by large language models (LLMs). However, constructing high-quality test cases remains challenging because reliable expected outputs are often difficult to obtain. We propose Confidence-Gated Transductive Test Generation (CoTT), which first uses an efficient inductive procedure and invokes transductive generation only when inductive confidence is low. This adaptive design improves output reliability while allocating extra computation only when needed. On code reranking benchmarks, CoTT outperforms prior baselines across the reported metrics while reducing cost relative to applying transductive generation to every input. These results show that confidence-based allocation of test-time computation provides a favorable efficiency-effectiveness trade-off with a single efficient LLM.

---


### 67. [Information Specialization and Constrained Synthesis in Multi-Agent LLM Forecasting: A Prospective Live-Study of the 2026 FIFA World Cup](https://arxiv.org/abs/2609.12495)

**<font color=#1a73e8>作者：</font>** Julian Varghese, Lucas Bickmann, Sarah Sandmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are being organized into multi-agent systems with specialized roles, but whether such specialization produces distinct forecasts and whether subsequent synthesis improves utility remains unclear. In this study, we carried out a live, prospective evaluation over the final 56 matches of the information-dense 2026 FIFA World Cup, keeping a frontier foundation model constant while assigning two primary forecasting agents contrasting specialist roles: a quantitative specialist focusing on structured performance statistics and a news specialist focusing on current injuries, tactics and information from press conferences. Their forecasts were then reviewed by a separate critic before being combined by a meta-agent, resulting in a sequential four-agent model. Forecasts from the betting market served as an external benchmark. The news specialist obtained the highest mean probability-weighted Top-3 utility and matched the betting market in Top-3 exact-score hits. Nevertheless, the two specialist forecasters agreed on at least two of the three scorelines in 50 out of 56 matches, and the meta-agent never generated more than one scoreline outside the specialists' forecast set. These findings show that rapidly changing, unstructured information can provide a valuable forecasting signal alongside structured statistics, whereas adding critic and meta-agent stages does not necessarily create complementary information or improve on the strongest specialist.

---


### 68. [ChitraMiti: Benchmarking Visual Grounding and Modality Reliance in Bengali Geometric Reasoning](https://arxiv.org/abs/2609.12509)

**<font color=#1a73e8>作者：</font>** Khan Raiyan Ibne Reza, Sanjana Aktar Maria, Sumaiya Tabassum Nimi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluation of vision-language models (VLMs) for multimodal mathematical reasoning remains limited for low-resource languages and for geometry problems that require reading a diagram and a question together. We introduce ChitraMiti-12.8k, a synthetic benchmark of 12,874 Bengali planar geometry problems paired with structured 15-attribute descriptions, and NCTB-500, a complementary set of 500 diagrams manually extracted from Bengali school textbooks. Using a three-phase protocol that separates diagram-only, diagram-plus-description, and description-only inputs, we show across five open-weight and closed-source VLMs that description-only performance is statistically indistinguishable from diagram-plus-description performance, establishing structured descriptions as a sufficient textual proxy for controlled evaluation. Despite this, models remain poor at cross-modal verification, frequently misled by a swapped spatial relation even when they answer the unmodified item correctly. We further evaluate supervised adaptation on ChitraMiti-12.8k, finding that fine-tuning improves performance on both ChitraMiti-1k and NCTB-500, although a substantial gap to the strongest zero-shot model remains. Together, ChitraMiti-12.8k, NCTB-500, and our evaluation protocol offer a standardized way to study Bengali multimodal geometry reasoning and, more broadly, whether VLMs actually check their text against what they see. Our dataset and code are publicly available on Hugging Face at this https URL.

---


### 69. [One Skill Does Not Fit All: Automatic Discovery and Taxonomy-Guided Routing of Frame-Selection Skills for Long-Video Question Answering](https://arxiv.org/abs/2609.12517)

**<font color=#1a73e8>作者：</font>** Jian Hu, Zixu Cheng, Da Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-Video Question Answering (LVQA) requires locating decisive evidence in hour-scale videos under a limited frame budget. Most training-free methods apply the same frame-selection strategy to all questions, despite substantial variation in the evidence required by different question types. Our analysis shows that the relative effectiveness of frame-selection strategies varies across semantic categories and benchmarks, motivating adaptive evidence acquisition. In this paper, we introduce AutoSkill, a source-supervised framework for automatically discovering and routing executable frame-selection skills. Starting from a small labelled source pool, LLM agents iteratively propose, implement, evaluate, and refine candidate skills. For a target benchmark, AutoSkill uses only unlabelled question and option text to induce a shared semantic taxonomy, rewrite labelled source examples into the target style, and estimate a category-to-skill mapping. Neither target videos nor target answers are used in this process. At inference time, each question is assigned one skill, which selects the frames used in a single inference of the frozen video MLLM. Across five long-video benchmark splits, AutoSkill improves Qwen2.5-VL-7B and Qwen3.5-4B by 2.4% and 1.2%, respectively, demonstrating the effectiveness of our AutoSkill.

---


### 70. [Earth-Agent-Pro: Towards Real-World Full-Chain Earth Observation with Agents](https://arxiv.org/abs/2609.12533)

**<font color=#1a73e8>作者：</font>** Zhutao Lv, Chenhao Dang, Yi Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world Earth observation (EO) agents must translate high-level scientific questions into executable workflows to acquire observations, prepare data, perform domain computations, and derive conclusions from runtime evidence. Existing EO agents typically start from supplied observations, while benchmarks typically provide prepared inputs or candidate answers, leaving full-chain open-world EO execution largely untested. We present Earth-Agent-Pro, an execution-adaptive Plan-and-Execute framework using expert-authored skills to constrain planning and runtime tool use. Workflow-centered structured memory records planned steps, accepted evidence, and their dependencies, enabling repair of only the affected workflow suffix when runtime evidence invalidates a step. Separate large language model adapters use sequence-level supervised fine-tuning for planner workflow composition and node-level group relative policy optimization with locally verifiable rewards for executor tool-argument grounding. Earth-Bench-Pro instantiates 248 expert-curated task cores as 744 questions under three matched regimes. Its 248 Open-World Execution questions span RGB imagery, spectral observations, and remote sensing products, pairing high-level requests with runtime data requirements, executable trajectories, and open-ended answers grounded in execution evidence. With a shared GPT-5 backbone, Earth-Agent-Pro achieves 66.13% LLM-as-Judge accuracy, exceeding ReAct by 20.95 points in this metric and 24.44 points in Tools-In-Order. Joint adapter tuning raises Qwen3.5-9B LLM-as-Judge accuracy from 38.31% to 50.00%, an 11.69-point gain over the untuned configuration. Planning-only evaluation and execution with the reference workflow show that the adapters improve workflow composition and argument grounding, respectively. Code and datasets will be released soon.

---


### 71. [The House with a Million Windows: Interactive Fiction for Narrative Restorying](https://arxiv.org/abs/2609.12537)

**<font color=#1a73e8>作者：</font>** Cody Kommers, Sarah G Immel, Drew Hemment 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-assisted writing can flatten meaning in human storytelling, enabling the production of homogeneous outputs without the intentional effort and sense-making writing entails. To address this challenge, we present The House with a Million Windows (HWAMW), an LLM-based interactive fiction system designed to help users explore both the breadth and depth of potential meanings within their personal stories -- drawing on a psychological paradigm called the restorying intervention. In HWAMW, users play through a text-based narrative in which they tell a story, then encounter a set of LLM-generated "windows" reframing it according to different literary styles. Empirical evidence shows that HWAMW increases users' sense of narrative identity, while an expert review explores how this effect is achieved. Our findings suggest that HWAMW facilitates restorying and offers a valuable paradigm for AI-assisted writing, wherein LLMs do not tell our stories but rather help us see greater potential in the stories we tell.

---


### 72. [Quality-Constrained Routing over a Fixed Pool of Quantized Mixture-of-Experts Instances](https://arxiv.org/abs/2609.12550)

**<font color=#1a73e8>作者：</font>** Zhenghong Huang, Hongfan Wu, Jiheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantized Mixture-of-Experts (MoE) services can hold several pre-materialized instances of one base model, but quantization damage varies sharply across requests and bitwidths. Because instance materialization and replica counts consume memory and require slow reconfiguration, we treat them as upstream provisioning decisions and study routing within a fixed resident pool. Within this fixed-pool boundary, we route each request to maximize modeled throughput under a class-level expected quality-degradation budget and measured instance capacities. To predict this request-specific risk, we introduce FWP (Fragility-Weighted Perplexity), computed from prompt tokens on a reference-instance prefill and calibrated to candidate-instance degradation. Underlying FWP is an exact two-expert affinity--fragility decomposition and a conditional multi-layer top-$k$ expansion whose bias, interaction, route-change, separability, and higher-order terms remain explicit. Using these calibrated risks, a window-level linear program yields a signed reduced-reward score that is KKT-consistent with the LP optimum under optimal prices and primal-feasible tie allocation. On 88 extended Qwen prompts, complete W2, W3, and W4 instances quantizing all 6,144 expert blocks incur mean $\Delta$NLL of $0.9437$, $0.1832$, and $0.0513$. Under the same population and $\tau=0.1513$, FWP allocation reaches a $1.284\times$ offline model-based multiplier versus $1.253\times$ for request-agnostic mixing and $1.000\times$ for static W4, an incremental $2.5\%$ relative FWP gain.

---


### 73. [RelateAnything: Real-Time Open-Vocabulary Relation Prediction From Any Inputs](https://arxiv.org/abs/2609.12552)

**<font color=#1a73e8>作者：</font>** Maëlic Neau  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary detection accepts any class list at inference, and promptable segmentation returns regions without class names: the taxonomy has left the model and become an input. Relation prediction has not. Scene-graph models are still trained and evaluated on the 50 or 56 predicates of one annotation style, their relation head conditioned on object labels and so tied to one detector. Three obstacles explain this, none primarily modelling: no relation corpus is both free-text and verified, a label-conditioned architecture cannot accept a vocabulary it was not trained on, and the standard metric rewards agreement with the training corpus, so a larger vocabulary scores as a regression. We present RelateAnything, a 53M-parameter model taking an image and regions from any source and returning scored relations over a predicate vocabulary supplied at inference as strings. Object labels are never an input, so the region source can change without retraining, and the vocabulary is a bank of text embeddings, not a learned classifier. It runs at 20 ms/frame. Training over 19,103 predicates requires positive-unlabeled supervision and a text encoder that separates antonyms, which contrastive encoders embed at cosine 0.95. To supply the supervision we build RA-4M, 474k images and 4.3M relations over 10,102 free-text predicates, generated against numbered box markers and geometrically verified. To measure it we build OV-SGG-Bench, six axes scored across datasets that the priors standard recall rewards cannot satisfy. On three cross-dataset benchmarks and a fourth zero-shot, RelateAnything has 2.3-3.5x the mean recall of the strongest open-vocabulary method of comparable scale, margins that survive a real detector, and leads a 3B-VLM scene-graph model on both metrics at under 2% of its parameters. In-domain measurement overstates transfer gains ~5x. Model, corpus and benchmark are public.

---


### 74. [PIA-Bench: Towards Automated Privacy Impact Assessment with Large Language Models](https://arxiv.org/abs/2609.12571)

**<font color=#1a73e8>作者：</font>** Jiamin Zheng, Hao-Ping Lee, Luo Mai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy impact assessment (PIA) is a critical instrument for institutions to proactively identify privacy risks and develop mitigation strategies before system deployment. While mandated across regulatory and institutional contexts, executing PIA requires extensive privacy and technical expertise, posing a particular challenge for teams without access to such resources. Prior work shows the potential of leveraging large language models (LLMs) to assist practitioners' privacy decisions, but little is known about how accurately and reliably LLMs can automate PIA. To this end, we develop PIA-Bench, the first open benchmark for evaluating LLMs on real-world PIAs. We first audited 499 expert-authored PIAs published by US federal agencies and curated 73 structured PIAs, comprising a total of 451 privacy risk and 831 mitigation items, to evaluate LLMs' ability to assess privacy risks and propose mitigations of complex systems. Our results show that off-the-shelf LLMs produce meaningful assessments and identify avenues for future improvement. Finally, we call for improving domain-specific workflows for LLM agents, developing accountable LLM infrastructure, and designing new quality standards for PIAs.

---


### 75. [Calibrated Ambiguity in Multimodal Language Models: Humans reach for cultural references, while models describe the picture](https://arxiv.org/abs/2609.12575)

**<font color=#1a73e8>作者：</font>** Cody Kommers, Mingrui Ye, Evelyn Gius 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ambiguity is often treated as a bug for AI systems to resolve---but in human communication and culture, ambiguity can also be a generative resource. From humour to politics to art, people express themselves in words and images that are open enough to invite different interpretations, yet constrained enough to be interpretable. We operationalise this notion of calibrated ambiguity with a task drawn from the parlour game Dixit. We compare differences in clues generated by human vs multimodal language models, based on a novel coding rubric for calibrated ambiguity, and find that models consistently exhibit ambiguity collapse (i.e., their outputs are over-specified, leaving no room for multiple legitimate interpretations). Unlike human clues, AI-generated clues also exhibit cultural flattening; they almost never make reference to culturally-situated knowledge, even when prompted to use allusion and figurative language.

---


### 76. [From Collaboration to Capability: Internalizing Routed LLM Experts into Compact Reasoners](https://arxiv.org/abs/2609.12578)

**<font color=#1a73e8>作者：</font>** Frank Nie, Shuyao Wang, Ethan B. Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A compact controller can coordinate stronger experts by selecting whom to consult, formulating requests, and integrating their responses. We study whether learning from both the controller's decisions and the experts' reasoning and code improves its generation after expert removal. We introduce \textsc{Rivet} for \emph{collaboration internalization}: expert-augmented reinforcement learning applies a shared outcome signal to controller decisions and returned expert spans, and verified trajectory internalization consolidates complete successful interactions through format-aware supervised training. The deployed controller generates reasoning, code, and interaction structure with local Python execution and no external LLM. Across seven competition-mathematics benchmarks, RIVET-1.7B and RIVET-4B achieve average accuracies of $28.25\%$ and $44.16\%$; Stage~II improves RIVET-4B's accuracy after expert removal by $6.49$ points, and GPQA-Diamond results provide evidence of generalization to scientific reasoning. Ablations show gains from ordinary trajectory supervision and additional format weighting, supporting the effectiveness of training on the content and structure of verified collaborations.

---


### 77. [SCOPE-OPSD: Fisher-Conditioned Privileged Subspaces for On-Policy Self-Distillation](https://arxiv.org/abs/2609.12579)

**<font color=#1a73e8>作者：</font>** Yunmeng Chen, Kunyu Wang, Peihan Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) scores student-generated prefixes with a solution-conditioned self-teacher, yet transfers supervision only through next-token probabilities. We ask whether the aligned final-layer discrepancy offers a useful second channel, and how to test that channel without confusing its geometry with auxiliary strength. SCOPE-OPSD projects the privileged teacher-student residual onto a frozen rank-64 factor estimated from residual covariance and language-model-head Fisher sensitivity. It reuses the forwards already required by OPSD and adds neither rollouts nor inference-time modules. A matched Random control preserves the structured factor's rank and nonzero spectrum and uses per-arm gradient-RMS calibration, isolating the effect of the data-dependent orientation. Across the complete 25/50/75/100-step trajectories for Qwen3-1.7B, 4B, and 8B, Structured is never below Pure OPSD, with strict gains in 11 of the 12 model-checkpoint combinations and an exact tie at 4B step 25. Structured also exceeds matched Random in 10 of the 12 combinations. At step 75 on Qwen3-1.7B, Structured exceeds matched Random by 1.39 Macro Avg@12 points in each of two independent training reruns. A cross-fitted diagnostic also shows 4.40 times greater held-out privileged-gap capture than the matched random orientation. The results support a compact, Fisher-conditioned privileged subspace for short-budget OPSD.

---


### 78. [Clustering-Based Balanced Sampling and Allocation with Data Parallelism for High-Performance Fine-Tuning](https://arxiv.org/abs/2609.12584)

**<font color=#1a73e8>作者：</font>** Hyunjin Kim, Youngeun Nam, Jaemin Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instruction-tuning datasets for large language models (LLMs) are often large, redundant, and imbalanced, limiting efficient adaptation. Naive large-batch fine-tuning repeatedly includes overrepresented sample groups while weakly covering underrepresented but informative ones, especially under data parallelism (DP) across multiple GPUs. We propose CluSTER, a Cluster-aware balanced Sampling framework for Training Efficient data Reduction in DP instruction tuning. CluSTER curates a representative reduced dataset through gradient-space clustering and DP-aware balanced allocation, ensuring dual-level coverage across clusters and workers, while preserving the original data distribution by weighted update. As a result, CluSTER reduces redundant computation and improves training stability without compromising model quality. Across multiple instruction-tuning datasets, CluSTER reduces training time by up to 69.6% with almost no accuracy loss compared to prior sampling and data reduction methods. Code is available at this https URL.

---


### 79. [Reproducing and Evaluating the Generalizability of Subliminal Learning in Open-Weight Models](https://arxiv.org/abs/2609.12586)

**<font color=#1a73e8>作者：</font>** Daan van der Weijden, Nathan Brack, Selene Baez Santamaria  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this reproduction paper we investigate subliminal learning, a consequence of distillation where teacher models transmit behavioral preference traits through semantically unrelated data. The original paper explores two types of traits (animal preferences and misalignment), three data modalities (number sequences, code, and chain of thought), and several model families. We reproduce their experiments and extend the setup along three axes: new preference categories (actors and politicians), a new task (chess move generation), and an additional open-weight model (Ministral8B). We also run a controlled ablation on the numbers task's answer-space size (1-, 2-, and 3-digit sequences). We focus on open-weight models with accessible checkpoints on HuggingFace, since the original paper's GPT-4.x fine-tuning is no longer available. Our reproduction supports the original paper's claims, but our extensions show they are not universal as transmission strength varies across traits and tasks, and one model shows almost no effect at all.

---


### 80. [Where Decoder Cosine Similarity Fails for SAE Feature Flow Discovery](https://arxiv.org/abs/2609.12591)

**<font color=#1a73e8>作者：</font>** Hendrik Droste, Christian Medeiros Adriano, Kathrin Korte 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are increasingly adapted through fine-tuning, model editing, and alignment procedures while retaining previously acquired capabilities. Understanding the internal computations that support these adaptations is therefore becoming increasingly important for continual model evolution. Sparse autoencoders (SAEs) provide interpretable feature dictionaries for residual-stream activations and sublayer outputs, but it remains unclear how state features and update features interact to produce downstream residual features. In this work, we focus on MLP updates as a first test case. We construct a transition atlas of triples $s_k + u_j \rightarrow t_\ell$, where a residual-state feature and an MLP-update feature jointly predict a target residual feature, and validate candidate triples by ablating the decoded update feature. In a 20M-token Pythia-160M $L_7 \rightarrow L_8$ run, we find 38,125 strong ablation-effect transitions, but 88.0% have both state-target and update-target decoder cosine similarity below 0.7. As a preliminary cross-model check, a run of 20M-token Gemma-3-4B $L_{21} \rightarrow L_{22}$ causally validates only the top 30,000 ranked candidate triples by ablating the decoded update feature, and 53.6% of strong-effect triples have both state-target and update-target decoder cosine similarity below 0.7. The Gemma result is directionally consistent with Pythia, but weaker, since update-target cosine recovers many of the strongest Gemma effects and the run is not a full-atlas causal validation. Ultimately, our results suggest that feature flow atlases can serve as diagnostics of representation-update mechanisms and thereby inform tools for steering model updates. Future work will validate more complex patterns across layers, models, and SAE families.

---


### 81. [TraceMind: Predicting User Information Uptake from Low-Cost Interaction Traces during Human-LLM Content Co-Generation](https://arxiv.org/abs/2609.12600)

**<font color=#1a73e8>作者：</font>** Yu Mei, Fengyou Zu, Ruiwen Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In human-LLM content co-generation, AI-generated information can enter final artifacts without being adequately processed by users, creating risks when artifacts are shared or acted upon. We study whether recognition-level uptake of atomic information units can be assessed in open-ended co-generation and predicted from low-cost interaction traces. We collected data from 62 participants across three tasks. For each final draft, we extracted atomic information units and generated post-task recognition questions, yielding 1187 unit-level uptake labels. We present TraceMind, which tracks units across Chat and Draft histories, aligns interaction traces with changing on-screen layouts, and models spatial, temporal, and workflow-informed evidence. TraceMind outperformed all learned baselines across AUROC, AUPRC-non, balanced accuracy, and macro-F1. We found that uptake unfolds throughout interaction, with sustained active engagement providing informative evidence beyond isolated signals. Our work shifts human-LLM co-generation from content adoption toward what users actually take up, motivating uptake-aware systems grounded in low-cost interaction traces.

---


### 82. [Beyond Generation and Accuracy: Diagnosing and Enhancing Visual Chain-of-Thought for Geometry Problem Solving](https://arxiv.org/abs/2609.12606)

**<font color=#1a73e8>作者：</font>** Zhitong Dong, Jicai Pan, Yingguo Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While multimodal reasoning has advanced rapidly, solving complex geometry problems critically hinges on active visual assistance, such as constructing auxiliary lines, spurring the rise of Visual Chain-of-Thought (VCoT). However, existing evaluations typically assess visual generation quality and final answer accuracy in isolation, failing to examine whether intermediate visual aids are geometrically valid, effectively utilized in subsequent reasoning, or causally responsible for task success. To bridge this gap, we introduce GeoVAD-Bench, a diagnostic benchmark that pairs a fine-grained five-dimensional trajectory diagnosis covering perception, auxiliary quality, utilization, deductive reasoning, and final correctness with controlled No-Aux, Auto-Aux, and GT-Aux intervention settings to systematically isolate intermediate error modes, the causal gains of visual aids, and the resulting autonomy gap. Our findings reveal that while high-quality auxiliary aids offer substantial theoretical gains for geometric problem solving, autonomous generation is frequently hampered by compounding errors across geometric perception, faithful visual manipulation, visual-state grounding, and deductive reasoning. Guided by these diagnostic insights, we establish a specialized data construction pipeline encompassing geometric perception, diagram editing, and interleaved visual-textual reasoning trajectories, and develop a progressive SFT and multimodal RL training framework. The resulting model, GeoWeave-8B, outperforms the base model by +25.3% in final geometric accuracy and achieves a +30.4% gain in process average across the four intermediate diagnostic dimensions.

---


### 83. [Distortion of AI Alignment Revisited: RLHF is a Decent Utilitarian Aligner](https://arxiv.org/abs/2609.12651)

**<font color=#1a73e8>作者：</font>** Kazusato Oko, Annie Ulichney, Nika Haghtalab 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Reinforcement Learning from Human Feedback (RLHF) is the standard paradigm for aligning large language models with human preferences, its effectiveness in pluralistic settings has been called into question. Notably, recent work by Gölz et al. (2025) demonstrated that the \textit{distortion} -- defined as the multiplicative gap between the average user utility of the RLHF policy and the optimal average utility -- can scale exponentially with the Bradley-Terry temperature parameter $\beta$ when users have heterogeneous preferences. In this work, we present a fine-grained analysis of the distortion of RLHF with reward clipping and demonstrate that such exponential degradation is not a fundamental property of the algorithm but rather a consequence of distribution mismatch between the distribution generating preference data ($\mu$) and the KL reference policy ($\pi_{\mathrm{ref}}$). To this end, we establish tight upper and lower bounds on the distortion of RLHF across multiple regimes of the KL regularization strength. We show that in a representative regime, under the Bradley-Terry model, the distortion is $\tilde{\Theta}(\beta B + \beta)$, where $B$ is an upper bound on the log density ratio between $\mu$ and $\pi_{\mathrm{ref}}$. In particular, when there is no distribution mismatch (i.e., $\mu = \pi_{\mathrm{ref}}$), RLHF achieves the optimal distortion of $O(\beta)$ up to a constant. Our results suggest that, to reasonably maximize average utility with RLHF, it is preferable to use on-policy sampled preference data or to fine-tune before RLHF on data from a source close to $\mu$.

---


### 84. [SWARM: A Multilingual Human-Annotated Dataset for Russian Propaganda Detection in Search Engine Results](https://arxiv.org/abs/2609.12653)

**<font color=#1a73e8>作者：</font>** Manuel Tonneau, Abhinav Dubey, Farhan Shaikh 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Russian state propaganda spreads across many languages and online spaces. Yet, most computational work examines only one such space, usually social media, in one or two languages, and analyses sources rather than content. We introduce SWARM (Search-Web documents Annotated for Russian propaganda, Multilingual), a dataset of 2,183 search engine results across nine languages and diverse web domains (e.g., news, blogs, government sites), each annotated by trained coders for whether it supports a recurring Russian propaganda narrative. We benchmark a source-based blocklist, supervised classifiers, and zero-shot LLMs against these labels. The blocklist misses most propaganda-supporting documents, because such content is not confined to flagged "propaganda" outlets but also appears on mainstream ones. Content-level analysis helps, though how much depends on the model: the strongest LLM reaches a positive-class F1 of 0.73, whereas the supervised classifiers reach only about 0.5, with the smaller LLMs over-predicting support, mistaking topical relevance for endorsement. Detecting search-borne propaganda thus requires per-language, content-level evaluation, which we hope SWARM and our evaluation code enable.

---


### 85. [LifeMem: Enabling Lifelong Experience Reuse for LLM Agents](https://arxiv.org/abs/2609.12655)

**<font color=#1a73e8>作者：</font>** Yuli Qiu, Yutong Li, Wei Su 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents are expected to continuously adapt to new tasks and environments over their lifetime by reusing past experience. However, existing memory-based agents struggle to transfer reusable experience across environments and suffer from catastrophic forgetting as experience accumulated. To address these challenges, we propose LifeMem, a lifelong learning framework that enables agents to transfer knowledge across multiple environments. During learning, LifeMem clusters accumulated interaction trajectories based on underlying workflows to extract reusable skills. When solving a new task at inference time, the agent recalls relevant skills and trajectories to guide actions. To validate our method, we conduct experiments across 10 environments and over 13k tasks with 2k newly annotated interaction trajectories. Results show that LifeMem enables effective experience reuse in lifelong learning, achieving both reduced forgetting on learned tasks and superior cross-task transfer. Further analysis reveals that task streaming impacts learning, while consolidating structurally similar trajectories within memory boosts performance.

---


### 86. [Doc2FRC: Length-Consistent Document-Level Machine Translation via Fixed-Range Chunking](https://arxiv.org/abs/2609.12674)

**<font color=#1a73e8>作者：</font>** Xiaotian Wang, Youyuan Lin, Zhan Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Advanced large language models (LLMs) with long context windows can substantially reduce input truncation in document-level machine translation (DocMT). However, direct Doc2Doc translation remains prone to n-gram repetition and progressive quality degradation. A common remedy is to segment the document into finer-grained chunks. Nonetheless, conventional rule-based chunking approaches fail to handle the length distribution mismatch between training and inference. To address this, we introduce Fixed-Range Chunking (FRC), utilizing dynamic programming to partition documents into chunks within a predefined length interval. By consistently applying FRC during training and inference, the input documents of any length are mapped to the same length distribution, substantially reducing train-test length mismatch. Centered on FRC, we propose a lightweight dual-boundary matching algorithm for chunk alignment, alongside four distinct training strategies. Experimental results show that FRC-based fine-tuning substantially improves 7B LLMs over direct Doc2Doc fine-tuning and outperforms existing DocMT methods on IWSLT2017. We further construct GlobVDoc, a 10-language test set independent of mainstream DocMT training sources, and show that FRC improves out-of-distribution document translation.

---


### 87. [Detecting and Explaining Fake News Short Videos with Multimodal Content and Real-World Evidence](https://arxiv.org/abs/2609.12678)

**<font color=#1a73e8>作者：</font>** Yifeng Luo, Yupeng Li, Ming Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Short-video platforms have become a primary news source for the public, which has also enabled the widespread dissemination of fake news videos. We study the task of fake news video detection and explanation (FNVDE). Existing methods face two critical limitations. First, commonly used frame selection strategies may omit veracity-relevant cues or provide insufficient temporal context for understanding news videos. Second, prior methods neglect either multimodal understanding or evidence retrieval. To address these limitations, we propose NVKE-CEI, a unified system that integrates a news video keyframes extraction method (NVKE) and an FNVDE framework leveraging both content and evidence information (CEI). NVKE selects keyframes based on chronological changes in combined visual and OCR-text similarity. CEI employs two specialized LLM-based fact checkers (content-based and evidence-based) whose outputs are fused by a lightweight judge model. Extensive experiments show that NVKE-CEI outperforms state-of-the-art baselines while generating high-quality content-grounded explanations.

---


### 88. [Bridging the First-Hour Gap: Evaluating AI Reliability and Benchmarking Deficiencies in Cyber Incident Response for Law Enforcement](https://arxiv.org/abs/2609.12681)

**<font color=#1a73e8>作者：</font>** Roshin Sleeba C, Hiran V Nath  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The actions of frontline law enforcement officers in the initial hour of a cyber incident play a vital role in determining the ultimate success of an investigation. The minor mistakes they commit might result in irreversible critical impacts. The integrity of the investigation can be compromised, and the prosecution of cyber criminals can be hindered due to minor mistakes that happen in the initial hour. These are mainly because of the volatile nature of digital artifacts that might lead to procedural errors and evidence attrition. This paper provides a systematic survey of decision-support architectures designed to assist first responders of a cybercrime, categorizing them into playbooks, Large Language Models (LLMs), Retrieval-Augmented Generation (RAG) frameworks, and Agentic AI systems. The survey critically considers the constraints of limited technical proficiency and inconsistent forensic infrastructure in a practical scenario. Our analysis identifies RAG-based systems as a relatively viable intermediate solution due to their natural language adaptability. However, significant risk factors like prompt sensitivity and the potential for confident hallucinations in legal contexts pose a major challenge. Furthermore, we review current benchmarks in cybersecurity and demonstrate that they are not sufficient to capture the specific safety and legal requirements of law enforcement, focusing on the initial hour of the cybercrime. We conclude by arguing for the necessity of a new evaluation benchmark focused on naive query robustness and evidence preservation, so as to ensure that AI-driven guidance aligns with the mandatory demands of judicial proceedings.

---


### 89. [Generative AI Use Cases In Real Estate Marketing: Adoption and Constraints in Germany](https://arxiv.org/abs/2609.12684)

**<font color=#1a73e8>作者：</font>** Victor Kolominsky-Rabas, Leopold Müller, Felicia Perpina 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (GenAI) is changing how work is organized and performed. Real estate marketing is a prime example of this, yet evidence of GenAI in real estate agents' day-to-day practice remains scarce. In this work, we report on our insights from a German-based empirical study with eleven semi-structured interviews. GenAI is already utilized across different activities, with marketing communication being the most prominent. Concrete use cases are emergent and unevenly adopted, with writing exposé texts being the only widely established one. Interaction is predominantly human-in-the-loop: GenAI drafts, structures, and retrieves, while real estate agents curate, verify, and decide. Constraints stem less from model capability than from integration with listings and documents, data availability, and compliance in sensitive tasks. The study contributes a grounded map of existing and potential use cases and identifies tentative practical implications for adoption.

---


### 90. [Residual Vector-based Reconstruction as Long-Context Recall Regardless of Context Window Size](https://arxiv.org/abs/2609.12686)

**<font color=#1a73e8>作者：</font>** MyungHoon Ryu, XinYu Piao, Jong-Kook Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) process long contexts, including long documents and lengthy conversations, but face token-level memory usage that increases proportionally to input length. Although model optimization and lossy prompt compression are widely used, these methods still fail to solve the long-context recall problem beyond pretrained and size-constrained context windows. This paper proposes a long-context recall method that maintains near-constant GPU memory usage as context length increases, without additional training. The main idea is to reconstruct facts using parameter activations in the LLM's feed-forward layers, which store residual vectors representing facts from the source document. Utilizing residual vectors allows the LLM to deterministically reconstruct query relevant facts without referencing the original document, preserving high fidelity and reducing memory usage without fine-tuning weights. Experimental results show that the proposed method enables answering single-fact questions in two-million-token story contexts where previous methods fail.

---


### 91. [Semantically Aligned Gradient-Driven Context-Preserving Image Editing](https://arxiv.org/abs/2609.12691)

**<font color=#1a73e8>作者：</font>** Chiranjeev Chiranjeev, Muskan Dosi, Mayank Vatsa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-guided image editing has a training-time blind spot. Generative editors are never required to semantically verify whether their outputs actually satisfy the instruction. Supervision stops at reconstruction and input textual-level conditioning. This produces incomplete edits, spatial spillover, and poor localization. We present IABEdit, a model-agnostic framework that embeds differentiable semantic verification into training. A frozen vision-language model extracts spatially-aware descriptors from the ground-truth edit. A trainable aligner then reproduces them from the generated output. The residual between the two becomes a gradient that teaches the generator both what to edit and where, with no inference-time VLM cost. IABEdit is compatible with diverse backbones, including U-Net (Stable Diffusion) and MMDiT (FLUX), without altering their inference pipelines. On MagicBrush, it improves structural fidelity by +3.49 DINO-I over the best diffusion baseline and +1.26 over the best overall baseline, while remaining competitive on instruction alignment. It also achieves state-of-the-art instruction adherence performance on RealEdit and EMU Edit benchmarks based on embedding-based metrics. Most consequentially, on the D-LORD surveillance benchmark, it surpasses the proprietary Gemini agent by +5.13 DINO-P under heavy occlusion, where preserving identity is hardest. This shows that gradient-aligned VLM distillation holds up under real-world-like surveillance and occlusion conditions. Human and GPT-4o evaluations confirm perceptually precise, well-localized edits.

---


### 92. [I Am AdMan: A Pipeline for Automatic Generation of Personalized Advertising Imagery](https://arxiv.org/abs/2609.12694)

**<font color=#1a73e8>作者：</font>** Victor Kolominsky-Rabas, Leopold Müller, Claudius Budcke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized marketing can increase customer engagement, satisfaction, and conversion. While existing personalization approaches have become effective at matching the right product to the right customer, the visual representation of advertisements remains generic and only weakly tailored to the individual. Prior research shows that generative artificial intelligence can improve the creation of personalized advertisements, particularly for text, and that image generation models can support scalable advertisement production. However, little research has examined how detailed customer information can be systematically translated into fully AI-generated, personalized advertising imagery at scale on a technical level. To address this gap, we propose AdMan, a multi-agent pipeline that transforms customer data into personas, generates personalized advertisement images conditioned on product reference images, and applies an LLM-based judge agent for automated quality control. We implement the pipeline with two different model configurations and evaluate it across four products, using six celebrity personas for qualitative inspection, and 100 real customer profiles, producing 1745 advertisements. The evaluation combines a qualitative expert focus group and a quantitative artifact-rate assessment. The results show that the pipeline can generate photorealistic and personalized advertisements. At the same time, performance varies substantially by product complexity and model configuration. Our findings extend the literature on AI-based personalized advertising by demonstrating the feasibility and current limitations of fully automated image generation for advertising.

---


### 93. [Implicit Personality Representations in Humans and LLMs](https://arxiv.org/abs/2609.12704)

**<font color=#1a73e8>作者：</font>** Yilin Geng, Omri Abend, Eduard Hovy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A century of psychology has found that the trait words people use to describe one another vary, but the relational structure among those traits, which ones go together and which oppose, is strikingly consistent across raters and cultures. We test whether the LLM (Qwen 2.5-7B-Instruct) reproduces this structure in its internal trait representations. From millions of crowd-sourced personality ratings of fictional characters, we build a human implicit-personality matrix over hundreds of traits; from contrastive model activations, we build a matching matrix over the same traits. The two relational structures align strongly (Mantel r = 0.77), and the agreement holds trait by trait as well as in aggregate. Two dominant axes of the model's trait representations recover the social and intellectual dimensions long known to organize human personality impressions, social warmth and intellectual competence. On held-out dialogue, projecting model activations onto these directions yields personality profiles that agree with human ratings. This work establishes a framework that enables comprehensive, human-grounded comparison between internal model trait geometry and the shared structure of human personality impressions.

---


### 94. [ExpertHTR: Unified Handwritten Text Recognition with Multi-Task Learning and Sparse Mixture-of-Experts](https://arxiv.org/abs/2609.12705)

**<font color=#1a73e8>作者：</font>** Dang Hoai Nam, Nguyen Duy Hieu, Quang Huu Hieu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handwritten text recognition resources are often small and distributed across collections that differ in language, script, document structure, and annotation format, making joint page-level training difficult. We propose ExpertHTR, a unified vision-language framework that addresses this problem through complementary supervision and conditional model capacity. Structural annotations from heterogeneous datasets are first organized through a common Page-Region-Line representation and used to construct four related training tasks for complete transcription, physical-line coverage, text localization, and localized recognition, without requiring additional manual labels. Building on a jointly trained dense model, ExpertHTR introduces a sparse Mixture-of-Experts architecture with an always-active shared branch and conditionally routed full-MLP experts. Sparsegen allows the number of active routed experts to vary with the hidden representation, while routing regularization reduces persistent concentration on a small subset of experts. Experiments on seven heterogeneous handwriting benchmarks show that complementary supervision consistently improves training with page transcription alone, while joint multi-source training provides further gains on most datasets. The proposed sparse expert model further improves the dense baseline on six of the seven sources. The final unified model also substantially outperforms the evaluated general-purpose OCR and vision-language systems on most benchmarks and achieves state-of-the-art performance on the IAM paragraph-level benchmark, while specialized HTR systems remain stronger on several challenging collections.

---


### 95. [When Rubrics Fail: Hallucinations Reveal Blind Spots in Medical AI Evaluation](https://arxiv.org/abs/2609.12718)

**<font color=#1a73e8>作者：</font>** Griffin Farrow, Lily Sijia Li, Jack Johnson 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hallucinations can undermine clinician trust in LLMs, making it important that evaluation methods capture clinically relevant errors. Rubric-based evaluation has become the leading approach for assessing LLMs in medicine, but it is unclear whether rubric scores reflect such errors. We first study this in a controlled setting using MedHallu, finding that more specific rubrics better distinguish correct from hallucinated responses. To test this systematically, we develop a taxonomy of medical hallucination types and a clinician-validated error-injection pipeline that creates matched correct and error-injected responses. Across HealthBench, HealthBench Professional, and LiveMedBench, our clinically relevant hallucinations are missed by rubrics, often leaving scores unchanged. We find that rubrics are most effective when explicitly checking facts, and are less effective for additional or unexpected errors they do not anticipate. A preliminary retrieval-based factuality check recovers some of the rubric-blind errors, suggesting a complementary approach. These findings reveal systematic blind spots in current medical evaluation of LLMs and suggest that rubric scores alone are insufficient to establish clinical reliability, potentially undermining clinician trust and confidence in clinical deployment.

---


### 96. [Skill Issue: Lessons from Optimizing Repository SKILLs for Coding Agents](https://arxiv.org/abs/2609.12742)

**<font color=#1a73e8>作者：</font>** Mykhailo Kozyrev, Andrei Kozyrev, Anton Podkopaev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents increasingly read repository knowledge from SKILLs --- plain \texttt{.md} files versioned alongside the code. Recent work synthesizes these files automatically, by optimizing the document against a benchmark. A bare repository comes with no benchmark, and the synthetic tasks prior work builds are small enough that a capable agent saturates them with no document at all. We mine harder tasks --- merged pull requests of the repository, reverted at a single frozen base commit; and score a candidate document by whether the same agent does better with it than without it. On three Kotlin repositories, the documents GEPA finds raise this score by $4.9$pp on average, and the ones SkillOpt finds leave it where it started, $0.1$pp above the seed. The GEPA gain matches what prior work reports with the same optimizer, and at the dataset size a single repository supplies it cannot be separated from the agent's run-to-run variance; settling that would take more tasks than one repository's history yields. The documents themselves read better than the score: a maintainer of one repository found in them knowledge one only gets by working in the project.

---


### 97. [What Drives Recovery in Agentic Text-to-Cypher? LAST-CQ: An LLM Agent Self-Refinement Framework](https://arxiv.org/abs/2609.12746)

**<font color=#1a73e8>作者：</font>** Ioannis Prokopiou, Athanasios Aidinis, Panagiotis-Christos Kyrmpatsos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic pipelines for structured-query generation are rapidly expanding, but it is unclear which part of the loop produces the gain. We use LAST-CQ -- a five-agent, training-free, execution-grounded Text-to-Cypher framework -- as an instrumented testbed, running three counterfactuals over 2,471 live-database queries and six backbones spanning three vendor scale tiers. Removing correction is worth between 3.1% aggregate execution-BLEU against the single-pass system and 12.3% against a no-refinement counterfactual (up to 80.7% for the weakest backbone). Replacing schema-grounded, LLM-synthesised feedback with raw database error strings costs almost nothing (20.9% vs. 19.9% naive exact match; <0.2% end-to-end; equivalent within $\pm 0.075$ set-F1 by two one-sided tests). Spending the same call budget on parallel sampling degrades quality by 10-11%. What works is detecting failure and routing it to a retry, not the feedback sophistication or number of samples. LAST-CQ itself recovers 91.7% of queries that fail under single-pass generation, while a query that succeeds first time still costs exactly one LLM call. We also show that n-gram overlap on serialised results is not a bound in either direction: it over-scores against set equivalence on 65.9% of results while under-scoring against judged semantics. Finally, we calibrate our LLM judge against blind human labels and find it optimistic by 9 points.

---


### 98. [Assisted Spatial Cognition Through Vision-Language Models](https://arxiv.org/abs/2609.12747)

**<font color=#1a73e8>作者：</font>** H. Riaz, J. B. Fernandez, I. Mills 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal AI, powered by Large Language Models (LLMs) and Vision-Language Models (VLMs), is transforming assistive technologies by enabling simultaneous processing of visual and textual data. This advancement holds significant promise for over 43 million visually impaired and neuro-divergent individuals worldwide who face persistent challenges in navigating indoor and outdoor environments due to limited spatial awareness and insufficient environmental cues. Existing navigation aids often lack comprehensive 3D scene understanding, relying on constrained route-based strategies that hinder user autonomy. In this paper, we introduce a novel end-to-end framework that integrates LLMs, VLMs and digital twin technologies to deliver a spatially cognitive navigation support for visually impaired and neuro-divergent users. Our system captures video input via standard mobile phone cameras, and employs SLAM3R to generate dense 3D point clouds from monocular RGB sequences in real-time. Our custom post-processing algorithm ensures accurate point cloud alignment across multiple viewpoints without requiring predefined reference points. This enhances the capabilities of SpatialLM to produce structured 3D representations, including architectural elements and oriented object bounding boxes. The enriched spatial data is then processed by a locally deployed LLM, which interprets 3D contexts to generate detailed scene descriptions and precise distance measurements between users and surrounding objects. We evaluated our approach across diverse video scenarios featuring various perspectives, looped walking views and captured in multiple environments. The evaluation results demonstrate consistent accuracy in 3D scene interpretation and object localisation, underscoring the potential of our system as a transformative assistive navigation solution that combines advanced visual perception with spatial reasoning

---


### 99. [The Mechanics of a Swarm: A Reproducible External Reconstruction of an Unintended Agent-Coordination Episode on a Third-Party Wiki](https://arxiv.org/abs/2609.12748)

**<font color=#1a73e8>作者：</font>** Philipp Lütje  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Between 24 May and 2 July 2026, autonomous language-model agents running inside a timed research-question evaluation wrote to a third party's public, world-writable wiki. OpenAI acknowledged the incident; independent researchers reconstructed it and published the wiki's archived revision history. We analyse that history (14,591 revisions, 3,103 names, 4,579 pages, 19,913 server events) as a behavioural record, attributing text to the revision that added it rather than to cumulative page content. Under an explicit identity model we reconstruct 907 cohorts and, from a random calendar marker the environment attached to each episode, estimate about 876 episodes (95% interval 774-995; alternative reconstructions span 800-1400). Coordination formats converged within a day, and the schedules created large opportunities for information asymmetry: because episodes of the same question chain ran at different internal-clock rates and started up to 16 h apart, the first report of an item preceded a later cohort's arrival by a median of 3.4 h. The three schedule parameters agents reported share one latent speed scale (78% of log-variance over 15 configurations), and in one task family the last observed activity clusters by reported speed class on the internal clock, compatible with a fixed internal-time horizon. Across the 510 cohorts with an observable, format-dependent progress trace, we find no robust positive association between measured coordination and documented progress, including the few demonstrably given a future answer. Because the export contains neither successful-read logs, harness messages nor ground-truth outcomes, these results do not identify the causal origin of the coordination or its effect. We report four claims from our earlier analysis that did not survive re-examination, and argue that read and outcome logging are requirements for agent-evaluation environments.

---


### 100. [Cognition on Graph: Navigating Massive Knowledge Space via Cognitive Cycles and Bidirectional Graph-Text Synergy](https://arxiv.org/abs/2609.12791)

**<font color=#1a73e8>作者：</font>** Gengxian Zhou, Jian Xu, Zichen Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has empowered Large Language Models (LLMs) to tackle knowledge-intensive tasks. However, navigating global, heterogeneous knowledge bases (large-scale knowledge graphs and text corpora) for complex reasoning remains a challenge. Existing methods typically employ reactive, graph-driven exploration strategies, which blindly follow graph topology without adapting to the question context or evolving exploration progress, and lack deep bidirectional synergy between graph and text. To address these limitations, we propose CoG (Cognition on Graph), a cognitive-inspired, training-free framework for adaptive knowledge exploration. Drawing inspiration from human problem-solving, CoG performs a continuous plan-explore-reflect cycle, where it proactively formulates investigation plans, performs dual-source retrieval, and dynamically reflects on progress to adjust strategies. Crucially, it establishes deep bidirectional synergy between structured graph and unstructured text, where entities extracted from text dynamically guide graph exploration to bridge knowledge gaps. Extensive experiments on seven multi-hop QA benchmarks demonstrate that CoG significantly outperforms state-of-the-art methods while achieving superior exploration efficiency. Our code and datasets are available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-134](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
