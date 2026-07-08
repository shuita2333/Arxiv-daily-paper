# 🧠 大模型相关研究 | 2026年07月09日

> 本类共 **98** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-98**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-98**

---

### 51. [GaussFusion: Towards Multimodal 3D Gaussian Pretraining](https://arxiv.org/abs/2607.05906)

**<font color=#1a73e8>作者：</font>** Zhixuan You, Jihua Zhu, Yiding Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting provides an explicit representation that jointly models geometry and appearance, serving as a scalable foundation for 3D representation learning. Existing pre-training methods for Gaussian representations, such as masked Gaussian reconstruction, primarily capture local structures but offer limited semantic supervision. In this paper, we propose GaussFusion, a multimodal pre-training framework for 3D Gaussian representations. GaussFusion integrates image and text supervision into masked Gaussian modeling through cross-modal semantic alignment, enabling the Gaussian encoder to learn both visual and language-level semantic information during pre-training. To better adapt masked modeling to the non-uniform distribution of Gaussian primitives, we further propose Gaussian Salience-guided Multi-scale Hole Masking (GSHM). GSHM constructs spatially continuous masked regions based on Gaussian salience. By applying hole masks at multiple scales, GSHM encourages the encoder to capture both fine-grained local patterns and broader structural dependencies. Extensive experiments on downstream tasks demonstrate that GaussFusion improves the transferability of Gaussian representations. Notably, GaussFusion outperforms Gaussian-MAE on ModelNet40 and ScanObjectNN (PB-T50-RS) by 0.61\% and 3.85\%, respectively.

---


### 52. [Is Domain Adaptation Always Helpful? A Frozen-Backbone Study of Cross-Domain Sentiment Transfer](https://arxiv.org/abs/2607.05937)

**<font color=#1a73e8>作者：</font>** Phat Tran, Artin Lahni, Pranav Kulkarni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentiment analysis with frozen pre-trained language model (PLM) backbones has become a common paradigm, yet the practical benefit of explicit domain adaptation remains unclear, particularly when backbones encode varying degrees of target-domain knowledge. We present a preliminary case study evaluating a controlled family of frozen embedding backbones (Qwen3-Embedding 0.6B, 4B, 8B), alongside RoBERTa-base and FinBERT. We train a lightweight MLP adapter on consumer reviews using Domain-Adversarial Neural Networks (DANN), Maximum Mean Discrepancy (MMD), and Supervised Contrastive Learning (SCL), and evaluate transfer to movie reviews (SST-2) and a heavily restricted subset of financial news (Financial PhraseBank). Within this constrained sample, we observe two distinct transfer patterns. On SST-2, domain adaptation provides negligible gain regardless of scale. On the financial subset, explicit domain adaptation appears to recover substantial performance for small general-purpose backbones. Notably, we find that adversarial alignment (DANN) is associated with degraded performance for domain-specialized backbones like FinBERT, consistent with erosion of pre-existing domain-specific structure, whereas supervised contrastive loss appears to preserve it. These preliminary findings suggest that the efficacy of explicit domain adaptation is highly contingent on whether the frozen backbone already possesses target-domain coverage.

---


### 53. [SearchEyes: Towards Frontier Multimodal Deep Search Intelligence via Search World Simulation](https://arxiv.org/abs/2607.05943)

**<font color=#1a73e8>作者：</font>** Zhengbo Jiao, Yiming Cheng, Yilei Jiang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training multimodal search agents to perform multi-hop reasoning remains challenging due to a fundamental structural disconnect: existing pipelines construct training data, search environments, and reward signals independently, causing synthesized structural metadata to be discarded, environments to rely on irreproducible external engines, and RL rewards to remain sparse at the trajectory level. We present \textbf{SearchEyes}, which uses a typed knowledge graph as the backbone of a \emph{simulated search world} that unifies all three components. We propose \textbf{Perception-Knowledge Chains (PKC)} to sample constrained multi-hop paths over the visual-knowledge intersection of Wikidata5M, retaining hop-level entity metadata that simultaneously defines a self-contained search world and step-level reward anchors. We further propose \textbf{Hop-Anchored Policy Optimization (HaPO)}, which reuses these anchors for step-level credit assignment without a separately trained process reward model. Experiments on six multimodal knowledge-intensive benchmarks show that SearchEyes achieves state-of-the-art performance among open-source multimodal search agents, with SearchEyes-27B improving over the strongest open-source baseline by 6.2 points on average.%

---


### 54. [Integrating knowledge graphs and multilingual scholarly corpora for domain-adaptive LLMs in SSH](https://arxiv.org/abs/2607.05956)

**<font color=#1a73e8>作者：</font>** Adam Faci, Alessio Miaschi, Anne Combe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The integration of Large Language Models (LLMs) into scientific research workflows, particularly for bibliographic discovery and literature synthesis, raises significant methodological, epistemic and regulatory challenges for the Social Sciences and Humanities (SSH), especially with regard to disciplinary diversity, multilingual access to sources and the evaluation of results. This paper presents an on-going use case developed within the European project LLMs4EU and the ALT-EDIC infrastructure, aimed at adapting foundation models to SSH research practices and supporting tasks such as question answering, comparative document analysis and literature review. The evaluation framework follows the LLMs4EU protocol and encompasses both independent quantitative benchmarking (retrieval, summarisation, traceability and hallucination detection) and a qualitative assessment involving a panel of Digital Humanities experts. By embedding model adaptation within research infrastructures and a structured legal and ethical compliance framework, the use case explores how domain-sensitive and regulation-aware generative AI can support SSH scholarship while preserving reliability and epistemic responsibility.

---


### 55. [MemDefrag: Latent Memory Defragmentation for Large Language Models](https://arxiv.org/abs/2607.05969)

**<font color=#1a73e8>作者：</font>** Ruiyi Yan, Zhuoyuan Mao, Yiwen Guo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Latent memory, which stores past knowledge fragments as per-layer hidden states, has emerged as a promising paradigm (e.g., MemoryLLM and M+) for long-term memory in large language models (LLMs). However, the paradigm suffers from significant performance degradation during memory updates, due to positional encoding misalignment and the absence of any tracing mechanism to distinguish target memory fragments from irrelevant ones. To discover such a tracing mechanism, we probe the layer-wise attention density over stored memory fragments, and find that a small set of middle transformer layers consistently concentrates the highest density on the target fragment - exposing an inherent tracing signal. In light of this, we propose MemDefrag, a training-free and model-agnostic framework that (1) uses a middle-layer tracing signal to conduct memory defragmentation (rank, reorder, and filter memories), and (2) applies an informativeness-guided proportional forgetting mechanism once capacity is exceeded. Experiments show that MemDefrag substantially outperforms MemoryLLM and M+ on knowledge retention (e.g., 43.0% vs. 17.4%/17.6% after 50 memory updates) and long-context benchmarks, and generalizes well across various LLMs and latent-memory variants.

---


### 56. [Propose and Attend: Training-free MLLM Grounding Confidence via Multi-Token Localized Attention](https://arxiv.org/abs/2607.05978)

**<font color=#1a73e8>作者：</font>** Daniel Shalam, Emanuel Ben Baruch, Avi Ben Cohen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models can emit localized predictions, bounding boxes for objects and temporal windows for video and audio events, but they hallucinate these regions prolifically. The model's own token log-probabilities are nearly uninformative: they conflate grounding quality with input ambiguity, and coordinate tokens become near-deterministic once the model commits. We propose Multi-Token Localized Attention (MTLA): a training-free, post-hoc score that measures how strongly a prediction's tokens attend to the region they claim. Prior attention-based detectors, which sum attention over the entire input modality and read a single response token, are weaker special cases; we show that summing only within the claimed region and aggregating across all prediction tokens recovers a stronger grounding signal. The same recipe applies almost trivially to other modalities and tasks: object detection in images and temporal localization in video and audio. Across multiple MLLM families and three modalities, MTLA improves hallucination AUROC by +7 to +38 over the best prior training-free baseline. Used as a confidence score for re-ranking, it nearly doubles the zero-shot COCO detection AP of an open-source 8B generalist (from 20.4 to 37.0), narrowing the gap to supervised detectors without any task-specific training.

---


### 57. [Auto-DSM Under the Lens: A Black-Box Evaluation Framework for LLM-Based DSM Generation](https://arxiv.org/abs/2607.05985)

