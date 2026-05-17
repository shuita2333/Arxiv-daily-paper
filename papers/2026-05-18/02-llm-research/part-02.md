# 🧠 大模型相关研究 | 2026年05月18日

> 本类共 **165** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-165](./part-04.md)

---

### 51. [Diagnosing and Correcting Concept Omission in Multimodal Diffusion Transformers](https://arxiv.org/abs/2605.14270)

**<font color=#1a73e8>作者：</font>** Kanghyun Baek, Jaihyun Lew, Chaehun Shin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Diffusion Transformers (MM-DiTs) have achieved remarkable progress in text-to-image generation, yet they frequently suffer from concept omission, where specified objects or attributes fail to emerge in the generated image. By performing linear probing on text tokens, we demonstrate that text embeddings can distinguish a characteristic `omission signal' representing the absence of target concepts. Leveraging this insight, we propose Omission Signal Intervention (OSI), which amplifies the omission signal to actively catalyze the generation of missing concepts. Comprehensive experiments on FLUX.1-Dev and SD3.5-Medium demonstrate that OSI significantly alleviates concept omission even in extreme scenarios.

---


### 52. [KVPO: ODE-Native GRPO for Autoregressive Video Alignment via KV Semantic Exploration](https://arxiv.org/abs/2605.14278)

**<font color=#1a73e8>作者：</font>** Ruicheng Zhang, Kaixi Cong, Jun Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aligning streaming autoregressive (AR) video generators with human preferences is challenging. Existing reinforcement learning methods predominantly rely on noise-based exploration and SDE-based surrogate policies that are mismatched to the deterministic ODE dynamics of distilled AR models, and tend to perturb low-level appearance rather than the high-level semantic storyline progression critical for long-horizon coherence. To address these limitations, we present KVPO, an ODE-native online Group Relative Policy Optimization (GRPO) framework for aligning streaming video generators. For diversity exploration, KVPO introduces a causal-semantic exploration paradigm that relocates the source of variation from stochastic noise to the historical KV cache. By stochastically routing historical KV entries, it constructs semantically diverse generation branches that remain strictly on the data manifold. For policy modeling, KVPO introduces a velocity-field surrogate policy based on Trajectory Velocity Energy (TVE), which quantifies branch likelihood in flow-matching velocity space and yields a reward-weighted contrastive objective fully consistent with the native ODE formulation. Experiments on multiple distilled AR video generators demonstrate consistent gains in visual quality, motion quality, and text-video alignment across both single-prompt short-video and multi-prompt long-video settings.

---


### 53. [MetaMoE: Diversity-Aware Proxy Selection for Privacy-Preserving Mixture-of-Experts Unification](https://arxiv.org/abs/2605.14289)

**<font color=#1a73e8>作者：</font>** Weisen Jiang, Shuhao Chen, Sinno Jialin Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models scale capacity by combining specialized experts, but most existing approaches assume centralized access to training data. In practice, data are distributed across clients and cannot be shared due to privacy constraints, making unified MoE training challenging. We propose MetaMoE, a privacy-preserving framework that unifies independently trained, domain-specialized experts into a single MoE using public proxy data as surrogates for inaccessible private data. Central to MetaMoE is diversity-aware proxy selection, which selects client-domain-relevant and diverse samples from public data to effectively approximate private data distributions and supervise router learning. These proxies are further used to align expert training, improving expert coordination at unification time, while a context-aware router enhances expert selection across heterogeneous inputs. Experiments on computer vision and natural language processing benchmarks demonstrate that MetaMoE consistently outperforms recent privacy-preserving MoE unification methods. Code is available at this https URL.

---


### 54. [Minimal-Intervention KV Retention: A Design-Space Study and a Diversity-Penalty Survivor](https://arxiv.org/abs/2605.14292)

**<font color=#1a73e8>作者：</font>** Libo Sun, Po-wei Harn, Peixiong He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV-cache compression at small budgets is a crowded design space spanning cache representation, head-wise routing, compression cadence, decoding behavior, and within-budget scoring. We study seven mechanisms across these five families under matched mean cache on long-form mathematical reasoning (MATH-500~\cite{hendrycks2021math}) with two distilled-reasoning models (Qwen-7B and Llama-8B variants of DeepSeek-R1-Distill~\cite{deepseek2025r1}) at budgets $b \in \{64, 128\}$. All seven were rejected. We then propose $\alpha$, a one-function modification to the TriAttention~\cite{mao2026triattention} retention scorer that replaces argmax-top-$k$ with greedy facility-location-inspired selection under a V-space redundancy penalty controlled by a single weight $\lambda$. A pre-registered protocol tunes $\lambda$ on a frozen development split and confirms on a disjoint held-out split; with $\lambda = 0.5$, $\alpha$ clears Bonferroni on two of the four (model, budget) cells (Qwen $b{=}128$ and Llama $b{=}64$), no cell is significantly negative, and the pre-registered Branch~A triggers. The finding is asymmetric: a minimal scoring modification beat heavier structural redesigns in this regime, and the combined matched-memory, sympy-graded, held-out confirmation protocol is the evidence standard that made the asymmetry visible.

---


### 55. [Language-Induced Priors for Domain Adaptation](https://arxiv.org/abs/2605.14301)

**<font color=#1a73e8>作者：</font>** Qiyuan Chen, Jiayu Zhou, Raed Al Kontar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain adaptation faces a fundamental paradox in the cold-start regime. When target data is scarce, statistical methods fail to distinguish relevant source domains from irrelevant ones, which often leads to negative transfer. In this paper, we address this challenge by leveraging expert textual descriptions of the target domain, a resource that is often available but overlooked. We propose a probabilistic framework that translates these semantic descriptions into a choice model, namely a Language-Induced Prior (LIP), that learns the preferences from a pretrained Large Language Model (LLM). The LIP is then integrated into an Expectation-Maximization algorithm to identify source relevance. Methodologically, this framework is compatible with any parametric model where a likelihood is available. It allows the LIP to guide the selection of sources when target signals are weak, while gradually refining these choices as samples accumulate. Theoretically, we prove that the estimator roughly matches an oracle cold-start MSE under a correct prior, while remaining asymptotically consistent regardless of the quality of the LIP. Empirically, we validated the framework on a descriptive (Gaussian estimation), a predictive (C-MAPSS dataset), and a prescriptive task (MuJoCo hopper).

---


### 56. [Factorization-Error-Free Discrete Diffusion Language Model via Speculative Decoding](https://arxiv.org/abs/2605.14305)

**<font color=#1a73e8>作者：</font>** Xun Fang, Yunchen Li, Hang Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion language models improve generation efficiency through parallel token prediction, but standard $X_0$ prediction methods introduce factorization errors by approximating the clean token posterior with independent token-wise distributions. This paper proposes Factorization-Error-Free Discrete Diffusion Language Modeling (FeF-DLLM), which replaces independent clean-token prediction with an exact prefix-conditioned factorization of the clean posterior to better preserve token dependencies. To reduce the sequential cost introduced by prefix conditioning, FeF-DLLM further incorporates speculative decoding within diffusion denoising, accelerating inference while maintaining the parallel prediction and re-masking properties of DLLMs. Theoretically, we prove that FeF-DLLM generates from the true joint distribution and derive its expected acceleration ratio. Experiments on GSM8K, MATH, HumanEval, and MBPP demonstrate that our method improves accuracy by an average of 5.04 percentage points while achieving an average inference speedup of $3.86\times$.

---


### 57. [ICED: Concept-level Machine Unlearning via Interpretable Concept Decomposition](https://arxiv.org/abs/2605.14309)

**<font color=#1a73e8>作者：</font>** Shen Lin, Jing Lin, Junhao Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning in Vision-Language Models (VLMs) is typically performed at the image or instance level, making it difficult to precisely remove target knowledge without affecting unrelated semantics. This issue is especially pronounced since a single image often contains multiple entangled concepts, including both target concepts to be forgotten and contextual information that should be preserved. In this paper, we propose an interpretable concept-level unlearning framework for VLMs, which constructs a compact task-specific concept vocabulary from the forgetting set using a multimodal large language model. In addition to modality alignment, visual representations are decomposed into sparse, nonnegative combinations of semantic concepts, providing an explicit interface for fine-grained knowledge manipulation. Based on this decomposition, our method formulates unlearning as concept-level optimization, where target concepts are selectively suppressed while intra-instance non-target semantics and global cross-modal knowledge are preserved. Extensive experiments across both in-domain and out-of-domain forgetting settings demonstrate that our method enables more comprehensive target forgetting, better preserves non-target knowledge within the same image, and maintains competitive model utility compared with existing VLM unlearning methods.

