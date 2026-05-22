# 📦 其他研究 | 2026年05月23日

> 本类共 **347** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-347](./part-07.md)

---

### 201. [Sibyl-AutoResearch: Autonomous Research Needs Self-Evolving Trial-and-Error Harnesses, Not Paper Generators](https://arxiv.org/abs/2605.22343)

**<font color=#1a73e8>作者：</font>** Chengcheng Wang, Qinhua Xie, Wei He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Autonomous research systems increasingly make the scientific workflow executable: agents can propose ideas, run code, inspect results, and draft papers. But executable workflows do not by themselves produce research judgment. We analyze where current systems lose trial experience: weak evidence becomes prose, pilot signals become broad claims, memory remains textual, and recurring process failures do not change later behavior. We introduce Sibyl-AutoResearch, a self-evolving AutoResearch framework built around Scientific Trial-and-Error Harnesses. A harness lets agents run bounded trials, preserve positive and negative outcomes, and route lessons into later planning, validation, claim scope, scheduling, critique, writing, and harness repair. We formalize this through two auditable conversion units: trial-to-behavior conversion, which links trial signals to later research actions, and trial-to-harness-behavior conversion, which links recurring process failures to system updates. We implement the framework in SIBYL, a file-backed autonomous research system that exposes the state, roles, memory, gates, and artifact traces needed to inspect these conversion paths. A retrospective audit identifies eight high-confidence conversion events, with a median latency of one iteration and a maximum latency of three iterations. A recovered-failure registry further shows how five naturally occurring failure classes, including duplicate results, stale numbers, and unsupported statistics, were blocked, downgraded, or routed into later repair. These traces do not establish a comparative performance claim; they show that the proposed conversion units are recoverable from realistic autonomous-research workspaces. The SIBYL framework and system are available at this https URL.

---


### 202. [Partial Fusion of Neural Networks: Efficient Tradeoffs Between Ensembles and Weight Aggregation](https://arxiv.org/abs/2605.22350)

**<font color=#1a73e8>作者：</font>** Fabian Morelli, Stephan Eckstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensembles of neural networks typically outperform individual networks but incur large computational costs, whereas weight aggregation produces less costly, yet also less accurate, aggregate models. We introduce partial fusion of networks, which interpolates between ensembles and weight aggregation and thus allows for a flexible tradeoff between computational cost and performance. A direct way to achieve this is to extend existing weight aggregation methods based on neuron-level similarity between different networks, where partial fusion then only aggregates weights of neurons which are most similar. We showcase one particular method to jointly identify which neurons are most similar and match them via partial optimal transport. Further, we consider the more general perspective of weight aggregation and partial fusion as generalized pruning of ensemble models, where neurons cannot just be deleted, but also linearly combined. Finally, we show that generalized pruning applied to a single network yields similar benefits as partial fusion by allowing for a tradeoff between isolating, deleting, and linearly combining neurons based on similarity. Our code is available at this https URL.

---


### 203. [QuantSR+: Pushing the Limit of Quantized Image Super-Resolution Networks](https://arxiv.org/abs/2605.22351)

**<font color=#1a73e8>作者：</font>** Haotong Qin, Xudong Ma, Xianglong Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-bit quantization is widely used to compress super-resolution (SR) models and reduce storage and computation costs for deployment on resource-limited devices. However, when SR models are pushed to ultra-low precision (2-4 bits), performance can drop sharply due to diminished representational capacity and the detail-sensitive nature of SR. To address these issues, we propose QuantSR+, a unified framework that improves quantization operators, network design, and training optimization, achieving better trade-offs between accuracy and efficiency than prior low-bit SR methods. QuantSR+ mainly relies on three technical contributions: (1) Redistribution-driven Bit Determination (RBD), which reshapes quantization distributions in both forward and backward passes to preserve representation fidelity; (2) Quantized Slimmable Architecture (QSA), which begins with an over-parameterized model and progressively prunes less critical blocks to meet efficiency budgets while pushing the accuracy performance; and (3) Slimming-guided Function-localized Distillation (SFD), which enforces block-aware feature alignment via a direct loss and a progressive, function-local training schedule to capture quantization effects better and speed up convergence. Extensive experiments show that QuantSR+ achieves state-of-the-art performance against both specialized quantized SR methods and generic quantization approaches. For SwinIR-S on Urban100 (x4), it improves PSNR by 0.29 dB over the 2-bit SOTA baseline. Meanwhile, it delivers strong efficiency gains at 2-bit, reducing operations by up to 87.9% and storage by 89.4%. QuantSR+ is effective for both convolutional and transformer-based SR models, indicating broad applicability.

---


### 204. [TransitLM: A Large-Scale Dataset and Benchmark for Map-Free Transit Route Generation](https://arxiv.org/abs/2605.22355)

**<font color=#1a73e8>作者：</font>** Hanyu Guo, Jiedong Yang, Chao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Public transit route planning traditionally depends on structured map infrastructure and complex routing engines, and no existing dataset supports training models to bypass this dependency. We present TransitLM, a large-scale dataset of over 13 million transit route planning records from four Chinese cities covering 120,845 stations and 13,666 lines, released as a continual pre-training corpus and benchmark data for three evaluation tasks with complementary metrics. Experiments show that an LLM trained on TransitLM produces structurally valid routes at high accuracy and implicitly grounds arbitrary GPS coordinates to appropriate stations without any explicit mapping. These results demonstrate that transit route planning can be learned entirely from data, enabling end-to-end, map-free route generation directly from origin-destination information. The dataset and benchmark are available at this https URL, with evaluation code at this https URL.

---


### 205. [VEELA: A Clinically-Constrained Benchmark for Liver Vessel Segmentation in Computed Tomography Angiography](https://arxiv.org/abs/2605.22357)

**<font color=#1a73e8>作者：</font>** Ziya Ata Yazıcı, N. Sinem Gezer, İlkay Öksüz 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of hepatic and portal vessels in contrast-enhanced computed tomography angiography (CTA) remains challenging due to complex vascular topology, peripheral visibility limitations, and acquisition-induced ambiguities. While existing public datasets offer valuable benchmarks, few include clinically realistic annotation constraints. We introduce VEELA (Vessel Extraction and Extrication for Liver Analysis), a rigorously curated liver vessel dataset derived from 40 CTA scans inherited from the CHAOS grand-challenge cohort. All vessels were manually delineated slice-by-slice under multi-expert consensus, using a strict visibility-driven annotation policy and avoiding anatomically inferred interpolation. This design explicitly captures anatomical variability and imaging-related uncertainty. As a continuation of the CHAOS challenge, VEELA enables reproducible cross-benchmark evaluation while extending the scope to fine-grained hepatic and portal vessel segmentation. We further establish a standardized benchmarking framework and analyze complementary evaluation metrics, including topology-aware (clDice), overlap-based (IoU), boundary-sensitive (NSD), and geometry-aware (area, length) measures. Our results demonstrate that different metrics capture distinct aspects of vascular integrity, underscoring the necessity of multi-perspective evaluation for clinically meaningful vessel segmentation. VEELA is publicly released to facilitate reproducible research and support the development of robust vascular segmentation methods. Researchers can access the evaluation metrics, dataset, and submission platform at this https URL.

---


### 206. [GazePrior: Zero-Shot AR/VR Eye Tracking via Learned 3D Gaze Reconstruction](https://arxiv.org/abs/2605.22359)

**<font color=#1a73e8>作者：</font>** Corentin Dumery, David Colmenares, Alexander Fix 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Eye tracking (ET) is a foundational technology for advanced AR/VR applications. However, training ET models for every new ET device is challenging: real data collection is costly and time-consuming, while existing synthetic data generation methods lack realism. To remove the need for additional data collection while maintaining data quality, we introduce a data-driven 3D prior that models the distribution of human eyes across diverse identities, gaze directions, and light settings. This model, which we coin GazePrior, then enables sparse-input 3D reconstruction of annotated data collected with previous ET devices, which can in turn be rendered from the cameras of any target ET device. Our approach synthesizes data with the realism, diversity and ground-truth accuracy of real data collection without its prohibitive costs. Our experiments demonstrate that ET models trained with our synthesized data outperform previous zero-shot methods, achieving higher accuracy and robustness.

---


