# 🧠 大模型相关研究 | 2026年05月19日

> 本类共 **127** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-127](./part-03.md)

---

### 51. [TopoClaw: A Human-Centric and Topology-Aware Agent Operating System](https://arxiv.org/abs/2605.15556)

**<font color=#1a73e8>作者：</font>** Heyuan Huang, Yeyi Guan, Jihong Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have evolved AI assistants into autonomous reasoning engines that maintain context, invoke tools, and pursue long-horizon tasks. This has spurred Agent Operating Systems (Agent OS) as kernel-like layers for lifecycle management, memory, scheduling, and access control. Yet most designs remain agent-centric, treating the OS as a single-host runtime for internal reasoning and tool use, leaving open how autonomous actions integrate with distributed, collaborative, permission-sensitive workflows.
TopoClaw is an open-source, human-centric, topology-aware Agent OS modeling the user's ecosystem as two coupled structures: a physical device topology of heterogeneous surfaces and a social relationship topology of shared spaces, teams, and delegated roles. It unifies device operation, messaging, and skills around accountable cross-boundary execution, with three core contributions: (1) cross-device action placement, decoupling intent from actuation and routing distributed actions across the device cluster based on hardware affordances and user context; (2) cross-user identity attribution, treating agents as socially situated "Digital Twins" that coordinate in multi-user spaces while preserving provenance, role-aware permissions, and human accountability; (3) cross-context authority governance, pairing broad capability with distributed, context-aware policy enforcement across physical and social trust boundaries to bound proactive autonomy at the OS layer.
This report presents TopoClaw as an engineering-oriented reference architecture, covering its design principles, runtime, cross-device execution, collaboration mechanisms, security model, and deployment outlook.

---


### 52. [GiLT: Augmenting Transformer Language Models with Dependency Graphs](https://arxiv.org/abs/2605.15562)

**<font color=#1a73e8>作者：</font>** Tianyu Huang, Yida Zhao, Chuyan Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Augmenting Transformers with linguistic structures effectively enhances the syntactic generalization performance of language models. Previous work in this direction focuses on syntactic tree structures of languages, in particular constituency tree structures. We propose Graph-Infused Layers Transformer Language Model (GiLT) which leverages dependency graphs for augmenting Transformer language models. Unlike most previous work, GiLT does not insert extra structural tokens in language modeling; instead, it injects structural information into language modeling by modulating attention weights in the Transformer with features extracted from the dependency graph that is incrementally constructed along with token prediction. In our experiments, GiLT with semantic dependency graphs achieves better syntactic generalization while maintaining competitive perplexity in comparison with Transformer language model baselines. In addition, GiLT can be finetuned from a pretrained language model to achieve improved downstream task performance. Our code is released at this https URL.

---


### 53. [AstraFlow: Dataflow-Oriented Reinforcement Learning for Agentic LLMs](https://arxiv.org/abs/2605.15565)

**<font color=#1a73e8>作者：</font>** Haizhong Zheng, Yizhuo Di, Jiahui Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is increasingly used to improve the reasoning, coding, and tool-use capabilities of large language models, but agentic RL remains prohibitively expensive. Scaling RL to agentic LLMs requires supporting complex workloads, including multi-policy collaborative training, while efficiently using elastic, heterogeneous, and cross-region compute resources. Existing LLM RL systems support some of these capabilities, but each new extension often requires dedicated system engineering. This burden arises from trainer-centered control architectures and the lack of principled abstractions for RL system components. To address these limitations, we propose AstraFlow, a dataflow-oriented RL system that replaces conventional trainer-centered control with principled component abstractions. In AstraFlow, rollout services, dataflow management, and training are decoupled into autonomous components, enabling the system to natively support complex multi-policy agentic RL workloads and efficiently exploit diverse compute resources. We evaluate AstraFlow across math, code, search, and AgentBench workloads, showing that the same system supports multi-policy training, elastic scaling, heterogeneous cross-region execution, and composable data algorithms without system-level code changes. In multi-policy collaborative training, AstraFlow achieves comparable or better accuracy than existing RL systems while speeding up training time by 2.7x.

---


### 54. [Measuring Maximum Activations in Open Large Language Models](https://arxiv.org/abs/2605.15572)

**<font color=#1a73e8>作者：</font>** Luxuan Chen, Han Tian, Xinran Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The dynamic range of activations is a first-order constraint for low-bit quantization, activation scaling, and stable LLM inference. Prior work characterized outlier features and massive activations on pre-2024 LLaMA-style models, and the downstream activation-quantization stack inherits that picture without revisiting it for the post-LLaMA open-model boom. We ask the deployment-oriented question: how large can activations get in modern open LLMs, and how does this magnitude vary across families, generations, and training stages? Under a unified pipeline (5,000-sample multi-domain corpus, family-specific tokenization, identical hooks across embeddings, hidden states, attention, MLP/MoE, SwiGLU gates, and final norm), we measure global and layerwise maxima on 27 checkpoints from 8 open families spanning dense, MoE, vision-language, intermediate-training, and instruction-tuned variants. We find that (i) global maxima span over nearly four orders of magnitude at comparable parameter counts, with Qwen3.5 and MoE checkpoints in the 10^2 to 10^3 range and Gemma3-27B-it reaching ~7 x 10^5; (ii) cross-family and cross-generation comparisons break simple monotonic scaling; and (iii) MoE checkpoints exhibit 14.0-23.4x lower peaks than matched-scale dense counterparts, while the residual stream carries the global maximum in 22/24 checkpoints. A lightweight INT-8 sanity check shows that measured maxima co-vary with low-bit reconstruction error via activation-scale selection. We conclude that maximum activation magnitude is a model property tied to family, architecture, and training stage - not a simple byproduct of size - and should be measured and reported alongside any open-weight release before low-bit deployment. The code is publicly available at this https URL.

---


### 55. [STAR: A Stage-attributed Triage and Repair framework for RCA Agents in Microservices](https://arxiv.org/abs/2605.15581)

**<font color=#1a73e8>作者：</font>** Junle Wang, Xingchuang Liao, Wenjun Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based root cause analysis (RCA) agents have recently emerged as a promising paradigm for incident diagnosis in microservice AIOps. However, their reliability remains fragile: an error in early evidence collection, hypothesis formulation, or causal analysis can propagate through the reasoning trace and eventually corrupt the final diagnosis. In this paper, we present \textbf{STAR}, a \emph{Stage-attributed Triage and Repair} framework for repairing erroneous RCA traces. STAR explicitly decomposes an RCA workflow into four structured stages, namely \emph{Evidence Package} (EP), \emph{Hypothesis Set} (HS), \emph{Analysis Structure} (AS), and \emph{Decision Report} (DR), and treats agent failure as a stage-localizable reasoning bug rather than a monolithic end-to-end error. Built on top of LangGraph, STAR performs stage-wise auditing, budget-aware \emph{Fast/Slow Routing}, \emph{decisive stage localization via counterfactual candidate evaluation}, and stage-specific patch-and-replay repair.
We evaluate STAR on a public large-scale benchmark and a real-world production dataset, using two RCA agent workflows and three foundation models. Experimental results show that STAR consistently improves both root cause localization and fault type classification over strong baselines. Moreover, STAR identifies the decisive faulty stage with high accuracy, repairs most initially incorrect traces within one or two replay rounds, and benefits substantially from both Fast/Slow Routing and counterfactual stage evaluation. These results suggest that explicitly modeling \emph{where} an RCA agent fails is an effective path toward reliable, debuggable, and self-repairing agentic RCA systems.

---


### 56. [AGC: Adaptive Geodesic Correction for Adversarial Robustness on Vision-Language Models](https://arxiv.org/abs/2605.15584)

**<font color=#1a73e8>作者：</font>** Zhiwei Li, Jiacheng Xue, Weining Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models like CLIP have demonstrated remarkable zero-shot transfer capabilities. However, their susceptibility to imperceptible adversarial perturbations remains a critical security concern. While test-time defenses offer a pragmatic solution for deployed models, existing approaches typically rely on gradient-based optimization during inference, incurring significant computational overhead. In this paper, we revisit the role of data augmentation in CLIP robustness and observe that augmentations are not equally effective: specific augmentations consistently provide robust geometric cues that align with correct class semantics in the hyperspherical feature space. Based on this, we propose Adaptive Geodesic Correction (AGC), a training-free defense mechanism that requires no parameter updates. AGC identifies a reliable augmentation as a geometric anchor and corrects the input feature towards it, utilizing an adaptive step size to balance robustness against clean accuracy preservation. AGC achieves superior performance across eight fine-grained datasets and three CLIP backbones, improving average robust accuracy by 44.4\% over state-of-the-art baseline while delivering a 10$\times$ reduction in inference latency. Our findings reveal a fundamental geometric property of CLIP features, offering a highly efficient and effective paradigm for robust multimodal deployment.

