# 🧠 大模型相关研究 | 2026年05月06日

> 本类共 **203** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-203](./part-05.md)

---

### 51. [Colinearity Decay: Training Quantization-Friendly ViTs with Outlier Decay](https://arxiv.org/abs/2605.01330)

**<font color=#1a73e8>作者：</font>** Jin Tong, Guang Liang, Peilin Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-bit quantization is a practical route for efficiently deploying vision Transformers, yet activation outliers complicate fully quantized deployment. Existing methods either handle quantization post-training or suppress large activations during training; however, aggressively restricting outliers in vision models can lead to a poorer trade-off between full-precision and quantized accuracy. We argue that rather than simply suppressing outliers, the training objective should control the structural amplification that makes them harmful. To this end, we introduce Colinearity-Decay (CD), a structural regularizer for ordered matrix pairs within Transformer blocks. CD penalizes detrimental cross-matrix alignment and mitigates extreme activations without altering the architecture or task loss. Applied as a decoupled update, CD is non-invasive and introduces minimal training overhead. Across ImageNet-1K pre-training, COCO detection, and downstream fine-tuning, CD consistently boosts quantized accuracy across multiple pipelines while preserving, or even improving, full-precision performance. Ultimately, our results demonstrate that structural regularization effectively prepares vision Transformers for low-bit deployment with zero inference-time overhead.

---


### 52. [OralMLLM-Bench: Evaluating Cognitive Capabilities of Multimodal Large Language Models in Dental Practice](https://arxiv.org/abs/2605.01333)

**<font color=#1a73e8>作者：</font>** Rongyang Wang, Shuang Zhou, Jiashuo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have emerged as a promising paradigm for dental image analysis. However, their ability to capture the multi-level cognitive processes required for radiographic analysis remains unclear. Here, we present a comprehensive benchmark to evaluate the cognitive capabilities of MLLMs in dental radiographic analysis. It spans three critical imaging modalities, i.e., periapical, panoramic, and lateral cephalometric radiographs, and defines four cognitive categories: perception, comprehension, prediction, and decision-making. The benchmark comprises 27 clinically grounded tasks derived from public datasets, with manually curated annotations and 3,820 clinician assessments for evaluation. Six frontier MLLMs, including GPT-5.2 and GLM-4.6, are evaluated. We demonstrate the performance gap between MLLMs and clinicians in dental practice, delineate model strengths and limitations, characterize failure patterns, and provide recommendations for improvement. This data resource will facilitate the development of next-generation artificial intelligence systems aligned with clinical cognition, safety requirements, and workflow complexity in dental practice.

---


### 53. [DiagramNet: An End-to-End Recognition Framework and Dataset for Non-Standard System-Level Diagrams](https://arxiv.org/abs/2605.01338)

**<font color=#1a73e8>作者：</font>** Jincheng Lou, Ruohan Xu, Jiapeng Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> System-level diagrams encode the architectural blueprint of chip design, specifying module functions, dataflows, and interface protocols. However, non-standardized symbols and the scarcity of structured training data hinder existing multimodal large language models (MLLMs) from recognizing these diagrams. To address this gap, we introduce DiagramNet, the first multimodal dataset for system-level diagrams, comprising 10,977 connection annotations and 15,515 chain-of-thought QA pairs across four tasks: Listing, Localization, Connection, and Circuit QA. Building on this dataset, we propose a progressive training pipeline together with a decoupled multi-agent workflow that decomposes complex visual reasoning into Perception, Reasoning, and Knowledge stages. On the DiagramNet benchmark, integrating our 3B-parameter model with the proposed workflow surpasses the 2025 EDA Elite Challenge winner and outperforms GPT-5, Claude-Sonnet-4, and Gemini-2.5-Pro by over 2x in end-to-end evaluation. Notably, the workflow generalizes beyond our model, boosting Task 1 performance by 128.7x for Gemini-2.5-Pro and 12.4x for GPT-5. Furthermore, with only 60 images for detector adaptation, the method transfers effectively to AMSBench, achieving zero-shot connectivity reasoning on par with GPT-5 and Claude-Sonnet-4 while surpassing the AMS state-of-the-art method Netlistify.

---


### 54. [Active Reasoning Vision-Language Models via Sequential Experimental Design](https://arxiv.org/abs/2605.01345)

**<font color=#1a73e8>作者：</font>** Anjie Liu, Ziqin Gong, Yan Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual perception in modern Vision-Language Models (VLMs) is constrained by a fundamental perceptual bandwidth bottleneck: a broad field of view inevitably sacrifices the fine-grained details necessary for complex reasoning. Inspired by the classical paradigms of active vision and information foraging, we frame overcoming this limitation as a sequential decision-making process. We formalise this process through the lens of the sequential Bayesian optimal experimental design (S-BOED) problem. While exact Bayesian inference is intractable in continuous gigapixel spaces, we derive principled yet tractable approximations that balance spatial coverage against resolution. To validate this framework, we present a training-free inference strategy as a practical instantiation of the S-BOED objective for agents equipped with multiple vision tools. Designed as a flexible template, this strategy accommodates arbitrary optimisation algorithms, ranging from efficient greedy sampling to look-ahead planning, to approximate the optimal design. Empirical evaluations on gigapixel-level benchmarks demonstrate that our approach further boosts the performance of state-of-the-art models, significantly outperforming standard baselines and effectively narrowing the gap towards human-annotated oracles.

---


### 55. [LLM Output Detectability and Task Performance Can be Jointly Optimized](https://arxiv.org/abs/2605.01350)

**<font color=#1a73e8>作者：</font>** Koshiro Saito, Ryuto Koike, Masahiro Kaneko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting machine-generated text is essential for transparency and accountability when deploying large language models (LLMs). Among detection approaches, watermarking is a statistically reliable method by design -- it embeds detectable signals into LLM outputs by biasing their token distributions. However, it has been reported that watermarked LLMs often perform worse on downstream tasks. We propose PUPPET, a framework that fine-tunes an LLM via reinforcement learning to generate text that is both more detectable and better performing on downstream tasks. We use two reward functions: a detector that outputs a machine-class likelihood and an evaluator that measures a task-specific metric. Experiments on long-form QA, summarization, and essay writing show that LLMs trained with PUPPET achieve high detectability competitive with watermarking methods while outperforming them on downstream tasks. The analysis shows that this optimization can be performed efficiently with only a few thousand samples in 1--2 GPU hours. Moreover, these gains are consistent across out-of-domain tasks, different LLM families, and model sizes, and are even robust to paraphrasing attacks.

---


### 56. [Model-Based Proactive Cost Generation for Learning Safe Policies Offline with Limited Violation Data](https://arxiv.org/abs/2605.01356)

**<font color=#1a73e8>作者：</font>** Ruiqi Xue, Lei Yuan, Kainuo Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning constraint-satisfying policies from offline data without risky online interaction is crucial for safety-critical decision making. Conventional methods typically learn cost value functions from abundant unsafe samples to define safety boundaries and penalize violations. However, in high-stakes scenarios, risky trial-and-error is infeasible, yielding datasets with few or no unsafe samples. Under this limitation, existing approaches often treat all data as uniformly safe, overlooking safe-but-infeasible states - states that currently satisfy constraints but inevitably violate them within a few steps - leading to deployment failures. Drawing inspiration from the concept of knowledge-data integration, we leverage large language models (LLMs) to incorporate natural language knowledge into the policy to address this challenge. Specifically, we propose PROCO, a model-based offline safe reinforcement learning (RL) framework tailored to datasets largely free of violations. PROCO first learns a dynamics model from offline data and constructs a conservative cost function by grounding natural-language knowledge of unsafe states in LLMs, enabling risk estimation even without observed violations. Using the cost function and learned model, PROCO performs model-based rollouts to synthesize diverse counterfactual unsafe samples, supporting reliable feasibility identification and feasibility-guided policy learning. Across a range of Safety-Gymnasium tasks with exclusively safe or minimally risky training data, PROCO integrates seamlessly with a variety of offline safe RL algorithms and consistently demonstrates reduced constraint violations and improved safety performance compared to both the original methods and other behavior cloning baselines.

---


### 57. [VoxAfford: Multi-Scale Voxel-Token Fusion for Open-Vocabulary 3D Affordance Detection](https://arxiv.org/abs/2605.01365)