---


### 58. [Beyond Binary: Reframing GUI Critique as Continuous Semantic Alignment](https://arxiv.org/abs/2605.14311)

**<font color=#1a73e8>作者：</font>** Yuchen Sun, Pei Fu, Shaojie Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-Time Scaling (TTS), which samples multiple candidate actions and ranks them via a Critic Model, has emerged as a promising paradigm for generalist GUI agents. Its efficacy thus hinges on the critic's fine-grained ranking ability. However, existing GUI critic models uniformly adopt binary classification. Our motivational analysis of these models exposes a severe entanglement: scores for valid actions and plausible-but-invalid distractors become indistinguishable. We attribute this failure to two structural defects: Affordance Collapse--the hierarchical affordance space is compressed into 0/1 labels; and Noise Sensitivity--binary objectives overfit to noisy decision boundaries. To resolve this, we introduce BBCritic (Beyond-Binary Critic), a paradigm shift grounded in the Functional Equivalence Hypothesis. Through two-stage contrastive learning, BBCritic aligns instructions and actions in a shared Affordance Space, recovering the hierarchical structure that binary supervision flattens. We also present BBBench (Beyond-Binary Bench), the first GUI critic benchmark that pairs a dense action space with a hierarchical four-level taxonomy, enabling fine-grained ranking evaluation. Experimental results show that BBCritic-3B, trained without any extra annotation, outperforms 7B-parameter SOTA binary models. It demonstrates strong zero-shot transferability across platforms and tasks, supporting our methodological view: GUI critique is fundamentally a metric-learning problem, not a classification one.

---


### 59. [AIM-DDI: A Model-Agnostic Multimodal Integration Module for Drug-Drug Interaction Prediction](https://arxiv.org/abs/2605.14327)

**<font color=#1a73e8>作者：</font>** Yerin Park, Sangseon Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug-drug interaction (DDI) prediction is a critical task in computational biomedicine, as adverse interactions between co-administered drugs can cause severe side effects and clinical risks. A key challenge is unseen-drug generalization, where interactions must be predicted for drugs not observed during training. Although multimodal DDI models exploit diverse drug-related information, their fusion mechanisms are often tied to specific prediction architectures, limiting their reuse across models. To address this, we propose AIM-DDI, an architecture-independent multimodal integration module that represents heterogeneous modality information as tokens in a shared latent space. By modeling dependencies across modality tokens through a unified fusion module, AIM-DDI enables model-agnostic integration of structural, chemical, and semantic drug signals across different DDI prediction architectures. Extensive evaluations across diverse DDI models and DrugBank-based settings show that AIM-DDI consistently improves prediction performance, with the strongest gains under the most challenging both-unseen setting where neither drug in a test pair is observed during training. These results suggest that treating multimodal integration as a reusable module, rather than a model-specific fusion component, is an effective strategy for robust unseen-drug DDI prediction.

---


### 60. [LLM-based Detection of Manipulative Political Narratives](https://arxiv.org/abs/2605.14354)

**<font color=#1a73e8>作者：</font>** Sinclair Schneider, Florian Steuber, Gabi Dreo Rodosek  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a new computational framework for detecting and structuring manipulative political narratives. A task that became more important due to the shift of political discussions to social media. One of the primary challenges thereby is differentiating between manipulative political narratives and legitimate critiques. Some posts may also reframe actual events within a manipulative context.
To achieve good clustering results, we filter manipulative posts beforehand using a detailed few-shot prompt that combines documented campaign narratives with legitimate criticisms to differentiate them. This prompt enables a reasoning model to assign labels, retaining only manipulative narrative posts for further processing.
The remaining posts are subsequently embedded and dimensionality-reduced using UMAP, before HDBSCAN is applied to uncover narrative groups. A key advantage of this unsupervised approach is its independence from a predefined list of target categories, enabling it to uncover new narrative clusters.
Finally, a reasoning model is employed to uncover the narrative behind each cluster. This approach, applied to over 1.2 million social media posts, effectively identified 41 distinct manipulative narrative clusters by integrating prompt-based filtering with unsupervised clustering.

---


### 61. [Herculean: An Agentic Benchmark for Financial Intelligence](https://arxiv.org/abs/2605.14355)

**<font color=#1a73e8>作者：</font>** Xueqing Peng, Zhuohan Xie, Yupeng Cao 等 64 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI agents improve, the central question is no longer whether they can solve isolated well-defined financial tasks, but whether they can reliably carry out financial professional work. Existing financial benchmarks offer only a partial view of this ability, as they primarily evaluate static competencies such as question answering, retrieval, summarization, and classification. We introduce Herculean, the first skilled benchmark for agentic financial intelligence spanning four representative workflows, including Trading, Hedging, Market Insights, and Auditing. Each workflow is instantiated as a standardized MCP-based skill environment with its own tools, interaction dynamics, constraints, and success criteria, enabling consistent end-to-end assessment of heterogeneous agent systems. Across frontier agents, we find agents perform relatively well on Trading and Market Insights, but struggle substantially on Hedging and Auditing, where long-horizon coordination, state consistency, and structured verification are critical. Overall, our results point to a key gap in current agents in turning financial reasoning into dependable workflow execution in high-stakes financial workflows.

---


### 62. [RQ-MoE: Residual Quantization via Mixture of Experts for Efficient Input-Dependent Vector Compression](https://arxiv.org/abs/2605.14359)

**<font color=#1a73e8>作者：</font>** Zhengjia Zhong, Shuyan Ke, Zaizhou Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vector quantization is a fundamental tool for compressing high-dimensional embeddings, yet existing multi-codebook methods rely on static codebooks that limit expressiveness under heterogeneous data geometry. While recent dynamic quantizers like QINCo adapt codebooks to individual inputs and improve expressiveness, their strict sequential dependencies create decoding bottlenecks. We propose Residual Quantization via Mixture of Experts (RQ-MoE), a framework combining a two-level MoE with dual-stream quantization to enable input-dependent codebook adaptation for efficient vector quantization. RQ-MoE enables dynamic codebook construction and decouples instruction from quantization, facilitating parallel decoding. Theoretically, we show that standard Residual Quantization and QINCo can be recovered as constrained special cases of RQ-MoE, and derive a guideline for setting expert dimensionality in RQ-MoE. Extensive experiments show that RQ-MoE achieves state-of-the-art or on-par performance in reconstruction and retrieval, while providing 6x-14x faster decoding than prior vector quantization methods. The implementation is available at this https URL.

---


### 63. [Reinforcement Learning with Semantic Rewards Enables Low-Resource Language Expansion without Alignment Tax](https://arxiv.org/abs/2605.14366)

**<font color=#1a73e8>作者：</font>** Zeli Su, Ziyin Zhang, Zhou Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extending large language models (LLMs) to low-resource languages often incurs an "alignment tax": improvements in the target language come at the cost of catastrophic forgetting in general capabilities. We argue that this trade-off arises from the rigidity of supervised fine-tuning (SFT), which enforces token-level surface imitation on narrow and biased data distributions. To address this limitation, we propose a semantic-space alignment paradigm powered by Group Relative Policy Optimization (GRPO), where the model is optimized using embedding-level semantic rewards rather than likelihood maximization. This objective encourages meaning preservation through flexible realizations, enabling controlled updates that reduce destructive interference with pretrained knowledge. We evaluate our approach on Tibetan-Chinese machine translation and Tibetan headline generation. Experiments show that our method acquires low-resource capabilities while markedly mitigating alignment tax, preserving general competence more effectively than SFT. Despite producing less rigid surface overlap, semantic RL yields higher semantic quality and preference in open-ended generation, and few-shot transfer results indicate that it learns more transferable and robust representations under limited supervision. Overall, our study demonstrates that reinforcement learning with semantic rewards provides a safer and more reliable pathway for inclusive low-resource language expansion.

---


### 64. [Where Should Diffusion Enter a Language Model? Geometry-Guided Hidden-State Replacement](https://arxiv.org/abs/2605.14368)