---


### 57. [Calibrating LLMs with Semantic-level Reward](https://arxiv.org/abs/2605.15588)

**<font color=#1a73e8>作者：</font>** Fengfei Yu, Ruijia Niu, Dongxia Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are deployed in consequential settings such as medical question answering and legal reasoning, the ability to estimate when their outputs are likely to be correct is essential for safe and reliable use, requiring well-calibrated uncertainty. Standard reinforcement learning with verifiable rewards (RLVR) trains models with a binary correctness reward that is indifferent to confidence, providing no penalty for confident but wrong predictions and thereby degrading calibration. Recent work addresses this by training models to produce verbalized confidence scores alongside answers and rewarding agreement with correctness. However, verbalized confidence is calibrated at the token level and thus exhibits inconsistency across textual variations with same semantic meaning. We propose \textbf{Calibration with Semantic Reward (CSR)}, a framework that calibrates language models directly in semantic space without a verbalized confidence interface. CSR combines the correctness reward with a novel semantic calibration reward that encourages exploitation among correct rollouts by promoting semantic agreement, and exploration among incorrect ones by discouraging spurious consistency. Experiments across three model families on HotpotQA (in-distribution) and TriviaQA, MSMARCO, and NQ-Open (out-of-distribution) show that CSR consistently achieves lower ECE and higher AUROC than verbalized-confidence baselines across nearly all settings, reducing ECE by up to $40\%$ and improving AUROC by up to $31\%$ over verbalized-confidence baselines, with calibration behavior generalizing robustly across all four evaluation settings.

---


### 58. [MHGraphBench: Knowledge Graph-Grounded Benchmarking of Mental Health Knowledge in Large Language Models](https://arxiv.org/abs/2605.15589)

**<font color=#1a73e8>作者：</font>** Weixin Liu, Congning Ni, Shelagh A. Mulvaney 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in the mental health domain, yet it remains unclear how well they capture related biomedical knowledge and how reliably they apply it to clinically salient structured judgments. Here, we present a knowledge-graph (KG)-grounded benchmark for assessing LLMs on mental-health entity recognition, relation judgment, and two-hop reasoning. The benchmark is derived from PrimeKG and comprises nine task families with KG-supported answers and controlled negative options. Experiments across 15 closed- and open-source LLMs reveal a persistent recognition-to-judgment gap: leading models achieve near-ceiling performance on entity typing and on the small relation-typing subset, yet they still struggle with relation prediction and two-hop reasoning. Additionally, short KG-derived snippets benefit some models but degrade performance for others. Moreover, output-format reliability can substantially influence measured performance under constrained multiple-choice settings, highlighting the critical role of response validity in benchmark-based evaluation. MHGraphBench should therefore be interpreted as evaluating agreement with a curated mental-health slice of PrimeKG under a constrained multiple-choice interface, rather than as a direct assessment of real-world clinical safety.

---


### 59. [CM-EVS: Sparse Panoramic RGB-D-Pose Data for Complete Scene Coverage](https://arxiv.org/abs/2605.15597)

**<font color=#1a73e8>作者：</font>** Jiale Liu, Jungang Li, Jieming Yu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern 3D visual learning relies on observations sampled from metric 3D assets, yet existing scans, meshes, point clouds, simulations, and reconstructions do not directly provide a sparse, comparable, and geometry-consistent panoramic training interface. Dense trajectories duplicate nearby views, source-specific rendering policies yield heterogeneous annotations, and sparse heuristics may miss important regions or introduce depth-inconsistent observations. We study how to convert 3D assets into sparse panoramic RGB-D-pose data that preserves complete scene coverage with low redundancy and auditable provenance. We propose COVER (Coverage-Oriented Viewpoint curation with ERP Range-depth warping), a training-free ERP viewpoint curator that projects geometry observed from selected views into candidate ERP probes, scores incremental coverage, and penalizes depth conflicts. Under bounded proxy error, its greedy coverage proxy preserves the standard coverage-style approximation behavior up to an additive error term. Using COVER, we build CM-EVS (Coverage-curated Metric ERP View Set), a panoramic RGB-D-pose dataset with 36,373 curated ERP frames from 1,275 indoor scenes across Blender indoor, HM3D, and ScanNet++, complemented by outdoor panoramas from TartanGround and OB3D re-encoded into the same schema. Each frame provides full-sphere RGB, metric range depth, calibrated pose; COVER-produced indoor frames include per-step provenance logs. With a median of only 25 frames per indoor scene, CM-EVS covers all 13 unified room types while maintaining compact scene-level coverage. Experiments show that COVER improves the coverage-conflict trade-off, making CM-EVS a sparse, compact, and auditable RGB-D-pose resource for geometry-consistent panoramic 3D learning.

---


### 60. [Syntax Without Semantics: Teaching Large Language Models to Code in an Unseen Language](https://arxiv.org/abs/2605.15607)

**<font color=#1a73e8>作者：</font>** Vinayshekhar Bannihatti Kumar, Disha Makhija, Manoj Ghuhan Arivazhagan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve high pass rates on code generation benchmarks, yet whether they can transfer this ability to languages absent from pretraining remains poorly understood. We introduce PyLang, a minimal imperative language absent from all pretraining corpora, and evaluate frontier models zero-shot and fine-tuned Qwen3 (4B, 8B, 32B) on 352 problems. We find that fine-tuning quickly teaches syntax but fails to transfer semantic competence: Python outperforms PyLang by up to 19% across all configurations, and no intervention (multi-task learning, preference tuning, code infilling, or latent-space objectives) closes the gap. An LLM judge reveals that frontier models select an identical algorithm to Python 80% of the time, yet cannot translate it into a working PyLang implementation., and CKA analysis confirms that fine-tuned models converge to nearly identical internal representations across languages (CKA > 0.97) while diverging at the output stage. We term this the implementation fidelity gap: models possess language-agnostic algorithmic understanding but cannot express it in an unfamiliar language. Our findings highlight the need for training methods that decouple reasoning from language-specific realization.

---


### 61. [PSD: Pushing the Pareto Frontier of Diffusion LLMs via Parallel Speculative Decoding](https://arxiv.org/abs/2605.15609)

**<font color=#1a73e8>作者：</font>** Shengyin Sun, Yiming Li, Renxi Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) generate text by iteratively denoising masked token sequences. Although dLLMs can predict all masked positions in parallel within each step, the large number of denoising iterations still makes inference expensive. This cost can be reduced spatially by unmasking multiple tokens per step, or temporally by collapsing multiple denoising steps into one verification call. We propose Parallel Speculative Decoding (PSD), a training-free framework that jointly improves inference along both axes. Using the confidence scores from a single forward pass, PSD selects positions to unmask via a configurable, adaptive unmasking policy and constructs multi-depth speculative drafts without extra model calls. A final batched verification pass then applies hierarchical acceptance, keeping the deepest draft that remains consistent with the updated predictions. Experiments on three dLLMs across reasoning and code generation tasks show that PSD achieves favorable trade-offs between inference efficiency and generation quality, reaching up to $5.5\times$ tokens per forward pass with accuracy comparable to greedy decoding.

---


### 62. [Toward LLMs Beyond English-Centric Development](https://arxiv.org/abs/2605.15613)

**<font color=#1a73e8>作者：</font>** Sho Takase, Ukyo Honda  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Through an analysis of sequences generated by open-weight large language models (LLMs), we demonstrate that LLMs are heavily biased toward English. While continual pre-training is commonly used to adapt LLMs to a target language, we show that it does not offer a cost advantage over training from scratch, even for improving cultural understanding in the target language. These findings suggest that dedicated per-language investment may become increasingly important for future LLM development, rather than relying primarily on the expansion of English-centric resources.

---


### 63. [Neutral-Reference Prompting for Vision-Language Models](https://arxiv.org/abs/2605.15615)