### 207. [Scaling Observation-aware Planning in Uncertain Domains](https://arxiv.org/abs/2605.22364)

**<font color=#1a73e8>作者：</font>** Adrian Zvizdenco, Arthur Conrado Veiga Bosquetti, Alberto Lluch Lafuente 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deciding which sensing capabilities to deploy on an agent in uncertain domains is a fundamental engineering challenge, in which one balances task achievability against the high costs of hardware and processing. This problem has previously been formalized as the Optimal Observability Problem (OOP), based on the well-known Partially Observable Markov Decision Process (POMDP) model for decision-making. This work studies (sub-)symbolic techniques to scale solving of decidable fragments of the OOP, namely the Sensor Selection Problem (SSP) and the Positional Observability Problem (POP). Besides improving the original approach based on parameter synthesis, we develop a new solving method that identifies sensible observation functions via decomposition of POMDPs, improving performance by 3 and 5 orders of magnitude for instance size and runtime, respectively.

---


### 208. [TimeGuard: Channel-wise Pool Training for Backdoor Defense in Time Series Forecasting](https://arxiv.org/abs/2605.22365)

**<font color=#1a73e8>作者：</font>** Quang Duc Nguyen, Siyuan Liang, Yiming Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Time Series Forecasting (TSF) plays a critical role across many domains, yet it is vulnerable to backdoor attacks. However, backdoor defenses tailored to TSF remain underexplored, due to data entanglement and task-formulation shift challenges. To fill this gap, we conduct a systematic evaluation of thirteen representative backdoor defenses across the TSF life cycle and analyze their failure modes. Our results reveal two fundamental issues: (1) data entanglement induces channel-level signal dilution, rendering sample-filtering and trigger-synthesis defenses ineffective at localizing backdoors; and (2) task-formulation shift leads to training-loss degeneration, causing poisoned and clean windows to become indistinguishable at training stages. Based on these findings, we propose a training-time backdoor defense for TSF, termed TimeGuard. Our method adopts channel-wise pool training as the core paradigm and initializes a high-confidence pool using time-aware criteria to mitigate signal dilution. Moreover, we introduce distance-regularized loss selection to progressively expand the reliable pool during training and ease loss degeneration. Extensive experiments across multiple datasets, forecasting architectures, and TSF backdoor attacks demonstrate that TimeGuard substantially improves robustness, boosting $\mathrm{MAE}_\mathrm{P}$ by $1.96\times$ over the leading baseline, while preserving clean performance within 5% $\mathrm{MAE}_\mathrm{C}$.

---


### 209. [VeriScale: Adversarial Test-Suite Scaling for Verifiable Code Generation](https://arxiv.org/abs/2605.22368)

**<font color=#1a73e8>作者：</font>** Yifan Bai, Xiaoyang Liu, Zihao Mou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed for software engineering, constructing high-quality benchmarks is crucial for evaluating not just the functional correctness, but also the formal verifiability of generated code. However, existing benchmarks are limited by the quantity and quality of positive and negative test cases, leading to an overestimation of model capabilities in generating specifications and implementations. To address this, we propose VeriScale, a novel framework driven by the adversarial implementations. It consists of two stages: test-suite expansion to construct diverse and challenging test cases, and test-suite reduction to distill them into compact yet discriminative suites. While VeriScale is general, we instantiate it on Verina to construct VerinaPlus, which expands the original test suites by over 83$\times$, and VerinaLite, a lightweight 14$\times$ variant. Our experiments across eight state-of-the-art LLMs demonstrate that VerinaPlus exposes substantial model weaknesses hidden by the original benchmark, evidenced by sharp score drops on both SpecGen and CodeGen tasks, whereas VerinaLite maintains this discriminative power at a fraction of the evaluation cost. The enhanced benchmarks and source code are publicly available at this https URL.

---


### 210. [ASAP: Attention Sink Anchored Pruning](https://arxiv.org/abs/2605.22372)

**<font color=#1a73e8>作者：</font>** Jaehyuk Lee, Hanyoung Kim, Yanggee Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) face severe computational bottlenecks due to the quadratic complexity of self-attention at high resolutions. Existing token reduction methods rely on local metrics - such as single-layer attention scores - that are inherently vulnerable to the attention sink phenomenon, where uninformative tokens are paradoxically preserved over salient foreground objects. We propose ASAP (Attention Sink Anchored Pruning), a training-free framework that recasts this sink as a feature. Modeling ViT information flow as a Lazy Random Walk, ASAP identifies the sink as a dominant accumulator of probability mass. By computing the diffusion distance to the sink within the cumulative transition matrix, ASAP partitions tokens via Radial Diffusion Clustering and compresses background redundancy through Transition Weight Pooling in a single shot. Extensive experiments across image, video, and vision-language tasks demonstrate ASAP outperforms state-of-the-art methods, accelerating throughput by up to 48% while maintaining - or even exceeding - baseline accuracy.

---


### 211. [Boundary-targeted Membership Inference Attacks on Safety Classifiers](https://arxiv.org/abs/2605.22373)

**<font color=#1a73e8>作者：</font>** Anthony Hughes, Alexander Goldberg, Prince Jha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety classifiers are essential safeguards within generative AI systems, filtering harmful content or identifying at-risk users when interacting with large language models. Despite their necessity, these models are trained on sensitive datasets including discussions of self-harm and mental health, raising important, yet poorly understood, privacy concerns. Membership inference attacks (MIAs) allow adversaries to infer membership of examples used to train models. In this work, we hypothesize that identifying the examples on which the classifier is least confident are informative for an adversary to infer membership. This reflects a localized failure of generalization, where the model relies on memorization to resolve ambiguity in the training set. To investigate this, we introduce a new boundary-targeted selection strategy that identifies low confidence examples that amplify the signal of an examples membership within a training set. Our experimental results show that an adversary can recover 19\% of the conversations a safety classifier flagged as indicating user distress, at a 5\% false-positive rate, on a classifier fine-tuned for detecting a user who may require emotional support. This is $3.5$ times more than attacking using state-of-the-art MIA methods alone. Finally, we characterize the boundary laying examples and show that content-based filtering is ineffective for protection, and existing noise strategies can effectively mitigate susceptibility of these examples.

---


### 212. [Towards Explainability of SLMs by investigating Token Level Activation](https://arxiv.org/abs/2605.22377)

**<font color=#1a73e8>作者：</font>** Sayantani Ghosh, Rajashik Datta, Amit Kumar Das 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based language models such as BERT having 110M+ parameters have revolutionized natural language understanding, yet their internal mechanisms remain largely opaque to researchers and practitioners. Traditional attention-based interpretability methods often emphasize structurally important but semantically weak tokens such as punctuation marks rather than meaningful semantic relationships. This work introduces a lightweight and model-agnostic framework for quantifying token-level representational importance using hidden-state activation strengths at Layer 8 of BERT. The proposed Activation Flow Network (AFN) framework computes Token Activation Strength using the L2 norm of Layer-8 hidden representations, enabling direct ranking of semantically salient tokens. The study further introduces a threshold-based activation bucket formulation that partitions tokens into HIGH-activation and LOW-activation groups using an empirical upper-quartile activation boundary. Experimental observations demonstrate that semantically meaningful content words consistently occupy the HIGH-activation bucket and dominate representational activation shifts, while structurally supportive tokens contribute comparatively less. The results suggest that Layer 8 acts as a critical semantic consolidation zone balancing structural and semantic information processing. By revealing how activation magnitudes concentrate around semantically informative tokens, this work provides an interpretable and computationally efficient alternative to attentioncentric analysis, contributing toward transforming BERT from a "black box" into a more transparent "glass box" model for natural language understanding.

---


### 213. [Multi-Stage Training for Abusive Comment Detection in Indic Languages](https://arxiv.org/abs/2605.22380)

**<font color=#1a73e8>作者：</font>** Pranshu Rastogi, Madhav Mathur, Ramaneswaran S 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years social media has become an increasingly popular tool for communication. People use it to share their ideas, exchange information, and discuss thoughts. Given its prevalence and widespread reach, social media must remain a safe space for people. Content generated on social media can be abusive and it has become increasingly important to detect such content. In this paper, we use a language-based preprocessing and an ensemble of several models and analyze their performance of abusive comment detection. Through extensive experimentation, we propose a pipeline that minimizes the false-positive rate (marking non-abusive as abusive) so that these systems can detect abusive comments without undermining the freedom of expression.

