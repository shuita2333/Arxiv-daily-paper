# 🧠 大模型相关研究 | 2026年05月22日

> 本类共 **143** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-143](./part-03.md)

---

### 51. [Do No Harm? Hallucination and Actor-Level Abuse in Web-Deployed Medical Large Language Models](https://arxiv.org/abs/2605.20591)

**<font color=#1a73e8>作者：</font>** Sunday Oyinlola Ogundoyin, Muhammad Ikram, Rahat Masood  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical large language models (LLMs), including custom medical GPTs (MedGPTs) and open-source models, are increasingly deployed on web platforms to provide clinical guidance. However, they pose risks of hallucination, policy noncompliance, and unsafe design. We conduct a large-scale assessment of 6,233 MedGPTs, evaluating a stratified sample of 1,500, together with 10 open-source LLMs. We introduce two frameworks: MedGPT-HEval for hallucination detection and an LLM-based pipeline for assessing policy violations and developer intent. Our results show that 25-30% of MedGPTs exhibit low factual accuracy, with bottom- and middle-tier models at highest risk; 33.6-54.3% violate operational thresholds, and 57.06% of Action-enabled models lack adequate privacy disclosures. Compared with open-source models, MedGPTs achieve higher factual accuracy and semantic alignment, though open-source models are more stable. These results reveal systemic gaps in hallucination and compliance, highlighting the need for multi-metric evaluation and stronger safeguards. We release HAA-MedGPT, a structured dataset that supports future research on the safety of web-facing medical LLMs.

---


### 52. [Self-Training Doesn't Flatten Language -- It Restructures It: Surface Markers Amplify While Deep Syntax Dies](https://arxiv.org/abs/2605.20602)

**<font color=#1a73e8>作者：</font>** Ming Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Successive self-training on a language model's own outputs is widely characterized as a process of flattening: diversity drops, distributions narrow, and the text becomes "more like itself." We provide evidence that this characterization is incomplete. Across eleven generations of self-training on five models (GPT-2 124M, Pythia-410M, Pythia-1.4B, OPT-1.3B, Pythia-2.8B), language is not flattened uniformly -- it is restructured. Surface markers (discourse connectives, hedges, em-dashes) rise, while mid- and deep-syntactic structures (questions, parentheticals, passives, subjunctives) collapse. We formalize this asymmetric collapse as the Structural Depth Hypothesis (SDH): the per-generation decay rate of a linguistic feature is predicted primarily by its structural depth -- the number of nested syntactic dependencies it requires -- and only secondarily by its generation-zero output frequency. Pooling 17-feature panels from five models spanning three architecture families (N=85), the pooled Spearman correlation is rho=0.540 (p < 10^{-6}; cluster-bootstrap 95% CI [0.434, 0.634]), while frequency is a substantially weaker predictor (rho=0.225). A matched human-text fine-tuning control yields rho=0.039 (p=0.88), confirming the gradient is self-training-specific. We further document a Superficial Complexity Paradox: aggregate complexity proxies (dep-tree depth, TTR, word length) all rise as the underlying clause structure dies, with direct implications for training-data curation and LLM-text detection.

---


### 53. [Evaluating Temporal Semantic Caching and Workflow Optimization in Agentic Plan-Execute Pipelines](https://arxiv.org/abs/2605.20630)

**<font color=#1a73e8>作者：</font>** Alimurtaza Mustafa Merchant, Krish Veera, Sajal Kumar Goyla 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial asset operations workflows are latency-sensitive because a single user query may require coordination over sensor data, work orders, failure modes, forecasting tools, and domain-specific agents. We evaluate this problem on AssetOpsBench (AOB), an industrial agent benchmark whose plan-execute pipeline exposes repeated overhead from tool discovery, LLM planning, MCP tool execution, and final summarization. Existing LLM caching techniques such as KV-cache reuse and embedding-based semantic caching were designed for chatbot serving and break down when output validity depends on time, asset, or sensor parameters. We propose two complementary optimization layers for AOB plan-execute pipelines: a temporal semantic cache and a set of MCP workflow optimizations combining disk-backed tool-discovery caching and dependency-aware parallel step execution. MCP workflow optimizations corresponded to a 1.67x speedup and reduced median end-to-end latency by about 40.0% while the temporal-cache benchmark achieved a median of 30.6x speedup on cache hits. Beyond the speedup, our results expose a concrete failure mode of pure semantic caching for parameter-rich industrial queries, providing a critical analysis of how caching choices interact with evaluation correctness in MCP-backed agent benchmarks.

---


### 54. [Pareto-Enhanced Portrait Generation: Vision-Aligned Text Supervision for Alignment, Realism, and Aesthetics](https://arxiv.org/abs/2605.20640)

**<font color=#1a73e8>作者：</font>** Yunlong Wang, Jinjin Shi, Wenbin Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models often face a severe trilemma in human portrait generation: text-image alignment, photorealism, and human-perceived aesthetics inherently inhibit one another. Supervised Fine-Tuning (SFT) is an effective method for enhancing the photorealism of image generation. However, it often leads to overfitting to the training dataset, corrupts pre-trained image priors, and degrades alignment or aesthetics. To break this bottleneck, we propose a feature supervision paradigm for Multimodal Diffusion Transformers (MM-DiT). Specifically, we introduce a lightweight cross-modal alignment mechanism that implicitly extracts multi-granularity vision-aligned text representations from SigLIP 2 and applies supervision to the image branch of MM-DiT during the training stage, with zero extra inference overhead. Our method injects vision-aligned text guidance while preserving the base model's original generalization, avoiding degradation caused by SFT. Furthermore, our method directly mines implicit multi-granularity aesthetic signals from pre-trained vision foundation models to optimize human-perceived aesthetics. Extensive experiments on MM-DiTs show that our method pushes the Pareto frontier and achieves synergistic improvements across text-image alignment, photorealism, and human-perceived aesthetics.

---


### 55. [REFLECTOR: Internalizing Step-wise Reflection against Indirect Jailbreak](https://arxiv.org/abs/2605.20654)

**<font color=#1a73e8>作者：</font>** Jiachen Ma, Jiawen Zhang, Xiangtian Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) demonstrate remarkable capabilities, they remain susceptible to sophisticated, multi-step jailbreak attacks that circumvent conventional surface-level safety alignment by exploiting the internal generation process. To address these vulnerabilities, we propose Reflector, a principled two-stage framework that internalizes self-reflection within the generation trajectory. Reflector first leverages teacher-guided generation to produce high-quality reflection data for supervised fine-tuning (SFT), establishing structured reflection patterns. It subsequently uses Reinforcement Learning (RL) with outcome-driven and reward-validity supervision to instill robust, autonomous self-reflection capabilities. Empirical results show that Reflector achieves Defense Success Rates (DSR) exceeding 90% against complex indirect attacks while generalizing robustly across diverse threat scenarios. Notably, the framework enhances both task-specific and general utility, yielding a 5.85% gain on GSM8K alongside improved performance on knowledge-intensive benchmarks. By internalizing trajectory-level safety, Reflector overcomes the fundamental limitations of surface alignment without significant computational overhead, offering an efficient and scalable solution for the development of safe and capable LLMs.

---


### 56. [On the limits and opportunities of AI reviewers: Reviewing the reviews of Nature-family papers with 45 expert scientists](https://arxiv.org/abs/2605.20668)

**<font color=#1a73e8>作者：</font>** Seungone Kim, Dongkeun Yoon, Kiril Gashteovski 等 58 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the advancement of AI capabilities, AI reviewers are beginning to be deployed in scientific peer review, yet their capability and credibility remain in question: many scientists simply view them as probabilistic systems without the expertise to evaluate research, while other researchers are more optimistic about their readiness without concrete evidence. Understanding what AI reviewers do well, where they fall short, and what challenges remain is essential. However, existing evaluations of AI reviewers have focused on whether their verdicts match human verdicts (e.g., score alignment, acceptance prediction), which is insufficient to characterize their capabilities and limits. In this paper, we close this gap through a large-scale expert annotation study, in which 45 domain scientists in Physical, Biological, and Health Sciences spent 469 hours rating 2,960 individual criticisms (each targeting one specific aspect of a paper) from human-written and AI-generated reviews of 82 Nature-family papers on correctness, significance, and sufficiency of evidence. On a composite of all three dimensions, a reviewing agent powered by GPT-5.2 scores above each paper's top-rated human reviewer (60.0% vs. 48.2%, p = 0.009), while all three AI reviewers (including Gemini 3.0 Pro and Claude Opus 4.5) exceed the lowest-rated human across every dimension. AI reviewers' accurate criticisms are also more often rated significant and well-evidenced, and surface a distinct 26% of issues no human raises. However, AI reviewers overlap far more than humans do (21% vs. 3% for cross-reviewer pairs), and exhibit 16 recurring weaknesses humans do not share, such as limited subfield knowledge, lack of long context management over multiple files, and overly critical stance on minor issues. Overall, our results position current AI reviewers as complements to, not substitutes for, human reviewers.