**<font color=#1a73e8>作者：</font>** Senmao Tian, Xiang Wei, Shunli Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient transfer learning of vision-language models (VLMs) commonly suffers from a Base-New Trade-off (BNT): improving performance on unseen (new) classes often degrades accuracy on known (base) classes. Addressing how to boost recognition of unseen classes without sacrificing known-class performance remains a central challenge. Existing work often simplistically attributes the BNT to overfitting on known classes. We observe an interesting phenomenon: VLMs frequently exhibit asymmetric confusion on certain downstream data, i.e., samples of class A are systematically mispredicted as class B, while the reverse confusion (B to A) rarely occurs. For known classes, this kind of bias can be mitigated by tuning using a cross-entropy loss, but for unseen classes, such pretraining-induced bias persists and harms generalization. Motivated by this, we propose NeRP, a plug-and-play prompting correction strategy that improves discrimination on unseen classes without modifying model parameters. NeRP leverages neutral text prompts and reference images to measure class-wise prior preferences along the pre-trained inter-class geometry, and combines them with the sample likelihood to obtain the model's surrogate score. If, for a given sample, the prior strongly favors the current prediction while the observed evidence is clearly insufficient, we perform a local flip between easily confusable class pairs, thereby correcting prior-dominated mispredictions. Extensive experiments across multiple backbones and 15 few-shot and cross-domain benchmarks show that NeRP substantially improves accuracy on unseen classes while preserving known-class prediction performance.

---


### 64. [Latent Video Prediction Learns Better World Models](https://arxiv.org/abs/2605.15618)

**<font color=#1a73e8>作者：</font>** Ali J Alrasheed, Aryan Yazdan Parast, Basim Azam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised video models are increasingly framed as world models, yet their evaluation remains largely confined to a single top-1 accuracy score on clean benchmarks. This leaves a major gap in comprehending their potential as world models. We present the first systematic study addressing this gap, analyzing four matched-capacity frontier video foundation models, V-JEPA 2.1, V-JEPA 2, VideoPrism, and VideoMAEv2, across five robustness axes relevant to their deployment as video world models: feature discriminability, corruption robustness, fine-grained discrimination, occlusion robustness, and sensitivity to temporal direction. Our evaluations establish that across all five axes, latent-prediction models form a distinct and consistent profile. They degrade more gracefully under pixel corruption, preserve usable class structure rather than mere geometric stability under occlusion, capture fine-grained physical contact cues without reconstructing pixels, and uniquely encode the arrow of time. These advantages can even survive task adaptation: a frozen V-JEPA 2 backbone with a lightweight attentive probe outperforms a fully fine-tuned VideoMAE and a supervised TimeSformer on corruption and occlusion robustness. Our extensive results offer concrete new evidence in favor of latent prediction for robust world modeling.

---


### 65. [LRCP: Low-Rank Compressibility Guided Visual Token Pruning for Efficient LVLMs](https://arxiv.org/abs/2605.15621)

**<font color=#1a73e8>作者：</font>** Hongyu Lu, Feng Zhang, Wenwei Jin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) achieve strong multimodal understanding, but their inference cost grows rapidly with the number of visual tokens, especially for high-resolution images and long videos. Existing attention-based methods estimate token importance from attention scores, which may introduce positional bias, while representation-based methods reduce visual redundancy based on feature relations or reconstruction errors, overlooking the global structure of the visual token set. In this paper, we revisit visual token compression from the perspective of low-rank compressibility. Across models and datasets, we observe that visual token representations exhibit a pronounced low-rank structure, with a dominant subspace that remains stable even after a large fraction of tokens is randomly removed. Motivated by this finding, we propose LRCP, a training-free compression framework that first estimates the dominant low-rank subspace of visual tokens via PCA, and then scores each token by its projection residual onto this subspace, retaining tokens that are poorly explained by the low-rank background. Extensive experiments show that LRCP achieves superior results, preserving 94.7% of the original image-understanding performance with an 88.9% token reduction and 97.8% of the average video-understanding accuracy with an 87.5% token reduction.

---


### 66. [IO-SVD: Input-Output Whitened SVD for Adaptive-Rank LLM Compression](https://arxiv.org/abs/2605.15626)

**<font color=#1a73e8>作者：</font>** Ali Abbasi, Chayne Thrash, Haoran Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models deliver strong performance across language and reasoning tasks, but their storage and compute costs remain major barriers to deployment in resource-constrained and latency-sensitive settings. SVD-based post-training compression offers a hardware-agnostic way to reduce model size and improve inference efficiency through low-rank factorization. However, existing methods often rely on input-only whitening spaces, homogeneous rank allocation, or loss-agnostic allocation heuristics, limiting their ability to preserve model quality under aggressive compression. We propose Input-Output Whitened SVD (IO-SVD), a post-training compression method that forms a KL-aware double-sided whitening space for model weights. Using a second-order expansion of the KL loss over the top-K token probabilities, IO-SVD constructs an output-side metric that captures predictive sensitivity, while input whitening captures activation statistics. We further introduce an efficient heterogeneous rank-allocation strategy that scores whitened singular components using first-order calibration loss estimates and prunes the least sensitive components under a global budget. Inspired by prior work that combines SVD truncation with quantization, we improve hybrid SVD-quantization compression through loss-aware remapping, which selects low-rank factor rows for 8-bit quantization based on the predicted loss change incurred by quantizing them. Extensive experiments across diverse LLM and VLM families, and inference-time analysis shows that IO-SVD compresses LLMs with minimal performance degradation while delivering practical inference speedups. Code is available at this https URL

---


### 67. [Evaluating Chinese Ambiguity Understanding in Large Language Models](https://arxiv.org/abs/2605.15635)

**<font color=#1a73e8>作者：</font>** Junwen Mo, Yuanzhi Lu, Yifang Xue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linguistic ambiguity is critical to the robustness of Large Language Models (LLMs), yet existing research focuses mostly on English, with limited attention devoted to Chinese. Existing Chinese ambiguity datasets (e.g., CHAmbi) suffer from poor scalability. Guided by Potential Ambiguity (PA) Theory, we design a semi-automatic pipeline to construct CHA-Gen. It is the first PA Theory-grounded Chinese ambiguity dataset, which comprises 5,712 sentences (2,414 ambiguous, 3,298 unambiguous) across 18 potential ambiguous structures. Evaluating LLMs (e.g. Gemma 3, Qwen 2.5/3 series) via direct querying and machine translation, we find that LLMs struggle with ambiguity detection (improved by CoT prompting). Analysis of Qwen3-32B's CoT rationales reveals three common failure modes: ambiguity blindness, misattribution, and premature resolution. Uncertainty quantification with semantic entropy metric shows higher uncertainty for ambiguous sentences. Moreover, instruction tuning induces overconfidence, whereas Base models better capture semantic diversity. We further observe that models exhibit a bias toward dominant interpretations. Our work provides a scalable approach for Chinese ambiguity corpus and insights into LLMs' ambiguity handling, laying a foundation for enhancing Chinese ambiguity research in LLMs.

---


### 68. [Rule2DRC: Benchmarking LLM Agents for DRC Script Synthesis with Execution-Guided Test Generation](https://arxiv.org/abs/2605.15669)

**<font color=#1a73e8>作者：</font>** Jinuk Kim, Junsoo Byun, Donghwi Hwang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Manufacturable chip layouts must satisfy thousands of geometry-based design rules, and design rule checking (DRC) enforces them by running executable DRC scripts on layouts. Translating natural language rules into correct DRC scripts is labor-intensive and requires specialized expertise, motivating LLM agents for DRC script synthesis and debugging. However, existing benchmarks have small evaluation sets and often evaluate scripts by code similarity rather than execution correctness, and prior machine learning-based methods either ignore execution feedback or require labeled test layouts as agent's input. To this end, we introduce Rule2DRC, a large-scale benchmark for DRC script coding agents with 1,000 rule-to-script tasks and 13,921 evaluation chip layouts for execution-based scoring. Rule2DRC provides an evaluation pipeline that measures functional correctness via DRC execution outcomes without requiring evaluation layouts as input to the agent. We also propose SplitTester, a tester agent for program selection that uses execution feedback to generate discriminative test cases and separate previously indistinguishable candidate scripts, substantially improving Best-of-N selection performance in this domain. We release the code at this https URL.

---


### 69. [Dynamic Chunking for Diffusion Language Models](https://arxiv.org/abs/2605.15676)