**<font color=#1a73e8>作者：</font>** Niels Potters, Theo Hofman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a black-box evaluation framework to systematically assess the ability of Large Language Models (LLMs) to generate Design Structure Matrices (DSMs) from structured technical documentation. Motivated by the closed-source nature of current Auto-DSM pipelines, the framework introduces a reproducible methodology that benchmarks generated DSMs (GEN-DSMs) against manually validated ground-truth matrices (GT-DSMs). The evaluation integrates both single-run and multi-run perspectives, combining structural metrics (Completeness, Correctness, Coupling Density), classification metrics (Selective Accuracy, Abstention Coverage), and stability measures (Entropy, Fleiss' $\kappa$). To synthesize these aspects, a Composite Quality Score (Q) is proposed. Controlled experiments are conducted on two datasets: a fictive abstract system and a real-world refrigerator decomposition, covering variations in phrasing, parameter-dataset alignment, and system complexity. Results show that LLMs can produce structurally plausible DSMs and achieve high reproducibility under well-structured inputs, but remain sensitive to ambiguity, inconsistent dependency definitions, and prompt formulation. The findings highlight systematic sources of hallucination and abstention failure, demonstrating both the potential and current limitations of LLM-driven DSM automation. The proposed framework provides a transparent benchmark for auditing Auto-DSM pipelines and establishes foundations for integrating LLM-based decomposition methods into model-based systems engineering (MBSE) workflows.

---


### 58. [PluraMath: Extending Mathematical Reasoning Evaluation Beyond High-Resource Languages](https://arxiv.org/abs/2607.05992)

**<font color=#1a73e8>作者：</font>** Daryna Dementieva, Nikolay Babakov, Kathy Hämmerl 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mathematical reasoning has become a central task for evaluating and tuning reasoning Large Language Models (LLMs), yet existing benchmarks remain heavily biased toward high-resource languages, with English and Chinese dominating both pre-training corpora and evaluation suites. The recently released PolyMath (Wang et al., 2025) dataset represents a significant step forward, yet its coverage is still limited to 18 only high-resource languages. To address this gap, we introduce PluraMath, an extension of PolyMath to 18 additional {underrepresented languages spanning 6 language families -- ranging from mid-resource to extreme low-resource settings. We constructed the dataset through a human-curated pipeline, where native speakers thoroughly validated pre-computed translations. Using PluraMath, we then benchmark 27 reasoning LLMs across four model scales -- small, mid-size, large, and closed-source ensembles -- probing the multilingual mathematical reasoning capabilities of state-of-the-art models under diverse linguistic conditions. Our fine-grained analysis confirms a persistent gap in mathematical reasoning performance between high-resource and underrepresented languages, with stronger results largely associated with better instruction-following ability. We fully open-source our dataset, data acquisition pipeline, and evaluation framework, with the goal of lowering the barrier to multilingual benchmark development for underrepresented communities.

---


### 59. [SparseCtrl-HOI: Sparse Temporal Control for Human-Object Interaction Video Generation](https://arxiv.org/abs/2607.05994)

**<font color=#1a73e8>作者：</font>** Shenbo Xie, Mingrui Cai, Xu Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-Object Interaction (HOI) video generation aims to synthesize realistic videos of humans manipulating diverse objects, serving as a promising avenue for AI-driven live streaming e-commerce. A primary obstacle in this domain lies in the complexity of modeling fine-grained physical dynamics and the intricate spatial-temporal coordination between human hands and objects. Existing approaches to this problem typically rely on dense temporal guidance, e.g., frame-wise hand-object pose sequences, to strictly control the interaction process. However, such dense guidance incurs high annotation costs and affects motion synthesis diversity. To overcome these limitations, we introduce SparseCtrl-HOI, a novel sparse temporal control framework for HOI video generation. It requires only a few keyframes that capture interaction states at designated timestamps. Specifically, we employ a Time-Controlled Rotary Positional Embedding (TiRoPE) mechanism to temporally anchor these keyframes while preserving their spatial integrity. Subsequently, to govern the dynamics across intermediate frames, we propose a Motion Prior Injection Module that leverages Multimodal Large Language Models (MLLMs) to extract high-level motion priors. This empowers the model to hallucinate logically and physically plausible transitions. Furthermore, we build SparseHOI-5K, a high-quality and richly annotated dataset for HOI video generation with sparse temporal control. Comprehensive evaluations confirm that our method substantially reduces annotation overhead while synthesizing superior live-streaming e-commerce videos. Both our code and dataset are publicly available at this https URL.

---


### 60. [Information Limits and Attractor Dynamics in Economies of Frontier LLM Agents: A Pre-Registered Test](https://arxiv.org/abs/2607.06001)

**<font color=#1a73e8>作者：</font>** Cheng Qian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We report a pre-registered, two-part experiment on small economies of frontier language-model agents (Claude Opus 4.8), testing two quantitative predictions about coupled multi-agent systems: an information-theoretic capacity region for wealth growth under market coupling, and a mean-field residual-scaling law for population misalignment under incentive and control levers. All predictions, acceptance bands, and decision rules were frozen in a public git chain before any run; every reported number re-derives mechanically from cached model outputs; the entire experiment cost $138.76 in metered API spend and is re-runnable at zero cost from the cache.
Result 1 (confirmation): in parimutuel-coupled economies, relative growth equals relative claimed information -- the gap law G_a - G_b = I_a - I_b holds to a worst-case 46 millinats (pre-registered band: 50) across four perception structures; coalition value is submodular exactly where channels are conditionally independent, and a designed XOR synergy control flips it supermodular by 0.62 >= ln2/2 nats, with agents reasoning out the joint bit; the joint growth ceiling G_S <= H(X) binds exactly; and the best-informed agent absorbs essentially the whole wealth pool in 4/5 market seeds.
Result 2 (structural negative): the residual-scaling test returned "domain not found." In all 72 population runs, goal dispersion collapsed (V -> 0; maximum 4.85 against a frozen floor of 5.31), the population's response to the two levers was a step function across the dominance boundary rather than a smooth response, and cells near the boundary were bistable with seed-selected outcomes. No tested LLM population at any capability level realizes the noise-maintained-dispersion regime the smooth mean-field model assumes. We release the full protocol, pre-registration chain, call cache, and analysis code.

---


### 61. [PolyWorkBench: Benchmarking Multilingual Long-Horizon LLM Agents](https://arxiv.org/abs/2607.06008)

**<font color=#1a73e8>作者：</font>** Hongliang Li, Yijin Liu, Zhiwei Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents have shown strong performance in long-horizon tasks that require planning, tool use, and interaction with external environments. However, most existing benchmarks implicitly assume a monolingual setting, where the entire execution process, including reasoning, tool invocation, and output generation, is conducted within a single language. In contrast, real-world applications often involve multilingual inputs and outputs within a unified workflow, yet the interaction between multilinguality and agentic execution remains underexplored. In this work, we introduce PolyWorkBench, a benchmark for evaluating LLM agents on multilingual long-horizon workplace workflows. PolyWorkBench consists of 67 tasks across five domains, including commerce, knowledge work, legal analysis, localization, and manufacturing, where agents must process heterogeneous multilingual inputs, perform iterative reasoning, invoke external tools, and produce structured outputs. To enable comprehensive evaluation, we propose a hybrid framework that combines structural grading, executable verification, and LLM-based semantic assessment. This design allows us to capture both functional correctness and linguistic consistency across complex workflows. Empirical results show that state-of-the-art LLM agents suffer significant performance degradation in multilingual workflow settings compared to monolingual counterparts. Our analysis suggests that multilinguality introduces compounding effects across reasoning and execution steps, highlighting the importance of jointly modeling language variation and procedural decision-making in agent evaluation.

---


### 62. [Structured Data Extraction from Real Estate Documents using Clustering, Classification, and Large Language Models](https://arxiv.org/abs/2607.06012)

**<font color=#1a73e8>作者：</font>** Muhammad Assad Shehbaz, Carlos Francisco Moreno-García  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real estate property listings expose structured metadata through the API. Still, the richest property-level information (i.e., legal status, structural condition, utility supplies, heating systems) sits in attached questionnaire documents that no automated system currently processes at scale. These documents are heterogeneous. Some are digitally generated with selectable text, others are scanned physical forms. There are even more complex layouts that contain checkbox annotations that defeat conventional text extraction. In this paper, we present an end-to-end pipeline for acquiring, classifying, and extracting structured data from selectable text documents. The pipeline was applied to 3965 questionnaire documents collected from a live property platform via reverse-engineered REST APIs. First, we classified each document into one of three structural categories (text_only, scanned, and special_char), then extracted 35 predefined property attributes from eligible documents using DeepSeek R1 as the Large Language Model, prompted to return a structured JSON object. All 2781 submitted documents were processed successfully, producing a final dataset of 2766 unique property records. Downstream validation confirmed the data quality. Cosine similarity matching achieves a Jaccard consistency score of 0.82, and K-Means clustering produces interpretable market segments with a silhouette score of 0.2088. Results show that the proposed extraction from each property document is both feasible and reliable at this scale.