---


### 57. [Modular Multimodal Classification Without Fine-Tuning: A Simple Compositional Approach](https://arxiv.org/abs/2605.20674)

**<font color=#1a73e8>作者：</font>** Herman Bergström, Aditya Mehrotra, Rahul G. Krishnan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce CoMET, \textit{\textbf{C}omposing \textbf{M}odality \textbf{E}ncoders with \textbf{T}abular foundation models}, a simple yet highly competitive method for multimodal classification: pass each modality through a frozen pre-trained backbone, compress the resulting embeddings with PCA, and concatenate as input into a Tabular Foundation Model (TFM) for prediction. We show that PCA alone suffices to act as an adaptor yielding strong, robust performance across modalities. When the \texttt{CLS} tokens of the foundation model align poorly with downstream tasks, we propose \textbf{PALPooling}, a lightweight adaptive token pooler that consistently improves representation quality. By composing strong frozen representation learning backbones with TFMs, our approach achieves state-of-the-art results across diverse multimodal benchmarks without any training. On hierarchical tasks with large fine-grained class spaces, our approach enables fast and scalable classification, handling datasets with over 500,000 samples and 2,000 classes without any fine-tuning. Overall, our results show that the composition of foundation models is a simple, yet powerful, out-of-the-box solution for multimodal learning, challenging the necessity of complex, end-to-end training pipelines for new problems.

---


### 58. [VISTAQA: Benchmarking Joint Visual Question Answering and Pixel-Level Evidence](https://arxiv.org/abs/2605.20676)

**<font color=#1a73e8>作者：</font>** Mozhgan Nasr Azadani, Yimu Wang, Yongpeng Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Establishing a clear link between model predictions and the visual evidence that supports them is critical for transparency and reliability in multimodal reasoning, yet current multimodal large language model (MLLM) evaluations do not explicitly enforce this alignment. Existing benchmarks assess either textual answer correctness or pixel-level localization in isolation, leaving the coupling of reasoning and grounding an open challenge. We introduce VISTAQA, a comprehensive benchmark for joint evaluation of free-form answer correctness and pixel-level evidence grounding in visual question answering. VISTAQA comprises 1,157 expert-curated samples spanning six task types and six visual domains, ranging from direct perception to compositional and relational reasoning. VISTAQA requires models to not only answer correctly, but to also provide precise segmentation masks that support their answers. It also includes hallucination-aware examples where no valid visual evidence exists. To support this enhanced evaluation, we introduce GROVE, a unified evaluation metric that enforces joint correctness by combining textual accuracy and grounding quality via a per-sample geometric mean, ensuring neither dimension can compensate for deficiencies in the other. Comprehensive experiments across grounding-aware models and hybrid pipelines with general-purpose MLLMs reveal that even the strongest systems achieve limited performance under GROVE, highlighting a substantial gap between answer accuracy and visual evidence alignment.

---


### 59. [Dynamic TMoE: A Drift-Aware Dynamic Mixture of Experts Framework for Non-Stationary Time Series Forecasting](https://arxiv.org/abs/2605.20678)

**<font color=#1a73e8>作者：</font>** Jiawen Zhu, Shuhan Liu, Di Weng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-stationary time series forecasting is challenged by evolving distribution shifts that static models struggle to capture. While Mixture-of-Experts (MoE) architectures offer a promising paradigm for decoupling complex drift patterns, existing approaches are limited by fixed expert pools and memoryless routing, hampering their ability to adapt to abrupt regime shifts. To address this, we propose Dynamic TMoE, a framework that unifies architectural evolution with temporal continuity during learning phase. By detecting distribution shifts via Maximum Mean Discrepancy (MMD), we dynamically instantiate heterogeneous experts and prune redundant ones to optimize capacity. Additionally, a temporal memory router leverages recurrent states and an anomaly repository to ensure stable, context-aware expert selection without requiring test-time updates. Experiments on nine benchmarks demonstrate state-of-the-art performance, reducing MSE by 10.4% and MAE by 7.8%. Code is available at this https URL.

---


### 60. [IndusAgent: Reinforcing Open-Vocabulary Industrial Anomaly Detection with Agentic Tools](https://arxiv.org/abs/2605.20682)

**<font color=#1a73e8>作者：</font>** Rongbin Tan, Fangfang Lin, Zhenlong Yuan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have shown remarkable capability in bridging visual perception and textual reasoning, enabling zero-shot understanding across diverse industrial scenarios. However, their performance in open-vocabulary industrial anomaly detection (IAD) is often limited by domain-misaligned reasoning and hallucinated structural inferences. To address these challenges, we propose \textbf{IndusAgent}, a tool-augmented agentic framework for open-vocabulary IAD. Specifically, we first construct \textbf{Indus-CoT}, a structured dataset that integrates global visual observations, high-resolution local patches, and expert normalcy priors, providing supervision for fine-tuning the model on rigorous industrial inspection trajectories. Building on this, IndusAgent dynamically orchestrates a set of external tools, including dynamic region cropping, high-frequency feature enhancement, and prior retrieval, thus enabling the agent to actively resolve visual ambiguities and disentangle subtle anomalies. Furthermore, we introduce a gated reinforcement learning objective that jointly optimizes anomaly classification, localization accuracy, anomaly type reasoning, and efficient tool usage, ensuring that tool invocation occurs only when beneficial. Extensive evaluations on five industrial anomaly benchmarks, including MVTec-AD, VisA, MPDD, DTD, and SDD, demonstrate that IndusAgent achieves state-of-the-art zero-shot performance among all existing methods, validating our robustness and generalization capacity.

---


### 61. [Declarative Data Services: Structured Agentic Discovery for Composing Data Systems](https://arxiv.org/abs/2605.20690)

**<font color=#1a73e8>作者：</font>** Shanshan Ye, Duo Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic discovery has shown that LLM-driven search can find novel algorithms, designs, and code under benchmark conditions. Translating the paradigm to multi-system data backends surfaces a harder problem: the search space is heterogeneous, the verifier is whether a deployed stack actually runs, and composition knowledge is unevenly captured in pretraining. Unbounded agentic discovery, a coding agent iterating on failure-log feedback, fails to converge consistently on a working stack even when iteration and explicit composition knowledge are added. We propose Declarative Data Services (DDS), an architecture for structured agentic discovery of data-system compositions from declarative user intent. The framework owns four typed contracts at successive layers (intent, operator DAG, per-system skills, runtime attribution) that decompose the global search into bounded sub-searches; sub-agents search each typed space, while the framework provides the channels by which knowledge flows forward as inline skill citations and errors route backward as typed signals. As a proof of life on a trading-backend workload, DDS converges where unbounded discovery does not; runtime failures become skill patches that the next deployment cites inline. We position this as an early prototype reporting lessons from real-world data-system composition.

---


### 62. [SAVER: Selective As-Needed Vision Evidence for Multimodal Information Extraction](https://arxiv.org/abs/2605.20713)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Shuhao Hu, Bokun Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal IE in social media is difficult because a post may attach multiple images that are weakly related, redundant, or even misleading with respect to the text. In this setting, always-on multimodal fusion wastes computation and can amplify spurious visual cues. The core challenge is to decide, for each candidate span or marked entity pair, whether vision should be consulted at all and, if so, which small subset of images provides trustworthy evidence.
We propose SAVER, a selective vision-as-needed framework for multimodal named entity recognition and multimodal relation extraction. SAVER uses a Conformal Groundability Gate (CGG) to estimate span-level visual groundability in MNER, derive pair-level activation in MRE from the two marked entities, and calibrate the activation threshold on a held-out split via a conformal-style procedure with Clopper--Pearson upper bounds. When activated, a submodular relevance--diversity selector chooses a compact evidence subset across images, which is then aggregated by a Set Transformer. An energy-inspired joint scoring head combines text, optional visual evidence, text--image consistency, and sparse routing for entity typing or relation classification.
Experiments show that SAVER consistently improves F1 over strong text-only and always-on multimodal baselines, while reducing AURC, increasing activation coverage at a fixed risk level, and lowering FLOPs and P90 latency.

---


### 63. [MTR-Suite: A Framework for Evaluating and Synthesizing Conversational Retrieval Benchmarks](https://arxiv.org/abs/2605.20729)