**<font color=#1a73e8>作者：</font>** Haowen Sun, Shaolong Zhang, Mingyang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D affordance detection requires localizing interaction regions on point clouds given novel affordance descriptions. Recent methods extend multimodal large language models (MLLMs) with special output tokens that are decoded into segmentation masks. However, these tokens are produced through autoregressive generation, which models sequential dependencies rather than spatial neighborhood relations, leaving them semantically rich but spatially impoverished for 3D localization. We propose Voxel-enhanced Affordance detection (VoxAfford), which bypasses this bottleneck by injecting multi-scale geometric features from a frozen pre-trained 3D VQVAE encoder into the output tokens after generation. Each output token uses its affordance semantics as a query to retrieve relevant geometric patterns from its paired voxel scale via cross-attention, with a learned compatibility gate controlling the injection strength. The enhanced tokens are then aggregated into a spatially-aware affordance prompt through semantic-conditioned attention and propagated alongside per-point features to generate the final mask. Experiments on open-vocabulary affordance detection tasks show that VoxAfford achieves state-of-the-art performance with approximately an 8% improvement in mIoU, and real robot experiments confirm zero-shot transfer to novel objects.

---


### 58. [Embedding-based In-Context Prompt Training for Enhancing LLMs as Text Encoders](https://arxiv.org/abs/2605.01372)

**<font color=#1a73e8>作者：</font>** Ailiang Lin, Zhuoyun Li, Keyu Mao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been widely explored for embedding generation. While recent studies show that in-context learning (ICL) effectively enhances the representational capability of LLMs by prepending a few task-related demonstrations, it causes substantial token overhead due to the increased sequence length. In this work, we propose EPIC, a novel embedding-based in-context prompt training strategy that leverages ICL to generate high-quality embeddings while reducing computational burden during both training and inference. This approach replaces discrete text demonstrations with their corresponding continuous embeddings, which not only encourages the LLM to align semantically-related text pairs during contrastive learning, but also requires the model to interpret demonstration embeddings as part of the in-context prompt. Consequently, EPIC-trained models achieve excellent embedding performance both with or without in-context prompts at inference time. Comprehensive experiments demonstrate that our method establishes new state-of-the-art results on the MTEB benchmark, surpassing frontier models trained solely on publicly available retrieval data. Extensive ablation studies further validate the effectiveness and necessity of our mechanism.

---


### 59. [Focus on the Core: Empowering Diffusion Large Language Models by Self-Contrast](https://arxiv.org/abs/2605.01373)

**<font color=#1a73e8>作者：</font>** Jinyuan Feng, Xin Yu, Yiqun Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The iterative denoising paradigm of Diffusion Large Language Models (DLMs) endows them with a distinct advantage in global context modeling. However, current decoding strategies fail to leverage this capability, typically exhibiting a local preference that overlooks the heterogeneous information density within the context, ultimately degrading generation quality. To address this limitation, we systematically investigate high-information-density (HD) tokens and present two key findings: (1) explicitly conditioning on HD tokens substantially improves output quality; and (2) HD tokens exhibit an early-decoding tendency, converging earlier than surrounding tokens. Motivated by these findings, we propose Focus on the Core \textbf{(FoCore)}, a training-free decoding strategy that utilizes HD tokens in a self-contrast manner, wherein HD tokens are temporarily remasked as negative samples, to guide generation. We further introduce FoCore\_Accelerate \textbf{(FoCore\_A)}, an efficient variant that, upon detecting HD token convergence, performs parallel decoding over stable candidates within a local context window, substantially accelerating generation. Extensive experiments on math, code and logical reasoning benchmarks demonstrate that FoCore consistently improves generation quality and efficiency across both LLaDA and Dream backbones. For instance, on HumanEval, FoCore improves pass@1 from 39.02 to 42.68 over standard Classifier-Free Guidance, while FoCore-A reduces the number of decoding steps by 2.07x and per-sample latency from 20.76s to 8.64s (-58.4\%).

---


### 60. [MTA: Multi-Granular Trajectory Alignment for Large Language Model Distillation](https://arxiv.org/abs/2605.01374)

**<font color=#1a73e8>作者：</font>** Pham Khanh Chi, Quoc Phong Dao, Thuat Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation is a key technique for compressing large language models (LLMs), but most existing methods align representations at fixed layers or token-level outputs, ignoring how representations evolve across depth. As a result, the student is only weakly guided to capture the teacher's internal relational structure during distillation, which limits knowledge transfer. To address this limitation, we propose Multi-Granular Trajectory Alignment (MTA), a framework that aligns teacher and student representations along their layer-wise transformation trajectory. MTA adopts a layer-adaptive strategy: lower layers are aligned at the word level to preserve lexical information, while higher layers operate on phrase-level spans (e.g., noun and verb phrases) to capture compositional semantics. We instantiate this idea through a Dynamic Structural Alignment loss that matches the relative geometry among semantic units within each layer. This design is motivated by empirical findings that Transformer representations become increasingly abstract with depth, and is also consistent with linguistic views in which higher-level meaning emerges through the composition of lower-level lexical units. We further incorporate a Hidden Representation Alignment loss to directly align selected teacher-student layers. Experiments show that MTA consistently outperforms state-of-the-art baselines on standard benchmarks, with ablations confirming the contribution of each component.

---


### 61. [MemORAI: Memory Organization and Retrieval via Adaptive Graph Intelligence for LLM Conversational Agents](https://arxiv.org/abs/2605.01386)

**<font color=#1a73e8>作者：</font>** Hung Pham Van, Nguyen Manh Hieu, Khang Pham Tran Tuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) lack persistent memory for long-term personalized conversations. Existing graph-based memory systems suffer from information dilution, absent provenance tracking, and uniform retrieval that ignores query context. We introduce MemORAI (Memory Organization and Retrieval via Adaptive Graph Intelligence), a framework that integrates three innovations: selective memory filtering with dual-layer compression to retain user-persona-relevant content, a provenance-enriched multi-relational graph tracking factual origins at the turn level, and query-adaptive subgraph retrieval with Dynamic Weighted PageRank that applies query-conditioned edge weighting. Evaluated on LOCOMO and LongMemEval benchmarks, MemORAI achieves state-of-the-art performance in memory retrieval and personalized response generation, demonstrating that selective storage, enriched representation, and adaptive retrieval are essential for coherent, personalized LLM agents.

---


### 62. [Verbal-R3: Verbal Reranker as the Missing Bridge between Retrieval and Reasoning](https://arxiv.org/abs/2605.01399)

**<font color=#1a73e8>作者：</font>** Sangkwon Park, Donghun Kang, Jisoo Mok 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The conventional Retrieval-Augmented Generation (RAG) paradigm of injecting raw retrieved texts into the Large Language Model (LLM)'s context often results in suboptimal integration of retrieved information. This paper proposes to bridge retrieval results and the LLM's reasoning ability through Verbal Annotations, analytic narratives that explicitly articulate the logical connection between a search query and retrieved contexts. Our empirical investigation reveals the potential of Verbal Annotations to substantially enhance the LLM's ability to generate accurate, contextually-grounded responses. Motivated by this finding, we introduce Verbal-R3, a novel agentic RAG framework that consists of a Generator and a Verbal Reranker. The Generator performs iterative retrieval and reasoning, while the Verbal Reranker returns relevance scores and Verbal Annotations to guide the reasoning and answering process of the Generator. The inference process of Verbal-R3 is further refined through relevance-guided test-time scaling, which efficiently allocates test-time compute for effective trajectory expansion. Verbal-R3 achieves state-of-the-art performance on complex Question Answering benchmarks, validating the effectiveness of the proposed framework.

---


### 63. [Injecting Distributional Awareness into MLLMs via Reinforcement Learning for Deep Imbalanced Regression](https://arxiv.org/abs/2605.01402)

**<font color=#1a73e8>作者：</font>** Yao Du, Shanshan Li, Xiaomeng Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) struggle with numerical regression under long-tailed target distributions. Token-level supervised fine-tuning (SFT) and point-wise regression rewards bias learning toward high-density regions, leading to regression-to-the-mean behavior and poor tail performance. We identify the lack of cross-sample relational supervision as a key limitation of existing MLLM training paradigms. To address it, we propose a distribution-aware reinforcement learning framework based on Group Relative Policy Optimization, which introduces batch-level comparison-based supervision via the Concordance Correlation Coefficient-based reward to align predicted and ground-truth distributions in terms of correlation, scale, and mean. The framework is plug-and-play, requiring no architectural modification. Experiments on a unified suite of long-tailed regression benchmarks show consistent improvements over SFT and existing MLLM regression methods, with particularly strong gains in medium- and few-shot regimes.