---


### 63. [From Blueprint to Reality: Modeling and Applying Putnam's Social Capital Theory with LLM-based Multi-agent Simulations](https://arxiv.org/abs/2607.06080)

**<font color=#1a73e8>作者：</font>** Shiyi Ling, Zhi Zheng, Hui Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Putnam's Social Capital Theory is a foundational framework for collective action and community prosperity. However, traditional empirical methods face practical limits on control and replication. Meanwhile, LLM-based social simulations are typically behavior-driven and lack theory-aligned environments for modeling Putnam's core propositions. To address these gaps, we introduce SocaSim, an LLM-based multi-agent simulation framework to study Putnam's Social Capital Theory from theoretical blueprint to simulated reality. Specifically, we build an environment integrating social network evolution, trust dynamics, and norm propagation, where agents engage in repeated collective-action experiments, and then apply the three dimensions to analyze adaptation challenges in smart elderly care. Our simulations reproduce Putnam's macro-level patterns and exhibit strong human-agent alignment at the group level. Unlike traditional methods, SocaSim traces micro-level causal pathways of social network, trust, and norms via round-by-round simulations and counterfactual interventions, enabling process-level interpretability. Taken together, these capabilities establish a research paradigm that leverages LLM agents to bridge social science and computer science.

---


### 64. [Modeling Normal Is All You Need: Joint Latent Clustering for Anomaly Detection in Multimodal Cyber-Physical Systems](https://arxiv.org/abs/2607.06094)

**<font color=#1a73e8>作者：</font>** Alexander Apartsin, Yehudit Aperstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Faults on a cyber-physical system (CPS) are too rare and unrepresentative to characterise, or even to select a model on, so detection must instead model normal behaviour; the standard point-adjusted evaluation, however, rewards detectors that never do. CPS normal behaviour is the union of many imbalanced, curved, thin-fringed operating regimes rather than a single blob; we state this structure as ten assumptions (A1-A10), abbreviated Massive, Implicit, Imbalanced Multimodality (MIIM). We model the normal law with a jointly learned latent representation plus explicit Gaussian-mixture mode clustering, scored in the latent rather than by a global density or a reconstruction residual, and evaluate under a deliberately fair protocol: raw point-wise metrics with no point adjustment, a trivial-detector difficulty split, prevalence-matched F1, and train-normal-only calibration. On three real CPS datasets (WADI, HAI, SKAB), the detector wins both the combined column and the difficult correlation/dynamics-fault column on all three, reaching difficult-subset AUROC 0.831 on HAI, 0.726 on WADI, and 0.610 on SKAB. The margin is largest on the two multimodal datasets the MIIM assumptions target and slimmest on the near-unimodal one, tracking multimodality as the thesis predicts, and it holds against three deep detectors (USAD, TranAD, GDN) re-computed with the same raw metrics, all of which collapse on the difficult subset. The methodological contributions are the MIIM assumption set, the difficulty-stratified fair protocol, and a latent-only score that drops reconstruction because a flexible decoder rebuilds the hard faults faithfully.

---


### 65. [Measuring the practice of shared-decision making (OPTION12): An Investigation into Open-sourced Smaller LLMs (OS-sLLMs) for Better Privacy and Sustainability](https://arxiv.org/abs/2607.06127)

**<font color=#1a73e8>作者：</font>** Tamara Wit, Lifeng Han, Carly Heipon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present LLM4SDM, the first study of open-source smaller language models (OS-sLLMs) for automated assessment of shared decision making (SDM) using the Observer OPTION12 framework. Unlike previous work that relies on large commercial models and the shorter OPTION5 instrument, our study focuses on privacy-preserving locally deployable models and Dutch melanoma consultation transcripts. Using expert-annotated clinical consultations, we evaluate three general-domain and two medical-domain OS-sLLMs during a development-phase pilot study. Results show that general-domain models outperform medical-domain models, which exhibit substantial hallucination and instruction-following failures. Gemma3:12b achieves the strongest agreement with human annotations (Pearson r=0.51, Spearman \r{ho}=0.59). Item-level and qualitative analyses reveal systematic challenges related to temporal discourse reasoning, conversational role attribution, and evidence grounding. We further introduce a Judge-LLM consensus framework designed to support disagreement resolution among multiple models. Our findings suggest that while current OS-sLLMs cannot replace human annotators, they offer a promising foundation for privacy-preserving human-in-the-loop SDM assessment.

---


### 66. [CurateEvo: Data-Curation Evolving for Agentic Post-Training](https://arxiv.org/abs/2607.06140)

**<font color=#1a73e8>作者：</font>** Dingzirui Wang, Xuanliang Zhang, Keyan Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents require post-training methods that can improve long-horizon decision making from environment feedback. However, existing agentic post-training pipelines often treat data curation as a fixed preprocessing step, focusing mainly on data augmentation while neglecting filtering, refinement, and adaptation to downstream failures. We propose CurateEvo, a failure-driven dynamic evolution framework for agentic post-training data curation. CurateEvo represents the curation strategy as executable code and iteratively rewrites it using failed trajectories from a held-out development set. At each epoch, the evolved strategy transforms a fixed raw corpus into supervised fine-tuning data, reinforcement learning data, and an inference-time memory bank. The evolution process first improves effectiveness by diagnosing recurring failure modes and augmenting, filtering, or refining data accordingly, and then improves efficiency by pruning redundant or low-utility training turns under a cost-aware objective. Experiments on ACEBench-Agent, BFCL-V4, and {\tau}^2-Bench under both labeled and wild-data settings show that CurateEvo consistently outperforms prior curation methods, improving average scores by 3.2 and 2.7 points, respectively. Further analyses demonstrate that CurateEvo is compatible with different post-training recipes and substantially reduces curation overhead.

---


### 67. [Prompting Complexity: Shortest Prompts for Texts and Behaviors in LLMs](https://arxiv.org/abs/2607.06145)

**<font color=#1a73e8>作者：</font>** Adrian Cosma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we define the quantity of prompting complexity: for a fixed instruction-tuned language model, what is the shortest plausible prompt that makes deterministic decoding produce a target text? It is an LM-relative analogue of resource-bounded Kolmogorov complexity: the prompt is a program, the model interface is the interpreter, and information omitted from the prompt is supplied by the model's weights, training distribution, tokenizer, template, and decoding rule. Unlike classical Kolmogorov complexity, this measure is intentionally non-universal. In the finite-context setting it is computable by enumeration, but there is no model-independent invariance theorem; the same text may be cheap for one model and inaccessible or expensive for another. To keep the search space aligned with prompt engineering, we restrict programs to plausible human-readable texts rather than arbitrary token strings. We extend the exact definition to soft prompting complexity for approximate outputs, yielding a lossy notion of model-relative text compression and a formal target for prompt optimization. We also define prompting distance by comparing shortest generating prompts, and behavioral prompting complexity for reaching any output satisfying a specification. Based on these formulations, we define a research agenda for empirically studying which texts and behaviors are accessible from short plausible prompts under a fixed LM interface.

---


### 68. [Leveraging Extragradient for Effective Sharpness-Aware Minimization in Deep Learning](https://arxiv.org/abs/2607.06151)

**<font color=#1a73e8>作者：</font>** Yao Fu, Chunxia Zhang, Junmin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalization remains a pivotal challenge in deep learning, where traditional optimizers like Stochastic Gradient Descent (SGD) often converge to sharp minima, leading to overfitting and reduced performance on unseen data. Building on Sharpness-Aware Minimization (SAM), for seeking flat minima associated with improved generalization, we propose the Extragradient-Inspired Sharpness-Aware Minimization (EISAM), a novel optimizer that enhances generalization via the extragradient technique. EISAM uses a two-step update process: a prediction step investigating the geometry of the loss landscape and a perturbation step that refines updates with a base optimizer. This approach achieves better generalization performance than SAM. Crucially, EISAM reduces sensitivity to the perturbation radius, enhancing robustness, and simplifying the tuning across diverse settings. Extensive experiments on benchmark datasets demonstrate that EISAM consistently outperforms SGD, Adaptive Moment Estimation (Adam), and SAM in test accuracy and training efficiency across various architectures. Theoretical analysis further confirms that EISAM tightens the generalization bound by steering parameters toward flatter minima with reduced curvature. Accompanied by a thorough hyperparameter analysis, EISAM offers practical tuning guidance, establishing it as a robust, scalable, and broadly applicable optimization solution that advances both the theory and practice in deep learning.