**<font color=#1a73e8>作者：</font>** Junhao Ruan, Abudukeyumu Abudula, Bei Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurate evaluation of conversational retrieval is pivotal for advancing Retrieval-Augmented Generation (RAG) systems. However, existing conversational retrieval benchmarks suffer from costly, sparse human annotation or rigid, unnatural automated heuristics. To address these challenges, we introduce MTR-Suite, a unified framework for auditing, synthesizing, and benchmarking retrieval. It features: (1) MTR-Eval, an LLM-based auditor quantifying alignment gaps in previous benchmarks; (2) MTR-Pipeline, a multi-agent system using greedy traversal clustering to generate high-fidelity dialogues at 1/400th human cost; and (3) MTR-Bench, a rigorous general-domain benchmark. MTR-Bench mimics production-style challenges (hard topic switching, verbosity), offering superior discriminative power. We make our code and data publicly available to facilitate future research at this https URL.

---


### 64. [Distributional Alignment as a Criterion for Designing Task Vectors in In-Context Learning](https://arxiv.org/abs/2605.20730)

**<font color=#1a73e8>作者：</font>** Jihoon Kwon, Jiwon Choi, Jy-yong Sohn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) allows large language models (LLMs) to adapt to new tasks through demonstrations, yet it suffers from escalating inference costs as context length increases. While task vectors offer a promising alternative by compressing demonstrations into compact hidden-state representations, their quality has been evaluated only through downstream task accuracy. This indirect criterion provides limited insight into how to design more effective task vector extraction methods. In this paper, we posit that inference using task vectors should align their predictive distribution with that of ICL. To quantify this, we introduce $d_{\text{NTP}}$, a metric that measures the discrepancy in next-token probabilities between task vector-based and ICL-based inference. Our empirical analysis reveals that $d_{\text{NTP}}$ serves as a performance proxy, exhibiting a strong negative correlation with downstream accuracy. Motivated by this, we develop Linear Task Vector (LTV), a method designed to minimize $d_{\text{NTP}}$ via a closed-form linear mapping that estimates demonstration effects through regression. Across eight classification benchmarks and five LLMs, LTV consistently outperforms existing task vector baselines, improving average accuracy by 9.2\% while reducing inference latency. We further show that LTV outperforms the baselines on regression tasks. Moreover, we investigate the transferability of LTV across different model scales; an aspect that has remained nascent in task vector research. Specifically, we empirically show that task vectors from a larger model can enhance a smaller model's performance by 6.4\%, suggesting a new utility for extracted task representations.

---


### 65. [STAR-IOD: Scale-decoupled Topology Alignment with Pseudo-label Refinement for Remote Sensing Incremental Object Detection](https://arxiv.org/abs/2605.20738)

**<font color=#1a73e8>作者：</font>** Yaoteng Zhang, Qing Zhou, Junyu Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing imagery typically arrives in the form of continuous data streams. Traditional detectors often forget previously learned categories when learning new ones; therefore, research on Remote Sensing Incremental Object Detection (RS-IOD) is of great significance. However, existing methods largely overlook the intra-class scale variations prevalent in remote sensing scenes, which undermines the effectiveness of knowledge transfer and old knowledge preservation. Moreover, RS-IOD also suffers from missing annotations, which cause the model to misclassify old-class instances as background. To address these challenges, we propose a novel framework, STAR-IOD. First, we introduce a Subspace-decoupled Topology Distillation (STD) module to transfer structural knowledge, explicitly aligning inter-class topological relationships and mitigating intra-class representation discrepancies induced by scale shifts. Furthermore, we introduce the Clustering-driven Pseudo-label Generator (CPG), a plug-and-play module that leverages K-Means clustering to dynamically identify class-specific thresholds, thereby guaranteeing an accurate distinction between true positive targets and background noise and alleviating the issue of missing annotations for old classes. We also constructed two Remote Sensing Incremental Object Detection datasets, DIOR-IOD and DOTA-IOD to facilitate research on RS-IOD. Extensive experiments demonstrate that our method outperforms state-of-the-art approaches by 1.7% and 2.1% mAP on DIOR-IOD and DOTA-IOD, respectively, effectively alleviating catastrophic forgetting while preserving strong detection performance on both base and novel classes. The code and dataset are released at: this https URL.

---


### 66. [Distribution-Aware Reward: Reinforcement Learning over Predictive Distributions for LLM Regression](https://arxiv.org/abs/2605.20740)

**<font color=#1a73e8>作者：</font>** Jungsoo Park, Hyungjoo Chae, Ethan Mendes 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can predict real-valued quantities from heterogeneous inputs such as text, code, and molecular strings, but most training objectives score each decoded floating-point number independently, improving point estimates without ensuring calibrated predictive distributions. This limits applications requiring candidate ranking or uncertainty estimation. We introduce Distribution-Aware Reward, an on-policy reinforcement learning objective whose main contribution is to train language models to produce better predictive distributions for regression tasks, rather than only optimizing individual decoded outputs against scalar targets. Our method treats multiple decoded samples as an empirical predictive distribution, evaluates it with the Continuous Ranked Probability Score, and assigns leave-one-out credit based on each rollout's marginal contribution to distribution quality, rewarding predictions that are both accurate and appropriately dispersed. We evaluate our method on a controlled Gaussian-mixture task, code performance prediction, and molecular property prediction from SMILES strings. Across tasks, our method improves over supervised fine-tuning and pointwise reinforcement learning baselines, with strong rank-correlation gains, including a 6-point Spearman improvement on KBSS. On MoleculeNet, it uses only SMILES strings yet remains competitive with strong graph-based and 3D molecular models. Further analyses show that our method mitigates rollout diversity collapse and improves uncertainty diagnostics, suggesting that directly optimizing predictive distributions makes language model regression more robust and better calibrated.

---


### 67. [Correcting Stochastic Update Bias in Preconditioned Language Model Optimizers](https://arxiv.org/abs/2605.20756)

**<font color=#1a73e8>作者：</font>** Nikhil Nayak, Julia White, Urchade Zaratiana 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preconditioned optimizers are central to language model training, but their stochastic update rules are usually treated as direct approximations to population preconditioned descent. We show that this view misses two finite-sample biases. First, the gradient and preconditioner are typically estimated from the same minibatch, introducing gradient--preconditioner coupling bias. Second, even when the preconditioner estimate is unbiased, its inverse or inverse-root is generally biased because inversion is nonlinear. We propose a single-batch bias-correction framework that addresses both effects: cross-fitted preconditioning estimates the numerator and preconditioner from independent microbatch groups, while variance-corrected inversion uses microbatch variability to subtract the leading delta-method bias term. The framework applies to diagonal moment, diagonal curvature, and matrix preconditioning methods, instantiated in AdamW, Sophia, and Shampoo. Bias correction reduces held-out pretraining loss on Qwen2.5-0.5B by $0.15$, $0.07$, and $0.11$ nats, respectively; the effects on mixed-quality pretraining and downstream instruction tuning are consistently neutral-to-positive. Together, these results establish bias correction as a practical mechanism for reducing finite-sample update bias and improving the performance of preconditioned optimizers.

---


### 68. [Findings of the Counter Turing Test: AI-Generated Text Detection](https://arxiv.org/abs/2605.20761)

**<font color=#1a73e8>作者：</font>** Rajarshi Roy, Gurpreet Singh, Ashhar Aziz 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of AI-generated text has introduced significant challenges in maintaining the integrity of digital content. Advanced generative models such as GPT-4, Claude 3.5, and Llama can produce highly coherent and human-like text, making it increasingly difficult to differentiate between human-written and AI-generated content. While these models have transformative applications, their misuse has raised concerns about misinformation, biased narratives, and security threats.
This paper provides a comprehensive analysis of state-of-the-art AI-generated text detection techniques and evaluates their effectiveness through the Counter Turing Test (CT2) shared tasks. Task A (Binary Classification) required participants to distinguish between human-written and AI-generated text, while Task B (Model Attribution) focused on identifying the specific language model responsible for generating a given text. The results demonstrated high performance in binary classification, with the top system achieving an F1 score of 1.0000, but significantly lower scores in model attribution, where the best system achieved 0.9531, highlighting the increased complexity of this task.
The top-performing teams leveraged fine-tuned transformer models, ensemble learning, and hybrid detection approaches, with DeBERTa-based and BART-based methods demonstrating strong results. However, the lower scores in Task B underscore the challenges of distinguishing outputs from different LLMs, necessitating further research into adversarial robustness, feature extraction, and cross-domain generalization.

---


### 69. [The Illusion of Intervention: Your LLM-Simulated Experiment is an Observational Study](https://arxiv.org/abs/2605.20767)