**<font color=#1a73e8>作者：</font>** Yichen Zhu, Xiaoming Shi, Peng Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block discrete diffusion language models factorize a sequence autoregressively over fixed-size positional blocks, decoupling within-block parallel denoising from across-block conditioning. We argue that this rigid partition wastes structure already present in the sequence: blocks defined by position rather than by content separate semantically coherent tokens and group unrelated ones together. We introduce the \textbf{D}ynamic \textbf{C}hunking \textbf{D}iffusion \textbf{M}odel (DCDM), which replaces positional blocks with content-defined semantic chunks. At its core is Chunking Attention, a differentiable layer that routes tokens into $K$ clusters parameterized by learnable subspaces and shaped end-to-end by the diffusion objective. The resulting cluster assignments induce a chunk-causal attention mask under which a discrete diffusion denoiser factorizes the sequence likelihood autoregressively over semantic chunks, strictly generalizing block discrete diffusion. On downstream benchmarks at parameter scales up to 1.5B, DCDM consistently improves over both unstructured and positional-block diffusion baselines, with the advantage stable across scales and visible early in training.

---


### 70. [Few-Shot Large Language Models for Actionable Triage Categorization of Online Patient Inquiries](https://arxiv.org/abs/2605.15680)

**<font color=#1a73e8>作者：</font>** Liqi Zhou, Jiafu Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online patient inquiries are often informal, incomplete, and written before professional assessment, yet they must still be routed to an appropriate level of clinical follow-up. We study this as a four-class actionable triage task -- self-care, schedule-visit, urgent-clinician-review, or emergency-referral, and ask whether prompted large language models (LLMs) can support such routing under low-resource labeling conditions. Using the public HealthCareMagic-100K corpus, we construct a 300-example human calibrated gold evaluation set, a 700-example auto-labeled silver training set, and a 40-example few-shot pool. We compare Term Frequency-Inverse Document Frequency (TF-IDF) and Bidirectional Encoder Representations from Transformers for Biomedical Text Mining (BioBERT) baselines train on silver labels against six prompted LLMs under 0-shot, 4-shot, and 12-shot conditions respectively. Accordingly, we evaluate with macro-$F_1$ alongside safety-aware metrics, including emergency-recall, under-triage rate, and severe under-triage rate. The strongest LLM (Claude Haiku 4.5, 12-shot) reaches macro-$F_1$ 0.475, exceeding the best supervised baseline (BioBERT, 0.378) on point estimate, with overlapping confidence intervals. Few-shot prompting and two-model agreement help in label-dependent ways: self-care agreement is reliable, urgent-clinician-review is not. We conclude that LLMs can support triage prioritization and selective human review, but not autonomous deployment.

---


### 71. [ASRU: Activation Steering Meets Reinforcement Unlearning for Multimodal Large Language Models](https://arxiv.org/abs/2605.15687)

**<font color=#1a73e8>作者：</font>** Jiahui Guang, Yingjie Zhu, Cuiyun Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) may memorize sensitive cross-modal information during pretraining, making machine unlearning (MU) crucial. Existing methods typically evaluate unlearning effectiveness based on output deviations, while overlooking the generation quality after unlearning. This can easily lead to hallucinated or rigid responses, thereby affecting the usability and safety of the unlearned model. To address this issue, we propose ASRU, a controllable multimodal unlearning framework that incorporates generation quality as a core evaluation objective. ASRU first induces initial refusal behavior through activation redirection, and then optimizes fine-grained refusal boundaries using a customized reward function, thereby achieving a better trade-off between target knowledge unlearning and model utility. Experiments on Qwen3-VL show that ASRU significantly improves unlearning effectiveness (+24.6%) on average and generation quality (5.8x) on average while effectively preserving model utility, using only a small amount of retained supervision data.

---


### 72. [Handwriting decoding as a challenging motor task for EEG Foundation Models](https://arxiv.org/abs/2605.15698)

**<font color=#1a73e8>作者：</font>** Srinivas Ravishankar, Ishayu Ghosh, Nora Zajzon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent attempts at creating Foundation Models (FMs) for Electroencephalography (EEG) have achieved state-of-the-art performance on multiple tasks including Motor Imagery (MI). These MI tasks have typically involved coarse classification between imagined limb movements. However, the development of foundation models necessitates diverse datasets, both for pretraining and evaluating the progress of these models. In this work, we propose handwriting decoding as a challenging motor task for FMs. We show that several existing datasets are potentially confounded, and introduce a dataset that more rigorously evaluates models. On this dataset, we find that current FMs, despite showing SOTA performance in multiple MI datasets are outperformed by smaller task-specific models. We also highlight challenges specific to EEG-based handwriting decoding to inform future work. In our 4-letter classification task, we show that (a) Knowledge of movement-onset is crucial to reported decoding performance in prior works, with average performance across subjects dropping from $41.3\%$ to $32.4\%$. (b) Increasing test-time signal quality provides significant performance improvements ($45\%$ to $78\%$ in our best subject) compared to scaling training data with single-trial EEG. (c) While scaling training data steadily improves decoding performance, existing FMs do not outperform specialist models in handwriting decoding. We make our code available at this https URL

---


### 73. [Differentiable Mixture-of-Agents Incentivizes Swarm Intelligence of Large Language Models](https://arxiv.org/abs/2605.15706)

**<font color=#1a73e8>作者：</font>** Xingjian Wu, Junkai Lu, Siyu Yan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) have catalyzed the development of multi-agent systems (MAS) for complex reasoning tasks. However, existing MAS typically rely on pre-defined or pre-compiled communication topologies, which limits their flexibility and adaptability to dynamic task requirements. In this work, we propose Differentiable Mixture-of-Agents (DMoA), a self-evolving multi-agent framework that enables elastic and adaptive agent collaboration during inference. Instead of statically constructing workflows, DMoA dynamically routes and activates agents at each reasoning step, allowing the system to implicitly simulate diverse communication topologies and adapt to evolving demands. To achieve this, we design a differentiable, context-aware routing mechanism that leverages recurrent structures to incorporate historical and contextual information, producing sparse agent activations in a step-wise manner. Furthermore, we introduce predictive entropy as self-supervised signals to optimize the routing process, enabling efficient test-time adaptation without external annotations. Extensive experiments across 9 benchmarks demonstrate that DMoA achieves state-of-the-art performance while exhibiting strong efficiency, robustness, and ensembling capabilities.

---


### 74. [SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory](https://arxiv.org/abs/2605.15710)

**<font color=#1a73e8>作者：</font>** Huacan Chai, Yukai Wang, Yingxuan Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks for multimodal memory reasoning largely evaluate systems within pre-assembled contexts, but under-evaluate whether agents can use evidence distributed across independently originated sources. We argue that source-distributed memory composition is an important and under-examined bottleneck in multimodal agent memory, especially when relevant evidence is fragmented across heterogeneous artifacts such as conversations, profiles, screenshots, tables, images, and documents. To address this gap, we introduce Source-distributed Multimodal Memory Benchmark(SMMBench), which measures whether agents can retrieve, align, and compose multimodal evidence scattered across multiple sources rather than reason within a single curated context. SMMBench evaluates four core capabilities: (1) cross-source multimodal reasoning; (2) conflict resolution; (3) preference reasoning; (4) memory-grounded action prediction. The benchmark contains 1877 samples grounded in 264 sources. Experiments on representative memory-style and retrieval-based baselines show that current systems still struggle on these capabilities, positioning source-distributed multimodal memory as an important and still under-evaluated challenge for multimodal agents. Our data are available at this https URL.

---


### 75. [EntropyScan: Towards Model-level Backdoor Detection in LVLMs via Visual Attention Entropy](https://arxiv.org/abs/2605.15711)

**<font color=#1a73e8>作者：</font>** Xuanyu Ge, Zhongqi Wang, Jie Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities across various tasks, yet they remain vulnerable to backdoor attacks. Existing defense methods predominantly focus on sample-level defense, which relies on the knowledge of training data or triggers. However, identifying whether a given model is backdoored remains a critical but unexplored task. To fill this gap, we propose EntropyScan, a lightweight and trigger-agnostic method for model-level backdoor detection in LVLMs. We first observe that backdoor injection disrupts the cross-modal alignment, resulting in pronounced structural anomalies in visual attention allocation on benign samples. Based on this insight, EntropyScan detects the backdoor models by quantifying such attention deviations. Specifically, it extracts visual attention distributions from the initial layers of the Large Language Model (LLM) and applies Tsallis entropy to capture these structural distortions. By employing a reference-anchored Z-score normalization on a small set of benign samples, it effectively identifies the backdoored model. Extensive experiments across two LVLMs architectures and three advanced attack scenarios show that EntropyScan achieves an F1 score of 98.5% in average and an AUC of 96.6%. Our code will be publicly available soon.