---


### 64. [Medmarks: A Comprehensive Open-Source LLM Benchmark Suite for Medical Tasks](https://arxiv.org/abs/2605.01417)

**<font color=#1a73e8>作者：</font>** Benjamin Warner, Ratna Sagari Grandhi, Max Kieffer 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) for medical applications remains challenging due to benchmark saturation, limited data accessibility, and insufficient coverage of relevant tasks. Existing suites have either saturated, heavily depend on restricted datasets, or lack comprehensive model coverage. We introduce Medmarks, a fully open-source evaluation suite with 30 benchmarks spanning question answering, information extraction, medical calculations, and open-ended clinical reasoning. We perform a systematic evaluation of 61 models across 71 configurations using verifiable metrics and LLM-as-a-Judge. Our results show that frontier reasoning models (Gemini 3 Pro Preview, GPT-5.1, & GPT-5.2) achieve the highest performance across both benchmarks, most frontier proprietary models are significantly more token efficient than open-weight alternatives, medically fine-tuned models outperform their generalist counterparts, and that models are susceptible to answer-order bias (particularly smaller models and Grok 4). A subset of our evals (Medmarks-T) can be directly used as reinforcement learning environments to post-train LLMs for medical reasoning. Code is available at this https URL

---


### 65. [Quantifying Multimodal Capabilities: Formal Generalization Guarantees in Pairwise Metric Learning](https://arxiv.org/abs/2605.01424)

**<font color=#1a73e8>作者：</font>** Richeng Zhou, Xuelin Zhang, Liyuan Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal learning leverages the integration of diverse data modalities to enhance performance in complex tasks. Yet, it frequently encounters incomplete or redundant modality data in real-world scenarios. This paper presents a fine-grained theoretical analysis of the generalization properties of multimodal metric learning models, addressing critical gaps in understanding the relationship between modality selection and algorithmic performance. We establish hierarchical relationships between function classes corresponding to different modality subsets and quantify the discrepancy between learned mappings and ground truth. Through rigorous analysis of pairwise complexity within the multimodal learning framework, we derive novel generalization error bounds that reveal the joint impact of modality quantity and granularity on model performance. Our theoretical findings on both upper and lower bounds demonstrate that incorporating fine-grained modality features reduces the complexity of the hypothesis space by enhancing modality complementarity. This work offers both theoretical foundations and practical implications for improving convergence rates and accuracy in multimodal learning systems.

---


### 66. [Artificial intelligence language technologies in multilingual healthcare: Grand challenges ahead](https://arxiv.org/abs/2605.01441)

**<font color=#1a73e8>作者：</font>** Vicent Briva-Iglesias  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI language technologies (AILTs), increasingly enabled by large language models (LLMs), are becoming embedded in multilingual healthcare workflows for translation, rewriting, documentation, interpreting, and messaging in language-discordant settings. Yet fluent output is not the same as clinically safe or equitable communication: performance varies across languages, accents, tasks, and workflows, and efficiency gains can hide errors, reduce traceability, and shift responsibility across clinicians, translators, interpreters, and health systems. This narrative review synthesises recent peer-reviewed evidence across written communication, spoken communication, and emerging agentic workflows. Using the Human-Centered AI Language Technology (HCAILT) lens, it examines capabilities, evaluation practices, implementation patterns, and recurrent errors through reliability, safety culture, and trustworthiness. We identify key convergences and contradictions in the literature and propose seven grand challenges for the next phase of research and deployment. Progress, we argue, requires not only better models but also accountable sociotechnical design, calibrated human oversight, and stronger collaboration across MT/NLP, translation studies, HCI, clinical practice, implementation science, and policy.

---


### 67. [Auditing demographic bias in AI-based emergency police dispatch: a cross-lingual evaluation of eleven large language models](https://arxiv.org/abs/2605.01451)

**<font color=#1a73e8>作者：</font>** William Guey, Wei Zhang, Pierrick Bougault 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are rapidly being integrated into high-stakes public safety systems, including emergency call triage and dispatch decision support, yet their demographic fairness in this context remains largely untested. Here we introduce a cross-lingual audit framework that operationalizes the Police Priority Dispatch System as a five-level ordinal classification task and applies a controlled minimal-pair design to isolate the effect of demographic cues. Across 19,800 model outputs spanning 11 frontier models, 15 scenario pairs, three demographic categories (religious appearance, gender, and race), and two languages (English and Mandarin Chinese), we find that demographic bias emerges systematically when incident severity is ambiguous but largely disappears when the operational priority is clearly determined by call content. Bias magnitude varies by demographic axis, with the largest effects observed for religious appearance, followed by gender and race. Critically, bias does not transfer consistently across languages: gender bias is substantially amplified in Mandarin Chinese, whereas race bias is more pronounced in English, revealing cross-lingual asymmetries that aggregate analyses obscure. In several scenarios, demographic cues produce counter-directional effects, challenging simple stereotype-amplification accounts of model behavior. These findings suggest that bias in LLM-based dispatch is not a fixed property of models alone, but arises from the interaction between demographic signals, contextual ambiguity, and language. Beyond these empirical results, the proposed framework provides a scalable audit infrastructure that enables deploying agencies to evaluate candidate models on jurisdiction-relevant scenarios prior to real-world adoption.

---


### 68. [Evaluating LLMs on Large-Scale Graph Property Estimation via Random Walks](https://arxiv.org/abs/2605.01484)

**<font color=#1a73e8>作者：</font>** Sunil Kumar Maurya, Xin Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the rapidly improving reasoning abilities of Large Language Models (LLMs), there is also a rising demand to use them in a wide variety of domains. This brings about the need to carefully evaluate the limits of the capabilities of these models with various tests and benchmarks. Graph structures are ubiquitous in real-world data, and are often used to represent and analyze relationship patterns within data. Many benchmarks have already been proposed in the graph literature to test the reasoning ability of LLMs to follow and execute graph algorithms. However, due to the limited context length of LLMs, these benchmarks consist of very small graphs. In real-world data, the size of graphs can be significantly larger, and in many cases, not fully accessible. In this paper, we examine a class of problems that arises with very large graphs having limited accessibility. We propose a large graph benchmark dataset, EstGraph, and introduce four distinct tasks designed to estimate large graph properties. We evaluate the reasoning abilities of LLMs on these tasks using a wide variety of graph datasets. In addition, we provide task-specific prompt constructions based on random walk sampling of large graphs (up to millions of nodes) that effectively convey sufficient information to LLMs within the limits of context length.

---


### 69. [MAP-Law: Coverage-Driven Retrieval Control for Multi-Turn Legal Consultation](https://arxiv.org/abs/2605.01486)

**<font color=#1a73e8>作者：</font>** Qinchuan Cheng, Ruixuan Xie, Jiaqi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Legal consultation is a high-stakes, knowledge-intensive task that requires agents to identify relevant legal issues, retrieve authoritative support, and determine when evidence is sufficient for a recommendation. Although retrieval-augmented generation has improved grounding in legal question answering, many multi-turn legal agents still rely on fixed retrieval depth or coarse heuristic control. This often leads to either insufficient support for key legal elements or excessive retrieval that increases context burden and weakens answer focus.
We propose MAP-Law, a coverage-driven framework for retrieval control in multi-turn legal consultation. MAP-Law models consultation as a controlled retrieval process over a joint structured state consisting of issue nodes, legal element nodes, and evidence nodes. After each retrieval round, the agent computes Element Coverage, Evidence Coverage, and Marginal Gain, and uses these signals to decide whether to continue retrieval, redirect the search, or generate the final response. In this way, MAP-Law turns stopping from a fixed hyperparameter into an interpretable and auditable decision aligned with legal argumentative structure.
Experiments on a self-constructed dataset of 50 cases across eight labor-law scenarios show that MAP-Law with DeepSeek as the action selector achieves an Element Coverage of 0.860 using only 2.9 retrieval rounds and 5.8 evidence pieces on average. Compared with a fixed seven-round baseline, it reduces evidence volume by over 80% and retrieval rounds by 58%. Ablation results further confirm the independent contributions of coverage-driven stopping, joint graph representation, and LLM-based action selection.

---


### 70. [SciResearcher: Scaling Deep Research Agents for Frontier Scientific Reasoning](https://arxiv.org/abs/2605.01489)