**<font color=#1a73e8>作者：</font>** Victoria Lin, Taedong Yun, Maja Matarić 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show potential as simulators of human behavior, offering a scalable way to study responses to interventions. However, because LLMs are trained largely on observational data, interventions in experiments with LLM-simulated synthetic users can induce unintended shifts in latent user attributes, causing user drift where the implicit simulated population differs across treatment conditions, potentially distorting effect estimates. We formalize the confounding or selection bias that can arise due to user drift and show how intervention-dependent shifts can inflate or attenuate observed differences in user responses under intervention. To diagnose confounding, we propose using negative control outcomes--attributes that should remain invariant under intervention--to identify distribution shifts across intervention conditions, providing evidence of user drift. To mitigate drift, we study adjusting the persona specification by eliciting additional confounders, finding that targeted, setting-relevant confounders can substantially reduce bias across survey-style and multi-turn agent evaluations.

---


### 70. [VIHD: Visual Intervention-based Hallucination Detection for Medical Visual Question Answering](https://arxiv.org/abs/2605.20772)

**<font color=#1a73e8>作者：</font>** Jiayi Chen, Benteng Ma, Zehui Liao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While medical Multimodal Large Language Models (MLLMs) have shown promise in assisting diagnosis, they still frequently generate hallucinated responses that appear linguistically plausible but lack visual evidence. Such hallucinations pose risks to clinical decision-making and necessitate effective detection. Existing introspective detection methods primarily perform uncertainty estimation or logical verification by analyzing model responses conditioned on original or perturbed inputs. However, such external perturbations are often heuristic and context-agnostic, which overlooks the internal cross-modal dependency between generated tokens and related visual tokens during decoding. To address this issue, we propose VIHD, a Visual Intervention-based Hallucination Detection method that leverages targeted visual token masking to calibrate semantic entropy for more effective hallucination detection. VIHD locates visually dominant decoder layers via Visual Dependency Probing (VDP), executes Visual Intervention Decoding (VID) via token masking to calibrate the semantic distribution, and quantifies the resulting Calibrated Semantic Entropy (CSE) as a reliable hallucination signal. Extensive experiments on three medical VQA benchmarks with two medical MLLMs demonstrate that VIHD consistently outperforms state-of-the-art methods, underscoring the importance of fine-grained visual dependency for hallucination detection. The code will be available at this https URL

---


### 71. [Learning to Think in Physics: Breaking Shortcut Learning in Scientific Diffusion via Representation Alignment](https://arxiv.org/abs/2605.20780)

**<font color=#1a73e8>作者：</font>** Haozhe Jia, Pengyu Yin, Wenshuo Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed diffusion models typically enforce PDE constraints only on final outputs, leaving intermediate representations unconstrained and prone to shortcut learning under shifted boundary conditions. We introduce **REPA-P**, a teacher-free, architecture-agnostic framework that aligns intermediate features with physical states using first-principles residuals. REPA-P attaches lightweight $1{\times}1$ projection heads to selected layers, decodes hidden activations into physical quantities, and applies PDE residual losses during training. These heads are discarded at inference, introducing **zero overhead**. Across four PDE tasks, including Darcy flow, topology optimization, electrostatic potential, and turbulent channel flow, REPA-P accelerates convergence by up to $2{\times}$, reduces physics residuals by up to $66.4\%$, and improves out-of-distribution robustness by up to $49.3\%$, with consistent gains on both U-Net and Diffusion Transformer backbones. Ablations show that supervising a small set of intermediate layers captures most benefits and complements output-level physics losses. Code is available at [this https URL](this https URL).

---


### 72. [Assessing socio-economic climate impacts from text data](https://arxiv.org/abs/2605.20793)

**<font color=#1a73e8>作者：</font>** Mariana Madruga de Brito, Brielen Madureira, Taís Maria Nunes Carvalho 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in natural language processing (NLP) and large language models (LLMs) have enabled the systematic use of large-scale textual data from news, social media, and reports to create datasets with socio-economic impacts of climate hazards such as floods, droughts, storms, and multi-hazard events. As the field of text-as-data for impact assessment expands, so does its methodological complexity. Yet research remains fragmented, with no clear guidelines for defining what constitutes an impact, handling temporal and spatial biases, and selecting appropriate modeling and post-processing strategies. This lack of coherence limits transparency and comparability across studies. Here, we address this gap by synthesising common practices, describing key challenges specific to the use of text-as-data methods for analyzing socio-economic impact data, and proposing recommendations to address them. By providing guidance on best practices, we aim to support the construction of robust text-derived socio-economic impact datasets that can more accurately inform disaster risk management and attribution studies.

---


### 73. [What Semantics Survive the Connector? Diagnosing VLM-to-DiT Alignment in Video Editing](https://arxiv.org/abs/2605.20795)

**<font color=#1a73e8>作者：</font>** Hangyu Lin, Chao Wen, Chengming Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching based video generative models have been increasingly relying on prepended Vision-Language Models (VLMs) to handle complex, instruction-based video editing. The prevailing assumption underlying this paradigm is that a connector module can seamlessly align the VLM's rich multi-modal reasoning with the original text embedding space of DiTs. However, we hypothesize that this alignment acts as a severe semantic bottleneck, degrading fine-grained structural variables. Verifying this is challenging, as end-to-end evaluations conflate alignment failures with generation errors, and natural datasets lack disentangled annotations. To rigorously investigate this, we propose a controlled data processing pipeline based on video composition that results in TRACE-Edit, a diagnostic dataset focusing on relation-based editing. Leveraging this dataset, we propose a comprehensive diagnostic protocol to analyze two important designs of meta-query and connector in the existing video editing models. Systematic evaluation of four representative model cases reveals that fine-grained structural semantics can be severely degraded during alignment. Our findings overturn the assumption of lossless semantic transfer, identifying the VLM-to-DiT alignment as a major bottleneck and providing a new diagnostic foundation for future multi-modal alignment architectures.

---


### 74. [OlmoEarth v1.1: A more efficient family of OlmoEarth models](https://arxiv.org/abs/2605.20804)

**<font color=#1a73e8>作者：</font>** Gabriel Tseng, Yawen Zhang, Favyen Bastani 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a set of improvements to the OlmoEarth family. These improvements allow us to cut compute costs during training ($1.7 \times$ reduction in GPU hours required to train our Base models) and inference ($2.9\times$ reductions in MACs on Sentinel-2 tasks), while maintaining the models' overall performance. All training code is available at this http URL.

---


### 75. [Spatial Gram Alignment for Ultra-High-Resolution Image Synthesis](https://arxiv.org/abs/2605.20808)

**<font color=#1a73e8>作者：</font>** Jinjin Zhang, Xiefan Guo, Di Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern ultra-high-resolution image synthesis relies heavily on the robust generative capacity of large-scale pre-trained Latent Diffusion Models (LDMs). While recent representation alignment methods have proven effective by distilling visual priors from foundation models (e.g., SAM or DINO) into generative latent features, scaling these approaches to pre-trained LDMs at extreme resolutions exposes a critical learnability-fidelity conflict. Specifically, forcing direct patch-wise feature distillation inherently perturbs the pre-trained latent manifold, ultimately leading to generation degradation. To address this bottleneck, we propose Spatial Gram Alignment (SGA), a novel framework that explicitly leverages the representation priors of vision foundation models while preserving the native generative capacity of LDMs. Moving beyond restrictive direct alignment, SGA imposes a non-invasive spatial constraint by aligning the internal self-similarities of the generative features with those of the foundation priors. This spatial constraint effectively establishes macroscopic structural coherence, while the native generative objectives retain the microscopic pixel-level fidelity inherent to the original LDMs. Notably, this versatile strategy integrates seamlessly across both intermediate diffusion features and VAE latents within pre-trained LDMs. Extensive experiments demonstrate that SGA achieves state-of-the-art performance for ultra-high-resolution text-to-image synthesis, yielding an effective reconciliation between global structural integrity and fine-grained visual details. Code is available at this https URL.

---


### 76. [Refining and Reusing Annotation Guidelines for LLM Annotation](https://arxiv.org/abs/2605.20809)

**<font color=#1a73e8>作者：</font>** Kon Woo Kim, Jin-Dong Kim, Akiko Aizawa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) demonstrate remarkable performance on zero-shot annotation tasks, they often struggle with the specialized conventions of gold-standard benchmarks. We propose the systematic reuse and refinement of annotation guidelines as an alignment mechanism, introducing an iterative moderation framework that simulates the early phases of annotation projects. We evaluate three hypotheses: (1) the efficacy of guideline integration, (2) the advantage of reasoning optimized models, and (3) the viability of moderation under minimal supervision. Testing across biomedical NER tasks (NCBI Disease, BC5CDR, BioRED) with three LLM families (GPT, Gemini, DeepSeek), our results empirically confirm all three hypotheses. While the iterative moderation framework shows good potential in effectively refining guidelines, our analysis also reveals substantial room for improvement.