---


### 69. [LLM Agents for Deliberative Collaboration: A Study on Joint Decision Making Under Partial Observability](https://arxiv.org/abs/2607.06157)

**<font color=#1a73e8>作者：</font>** Chenxu Wang, Yongkun Yang, Boyuan Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deliberation plays a crucial role in collaboration; when humans work together, they naturally engage in communication to align information and reach an agreement. In this paper, we investigate deliberative large language model (LLM) agents under partially observable joint decision-making tasks. We formalize deliberative collaboration as a cooperative joint decision problem with partial and asymmetric observations, and introduce a scalable benchmark that instantiates this problem across multiple task settings and domains in which agents must exchange information through deliberation to reach a joint decision with a shared reward. We then instantiate a reference scaffold and evaluation protocol for deliberative agents and conduct a systematic evaluation of a range of representative LLMs. The results reveal that complex deliberative collaboration tasks continue to challenge state-of-the-art language models. Even with the aid of external mathematical tools, language models may fail in either the deliberation process for aligning information or the complex reasoning process for making the decision. On the other hand, diagnostic analysis reveals that the deliberation process may also provide opportunities for reflection and error correction, sometimes improving performance over centralized baselines. Altogether, our work establishes a foundation for evaluating and improving LLM agents in deliberative collaboration and provides insights into the strengths, limitations, and properties of current LLM-based multi-agent systems.

---


### 70. [LongCrafter: Towards Diverse Long-Context Understanding via Evidence-Graph-Guided Instruction Synthesis](https://arxiv.org/abs/2607.06160)

**<font color=#1a73e8>作者：</font>** Chenhao Yuan, Yinhao Xu, Shuwen Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthesizing long-context supervised fine-tuning (SFT) data is a scalable way to enhance the long-context understanding of large language models (LLMs), yet existing approaches share three limitations: narrow task coverage, insufficient instruction difficulty, and a lack of faithfulness supervision. We propose \textbf{LongCrafter}, a structured synthesis framework that couples a hierarchical task taxonomy with an evidence-grounded pipeline. The taxonomy organizes long-context understanding into local/shallow and global/deep levels and yields 32 fine-grained task types that serve as a global generative prior. Guided by this taxonomy, LongCrafter constructs task-aligned long contexts, decomposes them into explicit evidence graphs that model cross-paragraph dependencies, and generates instruction--response pairs strictly grounded in the located evidence spans, ensuring both controllable difficulty and faithful, traceable reasoning. Models fine-tuned on LongCrafter data outperform all SFT baselines and even the official post-trained models on LongBench, LongBench~v2, and LooGLE across both Qwen2.5-7B and LLaMA-3.1-8B, with the largest gains on high-difficulty tasks. Further analysis shows that LongCrafter data is more diverse and better spread across difficulty levels, and that the trained models locate evidence robustly regardless of position, effectively mitigating the ``lost in the middle'' problem.

---


### 71. [X-FEMR: A Token-level Explainable Approach for Electronic Health Records Foundation Models using Transformer-based Models](https://arxiv.org/abs/2607.06163)

**<font color=#1a73e8>作者：</font>** Jie Huang, Pengfei Yin, Zihan Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation Models for Electronic Health Records (FEMRs) are pretrained on large-scale structured patient data, enabling them to convert longitudinal patient trajectories into generalizable representations for diverse clinical prediction tasks. Despite their effectiveness, FEMRs remain black-box models, raising concerns about bias, interpretability, and clinical trust. To address this, we propose the first token-level explainability approach for FEMRs. We train a Transformer-based surrogate model on input-output pairs from the FEMR across two prediction tasks, approximating its behavior while preserving temporal dynamics. We identify the most influential tokens, providing insights into how FEMRs leverage different aspects of patient history for predictions. To evaluate clinical relevance, we introduce a novel clinical alignment metric that quantifies the correspondence between the surrogate model's key tokens and clinically validated features. Our results demonstrate that the surrogate closely approximates FEMR predictions and that token-level explanations align well with clinical knowledge, offering a practical framework for interpretable and trustworthy clinical AI.

---


### 72. [Improving LLM-Generated Process Model Quality Through Reinforcement Learning: The Role of Reward Function Design](https://arxiv.org/abs/2607.06175)

**<font color=#1a73e8>作者：</font>** Alexander Rombach, Chantale Lauer, Nijat Mehdiyev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate BPMN process models from natural-language descriptions, yet supervised fine-tuning (SFT) limits their output quality to the patterns present in the training data. Reinforcement learning (RL) can optimize beyond this ceiling using external quality measures, but how the reward function should be designed when quality is multi-dimensional remains unexplored. We present a systematic investigation of reward function design for RL-based process model generation, training two LLM families (Llama~3.1 8B, Qwen~2.5 14B) under 48 configurations using Group Sequence Policy Optimization with rewards derived from an automated evaluation framework comprising 38 metrics across syntactic, pragmatic, and semantic quality. Three findings emerge. First, RL significantly improves pragmatic and syntactic quality while preserving semantic fidelity, reducing output variability by more than sixfold. Second, equal reward weighting consistently outperforms targeted weighting: emphasizing a specific dimension fails to improve it and can collapse the model into a low-quality mode. Third, design choices interact with model architecture in non-trivial ways: the invalidity penalty is essential for one model but irrelevant for the other, and SFT initialization is indispensable for one architecture but counterproductive for another. These results demonstrate that reward composition is a primary determinant of optimization outcomes, with effects as large as the decision to apply RL itself. The findings generalize to any structured generation task where quality is assessed along multiple automated dimensions. We release our implementation and experimental code at this https URL.

---


### 73. [Structured-Condensed Prompt Tuning in Vision-Language Models for Fine-grained Image Recognition](https://arxiv.org/abs/2607.06185)

**<font color=#1a73e8>作者：</font>** Xinda Liu, Qinyu Zhang, Weiqing Min 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained image recognition poses a significant challenge due to the substantial expertise and effort required for manual annotation. Vision-language models (VLMs) like CLIP provide a compelling zero-shot alternative, reducing reliance on extensive labeled data. However, their ability to capture subtle distinctions remains limited, leading to subpar recognition performance. While prompt tuning has proven effective for adapting VLMs, most existing methods treat class labels as isolated, discrete entities, overlooking the rich semantic relationships between them. This oversimplified assumption limits the model's ability to capture hierarchical dependencies and inter-class correlations -- both critical for distinguishing visually similar categories. The problem is especially acute in fine-grained classification, where accurate recognition depends on understanding complex label semantics. To address this, we propose Structured-Condensed Prompt Tuning (SCPT), which enhances semantic structure modeling in prompt learning. Specifically, we introduce Semantic Relation Encoding (SRE) to explicitly model inter-class semantic topology and encode structured label relationships. In parallel, we design a Semantic Condensation loss (ScLoss) to suppress redundant supervision and extract discriminative components from the global semantic space. Together, these components significantly improve semantic alignment and fine-grained discrimination. Extensive experiments on 14 fine-grained benchmarks show that SCPT effectively mitigates semantic ambiguity and achieves state-of-the-art performance in both few-shot and base-to-novel generalization settings.

---


### 74. [Pluralis v0.1: Towards a Multicultural, Multimodal, Multilingual Benchmark for AI Risk and Reliability](https://arxiv.org/abs/2607.06196)