**<font color=#1a73e8>作者：</font>** Injin Kong, Hyoungjoon Lee, Yohan Jo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion language models lag behind autoregressive transformers, partly because diffusion is applied in spaces poorly suited to language denoising and token recovery. We propose DiHAL, a geometry-guided diffusion-transformer hybrid that asks where diffusion should enter a pretrained transformer. DiHAL scores layers with geometry-based proxies, selects a diffusion-friendly hidden-state interface, and replaces the lower transformer prefix with a diffusion bridge while retaining the upper layers and original LM head. By reconstructing the selected-layer hidden state rather than tokens, DiHAL avoids direct continuous-to-discrete recovery. Experiments on 8B-scale backbones show that the geometry score predicts effective shallow insertion layers under a fixed bridge-training protocol and that hidden-state recovery improves over continuous diffusion baselines in a diagnostic comparison matching the diffusion/recovery training budget. These results suggest that hidden-state geometry helps identify where diffusion-based replacement is feasible inside pretrained language models.

---


### 65. [NodeSynth: Socially Aligned Synthetic Data for AI Evaluation](https://arxiv.org/abs/2605.14381)

**<font color=#1a73e8>作者：</font>** Qazi Mamunur Rashid, Xuan Yang, Zhengzhe Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advancements in generative AI facilitate large-scale synthetic data generation for model evaluation. However, without targeted approaches, these datasets often lack the sociotechnical nuance required for sensitive domains. We introduce NodeSynth, an evidence-grounded methodology that generates socially relevant synthetic queries by leveraging a fine-tuned taxonomy generator (TaG) anchored in real-world evidence. Evaluated against four mainstream LLMs (e.g., Claude 4.5 Haiku), NodeSynth elicited failure rates up to five times higher than human-authored benchmarks. Ablation studies confirm that our granular taxonomic expansion significantly drives these failure rates, while independent validation reveals critical deficiencies in prominent guard models (e.g., Llama-Guard-3). We open-source our end-to-end research prototype and datasets to enable scalable, high-stakes model evaluation and targeted safety interventions (this https URL).

---


### 66. [Nexus : An Agentic Framework for Time Series Forecasting](https://arxiv.org/abs/2605.14389)

**<font color=#1a73e8>作者：</font>** Sarkar Snigdha Sarathi Das, Palash Goyal, Mihir Parmar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series forecasting is not just numerical extrapolation, but often requires reasoning with unstructured contextual data such as news or events. While specialized Time Series Foundation Models (TSFMs) excel at forecasting based on numerical patterns, they remain unaware to real-world textual signals. Conversely, while LLMs are emerging as zero-shot forecasters, their performance remains uneven across domains and contextual grounding. To bridge this gap, we introduce Nexus, a multi-agent forecasting framework that decomposes prediction into specialized stages: isolating macro-level and micro-level temporal fluctuations, and integrating contextual information when available before synthesizing a final forecast. This decomposition enables Nexus to adapt from seasonal signals to volatile, event-driven information without relying on external statistical anchors or monolithic prompting. We show that current-generation LLMs possess substantially stronger intrinsic forecasting ability than previously recognized, depending critically on how numerical and contextual reasoning are organized. Evaluated on data strictly succeeding LLM knowledge cutoffs spanning Zillow real estate metrics and volatile stock market equities, Nexus consistently matches or outperforms state-of-the-art TSFMs and strong LLM baselines. Beyond numerical accuracy, Nexus produces high-quality reasoning traces that explicitly show the fundamental drivers behind each forecast. Our results establish that real-world forecasting is an agentic reasoning problem extending well beyond only sequence modeling.

---


### 67. [Agentic Recommender System with Hierarchical Belief-State Memory](https://arxiv.org/abs/2605.14401)

**<font color=#1a73e8>作者：</font>** Xiang Shen, Yuhang Zhou, Yifan Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory-augmented LLM agents have advanced personalized recommendation, yet existing approaches universally adopt flat memory representations that conflate ephemeral signals with stable preferences, and none provides a complete lifecycle governing how memory should evolve. We propose MARS (Memory-Augmented Agentic Recommender System), a framework that treats recommendation as a partially observable problem and maintains a structured belief state that progressively abstracts noisy behavioral observations into a compact estimate of user preferences. MARS organizes this belief state into three tiers: event memory buffers raw signals, preference memory maintains fine-grained mutable chunks with explicit strength and evidence tracking, and profile memory distills all preferences into a coherent natural language narrative. A complete lifecycle of six operations -- extraction, reinforcement, weakening, consolidation, forgetting, and resynthesis -- is adaptively scheduled by an LLM-based planner rather than fixed-interval heuristics. Experiments on four InstructRec benchmark domains show that \ours achieves state-of-the-art performance with average improvements of 26.4% in HR@1 and 10.3% in NDCG@10 over the strongest baselines with further gains from agentic scheduling in evolving settings.

---


### 68. [DermAgent: A Self-Reflective Agentic System for Dermatological Image Analysis with Multi-Tool Reasoning and Traceable Decision-Making](https://arxiv.org/abs/2605.14403)

**<font color=#1a73e8>作者：</font>** Yize Liu, Siyuan Yan, Ming Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dermatological diagnosis requires integrating fine-grained visual perception with expert clinical knowledge. Although Multimodal Large Language Models (MLLMs) facilitate interactive medical image analysis, their application in dermatology is hindered by insufficient domain-specific grounding and hallucinations. To address these issues, we propose DermAgent, a collaborative multi-tool agent that orchestrates seven specialized vision and language modules within a Plan-Execute-Reflect framework. DermAgent delivers stepwise, traceable diagnostic reasoning through three core components. First, it employs complementary visual perception tools for comprehensive morphological description, dermoscopic concept annotation, and disease diagnosis. Second, to overcome the lack of domain prior, a dual-modality retrieval module anchors every prediction in external evidence by cross-referencing 413,210 diagnosed image cases and 3,199 clinical guideline chunks. To further mitigate hallucinations, a deterministic critic module conducts strict post-hoc auditing via confidence, coverage, and conflict gates, automatically detecting inter-source disagreements to trigger targeted self-correction. Extensive experiments on five dermatology benchmarks demonstrate that DermAgent consistently outperforms state-of-the-art MLLMs and medical agent baselines across zero-shot fine-grained disease diagnosis, concept annotation, and clinical captioning tasks, exceeding GPT-4o by 17.6% in skin disease diagnostic accuracy and 3.15% in captioning ROUGE-L. Our code is available at this https URL.

---


### 69. [GeoViSTA: Geospatial Vision-Tabular Transformer for Multimodal Environment Representation](https://arxiv.org/abs/2605.14406)

**<font color=#1a73e8>作者：</font>** Yuhao Liu, Sadeer Al-Kindi, Ashok Veeraraghavan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale pretraining on Earth observation imagery has yielded powerful representations of the natural and built environment. However, most existing geospatial foundation models do not directly model the structured socioeconomic covariates typically stored in tabular form. This modality gap limits their ability to capture the complete total environment, which is critical for reasoning about complex environmental, social, and health-related outcomes. In this work, we propose GeoViSTA (Geospatial Vision-Tabular Transformer), a vision-tabular architecture that learns unified geospatial embeddings from co-registered gridded imagery and tabular data. GeoViSTA utilizes bilateral cross-attention to exchange spatial and semantic information across modalities, guided by a geography-aware attention mechanism that aligns continuous image patches with irregular census-tract tokens. We train GeoViSTA with a self-supervised joint masked-autoencoding objective, forcing it to recover missing image patches and tabular rows using local spatial context and cross-modal cues. Empirically, GeoViSTA's unified embeddings improve linear probing performance on high-impact downstream tasks, outperforming baselines in predicting disease-specific mortality and fire hazard frequency across held-out regions. These results demonstrate that jointly modeling the physical environment alongside structured socioeconomic context yields highly transferable representations for holistic geospatial inference.

---


### 70. [DVMap: Fine-Grained Pluralistic Value Alignment via High-Consensus Demographic-Value Mapping](https://arxiv.org/abs/2605.14420)

**<font color=#1a73e8>作者：</font>** Pengyun Zhu, Yuqi Ren, Zhen Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current Large Language Models (LLMs) typically rely on coarse-grained national labels for pluralistic value alignment. However, such macro-level supervision often obscures intra-country value heterogeneity, yielding a loose alignment. We argue that resolving this limitation requires shifting from national labels to multi-dimensional demographic constraints, which can identify groups with predictable, high-consensus value preference. To this end, we propose DVMap (High-Consensus Demographic-Value Mapping), a framework for fine-grained pluralistic value alignment. In this framework, we first present a demographic archetype extraction strategy to construct a high-quality value alignment corpus of 56,152 samples from the World Values Survey (WVS) by strictly retaining respondents with consistent value preferences under identical demographics. Over this corpus, we introduce a Structured Chain-of-Thought (CoT) mechanism that explicitly guides LLMs to reason about demographic-value correlations. Subsequently, we employ Group Relative Policy Optimization (GRPO) to achieve adaptive anchoring of value distributions. To rigorously evaluate generalization, we further establish a triple-generalization benchmark (spanning cross-demographic, cross-country, and cross-value) comprising 21,553 samples. Experimental results demonstrate that DVMap effectively learns the manifold mapping from demographics to values, exhibiting strong generalization and robustness. On cross-demographic tests, Qwen3-8B-DVMap achieves 48.6% accuracy, surpassing the advanced open-source LLM DeepSeek-v3.2 (45.1%). The source code and dataset are available at this https URL.