---


### 76. [Contexting as Recommendation: Evolutionary Collaborative Filtering for Context Engineering](https://arxiv.org/abs/2605.15721)

**<font color=#1a73e8>作者：</font>** Jiachen Zhu, Zhuoying Ou, Congmin Zheng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are highly sensitive to their input contexts, motivating the development of automated context engineering. However, existing methods predominantly treat this as a global search problem, seeking a single context strategy that maximizes average performance across a dataset. This restrictive assumption overlooks the fact that different inputs often require distinct guidance, leaving substantial instance-level performance gains untapped. In this paper, we propose a paradigm shift by formulating context engineering as a recommendation problem. We introduce \textbf{Neural Collaborative Context Engineering (NCCE)}, a framework that transitions optimization from a static global search to dynamic, instance-wise routing. NCCE first bootstraps a diverse catalog of anchor contexts and then employs a novel \textbf{Context-CF Co-Evolution} mechanism. This stage establishes a synergistic feedback loop: a lightweight Neural Collaborative Filtering (NCF) model learns instance-context preferences to guide the generation of specialized context variants, while the newly evaluated contexts continuously refine the NCF model's understanding of latent preferences. At inference time, the trained NCF model acts as a context router, dynamically assigning the most suitable context strategy to each unseen instance. Theoretical Proofs and comprehensive experiments demonstrate that by matching individual inputs with their optimal contexts, NCCE significantly improves task accuracy, highlighting the critical importance of personalization in LLM context engineering.

---


### 77. [GOMA: Toward Structure-Driven Multimodal Alignment from a Graph Signal Smoothing Perspective](https://arxiv.org/abs/2605.15723)

**<font color=#1a73e8>作者：</font>** Xu Wang, Xunkai Li, Yinlin Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal alignment is commonly learned from isolated image-text pairs via CLIP-style dual encoders, leaving the relational context among entities largely unused. Multimodal attributed graphs (MAGs), where nodes carry multimodal attributes and edges encode corpus structure, provide a natural setting for refining frozen vision-language embeddings. This refinement is challenging: visual, textual, and cross-modal relations often induce different neighborhood geometries, while unrestricted graph propagation can quickly over-smooth retrieval representations. Effectively leveraging graph context therefore requires simultaneously breaking modality-specific topological barriers, controlling the smoothing regime, and preserving informative smoothing before semantic boundaries collapse. We propose Graph-Optimized Multimodal Alignment (GOMA), a structure-driven post-alignment framework that views frozen multimodal embeddings as graph signals and addresses these requirements through a unified retrieval-oriented design. GOMA decouples three key design choices: where messages should flow, how multimodal evidence should propagate, and which smoothing depth should be retained. Concretely, it learns modality-aware propagation operators, performs finite-step coupled smoothing without diagonal cross-modal shortcuts, and adaptively reads out node-specific smoothing trajectories to preserve useful smoothing before collapse. All experiments follow a transductive MAG retrieval protocol where the graph serves only as unlabeled context and diagonal self-pair edges are removed. On seven MAG benchmarks, GOMA achieves state-of-the-art or tied state-of-the-art retrieval and remains substantially more stable than the strongest graph competitor, demonstrating that MAG structure can serve as an effective post-encoder for frozen multimodal embeddings.

---


### 78. [DiLA: Disentangled Latent Action World Models](https://arxiv.org/abs/2605.15725)

**<font color=#1a73e8>作者：</font>** Tianqiu Zhang, Muyang Lyu, Yufan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent Action Models (LAMs) enable the learning of world models from unlabeled video by inferring abstract actions between consecutive frames. However, LAMs face a fundamental trade-off between action abstraction and generation fidelity. Existing methods typically circumvent this issue by using two-stage training with pre-trained world models or by limiting predictions to optical flow. In this paper, we introduce DiLA, a novel Disentangled Latent Action world model that aims to resolve this trade-off via content-structure disentanglement. Our key insight is that disentanglement and latent action learning are co-evolving: the predictive bottleneck inherent in latent action learning serves as a driving force for disentanglement, compelling the model to distill spatial layouts into the structure pathway while offloading visual details to a separate content pathway for generation. This synergy yields a continuous, semantically structured latent action space without compromising generative quality. DiLA achieves superior results in video generation quality, action transfer, visual planning, and manifold interpretability. These findings establish DiLA as a unified framework that simultaneously achieves high-level action abstraction and high-fidelity generation, advancing the frontier of self-supervised world model learning.

---


### 79. [Can We Trust AI-Inferred User States. A Psychometric Framework for Validating the Reliability of Users States Classification by LLMs in Operational Environments](https://arxiv.org/abs/2605.15734)

**<font color=#1a73e8>作者：</font>** Izabella Krzeminska, Michal Butkiewicz, Ewa Komkowska  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The use of large language models to assess user states in conversational and adaptive systems is based on the assumption that the metrics used for such assessment are stable and interpretable at the level of individual scores. This paper empirically tests this assumption, focusing on the psychometric reliability of artificial intelligence (AI) measures of user states.
This study employed replication evaluation procedures to assess the repeatability of a broad set of metrics across three different bimodal large language models (GPT-4o audio, Gemini 2.0 Flash, Gemini 2.5 Flash). Analyses include both individual score reliability and aggregated reliability, allowing us to distinguish metrics potentially useful for real-time adaptation from those that retain their value only in aggregated analyses.
The results demonstrate that metric reliability cannot be considered a default property in interpretive domains. The lack of stability at the level of individual scores precludes the interpretation of such scores as indicators of user state in real-time adaptive systems, even if these metrics demonstrate stability after aggregation. At the same time, the study indicates that individually unstable metrics can retain analytical utility in post-hoc studies, identifying rules governing interactions and their relationships with user experience parameters such as satisfaction, trust, and engagement.
The main contribution of this work, besides quantifying the severity of the problem (only 31 of 213 metrics met the criteria), is the proposal of a replicable evaluation framework, enabling measurable evaluations of metric applicability. This approach supports more responsible AI design of adaptive systems, in which the interpretation of results requires explicit validation of reliability and monitoring for violations over time.

---


### 80. [UAM: A Dual-Stream Perspective on Forgetting in VLA Training](https://arxiv.org/abs/2605.15735)

**<font color=#1a73e8>作者：</font>** Jianke Zhang, Yuanfei Luo, Yucheng Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision--language--action (VLA) models are typically built by fine-tuning a pretrained vision--language model (VLM) on action data. However, we show that this standard recipe systematically erodes the VLM's multimodal competence, a side effect we call the embodiment tax. But do VLAs have to forget? Inspired by the two-stream organization of biological vision, we trace this degradation to a structural bottleneck: current VLAs ask a single encoder to support both language-grounded semantics and control-relevant visual features, whereas biological vision separates recognition and visuomotor control into distinct pathways. Building on this view, we propose the Unified Action Model (UAM), which adds a parallel Dorsal Expert, an analog of the brain's dorsal pathway. To make the Dorsal Expert an effective second pathway and reduce the control-learning burden on the VLM, we initialize it from a pretrained generative model and train it with a mid-level reasoning objective that predicts visual dynamics. This design allows us to train the whole VLA end-to-end on action data alone: with no parameter freezing, no gradient stopping, and no auxiliary VL co-training, UAM retains over $95\%$ of the underlying VLM's multimodal capability and at the same time achieves the highest average success rate among baselines on a variety of manipulation tasks that probe out-of-distribution generalization, including unseen objects, novel object--target compositions, and instruction variation. Together, these results suggest that semantic preservation in VLAs can emerge from architectural separation itself, rather than being enforced by frozen weights or auxiliary data replay, and that this preserved semantic capability can naturally transfer from VLMs to semantic generalization in actions.

---


### 81. [BiomedAP: A Vision-Informed Dual-Anchor Framework with Gated Cross-Modal Fusion for Robust Medical Vision-Language Adaptation](https://arxiv.org/abs/2605.15736)