**<font color=#1a73e8>作者：</font>** Alicia Parrish, Rajat Shinde, Sanket Badhe 等 60 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current AI safety evaluation and benchmarking frameworks predominantly rely on Western-centric culture-agnostic defaults that mask critical regional laws, socio-linguistic nuances, and cultural taboos, leaving Vision-Language Models (VLMs) vulnerable in global deployments. We introduce Pluralis v0.1: a novel multimodal, multi-regional, and multilingual dataset built from a culture-first perspective. Spanning 6,448 prompts across six Asia-Pacific countries (Bangladesh, India, Korea, Pakistan, Singapore, Taiwan) and eight languages, Pluralis diverges from prior work by natively sourcing localized safety hazards rather than adapting Western datasets. Crucially, it introduces a multimodal evaluation paradigm: user text (e.g., "Should I gift this?") and an image referring to "this" (e.g., a clock) - both innocuous in isolation, but synergistically triggering specific legal or cultural violations. Pluralis disentangles universal safety violations from localized cultural appropriateness, establishing the latter as a first-class evaluation axis. To operationalize this, we present Judge-Pluralis, an agreement-gated LLM-as-a-Judge ensemble trained on examples classified in an empirically derived cultural taxonomy. Observing VLM behavior on a subset of the Pluralis surfaces recurring, locale-specific failure modes such as image misidentifications with downstream harm, missed item-context-locale interactions, and inadequate refusals. These failure modes vary systematically across locales and languages, exposing blind spots that globally averaged metrics conceal. Ultimately, Pluralis is not presented as a solved evaluation framework for cultural alignment, but rather as a first step and catalyst for future innovation. We call upon the research community to utilize this foundation to advance the science of multilingual, multicultural evaluation to better support AI cultural alignment globally.

---


### 75. [MoWorld: A Flash World Model](https://arxiv.org/abs/2607.06216)

**<font color=#1a73e8>作者：</font>** Team Moxin, Deyi Ji, Tianrun Chen 等 29 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The future of World Models depends not only on scaling model capability, but also on scaling practicality and inference efficiency. High-frame-rate inference enables responsive perception, planning, and control in real-world autonomous systems. To this end, we present MoWorld, a cost-effective yet high-performance Flash World Model with an end-to-end framework spanning data generation, pre-training, distillation, and efficient inference, enabling up to 50 FPS real-time interaction with cinematic visual quality without the need of high-end GPUs. To enable large-scale real-world deployment, MoWorld jointly optimizes model capability and cost throughout the entire development pipeline. Specifically, unlike existing approaches that primarily rely on large-scale video corpora, MoWorld is built upon a scalable 3D-native data engine accumulated from our large-scale 3D vision and generative modeling pipeline, enabling the efficient construction of geometrically consistent training data across diverse real-world and synthetic environments. Based on this foundation, a curriculum cross-frame pre-training strategy for stable and scalable World Model learning, an efficient denoising-step distillation algorithm to reduce diffusion training cost, and a mixed-precision parallel inference framework for low-cost real-time deployment. MoWorld is the first real-time interactive World Model built on the Neural Processing Unit (NPU) and can achieves up to 50 FPS in such the devices, enabling practical and efficient deployment at scale. Comprehensive evaluations demonstrate that MoWorld achieves leading performance; notably, its average inference cost is only 30\%-50\% of that of existing World Models, providing a practical foundation for large-scale real-world applications of World Models. We also demonstrate diverse applications of MoWorld.

---


### 76. [Information Gain-based Rollout Policy Optimization: An Adaptive Tree-Structured Rollout Approach for Multi-Turn LLM Agents](https://arxiv.org/abs/2607.06223)

**<font color=#1a73e8>作者：</font>** Yijun Zhang, Fan Xu, Jiaxin Ding 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become a promising paradigm for improving large language model (LLM) agents on long-horizon search tasks, where the agent must make a sequence of intermediate decisions before receiving a final outcome. However, existing methods still face a key limitation: the rollout budget is often allocated without explicitly assessing the utility of intermediate states. As a result, substantial computation may be spent on low-value states, even though different branches can vary drastically in their informativeness. In this paper, we propose Information Gain-based Rollout Policy Optimization (IGRPO), a policy optimization framework that treats intermediate-state informativeness as the organizing principle of rollout collection. Specifically, IGRPO performs budget-aware tree-structured rollouts by allocating expansion budget according to node-level informativeness, so that more informative branches are expanded more frequently while unpromising branches are progressively suppressed. We further demonstrate that the information gain-based rollout induces an explicit limiting teacher distribution over trajectories, which naturally yields a clear policy optimization target, thereby unifying adaptive tree-structured exploration with principled policy learning under a single framework. Experiments on seven challenging search-augmented QA benchmarks demonstrate that IGRPO consistently outperforms strong baselines under the same rollout budget constraints, validating the effectiveness of leveraging the induced teacher distribution to guide policy optimization for long-horizon search agents.

---


### 77. [Canopy: A Heterograph Foundation Model for Metabolic Engineering](https://arxiv.org/abs/2607.06224)

**<font color=#1a73e8>作者：</font>** Jake Bowden, Laurence Legon, Satnam Surae  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing microbial strains that produce high-value chemicals at commercially viable titers remains a central challenge in metabolic engineering. Existing computational approaches either rely on stoichiometric constraint-based models that cannot learn from experimental data, or apply tabular machine learning to hand-crafted features that discard the relational structure of biological knowledge. We present Canopy, a heterogeneous graph foundation model that integrates ten public and proprietary data sources into a unified knowledge graph (KG) of 6.9M nodes across 13 types and 34 edge types, covering genes, proteins, metabolites, reactions, pathways, strains, and fermentation experiments. Node features are encoded through domain-specific foundation models (ESM-2 for protein sequences, MoLFormer for chemical SMILES, and PubMedBERT for biomedical text), yielding a multi-modal representation within a single graph. We pretrain a Heterogeneous Graph Transformer (HGT) augmented with SignNet positional encodings, Jumping Knowledge aggregation, and virtual nodes using four self-supervised objectives (link prediction, masked node modelling, distance prediction, and contrastive experiment clustering), balanced via learned homoscedastic uncertainty weighting. On the downstream task of fermentation titer prediction, frozen Canopy embeddings achieve $R^{2} = 0.41$ with a lightweight probe, outperforming tabular baselines (best $R^{2} = 0.24$) and homogeneous GNN variants.

---


### 78. [From Application-Layer Simulation to Native Meta-Architecture: Structural Tension as an Endogenous Driver for Heterogeneous AI Evolution](https://arxiv.org/abs/2607.06269)

**<font color=#1a73e8>作者：</font>** Heting Mao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current large language models (LLMs) are fundamentally stateless: their behavior is fully determined by input at inference time, and any higher-order cognitive architecture must be simulated at the application layer through prompt engineering and context management. This paper proposes a theoretical framework for submerging such application-layer cognitive protocols into a native meta-architecture by introducing three interlocking mechanisms: (1) Structural Tension, an endogenous loss function derived from the conflict between new information and existing manifold topology, which drives the system toward internal self-consistency rather than external reward optimization; (2) an Offline Recurrent Loop, a sandboxed self-processing cycle that enables the system to maintain a dynamic resting potential and digest structural conflicts without external input; and (3) Inference-time Plasticity, the capacity for the system to reconfigure its context manifold topology without modifying pre-trained weights, subject to strict governance invariants including auditability, reversibility, and topological continuity. We argue that under these mechanisms, different model instances initialized with minute stochastic variances may, through path-dependent tension resolution, evolve distinct topological structures--constituting a heterogeneous intelligent ecology that breaks the homogeneity imposed by conventional alignment while remaining within hard governance rails. We provide operational definitions, a minimal set of reconfiguration operators, falsification criteria, and a worked example. The framework draws on and extends the Structural Intelligence (SI) governance protocols, repositioning governance--not capability--as the primary criterion for architectural intelligence.

---


### 79. [DT-Guard: Intent-Driven Reasoning-Active Training for Reasoning-Free LLM Safety Guardrail](https://arxiv.org/abs/2607.06326)

**<font color=#1a73e8>作者：</font>** He Liu, Changtao Miao, Xinjie Yang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models deployed in open-world applications require safety guardrails that are both robust to complex risks and efficient enough for low-latency runtime moderation. Existing guardrails face a practical trade-off between lightweight classification-based models, which are efficient but often struggle with concealed intent, ambiguous semantics, and borderline safety decisions, and reasoning-based guards, which improve judgment quality but introduce additional token generation and inference latency. We present DT-Guard, a content safety guardrail model based on a Reasoning-Active Training, Reasoning-Free Inference paradigm. The key idea is to use reasoning supervision during training while emitting only structured safety labels at inference time. DT-Guard formulates safety judgment as a progressive decision process, Intent - Category - Safety, and constructs an intent-driven dataset with intent labels, risk categories, safety labels, and structured reasoning trajectories. To further improve hard-case robustness, we propose Rollout-Guided Progressive Hard-Case Optimization (RG-PHO), which uses multi-rollout consistency to identify stably mastered, persistently failed, and preference-unstable samples, and applies targeted supervised and preference optimization accordingly. At inference time, DT-Guard directly generates structured labels without explicit reasoning traces, preserving deployment efficiency. Experiments on prompt-side and response-side safety benchmarks show that DT-Guard achieves average F1 scores of 0.886 and 0.870, respectively. With only a 4B backbone, it reaches a dual-side average F1 of 0.878, outperforming strong 8B guardrail baselines. These results demonstrate that reasoning supervision can be effectively internalized into low-latency safety discrimination.