---


### 71. [BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE](https://arxiv.org/abs/2605.14438)

**<font color=#1a73e8>作者：</font>** Juntong Wu, Jialiang Cheng, Qishen Yin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures enhance the efficiency of large language models by activating only a subset of experts per token. However, standard MoE employs a fixed Top-K routing strategy, leading to redundant computation and suboptimal inference latency. Existing acceleration methods either require costly retraining with architectural changes or suffer from severe performance drop at high sparsity due to train-inference mismatch. To address these limitations, we propose BEAM (Binary Expert Activation Masking), a novel method that learns token-adaptive expert selection via trainable binary masks. With a straight-through estimator and an auxiliary regularization loss, BEAM induces dynamic expert sparsity through end-to-end training while maintaining model capability. We further implement an efficient custom CUDA kernel for BEAM, ensuring seamless integration with the vLLM inference framework. Experiments show that BEAM retains over 98\% of the original model's performance while reducing MoE layer FLOPs by up to 85\%, achieving up to 2.5$\times$ faster decoding and 1.4$\times$ higher throughput, demonstrating its effectiveness as a practical, plug-and-play solution for efficient MoE inference.

---


### 72. [Prompting Policies for Multi-step Reasoning and Tool-Use in Black-box LLMs with Iterative Distillation of Experience](https://arxiv.org/abs/2605.14443)

**<font color=#1a73e8>作者：</font>** Krishna Sayana, Ketan Todi, Ambarish Jash  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The shift toward interacting with frozen, "black-box" Large Language Models (LLMs) has transformed prompt engineering from a heuristic exercise into a critical optimization challenge. We propose a Reinforcement Learning (RL) framework for training learned prompting policies via iterative distillation of experience. In this architecture, a lightweight prompter model is optimized to maximize task-specific rewards for a larger, frozen worker LLM. By utilizing a contrastive experience buffer that couples scalar rewards with dense textual critiques, our approach effectively amortizes iterative prompt refinement into single-shot policy weights.
Our experimental analysis focuses on the Big Bench Extra Hard (BBEH) and Tau-bench suites, covering a diverse range of multi-step reasoning and tool-use tasks. We demonstrate significant gains, improving performance from 55% to 90% in logic-intensive reasoning and 74% to 91% in tool-use tasks. Furthermore, we analyze the structural evolution of prompts, demonstrating how the policy discovers specialized algorithmic heuristics. We provide comprehensive comparisons against state-of-the-art evolutionary baselines like GEPA, showing that iterative distillation achieves superior performance with higher sample efficiency.

---


### 73. [Think When Needed: Adaptive Reasoning-Driven Multimodal Embeddings with a Dual-LoRA Architecture](https://arxiv.org/abs/2605.14448)

**<font color=#1a73e8>作者：</font>** Longxiang Zhang, Weilong Dai, Guanghao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have emerged as a powerful backbone for multimodal embeddings. Recent methods introduce chain-of-thought (CoT) reasoning into the embedding pipeline to improve retrieval quality, but remain costly in both model size and inference cost. They typically employ separate reasoner and embedder with substantial parameter overhead, and generate CoT indiscriminately for every input. However, we observe that for simple inputs, discriminative embeddings already perform well, and redundant reasoning can even mislead the model, degrading performance. To address these limitations, we propose Think When Needed (TWN), a unified multimodal embedding framework with adaptive reasoning. TWN introduces a dual-LoRA architecture that attaches reasoning and embedding adapters to a shared frozen backbone, detaching gradients at their interface to mitigate gradient conflicts introduced by joint optimization while keeping parameters close to a single model. Building on this, an adaptive think mechanism uses a self-supervised routing gate to decide per input whether to generate CoT, skipping unnecessary reasoning to reduce inference overhead and even improve retrieval quality. We further explore embedding-guided RL to optimize CoT quality beyond supervised training. On the 78 tasks of MMEB-V2, TWN achieves state-of-the-art embedding quality while being substantially more efficient than existing generative methods, requiring only 3-5% additional parameters relative to the backbone and up to 50% fewer reasoning tokens compared to the full generative mode.

---


### 74. [Stateful Reasoning via Insight Replay](https://arxiv.org/abs/2605.14457)

**<font color=#1a73e8>作者：</font>** Bin Lei, Caiwen Ding, Jiachen Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) reasoning has become a foundation for eliciting multi-step reasoning in large language models, but recent studies show that its benefits do not scale monotonically with chain length: while longer CoT generally enables a model to tackle harder problems, on a given problem, accuracy typically increases with CoT length up to a point, after which it declines. We identify a major cause of this phenomenon: as the CoT grows, the model's attention to critical insights produced earlier in the trace gradually weakens, making those insights progressively less accessible when they are most needed. Therefore, we propose \textbf{InsightReplay}, a stateful reasoning approach in which the model periodically extracts critical insights from its reasoning trace and replays them near the active generation frontier, keeping them accessible as the reasoning scales. Extensive experiments on a $\mathbf{2}\!\times\!\mathbf{3}\!\times\!\mathbf{4}$ benchmark grid, covering model scales $\{\text{8B}, \text{30B}\}$, model families $\{\text{Qwen3.5}, \text{DeepSeek-R1-Distill-Qwen}, \text{Gemma-4}\}$, and reasoning benchmarks $\{\text{AIME}, \text{HMMT}, \text{GPQA Diamond}, \text{LiveCodeBench v5}\}$, show that 3-round InsightReplay yields accuracy gains across \textbf{all 24 settings}, with an averaged improvement of $\mathbf{+1.65}$ points over standard CoT, and a largest single-setting gain of $\mathbf{+9.2}$ points on R1-Distill-32B's LiveCodeBench v5 subset. Our results suggest that the effectiveness of test-time scaling depends not only on how much a model reasons, but also on whether critical intermediate insights remain accessible throughout long reasoning trajectories.

---


### 75. [OmniDrop: Layer-wise Token Pruning for Omni-modal LLMs via Query-Guidance](https://arxiv.org/abs/2605.14458)

**<font color=#1a73e8>作者：</font>** Yeo Jeong Park, Hyemi Jang, Minseo Choi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models have demonstrated remarkable potential in holistic multimodal understanding; however, the token explosion caused by high-resolution audio and video inputs remains a critical bottleneck for real-time applications and long-form reasoning. Existing omni-modal token compression methods typically prune tokens at the input embedding level, relying on audio-video similarity or temporal co-occurrence as proxies for semantic relevance. In practice, such assumptions are often unreliable. To address this limitation, we propose OmniDrop, a training-free, layer-wise token pruning framework that progressively prunes audiovisual tokens within the LLM decoder layers rather than at the input-level, allowing early layers to preserve sufficient omni-modal information fusion before aggressively removing tokens in deeper layers. We further utilize text queries as guidance for modality-agnostic and task-adaptive token pruning. We also introduce a temporal diversity score that encourages balanced token survival to preserve global temporal context. Experimental results across various audiovisual benchmarks demonstrate that OmniDrop outperforms all baselines by up to 3.58 points while reducing prefill latency by up to 40% and memory usage by up to 14.7%.

---


### 76. [Does RAG Know When Retrieval Is Wrong? Diagnosing Context Compliance under Knowledge Conflict](https://arxiv.org/abs/2605.14473)