---


### 77. [PulseCol: Periodically Refreshed Column-Sparse Attention for Accelerating Diffusion Language Models](https://arxiv.org/abs/2605.20813)

**<font color=#1a73e8>作者：</font>** Yanyi Lyu, Letian Chen, Futing Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Inference in diffusion large language models (dLLMs) is computationally expensive, as full self-attention must be repeatedly executed at each step of the denoising process without KV cache. Recent sparse attention methods for dLLMs mitigate this cost via block-sparse computation, which is applied only in later iterations when model performance is less sensitive to coarse-grained sparse approximation, but yields limited improvements in computational efficiency and acceleration. This motivates a finer-grained sparsification strategy that can be applied from earlier iterations and leverages reusable sparsity patterns, enabling further efficiency gains. In this work, we introduce PulseCol, a periodically refreshed column-sparse attention method for accelerating diffusion language models. PulseCol replaces coarse block-level sparsity with a finer-grained column-sparse structure, allowing important attention interactions to be retained more precisely while exposing greater sparsity. Built on this column-level formulation, PulseCol further identifies sparse patterns at the early denoising step and reuses them across subsequent iterations, refreshing them only at a small number of intermediate steps to track the evolution of sparse attention patterns during denoising. Experiments show that PulseCol achieves higher sparsity and greater practical speedup than prior sparse attention methods for dLLMs, while maintaining model quality. Enabled by optimized GPU kernels for column-sparse attention, PulseCol delivers up to 1.95$\times$ end-to-end speedup over FlashAttention across several context lengths.

---


### 78. [GraphRAG on Consumer Hardware: Benchmarking Local LLMs for Healthcare EHR Schema Retrieval](https://arxiv.org/abs/2605.20815)

**<font color=#1a73e8>作者：</font>** Peter Fernandes, Ria Kanjilal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph-based Retrieval Augmented Generation (GraphRAG) extends retrieval-augmented generation to support structured reasoning over complex corpora, but its reliability under resource-constrained, privacy-sensitive deployments remains unclear. In healthcare, where Electronic Health Record (EHR) data is complex and strictly regulated, reliance on cloud-based large language models (LLMs) introduces challenges in cost, latency, and compliance. In this work, we present a systematic evaluation of GraphRAG for EHR schema retrieval using locally deployed open-source LLMs. We implement the Microsoft GraphRAG pipeline on real-world EHR schema documentation and benchmark four models, including Llama 3.1 (8B), Mistral (7B), Qwen 2.5 (7B), and Phi-4-mini (3.8B), each deployed via Ollama on a single consumer GPU (8 GB VRAM). We evaluate indexing efficiency, knowledge graph construction, query latency, answer quality, and hallucination under both global and local retrieval modes. Our results reveal substantial differences: Llama 3.1 produces the richest knowledge graph (1,172 entities), Qwen 2.5 achieves the best answer quality (3.3/5), Phi-4-mini fails to complete the pipeline due to structured-output errors, and Mistral exhibits degenerate repetition behavior. We further show that GraphRAG exhibits a practical capacity threshold, where models below approximately 7B parameters fail to reliably produce valid structured outputs and cannot complete the pipeline. In addition, indexing and answer quality are decoupled across models, and local retrieval consistently outperforms global summarization in both latency and factual grounding, with reduced hallucination. These findings demonstrate that GraphRAG is feasible on consumer hardware while highlighting the importance of model selection and retrieval design for robust deployment in regulated settings.

---


### 79. [OSGNet with MLLM Reranking @ Ego4D Episodic Memory Challenge 2026](https://arxiv.org/abs/2605.20818)

**<font color=#1a73e8>作者：</font>** Yisen Feng, Leigang Qu, Haoyu Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this report, we present our champion solutions for the Natural Language Queries and GoalStep tracks of the Ego4D Episodic Memory Challenge at CVPR 2026. Both tracks require accurately localizing temporal segments from long untrimmed egocentric videos. To address these tasks, we propose a reranking-based framework that effectively leverages the strong video-language reasoning capability of multimodal large language model (MLLM) while preserving the efficiency and candidate recall of conventional localization pipelines. Specifically, we first obtain a set of candidate segments from existing localization model OSGNet, and then employ MLLM to select the segment that best matches the given query, thereby refining the final prediction. Ultimately, our method achieved first place in both the Natural Language Queries and GoalStep tracks. Our code can be found at this https URL.

---


### 80. [MemGym: a Long-Horizon Memory Environment for LLM Agents](https://arxiv.org/abs/2605.20833)

**<font color=#1a73e8>作者：</font>** Wujiang Xu, Yu Wang, Kai Mei 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory is a central capability for LLM agents operating across long-horizon tasks. Existing memory benchmarks predominantly evaluate retention of personalized information in multi-turn chat scenarios, overlooking the dynamic memory formation that occurs during extended agent execution. Consequently, the memory systems they produce transfer poorly to realistic agentic environments, such as coding and web navigation. We present MemGym, a benchmark for agentic memory that unifies existing agent gyms and in-house memory-grounded pipelines behind one memory-reasoning interface. MemGym spans five evaluation tracks grouped into four agentic regimes: tool-use dialogue (tau2-bench), multi-turn deep-research search (MEMGYM-DR), coding (SWE-Gym and MEMGYM-CODEQA), and computer use (WebArena-Infinity). MemGym reports memory-isolated scores that decouple memory performance from reasoning, retrieval, and tool-use ability, so memory strategies can be ranked without those confounders. Our synthetic pipelines for MEMGYM-CODEQA and MEMGYM-DR are length-controllable, ablation-verified at every stage, and tightly aligned with downstream scenarios. To make evaluation on coding environments academically tractable, we train MemRM, a lightweight reward model (Qwen3-1.7B fine-tuned with QLoRA) that scores compression quality as a fast scalar read in place of full Docker rollouts.

---


### 81. [Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment](https://arxiv.org/abs/2605.20834)

**<font color=#1a73e8>作者：</font>** Zhiqin Yang, Yonggang Zhang, Wei Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) has emerged as a popular alternative to Reinforcement Learning from Human Feedback (RLHF), offering theoretical equivalence with simpler implementation. We prove this equivalence is conditional rather than universal, depending on an implicit assumption frequently violated in practice: the RLHF-optimal policy must prefer human-preferred responses. When this assumption fails, DPO optimizes relative advantage over the reference policy rather than absolute alignment with human preferences, leading to pathological convergence where policies decrease DPO loss while preferring dispreferred responses. We characterize when this assumption is violated, show the existence of an undesirable solution space, and prove that DPO and RLHF optimize fundamentally different objectives in such cases. To address this, we introduce Constrained Preference Optimization (CPO), augmenting RLHF with constraints for provable alignment. We further provide a geometric interpretation through soft margin ranking, revealing that DPO implements margin ranking with potentially negative targets. Our theoretical analysis establishes when DPOs' guarantees hold and provides solutions preserving simplicity with provable alignment. Comprehensive experiments on standard benchmarks demonstrate that CPO achieves state-of-the-art performance. Code is available at: this https URL.

---


### 82. [ArchSIBench: Benchmarking the Architectural Spatial Intelligence of Vision-Language Models](https://arxiv.org/abs/2605.20837)

**<font color=#1a73e8>作者：</font>** Qirui Shen, Wenda Wang, Jiachen Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Architectural spatial intelligence, the ability to recognize and infer architectural space, is fundamental to tasks such as robot navigation, embodied interaction, and 3D scene understanding and generation. Although extensive research has evaluated the basic spatial skills of Vision-Language Models (VLMs) such as relative orientation, distance comparison, and object counting, these tasks cover only the most elementary levels of spatial cognition and largely overlook higher-level cognition of architectural space, including layout understanding, circulation patterns, and functional zoning. In this work, we present ArchSIBench, a Benchmark for Architectural Spatial Intelligence based on the perspectives from architecture, cognitive science, and psychology. ArchSIBench covers five core dimensions: perception, reasoning, navigation, transformation, and configuration, comprising 17 fine-grained subtasks. Through careful manual annotation by experts with architectural backgrounds, we construct 3,000 question-answer pairs to enable comprehensive evaluation of architectural spatial intelligence. Based on ArchSIBench, we evaluate various VLMs and find that the architectural spatial intelligence of most models shows significant differences from human baselines; additionally, models exhibit substantial variability across capability dimensions. Some state-of-the-art models can approach the level of human evaluators without architectural training. However, a clear gap remains compared to human evaluators with architectural training, particularly in spatial transformation and configuration reasoning. We believe that ArchSIBench will provide important insights and systematic resources for measuring and advancing the architectural spatial intelligence of VLMs. The dataset and code are available at this https URL.