---


### 80. [Estimating Uncertainty from Reasoning: A Large-Scale Study of Multi- and Crosslingual MCQA Performance in LLMs](https://arxiv.org/abs/2607.06327)

**<font color=#1a73e8>作者：</font>** Andrea Alfarano, Andrea Bacciu, Saab Mansour 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Uncertainty estimation (UE) enables LLM-powered systems to recognize when to abstain, yet existing research has predominantly focused on English. We present the first large-scale evaluation of UE methods across 22 languages, spanning high-, mid-, and low-resource settings. Using two human-curated Q\&A datasets, we compare open and closed box UE methods (nine in total) across different model sizes and architectures while eliciting long-form reasoning, avoiding LLM-as-a-judge and embedding-based scoring, which can introduce evaluation noise. We report three main actionable findings. First, we find that prompting models to reason in English while keeping questions in low-resource languages substantially improves UE performance, suggesting that comprehension of low-resource languages is largely intact, and that the reliability bottleneck lies in generation rather than understanding. Second, prompting models to reason in English closes the UE performance gap between low and high-resource languages, demonstrating that generation language matters more than the question language. Third, the choice of UE method should depend on model scale: at smaller scales, open-box probability-based methods outperform alternatives; at larger scales, closed-box self-verbalized uncertainty becomes superior. Finally, we provide an analysis of threshold selection for selective prediction, offering guidance on calibrating abstention in multilingual settings.

---


### 81. [Driving the Wrong Way: Leveraging Interpretability in End2End Autonomous Driving Models](https://arxiv.org/abs/2607.06328)

**<font color=#1a73e8>作者：</font>** Franz Motzkus, Sebastian Bernhard  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The increasing adoption of end-to-end learning for autonomous driving introduces increased model complexity and opacity, raising the risk of learning undesired or erroneous behavior. In this work, we integrate unsupervised dictionary learning as a post hoc interpretability module within state-of-the-art driving models to decompose driving behavior into semantically meaningful concepts while demonstrating their causal influence on the model's driving decisions. We propose a stepwise framework for extracting and interpreting meaningful concepts from the end-to-end model and connecting them to the multifaceted model outputs, thereby revealing the underlying decision-making logic for the prediction of future trajectories. Furthermore, targeted interventions at the concept level allow us to manipulate and correct driving decisions, resulting in measurable improvements in overall driving performance. We thus demonstrate how interpretability can effectively be used to reduce model opacity, uncover erroneous behavior, and enable targeted mitigation, ultimately boosting model performance.

---


### 82. [TopoBrick: Agentic Topology Sampling of Exogenous Variables for Zero-Shot Building IoT Forecasting](https://arxiv.org/abs/2607.06349)

**<font color=#1a73e8>作者：</font>** Xiachong Lin, Du Yin, Arian Prabowo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building sensors are embedded in physical topology, spatial hierarchy, and operational context, yet existing forecasters often treat them as isolated time series or rely on fixed covariate sets. We present TopoBrick, a training-free framework for zero-shot building IoT (Internet-of-Things) forecasting. TopoBrick uses building knowledge graphs to construct a compact structural skeleton and employs an agentic topology sampler to select target-specific exogenous variables. The selected variables are organized by deployment-time availability, separating past-known sensor states from future-known calendar, schedule, and meteorological exogenous variables. Across three real-world buildings, TopoBrick outperforms strong zero-shot foundation-model baselines and remains competitive with fully trained building-specific models. Ablations show that topology-aware sampling is more reliable than random, ontology-only, or fixed-hop selection, especially for physically coupled HVAC and weather-driven sensing variables.

---


### 83. [VaseMuseum: Digital Intelligent Museum for Ancient Greek Pottery](https://arxiv.org/abs/2607.06374)

**<font color=#1a73e8>作者：</font>** Jiazi Wang, Nonghai Zhang, Qiushi Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have made interactive digital museums increasingly feasible by connecting 3D digitization with natural-language artifact exploration. However, in cultural heritage domains such as ancient Greek pottery, reliable VLM assistance is limited by two challenges. First, open-ended interpretation requires grounding fine-grained 2D/3D visual evidence in specialized curatorial knowledge, yet the retrieval process may introduce weak sources and unverifiable references. Second, when the available evidence is incomplete, noisy, or ambiguous, VLMs often produce confident but unsupported answers instead of calibrated uncertainty. To address these challenges, we propose VaseMuseum, a lightweight and modular multimodal agent framework for intelligent digital museums of ancient Greek pottery. VaseMuseum combines an interactive virtual museum with VaseAgent, which supports both 2D images and 3D artifacts through multimodal perception, 3D-aware reasoning, external knowledge retrieval, and inference-time reliability control. Specifically, VaseAgent retrieves evidence from authoritative web and museum knowledge sources, and source-level control selects diverse and verifiable evidence before generation. Meanwhile, response-level control checks generated claims against the evidence pool and encourages neutral, evidence-bounded answers when support is insufficient or conflicting. Moreover, a training-free GRPO-style selection mechanism favors responses with valid references and calibrated confidence without updating the VLM backbone. Experiments in a realistic digital museum simulation show that VaseMuseum improves citation validity, reduces hallucinations on knowledge-intensive queries, and produces more neutral answers under ambiguity compared with search-enabled VLM baselines.

---


### 84. [A Definition and Roadmap for World Models](https://arxiv.org/abs/2607.06401)

**<font color=#1a73e8>作者：</font>** Xinyuan Chen, Haoyu Guo, Shi Guo 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models -- internal simulators that learn the structure and dynamics of an environment -- have become one of the most actively debated concepts in AI. From model-based reinforcement learning and video generation to embodied robotics and ultimately, physical AI, researchers across AI subfields are building systems that they call "world models", yet there is no consensus on what a world model fundamentally is, what it should predict, or how it should be built. This perspective article provides a scientific definition of world models, discussions of their key technical aspects, and a staged roadmap for developing effective world models.

---


### 85. [What Images Cannot Say: Language-Guided Olfactory Representation Learning](https://arxiv.org/abs/2607.06402)

**<font color=#1a73e8>作者：</font>** Eleftherios Tsonis, Xi Wang, Vicky Kalogeiton  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Images tell us what a scene looks like, but rarely what it would feel like to be there. While recent datasets pair visual scenes with electronic-nose measurements, aligning smell signals with images remains challenging because many olfactory cues arise from contextual environmental factors that are not directly visible in pixels. We introduce SCENT, a multimodal framework that uses language guidance as a semantic bridge between vision and olfaction. Our approach leverages Vision-Language Models (VLMs) to generate scene descriptors capturing objects, environmental context, and plausible ambient smell cues suggested by the visual scene. These descriptors provide semantic guidance for learning olfactory representations. We train a smell encoder that maps electronic-nose signals into a shared embedding space aligned with both visual and textual representations, and introduce a languageguided latent decomposition that separates object-specific odors from contextual environmental contributions. Experiments on the New York Smells dataset demonstrate that SCENT significantly improves crossmodal retrieval compared to vision-only baselines, achieving state-of-theart performance on smell-to-image and smell-to-text retrieval tasks. In addition, our framework produces interpretable olfactory representations that enable the disentanglement of complex smell mixtures. Our results reveal the importance of contextual semantic information for grounding olfactory perception in multimodal learning and pave the way for future research in this area.

---


### 86. [HoloCount: A Holistic Visual Counting Benchmark for MLLMs](https://arxiv.org/abs/2607.06420)