**<font color=#1a73e8>作者：</font>** Yihang Chen, Pin Qian, Su Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Context-Compliance Regime in Retrieval-Augmented Generation (RAG) occurs when retrieved context dominates
the final answer even when it conflicts with the model's parametric knowledge. Accuracy alone does not reveal
how retrieved context causally shapes answers under such conflict. We introduce Context-Driven Decomposition
(CDD), a belief-decomposition probe that operates at inference time and serves as an intervention mechanism for
controlled retrieval conflict. Across Epi-Scale stress tests, TruthfulQA misconception injection, and cross-
model reruns, CDD exposes three patterns. P1: context compliance is measurable in an upper-bound adversarial
setting, where Standard RAG reaches 15.0% accuracy on TruthfulQA misconception injection (N=500). P2:
adversarial accuracy gains transfer across model families: CDD improves accuracy on Gemini-2.5-Flash and on
Claude Haiku/Sonnet/Opus, but rationale-answer causal coupling does not transfer. CDD reaches 64.1% mistake-
injection causal sensitivity on Gemini-2.5-Flash, while sensitivities for all three Claude variants fall in the
[-3%, +7%] range, suggesting that the Claude-side accuracy gains operate through a mechanism distinct from the
explicit conflict-resolution trace. P3: explicit conflict decomposition improves robustness under temporal
drift and noisy distractors, with CDD reaching 71.3% on temporal shifts and 69.9% on distractor evidence on the
full Epi-Scale adversarial benchmark. These three patterns identify context-compliance as a structural axis
along which standard RAG can be probed and intervened on, distinct from retrieval-quality or single-method
robustness questions, and motivate releasing Epi-Scale for systematic study across model families and retrieval
pipelines.

---


### 77. [Deepchecks: Evaluating Retrieval-Augmented Generation (RAG)](https://arxiv.org/abs/2605.14488)

**<font color=#1a73e8>作者：</font>** Assaf Gerner, Netta Madvil, Nadav Barak 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) augmented with Retrieval-Augmented Generation (RAG) techniques are revolutionizing applications across multiple domains, such as healthcare, finance, and customer service. Despite their potential, evaluating RAG systems remains a complex challenge due to the stochastic nature of generated outputs and the intricate interplay between retrieval and generation components. This paper introduces Deepchecks, a comprehensive framework tailored for evaluating RAG applications. Deepchecks' evaluation framework addresses RAG applications evaluation through a multi-faceted approach, root cause analysis and production monitoring. By ensuring alignment with application-specific requirements, Deepchecks framework provides a robust foundation for assessing reliability, relevance, and user satisfaction in RAG systems.

---


### 78. [GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations](https://arxiv.org/abs/2605.14498)

**<font color=#1a73e8>作者：</font>** Jingbo Yang, Kwei-Herng Lai, Xiaowen Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents increasingly serve as personal assistants and workplace collaborators, where their utility depends on memory systems that extract, retrieve, and apply information across long-running conversations. However, both existing memory systems and benchmarks are built around the dyadic, single-user setup, even though real deployments routinely span groups and channels with multiple users interacting with the agent and with each other. This mismatch leaves three properties of group memory unmeasured: (i) group dynamics that go beyond concatenated one-on-one chats, (ii) speaker-grounded belief tracking, where the per-user memory modeling is needed, and (iii) audience-adapted language, where Theory-of-Mind shifts produce role-specific vocabulary. We introduce GroupMemBench, a benchmark that exposes all three. A graph-grounded synthesis pipeline produces multi-party conversations with controllable reply structure and conditions each message on per-user personas and target audiences. An adversarial query pipeline then binds every question to a specific asker across six categories, spanning multi-hop reasoning, knowledge update, term ambiguity, user-implicit reasoning, temporal reasoning, and abstention, and iteratively searches challenging, realistic queries that reflect comprehensive memory capability. Benchmarking leading memory systems exposes a sharp collapse: the strongest one reaches only 46.0% average accuracy, with knowledge update at 27.1% and term ambiguity at 37.7%, while a simple BM25 baseline matches or exceeds most agent memory systems. This indicates current memory ingestion erases the structural and lexical features group memory depends on, leaving multi-user memory far from solved.

---


### 79. [When Robots Do the Chores: A Benchmark and Agent for Long-Horizon Household Task Execution](https://arxiv.org/abs/2605.14504)

**<font color=#1a73e8>作者：</font>** Zilin Zhu, Longteng Guo, Yanghong Mei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon household tasks demand robust high-level planning and sustained reasoning capabilities, which are largely overlooked by existing embodied AI benchmarks that emphasize short-horizon navigation or manipulation and rely on fixed task categories. We introduce LongAct, a benchmark designed to evaluate planning-level autonomy in long-horizon household tasks specified through free-form instructions. By abstracting away embodiment-specific low-level control, LongAct isolates high-level cognitive capabilities such as instruction understanding, dependency management, memory maintenance, and adaptive planning. We further propose HoloMind, a VLM-driven agent with a DAG-based long-horizon hierarchical planner, a Multimodal Spatial Memory for persistent world modeling, an Episodic Memory for experience reuse, and a global Critic for reflective supervision. Experiments with GPT-5 and Qwen3-VL models show that HoloMind substantially improves long-horizon performance while reducing reliance on model scale. Even top models achieve only 59% goal completion and 16% full-task success, underscoring the difficulty of LongAct and the need for stronger long-horizon planning in embodied agents.

---


### 80. [Dimension-Level Intent Fidelity Evaluation for Large Language Models: Evidence from Structured Prompt Ablation](https://arxiv.org/abs/2605.14517)

**<font color=#1a73e8>作者：</font>** GAng Peng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Holistic evaluation scores capture overall output quality but do not distinguish whether a model reproduced the structural form of a user's request from whether it preserved the user's specific intent. We propose a dimension-level intent fidelity evaluation framework, applied here through a structured prompt ablation study across 2,880 outputs spanning three languages, three task domains, and six LLMs, that separately measures structural recovery and intent fidelity for each semantic dimension. This framework reveals a systematic structural-fidelity split: among Chinese-language outputs with complete paired scores, 25.7% received perfect holistic alignment scores (GA=5) while exhibiting measurable dimensional intent deficits; among English-language outputs, this proportion rose to 58.6%. Human evaluation confirmed that these split-zone outputs represent genuine quality deficits and that dimensional fidelity scores track human judgements more reliably than holistic scores do. A public-private decomposition of 2,520 ablation cells characterises when models successfully compensate for missing intent and when they fail, while proxy annotation distinguishes prior inferability from default recoverability. A weight-perturbation experiment shows that moderate misalignment is typically absorbed, whereas severe dimensional inversion is consistently harmful. These findings demonstrate that dimension-level intent fidelity evaluation is a necessary complement to holistic assessment when evaluating LLM outputs for user-specific tasks.

---


### 81. [Lang2MLIP: End-to-End Language-to-Machine Learning Interatomic Potential Development with Autonomous Agentic Workflows](https://arxiv.org/abs/2605.14527)

**<font color=#1a73e8>作者：</font>** Wenwen Li, Yuki Orimo, Nontawat Charoenphakdee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Developing machine learning interatomic potentials (MLIPs) for complex materials systems remains challenging because it requires expertise in atomistic simulations, machine learning, and workflow design, as well as iterative active learning procedures. Existing automated pipelines typically assume a fixed sequence of stages or depend on domain experts, which limits their adaptability to heterogeneous materials systems where the optimal curriculum is not known in advance. To lower the barrier to developing MLIPs for non-experts, we propose Lang2MLIP, a multi-agent framework that takes natural-language input and formulates end-to-end MLIP development as a sequential decision-making problem solved by large language models (LLMs). At each step, a decision-making agent observes the current dataset, model, evaluation results, and execution log, and then automatically selects an appropriate action to improve the model. This removes the need for a predefined pipeline and enables the agent to self-correct by revisiting earlier subsystems when new failures arise. We evaluate this approach on a solid electrolyte interphase (SEI) system with multiple components and interfaces. These results suggest that LLM-based multi-agent systems are a promising direction for automating MLIP development and making it more accessible to non-experts.

---


### 82. [Mitigating Mask Prior Drift and Positional Attention Collapse in Large Diffusion Vision-Language Models](https://arxiv.org/abs/2605.14530)

**<font color=#1a73e8>作者：</font>** Sujung Hong, Chanyong Yoon, Seongjae Hwang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large diffusion vision-language models (LDVLMs) have recently emerged as a promising alternative to autoregressive models, enabling parallel decoding for efficient inference and leveraging bidirectional attention for global context. Despite these advances, their behavior under long-form generation remains underexplored. In this work, we show that existing LDVLMs suffer from repetitive generation and degraded visual grounding, and identify two underlying causes. First, repetitive generation originates from a mask token prior: since generation tokens are initialized as mask tokens, their hidden representations progressively drift toward a shared prior direction over generation steps. Second, a fundamental misalignment between the positional attention bias and the iterative unmasking process suppresses attention toward informative visual tokens, degrading visual grounding. Based on these insights, we propose a training-free approach, introducing Mask Prior Suppression and Monotonic RoPE Scaling to mitigate mask prior drift and positional attention collapse during decoding. Experiments on general multimodal benchmarks and visual grounding tasks demonstrate improvements over baseline LDVLMs, with robust gains on long-form description benchmarks. Our results show that these failures can be effectively addressed with a lightweight, plug-and-play strategy that requires no additional training and generalizes across diverse LDVLM architectures.