---


### 83. [LOSCAR-SGD: Local SGD with Communication-Computation Overlap and Delay-Corrected Sparse Model Averaging](https://arxiv.org/abs/2605.20866)

**<font color=#1a73e8>作者：</font>** Yassine Maziane, Ammar Mahran, Artavazd Maranjyan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Communication is a major bottleneck in distributed learning, especially in large-scale settings and in federated learning environments with slow links. Three standard ways to reduce this cost are communication compression, local training, and communication-computation overlap. Methods that combine these ingredients are used in practice and have been found to be effective for large-scale training, but there is little theory for methods that combine all three. We study a heterogeneous-compute setting in which different workers may take different numbers of local steps, and we propose LOSCAR-SGD, a Local SGD method that communicates only a sparse subset of model coordinates and continues optimizing while communication is in flight. A key ingredient is a delay-corrected merge rule that incorporates delayed synchronized information without discarding the progress made during the overlap phase. We give convergence guarantees for smooth non-convex objectives and show how sparsity, overlap, and worker heterogeneity affect the rate. To the best of our knowledge, this is the first theory for this combination of ingredients. Experiments further show that communication-computation overlap reduces training time and that the delay-corrected merge outperforms naive overwriting.

---


### 84. [ProCrit: Self-Elicited Multi-Perspective Reasoning with Critic-Guided Revision for Multimodal Sarcasm Detection](https://arxiv.org/abs/2605.20867)

**<font color=#1a73e8>作者：</font>** Yingjia Xu, Jiulong Wu, Bowen Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multimodal sarcasm detection requires reasoning over cross-modal incongruities between literal expression and intended meaning, yet the specific analytical perspectives needed vary across samples due to the diversity of sarcastic mechanisms. While recent methods make this analytical process explicit, they still rely on fixed, predefined perspectives that operate independently under hand-crafted routing rules. We argue that multimodal sarcasm detection instead calls for self-elicited multi-perspective reasoning, where a model autonomously generates the perspectives needed for each sample and progressively integrates them into a coherent analysis. To realize this goal, we propose ProCrit, a Proposal-Critic two-agent framework with a proposal agent for multi-perspective reasoning and a critic agent for external evaluation and targeted revision guidance. First, to overcome the lack of process-level supervision in existing sarcasm datasets, ProCrit synthesizes process-level reasoning annotations through a dynamic-role agentic rollout: a strong vision-language model sequentially spawns analytical roles within a shared context, and the resulting multi-role trajectories are flattened into sequences that preserve cross-perspective dependencies while enabling efficient autoregressive generation. Second, to improve reasoning reliability, ProCrit adopts a draft-critique-revise paradigm in which an independent critic identifies reasoning deficiencies and provides targeted natural-language feedback for directed revision. Finally, we develop a mutual-refinement training framework that jointly optimizes proposal drafting and feedback-guided revision via dual-stage reinforcement learning, while refining the critic agent according to the actual effectiveness of its feedback. Experiments on three widely used benchmarks demonstrate the effectiveness of ProCrit.

---


### 85. [Runtime-Certified Bounded-Error Quantized Attention](https://arxiv.org/abs/2605.20868)

**<font color=#1a73e8>作者：</font>** Dean Calver  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV cache quantization reduces the memory cost of long-context LLM inference, but introduces approximation error that is typically validated only empirically. Existing systems rely on average-case robustness, with no mechanism to detect or recover from failures at runtime. We present a tiered KV cache architecture that enables runtime-certified attention: INT8 keys and INT4 values are stored in GPU memory, while FP16 originals are retained in system RAM for deterministic fallback. A two-term error decomposition yields per-head, per-step bounds on (i) attention distribution distortion from key quantization and (ii) value reconstruction error. These bounds are computed online and used to drive adaptive precision selection and a multi-stage fallback ladder, which guarantees recovery to the exact dense attention output when required. Across PG-19, NIAH, and RULER benchmarks on LLaMA~3.1-8B with contexts up to 128K, the system matches dense FP16 KV quality within noise for language modelling and retrieval tasks, while recovering catastrophic failures observed in naive INT8/INT4 baselines. Value-sensitive tasks at short context expose a controlled trade-off between compression and fidelity, which can be eliminated via tighter value tolerances or FP16-value fallback. The certification is local (per-head, per-step) and does not guarantee end-to-end model correctness, but ensures that each attention computation is either bounded relative to an FP16 reference or exactly recovered via fallback. This reframes KV cache quantization as a runtime-verified computation rather than a fixed approximation. The goal is not raw speedups, but enabling safe deployment of aggressive KV compression under strict quality constraints.

---


### 86. [PlanningBench: Generating Scalable and Verifiable Planning Data for Evaluating and Training Large Language Models](https://arxiv.org/abs/2605.20873)

**<font color=#1a73e8>作者：</font>** Ziliang Zhao, Zenan Xu, Shuting Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Planning is a fundamental capability for large language models (LLMs) because such complex tasks require models to coordinate goals, constraints, resources, and long-term consequences into executable and verifiable solutions. Existing planning benchmarks, however, usually treat planning data as fixed collections of instances rather than controllable generation targets. This limits scenario coverage, ties difficulty to surface-level proxies rather than structural sources, and offers limited support for scalable generation, automatic verification, or planning-oriented training. We introduce PlanningBench, a framework for generating scalable, diverse, and verifiable planning data for both evaluation and training. PlanningBench starts from real planning scenarios and abstracts practical workflows into a structured taxonomy of more than 30 task types, subtasks, constraint families, and difficulty factors. Guided by this taxonomy, a constraint-driven synthesis pipeline instantiates self-contained planning problems with adaptive difficulty control, quality filtering, and instance-level verification checklists. This shifts planning data construction from fixed benchmark collection to controllable generation while preserving realistic task grounding. We use PlanningBench to evaluate open-source and closed-source frontier LLMs, and find that current models still struggle to produce complete solutions under coupled constraints. Beyond evaluation, reinforcement learning on verified PlanningBench data improves performance on unseen planning benchmarks and broader instruction-following tasks. Further analysis suggests that determinate or well-specified optimal solutions provide clearer reward signals and more stable training dynamics. Overall, PlanningBench provides a controllable source of planning data for diagnosing and improving generalizable planning abilities in LLMs.

---


### 87. [Governance by Construction for Generalist Agents](https://arxiv.org/abs/2605.20874)

**<font color=#1a73e8>作者：</font>** Segev Shlomov, Iftach Shoham, Alon Oved 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise agents are increasingly expected to operate autonomously across tools and interfaces, yet production deployments require governance by construction. Systems must specify which actions are allowed, when human oversight is required, and what information may be exposed, without rebuilding the agent for each domain. This demo presents CUGA's policy system, a modular policy-as-code layer that composes with a generalist LLM agent to deliver predictable, auditable, and compliance-aware behavior in compound workflows without model fine-tuning. We present a runtime governance architecture that enforces policy interventions at every critical stage of execution. Rather than passively constraining behavior, policies intercept the agent at five structural checkpoints: upstream of planning (Intent Guard), within the system prompt to steer reasoning (Playbook), at the tool-call boundary to enforce proper usage (Tool Guide), outside the reasoning loop as a Human-in-the-Loop gate for high-risk actions (Tool Approvals), and at the output stage to filter and structure the final response (Output Formatter). Together, these stages embed governance continuously across the agent's execution pipeline rather than treating it as an afterthought. Using a healthcare scenario and a multi-layered enforcement intervention, the demo shows dynamic playbook injection for structured tool-sequence enforcement, intent guards that block malicious or accidental harmful requests, and human-in-the-loop tool approval checkpoints for potentially destructive actions. The artifact illustrates how typed governance primitives enable faster, safer deployment of enterprise agentic systems while improving policy adherence and execution consistency.

---


### 88. [HDMoE: A Hierarchical Decoupling-Fusion Mixture-of-Experts Framework for Multimodal Cancer Survival Prediction](https://arxiv.org/abs/2605.20891)