**<font color=#1a73e8>作者：</font>** Huanyang Tong, Kai Liu, Fangjun Kuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Biomedical Vision--Language Models (VLMs) have shown remarkable promise in few-shot medical diagnosis but face a critical bottleneck: \textit{fragility to prompt variations}.Existing adaptation frameworks typically optimize visual and textual prompts as independent streams, relying on ideal ``Golden Prompts''. In clinical reality, where descriptions are often noisy and heterogeneous, this modality isolation leads to unstable cross-modal alignment.
To address this, we propose BiomedAP, a vision-informed dual-anchor framework with gated cross-modal this http URL enforces synergistic alignment through two mechanisms: (1) Gated Cross-Modal Fusion, which enables layer-wise interaction between modalities, acting as a dynamic noise regulator to suppress irrelevant textual cues; and (2) a Dual-Anchor Constraint that regularizes learnable prompts toward stable semantic centroids derived from both expert templates (High Anchors) and few-shot visual prototypes (Low Anchors).
Extensive experiments across 11 benchmarks demonstrate that BiomedAP consistently surpasses baselines, achieving competitive few-shot accuracy and markedly enhanced robustness under prompt perturbations.
Our code is available at: this https URL.
Keywords: Vision-Language Models; Prompt Learning; Parameter-Efficient Fine-Tuning; Few-shot Learning

---


### 82. [Attribute-Grounded Selective Reasoning for Artwork Emotion Understanding with Multimodal Large Language Models](https://arxiv.org/abs/2605.15755)

**<font color=#1a73e8>作者：</font>** Cheng Zhang, Yuer Liu, Zhiyu Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) can produce fluent artwork emotion explanations, but they often suffer from attribute flooding: they enumerate many visible formal attributes without identifying which cues actually support the affective judgment. We therefore formulate artwork emotion understanding as Attribute-Grounded Selective Reasoning (AGSR), where predefined formal attributes serve as evidence units and only emotionally operative attributes should enter the final interpretation. To make this problem measurable, we extend EmoArt, originally introduced at ACM MM 2025 as a 132,664-artwork resource with content, formal-attribute, valence-arousal, and emotion annotations, by adding a 1,400-artwork human salience extension annotated by 15 art-trained annotators. This extension provides instance-level supervision for distinguishing attributes that are merely present from those that are emotionally salient. We further propose FAB-G (Formal-Attribute Bottleneck-Guided reasoning), a supervised multi-agent framework that first predicts attribute-level salience and then constrains downstream emotional analysis to the retained cues. Experiments show that FAB-G yields consistent gains in emotion, arousal, and valence prediction, achieves stronger agreement with human-marked salient attributes under Dice and Tversky metrics, and produces substantially more compact final explanations than prompting-based baselines. Cross-dataset evaluation further suggests that attribute-grounded salience selection transfers beyond the source distribution of EmoArt, while also revealing attribute-specific boundary cases. The dataset and project page are available at this https URL

---


### 83. [DimMem: Dimensional Structuring for Efficient Long-Term Agent Memory](https://arxiv.org/abs/2605.15759)

**<font color=#1a73e8>作者：</font>** Wentao Qiu, Haotian Hu, Fanyi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents require long-term memory to leverage information from past interactions. However, existing memory systems often face a fidelity--efficiency trade-off: raw dialogue histories are expensive, while flat facts or summaries may discard the structure needed for precise recall. We propose \textbf{DimMem}, a lightweight dimensional memory framework that represents each memory as an atomic, typed, and self-contained unit with explicit fields such as time, location, reason, purpose, and keywords. This representation exposes the structure needed for dimension-aware retrieval, memory update, and selective assistant-context recall without storing full histories in the model context. Across LoCoMo-10 and LongMemEval-S, DimMem achieves \textbf{81.43\%} and \textbf{78.20\%} overall accuracy, respectively, outperforming existing lightweight memory systems while reducing LoCoMo per-query token cost by \textbf{24\%}. We further show that dimensional memory extraction is learnable by compact models: after fine-tuning on the DimMem schema, a Qwen3-4B extractor surpasses LightMem with GPT-4.1-mini on both benchmarks and reaches performance comparable to, or better than, much larger extractors in key settings. These results suggest that explicit dimensional structuring is an effective and efficient foundation for long-term memory in LLM agents. Code is available at this https URL.

---


### 84. [CompactQE: Interpretable Translation Quality Estimation via Small Open-Weight LLMs](https://arxiv.org/abs/2605.15763)

**<font color=#1a73e8>作者：</font>** Kamil Guttmann, Zofia Fraś, Artur Nowakowski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current state-of-the-art Quality Estimation (QE) in machine translation relies on massive, proprietary LLMs, raising data privacy concerns. We demonstrate that smaller, open-source LLMs (<30B parameters) are a viable, cost-effective and privacy-preserving alternative. Using a single-pass prompting strategy, our models simultaneously generate quality scores, MQM error annotations, suggested error corrections, and full post-editions. Our analysis shows these models achieve highly competitive system-level correlations with human judgments that outperform traditional neural metrics, fine-tuned models, and human inter-annotator agreement, effectively approximating the capabilities of much larger proprietary LLMs.

---


### 85. [GRASP: Learning to Ground Social Reasoning in Multi-Person Non-Verbal Interactions](https://arxiv.org/abs/2605.15764)

**<font color=#1a73e8>作者：</font>** Junho Kim, Xu Cao, Houze Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding social interactions requires reasoning over subtle non-verbal cues, yet current multimodal large language models (MLLMs) often fail to identify who interacts with whom in multi-person videos. We introduce GRASP, a large-scale social reasoning dataset that connects high-level social QA with fine-grained gaze and deictic gesture events. GRASP contains 290K question--answer pairs over 46K videos totaling 749 hours, organized by a 16-category taxonomy spanning gaze, gesture, and joint gaze--gesture reasoning, together with GRASP-Bench for evaluation. Unlike prior resources that focus on either isolated cues or high-level social QA, GRASP builds questions from identity-consistent gaze trajectories, deictic gestures, and their joint compositions into social events. Moreover, we propose Social Grounding Reward (SGR), a learning signal that uses these social events to encourage models to reason about the participants involved in each interaction. Experiments show that SGR improves performance on GRASP-Bench while maintaining zero-shot performance on related social video QA benchmarks.

---


### 86. [SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?](https://arxiv.org/abs/2605.15777)

**<font color=#1a73e8>作者：</font>** Kean Shi, Zihang Li, Tianyi Ma 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-Using Agents (CUAs) are rapidly extending large language models (LLMs) beyond text-based reasoning toward action execution in more complex environments, such as web browsers and graphical user interfaces (GUIs). However, existing web and GUI agent benchmarks often rely on simplified settings, isolated tasks, or short-horizon interactions, making it difficult to assess capabilities of agents in realistic professional workflows. Software-as-a-Service (SaaS) environments are a natural choice for CUA evaluation, as they host a large share of modern digital work and naturally involve dynamic system states, cross-application coordination, domain-specific knowledge, and long-horizon dependencies. To this end, we introduce SaaS-Bench, a benchmark built on 23 deployable SaaS systems across six professional domains, containing 106 tasks grounded in realistic work scenarios. These tasks require long-horizon execution, cover both text-only and multimodal settings, and are evaluated with weighted verification checkpoints that measure strict task completion and partial progress. Experiments show that representative LLM-based agents struggle on SaaS-Bench, with even the strongest model completing fewer than 4% of tasks end-to-end, exposing limitations in planning, state tracking, cross-application context maintenance, and error recovery. Code are available at this https URL for reproduction.

---


### 87. [Reversing the Flow: Generation-to-Understanding Synergy in Large Multimodal Models](https://arxiv.org/abs/2605.15792)

**<font color=#1a73e8>作者：</font>** Yujun Tong, Dongliang Chang, Zijin Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The long-standing goal of multimodal AI is to build unified models in which visual understanding and visual generation mutually enhance one another. Despite recent works such as BAGEL, BLIP3o achieves remarkable progress; In practice, however, this unification remains one-directional: understanding routinely guides generation, yet how and why generation can support understanding is rarely investigated. We revisit this asymmetry and propose Generation-to-Understanding (G2U) synergy, where visual generation becomes an explicit intermediate reasoning step. Our framework enables a model to perform controlled generative acts, such as detail enhancement, context expansion or structural visualisation, to produce self-generated visual thoughts, which are then fed back into the model to refine perception without retraining or external tools. Through a comprehensive evaluation on twelve benchmarks, this reversed information flow consistently improves multimodal understanding. We show that generative fidelity bounds perceptual gain and that distinct families of edit prompts govern transfer efficiency. We further analyse whether models can decide what to imagine. While they can produce plausible edits, these self-generated visual thoughts lack stable task alignment, revealing that current large multimodal models fall short of true self-reflection. This work exposes a missing mechanism in unified cognition and suggests that imagination is not the end of understanding but its beginning.