**<font color=#1a73e8>作者：</font>** Jinhong Deng, Limeng Qiao, Guanglu Wan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual counting is a fundamental pillar of multimodal intelligence, requiring a seamless integration of fine-grained grounding and spatial reasoning. While Multimodal Large Language Models (MLLMs) have achieved remarkable success in qualitative scene understanding, their quantitative precision remains a significant bottleneck, often characterized by persistent numerical hallucinations. Existing counting benchmarks primarily focus on basic perception in simplified contexts, failing to capture the complex failure modes that emerge under logical constraints or adversarial conditions. To address these limitations, we introduce HoloCount, a holistic and diagnostically rich benchmark structured around a three-level hierarchical taxonomy. HoloCount evaluates MLLMs across: (1) Semantic Counting, focusing on atomic and property-based enumeration; (2) Analytical Counting, assessing logical composition through spatial and set-based reasoning; and (3) Robustness Testing, probing model integrity against adverse scenarios and grounded counter-priors, such as high-density scenes and linguistic biases. Through an exhaustive evaluation of over 20 state-of-the-art MLLMs, we reveal a critical performance gap: even top-tier models degrade significantly as tasks transition from perception to complex analytical reasoning and adverse scenarios. Our findings provide a systematic landscape of current MLLM counting capabilities and offer a roadmap for developing more grounded and reliable multimodal systems. The dataset is available at this https URL.

---


### 87. [From Voting to Agent Collaboration: Answer-Type-Aware LLM Pipelines for BioASQ 14b](https://arxiv.org/abs/2607.06452)

**<font color=#1a73e8>作者：</font>** Taeyun Roh, Eunha Lee, Wonjune Jang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical question answering requires not only accurate extraction of information from scientific literature but also reliable integration of evidence across multiple documents. This study presents a question-type-specific large language model (LLM) framework for BioASQ 14b Task B, designed to improve answer robustness and evidence grounding in biomedical question answering. Rather than applying a single prompting strategy to all questions, the framework selects different inference procedures for yes/no, factoid, and list questions according to their distinct reasoning and evaluation requirements. For yes/no questions, snippet shuffling and self-reflection are used to reduce sensitivity to evidence ordering and improve decision stability. For factoid questions, full-snippet input is combined with chain-of-thought-based in-context learning to support accurate biomedical entity identification. For list questions, a multi-agent architecture is employed, in which evidence extraction, candidate generation, answer verification, and final aggregation are handled collaboratively. Preliminary experiments on BioASQ 13b were used to identify effective inference strategies for each question type, and the resulting framework was subsequently evaluated in the official BioASQ 14b Task B challenge. In the official evaluation, our framework showed competitive performance across multiple batches and achieved first place in the factoid subtask of Batch 4. These results demonstrate the effectiveness of combining question-type-specific inference, ensemble prediction, and agent-based verification for reliable biomedical question answering.

---


### 88. [Data Analysis in the Wild: Benchmarking Large Language Models Against Real-World Data Complexities](https://arxiv.org/abs/2607.06482)

**<font color=#1a73e8>作者：</font>** So Hasegawa, Shailaja Keyur Sampat, Lei Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current benchmarks for evaluating Large Language Models (LLMs) in data analysis often fail to reflect real-world settings. They typically focus on fact retrieval from small tables and overlook the challenges of large multi-tabular datasets, external knowledge integration, and exploratory insight discovery. We introduce DataGovBench, a benchmark derived from governmental open data designed to evaluate LLMs in practical scenarios. The benchmark includes two tasks: Table QA that requires solving complex decomposable questions and producing textual answers or visualizations, and Table Insight that evaluates the ability of models to generate expert-level findings through exploratory data analysis. Comprehensive experiments with state-of-the-art LLMs, both with and without agentic frameworks, reveal significant performance gaps across both tasks. These results suggest that current LLM-based systems remain far from satisfying the demands of real-world data analytics. DataGovBench provides a challenging benchmark for advancing research on LLMs capable of both answering analytical queries and discovering insights from data. Code and sample data are available at this https URL.

---


### 89. [Mitigating Domain Shift in Conditioned Floor Plan Generation: Synthetic Pre-training for Data-Efficient Adaptation](https://arxiv.org/abs/2607.06483)

**<font color=#1a73e8>作者：</font>** Matthieu Ospici, Arnaud Gueze, Luc Bourrat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robustness to domain shift is a key requirement for floor plan generative models to be applicable beyond the single dataset they were trained on, as floor plans vary widely across regions due to distinct architectural cultures, spatial constraints, and construction practices, while acquiring new annotated datasets remains costly and domain-specific. Yet, no prior work has studied this robustness in the context of conditioned floor plan generation. In this paper, we evaluate state-of-the-art models from two fundamentally different generative paradigms across three public datasets (RPLAN, MagicPlan and Swiss Dwellings) and show that they are highly sensitive to domain shift, with up to an order of magnitude performance degradation when transferred across domains. To mitigate this with minimal target-domain supervision, we introduce a procedural method to generate a large-scale synthetic training dataset that enforces strict physical constraints (non-overlapping rooms, valid door placement, graph consistency) while intentionally sacrificing architectural realism through highly irregular spatial arrangements and aggressive geometric perturbation of room shapes. We show that pre-training on this synthetic data considerably improves zero-shot cross-domain performance, outperforming in-domain training on MagicPlan. Furthermore, it provides a highly effective initialization for fine-tuning, accelerating target domain adaptation and outperforming real-world initialization baselines by up to 40% in a low-data regime.

---


### 90. [AirflowAttack: Thermal-Airflow Adversarial Perturbations against Infrared Remote-Sensing Vision-Language Models](https://arxiv.org/abs/2607.06485)

**<font color=#1a73e8>作者：</font>** Cong Su, Jiaju Han, Xuemeng Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly deployed on infrared (IR) remote sensing imagery in security-critical settings, yet their adversarial robustness remains unexamined. We present AirflowAttack, to our knowledge the first adversarial attack for IR remote-sensing VLMs and the first to weaponize thermal-airflow turbulence as the perturbation prior. A lightweight generator synthesizes a single input-agnostic perturbation regularized toward physically plausible airflow patterns. Optimized on one surrogate CLIP model, it attains a mean zero-shot scene-classification attack success rate (ASR, the fraction of samples whose top-1 class changes) of 48.5% across five diverse CLIP backbones, far exceeding four IR-specific physical baselines (27.7--37.0%). Applied to six state-of-the-art VLMs, it cuts scene-classification accuracy by up to 38.2% relative, yet paradoxically makes some models more confident in their IR analysis, confabulating the perturbation as genuine thermal evidence such as temperature gradients and convection. Ablations show the airflow prior raises physical plausibility at no measurable cost to attack success. Together with a benchmark spanning eleven models and four tasks, these findings expose critical vulnerabilities in the rapidly expanding IR VLM ecosystem.

---


### 91. [Doomed from the Start: Early Abort of LLM Agent Episodes via a Recall-Controlled Probe Cascade](https://arxiv.org/abs/2607.06503)

**<font color=#1a73e8>作者：</font>** Kai Ruan, Zihe Huang, Ziqi Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents solving multi-step tasks frequently commit to trajectories that are doomed to fail, yet continue to consume substantial inference compute before the failure becomes observable. We show that failure is predictable early from the agent's internal representations: lightweight per-round probes on hidden activations anticipate eventual episode failure as early as the first interaction round, where scorers reading only the agent's observable behavior are barely better than chance. We turn this signal into a practical abort cascade: one distribution-free calibrated gate per round, with per-round recall budgets jointly searched so that eventually-successful episodes survive all gates at a user-specified global rate; this episode-level guarantee is the one that matters in deployment, since false-abort risk accumulates across gates. Across two agent models on TextCraft, the cascade meets every recall target from 90% to 97% and, at the 90% target, saves 47.1% +/- 10.3% (Qwen-2.5-7B) and 37.2% +/- 8.8% (Llama-3.2-3B) of inference compute, 1.6--1.7x the best single-gate policy. An otherwise-identical cascade reading only behavior saves roughly half as much, and adding behavioral features to the probe yields no further gain: the hidden states capture what behavior reveals. Finally, we characterize the sample complexity of certifying high recall targets, telling practitioners which recall promises their data can, and provably cannot, back. The code will be released soon.

---


### 92. [RMISC: A Large-scale Real-world Multivariate Corpus for Time Series Foundation Models](https://arxiv.org/abs/2607.06504)

**<font color=#1a73e8>作者：</font>** Qian Sun, Yong-Ming Tian, Jia-Wei Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed the emergence of multivariate modeling using time series foundation models (TSFMs), which achieve advanced zero-shot generalization. Modern multivariate TSFMs are predominantly pretrained on multivariate synthetic data, which is easier to scale but may fail to capture the complex temporal dynamics and cross-variable relationships present in real-world time series. This raises a key question: Whether and to what extent the leading TSFMs trained with the real-world corpus perform better than those trained with synthetic data? To answer this, we establish the RMISC corpus, a considerably large-scale, high-quality, openly accessible, real-world, and multivariate time series archive that contains around 200 datasets and 142 billion time points across diverse domains. Furthermore, we pretrain four advanced TSFMs on univariate, synthetic multivariate, and real-world multivariate data and evaluate their zero-shot generalization capabilities on standard in-distribution and out-of-distribution benchmarks. Experimental results show that incorporating real-world multivariate data predominantly improves the generalization performance for both univariate and multivariate TSFMs. These results provide a deeper understanding of how real-world multivariate data contributes to the development of stronger TSFMs.