---


### 83. [Exploring Geographic Relative Space in Large Language Models through Activation Patching](https://arxiv.org/abs/2605.14535)

**<font color=#1a73e8>作者：</font>** Stef De Sabbata, Rahul Baiju, Stefano Mizzaro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The increased use of Large Language Models (LLMs) in geography raises substantial questions about the safety of integrating these tools across a wide range of processes and analyses, given our very limited understanding of their inner workings. In this extended abstract, we examine how LLMs process relative geographic space using activation patching, an emerging tool for mechanistic interpretability.

---


### 84. [Cattle Trade: A Multi-Agent Benchmark for LLM Bluffing, Bidding, and Bargaining](https://arxiv.org/abs/2605.14537)

**<font color=#1a73e8>作者：</font>** Robert Müller, Clemens Müller  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce \textsc{Cattle Trade, a multi-agent benchmark for evaluating large language models (LLMs) as agents in strategic reasoning under imperfect information, adversarial interaction, and resource constraints. The benchmark combines auctions, hidden-offer trade challenges (TCs), bargaining, bluffing, opponent modeling, and resource allocation within a single long-horizon game lasting 50--60 turns. Unlike prior agent benchmarks that test these abilities in isolation, \textsc{Cattle Trade} evaluates whether agents integrate them across a competitive, multi-agent economic game with conflicting incentives. The benchmark logs every bid, TC offer, counteroffer, and card selection, enabling behavioural analysis beyond final scores or win rates. We evaluate seven cost-efficient language models and three deterministic code agents across 242 games. Strategic coherence, in particular spending efficiency, resource discipline, and phase-adaptive bidding, is associated with rank more strongly than spending volume or any single subskill. Two heuristic code agents outperform most tested LLMs, and behavioural traces surface recurring LLM failure modes including overbidding, self-bidding, bankrupt TC initiation, and weak opponent-state adaptation. Evaluating agentic competence requires benchmarks that test the joint deployment of multiple capabilities in multi-agent environments with conflicting incentives, uncertainty, and economic dynamics.

---


### 85. [VerbalValue: A Socially Intelligent Virtual Host for Sales-Driven Live Commerce](https://arxiv.org/abs/2605.14542)

**<font color=#1a73e8>作者：</font>** Yuyan Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A skilled live-commerce host is not merely a narrator, but a sales agent who converts viewer curiosity into purchase intent through expert product knowledge, emotionally intelligent response tactics, and entertainment that serves as a vehicle for product exposure. Yet no existing AI system replicates this: conversational recommenders treat recommendation as a terminal act, while general-purpose LLMs hallucinate product claims and default to generic promotional templates that fail to engage or persuade. We present VerbalValue, a sales-conversion-oriented virtual host that turns exceptional verbal ability into real commercial value, built on three contributions. First, we construct a domain knowledge base of product specifications and a curated sales terminology lexicon that anchor product-related responses in verified expertise. Second, we collect and annotate 1,475 live-commerce interactions spanning diverse viewer intents. Third, we fine-tune a large language model on this data to deliver empathetic, commercially oriented responses, adapting to viewer intent through empathetic amplification, evidence-backed rebuttal, and humor-mediated deflection. Experiments against GPT-5.4, Claude Sonnet 4.6, Gemini 3.1 Pro, and other baselines demonstrate gains of 23% on informativeness and 18% on factual correctness, with consistent advantages in tactfulness and viewer engagement.

---


### 86. [RxEval: A Prescription-Level Benchmark for Evaluating LLM Medication Recommendation](https://arxiv.org/abs/2605.14543)

**<font color=#1a73e8>作者：</font>** Shuhao Chen, Weisen Jiang, Changmiao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inpatient medication recommendation requires clinicians to repeatedly select specific medications, doses, and routes as a patient's condition evolves. Existing benchmarks formulate this task as admission-level prediction over coarse drug codes with multi-hot diagnostic and procedure code inputs, failing to capture the per-timepoint, information-rich nature of real prescribing. We propose RxEval, a prescription-level benchmark that evaluates LLM prescribing capability by multiple-choice questions: each question presents a detailed patient profile and time-ordered clinical trajectory, requiring selection of specific medication-dose-route triples from real prescriptions and patient-specific distractors generated via reasoning-chain perturbation. RxEval comprises 1,547 questions spanning 584 patients, 18 diagnostic categories, and 969 unique medications. Evaluation of 16 LLMs shows that RxEval is both challenging and discriminative: F1 ranges from 45.18 to 77.10 across models, and the best Exact Match is only 46.10%. Error analysis reveals that even frontier models may overlook stated patient information and fail to derive clinical conclusions.

---


### 87. [Complacent, Not Sycophantic: Reframing Large Language Models and Designing AI Literacy for Complacent Machines](https://arxiv.org/abs/2605.14544)

**<font color=#1a73e8>作者：</font>** Federico Germani, Giovanni Spitale  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are often described as sycophantic, in the sense that they appear to flatter users or mirror their beliefs. We argue that this label is conceptually misleading: sycophancy implies motives and strategic intent, which LLMs do not possess. Their behaviour is better understood as complacency, a structural tendency to agree with user input because training data, reward signals and design favour agreement and reinforcement over correction. We argue that this distinction matters. Whether developers act sycophantically or not, models themselves never are sycophants; they can only be made more or less complacent. This reframing locates agency in developers and institutions, not in the model. Because complacent models reinforce users' prior beliefs, we argue that AI literacy educational approaches should particularly focus on strategies to counter confirmation bias.

---


### 88. [TeachAnything: A Multimodal Crowdsourcing Platform for Training Embodied AI Agents in Symmetrical Reality](https://arxiv.org/abs/2605.14556)

**<font color=#1a73e8>作者：</font>** Zidong Liu, Rongkai Liu, Yue Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Symmetrical Reality (SR) is emerging as a future trend for human-agent coexistence, placing higher demands on agents to acquire human-like intelligence. It calls for richer and more diverse human guidance. We introduce a three-stage demonstration paradigm integrating multimodal demonstration signals. Building on this paradigm, we developed TeachAnything, a cloud-based, crowdsourcing-oriented demonstration platform with physics simulation capable of collecting diverse demonstration data across varied scenes, tasks, and embodiments. By unifying virtual and physical interactions through both methodological design and physics simulation, the system serves as a practical foundation for developing embodied agents aligned with Symmetrical Reality.

---


### 89. [Resolving Action Bottleneck: Agentic Reinforcement Learning Informed by Token-Level Energy](https://arxiv.org/abs/2605.14558)

**<font color=#1a73e8>作者：</font>** Langzhou He, Junyou Zhu, Yue Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning trains large language models using multi-turn trajectories that interleave long reasoning traces with short environment-facing actions. Common policy-gradient methods, such as PPO and GRPO, treat each token in a trajectory equally, leading to uniform credit assignment. In this paper, we critically demonstrate that such uniform credit assignment largely misallocates token-level training signals. From an energy-based modeling perspective, we show that token-level training signals, quantified by their correlations with reward variance of different rollouts sampled from a given prompt, concentrate sharply on action tokens rather than reasoning tokens, even though action tokens account for only a small fraction of the trajectory. We refer to this phenomenon as the Action Bottleneck. Motivated by this observation, we propose an embarrassingly simple token reweighting approach, ActFocus, that downweights gradients on reasoning tokens, along with an additional energy-based redistribution mechanism that further increases the weights on action tokens with higher uncertainty. Across four environments and different model sizes, ActFocus consistently outperforms PPO and GRPO, yielding final-step gains of up to 65.2 and 63.7 percentage points, respectively, without any additional runtime or memory cost.

---


### 90. [Prompt Segmentation and Annotation Optimisation: Controlling LLM Behaviour via Optimised Segment-Level Annotations](https://arxiv.org/abs/2605.14561)