---


### 214. [Efficient Higher-order Subgraph Attribution via Message Passing](https://arxiv.org/abs/2605.22385)

**<font color=#1a73e8>作者：</font>** Ping Xiong, Thomas Schnake, Grégoire Montavon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explaining graph neural networks (GNNs) has become more and more important recently. Higher-order interpretation schemes, such as GNN-LRP (layer-wise relevance propagation for GNN), emerged as powerful tools for unraveling how different features interact thereby contributing to explaining GNNs. GNN-LRP gives a relevance attribution of walks between nodes at each layer, and the subgraph attribution is expressed as a sum over exponentially many such walks. In this work, we demonstrate that such exponential complexity can be avoided. In particular, we propose novel algorithms that enable to attribute subgraphs with GNN-LRP in linear-time (w.r.t. the network depth). Our algorithms are derived via message passing techniques that make use of the distributive property, thereby directly computing quantities for higher-order explanations. We further adapt our efficient algorithms to compute a generalization of subgraph attributions that also takes into account the neighboring graph features. Experimental results show the significant acceleration of the proposed algorithms and demonstrate the high usefulness and scalability of our novel generalized subgraph attribution method.

---


### 215. [Hybrid Kolmogorov-Arnold Network and XGBoost Framework for Week-Ahead Price Forecasting in Australia's National Electricity Market](https://arxiv.org/abs/2605.22387)

**<font color=#1a73e8>作者：</font>** Houxuan Zhou, Sriram Prasad, Chenghao Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate electricity price forecasting (EPF) is essential for market participants to support operational planning and risk management, yet remains challenging due to strong volatility, nonlinear dynamics, and frequent extreme price spikes. These challenges are particularly pronounced in the Australian National Electricity Market (NEM), where high renewable penetration further increases uncertainty. This paper investigates week-ahead electricity price forecasting and proposes a hybrid KAN+XGBoost framework that integrates Kolmogorov-Arnold Networks (KAN) with tree-based learning. The proposed approach combines the global nonlinear representation capability of KAN with the local robustness of XGBoost to capture both long-term dependencies and short-term price fluctuations. Experiments are conducted on real-world NEM data using an expanding window evaluation strategy. The results demonstrate that the proposed model outperforms benchmark methods, including SARIMAX, Long Short-Term Memory (LSTM), standalone KAN, and XGBoost, reducing MAE by approximately 12% compared to XGBoost and by over 50% compared to a naive baseline. The results suggest that hybrid learning strategies provide an effective and robust solution for electricity price forecasting in highly dynamic electricity markets.

---


### 216. [A Posterior-Predictive Variance Decomposition for Epistemic and Aleatoric Uncertainty in Wind Power Forecasting](https://arxiv.org/abs/2605.22390)

**<font color=#1a73e8>作者：</font>** Yinsong Chen, Samson S. Yu, Kashem M. Muttaqi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate wind power forecasting requires reliable uncertainty quantification, yet most existing methods report a single predictive uncertainty that conflates epistemic and aleatoric sources. This paper applies the law of total variance to the joint setting of heteroscedastic neural network regression and Bayesian posterior approximation, deriving an explicit decomposition of total uncertainty (TU) into aleatoric (AU) and epistemic (EU) components. The resulting estimators are compatible with standard posterior-approximation methods and with $\beta$-NLL training to regulate the mean--variance learning trade-off. A wind power--specific evaluation framework is proposed to validate disentanglement without access to ground-truth uncertainty labels, comprising three modules: controlled synthetic experiments to verify responses to heteroscedastic noise and distribution shift; data-property--driven validation on a real-world wind turbine SCADA dataset; and dataset-size scaling experiments to examine the predicted asymptotic behavior of EU. Across synthetic and real-world experiments, the decomposed AU and EU components respond in theoretically consistent directions to noise structure, distributional shift, and training-scale variation, supporting the theoretical consistency and operational utility of the proposed decomposition and evaluation protocol.

---


### 217. [Epicure: Navigating the Emergent Geometry of Food Ingredient Embeddings](https://arxiv.org/abs/2605.22391)

**<font color=#1a73e8>作者：</font>** Jakub Radzikowski, Josef Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Epicure, a family of three sibling skip-gram ingredient embeddings retrained from scratch on a multilingual recipe corpus. We aggregate 4.14M recipes from 11 sources spanning seven languages, English, Chinese, Russian, Vietnamese, Spanish, Turkish, Indonesian, German, and Indian-English, and normalise the raw ingredient strings to 1,790 canonical entries via an LLM-augmented pipeline. A 203,508-edge ingredient-ingredient NPMI graph and an 80,019-edge typed FlavorDB ingredient-compound graph, 2,247 typed compound nodes across 15 categories, seed three Metapath2Vec variants that share architecture and hyperparameters and differ only in the random-walk schema: Cooc walks the co-occurrence graph only, Chem walks the typed compound metapaths only, and Core blends both via injected ingredient-ingredient walks at controlled mixing, placing each model at a distinct point on the chemistry-vs-recipe-context spectrum.

---


### 218. [Minimum Description Length based Granular-Ball Tree Regularization for Spectral Clustering](https://arxiv.org/abs/2605.22410)

**<font color=#1a73e8>作者：</font>** Zeqiang Xian, Caihui Liu, Yong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spectral clustering largely depends on the affinity graph, yet constructing a graph that preserves reliable local connectivity while adapting to heterogeneous data structures remains challenging. Existing granular-ball-based spectral clustering methods usually reduce graph complexity by using coarse-grained representatives. However, the learned local regions are often treated as graph nodes or anchors, and their structural information is not sufficiently used to regularize the original sample-level graph. To address this issue, this paper proposes a Minimum Description Length based Granular-Ball Tree-Regularized Spectral Clustering method, termed MDL-GBTRSC. The proposed method constructs a granular-ball tree through local MDL model selection, with reciprocal neighborhood continuity used to discourage splits that break reliable local connections. The stable leaf balls obtained from the tree provide coding-scale information for regularizing the sample-level affinity graph. In addition, a shared-neighbor bridge code is introduced to adjust weak local bridge relations without requiring an additional user-specified threshold. In this way, MDL-GBTRSC connects interpretable local representation learning with affinity graph construction in a unified spectral clustering framework. Experiments on real and synthetic datasets show that MDL-GBTRSC achieves the best average ARI and NMI under the adopted fixed-configuration protocol compared with classical spectral clustering baselines and representative granular-ball, micro-cluster, and anchor-based methods.

---


### 219. [DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA](https://arxiv.org/abs/2605.22411)

**<font color=#1a73e8>作者：</font>** Jianing Yin, Tan Tang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents still struggle with long-term memory question answering, where answer-supporting evidence is often scattered across long conversational histories and buried in substantial irrelevant content. Existing memory systems typically process memory before future queries are known, then retrieve the resulting units based on similarity rather than their utility for answering the query. This workflow leaves downstream answerers to denoise retrieved candidates and reconstruct query-specific evidence. We present DeferMem, a long-term memory framework that decouples this problem into high-recall candidate retrieval and query-conditioned evidence distillation. DeferMem uses a lightweight segment-link structure to organize raw history and retrieve broad candidates at query time. It then applies a memory distiller trained with DistillPO, our reinforcement learning algorithm for distilling the high-recall but highly noisy candidates into a set of faithful, self-contained, and query-conditioned evidence. DistillPO formulates post-retrieval evidence distillation as a structured action comprising message selection and evidence rewriting. It optimizes this action with a decomposed-and-gated reward pipeline and structure-aligned advantage assignment, gating reward components from validity to quality checks while exposing task-level correctness feedback early and assigning each reward to its responsible output span. On LoCoMo and LongMemEval-S, DeferMem surpasses strong baselines in QA accuracy and memory-system efficiency, achieving the highest QA accuracy with the fastest runtime and zero commercial-API token cost for memory operations.

---


### 220. [Towards Clinically Interpretable Ophthalmic VQA via Spatially-Grounded Lesion Evidence](https://arxiv.org/abs/2605.22414)