**<font color=#1a73e8>作者：</font>** Huayi Wang, Haochao Ying, Yuyang Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal survival prediction, a crucial yet challenging task, demands the integration of multimodal medical data (\eg Whole Slide Images (WSIs) and Genomic Profiles) to achieve accurate prognostic modeling. Given the inherent heterogeneity across modalities, the feature decoupling-fusion paradigm has emerged as a dominant approach. However, these methods have the following shortcomings: (1) fail to reduce the redundant information of modality features before decoupling, which negatively affects the feature decoupling and fusion effect;(2) lack the ability to model the fine-grained relationships of the features and capture the local information interactions between intra- and inter-modality features. To address these issues, we propose a \underline{H}ierarchical \underline{D}ecoupling-Fusion \underline{M}ixture-\underline{o}f-\underline{E}xperts (HDMoE) framework with two levels of MoE and \underline{R}andom \underline{F}eature \underline{R}eorganization (RFR) this http URL the first-level MoE, shared experts and routed experts are employed to remove redundant information and extract fine-grained specific features within each modality, while the second-level MoE facilitates fine-grained inter-modality feature decoupling. Besides, we design two RFR modules following each level of MoE to finely fuse intra- and inter-modality features, which can help the model capture more fine-grained relationships between modalities. Extensive experimental results on our private Liver Cancer (LC) and three TCGA public datasets confirm the effectiveness of our proposed method. Codes are available at this https URL.

---


### 89. [FruitEnsemble: MLLM-Guided Arbitration for Heterogeneous ensemble in Fine-Grained Fruit Recognition](https://arxiv.org/abs/2605.20892)

**<font color=#1a73e8>作者：</font>** Enhui Yu, Junhui Li, Ruitong Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained fruit classification is a critical yet challenging task in agricultural computer vision, primarily hindered by a severe shortage of high-quality datasets and the high visual similarity between classes. To address these challenges, we first constructed a comprehensive dataset comprising 306 fruit categories with 116,233 samples. Moreover, we propose FruitEnsemble, a practical two-stage dynamic inference framework designed to overcome the generalization limitations of static single-model architectures. In the first stage, FruitEnsemble employs a validation-calibrated weighted ensemble of heterogeneous backbones to generate a robust Top-3 candidate pool. To tackle difficult samples, we introduce an expert arbitration mechanism: when ensemble confidence falls below 0.6, a multimodal large language model (MLLM) is triggered to perform rigorous visual verification by integrating external botanical descriptions using Chain-of-Thought (CoT) reasoning. Furthermore, we optimized the training pipeline with a hard sample-aware joint loss. Extensive experiments demonstrate that FruitEnsemble achieves a classification accuracy of 70.49\% and outperforms existing state-of-the-art models. Our framework provides an efficient, deployment-oriented solution for real-world agricultural visual sorting and quality inspection tasks.

---


### 90. [RISE: Reliable Improvement in Self-Evolving Vision-Language Models](https://arxiv.org/abs/2605.20914)

**<font color=#1a73e8>作者：</font>** Chaoran Xu, Yingmao Miao, Pengfei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved strong multimodal reasoning capabilities, but further improving them still relies heavily on large-scale human-constructed supervision for post-training. Such supervision is costly to obtain, especially for reasoning-intensive multimodal tasks where questions, answers, and feedback signals must be carefully designed. This motivates self-evolving learning, where a model improves itself through a dual-role closed loop: a questioner autonomously poses questions and a solver learns to solve them. However, we observe that current VLM self-evolving methods still face three major challenges: coarse-grained role alternation delays the interaction between question generation and solver adaptation; generated questions can progressively degrade in quality; and question types may collapse toward a narrow distribution. These issues limit the efficiency and reliability of self-evolution. Thus, we propose \textbf{RISE}, a reliable self-evolving framework for vision-language models. RISE is built on three complementary designs: fine-grained role alternation, which shortens the feedback loop between the questioner and the solver to improve efficiency; a quality supervisor, which improves question validity and pseudo-label reliability; and skill-aware dynamic balancing, which mitigates mode collapse and maintains broad skill coverage during evolution. Together, these components enable more reliable and effective self-evolution from unlabeled images. Experiments on two VLM backbones across seven benchmarks show that RISE consistently improves the base models, yielding broad and sustained gains. Our code is publicly available at this https URL.

---


### 91. [Calibration vs Decision Making: Revisiting the Reliability Paradox in Unlearned Language Models](https://arxiv.org/abs/2605.20915)

**<font color=#1a73e8>作者：</font>** Divyaksh Shukla, Ashutosh Modi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove the influence of specific training data from a model while preserving reliable behavior on the remaining data, making reliable prediction and uncertainty estimation essential for evaluation. Calibration is commonly used as a proxy for reliability in language models, but low calibration error does not necessarily imply reliable decision rules, as models may rely on spurious correlations while remaining well calibrated. We investigate this gap in generative language models using the multiple-choice question-answering evaluation protocol on the TOFU benchmark, measuring probabilistic reliability with calibration metrics (ECE, MCE, Brier) and decision-rule reliability via attribution-based shortcut detection with Integrated Gradients and Local Mutual Information. We find that fine-tuned models achieve low calibration error (ECE ~ 0.04) compared to pretrained models (ECE > 0.5), and models after unlearning retain similarly low calibration despite reduced accuracy on the forget split, while attribution analysis shows increased reliance on correlation-based tokens. These results demonstrate that good calibration can coexist with shortcut-based decision rules after unlearning, extending the reliability paradox to the machine unlearning setting.

---


### 92. [Strategy-Induct: Task-Level Strategy Induction for Instruction Generation](https://arxiv.org/abs/2605.20924)

**<font color=#1a73e8>作者：</font>** Po-Chun Chen, Hen-Hsen Huang, Hsin-Hsi Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Designing effective task-level prompts is crucial for improving the performance of Large Language Models (LLMs). While prior work on instruction induction demonstrates that LLMs can infer better instructions with limited examples, existing approaches often rely on input-output pairs, where obtaining labeled answers can be difficult or costly. To address this limitation, we propose Strategy-Induct, a framework that derives task-level instructions solely from a small set of example questions without requiring labeled answers. Our approach first prompts the model to generate explicit reasoning strategies for each question, forming (strategy, question) pairs. These pairs are then used to induce a task instruction that guides reasoning. Experiments across multiple tasks and model scales demonstrate that Strategy-Induct outperforms state-of-the-art methods in question-only settings. Furthermore, we observe that jointly utilizing LLMs and Large Reasoning Models across task instruction generation and inference may lead to further performance improvements.

---


### 93. [Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory](https://arxiv.org/abs/2605.20948)

**<font color=#1a73e8>作者：</font>** Runxi Cheng, Yuchen Guan, Yongxian Wei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scaling conditional memory offers a promising way to increase language-model capacity, but existing methods such as Engram learn large memory tables from scratch during pre-training, making memory scaling expensive and sometimes ineffective. We propose Memory Grafting, a conditional memory scaling method that utilizes frozen hidden states from a grafting model as conditional n-gram memory. Given frequent local n-grams, we run the grafting model offline, store final-token hidden representations as memory values, and let the recipient model retrieve them through exact longest-match suffix lookup. Retrieved memories are adapted by lightweight projections and gates, while a hash-based Engram fallback preserves coverage for unmatched contexts. Since the grafting model is only run offline and exact lookup has expected O(1) complexity with respect to memory-bank size, Memory Grafting expands external latent capacity with limited training and inference overhead. Experiments under matched recipient architectures and pre-training budgets show that Memory Grafting improves over both MoE and vanilla Engram baselines. In the 2.8B-scale setting, it improves the average benchmark score from 51.95 for MoE and 52.43 for vanilla Engram to 53.86. In the 0.92B-scale setting, all grafting-model variants improve over the baselines, with Qwen3.5-35B-A3B giving the strongest gains. These results suggest that pretrained models can serve as reusable constructors of external latent memory, providing a practical step toward scaling future language models beyond trainable parameters alone.

---


### 94. [Focus-then-Context: Subject-Centric Progressive Visual Token Reduction for Vision-Language Models](https://arxiv.org/abs/2605.20950)

**<font color=#1a73e8>作者：</font>** Yulin Zhao, Yun Wang, Dehua Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) face a bottleneck of prohibitive computational costs arising from massive visual token sequences during inference. Existing vision token reduction methods alleviate this burden, but they unintentionally preserve the isolated visual subject strictly aligned with the user's query, which fails to substantially explore salient subjects and their contextual relationships. In this paper, we propose SPpruner, a subject-centric progressive reduction paradigm that emulates the \textit{Focus-then-Context} mechanism of the human visual perception system. Specifically, we first construct a focus identification module to explicitly model the interplay between visual saliency and semantic relevance. Herein, it can excavate the comprehensive visual subject spectrum to ensure a high-fidelity representation of visual input. Subsequently, a context-aware structural scanning module is developed to aggregate contextual cues from neighboring regions. As such, it can effectively restore global relational dependencies to uphold the structural integrity of the preserved subjects. Extensive experiments demonstrate that our paradigm consistently outperforms SOTA methods, achieving up to 2.53 times speedup with only 22.2% of visual tokens retained in Qwen2.5-VL and a 67% FLOPs reduction on LLaVA with a negligible 0.6% accuracy drop.