**<font color=#1a73e8>作者：</font>** Tianshi Zheng, Rui Wang, Xiyun Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier scientific reasoning is rapidly emerging as a key foundation for advancing AI agents in automated scientific discovery. Deep research agents offer a promising approach to this challenge. These models develop robust problem-solving capabilities through post-training on information-seeking tasks, which are typically curated via knowledge graph construction or iterative web browsing. However, these strategies face inherent limitations in frontier science, where domain-specific knowledge is scattered across sparse and heterogeneous academic sources, and problem solving requires sophisticated computation and reasoning far beyond factual recall. To bridge this gap, we introduce SciResearcher, a fully automated agentic framework for frontier-science data construction. SciResearcher synthesizes diverse conceptual and computational tasks grounded in academic evidence, while eliciting information acquisition, tool-integrated reasoning, and long-horizon capabilities. Leveraging the curated data for supervised fine-tuning and agentic reinforcement learning, we develop SciResearcher-8B, an agent foundation model that achieves 19.46% on the HLE-Bio/Chem-Gold benchmark, establishing a new state of the art at its parameter scale and surpassing several larger proprietary agents. It further achieves 13-15% absolute gains on SuperGPQA-Hard-Biology and TRQA-Literature benchmarks. Overall, SciResearcher introduces a new paradigm for automated data construction for frontier scientific reasoning and offers a scalable path toward future scientific agents.

---


### 71. [FT-RAG: A Fine-grained Retrieval-Augmented Generation Framework for Complex Table Reasoning](https://arxiv.org/abs/2605.01495)

**<font color=#1a73e8>作者：</font>** Zebin Guo, Weidong Geng, Ruichen Mao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by grounding responses in external knowledge during inference. However, conventiona RAG systems under-perform on structured tabular data, largely due to coarse retrieval granularity and insufficient table semantic comprehension. To address these limitations, we introduce FT-RAG, a fine-grained framework that employs knowledge association by decomposing tables into entry-level semantic units to construct a structured graph. FT-RAG employs a structural neighbor expansion mechanism to find semantically connected entities during graph retrieval, followed by multi-modal fusion to consolidate the context of table retrieval results. Further, to address the scarcity of specialized datasets in this domain, we introduce Multi-Table-RAG-Lib, a benchmark comprising 9870 QA pairs with high complexity and difficulty, curated to demand multi-table integration and text-table information fusion for reasoning. FT-RAG surpasses top-performing baselines across all metrics, achieving a 23.5\% and 59.2\% improvement in table-level and cell-level Hit Rates, respectively. Generation performance also sees a remarkable 62.2\% increase in exact value accuracy recall. These metrics verify the framework's effectiveness in factual grounding across both pure tabular and heterogeneous table-text contexts. Therefore, our method establishes a new state-of-the-art performance for complex reasoning over mixed-modality documents.

---


### 72. [OmniEncoder: See, Hear, and Feel Continuous Motion Like Humans With One Encoder](https://arxiv.org/abs/2605.01506)

**<font color=#1a73e8>作者：</font>** Detao Bai, Shimin Yao, Weixuan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in omni-modal large language models have enabled remarkable progress in joint vision-audio understanding. However, prevailing architectures rely on modality-specific encoders with a \emph{video-coarse, audio-dense} design -- sampling visual frames at 1--2 fps while processing audio waveforms at 25 fps -- resulting in systems that perceive video \emph{frame by frame, modality by modality} rather than holistically as humans do. Such a discrepancy leaves models with impoverished cross-modal interaction during encoding and an inability to capture fine-grained visual motion. To bridge this gap, we present \textbf{Omni-Encoder, a unified Transformer backbone designed to co-embed visual and audio signals at a symmetrical 25 fps} within a shared latent space. This architecture leverages three core innovations -- the Omni-Encoder Token Template, Omni-RoPE, and Temporal Window Shifting -- to effectively reconcile the dual challenges of modality disentanglement and computational efficiency. Experiments demonstrate that, compared to the modality-specific baseline Qwen2.5-Omni under the same input token budget to the LLM decoder, Omni-Encoder delivers substantial gains on visual continuous understanding tasks -- such as sign language recognition and fine-grained sports action analysis -- while maintaining competitive performance on established audio-visual benchmarks such as AVQA and Speaker Identification and Localization. These results suggest that unified omnivorous encoding offers a promising direction for building omni-modal models that more closely reflect the integrated nature of human perception.

---


### 73. [MILD: Mediator Agent System with Bidirectional Perception and Multi-Layered Alignment for Human-Vehicle Collaboration](https://arxiv.org/abs/2605.01507)

**<font color=#1a73e8>作者：</font>** Jiyao Wang, Yunbiao Wang, Yubo Jiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prior studies report that partial driving automation can increase the cognitive demands on human drivers. This effect largely arises from human drivers' lack of transparent insight into the vehicle's intentions and decision logic, as well as from automated systems' limited awareness of the driver's dynamic state and preferences. This bidirectional misalignment undermines shared situational awareness and exacerbates coordination failures in human-vehicle interaction. To address these limitations, we argue for a paradigm shift that elevates the human role from passive supervisor to active manager. We introduce the Mediator-in-the-Loop-Driving (MILD) system, based on an agentic system architecture to facilitate synergistic human-vehicle collaboration. MILD integrates a perception agent for joint in-cabin and out-of-cabin understanding with a lightweight strategy agent that generates compliant and explainable action suggestions. To ensure these strategies are strictly aligned with safety regulations and human values, we develop Evidence- and Constraint-weighted Policy Optimization (ECPO). ECPO leverages automatic validators to steer the agent toward behaviors that are not only accurate but also structurally complete, substantiated by evidence, and free from constraint violations. Furthermore, a retrieval-augmented generation module dynamically incorporates constraints from traffic regulations, speed recommendations, and driver preferences into the decision loop. Field experiments across three open datasets demonstrate that MILD consistently outperforms baselines in both perception accuracy and strategy quality under auditable offline metrics, and yields higher human-rated policy adequacy, comfort, and explanation than baselines. This work offers a practical pathway for building auditable and aligned agents for human-vehicle collaborative driving.

---


### 74. [Two-Pass Zero-Shot Temporal-Spatial Grounding of Rare Traffic Events in Surveillance Video](https://arxiv.org/abs/2605.01512)

**<font color=#1a73e8>作者：</font>** Jiantang Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounding traffic accidents in real CCTV footage is a rare-event problem where training on labeled accident video is often prohibited, yet accurate joint localization in time, space, and collision type is required. We present a no-fine-tuning pipeline that elicits this joint output from frozen vision-language models through two ideas. First, a coarse-to-fine two-pass decomposition: a full-video pass at 1 fps produces a coarse (t, x, y, c) tuple, then a second pass at 5 fps within a +/- 3 s window refines time and location, with two deterministic confidence gates that revert to the coarse estimate on boundary hedges or edge-clamped coordinates. Second, a specialist role assignment: Qwen3-VL-Plus handles grounding, Gemini 3.1 Flash-Lite handles typing on a centered video clip. On the ACCIDENT@CVPR 2026 benchmark (2,027 real CCTV videos) we reach ACC^S = 0.539 (95% CI [0.525, 0.553]): +0.127 over the benchmark paper's best-of-baselines oracle (0.412), +0.143 over the strongest single-VLM baseline (Molmo-7B, 0.396), and +0.250 over the naive baseline (0.289). The VLM path uses up to three API calls per video (17% fall back to physics on API failures); the full run costs ~$20.

---


### 75. [MIRL: Mutual Information-Guided Reinforcement Learning for Vision-Language Models](https://arxiv.org/abs/2605.01520)

**<font color=#1a73e8>作者：</font>** Yin Zhang, Jiaxuan Zhao, Zonghan Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) frequently suffer from visual perception errors and hallucinations that compromise answer accuracy in complex reasoning tasks. Reinforcement Learning with Verifiable Rewards (RLVR) offers a promising solution by optimizing policies using answer correctness signals. Despite their effectiveness, prevailing RLVR methods face two critical limitations. First, much of the sampling budget is wasted on trajectories doomed to fail due to early visual description errors. Second, sparse rewards cannot distinguish whether failures stem from visual perception or reasoning stages. We introduce MIRL, a decoupled framework that addresses both limitations by leveraging mutual information (MI) between generated descriptions and visual inputs as a cheap pre-screening signal. This enables intelligent budget allocation toward high-potential trajectories via forking, while decoupled training provides independent MI-based rewards for visual perception optimization, resolving reward blindness. Experiments on six vision-language reasoning benchmarks demonstrate that MIRL achieves 70.22% average accuracy and successfully surpasses the performance of sampling 16 complete trajectories using only 10 pre-samples with top-6 selection (25% fewer complete trajectories). Our code is available at: this https URL.