**<font color=#1a73e8>作者：</font>** Xingyue Wang, Bo Liu, Meng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Question Answering (VQA) holds great promise for clinical support, particularly in ophthalmology, where retinal fundus photography is essential for diagnosis. However, ophthalmic VQA benchmarks primarily emphasize answer accuracy, neglecting the explicit visual evidence necessary for clinical interpretability. In this work, we introduce FundusGround, a new benchmark for clinically interpretable ophthalmic VQA with spatially-grounded lesion evidence. Specifically, we propose a three-stage pipeline that collects 10,719 fundus images with 15,595 image-level meticulously annotated lesions. To ensure anatomical consistency and clinical validity, all lesions are spatially localized using the Early Treatment Diabetic Retinopathy Study (ETDRS) grid, enabling standardized mapping to nine clinically meaningful retinal regions. Built upon this structured lesion evidence, 72,706 questions are then generated spanning four formats: open-ended, closed-ended, single-choice, and multiple-choice. We further benchmark multiple general- and medical- large vision-language models using dual metrics for answer accuracy and lesion-level reasoning. The experiments demonstrate that incorporating lesion-level visual evidence consistently improves model performance and transparency, highlighting the necessity of explicit spatial grounding for reliable and explainable ophthalmic VQA.

---


### 221. [Asymmetric Virtual Memory Paging for Hybrid Mamba-Transformer Inference](https://arxiv.org/abs/2605.22416)

**<font color=#1a73e8>作者：</font>** An Xuan Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid language models like Jamba mix attention layers with State Space Models (SSMs), creating two memory cache types with opposite profiles: Key-Value (KV) caches grow linearly with sequence length, while SSM states stay fixed per layer. Current inference engines handle this poorly. Unified pools pad SSM states to attention page sizes, wasting up to 7.3x capacity. Static dual pools cannot adapt when prompt distributions shift between requests. We present Asymmetric Virtual Memory Paging (AVMP). The allocator separates the two cache types into physically distinct pools behind a unified virtual address space, and migrates capacity between pools when one runs out. Migration triggers only on allocation failure, keeping behavior deterministic. We evaluate AVMP across 270 synthetic cells plus 60 cells of ShareGPT trace replay on an RTX 3060 12GB. Out-of-Memory events drop 7.6% and request throughput improves 1.83x to 13.3x across synthetic workloads and 2.36x on ShareGPT. All gains hold under paired-bootstrap 95% confidence intervals. A phase-time breakdown reveals two distinct mechanisms: shorter OOM recovery on capacity-pressured workloads, and faster allocation calls on KV-heavy workloads. Implementation is pure Python; Triton integration is future work.

---


### 222. [The Neglected Baseline in Model Interpretation](https://arxiv.org/abs/2605.22417)

**<font color=#1a73e8>作者：</font>** Yongjin Cui, Xiaohui Fan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We observe that existing model interpretation methods generally ignore the baseline, and such neglect often results in imprecise or even incorrect interpretation. In this paper, we reformulate the task of model interpretation and the interpretation principles for model interpretation results to demonstrate the importance of the baseline. We further unify gradient-based methods, Integrated Gradients (IG) methods, and Taylor expansion, clarifying the connections among them and explicitly identifying the baseline for each method. On this basis, we analyze the flaws and errors in related model interpretation methods (IG, LayerCAM, ODAM, Difference Map). We advocate evaluating the quality of model interpretation results precisely through the attribution error between the attribution result and the attribution target, rather than adopting flawed evaluation methods, such as those based on marginal-effect or the assumption of perfect model performance. We revise IG and develope a model interpretation method with a clear and reasonable baseline, achieving better results. Our method supports model interpretation based on features from any layer. Interpretation based on features from different layers are all reasonable, and the differences among these results reflect varying degrees of feature extraction at different feature extraction stages.

---


### 223. [Diffusion-guided Generalizable Enhancer for Urban Scene Reconstruction](https://arxiv.org/abs/2605.22420)

**<font color=#1a73e8>作者：</font>** Henry Che, Jingkang Wang, Yun Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban scene reconstruction from real-world observations has emerged as a powerful tool for self-driving development and testing. While current neural rendering approaches achieve high-fidelity rendering along the recorded trajectories, their quality degrades significantly under large viewpoint shifts, limiting the applicability for closed-loop simulation. Recent works have shown promising results in using diffusion models to enhance quality at these challenging viewpoints and distill improvements back into 3D representations. However, they often require costly per-scene optimization, and the distilled representations remain fragile and fail to generalize beyond limited synthesized views. To address these limitations, we propose GenRe, a novel diffusion-guided generalizable enhancer for urban scene reconstruction. GenRe takes as input any pretrained 3D Gaussian representation and fixes the deficiencies within a few minutes. By learning to distill generative priors across diverse scenes, GenRe produces robust and high-fidelity representation efficiently that generalizes reliably to challenging unseen viewpoints (e.g., lane change). Experiments show that GenRe outperforms existing methods in both quality and efficiency and benefits various downstream tasks, enabling robust and scalable sensor simulation for autonomous driving.

---


### 224. [FastTab: A Fast Table Recognizer with a Tiny Recursive Module and 1D Transformers](https://arxiv.org/abs/2605.22422)

**<font color=#1a73e8>作者：</font>** Laziz Hamdi, Amine Tamasna, Pascal Boisson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Table structure recognition (TSR) requires both table-level coherence (row/column counts, headers, spanning cells) and precise separator localization. We introduce FastTab, a grid-centric TSR model that avoids autoregressive HTML decoding by combining (i) a lightweight Tiny Recursive Module (TRM) for global reasoning and (ii) axial 1D Transformer encoders that capture long-range dependencies along rows and columns. The model predicts row/column counts, header rows, and separators to construct a grid, then infers rowspan/colspan using ROI-aligned cell features. Across four benchmarks (PubTabNet, FinTabNet, PubTables-1M, and SciTSR), FastTab achieves competitive structure recovery performance while operating at low-latency inference. We further study robustness under pixel-level anonymisation and show an extension to curved separators for camera-captured documents. The source code will be made publicly available at this https URL .

---


### 225. [Moment-Reenacting: Inverse Motion Degradation with Cross-shutter Guidance](https://arxiv.org/abs/2605.22423)

**<font color=#1a73e8>作者：</font>** Ji Xiang, Lin Guixu, Yin Zhengwei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion degradation, manifested as blur in global shutter (GS) images or rolling shutter (RS) distortion in RS counterparts, remains a fundamental challenge in computational imaging, especially under fast motion or low-light conditions. While prior works have treated blur decomposition and RS temporal super-resolution as separate tasks, this separation fails to exploit their intrinsic complementarity. In this paper, we propose a unified framework to invert motion degradation and reenact imaging moment by jointly leveraging the complementary characteristics of GS blur and RS distortion. To this end, we introduce a novel dual-shutter setup that captures synchronized blur-RS image pairs and demonstrate that this combination effectively resolves temporal and spatial ambiguities inherent in both modalities. For allowing flexible performance-cost trade-offs, we further extend this dual-shutter setup to a stereo Blur-RS configuration with a narrow baseline. In addition, we construct a triaxial imaging system to collect a real-world dataset with aligned GS-RS pairs and ground-truth high-speed frames, enabling robust training and evaluation beyond synthetic data. Our proposed network explicitly disentangles motion into context-aware and temporally-sensitive representations via a dual-stream motion interpretation module, followed by a self-prompted frame reconstruction stage. Extensive experiments validate the superiority and generalizability of our approach, establishing a new paradigm for realistic high-speed video reconstruction under complex motion degradations. Codes and more resources are available at this https URL.

---


### 226. [AMUSE: Anytime Muon with Stable Gradient Evaluation](https://arxiv.org/abs/2605.22432)