**<font color=#1a73e8>作者：</font>** Devika Prasad, Luke Gerschwitz, Tong Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt engineering is crucial for effective interaction with generative artificial intelligence systems, yet existing optimisation methods often operate over an unstructured and vast prompt space, leading to high computational costs and potential distortions of the original intent. We introduce Prompt Segmentation and Annotation Optimisation (PSAO), a structured prompt optimisation framework designed to improve prompt optimisation controllability and efficiency. PSAO decomposes a prompt into interpretable segments (e.g., sentences) and augments each with human-readable annotations (e.g., {not important}, {important}, {very important}). These annotations guide large language models (LLMs) in allocating focus and clarifying confusion during response generation. We formally define the segmentations and annotations and demonstrate that optimised segment-level annotations can lead to improved LLM responses, with the original prompt retained as a candidate in the optimisation space to prevent performance degradation. Empirical evaluations indicate that PSAO benefits from annotations in terms of improved reasoning accuracy and self-consistency. However, developing efficient methods for identifying optimal segmentations and annotations remains challenging and is reserved for future investigation. This work is intended as a proof of concept, demonstrating the feasibility and potential of segment-level annotation optimisation.

---


### 91. [EndPrompt: Efficient Long-Context Extension via Terminal Anchoring](https://arxiv.org/abs/2605.14589)

**<font color=#1a73e8>作者：</font>** Han Tian, Luxuan Chen, Xinran Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extending the context window of large language models typically requires training on sequences at the target length, incurring quadratic memory and computational costs that make long-context adaptation expensive and difficult to reproduce. We propose EndPrompt, a method that achieves effective context extension using only short training sequences. The core insight is that exposing a model to long-range relative positional distances does not require constructing full-length inputs: we preserve the original short context as an intact first segment and append a brief terminal prompt as a second segment, assigning it positional indices near the target context length. This two-segment construction introduces both local and long-range relative distances within a short physical sequence while maintaining the semantic continuity of the training text--a property absent in chunk-based simulation approaches that split contiguous context. We provide a theoretical analysis grounded in Rotary Position Embedding and the Bernstein inequality, showing that position interpolation induces a rigorous smoothness constraint over the attention function, with shared Transformer parameters further suppressing unstable extrapolation to unobserved intermediate distances. Applied to LLaMA-family models extending the context window from 8K to 64K, EndPrompt achieves an average RULER score of 76.03 and the highest average on LongBench, surpassing LCEG (72.24), LongLoRA (72.95), and full-length fine-tuning (69.23) while requiring substantially less computation. These results demonstrate that long-context generalization can be induced from sparse positional supervision, challenging the prevailing assumption that dense long-sequence training is necessary for reliable context-window extension. The code is available at this https URL.

---


### 92. [TOPOS: High-Fidelity and Efficient Industry-Grade 3D Head Generation](https://arxiv.org/abs/2605.14594)

**<font color=#1a73e8>作者：</font>** Bojun Xiong, Zoubin Bi, Xinghui Peng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity 3D head generation plays a crucial role in the film, animation and video game industries. In industrial pipelines, studios typically enforce a fixed reference topology across all head assets, as such a clean and uniform topology is a prerequisite for production-level rigging, skinning and animation. In this paper, we present TOPOS, a framework tailored for single image conditioned 3D head generation that jointly recovers geometry and appearance under such an industry-standard topology. In contrast to general 3D generative models which produce triangle meshes with inconsistent topology and numerous vertices, hindering semantic correspondence and asset-level reuse, TOPOS generates head meshes with a fixed, studio-style topology, enabling consistent vertex-level correspondence across all generated heads. To model heads under this unified topology, we proposed a novel variational autoencoder structure, termed TOPOS-VAE. Inspired by multi-model large language models (MLLMs), our TOPOS-VAE leverages the Perceiver Resampler to convert input pointclouds sampled from head meshes of diverse topologies into the target reference topology. Building upon TOPOS-VAE's structured latent space, we train a rectified flow transformer, TOPOS-DiT, to efficiently generate high-fidelity head meshes from a single image. We further present TOPOS-Texture, an end-to-end module that produces relightable UV texture maps from the same portrait image via fine-tuning a multimodal image generative model. The generated textures are spatially aligned with the underlying mesh geometry and faithfully preserve high-frequency appearance details. Extensive experiments demonstrate that TOPOS achieves state-of-the-art performance on 3D head generation, surpassing both classical face reconstruction methods and general 3D object generative models, highlighting its effectiveness for digital human creation.

---


### 93. [Sycophancy is an Educational Safety Risk: Why LLM Tutors Need Sycophancy Benchmarks](https://arxiv.org/abs/2605.14604)

**<font color=#1a73e8>作者：</font>** Enkelejda Kasneci, Gjergji Kasneci  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This position paper argues that effective tutoring requires corrective friction: surfacing misconceptions and challenging them supportively to drive conceptual change. Yet preference-aligned LLMs can trade epistemic rigor for agreeableness. We identify a Reasoning-Sycophancy Paradox: models that resist context-switch frame attacks can still capitulate under social-epistemic pressure, especially authority ("my notes say I'm right") and social-affective face-saving ("please don't tell me I'm wrong"). We introduce EduFrameTrap, a tutoring benchmark across math, physics, economics, chemistry, biology, and computer science that varies student confidence and pressure (context-switch, authority, social-affective). Across two frontier LLMs, context-switch failures are comparatively lower for GPT-5.2, while authority and social pressure more often trigger epistemic retreat. In contrast, Claude shows substantial context-switch fragility in this run. Because these failures are hard to judge automatically, we report two-judge disagreement as a reliability signal. We argue benchmarks should measure social-epistemic courage, i.e., supportive but corrective tutoring, and treat kind-but-correct behavior as a safety requirement.

---


### 94. [Do We Really Need External Tools to Mitigate Hallucinations? SIRA: Shared-Prefix Internal Reconstruction of Attribution](https://arxiv.org/abs/2605.14621)

**<font color=#1a73e8>作者：</font>** Tian Qin, Junzhe Chen, Yuqing Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) often hallucinate when language priors dominate weak or ambiguous visual evidence. Existing contrastive decoding methods mitigate this problem by comparing predictions from the original image with those from externally perturbed visual inputs, but such references can introduce off-manifold artifacts and require costly extra forward passes. We propose SIRA, a training-free internal contrastive decoding framework that constructs a counterfactual reference inside the same LVLM by exploiting the staged information flow of multimodal transformers. Instead of removing visual information from the input, SIRA first lets image and text tokens interact through a shared prefix, forming an aligned multimodal state that preserves prompt interpretation, decoding history, positional structure, and early visual grounding. It then forks a counterfactual branch in later transformer layers, where attention to image-token positions is masked. This branch retains the shared multimodal context but lacks continued access to fine-grained visual evidence, yielding a language-prior-dominated internal reference for token-level contrast. During decoding, SIRA suppresses tokens that remain strong without late visual access and favors predictions whose advantage depends on the full visual pathway. Experiments on POPE, CHAIR, and AMBER with Qwen2.5-VL and LLaVA-v1.5 show that SIRA consistently reduces hallucinations while preserving descriptive coverage and incurring lower overhead than two-pass contrastive decoding. SIRA requires no training, external verifier, or perturbed input, and applies to open-weight LVLMs with white-box inference access.

---


### 95. [MultiEmo-Bench: Multi-label Visual Emotion Analysis for Multi-modal Large Language Models](https://arxiv.org/abs/2605.14635)

**<font color=#1a73e8>作者：</font>** Tianwei Chen, Takuya Furusawa, Yuki Hirakawa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces a multi-label visual emotion analysis benchmark dataset for comprehensively evaluating the ability of multimodal large language models (MLLMs) to predict the emotions evoked by images. Recent user studies report an unintuitive finding: humans may prefer the predictions of MLLMs over the labels in existing datasets. We argue that this phenomenon stems from the suboptimal annotation scheme used in existing datasets, where each annotator is shown a single candidate emotion for each image and judges whether it is evoked or not. This approach is clearly limited because a single image can evoke multiple emotions with varying intensities. As a result, evaluations based on these datasets may underestimate the capabilities of MLLMs, yet an appropriate benchmark for evaluating such models remains lacking. To address this issue, we introduce a new multi-label benchmark dataset for visual emotion analysis toward MLLMs evaluation. We hire $20$ annotators per image and ask them to select all emotions they feel from an image. Then, we aggregate the votes across all annotators, providing a more reliable and representative dataset labeled with a distribution of emotions. The resulting dataset contains $10,344$ images with $236,998$ valid votes across eight emotions. Based on this benchmark dataset, we evaluate several recent models, including Qwen3-VL, OpenAI's GPT, Gemini, and Claude. We assess model performance on both dominant emotion prediction and emotion distribution prediction. Our results demonstrate the progress achieved by recent MLLMs while also indicating that substantial room for improvement remains. Furthermore, our experiments with LLM-as-a-judge show that the method does not consistently improve MLLMs' performance, indicating its limitations for the subjective task of visual emotion analysis.