---


### 76. [Automated Interpretability and Feature Discovery in Language Models with Agents](https://arxiv.org/abs/2605.01555)

**<font color=#1a73e8>作者：</font>** Arnau Marin-Llobet, Javier Ferrando  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce an autonomous multiagent framework for mechanistic interpretability that automates both explaining and finding internal features in large language models. The system runs two coupled loops: (1) explanation refinement, where an agent proposes competing hypotheses and iteratively tests them with targeted prompt controls and a multi-metric evaluation; and (2) feature discovery, where an agent generates prompt sets, constructs a k-nearest-neighbor graph in activation space, and retrieves candidate features using statistical separability and semantic coherence criteria. On Gemma-2 family models and MLP neurons in weight-sparse transformers, our agent improves over one-shot auto-interpretations, discovers language-specific and safety-relevant features, and produces auditable explanation traces, showing that agent-driven empirical loops yield sharper and more falsifiable explanations than one-shot labels.

---


### 77. [Fine-Tuning Pre-Trained Code Models for AI-Generated Code Detection](https://arxiv.org/abs/2605.01596)

**<font color=#1a73e8>作者：</font>** Jany-Gabriel Ispas, Sergiu Nisioi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes the system submitted by team \textbf{Archaeology} to SemEval-2026 Task~13 on AI-generated code detection. The shared task consists of three subtasks; we participate in Subtask-A (binary classification: human-written vs.\ AI-generated code) and Subtask-B (11-class attribution of the generating model). Starting from a TF-IDF and Logistic Regression baseline, we fine-tune four pre-trained code models (CodeBERT, GraphCodeBERT, UniXcoder, and CodeT5+) with separate strategies for each subtask. For Subtask-A, we use leave-one-language-out cross-validation, code augmentation, chunked inference with trimmed-mean aggregation, and threshold calibration on a difficult dataset. For Subtask-B, we use sandwich token packing, class-balanced loss, and multi-seed ensembling with test-time augmentation. Our best submissions obtain macro-F1 scores of 0.737 on Subtask-A (6th/81 teams) and 0.422 on Subtask-B (7th/34 teams).

---


### 78. [Evaluating Agentic AI in the Wild: Failure Modes, Drift Patterns, and a Production Evaluation Framework](https://arxiv.org/abs/2605.01604)

**<font color=#1a73e8>作者：</font>** Mukund Pandey  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing evaluation frameworks for large language models -- including HELM, MT-Bench, AgentBench, and BIG-bench -- are designed for controlled, single-session, lab-scale settings. They do not address the evaluation challenges that emerge when agentic AI systems operate continuously in production: compounding decision errors, tool failure cascades, non-deterministic output drift, and the absence of ground truth for long-horizon tasks. This paper makes three contributions. First, we present a taxonomy of seven failure modes unique to production agentic systems, each grounded in observations from systems operating at billion-event scale. Second, we demonstrate empirically where standard metrics -- ROUGE, BERTScore, accuracy/AUC, and the agentic benchmarks above -- fail to detect each failure mode. Third, we propose PAEF (Production Agentic Evaluation Framework), a five-dimension evaluation framework with an open-source reference implementation, designed for continuous evaluation on production traffic rather than episodic benchmark runs. Our analysis shows that standard metrics fail to detect four of the seven failure modes entirely and detect three others only after a lag of multiple evaluation cycles.

---


### 79. [Where Do Prompt Perturbations Break Generation? A Segment-Level View of Robustness in LoRA-Tuned Language Models](https://arxiv.org/abs/2605.01605)

**<font color=#1a73e8>作者：</font>** Zhuoyun Li, Boxuan Wang, Jinwei Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are sensitive to minor prompt perturbations, yet existing robustness methods usually enforce consistency at the whole-sequence level. This holistic view can hide an important failure mode: a perturbed response may remain globally similar to the clean one while drifting on a critical entity, relation, or conclusion. We introduce S$^2$R$^2$, a segment-level framework for robust LoRA fine-tuning. S$^2$R$^2$ decomposes clean and perturbed generations into semantic segments, aligns them with an optimal-transport objective, and penalises the segments with the largest meaning drift. To connect this output-side objective with model adaptation, we add an adapter-stability regulariser motivated by segment-level attention reallocation, using LoRA norm control as a tractable proxy for limiting perturbation-amplified evidence shifts. A PAC-Bayesian complexity view further explains why controlling adapter growth may support transfer beyond observed perturbations. Experiments on summarisation benchmarks show that S$^2$R$^2$ improves robustness under typographical noise, deletion, synonym replacement, and paraphrasing, while maintaining competitive clean performance and stronger cross-dataset transfer than consistency-based baselines.

---


### 80. [Less Interaction But More Explanation: A Communication Perspective on Agentic AI Interfaces](https://arxiv.org/abs/2605.01610)

**<font color=#1a73e8>作者：</font>** Eunchae Jang, S. Shyam Sundar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI systems have long been expected to interact with users, answering questions, generating content, and continuing (social) conversations. Agentic AI, however, breaks from this expectation, as its primary objective is workflow execution on behalf of the users. If a system becomes more agentic, do users need less interaction with the system? Our answer is: less routine back-and-forth, but more communication for oversight and explanation, as agentic AI proactively acts, not just responds. Grounded in a communication perspective, we discuss how users perceive the communicative roles of AI systems (whether as the source of actions or merely a channel), and how this can shape trust. Because agentic AI can play multiple communicative roles, it can complicate this source perception and introduce potential risks. To address this, we propose three types of explanations that agentic AI needs to incorporate (action-process, uncertainty, and coordination), and suggest that customization affordances that allow users to decide when and which explanations they see may be key to preserving human agency as AI autonomy increases.

---


### 81. [Importance-Guided Basis Selection for Low-Rank Decomposition of Large Language Models](https://arxiv.org/abs/2605.01627)

**<font color=#1a73e8>作者：</font>** Daniel Agyei Asante, Ernie Chang, Yang Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank decomposition is a compelling approach for compressing large language models, but its effectiveness hinges on selecting which singular-vector bases to retain for a target task. Existing methods such as Basel adapt singular-value coefficients on downstream data and prune bases with small re-learned magnitudes, a heuristic that can be misaligned with task performance because it ignores the local geometry of the loss landscape. We present Basis Selection with Importance (BSI), a principled low-rank compression framework that ranks and prunes bases by directly estimating the expected loss increase incurred when each basis is removed. BSI derives a derivative-based importance score from a second-order Taylor expansion of the task loss with respect to singular values, combining first-order sensitivity and second-order curvature to quantify pruning impact. To make this criterion practical for LLMs, we develop an efficient Hessian-diagonal estimator by adapting the Hutchinson randomized-probing method to loss curvature with symmetric parameter perturbations. We provide a comprehensive theoretical analysis, including loss-increase bounds under basis pruning, explicit propagation of Hessian-diagonal estimation error into these bounds, variance characterization tied to the Hessian spectrum, high-probability sample-complexity guarantees for achieving a target estimation accuracy, and guidance on perturbation intensity. Extensive experiments on mathematical reasoning benchmarks demonstrate that BSI consistently outperforms state-of-the-art low-rank decomposition baselines, with especially strong improvements under deep compression.

---


### 82. [Prosa: Rubric-Based Evaluation of LLMs on Real User Chats in Brazilian Portuguese](https://arxiv.org/abs/2605.01630)

**<font color=#1a73e8>作者：</font>** Roseval Malaquias Junior, Giovana Kerche Bonás, Thales Sales Almeida 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rankings produced by holistic LLM-as-a-judge scoring are sensitive to the bias of the chosen judge model. We show that switching to binary rubric scoring with multi-judge filtering removes this sensitivity: decomposing the judgement matters more than the judge model itself. To support this claim, we introduce Prosa, the first real user multi-turn Brazilian Portuguese chat benchmark: 1,000 WildChat conversations scored by three judges from three model families on 16 models. Under filtered rubric scoring the three judges agree on every one of the 16 ranks, whereas under holistic scoring they agree on only 7 of 16. Additionally, the rubric filtering pipeline increases the average score gap between neighbouring models by 47%, thereby improving Prosa's discriminative power. Evaluating a new model on Prosa costs approximately $2.1 when using Gemini 3 Flash as the judge. We release the benchmark and the filtering code to ensure that future models can be assessed under identical conditions. These artifacts also make our rubric-based scoring method reusable beyond Prosa, supporting other open-ended evaluation settings.