**<font color=#1a73e8>作者：</font>** Jueun Kim, Baekrok Shin, Jihun Yun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep learning commonly relies on AdamW with prescribed learning rate schedules, but recent works challenge both components: Schedule-Free optimization removes explicit schedules via iterate averaging, and Muon improves the update geometry by orthogonalizing momentum for matrix parameters. Despite Muon's strong empirical performance, its underlying mechanism remains partially understood. We study Muon through the river-valley loss landscape, where useful training progress occurs along a flat, low-curvature bulk subspace (the river), while high-curvature dominant directions form steep valley walls that induce oscillations. We empirically show that while Muon's orthogonalization accelerates river progress by increasing the bulk component, it also amplifies dominant-direction noise, causing oscillatory trajectories. Building on this, we propose Anytime MUon with Stable gradient Evaluation (AMUSE), which integrates Muon's rapid bulk progress with the stabilizing effect of Schedule-Free averaging. AMUSE uses a time-varying interpolation coefficient that initially evaluates gradients near the fast Muon sequence for rapid adaptation, then gradually shifts toward the stable averaged sequence to suppress valley-wall oscillations. As a result, AMUSE requires no learning rate schedules and supports anytime training. Across vision tasks and large language model pretraining, AMUSE consistently improves the performance-iteration Pareto frontier over (Schedule-Free) AdamW and Muon.

---


### 227. [Assisted Counterspeech Writing at the Crossroads of Hate Speech and Misinformation](https://arxiv.org/abs/2605.22435)

**<font color=#1a73e8>作者：</font>** Genoveffa Martone, Helena Bonaldi, Marco Guerini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hate speech and misinformation frequently co-occur online, amplifying prejudice and polarization. Given their scale, using Large Language Models (LLMs) to assist expert counterspeech (CS) writing has gained interest, yet prior work has addressed these phenomena separately. We bridge this gap by studying CS generation in contexts where both hate and misinformation co-occur. We test three knowledge-driven generation strategies: first we prompt an LLM with fact-checkers' guidelines and fact-checking articles; secondly, with NGOs' guidelines and reports; thirdly, we create a mixed strategy that combines guidelines and documents from both. 23 experts revise the generated CS, which are assessed via human and automatic metrics. While LLMs produce adequate CS in 40% of cases, expert edits substantially improve naturalness, exhaustiveness, and adherence to guidelines. Based on the post-edited CS, the mixed strategy proves to be the most effective in crowdsourcing evaluation, pairing strong factual correction with stereotype mitigation and empathetic engagement. We release a dataset of hateful and misinformed claims with expert-verified CS and supporting knowledge.

---


### 228. [Characterizing the Fault Response of the Intel Neural Compute Stick 2 Under Single-Pulse Electromagnetic Fault Injection](https://arxiv.org/abs/2605.22437)

**<font color=#1a73e8>作者：</font>** Štefan Kučerák, Jakub Breier, Xiaolu Hou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision processing units and other commercial neural-network inference accelerators are increasingly deployed in safety-relevant edge applications, but their fault response under transient hardware disturbances remains poorly characterized in the open literature. For the Intel Movidius Myriad X, packaged as the Intel Neural Compute Stick 2 (NCS2), only a single feasibility study has been published. We report a systematic single-pulse electromagnetic fault injection (EMFI) campaign on the NCS2 running three ImageNet-trained convolutional neural networks (ResNet-18, ResNet-50, VGG-11) on the OpenVINO runtime. Across 1,536 spot-test trials at characterized hotspots and approximately 16,000 parameter-search trials, single pulses produce four reproducible outcome classes: no measured accuracy change, minor silent data corruption, major persistent degradation that survives across subsequent inferences until model reload, and device hangs requiring USB power-cycling; these outcomes are respectively interpreted as no-effect, SDC with possible SET-like or small persistent-state mechanisms, SEU-like persistent corruption, and SEFI-like loss of functionality. Two findings are central. First, the major-degradation class can be induced at 18-31% of trials at characterized hotspots, with post-collapse top-1 accuracy below five percent and persistence across all subsequent inferences until explicit model reload - a regime that no inference-API-level mechanism detects. Second, this regime is also inducible by pulses delivered to an idle device with the model already loaded, demonstrating that load-time integrity checks alone are insufficient. We discuss mitigation strategies graded by class, focusing on mechanisms implementable at the application level without modification to the device firmware or the OpenVINO runtime.

---


### 229. [A Constant-Time Implementation Methodology for Activation Functions on Microcontrollers](https://arxiv.org/abs/2605.22441)

**<font color=#1a73e8>作者：</font>** Andrii Tyvodar, Andreas Rechberger, Dirmanto Jap 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Embedded neural-network inference can leak information through timing side channels, including leakage caused by the evaluation of activation functions. This work proposes a constant-time implementation methodology for activation functions on embedded microcontrollers and validates it on ReLU, sigmoid, tanh, GELU, and Swish on an ARM Cortex-M4 platform. The proposed methodology combines branchless selection, fixed-cost Padé-based approximation, dummy arithmetic where needed, and cycle alignment to obtain timing-regular activation-function implementations. As motivation, we also evaluate a desynchronization-based countermeasure and show that it remains vulnerable to a template-based timing attack. Experimental results show that the resulting protected implementations achieve identical cycle counts for all tested inputs, including (88) cycles in the three-function setting and (108) cycles in the five-function setting. At the same time, the numerical-error analysis indicates that the approximated nonlinear functions retain high accuracy. These results suggest that the proposed methodology provides a practical basis for constructing side-channel-resistant activation functions in embedded inference.

---


### 230. [Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts](https://arxiv.org/abs/2605.22446)

**<font color=#1a73e8>作者：</font>** Zhen Sun, Yongjian Guo, Haoran Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While large vision-language-action (VLA) models and generative world models (WM) have advanced long-horizon embodied intelligence, their practical deployment remains challenged by uncertainty in learning-based action generation. Low-quality actions may cause physical failures during execution or lead to misleading world-model rollouts with redundant rendering costs. To address this issue, we propose Pre-VLA, a unified runtime verification architecture that performs preemptive action validity assessment before physical execution or world-model imagination. Pre-VLA leverages an efficient multimodal backbone with modality-aware pooling and a lightweight dual-branch head to predict both safety confidence and critic-derived advantage scores for candidate action chunks. To handle severe class imbalance and unstable boundary decisions, we train Pre-VLA with a multi-task objective combining Focal classification, advantage regression, and soft-threshold calibration. During deployment, a dual-mode preemptive resampling scheduler filters low-quality actions and triggers adaptive resampling under a limited computation budget. Experiments on the LIBERO benchmark show that Pre-VLA improves the average closed-loop success rate across four suites from 30.79\% to 37.62\% over RynnVLA-002, reduces task execution steps, achieves 183.9 ms average forward verification time per action chunk, and mitigates error accumulation in world-model rollouts.

---


### 231. [Cohesion-6K: An Arabic Dataset for Analyzing Social Cohesion and Conflict in Online Discourse](https://arxiv.org/abs/2605.22447)

**<font color=#1a73e8>作者：</font>** Aisha Ali Al-Athba, Wajdi Zaghouani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The study of online discourse has become central to understanding societal polarization. While much research has focused on detecting overt toxicity, the subtle dynamics of social cohesion, meaning the interaction between divisive and unifying narratives, remain computationally underexplored (Bail, 2021; Gonzalez-Bailon and Lelkes, 2023). This paper presents Cohesion-6K, a manually and ChatGPT-assisted annotated dataset of six thousand Arabic public Facebook posts related to the Israeli Occupation of Palestine. Each post is assigned to one of five discourse categories that represent a continuum from conflict to cohesion: Conflict, Resolution, Community Engagement, Supportive Interactions, and Shared Values. The annotation process combines expert human judgment with model-assisted pre-labeling verified by trained annotators, achieving substantial inter-annotator agreement (Cohens kappa = 0.85). Quantitative analysis reveals a consistent engagement gap, where conflict-oriented posts receive between two and four times more user interaction than resolution-oriented ones (p < 0.01). This pattern illustrates how divisive discourse tends to attract disproportionate visibility in Arabic social media spaces. Cohesion-6K provides a transparent and reproducible resource for the study of online cohesion and polarization. The dataset, annotation guidelines, and preprocessing code will be released for research use under an open license, supporting future work in computational social science, digital communication, and Arabic natural language processing.

---


### 232. [S2ED: From Story to Executable Descriptions for Consistency-Aware Story Illustration](https://arxiv.org/abs/2605.22448)