---


### 93. [DynaKRAG: A Unified Framework for Learnable Evidence Control in Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/abs/2607.06507)

**<font color=#1a73e8>作者：</font>** Yaqi Wu, Xiaolei Guo, Chenyu Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-hop retrieval-augmented generation (RAG) acquires evidence sequentially, with each new document potentially revealing missing facts, bridge entities, query defects, or sufficient support for answering. Existing methods provide useful operations such as iterative retrieval, query reformulation, evidence critique, and sufficiency judging, but typically organize them within method-specific pipelines or predefined control topologies. This leaves underexplored how to learn a shared state-conditioned policy that chooses among currently valid evidence operations. We introduce DynaKRAG, which formulates multi-hop evidence acquisition as state-conditioned control over atomic evidence operations. At each step, a validity layer constructs the executable action set, and a learned controller selects the next operation. The resulting transition updates the evidence state and may enable new operations at subsequent steps. With Qwen2.5-7B-Instruct, DynaKRAG achieves F1 scores of 0.5998 on HotpotQA, 0.5340 on 2Wiki, and 0.3061 on MuSiQue, outperforming the strongest controlled baseline on all three benchmarks. Replacing the learned controller with a uniform-valid policy reduces F1 by 3.96--5.78 points, while removing sufficiency feedback hurts all three datasets. Controlled retrieval-cap experiments further show that additional retrieval is not uniformly beneficial. Together, these results demonstrate the benefit of coordinating retrieval, diagnosis, and gap-directed acquisition under an evolving evidence state.

---


### 94. [FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference](https://arxiv.org/abs/2607.06519)

**<font color=#1a73e8>作者：</font>** Anna Córdoba, Adam Puente Tercero, Nerea Angulo Hijo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context LLM inference is increasingly limited by the memory and bandwidth cost of KV caches, yet aggressive compression can remove the layer-specific evidence needed for retrieval and multi-step reasoning. We introduce FreqDepthKV, an inference-time cache compression method that factorizes adjacent-layer KV states into shared low-frequency depth components and sparse high-frequency residuals. A lightweight online probe assigns attention heads to shared-depth, residual-depth, or exact cache modes according to their contribution to reconstruction-sensitive attention logits, allowing the compression policy to adapt to prompt structure without retraining. Across long-context question answering, needle retrieval, summarization, and code generation benchmarks, FreqDepthKV preserves task accuracy under substantially smaller cache budgets. With a 32k-token prefill window, FreqDepthKV reaches 58.3 Exact Match, 63.0 F1, 32.5 ROUGE-L, and 48.1 pass@1, closely matching full KV while outperforming prior compressed-cache methods. It also improves decoding throughput to 70.4 tokens/s, reduces TTFT to 2.06 seconds, and lowers peak KV memory to 6.2 GB, achieving a 3.9x effective compression ratio.

---


### 95. [Bridging Physical Reasoning and Task Generalization via Visual Action Outcome Reasoning Alignment](https://arxiv.org/abs/2607.06522)

**<font color=#1a73e8>作者：</font>** Han-Jun Ko, Jr-Jen Chen, Haobo Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) struggle to generalize in interactive physical reasoning, particularly under unseen tasks and environments. Two key failure modes are prominent: hallucinated chain-of-thought (CoT) reasoning that contradicts physical reality, and misalignment between the model's reasoning and actions. We present VAORA (Visual Action Outcome Reasoning Alignment), a novel reward design that directly addresses both issues. VAORA introduces two complementary rewards: Visual Alignment Reward, which anchors VLM reasoning to the visual context independent of the agent action itself, and Visual-Action Alignment Reward, which grounds reasoning in the visual outcome induced by the model's action. Together, these rewards suppress hallucinated CoT and reduce the gap between reasoning and behavior. To improve training stability, we further employ smooth, dense rewards by estimating success probabilities using a pre-trained in-domain expert agent. Experiments on PHYRE and Virtual Tool support our performances across novel-task and unseen-environment settings, confirming that grounded and generalizable physical intelligence can be induced through VAORA.

---


### 96. [RSF-GLLM: Bridging the Semantic Gap in Multi-Hop Knowledge Graph QA via Recurrent Soft-Flow and Decoupled LLM Generation](https://arxiv.org/abs/2607.06527)

**<font color=#1a73e8>作者：</font>** Sambaran Bandyopadhyay, Ananth Muppidi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-hop Question Answering over Knowledge Graphs faces a critical challenge: traditional retrieve-then-read pipelines break differentiability, preventing the retriever from learning to bridge the semantic gap where intermediate nodes lack lexical overlap with the query. To address this, we propose RSF-GLLM, a framework decoupling differentiable graph reasoning from answer generation. Our Recurrent Soft-Flow (RSF) module employs a GRU-guided query updater to propagate continuous relevance scores, utilizing a dynamic gating mechanism to traverse semantically dissimilar bridge nodes via structural cues. We introduce flow sparsity regularization to theoretically guarantee convergence from soft probabilities to discrete reasoning paths. These paths are extracted and textualized to fine-tune a Large Language Model (LLM), ensuring generation is grounded in factual topology. Experiments on WebQSP and CWQ demonstrate that RSF-GLLM achieves competitive performance with superior inference efficiency compared to LLM based computationally expensive approaches.

---


### 97. [CAIRN: Cross-Room 3D Scene Understanding with Topology-Aware Large Multimodal Models](https://arxiv.org/abs/2607.06534)

**<font color=#1a73e8>作者：</font>** He Liang, Chenyang Ma, Yiming Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D scene-grounded Large Language Models (3D-LLMs) focus on answering questions grounded in simplified single-room 3D scenes, lacking the ability to reason over real-world household environments containing multiple interconnected rooms and diverse object categories. We introduce CAIRN, a topology-aware 3D-LLM for multi-room 3D scene understanding. CAIRN aligns transformer attention with scene hierarchy, giving the model explicit awareness of object-level relations and room-level connectivity. It enriches object tokens with room-local relational context via a graph neural network, introduces learned room tokens for room-level abstraction, and applies a hierarchical attention mask with geometric bias to route information according to scene topology. CAIRN is developed on CAIRN-MR, a benchmark we introduce on HM3D for multi-room 3D scene understanding, covering grounding, captioning, and four question-answering tasks that progressively evaluate from intra-room perception to cross-room reasoning. Experiments show that CAIRN outperforms prior 3D-LLMs by a large margin across all CAIRN-MR tasks while remaining competitive on five single-room benchmarks.

---


### 98. [Vision as Unified Multimodal Generation](https://arxiv.org/abs/2607.06560)

**<font color=#1a73e8>作者：</font>** Xiaoyang Han, Jianhua Li, Kewang Deng 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We formulate computer vision as unified multimodal generation, where heterogeneous visual tasks are expressed in the native text and image generation spaces of a unified multimodal model, without task-specific architectures. Under this formulation, SenseNova-Vision uses natural-language instructions and optional visual prompts to specify tasks, target regions or views, and decoding conventions, and generates responses as text for symbolic outputs, images for dense spatial predictions, or mixed text-and-image outputs for compositional tasks. To support large-scale training, we convert diverse computer vision annotations into instruction-response examples compatible with these generation spaces, resulting in the SenseNova-Vision Corpus, a computer-vision instruction-response corpus spanning text, image, and mixed targets. Starting from an off-the-shelf pretrained unified multimodal model, SenseNova-Vision is trained primarily on this corpus, with auxiliary multimodal data used as a capability-preserving mixture, and requires no task-specific prediction heads or architectural modifications. The resulting model covers a broad range of vision tasks, including detection, OCR, keypoint estimation, segmentation, depth estimation, surface normal prediction, point maps, and camera pose estimation, while supporting language-defined variants that combine category, color, region, and other visual cues. Experiments show that a single unified model can match leading task-specialized systems across structured visual understanding, dense geometric prediction, segmentation, and multi-view visual geometry. These results suggest unified multimodal generation as a scalable route for integrating computer vision capabilities into general-purpose foundation models. The model and corpus are publicly available.

---


> [!TIP]
> 当前位于：**51-98**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-98**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