---


### 83. [Omni-Fake: Benchmarking Unified Multimodal Social Media Deepfake Detection](https://arxiv.org/abs/2605.01638)

**<font color=#1a73e8>作者：</font>** Tianxiao Li, Zhenglin Huang, Haiquan Wen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal deepfakes are proliferating on social media and threaten authenticity, information integrity, and digital forensics. Existing benchmarks are constrained by their single-modality scope, simplified manipulations, or unrealistic distributions, which limit their ability to assess real-world robustness. To address these limitations, we present Omni-Fake, a unified omni-dataset for comprehensive multimodal deepfake detection in social-media settings. It comprises Omni-Fake-Set, a large-scale, high-quality dataset with 1M+ samples, and Omni-Fake-OOD, an out-of-distribution benchmark with 200k+ samples intentionally excluded from training to evaluate generalization. Omni-Fake spans four modalities (image, audio, video, and audio-video talking head) and supports a joint detection-localization-explanation protocol. On top of Omni-Fake, we further propose Omni-Fake-R1, a reinforcement-learning-driven multimodal detector that adaptively integrates visual and auditory cues and outputs structured decisions, localization, and natural-language explanations. Extensive experiments show significant gains in detection accuracy, cross-modal generalization, and explainability over state-of-the-art baselines. Project page: this https URL

---


### 84. [Adaptive Pluralistic Alignment: A pipeline for dynamic artificial democracy](https://arxiv.org/abs/2605.01642)

**<font color=#1a73e8>作者：</font>** Rachel Freedman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prevailing alignment methods target a fixed set of preferences and therefore risk forcing value lock-in as societal norms evolve over time. We introduce Adaptive Pluralistic Alignment (APA), a modular pipeline for updating pluralistically aligned AI systems to track evolving values and avoid value lock-in without repeating costly pretraining or large-scale data collection. APA has three stages: (1) learning compact personalized reward models via low-rank reward basis decomposition, (2) using these models as a jury that collectively selects among candidate outputs through social-choice-theoretic voting, and (3) efficiently adapting the jury over time by fitting new annotator weights over the fixed reward bases as values shift. The resulting system is efficient, explainable, steerable, and modular. We implement a proof-of-concept instantiation using the PRISM multi-user alignment dataset and simulated historical annotators, and provide preliminary analysis showing that jury composition and the choice of voting rule can substantially affect outcomes, particularly when jury preferences are heterogeneous. We provide full code and resulting preference datasets at this https URL.

---


### 85. [AI Alignment via Incentives and Correction](https://arxiv.org/abs/2605.01643)

**<font color=#1a73e8>作者：</font>** Rohit Agarwal, Joshua Lin, Mark Braverman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study AI alignment through the lens of law-and-economics models of deterrence and enforcement. In these models, misconduct is not treated as an external failure, but as a strategic response to incentives: an actor weighs the gain from violation against the probability of detection and the severity of punishment. We argue that the same logic arises naturally in agentic AI pipelines. A solver may benefit from producing a persuasive but incorrect answer, hiding uncertainty, or exploiting spurious shortcuts, while an auditor or verifier must decide whether costly monitoring is worthwhile. Alignment is therefore a fixed-point problem: stronger penalties may deter solver misbehavior, but they can also reduce the auditor's incentive to inspect, since auditing then mainly incurs cost on a population that appears increasingly aligned.
This perspective also changes what should count as a post-training signal. Standard feedback often attaches reward to the final answer alone, but a solver-auditor pipeline exposes the full correction event: whether the solver erred, whether the auditor inspected, whether the error was caught, and whether oversight incentives remained active. We formalize this interaction in a two-agent model in which a principal chooses rewards over joint correction outcomes, inducing both solver behavior and auditor monitoring. Reward design is therefore a bilevel optimization problem: rewards are judged not by their immediate semantic meaning, but by the behavioral equilibrium they induce. We propose a bandit-based outer-loop procedure for searching over reward profiles using noisy interaction feedback. Experiments on an LLM coding pipeline show that adaptive reward profiles can maintain useful oversight pressure and improve principal-aligned outcomes relative to static hand-designed rewards, including a substantial reduction in hallucinated incorrect attempts.

---


### 86. [Act2See: Emergent Active Visual Perception for Video Reasoning](https://arxiv.org/abs/2605.01657)

**<font color=#1a73e8>作者：</font>** Martin Q. Ma, Yuxiao Qu, Aditya Agrawal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) typically rely on static initial frames for video reasoning, restricting their ability to incorporate essential dynamic information as the reasoning process evolves. Existing methods that augment Chain-of-Thought (CoT) with additional frame information often exhibit suboptimal CoT quality and lack the crucial ability to synthesize visual information for hypothetical or counterfactual scenarios. We introduce Act-to-See (Act2See), a novel framework that enables active visual perception by empowering VLMs to actively interleave video frames within text CoTs. Act2See is developed via Supervised Fine-Tuning (SFT) on a high-quality dataset of reasoning traces generated by a frontier VLM. These traces integrate active calls to either retrieve existing frames or generate new ones, and are rigorously verified against human-annotated CoTs to ensure quality. This approach cultivates an emergent capability: at inference time, the model actively determines when to search for or synthesize the necessary visual evidence. Act2See establishes new state-of-the-art results on challenging benchmarks, including VideoEspresso and ViTIB, and outperforms comparable or larger models on Video-MME, EgoNormia, and VCR-Bench, demonstrating an advancement in enabling VLMs with active visual perception for video reasoning.

---


### 87. [Video Active Perception: Effective Inference-Time Long-Form Video Understanding with Vision-Language Models](https://arxiv.org/abs/2605.01662)

**<font color=#1a73e8>作者：</font>** Martin Q. Ma, Willis Guo, Aditya Agrawal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (VLMs) have advanced multimodal tasks such as video question answering (QA). However, VLMs face the challenge of selecting frames effectively and efficiently, as standard uniform sampling is expensive and performance may plateau. Inspired by active perception theory, which posits that models gain information by acquiring data that differs from their expectations, we introduce Video Active Perception (VAP), a training-free method to enhance long-form video QA using VLMs. Our approach treats keyframe selection as data acquisition in active perception and leverages a lightweight text-conditioned video generation model to represent prior world knowledge. Empirically, VAP achieves state-of-the-art zero-shot results on long-form or reasoning video QA datasets such as EgoSchema, NExT-QA, ActivityNet-QA, IntentQA, and CLEVRER, achieving an increase of up to 5.6 x frame efficiency by frames per question over standard GPT-4o, Gemini 1.5 Pro, and LLaVA-OV. Moreover, VAP shows stronger reasoning abilities than previous methods and effectively selects keyframes relevant to questions. These findings highlight the potential of leveraging active perception to improve the frame effectiveness and efficiency of long-form video QA.

---


### 88. [MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark for Evaluating LLM Safety](https://arxiv.org/abs/2605.01687)

**<font color=#1a73e8>作者：</font>** Jialin Song, Xiaodong Liu, Weiwei Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present MultiBreak, a scalable and diverse multi-turn jailbreak benchmark to evaluate large language model (LLM) safety. Multi-turn jailbreaks mimic natural conversational settings, making them easier to bypass safety-aligned LLM than single-turn jailbreaks. Existing multi-turn benchmarks are limited in size or rely heavily on templates, which restrict their diversity. To address this gap, we unify a wide range of harmful jailbreak intents, and introduce an active learning pipeline for expanding high-quality multi-turn adversarial prompts, where a generator is iteratively fine-tuned to produce stronger attack candidates, guided by uncertainty-based refinement. Our MultiBreak includes 10,389 multi-turn adversarial prompts, spans 2,665 distinct harmful intents, and covers the most diverse set of topics to date. Empirical evaluation shows that our benchmark achieves up to a 54.0 and 34.6 higher attack success rate (ASR)} than the second-best dataset on DeepSeek-R1-7B and GPT-4.1-mini, respectively. More importantly, safety evaluations suggest that diverse attack categories uncover fine-grained LLM vulnerabilities}, and categories that appear benign under single-turn can exhibit substantially higher adversarial effectiveness in multi-turn scenarios. These findings highlight persistent vulnerabilities of LLMs under realistic adversarial settings and establish MultiBreak as a scalable resource for advancing LLM safety.

---