**<font color=#1a73e8>作者：</font>** Sijing Yin, Jiamou Liu, Xiao Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-frame story illustration requires long-horizon coherence beyond single-image text-to-image generation, including narrative decomposition and persistent character identity, layout, and affect across frames. We propose Story-to-Executable Descriptions (S2ED), a training-free, model-agnostic, prompt-layer framework that converts a full story into a sequence of explicit, editable executable descriptions for more consistent rendering. S2ED coordinates three agents to segment the narrative, ground canonical character attributes, and enrich spatial and affective cues, enabling interpretable prompt-carried state propagation and local edits to repair drift without retraining the generator. Experiments on Flintstones and Shakoo Maku show that S2ED improves sequence-level consistency and character fidelity over strong prompting, large-model planning, and a reference training-based method, under both automatic metrics and human judgments. We also deploy S2ED in an end-to-end story-to-storybook system for children's illustrated stories, with a supplementary video.

---


### 233. [Don't Forget the Critic: Value-Based Data Rehearsal for Multi-Cyclic Continual Reinforcement Learning](https://arxiv.org/abs/2605.22454)

**<font color=#1a73e8>作者：</font>** Benjamin Poole, Andrew Quinn, Li Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data rehearsal has emerged as a leading approach for mitigating catastrophic forgetting in Continual Reinforcement Learning (CRL). However, existing work remains confined to policy gradient frameworks, regularizing only actors due to the performance degradation incurred by critic regularization. This actor-centric approach overlooks the potential of data rehearsal for value function approximation. Moreover, existing evaluations in CRL rarely consider multi-cyclic environments where task sequences repeat, a critical real-world scenario that exacerbates forgetting and plasticity. We investigate data rehearsal for Deep Q-Networks using Q-value regularization in multi-cyclic settings and propose Qreg+NWLU which introduces two simple modifications: (1) continuous data rehearsal that dynamically collects and updates stored Q-values throughout training, and (2) "No-Wait" regularization that applies immediately rather than after the first task. Together, these modifications yield improvements in learning efficiency, forgetting mitigation, and knowledge transfer over Qreg and conventional CRL methods within value function approximation settings.

---


### 234. [Making the Discrete Continuous: Synthetic RAW Augmentations for Fine-Grained Evaluation of Person Detection Performance in Low Light](https://arxiv.org/abs/2605.22455)

**<font color=#1a73e8>作者：</font>** Valeria Pais, Malena Mendilaharzu, Daniele Faccio 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world deployment of AI vision models is both fueled and limited by the data available for training and testing. Real datasets are sparse and uneven: long-tailed or unbalanced distributions hinder generalization, and the low number of samples in low density regions makes it hard to run evaluations. Synthetic data can fill these gaps, providing us with a way to sample the input space more continuously and improve data coverage for benchmarks. Focusing on the autonomous driving safety-critical case of pedestrian detection in the dark, we show how synthetic low-light samples can be used to better characterize the performance of a state-of-the-art object detection model as a function of the scene illumination. We use a synthetic RAW image augmentation technique to generate low-light samples that match the noise model of the camera sensor. Performance metrics on real and synthetic low-light data are similar, indicating that the AI model finds it hard to distinguish between them.

---


### 235. [KAPPS: A knowledge-based CPPS Architecture for the Circular Factory](https://arxiv.org/abs/2605.22457)

**<font color=#1a73e8>作者：</font>** Etienne Hoffmann, Jan-Felix Klein, Sören Weindel 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While linear manufacturing relies on homogeneous materials and predefined process sequences, circular manufacturing reintroduces used products with heterogeneous and uncertain conditions. This shift demands manufacturing systems capable of handling variable product states, dynamically reconfigurable processes, and the integration of human and machine knowledge. Conventional manufacturing IT architectures, designed for stable structures and deterministic execution, are unable to meet these requirements, as they cannot adequately represent and manage the uniqueness of individual components at runtime. Following a design science methodology for developing a Cyber Physical Production System for circular manufacturing, we derive 14 requirements from five complementary perspectives. Based on these requirements, we design KAPPS, a knowledge-based architecture that uses an ontology-grounded knowledge graph as a unifying data backbone, combined with a semantic interface layer to enable consistent data and information integration, reasoning, and communication across heterogeneous systems and services, turning the knowledge graph from an integration layer into the factories authoritative write-time state. KAPPS incorporates modules for constraint enforcement and event-driven planning, enabling incremental adaptation of execution plans under uncertainty and human-machine knowledge exchange. The applicability of KAPPS is demonstrated through two implemented use cases: (i) Anomaly detection and learning through knowledge graph mediated services and (ii) runtime constraint enforcement in a modular conveyor system. Subsequently, the architecture is evaluated against the 14 requirements (ed. abstract shortened)

---


### 236. [Perceived Safety of Workers in Encounters with Large Industrial AGVs](https://arxiv.org/abs/2605.22461)

**<font color=#1a73e8>作者：</font>** Ansgar Howey, Tim Schreiter, Andrey Rudenko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Automated Guided Vehicles (AGV) in factory automation are increasingly capable of moving autonomously in close proximity to human workers. While their physical safety is regulated by standards and directives, perceived safety and workers comfort in close-proximity interactions are being actively investigated in studies. There are three limitations in the prior art research to that end. Firstly, AGVs with larger payloads are understudied. Secondly, the test participants are usually students and not working professionals. Thirdly, while conducting in-person experiments with heavy machinery can be dangerous, the transfer of safety perception results from simulated experiments remains open. In this paper, we investigate industrial workers perceived safety in shared spaces with large AGVs in a real-world encounter and in virtual reality. We vary the passing distance and the shape of the collision avoidance maneuver, and evaluate perceived threat level using a handheld pressure-sensitive trigger interface and a post-experiment questionnaire. Additionally, we ask participants to set their own collision avoidance parameters based on their experience with the demonstrated trajectory profiles. In a within-subject study, we found that, while the threat levels are perceived overall slightly higher in VR, the passing distance of 1.5 to 2 meters is preferred among the demonstrated profiles, as well as in the self-defined trajectories.

---


### 237. [In Silico Modeling of the RAMPHO Buffer: Dissociating Informational and Energetic Masking via Phonetic Entropy in Deep Neural Networks](https://arxiv.org/abs/2605.22465)

**<font color=#1a73e8>作者：</font>** Stefan Bleeck  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The fundamental challenge of listening in multi-talker environments is a cognitive bottleneck, defined by the Ease of Language Understanding (ELU) model as a failure within the RAMPHO episodic buffer. Current deep neural networks for speech enhancement optimize purely for physical acoustics, failing to account for the cognitive penalty of informational masking. Here, we present an in silico simulation of the RAMPHO buffer using the frame-by-frame phonetic entropy of a self-supervised acoustic model (wav2vec 2.0). By contrasting a semantically intact distractor with a phase-decorrelated distractor (the Concentration Shield) across a signal-to-noise ratio (SNR) sweep, we successfully dissociate the cognitive penalty of informational distraction from the physical penalty of energetic decay. The simulation reveals a cognitive-acoustic Pareto optimization problem: destroying a distractor's semantic payload provides a release from informational masking at high SNRs, but fundamentally degrades temporal glimpsing cues at low SNRs.

---


### 238. [SADGE: Structure and Appearance Domain Gap Estimation of Synthetic and Real Data](https://arxiv.org/abs/2605.22467)

**<font color=#1a73e8>作者：</font>** Patryk Bartkowiak, Bartosz Kotrys, Dominik Michels 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose SADGE, a quantitative similarity metric that predicts the performance of synthetic image datasets for common computer vision tasks without downstream model training. Estimating whether a synthetic dataset will lead to a model that performs well on real-world data remains a bottleneck in model development. Existing evaluation metrics (e.g., PSNR, FID, CLIP) primarily measure semantic alignment between real and synthetic images (Appearance Similarity Score). Less commonly, structural similarity between images is considered to assess the domain gap (Geometric Similarity Score). However, to the best of our knowledge there exists no studies that evaluate which similarity metric is the best downstream predictor for a given synthetic dataset. In this paper, we show over a wide variety of different synthetic datasets and downstream tasks that neither appearance nor geometry alone can reliably predict downstream performance; rather, it is their non-linear interplay that dictates synthetic data utility. Specifically, we measure how commonly used Appearance and Geometric Similarity metrics computed between synthetic and real images correlate with downstream performance in object detection, semantic segmentation, and pose estimation. Across five public synthetic-to-real benchmark families and 15 dataset-level variants (79k image pairs), SADGE achieves the strongest association with downstream transfer performance under both linear and rank-based criteria, reaching Pearson r=0.88 and Spearman rho=0.77. We compute for each combination of geometry-based methods and appearance-based approaches SADGE scores across all benchmark families. The best configuration is obtained by fusing DINOv3 appearance similarity with MASt3R geometric consistency through a constrained bilinear interaction, outperforming both the strongest geometry-only baseline and the strongest appearance-only baseline .