---


### 95. [Finding the Correct Visual Evidence Without Forgetting: Mitigating Hallucination in LVLMs via Inter-Layer Visual Attention Discrepancy](https://arxiv.org/abs/2605.20965)

**<font color=#1a73e8>作者：</font>** Yutong Xie, Zhenglin Hua, Ran Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have shown remarkable performance on a wide range of vision-language tasks. Despite this progress, they are still prone to hallucination, generating responses that are inconsistent with visual content. In this work, we find that LVLMs tend to hallucinate when they pay insufficient attention to the correct visual evidence and gradually forget it during the generation process. We empirically find that although LVLMs overall attend insufficiently to visual evidence, they exhibit sensitivity to the correct visual evidence in specific layers, with notable inter-layer discrepancy. Motivated by this observation, we propose a novel hallucination mitigation method that enhances visual evidence based on Inter-Layer Visual Attention Discrepancy (ILVAD). Specifically, we obtain the attention weights from early generated tokens to visual tokens across layers and identify the tokens that are repeatedly activated as visual evidence, forming a saliency map. We then enhance attention to visual evidence during generation through the saliency map to reduce visual forgetting. In addition, we leverage the saliency map to obtain attention scores of generated text to visual evidence, in order to select and emphasize text tokens that are strongly grounded in visual evidence. Our method is training-free and plug-and-play. Multiple benchmark evaluations conducted on five recently released models show that our method can consistently mitigate hallucinations in different LVLMs over various architectures. Code is available at this https URL.

---


### 96. [ArPoMeme: An Annotated Arabic Multimodal Dataset for Political Ideology and Polarization](https://arxiv.org/abs/2605.20967)

**<font color=#1a73e8>作者：</font>** Wajdi Zaghouani, Kais Attia, Md. Rafiul Biswas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memes have become a prominent medium of political communication in the Arab world, reflecting how humor, imagery, and text interact to express ideological and cultural positions. Despite the centrality of memes to online political discourse, there is a lack of systematically curated resources for analyzing their multimodal and ideological dimensions in Arabic. This paper presents ArPoMeme, a large-scale dataset of approximately 7,300 Arabic political memes categorized by ideological orientation, including Leftist, Islamist, Pan-Arabist, and Satirical perspectives. The dataset captures the diversity of Arabic meme ecosystems by grounding classification in the self-identification of public Facebook pages and groups that produce and disseminate these memes. To ensure both scale and accuracy, we designed a semi-automated data collection pipeline combining Playwright-based Facebook scraping with Google Drive synchronization, followed by text extraction using the Qwen2.5-VL-7B vision language model. The extracted text was manually verified and annotated for three polarization dimensions: Us vs. Them framing, Hostility toward out-groups, and Calls to action. Annotation was conducted through a custom Streamlit-based interface supporting distributed labeling, real-time tracking, and version control. The resulting dataset links visual content, textual messages, and ideological orientation, enabling fine-grained analysis of political antagonism, mobilization, and humor. Quantitative analysis of the annotated corpus reveals strong asymmetries in antagonistic framing across ideological groups, with Islamist and satirical memes exhibiting the highest levels of hostility and mobilization cues. The dataset and the annotation tool offers a reproducible and publicly available resource for studying Arabic political discourse, multimodal ideology detection, and polarization dynamics.

---


### 97. [Towards Context-Invariant Safety Alignment for Large Language Models](https://arxiv.org/abs/2605.20994)

**<font color=#1a73e8>作者：</font>** Yixu Wang, Yang Yao, Xin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Preference-based post-training aligns LLMs with human intent, yet safety behavior often remains brittle. A model may refuse a harmful request in a standard prompt but comply when the same intent is wrapped in adversarial wording. We suggest that robust safety requires context-invariant alignment, where behavior depends on the underlying intent rather than surface form. Enforcing invariance is difficult in alignment because not all training signals are equally trustworthy; for some prompt variants we can obtain verifiable feedback (e.g., multiple-choice), while for open-ended variants we typically rely on noisy, gameable reward proxies (e.g., learned judges). As a result, standard symmetric invariance regularizers can reduce cross-context discrepancies by lowering performance on reliable variants instead of improving open-ended robustness. To address this, we introduce Anchor Invariance Regularization (AIR), which treats verifiable prompts as anchors and uses a stop-gradient target to regularize only the open-ended variants toward the anchor performance. AIR is implemented as a plug-in auxiliary loss and combined with group-based preference optimization (e.g., GRPO) via heterogeneous prompt grouping. Across Safety, Moral Reasoning, and Math, AIR improves context invariance, boosting in-distribution group accuracy by 12.71% and out-of-distribution consistency by 33.49%, making safety constraints robust to adversarial framings.

---


### 98. [Beyond the Bellman Recursion: A Pontryagin-Guided Framework for Non-Exponential Discounting](https://arxiv.org/abs/2605.20996)

**<font color=#1a73e8>作者：</font>** Hojin Ko, Jeonggyu Huh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most value-based and actor--critic reinforcement learning methods rely on Bellman-style recursions, yet these recursions collapse under non-exponential discounting common in human preferences and survival processes. We show the breakdown is structural: exponential discounting sits at a fragile intersection of multiplicativity and time homogeneity, and violating either property breaks standard dynamic programming. To overcome this, we propose Pontryagin-Guided Direct Policy Optimization (PG-DPO), a variational framework that abandons recursion and couples the Pontryagin Maximum Principle with Monte Carlo rollouts via an Adjoint-MC projection enforcing pointwise Hamiltonian maximization. Across multi-dimensional hyperbolic and survival-discount benchmarks, PG-DPO improves accuracy and stability where equation-driven solvers and critic-based baselines diverge.

---


### 99. [Beyond Text-to-SQL: An Agentic LLM System for Governed Enterprise Analytics APIs](https://arxiv.org/abs/2605.21027)

**<font color=#1a73e8>作者：</font>** Gundeep Singh, Parsa Kavehzadeh, Jing Xia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise analytics aims to make organizational data accessible for decision-making, yet non-technical users still face barriers when using traditional business intelligence tools or Text-to-SQL systems. While recent Text-to-SQL approaches based on Large Language Models (LLMs) promise natural language access to structured data, they fall short in enterprise settings where analytics pipelines rely on governed APIs rather than raw databases. In practice, these APIs encapsulate complex business logic to ensure consistency, auditability, and security. However, delegating mathematical or aggregation logic to an LLM introduces reliability and compliance risks. To this end, we present Analytic Agent, an LLM-based agentic system that translates natural language intents into secure interactions with enterprise analytics APIs. Evaluated on 90 real enterprise use cases constructed by domain experts, it reliably interprets user goals, validates permissions, executes governed queries, and generates compliant visualizations through multi-step reasoning and policy-aware orchestration.

---


### 100. [The Quiet Path from Seemingly Minor Design Errors to Workplace AI Incidents](https://arxiv.org/abs/2605.21035)

**<font color=#1a73e8>作者：</font>** Julia De Miguel Velázquez, Sanja Šćepanović, Andrés Gvirtz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent human-computer interaction (HCI) research has revealed a widespread misalignment between how developers design workplace artificial intelligence (AI) systems, and what workers actually need from them. Yet, little research has examined the effects of this gap, or how it may cause harm. We analyzed 1,524 reports of incidents in which AI systems were used to perform 171 occupational tasks across 12 industry sectors. Using an Large Language Model (LLM)-as-an-expert approach, we extracted the main traits of the AI systems involved in those incidents using an established framework of twelve traits. We then compared them with the traits that 202 workers highly familiar with those tasks would have preferred. We found that as many as 83\% of workplace incidents stem from worker-AI misalignments. In most cases, workers wanted systems that are precise, insightful, or personal, but instead received systems that are basic, simple, or general. Over the years, fast AI caused a considerable number of incidents, yet these declined, and imaginative AI, with the mass introduction of generative AI, started to cause incidents. We also compared the traits causing the incidents with the traits that 197 developers building AI systems for those tasks would have preferred. If the traits causing the incidents were the same as those designed by developers, then developers may be responsible for those incidents. We found that 74\% of task misalignments could be attributed to developers who tended to overfocus on efficiency and speed, especially for systems performing tasks in people-facing occupations such as those in the human resources sector. Our results call for design interventions that better align AI development with workers' needs, as without such corrections, workplace AI incidents are likely to persist, causing the invisible erosion of worker agency and organizational productivity.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-143](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