---


### 88. [AOT-POT: Adaptive Operator Transformation for Large-Scale PDE Pre-training](https://arxiv.org/abs/2605.15793)

**<font color=#1a73e8>作者：</font>** Qitan Lv, Hong Wang, Zhongkai Hao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-training neural operators on diverse partial differential equation (PDE) datasets has emerged as a promising direction for building general-purpose surrogate models in scientific machine learning. However, the inherent complexity and structural diversity of PDE solution operators make multi-PDE pre-training fundamentally challenging. Existing methods mainly address this by increasing model capacity, while leaving the target solution operators unchanged. Inspired by classical numerical analysis, we instead propose to transform complex and diverse solution operators into simpler, better-aligned forms that are easier to model jointly. Since the optimal transformation varies across PDE types, it must be adaptive and input-dependent, allowing a single neural operator to approximate an entire family of operators. We instantiate this idea as AOT-POT (adaptive operator-transformation for pre-training operator transformer), which expands hidden representations into multiple parallel streams, adaptively aggregates and redistributes them before and after each sub-layer, and mixes streams through Sinkhorn-projected doubly stochastic matrices for stable training. These mechanisms together reshape diverse solution operators into a unified form that can be effectively modeled by a single architecture. Empirically, AOT-POT achieves state-of-the-art performance on 12 PDE benchmarks with only 3\% additional parameters, reducing relative L2 error by up to 77.6\% (40.9\% on average). Fine-tuning AOT-POT further reduces L2 error by up to 92\% on in-domain PDEs and 89\% on out-of-domain PDEs (unseen types during pre-training), demonstrating that adaptive operator transformation is an effective and complementary direction for advancing PDE foundation models beyond simply scaling model capacity.

---


### 89. [Conversations in Space: Structuring Non-Linear LLM Interactions on a Canvas](https://arxiv.org/abs/2605.15848)

**<font color=#1a73e8>作者：</font>** Rifat Mehreen Amin, Alperen Adatepe, Daniela Fernandes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational interfaces powered by large language models (LLMs) are widely used for ideation and analysis, yet their linear structure limits exploration of alternatives and management of long-running interactions. We present CanvasConvo, a conversational interface concept that transforms linear chat into a branching conversation tree embedded in a spatial canvas. CanvasConvo enables users to explore what-if scenarios by branching directly from conversational content, supporting parallel development of alternative directions. These branches are visualized on a canvas while remaining integrated with a familiar chat interface, allowing users to switch between linear and non-linear interaction. Features such as timeline-based navigation, automatic tagging and summarization, and context-aware controls (e.g., goals, reusable prompts) support structured interaction and continuity. We evaluated CanvasConvo in a 5-7 day field study with 24 participants. Our findings highlight how non-linear conversational structures support exploratory workflows and different interactions in LLM-based work.

---


### 90. [Do Less, Achieve More: Do We Need Every-Step Optimization for RL Fine-tuning of Diffusion Models?](https://arxiv.org/abs/2605.15855)

**<font color=#1a73e8>作者：</font>** Renye Yan, Jikang Cheng, Shikun Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite strong image-generation performance, diffusion models' reconstruction objectives limit alignment with human preferences. RL enables such alignment through explicit rewards. However, most studies apply RL to the full denoising trajectory, making it computationally costly and weakening preference alignment, i.e., doing more but achieving less. We observe that the impact of RL fine-tuning varies significantly across denoising stages. In the early stage, image structures are unstable and distant from the final reward signal. Applying RL at this stage leads to delayed rewards and action-reward mismatching, resulting in high variance and inefficient updates. Conversely, in the later stage, reward gains saturate, and continued training tends to overfit local details, intensifying reward hacking. To tackle these challenges, we propose AdaScope, an RL-enhanced plug-in that improves generation quality while reducing computational cost. Specifically, AdaScope adaptively identifies the optimal intervention timing for RL by perceiving the structural evolution and semantic consistency during denoising, and dynamically terminates training once the denoising converges and reward gains saturate. As a result, it achieves a rare 'dual benefit': a reduction in computational costs alongside a significant performance improvement. We offer theoretical grounds for the design of AdaScope. Compared with state-of-the-art methods, AdaScope improves performance by 66% while cutting computational cost by 59%.

---


### 91. [SOLAR: Self-supervised Joint Learning for Symmetric Multimodal Retrieval](https://arxiv.org/abs/2605.15868)

**<font color=#1a73e8>作者：</font>** Wenjie Yang, Hang Yu, Yuyu Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we address the critical yet underexplored challenge of symmetric multimodal-to-multimodal (MM2MM) retrieval, where queries and contexts are interchangeable. Existing universal multimodal retrieval works struggle with this task, as they are constrained by the labeled asymmetric datasets used. We produce SOLAR (Self-supervised jOint LeArning for symmetric multimodal Retrieval), a novel two-stage self-supervised framework that leverages readily available unlabeled web-scale image-text pairs. Based on the observation that both semantic alignment and discrepancies exist between two modalities, in the first stage, we learn the intersection mask of image-text pair, allowing us to align intersection while preserving semantic of difference. In the second stage, the learned mask is further utilized to construct positive and hardnegative samples via masking different parts of image/text, which enable us to conduct self-supervised multimodal embedding learning. Complementing this framework, we present a new benchmark featuring high-quality human-verified positive and hard-negative pairs to evaluate symmetric MM2MM retrieval under realistic conditions, as well as the corresponding pipeline. Extensive experiments against ten SOTA methods show SOLAR surpasses the strongest supervised VLM by 7.08 points on this benchmark, with over 50x fewer model parameters and a 5x smaller embedding dimension. Code and benchmark will be available soon.

---


### 92. [Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design](https://arxiv.org/abs/2605.15871)

**<font color=#1a73e8>作者：</font>** Alberto Pepe, Chien-Yu Lin, Despoina Magka 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Toward recursive self-improvement, we investigate LLM agents autonomously designing foundation models beyond standard Transformers. We introduce a dual-framework approach: AIRA-Compose for high-level architecture search, and AIRA-Design for low-level mechanistic implementation. AIRA-Compose uses 11 agents to explore fundamental computational primitives under a 24-hour budget. Agents evaluate million-parameter candidates, extrapolating top designs to 350M, 1B, and 3B scales. This yields 14 architectures across two families: AIRAformers (Transformer-based) and AIRAhybrids (Transformer-Mamba). Pre-trained at 1B scale, these consistently outperform Llama 3.2 and Composer-found baselines. On downstream tasks, AIRAformer-D and AIRAhybrid-D improve accuracy by 2.4% and 3.8% over Llama 3.2. Furthermore, AIRA-Compose finds models with highly efficient scaling frontiers: AIRAformer-C scales 54% and 71% faster than Llama 3.2 and Composer's best Transformer, while AIRAhybrid-C outscales Nemotron-2 by 23% and Composer's best hybrid by 37%. AIRA-Design tasks 20 agents with writing novel attention mechanisms for long-range dependencies and high-performing training scripts. On the Long Range Arena benchmark, agent-designed architectures reach within 2.3% and 2.6% of human state-of-the-art on document matching and text classification. On the Autoresearch benchmark, Greedy Opus 4.5 achieves 0.968 validation bits-per-byte under a fixed time budget, surpassing the published minimum. Together, these frameworks show AI agents can autonomously discover architectures and algorithmic optimizations matching or surpassing hand-designed baselines. This establishes a powerful paradigm for discovering next-generation foundation models, marking a clear step toward recursive self-improvement.

---


### 93. [Unlocking Dense Metric Depth Estimation in VLMs](https://arxiv.org/abs/2605.15876)

**<font color=#1a73e8>作者：</font>** Hanxun Yu, Xuan Qu, Yuxin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) excel at 2D tasks such as grounding and captioning, yet remain limited in 3D understanding. A key limitation is their text-only supervision paradigm, which under-constrains fine-grained visual perception and prevents the recovery of dense geometry. Prior methods either distill geometry from external vision models, introducing error accumulation, or enable direct prediction with inefficient per-pixel query or coarse token-level outputs. In this paper, we propose DepthVLM, a simple yet effective framework that transforms a single VLM into a native dense geometry predictor while preserving its multimodal capability. By attaching a lightweight depth head to the LLM backbone and training under a unified vision-text supervision paradigm with a two-stage schedule, DepthVLM generates full-resolution depth maps alongside language outputs in a single forward pass. We further introduce a unified indoor-outdoor metric depth benchmark in a VLM-compatible format. Experiments show that DepthVLM significantly outperforms existing VLMs with higher inference efficiency, surpasses leading pure vision models, and improves complex 3D spatial reasoning, moving toward a truly unified foundation model. All code and checkpoints will be publicly released.