---


### 239. [MaSC: A Masked Similarity Metric for Evaluating Concept-Driven Generation](https://arxiv.org/abs/2605.22469)

**<font color=#1a73e8>作者：</font>** Patryk Bartkowiak, Lennart Petersen, Bartosz Kotrys 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating single-concept personalization in text-to-image diffusion requires measuring both concept preservation, which captures identity fidelity to a reference, and prompt following, which captures whether the generated scene matches the prompt. Existing metrics commonly compute these signals using global image or text-image embeddings, such as CLIP-I, DINO, and CLIP-T. We show that such metrics correlate poorly with human perception because they attend to the image as a whole instead of separating the concept subject from the background. We introduce MaSC, a masked similarity metric that uses externally provided foreground concept masks to decompose evaluation into subject-specific concept preservation and background-based prompt following. MaSC computes both scores from frozen SigLIP2 SO400M-NaFlex features: concept preservation is measured by masked max-cosine matching between foreground reference patches and generated-image patches, while prompt following is measured by comparing a background-only pooled image embedding to a subject-stripped prompt embedding. On DreamBench++ human ratings, MaSC achieves Krippendorff alpha = 0.471 for concept preservation, outperforming all tested non-LLM baselines and GPT-4V, and approaching GPT-4o. On ORIDa, a real-photo identity-preservation benchmark across physical environments, MaSC achieves AUC = 0.992, nearly perfectly distinguishing same-subject from cross-subject pairs. Its prompt-following score also outperforms the CLIP-T baseline shipped with DreamBench++. These results show that spatially decomposed aggregation is a strong design principle for evaluating concept-driven generation.

---


### 240. [Lost in Tokenization: Fundamental Trade-offs in Graph Tokenization for Transformers](https://arxiv.org/abs/2605.22471)

**<font color=#1a73e8>作者：</font>** Maya Bechler-Speicher, Gilad Yehudai, Gil Harari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers have become a central architecture for graph learning, but their application to graphs requires first choosing a tokenization: a graph-to-token map that determines which structural information is exposed at the input. In this work, we show that this choice is a fundamental component of transformer expressivity. We examine three tokenizations that serve as building blocks for many existing graph tokenizations: spectral, random-walk, and adjacency tokenizations. We prove that different tokenizations induce distinct depth regimes: the same graph computation may be realizable by a shallow transformer under one tokenization, while requiring substantially larger depth under another. For example, we prove that random-walk tokenization is lossy for any walk length, making it impossible in general to recover the graph from it, and that while spectral tokenization is lossless, it is ill-conditioned for local tasks. We further show that although both random-walk and spectral tokenizations are derived from adjacency information, it is impossible for a limited-depth transformer to convert between tokenization families in general. In particular, we establish lower bounds and impossibility results showing that unfavorable tokenizations may preclude the efficient recovery of more suitable structural representations. Finally, we complement our theory with controlled experiments on synthetic and real-world tasks, validating the predicted separations and showing that different tasks favor different structural views, and combining complementary tokenizations allows the transformer to leverage distinct signals from each representation.

---


### 241. [Winner-Take-All bottlenecks enforce disentangled symbolic representations in multi-task learning](https://arxiv.org/abs/2605.22472)

**<font color=#1a73e8>作者：</font>** Julian Gutheil, Simon Hitzginger, Robert Legenstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Winner-take-all (WTA) networks constitute a central circuit motif in cortical networks of the brain. In addition, WTA-like activations are abundant in modern deep learning models in the form of the softmax activation for example in attention layers of transformers. While their role in the extraction of latent factors has been studied for relatively simple generative models, their role in the context of highly non-linearly entangled latent factors has remained elusive. In this article, we show that a WTA bottleneck within a deep neural network can enforce under certain well-defined conditions the extraction of categorical latent factors of the data in a multi-task learning setup. In particular, we prove that the representation that emerges in the WTA bottleneck is highly symbolic, where a single neuron or a population of neurons encodes the presence of a single abstract feature such as a specific object, color, or position. We furthermore show empirically on two datasets, that this also holds for architectures and setups that do not fully comply with the assumptions of our theorem and demonstrate the advantages of the acquired symbolic representation for generalization. Our proposed model provides insights into the generalization capabilities of deep neural networks with WTA-like components and may serve as an interface between symbolic and subsymbolic AI systems.

---


### 242. [Structured-Sparse Attention for Entity Tracking with Subquadratic Sequence Complexity](https://arxiv.org/abs/2605.22476)

**<font color=#1a73e8>作者：</font>** Hangyue Zhao, Paul Caillon, Erwan Fagnou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Entity tracking requires maintaining and updating latent states for entities and attributes over long sequences. Recent task-specific attention operators can compress deep Transformer stacks into a few layers by performing multi-hop state propagation within a single layer, but their dense evaluation remains expensive. We show that in this setting, learned attention is strongly structured: most mass concentrates in local block-diagonal neighborhoods with a light cross-block residue. Exploiting this, we derive a blockwise evaluation of a resolvent-style operator that keeps within-block interactions exact and routes cross-block interactions through a reduced system. The resulting evaluation is subquadratic in sequence length $O(n^{4/3}d)$ (and $O(n^{7/3})$ when $d\approx n$). On controlled tracking benchmarks, our method matches the dense operator's accuracy while reducing wall-clock time by $12-29\%$ under a standardized measurement protocol, and is up to $2.4 \times$ faster than a compact dense Transformer at comparable exact-match accuracy. We further provide ablations over block size and model capacity, and identify a limitation: performance collapses when the number of simultaneously evolving properties exceeds the number of attention heads.

---


### 243. [Exact Hidden Paths in Noisy High Dimensional Path Spaces](https://arxiv.org/abs/2605.22477)

**<font color=#1a73e8>作者：</font>** Victor Duarte Melo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce a mathematical and cryptographic framework for exact recovery of noisy hidden paths in high dimensional discrete path spaces. The work is inspired by the path integral viewpoint, where global quantities arise from contributions over many possible trajectories. Instead of approximating a global path sum, we study the inverse problem of recovering one exact hidden trajectory from incomplete, noisy, projected, and aggregated observables.
The hidden object is a planted discrete path whose transitions may include macro steps, microscopic perturbations, and discrete noise. Public information is represented by large observable vectors rather than short hash digests, since excessive compression would bound the effective recovery problem by the digest size.
We formalize several recovery notions, including planted exact recovery, arbitrary witness recovery, canonical recovery, quotient recovery, and recovery of derived encodings. The main distinction is that approximate reconstruction and exact recovery are fundamentally different tasks. A method may reveal coarse geometry or dominant regions without recovering the precise microscopic sequence defining the hidden path.
We also discuss attack surfaces relevant to future cryptographic use, including linearization, lattice style recovery, dynamic programming, meet in the middle attacks, SAT and SMT formulations, approximation followed by rounding, witness collisions, and generic quantum search.
This work does not claim a complete post quantum cryptosystem. It provides a formal framework for studying exact hidden path recovery as a possible foundation for future cryptographic constructions

---


### 244. [Matching with Deliberation: Test-Time Evolutionary Hierarchical Multi-Agents for Zero-Shot Compositional Image Retrieval](https://arxiv.org/abs/2605.22478)

**<font color=#1a73e8>作者：</font>** Xingtian Pei, Yukun Song, Changwei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-Shot Compositional Image Retrieval (ZS-CIR) requires both preserving the visual continuity of the reference image and faithfully executing the semantic variables specified in the modification text, which constitutes the core challenge of the task. Existing methods often suffer from Perception Myopia in a single space, or fall into Logic Drift in iterative collaboration due to the perception ceiling of the underlying retriever. To address this issue, we propose a one-stop hierarchical Perception-to-Deliberation Framework (PDF), which, to the best of our knowledge, is the first to introduce experience self-evolution and Test-Time Scaling Law (TTS) into ZS-CIR. Relying on a hierarchical multi-agent architecture, PDF first utilizes an Intent Routing Manager to dynamically dispatch multi-view Worker perception signals based on modification intents to construct a high-recall candidate pool. Subsequently, the Decision Manager combines a Training-free Reasoning Policy Distillation mechanism with a Tournament-style TTS strategy to achieve self-evolving fine-grained reasoning, yielding the final retrieval results. Experimental results demonstrate that PDF achieves SOTA performance on three benchmark datasets: CIRR, CIRCO, and FashionIQ. This study indicates that experience-driven self-evolution and TTS represent a highly promising and scalable path for achieving zero-shot fine-grained multimedia retrieval. The code will be made publicly available upon acceptance.