### 89. [Latent State Design for World Models under Sufficiency Constraints](https://arxiv.org/abs/2605.01694)

**<font color=#1a73e8>作者：</font>** Keon Woo Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A world model matters to an agent only through the state it constructs. That state must preserve some information, discard other information, and support some future function: prediction, control, planning, memory, grounding, or counterfactual reasoning. This paper treats world-model research as latent state design under sufficiency constraints.
We propose a functional taxonomy that groups methods by what their latent state is for, rather than by architecture or application domain: predictive embedding, recurrent belief state, object/causal structure, latent action interface, grounded planning interface, and memory substrate. These roles expose distinctions that architecture-based groupings hide, including the gap between predictive sufficiency and control sufficiency, and the gap between passive video prediction and counterfactual action modeling.
The taxonomy supports an evaluation framework that judges a model by the sufficiency constraint its latent state was built to satisfy. We compare methods along seven axes: representation, prediction, planning, controllability, causal/counterfactual support, memory, and uncertainty. We use the resulting matrix as a diagnostic for what a latent state preserves, discards, and enables.
The conclusion that follows is that an actionable world model is the one whose state construction matches the task, not the one that preserves the most information.

---


### 90. [BIM Information Extraction Through LLM-based Adaptive Exploration](https://arxiv.org/abs/2605.01698)

**<font color=#1a73e8>作者：</font>** Sylvain Hellin, Suhyung Jang, Stefan Fuchs 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> BIM models provide structured representations of building geometry, semantics, and topology, yet extracting specific information from them remains remarkably difficult. Current approaches translate natural language into structured queries by assuming a fixed data organization (static approach), which BIM heterogeneity eventually invalidates. We address this with a new paradigm, adaptive exploration, where an LLM-based agent iteratively executes code to extract information from a BIM model, discovering its structure at runtime instead of assuming it. We evaluate this approach on ifc-bench v2, an open-source BIM question-answering benchmark introduced alongside this work, comprising 1,027 tasks across 37 IFC models from 21 projects. A factorial ablation across two LLM capability levels and four augmentation strategies shows that adaptive exploration significantly outperforms static query generation across all configurations, regardless of the augmentation strategy. These results indicate that BIM heterogeneity is best addressed at the paradigm level, not by further optimizing static approaches.

---


### 91. [Probe-Geometry Alignment: Erasing the Cross-Sequence Memorization Signature Below Chance](https://arxiv.org/abs/2605.01699)

**<font color=#1a73e8>作者：</font>** Anamika Paul Rupa, Anietie Andy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent attacks show that behavioural unlearning of large language models leaves internal traces recoverable by adversarial probes. We characterise where this retention lives and show it can be surgically removed without measurable capability cost. Our central protocol is a leave-one-out cross-sequence probe that tests whether a memorisation signature generalises across held-out sequences. The signature is real and consistent across scale: memorisation-specific gaps of +0.32, +0.19, +0.30 on Pythia-70M, GPT-2 medium, and Mistral-7B; on Pythia-70M, the random-initialisation control collapses to -0.04 at the deepest layer where the pretrained signature peaks. The probe direction is causally separable from recall -- projecting it out collapses the signature locally (+0.44 -> -0.19) while behavioural recall barely changes -- and a probe trained on naturally memorised content does not classify fine-tuning-injected secrets, marking two representationally distinct regimes. We then introduce probe-geometry alignment (PGA), a surgical erasure that aligns activations along the probe's live readout direction at each depth. PGA drives the cross-sequence probe below random chance at all four scales tested (toy depth-4: 0.17; Pythia-70M: 0.07; Mistral-7B: 0.45; GPT-2 medium: 0.06 via MD-PGA k=2) and remains robust to six adversarial probe variants. Against a re-fitting attacker who trains a fresh probe on PGA-treated activations, we extend PGA adversarially, defeating the re-fit probe at every memorisation-relevant depth while preserving five zero-shot capability benchmarks within 2.8 percentage points per task (mean {\Delta}acc = +0.2pp). The cross-sequence signature is a real, causally separable, regime-specific property of pretrained representations -- removable below chance with a single rank-one intervention per depth at no measurable capability cost.

---


### 92. [TrajRAG: Retrieving Geometric-Semantic Experience for Zero-Shot Object Navigation](https://arxiv.org/abs/2605.01700)

**<font color=#1a73e8>作者：</font>** Yiyao Wang, Sixian Zhang, Keming Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing zero-shot Object Goal Navigation (ObjectNav) methods often exploit commonsense knowledge from large language or vision-language models to guide navigation. However, such knowledge arises from internet-scale text rather than embodied 3D experience, and episodic observations collected during navigation are typically discarded, preventing the accumulation of lifelong experience. To this end, we propose Trajectory RAG (TrajRAG), a retrieval-augmented generation framework that enhances large-model reasoning by retrieving geometric-semantic experiences. TrajRAG incrementally accumulates episodic observations from past navigation episodes. To structure these observations, we propose a topological-polar (topo-polar) trajectory representation that compactly encodes spatial layouts and semantic contexts, effectively removing redundancies in raw episodic observations. A hierarchical chunking structure further organizes similar topo-polar trajectories into unified summaries, enabling coarse-to-fine retrieval. During navigation, candidate frontiers generate multiple trajectory hypotheses that query TrajRAG for similar past trajectories, guiding large-model reasoning for waypoint selection. New experiences are continually consolidated into TrajRAG, enabling the accumulation of lifelong navigation experience. Experiments on MP3D, HM3D-v1, and HM3D-v2 show that TrajRAG effectively retrieves relevant geometric-semantic experiences and improves zero-shot ObjectNav performance.

---


### 93. [The Reasoning Trap: An Information-Theoretic Bound on Closed-System Multi-Step LLM Reasoning](https://arxiv.org/abs/2605.01704)

**<font color=#1a73e8>作者：</font>** Kwan Soo Shin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When copies of the same language model are prompted to debate, they produce diverse phrasings of one perspective rather than diverse perspectives. Multi-agent debate (MAD), and more broadly closed-system reasoning where agents iteratively transform each other's outputs, tends to preserve answer accuracy while degrading the reasoning behind those answers. We name the multi-agent case the Debate Trap and the broader phenomenon the Reasoning Trap, offering a programmatic theory of evidence-grounded reasoning this http URL framework has three parts: (i) SFS (Supported Faithfulness Score), a claim-level metric verifying decomposed atomic claims against provided evidence (decomposer-invariant rankings: Spearman rho=1.0); (ii) EGSR (Evidence-Grounded Socratic Reasoning), replacing adversarial argumentation with evidence-grounded inquiry; (iii) Theorem 1 (DPI Bound): under standard MAD, the chain E -> O^0 -> O^1 -> ... is Markov, and the Data Processing Inequality implies E[I(E;O^{t+1})] <= E[I(E;O^t)]. Three companion results -- open-system recovery (Theorem 2), EGSR accumulation (Lemma 2), and vote-aggregation floor (Proposition 1) -- partition multi-step LLM reasoning by its information-theoretic relationship to E. Across 16 conditions on SciFact (300 claims) and FEVER (1,000 claims), DebateCV (C13) preserves 88% of baseline accuracy while SFS drops 43%; majority-vote MAD (C15) reduces SFS to 1.7% of baseline (p < 10^{-6}, d = -0.96); EGSR recovers 98%. An R6 cohort study (Korean n=10x30 FEVER; English n=3x200 SciFact) finds inter-rater Fleiss kappa <= +0.018 with 0.8-1.4 Likert intra-rater shifts across language and domain -- the human agreement that faithfulness metrics have been calibrated against is not itself stable. We offer one falsifiable conjecture: any closed-system reasoning protocol preserving Theorem 1's Markov structure is, in expectation, subject to the same DPI bound.

---


### 94. [Are LLMs More Skeptical of Entertainment News?](https://arxiv.org/abs/2605.01727)