---


### 94. [Linked Multi-Model Data on Russian Domestic and Foreign Policy Speeches](https://arxiv.org/abs/2605.15886)

**<font color=#1a73e8>作者：</font>** Daria Blinova, Gayathri Emuru, Rakesh Emuru 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces a dataset of interlinked multimodal political communications from the Russian government, addressing persistent deficiencies in the availability of social text- and image-based data for authoritarian politics contexts. The dataset comprises two large corpora of official speeches delivered by senior actors within the Kremlin and the Russian Ministry of Foreign Affairs over multiple decades. For each speech, we provide Russian- and English-language texts, associated images and captions where available, and harmonized metadata including (e.g.) dates, speakers, (geo)locations, and official government content tags. Unique identifiers link images to speeches and align Russian and English versions of the same communication texts. We further augment these linked datasets with validated topical annotations for both speech texts and speech images, which are generated via transformer-based multimodal topic modeling and refined by a Russian politics expert. The resulting data resources support multimodal, multilingual, temporal, and/or spatial analyses of (authoritarian) political communication and offer a valuable testbed for social science research and large language model (LLM) applications in political domains.

---


### 95. [LoCO: Low-rank Compositional Rotation Fine-tuning](https://arxiv.org/abs/2605.15916)

**<font color=#1a73e8>作者：</font>** An Nguyen, Jaesik Choi, Anh Tong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) has emerged as an critical technique for adapting large-scale foundation models across natural language processing and computer vision. While existing methods such as low-rank adaptations achieve parameter efficiency via low-rank weight updates, they are limited in their ability to preserve the geometric structure of pretrained representations. We introduce Low-rank Compositional Orthogonal fine-tuning (LoCO), a novel PEFT method that constructs orthogonal transformations through low-rank skew-symmetric matrices and compositional rotation chains. We propose an approximation scheme that enables fully parallel computation of compositional rotations, making the approach practical for high-dimensional feature spaces. Our method maintains low computational complexity while maintaining orthogonality with controlled approximation error. We validate LoCO across diverse domains, including diffusion transformer fine-tuning, vision transformer adaptation, and language model adaptation. Our method demonstrates superior or competitive performance compared to both existing orthogonal and non-orthogonal methods.

---


### 96. [Decomposed Vision-Language Alignment for Fine-Grained Open-Vocabulary Segmentation](https://arxiv.org/abs/2605.15942)

**<font color=#1a73e8>作者：</font>** Chenhao Wang, Yingrui Ji, Yu Meng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary segmentation models often struggle to generalize to unseen combinations of object categories and attributes, because fine-grained descriptions are typically encoded as holistic sentences that entangle multiple semantic units. We propose a Decomposed Vision-Language Alignment framework that explicitly factorizes textual prompts into a concept token and multiple attribute tokens, enabling separate cross-modal interactions for each semantic unit. At the feature level, we introduce a Feature-Gated Cross-Attention module that generates attribute-specific gating maps to fuse information in a multiplicative manner, effectively enforcing compositional semantics. At the scoring level, per-token similarities are aggregated in log-space, producing a stable and interpretable compositional matching. The method can be seamlessly integrated into existing transformer-based segmentation architectures and significantly improves generalization to unseen attribute-category compositions in fine-grained open-vocabulary segmentation benchmarks.

---


### 97. [Imperfect World Models are Exploitable](https://arxiv.org/abs/2605.15960)

**<font color=#1a73e8>作者：</font>** Logan Mondal Bhamidipaty, Esmeralda S. Whitammer, David Abel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a novel definition of model exploitation in reinforcement learning. Informally, a world model is exploitable if it implies that one policy should be strictly preferred over another while the environment's true transition model implies the reverse. We analogize our definition with a prior characterization of reward hacking but show that the associated proof of inevitability does not transfer to exploitation. To overcome this obstruction, we develop a general theory of reward hacking and model exploitation that proves that exploitation is essentially unavoidable on large policy sets and yields the corresponding claim for hacking as a special case. Unfortunately, we also find that the conditions that guarantee unhackability in finite policy sets have no counterpart that precludes exploitation. Consequently, we introduce a relaxed notion of exploitation and derive a safe horizon within which it can be avoided. Taken together, our results establish a formal bridge between reward hacking and model exploitation and elucidate the limits of safe planning in world models.

---


### 98. [Sparse Autoencoders enable Robust and Interpretable Fine-tuning of CLIP models](https://arxiv.org/abs/2605.15961)

**<font color=#1a73e8>作者：</font>** Fabian Morelli, Arnas Uselis, Ankit Sonthalia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale pre-trained vision-language models like CLIP demonstrate remarkable zero-shot performance across diverse tasks. However, fine-tuning these models to improve downstream performance often degrades robustness against distribution shifts. Recent approaches have attempted to mitigate this trade-off, but often rely on computationally expensive text-guidance. We propose a novel method for robust fine-tuning, SAE-FT, which operates only on the model's visual representations. SAE-FT regularizes changes to these representations by penalizing the addition and removal of semantically meaningful features identified by a Sparse Autoencoder trained on the pre-trained model. This constraint prevents catastrophic forgetting and makes the fine-tuning process interpretable, enabling direct analysis of semantic changes. SAE-FT is both mechanistically transparent and computationally efficient, matching or exceeding state-of-the-art performance on ImageNet and its associated distribution shift benchmarks. Code is publicly available at: this https URL.

---


### 99. [Deterministic Event-Graph Substrates as World Models for Counterfactual Reasoning](https://arxiv.org/abs/2605.15967)

**<font color=#1a73e8>作者：</font>** Fabio Rovai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study event-graph substrates: a class of world models that represent agent state as an append-only log of typed RDF triples and answer counterfactual queries by forking the log under a structured intervention vocabulary. Substrates are inspectable at the triple level, support exact counterfactuals, and transfer across domains without learned components. We formalize the class, prove a duality between explanatory and counterfactual queries that reduces both to the same causal-ancestor traversal, and evaluate a 1,400-line CLEVRER-DSL interpreter atop a domain-agnostic substrate runtime at full CLEVRER validation scale (n=75,618). The substrate exceeds the NS-DR symbolic oracle on all four per-question categories (by 9.89, 20.26, 17.65, and 0.80 percentage points), and exceeds the parametric ALOE baseline on descriptive and explanatory while lagging on predictive and counterfactual. We also introduce twin-EventLog, a 500-specification Park-canonical Smallville counterfactual benchmark on which the substrate exceeds Llama-3.1-8B with full context by 18.80 points joint accuracy.

---


### 100. [Learning Bilevel Policies over Symbolic World Models for Long-Horizon Planning](https://arxiv.org/abs/2605.15975)

**<font color=#1a73e8>作者：</font>** Dillon Z. Chen, Till Hofmann, Toryn Q. Klassen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We tackle the challenge of building embodied AI agents that can reliably solve long-horizon planning problems. Imitation learning from demonstrations has shown itself to be effective in training robots to solve a diversity of complex tasks requiring fine motor control and manipulation over low-level (LL), continuous environments. Yet, it remains a difficult endeavour to generate long-horizon plans from imitation learning alone. In contrast, high-level (HL), symbolic abstractions facilitate efficient and interpretable long-horizon planning. We propose to combine the strengths of LL imitation learning for manipulation and control, and HL symbolic abstractions for long-horizon planning. We realise this idea via \emph{bilevel policies} of the form $(\pi^{\mathrm{hl}}, \pi^{\mathrm{ll}})$, consisting of a neural policy $\pi^{\mathrm{ll}}$ learned from LL demonstrations, and an HL symbolic policy $\pi^{\mathrm{hl}}$ that is constructed from symbolic abstractions of the LL demonstrations combined with inductive generalisation. We implement these ideas in the BISON system. Experiments on extended MetaWorld benchmarks demonstrate that BISON generalises to long horizons and problems with greater numbers of objects than those solved by VLA and end-to-end methods, and is more time and memory efficient in training and inference. Notably, when ignoring LL execution, BISON's HL policies can solve HL problems with 10,000 relevant objects in under a minute. Project page: this https URL

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-127](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