---


### 245. [Implicit Regularization of Mini-Batch Training in Graph Neural Networks](https://arxiv.org/abs/2605.22480)

**<font color=#1a73e8>作者：</font>** Clement Wang, Antoine Vialle, Robin Vaysse 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mini-batch training of Graph Neural Networks (GNNs) is fundamentally different from training on i.i.d. data: sampling a subgraph alters the topology and introduces boundary effects, leading prior work to develop structure-aware samplers that preserve local connectivity and reduce embedding variance. Surprisingly, we demonstrate that the simplest possible scheme, Random Node Sampling (RNS), training on the induced subgraph of uniformly sampled nodes, matches or outperforms full-graph training on 8 of 10 datasets at a fraction of the wall-clock time and memory. To explain this, we apply backward error analysis to graph mini-batch Stochastic Gradient Descent (SGD) and show that it implicitly minimizes the sampled loss plus a regularizer proportional to the mini-batch gradient variance, a quantity directly shaped by the sampler. Although RNS discards local structure, it produces mini-batches whose expected loss is closer to the full-graph loss, and whose per-batch gradients have lower variance, yielding a better implicit objective. Our analysis reframes the choice of graph sampler as a form of implicit regularization, and identifies RNS as a strong, theoretically grounded method for scalable GNN training.

---


### 246. [When Stronger Triggers Backfire: A High-Dimensional Theory of Backdoor Attacks](https://arxiv.org/abs/2605.22481)

**<font color=#1a73e8>作者：</font>** Donald Flynn, Hadas Yaron Goldhirsh, Jonathan P. Keating 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backdoor poisoning attacks behave counter-intuitively in high dimensions: stronger training triggers can help the defender. We study regularised generalised linear models on Gaussian-mixture data in the proportional regime ($p/n \to \kappa$), varying the training trigger strength $\alpha$ against a fixed test trigger. Three phenomena emerge: (i) clean test accuracy increases with $\alpha$; (ii) attack success peaks at a finite $\alpha$ and then declines; and (iii) the most damaging trigger direction is the minimum eigenvector of the data covariance. We prove all three results in closed form for the squared loss, and extend (i) and (ii) to general convex GLM losses via a Gaussian-proxy fixed-point system. We identify a finite-sample noise floor proportional to $\kappa$ as the mechanism behind (i), invisible to classical $n \gg p$ analysis. Experiments on CIFAR-10 and Gaussian surrogates match the theory closely; ResNet-18 experiments show the same phenomena beyond the convex setting.

---


### 247. [Represented Is Not Computed: A Causal Test of Candidate Algorithmic Intermediates in a Transformer](https://arxiv.org/abs/2605.22488)

**<font color=#1a73e8>作者：</font>** Ishita Darade, Sushrut Thorat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured prompts require integrating components according to task-relevant relations. How a network implements this integration is often hard to judge in language or vision, where those relations are rarely specified precisely enough to define a candidate internal algorithm. Arithmetic offers a cleaner setting. We study a Transformer trained on base-digit extraction: given $N$, $B$, and $D$, it must report the coefficient of $B^D$ in the base-$B$ expansion of $N$. The closed-form solution, $\lfloor N/B^D \rfloor \bmod B$, provides explicit candidate algorithmic intermediates. Across three seeds, the model reaches 99.83% exact-answer accuracy on held-out number-base intersections, establishing reliable task competence. Linear probes decode the intermediates, making staged arithmetic computation plausible. Causal tests then separate representation from use: within the localized route from the stream with $D$ as input to the output positions, behavior depends on early $D$-selective communication, independent of $N$ and $B$. Relatedly, a sparse circuit search finds mostly separate $N$, $B$, and $D$ routes that combine late rather than the staged route suggested by the probes. Thus, the model represents the intermediates that make the closed-form solution plausible, but the identified localized causal route does not transmit them to the output stream. This case shows that probe-based conclusions can diverge sharply from causal observations, even when explicit algorithmic hypotheses are available.

---


### 248. [Training-Free Fine-Grained Semantic Segmentations in Low Data Regimes: A FungiTastic Baseline](https://arxiv.org/abs/2605.22492)

**<font color=#1a73e8>作者：</font>** Sebastian Cavada, Francesco Pelosin, Lapo Faggi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained semantic segmentation requires both precise localization and discrimination between visually similar classes. In FungiTastic, this problem is further complicated by a long-tailed distribution and strong variation in image acquisition conditions. We propose a training-free two-stage framework that decouples segmentation from classification. SAM3 first produces class-agnostic mushroom masks using macro-taxonomic prompts, and DINOv3 then assigns fine-grained labels through prototype matching in the embedding space. To improve this stage, we apply a simple transformation of the DINOv3 feature space that improves prototype-based classification. Compared with class-specific prompting, our approach is more scalable and keeps the segmentation cost low. We report results from one-shot to few-hundred-shot regimes, providing, to the best of our knowledge, the first baseline for fine-grained semantic segmentation in low-data settings.

---


### 249. [The Signal in the Noise: OOD Detection Through Goodness-of-Fit Testing in Factorised Latent Spaces](https://arxiv.org/abs/2605.22496)

**<font color=#1a73e8>作者：</font>** Philipp Bomatter, Jack Geary, Henry Gouk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep generative models offer a natural foundation for out-of-distribution (OOD) detection, yet prior work has shown that their assigned likelihoods are notoriously unreliable indicators for in- vs out-of-distribution data. In this paper, we address this problem by leveraging the diffeomorphic and mass-preserving properties of continuous normalising flows. Our analysis shows that OOD samples are mapped to noise samples that are highly atypical under the noise prior in ways not captured by the likelihood. Based on this observation, we propose a new method -- Signal in the Noise (SITN) -- for OOD detection on the single-sample level. SITN requires no access to OOD data, incurs minimal computational overhead, and provides strict control of false positive rates. Comprehensive evaluations through standard benchmarks and synthetic perturbations highlight the method's effectiveness and the absence of the complexity bias inherent to likelihood-based methods.

---


### 250. [The Neural Compiler: Program-to-Network Translation for Hybrid Scientific Machine Learning](https://arxiv.org/abs/2605.22498)

**<font color=#1a73e8>作者：</font>** Lucas Sheneman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific machine learning often requires combining known physics with unknown parameters or correction terms learned from data. Existing approaches either ignore known structure, encode it as a soft penalty, or require hand-written PyTorch code for each equation. We present The Neural Compiler, a system that translates programs written in a first-order Scheme-like expression language into frozen, differentiable PyTorch modules. These modules match the source program to floating-point precision and provide gradients through autograd. In hybrid models, the compiled module encodes known physics exactly while learned components model the unknown remainder. We evaluate the compiler across six experiment domains: Feynman physics equations, Lotka-Volterra dynamics, a damped pendulum, a one-dimensional heat equation, three-dimensional vector mechanics, and compositional generalization. Compiled modules match hand-coded PyTorch implementations numerically for single equations, showing no accuracy loss from compilation. With only 1 to 4 trainable parameters, compiled models recover physical constants to less than 1 percent error in most cases, while standard PINN baselines with more than 8500 parameters show 7 to 93 percent error. Compiled modules also compose with zero error, while neural approximations can accumulate large errors in deep composition chains. The main value of the compiler is not improved accuracy over hand-coded equations, but systematic composability: it generates correct, differentiable modules from symbolic specifications without rewriting each equation by hand. The system supports 51 primitive operations, including vector and matrix algebra, enabling PDE discretizations and hybrid scientific models. This string-in, module-out interface also provides a natural target for large language models that translate scientific descriptions into executable differentiable modules.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-347](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