**<font color=#1a73e8>作者：</font>** Huiqian Lai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for automated news credibility assessment, yet it remains unclear whether they apply even-handed standards across journalistic genres. We examine whether zero-shot LLMs are more likely to misclassify legitimate entertainment news as fake than legitimate hard news, using a within-dataset design on GossipCop from FakeNewsNet. Across four frontier models, we find a clear but model-specific genre asymmetry: DeepSeek-V3.2 and GPT-5.2 show false-positive-rate gaps of 10.1 and 8.8 percentage points, respectively (both $p < .001$), whereas Claude Opus 4.6 and Gemini 3 Flash show no comparable difference. A style-swap experiment yields only limited and inconsistent changes, suggesting that the asymmetry is not reducible to stylistic register alone. Prompt-based mitigation is likewise possible but not generic: framing the model as an entertainment-news fact-checker reduces false positives for DeepSeek-V3.2 by about 50\% without detectable recall loss, but offers little improvement for GPT-5.2. Exploratory qualitative coding further suggests two recurring error patterns in sampled false positives: treating private-life claims as inherently unverifiable and discounting entertainment journalism as an epistemically weaker genre. Taken together, these findings show that aggregate performance metrics can obscure structured false positives within legitimate journalism. We argue that LLM-based credibility assessment may not only evaluate truth claims but also differentially recognize the legitimacy of journalistic genres, and that evaluation should therefore include genre-stratified false-positive analysis alongside overall accuracy.

---


### 95. [EGAD: Entropy-Guided Adaptive Distillation for Token-Level Knowledge Transfer](https://arxiv.org/abs/2605.01732)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Zhibin Zhang, Guangxin Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved remarkable performance across diverse domains, yet their enormous computational and memory requirements hinder deployment in resource-constrained environments. Knowledge distillation offers a promising solution by transferring knowledge from a large teacher model to a smaller student model. However, existing distillation methods typically treat all tokens equally, ignoring the fact that different tokens contribute unequally to model decisions. This can lead to inefficient knowledge transfer and reduced learning effectiveness. To address this limitation, we propose an entropy-based adaptive distillation strategy that dynamically adjusts the training process at the token level. Our method leverages the teacher's output entropy to guide three aspects of distillation. Specifically, we introduce a token-level curriculum by dynamically shifting focus from low- to high-entropy tokens during training. We further adjust the distillation temperature based on token entropy to better capture teacher confidence patterns. Moreover, we employ a dual-branch architecture for efficient logits-only distillation on easy tokens and deeper feature-based distillation on difficult tokens. Extensive experiments validate the soundness and effectiveness of our method.

---


### 96. [GEASS: Training-Free Caption Steering for Hallucination Mitigation in Vision-Language Models](https://arxiv.org/abs/2605.01733)

**<font color=#1a73e8>作者：</font>** Zeshang Li, Shuoyang Zhang, Jiashen Ding  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) excel at grounded reasoning but remain prone to object hallucination. Recent work treats self-generated captions as a uniformly positive resource, yet we find that naively embedding one can degrade rather than help--dropping Qwen2.5-VL-3B accuracy on HallusionBench by nearly 10 points. Two structural properties explain this. First, captions anchor not only the model's final answer but also its reasoning trajectory and lexical choices. Second, caption errors are asymmetric: omissions vastly outnumber fabrications, yet each fabrication carries a much larger per-instance impact. A caption's usefulness is therefore a per-query property, not a per-corpus one. We propose GEASS (Gated Evidence-Aware Selective Steering), a training-free module that decides on each query how much of the caption the model consumes: it gates the caption by the clean path's confidence, weights it by the entropy reduction it produces, and raises the evidence bar when the two pathways disagree. Experiments on POPE and HallusionBench across four VLMs show that GEASS consistently improves over vanilla inference and contrastive decoding, with only two extra forward passes per query.

---


### 97. [Less is More: Geometric Unlearning for LLMs with Minimal Data Disclosure](https://arxiv.org/abs/2605.01735)

**<font color=#1a73e8>作者：</font>** Chenchen Tan, Xinghao Li, Shujie Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed in real-world systems, they must support post-hoc removal of specific content to meet privacy and governance requirements. This motivates selective unlearning, which suppresses information about a particular entity or topic while preserving the LLM's general utility. However, most existing LLM unlearning methods require access to the original training corpus and rely on output-level refusal tuning or broad gradient updates, creating a tension among unlearning strength, non-target preservation, and data availability. We propose Geometric Unlearning (GU), an approach that operates directly on the model's prompt-time planning states without access to the original training corpus. GU distills a compact, low-rank geometry of desired safe behavior from a small set of safe reference prompts, and uses lightweight anchor-in-context synthetic prompts to trigger localized, projection-based alignment of hidden planning representations to this safe geometry. A teacher-distillation regularizer on synthetic non-target anchors further reduces collateral drift. Across privacy-oriented unlearning benchmarks (ToFU and UnlearnPII), GU achieves strong target suppression with minimal impact on non-target performance, demonstrating that effective unlearning can be achieved with minimal synthetic data.

---


### 98. [Mitigating Multimodal LLMs Hallucinations via Relevance Propagation at Inference Time](https://arxiv.org/abs/2605.01766)

**<font color=#1a73e8>作者：</font>** Itai Allouche, Joseph Keshet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have revolutionized the landscape of AI, demonstrating impressive capabilities in tackling complex vision and audio-language tasks. However, a critical challenge remains: these models often suffer from hallucinations, generating outputs that diverge from the provided perceptual inputs. This tendency stems from an inherent imbalance in modality utilization during inference, where the dominance of textual tokens undermines the potential of perceptual inputs. As a result, the model frequently resorts to textual language priors at the expense of grounded evidence. To tackle this issue, we propose Learning Inference-time Modality Enhancement (LIME), a training-free framework designed to bolster multimodal grounding by explicitly enhancing modality usage during decoding. LIME leverages Layer-wise Relevance Propagation (LRP) to quantify token-level contributions and defines a relevance-based objective that promotes increased reliance on perceptual inputs. This objective is enforced through inference-time updates to the model's key-value representations, without modifying model parameters or requiring additional training data. We evaluate LIME across multiple multimodal benchmarks in both vision and audio domains, demonstrating consistent reductions in hallucinations and enhanced grounding while preserving generation quality. Further analysis shows that LIME increases modality contribution and produces more localized and semantically aligned relevance patterns.

---


### 99. [MedScribe: Clinically Grounded CT Reporting through Agentic Workflows](https://arxiv.org/abs/2605.01779)

**<font color=#1a73e8>作者：</font>** Giuseppe A. Orlando, Paolo Papotti, Maria A. Zuluaga 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have shown potential for automated radiology report generation, yet existing approaches rely on global embedding compression of volumetric data, often leading to hallucinated findings and limited anatomical grounding in 3D CT imaging. We introduce MedScribe, a hypothesis-driven framework that reformulates report generation as an iterative evidence acquisition process rather than a single-pass encoding task. MedScribe models reporting as a sequential decision process in which a large language model dynamically invokes pathology-specific diagnostic tools to extract localized volumetric features. These structured features are used to query a multidimensional retrieval space aligned with pathology-specific textual evidence. By explicitly accumulating quantitative evidence prior to synthesis, the framework enforces fine-grained grounding and reduces unsupported claims. Without task-specific fine-tuning, MedScribe improves clinical accuracy, factual consistency, and interpretability on CT-RATE and RadChestCT compared to state-of-the-art 2D and 3D VLMs, demonstrating the value of hypothesis-driven reasoning for reliable medical image reporting.

---


### 100. [Embody4D: A Generalist 4D World Model for Embodied AI](https://arxiv.org/abs/2605.01799)

**<font color=#1a73e8>作者：</font>** Peiyan Tu, Hanxin Zhu, Jingwen Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models have made significant progress in modeling dynamic environments; however, most embodied world models are still restricted to 2D representations, lacking the comprehensive multi-view information essential for embodied spatial reasoning. Bridging this gap is non-trivial, primarily due to challenges from severe scarcity of paired multi-view data, the difficulty of maintaining spatiotemporal consistency in generated 3D geometries, and the tendency to hallucinate manipulation details. To address these challenges, we propose Embody4D, a dedicated video-to-video world model for embodied scenarios, capable of synthesizing arbitrary novel views from a monocular video. First, to tackle data scarcity, we introduce a 3D-aware compositional synthesis pipeline to curate a heterogeneous dataset compositing cross-embodiment robotic arms with diverse backgrounds, guaranteeing broad generalization. Second, to enforce geometric stability, we devise an adaptive noise injection strategy; by leveraging confidence disparities across image regions, this method selectively regularizes the diffusion process to ensure strict spatiotemporal consistency. Finally, to guarantee manipulation fidelity, we incorporate an interaction-aware attention mechanism that explicitly attends to the robotic interaction regions. Extensive experiments demonstrate that Embody4D achieves state-of-the-art performance, serving as a robust world model that synthesizes high-fidelity, view-consistent videos to empower downstream robotic planning and learning.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-203](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