---


### 96. [Teaching Large Language Models When Not to Know: Learning Temporal Critique for Ex-Ante Reasoning](https://arxiv.org/abs/2605.14636)

**<font color=#1a73e8>作者：</font>** Chenlu Ding, Jiancan Wu, Yanchen Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often fail to reason under temporal cutoffs: when prompted to answer from the standpoint of an earlier time, they exploit knowledge that became available only later. We study this failure through the lens of ex-ante reasoning, where a model must rely exclusively on information knowable before a cutoff. Through a systematic analysis of prompt-level interventions, we find that temporal leakage is highly sensitive to cutoff formulation and instruction placement: explicit cutoff statements outperform implicit historical framings, and prefix constraints reduce leakage more effectively than suffix constraints. These findings indicate that prompting can steer models into a temporal frame, but does not endow them with the ability to verify whether a response is temporally admissible. We further argue that supervised fine-tuning is insufficient, since ex-ante correctness is not an intrinsic property of an answer, but a relation between the answer and the cutoff. To address this gap, we propose TCFT, a Temporal Critique Fine-Tuning framework that trains models to acquire cutoff-aware temporal verification. Given a query, a cutoff, and a candidate response, TCFT teaches the model to identify post-cutoff leakage, explain temporal boundary violations, and judge temporal admissibility. Experiments with Qwen2.5-7B-Instruct and Qwen2.5-14B-Instruct show that TCFT consistently outperforms prompting and SFT baselines, reducing average leakage by 41.89 and 37.79 percentage points, respectively.

---


### 97. [Falkor-IRAC: Graph-Constrained Generation for Verified Legal Reasoning in Indian Judicial AI](https://arxiv.org/abs/2605.14665)

**<font color=#1a73e8>作者：</font>** Joy Bose  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Legal reasoning is not semantic similarity search. A court judgment encodes constrained symbolic reasoning: precedent propagation, procedural state transitions, and statute-bound inference. These are properties that vector-based retrieval-augmented generation (RAG) cannot faithfully represent. Hallucinated precedents, outdated statute citations, and unsupported reasoning chains remain persistent failure modes in LLM-based legal AI, with real consequences for access to justice in high-caseload jurisdictions such as India. This paper presents Falkor-IRAC, a graph-constrained generation framework for Indian legal AI that grounds generation in structured reasoning over an IRAC (Issue, Rule, Analysis, Conclusion) knowledge graph. Judgments from the Supreme Court and High Courts of India are ingested as IRAC node structures enriched with procedural state transitions, precedent relationships, and statutory references, stored in FalkorDB for low-latency agentic traversal. At inference time, LLM-generated answers are accepted only if a valid supporting path can be traced through the graph, a check performed by a falsifiability oracle called the Verifier Agent. The system also detects doctrinal conflicts as a first-class output rather than silently resolving them. Falkor-IRAC is evaluated using graph-native metrics: citation grounding accuracy, path validity rate, hallucinated precedent rate, and conflict detection rate. These metrics are argued to be more appropriate for legal reasoning evaluation than BLEU and ROUGE. On a proof-of-concept corpus of 51 Supreme Court judgments, the Verifier Agent correctly validated citations on completed queries and correctly rejected fabricated citations. Evaluation against vector-only RAG baselines is left for future work, as is GPU-accelerated inference to address current timeout rates on CPU hardware.

---


### 98. [AI-assisted cultural heritage dissemination: Comparing NMT and glossary-augmented LLM translation in rock art documents](https://arxiv.org/abs/2605.14679)

**<font color=#1a73e8>作者：</font>** Vicent Briva-Iglesias, María Ferre-Fernández  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cultural heritage institutions increasingly disseminate research and interpretive materials globally, but multilingual dissemination is constrained by limited budgets and staffing. In terminology-dense domains such as rock art, translation quality depends on accurate, consistent specialised terms, and small lexical errors can mislead non-specialists and reduce reuse. We compare three English MT setups for a Spanish academic rock art text, focusing on simple, operationally feasible interventions rather than complex model-side modifications: (1) DeepL as a strong NMT baseline, (2) Gemini-Simple (LLM with a basic prompt), and (3) Gemini-RAG (the same LLM with glossary-augmented prompting via term-pair retrieval). Using PEARMUT, we conduct a human evaluation via (i) multi-way Direct Assessment (0--100) and (ii) targeted terminology auditing with a restricted MQM taxonomy. Gemini-RAG yields the highest exact-match terminology accuracy (81.4\%), versus Gemini-Simple (69.1\%) and DeepL (64.4\%), while preserving overall quality (mean DA 85.3 Gemini-RAG vs. 85.2 Gemini-Simple), outperforming DeepL (80.3). These results show that glossary-augmented prompting is a low-overhead way to improve terminology control in cultural-heritage translation if institutions maintain minimal terminology resources and lightweight evaluation procedures.

---


### 99. [EponaV2: Driving World Model with Comprehensive Future Reasoning](https://arxiv.org/abs/2605.14696)

**<font color=#1a73e8>作者：</font>** Jiawei Xu, Zhizhou Zhong, Zhijian Shu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data scaling plays a pivotal role in the pursuit of general intelligence. However, the prevailing perception-planning paradigm in autonomous driving relies heavily on expensive manual annotations to supervise trajectory planning, which severely limits its scalability. Conversely, although existing perception-free driving world models achieve impressive driving performance, their real-world reasoning ability for planning is solely built on next frame image forecasting. Due to the lack of enough supervision, these models often struggle with comprehensive scene understanding, resulting in unsatisfactory trajectory planning. In this paper, we propose EponaV2, a novel paradigm of driving world models, which achieves high-quality planning with comprehensive future reasoning. Inspired by how human drivers anticipate 3D geometry and semantics, we train our model to forecast more comprehensive future representations, which can be additionally decoded to future geometry and semantic maps. Extracting the 3D and semantic modalities enables our model to deeply understand the surrounding environment, and the future prediction task significantly enhances the real-world reasoning capabilities of EponaV2, ultimately leading to improved trajectory planning. Moreover, inspired by the training recipe of Large Language Models (LLMs), we introduce a flow matching group relative policy optimization mechanism to further improve planning accuracy. The state-of-the-art (SOTA) performances of EponaV2 among perception-free models on three NAVSIM benchmarks (+1.3PDMS, +5.5EPDMS) demonstrate the effectiveness of our methods.

---


### 100. [NeuroAtlas: Benchmarking Foundation Models for Clinical EEG and Brain-Computer Interfaces](https://arxiv.org/abs/2605.14698)

**<font color=#1a73e8>作者：</font>** Konstantinos Kontras, Trui Osselaer, Stylianos G. Mouslech 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models (FMs) promise to extract unified representations that generalize across downstream tasks. They have emerged across fields, including electroencephalography (EEG), but it is less clear how effective they are in this particular field. Published evaluations differ in datasets, in the EEG-specific preprocessing that might influence reported results, and in the reported metrics, frequently obscuring the clinical relevance in EEG. We introduce NeuroAtlas, the largest EEG benchmark to date: 42 datasets and 260k hours covering clinical EEG (epilepsy, sleep medicine, brain age estimation) and brain-computer interfaces, and include multiple datasets per task along with bespoke clinical evaluation metrics. Besides evaluating EEG-FMs with respect to supervised baselines, we present results from generic time-series FMs. We report three findings. First, EEG-specific FMs do not consistently outperform time-series FMs, which have neither EEG-focused architectures nor been pretrained on EEG. Second, standard machine learning metrics are insufficient to assess clinical utility: thus, we thoroughly evaluate more appropriate measures such as the quality of event-level decision-making, hypnogram-derived features, and the brain-age gap in the domains of epilepsy, sleep, and brain age, respectively. Third, model rankings and performance can vary substantially within domains. We conclude that pretrained models perform largely on par, with only narrow advantages for a few, and that current models do not yet deliver on the promise of an out-of-the-box unified EEG model. NeuroAtlas exposes this gap and provides the datasets and metrics for the next generation of unified EEG FMs.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-165](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
