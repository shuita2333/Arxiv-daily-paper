# 🧠 大模型相关研究 | 2026年05月05日

> 本类共 **79** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-79**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-79**

---

### 51. [Leveraging Vision-Language Models as Weak Annotators in Active Learning](https://arxiv.org/abs/2605.00480)

**<font color=#1a73e8>作者：</font>** Phuong Ngoc Nguyen, Kaito Shiku, Ryoma Bise 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Active learning aims to reduce annotation cost by selectively querying informative samples for supervision under a limited labeling budget. In this work, we investigate how vision-language models (VLMs) can be leveraged to further reduce the reliance on costly human annotation within the active learning paradigm. To this end, we find that the reliability of VLMs varies significantly with label granularity in fine-grained recognition tasks: they perform poorly on fine-grained labels but can provide accurate coarse-grained labels. Leveraging this property, we propose an active learning framework that combines fine-grained human annotations with coarse-grained VLM-generated weak labels through instance-wise label assignment. We further model the systematic noise in VLM-generated labels using a small set of trusted full labels. Experiments on CUB200 and FGVC-Aircraft show that the proposed framework consistently outperforms existing active learning methods under the same annotation budget.

---


### 52. [Hierarchical Abstract Tree for Cross-Document Retrieval-Augmented Generation](https://arxiv.org/abs/2605.00529)

**<font color=#1a73e8>作者：</font>** Ziwen Zhao, Menglin Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) enhances large language models with external knowledge, and tree-based RAG organizes documents into hierarchical indexes to support queries at multiple granularities. However, existing Tree-RAG methods designed for single-document retrieval face critical challenges in scaling to cross-document multi-hop questions: (1) poor distribution adaptability, where $k$-means clustering introduces noise due to rigid distribution assumptions; (2) structural isolation, as tree indexes lack explicit cross-document connections; and (3) coarse abstraction, which obscures fine-grained details. To address these limitations, we propose $\Psi$-RAG, a tree-RAG framework with two key components. First, a hierarchical abstract tree index built through an iterative "merging and collapse" process that adapts to data distributions without a priori assumption. Second, a multi-granular retrieval agent that intelligently interacts with the knowledge base with reorganized queries and an agent-powered hybrid retriever. $\Psi$-RAG supports diverse tasks from token-level question answering to document-level summarization. On cross-document multi-hop QA benchmarks, it outperforms RAPTOR by 25.9% and HippoRAG 2 by 7.4% in average F1 score. Code is available at this https URL.

---


### 53. [AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs](https://arxiv.org/abs/2605.00539)

**<font color=#1a73e8>作者：</font>** Wenxiang Lin, Juntao Huang, Luhan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantization is a key method for reducing the GPU memory requirement of training large language models (LLMs). Yet, current approaches are ineffective for 4-bit activations and 8-bit gradients, which would easily cause slow convergence or accuracy loss. To address this, we introduce AGoQ, incorporating two new techniques: 1) a layer-aware activation quantization algorithm that allocates appropriate bit-widths for activations of various layers based on their types and pipeline stages to achieve near 4-bit activation storage, and 2) a gradient quantization algorithm that reduces memory usage and shortens communication time by employing 8-bit gradient storage and precision-preserving 8-bit All-Reduce communication. We conduct extensive experiments using different sizes of LLMs on two GPU clusters (up to 64 GPUs), and the experimental results show that our AGoQ reduces the memory by up to 52\% and achieves up to 1.34$\times$ improvement of training speed compared to state-of-the-art training systems Megatron-LM (w/ or w/o ZeRO), COAT and DeepSpeed with 8B to 32B LLaMA models, while achieving convergence loss on pretraining and comparable accuracy on downstream tasks with LLaMA architectures.

---


### 54. [Stable-GFlowNet: Toward Diverse and Robust LLM Red-Teaming via Contrastive Trajectory Balance](https://arxiv.org/abs/2605.00553)

**<font color=#1a73e8>作者：</font>** Minchan Kwon, Sunghyun Baek, Minseo Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) Red-Teaming, which proactively identifies vulnerabilities of LLMs, is an essential process for ensuring safety. Finding effective and diverse attacks in red-teaming is important, but achieving both is challenging. Generative Flow Networks (GFNs) that perform distribution matching are a promising methods, but they are notorious for training instability and mode collapse. In particular, unstable rewards in red-teaming accelerate mode collapse. We propose Stable-GFN (S-GFN), which eliminates partition function $Z$ estimation in GFN and reduces training instability. S-GFN avoids Z-estimation through pairwise comparisons and employs a robust masking methodology against noisy rewards. Additionally, we propose a fluency stabilizer to prevent the model from getting stuck in local optima that produce gibberish. S-GFN provides more stable training while maintaining the optimal policy of GFN. We demonstrate the overwhelming attack performance and diversity of S-GFN across various settings.

---


### 55. [Jailbreaking Vision-Language Models Through the Visual Modality](https://arxiv.org/abs/2605.00583)

**<font color=#1a73e8>作者：</font>** Aharon Azulay, Jan Dubiński, Zhuoyun Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The visual modality of vision-language models (VLMs) is an underexplored attack surface for bypassing safety alignment. We introduce four jailbreak attacks exploiting the vision component: (1) encoding harmful instructions as visual symbol sequences with a decoding legend, (2) replacing harmful objects with benign substitutes (e.g., bomb -> banana) then prompting for harmful actions using the substitute term, (3) replacing harmful text in images (e.g., on book covers) with benign words while visual context preserves the original meaning, and (4) visual analogy puzzles whose solution requires inferring a prohibited concept. Evaluating across six frontier VLMs, our visual attacks bypass safety alignment and expose a cross-modality alignment gap: text-based safety training does not automatically generalize to harmful intent conveyed visually. For example, our visual cipher achieves 40.9% attack success on Claude-Haiku-4.5 versus 10.7% for an equivalent textual cipher. To further our insight into the attack mechanism, we present preliminary interpretability and mitigation results. These findings highlight that robust VLM alignment requires treating vision as a first-class target for safety post-training.

---


### 56. [Intrinsic Gradient Suppression for Label-Noise Prompt Tuning in Vision-Language Models](https://arxiv.org/abs/2605.00591)

**<font color=#1a73e8>作者：</font>** Jiayu Li, Jiaxin Qi, Sheng Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive vision-language models like CLIP exhibit remarkable zero-shot generalization. However, prompt tuning remains highly sensitive to label noise, as mislabeled samples generate disproportionately large gradients that can overwhelm pre-trained priors. We argue that because CLIP already provides a near-optimal initialization, adaptation should be inherently conservative, particularly against the extreme gradient updates common in noisy settings. To this end, we propose Double-Softmax Prompt Tuning (DSPT), a hyperparameter-free method for intrinsic gradient suppression. By applying a sequential probabilistic normalization, DSPT induces a self-adaptive saturation zone that suppresses gradients from high-error noisy samples while maintaining informative updates. We also provide both theoretical analysis and empirical evidence about how this mechanism achieves adaptive suppression. This design transforms ``gradient vanishing'', traditionally a training bottleneck, into a principled noise-filtering shield for label-noise prompt tuning. Extensive experiments confirm that this simple, drop-in design achieves state-of-the-art robustness across various noisy benchmarks, outperforming methods with complex architectures and handcrafted hyperparameters.

---


### 57. [Beyond Decodability: Reconstructing Language Model Representations with an Encoding Probe](https://arxiv.org/abs/2605.00607)

**<font color=#1a73e8>作者：</font>** Gaofei Shen, Martijn Bentum, Tom Lentz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Probing is widely used to study which features can be decoded from language model representations. However, the common decoding probe approach has two limitations that we aim to solve with our new encoding probe approach: contributions of different features to model representations cannot be directly compared, and feature correlations can affect probing results. We present an Encoding Probe that reverses this direction and reconstructs internal representations of models using interpretable features. We evaluate this method on text and speech transformer models, using feature sets spanning acoustics, phonetics, syntax, lexicon, and speaker identity. Our results suggest that speaker-related effects vary strongly across different training objectives and datasets, while syntactic and lexical features contribute independently to reconstruction. These results show that the Encoding Probe provides a complementary perspective on interpreting model representations beyond decodability.

---


### 58. [Decouple before Integration: Test-time Synthesis of SFT and RLVR Task Vectors](https://arxiv.org/abs/2605.00610)

**<font color=#1a73e8>作者：</font>** Chaohao Yuan, Chenghao Xiao, Yu Rong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> SFT and RLVR represent two fundamental yet distinct paradigms for LLM post-training, each excelling in distinct dimensions. SFT expands knowledge breadth while RLVR enhances reasoning depth. Yet integrating these complementary strengths remains a formidable challenge. Sequential training can cause catastrophic forgetting, and joint optimization often suffers from severe gradient conflicts. We analyze SFT and RLVR through the lens of task vectors and reveal three structural properties behind these failures: a 30* magnitude disparity, 45* sign interference, and heterogeneous module-wise update distributions. These findings show SFT and RLVR are difficult to integrate directly, but they also suggest that the two paradigms modify partly complementary components of the model. Motivated by these observations, we propose Decoupled Test-time Synthesis (DoTS), a post-hoc framework allows SFT and RLVR checkpoints to be trained independently and synthesizes their capabilities only at inference time via task vector arithmetic, without updating model parameters. To reduce interference, DOTS applies selective sparsification with norm-preserving rescaling. It then uses Bayesian optimization on a small set of unlabeled queries to search for combination coefficients on the Pareto frontier of consistency and perplexity. Empirically, \ours matches or exceeds the performance of training-based SFT--RLVR integration methods across multiple mathematical reasoning benchmarks, incurring only $\sim$3\% of the computational cost. When applied to stronger post-trained checkpoints, DOTS surpasses SOTA models and generalizes to out-of-domain benchmarks without re-tuning. Code is available at this https URL.

---


### 59. [SC-Taxo: Hierarchical Taxonomy Generation under Semantic Consistency Constraints using Large Language Models](https://arxiv.org/abs/2605.00620)

**<font color=#1a73e8>作者：</font>** Shiqiang Cai, Nianhong Niu, Shizhu He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific literature is expanding at an unprecedented pace, making it increasingly challenging to efficiently organize and access domain knowledge. A high-quality scientific taxonomy offers a structured and hierarchical representation of a research field, facilitating literature exploration and topic navigation, as well as enabling downstream applications such as trend analysis, idea generation, and information retrieval. However, existing taxonomy generation approaches often suffer from structural inconsistencies and semantic misalignment across hierarchical levels. Through empirical analysis, we find that these issues largely stem from inadequate modeling of hierarchical semantic consistency. To address this limitation, we propose a semantic-consistent taxonomy generation (SC-Taxo) framework that leverages large language models (LLMs) with hierarchy-aware refinement stages to ensure semantic consistency. Specifically, SC-Taxo introduces a bidirectional heading generation mechanism that jointly performs bottom-up abstraction and top-down semantic constraint, while further capturing peer-level semantic dependencies to enhance horizontal consistency. Experiments on multiple benchmark datasets demonstrate consistent improvements in hierarchy alignment and heading quality, and additional evaluation on Chinese scientific literature validates its robust cross-lingual generalization.

---


### 60. [CMTA: Leveraging Cross-Modal Temporal Artifacts for Generalizable AI-Generated Video Detection](https://arxiv.org/abs/2605.00630)

**<font color=#1a73e8>作者：</font>** Hang Wang, Chao Shen, Chenhao Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The proliferation of advanced AI video synthesis techniques poses an unprecedented challenge to digital video authenticity. Existing AI-generated video (AIGV) detection methods primarily focus on uni-modal or spatiotemporal artifacts, but they overlook the rich cues within the visual-textual cross-modal space, especially the temporal stability of semantic alignment. In this work, we identify a distinctive fingerprint in AIGVs, termed cross-modal temporal artifact (CMTA). Unlike real videos that exhibit natural temporal fluctuations in cross-modal alignment due to semantic variations, AIGVs display unnaturally stable semantic trajectories governed by given input prompts. To bridge this gap, we propose the CMTA framework, a cross-modal detection approach that captures these unique temporal artifacts through joint cross-modal embedding and multi-grained temporal modeling. Specifically, CMTA leverages BLIP to generate frame-level image captions and utilizes CLIP to extract corresponding visual-textual representations. A coarse-grained temporal modeling branch is then designed to characterize temporal fluctuations in cross-modal alignment with a GRU. In parallel, a fine-grained branch is constructed to capture intricate inter-frame variations from integrated visual-textual features with a Transformer encoder. Extensive experiments on 40 subsets across four large-scale datasets, including GenVideo, EvalCrafter, VideoPhy, and VidProM, validate that our approach sets a new state-of-the-art while exhibiting superior cross-generator generalization. Code and models of CMTA will be released at this https URL

---


### 61. [H-RAG at SemEval-2026 Task 8: Hierarchical Parent-Child Retrieval for Multi-Turn RAG Conversations](https://arxiv.org/abs/2605.00631)

**<font color=#1a73e8>作者：</font>** Passant Elchafei, Hossam Emam, Mohamed Alansary 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present H-RAG, our submission to SemEval-2026 Task 8 (MTRAGEval), addressing both Task A (Retrieval) and Task C (Generation with Retrieved Passages). Task A evaluates standalone retrieval quality, while Task C assesses end-to-end retrieval-augmented generation (RAG) in multi-turn conversational settings, requiring both accurate answer generation and faithful grounding in retrieved evidence. Our approach implements a hierarchical parent-child RAG pipeline that separates fine-grained child-level retrieval from parent-level context reconstruction during generation. Documents are segmented into overlapping sentence-based child chunks, while full documents are preserved as parent units to provide coherent context. Retrieval combines hybrid dense-sparse search, tunable weighting, and embedding-based similarity rescoring over child chunks. Retrieved evidence is aggregated at the parent level and supplied to an instruction-tuned language model for response generation. H-RAG achieves an nDCG@5 score of 0.4271 on Task A and a harmonic mean score of 0.3241 on Task C (RB_agg: 0.2488, RL_F: 0.2703, RB_llm: 0.6508), underscoring the importance of retrieval configuration and parent-level aggregation in multi-turn RAG performance.

---


### 62. [BlenderRAG: High-Fidelity 3D Object Generation via Retrieval-Augmented Code Synthesis](https://arxiv.org/abs/2605.00632)

**<font color=#1a73e8>作者：</font>** Massimo Rondelli, Francesco Pivi, Maurizio Gabbrielli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic generation of executable Blender code from natural language remains challenging, with state-of-the-art LLMs producing frequent syntactic errors and geometrically inconsistent objects. We present BlenderRAG, a retrieval-augmented generation system that operates on a curated multimodal dataset of 500 expert-validated examples (text, code, image) across 50 object categories. By retrieving semantically similar examples during generation, BlenderRAG improves compilation success rates from 40.8% to 70.0% and semantic normalized alignment from 0.41 to 0.77 (CLIP similarity) across four state-of-the-art LLMs, without requiring fine-tuning or specialized hardware, making it immediately accessible for deployment. The dataset and code will be available at this https URL.

---


### 63. [Learning Multimodal Energy-Based Model with Multimodal Variational Auto-Encoder via MCMC Revision](https://arxiv.org/abs/2605.00644)

**<font color=#1a73e8>作者：</font>** Jiali Cui, Zhiqiang Lao, Heather Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Energy-based models (EBMs) are a flexible class of deep generative models and are well-suited to capture complex dependencies in multimodal data. However, learning multimodal EBM by maximum likelihood requires Markov Chain Monte Carlo (MCMC) sampling in the joint data space, where noise-initialized Langevin dynamics often mixes poorly and fails to discover coherent inter-modal relationships. Multimodal VAEs have made progress in capturing such inter-modal dependencies by introducing a shared latent generator and a joint inference model. However, both the shared latent generator and joint inference model are parameterized as unimodal Gaussian (or Laplace), which severely limits their ability to approximate the complex structure induced by multimodal data. In this work, we study the learning problem of the multimodal EBM, shared latent generator, and joint inference model. We present a learning framework that effectively interweaves their MLE updates with corresponding MCMC refinements in both the data and latent spaces. Specifically, the generator is learned to produce coherent multimodal samples that serve as strong initial states for EBM sampling, while the inference model is learned to provide informative latent initializations for generator posterior sampling. Together, these two models serve as complementary models that enable effective EBM sampling and learning, yielding realistic and coherent multimodal EBM samples. Extensive experiments demonstrate superior performance for multimodal synthesis quality and coherence compared to various baselines. We conduct various analyses and ablation studies to validate the effectiveness and scalability of the proposed multimodal framework.

---


### 64. [AdaMeZO: Adam-style Zeroth-Order Optimizer for LLM Fine-tuning Without Maintaining the Moments](https://arxiv.org/abs/2605.00650)

**<font color=#1a73e8>作者：</font>** Zhijie Cai, Haolong Chen, Guangxu Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning LLMs is necessary for various dedicated downstream tasks, but classic backpropagation-based fine-tuning methods require substantial GPU memory. To this end, a recent work, MeZO, which relies solely on forward passes to fine-tune LLMs, significantly reduces GPU requirements at the cost of slower convergence due to its indifference to loss landscapes. Standard solutions, such as Adam, explore loss landscapes by estimating the first- and second-order moments and storing them in memory to guide the model's movement through dimensions with lower curvature and vice versa. However, directly applying Adam negates MeZO's advantage as it will triple the memory requirement. In light of this, we propose AdaMeZO, a zeroth-order optimizer that leverages Adam-style first- and second-moment estimates without maintaining them in memory. We present a theoretical analysis of AdaMeZO, corroborated by extensive experiments demonstrating AdaMeZO's performance, showing that AdaMeZO can outperform MeZO while requiring up to $70\%$ fewer forward passes. Trajectory visualizations affirm AdaMeZO's ability to adapt to diverse loss landscapes.

---


### 65. [UniVidX: A Unified Multimodal Framework for Versatile Video Generation via Diffusion Priors](https://arxiv.org/abs/2605.00658)

**<font color=#1a73e8>作者：</font>** Houyuan Chen, Hong Li, Xianghao Kong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress has shown that video diffusion models (VDMs) can be repurposed for diverse multimodal graphics tasks. However, existing methods often train separate models for each problem setting, which fixes the input-output mapping and limits the modeling of correlations across modalities. We present UniVidX, a unified multimodal framework that leverages VDM priors for versatile video generation. UniVidX formulates pixel-aligned tasks as conditional generation in a shared multimodal space, adapts to modality-specific distributions while preserving the backbone's native priors, and promotes cross-modal consistency during synthesis. It is built on three key designs. Stochastic Condition Masking (SCM) randomly partitions modalities into clean conditions and noisy targets during training, enabling omni-directional conditional generation instead of fixed mappings. Decoupled Gated LoRA (DGL) introduces per-modality LoRAs that are activated when a modality serves as the generation target, preserving the strong priors of the VDM. Cross-Modal Self-Attention (CMSA) shares keys and values across modalities while keeping modality-specific queries, facilitating information exchange and inter-modal alignment. We instantiate UniVidX in two domains: UniVid-Intrinsic, for RGB videos and intrinsic maps including albedo, irradiance, and normal; and UniVid-Alpha, for blended RGB videos and their constituent RGBA layers. Experiments show that both models achieve performance competitive with state-of-the-art methods across distinct tasks and generalize robustly to in-the-wild scenarios, even when trained on fewer than 1,000 videos. Project page: this https URL

---


### 66. [Beyond Benchmarks: MathArena as an Evaluation Platform for Mathematics with LLMs](https://arxiv.org/abs/2605.00674)

**<font color=#1a73e8>作者：</font>** Jasper Dekoninck, Nikola Jovanović, Tim Gehrunger 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are becoming increasingly capable mathematical collaborators, but static benchmarks are no longer sufficient for evaluating progress: they are often narrow in scope, quickly saturated, and rarely updated. This makes it hard to compare models reliably and track progress over time. Instead, we need evaluation platforms: continuously maintained systems that run, aggregate, and analyze evaluations across many benchmarks to give a comprehensive picture of model performance within a broad domain. In this work, we build on the original MathArena benchmark by substantially broadening its scope from final-answer olympiad problems to a continuously maintained evaluation platform for mathematical reasoning with LLMs. MathArena now covers a much wider range of tasks, including proof-based competitions, research-level arXiv problems, and formal proof generation in Lean. Additionally, we maintain a clear evaluation protocol for all models and regularly design new benchmarks as model capabilities improve to ensure that MathArena remains challenging. Notably, the strongest model, GPT-5.5, now reaches 98% on the 2026 USA Math Olympiad and 74% on research-level questions, showing that frontier models can now comfortably solve extremely challenging mathematical problems. This highlights the importance of continuously maintained evaluation platforms like MathArena to track the rapid progress of LLMs in mathematical reasoning.

---


### 67. [Evaluating the Architectural Reasoning Capabilities of LLM Provers via the Obfuscated Natural Number Game](https://arxiv.org/abs/2605.00677)

**<font color=#1a73e8>作者：</font>** Lixing Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Large Language Models have achieved notable success on formal mathematics benchmarks such as MiniF2F, it remains unclear whether these results stem from genuine logical reasoning or semantic pattern matching against pre-training data. This paper identifies Architectural Reasoning: the ability to synthesize formal proofs using exclusively local axioms and definitions within an alien math domain, as the necessary ability for future automated theorem discovery AI. We use the Obfuscated Natural Number Game, a benchmark to evaluate Architectural Reasoning. By renaming identifiers in the Natural Number Game in Lean 4, we created a zero-knowledge, closed environment. We evaluate state-of-the-art models, finding a universal latency tax where obfuscation increases inference time. The results also reveal a divergence in robustness: while general models (Claude-Sonnet-4.5, GPT-4o) suffer performance degradation, reasoning models (DeepSeek-R1, GPT-5, DeepSeek-Prover-V2) maintain the same accuracy despite the absence of semantic cues. These findings provide a quantitative metric for assessing the true capacity for mathematical reasoning.

---


### 68. [Static and Dynamic Graph Alignment Network for Temporal Video Grounding](https://arxiv.org/abs/2605.00684)

**<font color=#1a73e8>作者：</font>** Zhanjie Hu, Bolin Zhang, Jianhua Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal Video Grounding (TVG) aims to localize temporal moments in an untrimmed video that semantically correspond to given natural language queries. Recently, Graph Convolutional Networks (GCN) have been widely adopted in TVG to model temporal relations among video clips and enhance contextual reasoning by constructing clip-level graphs. Despite their effectiveness, existing GCN-based TVG methods encounter three critical bottlenecks: 1) Most methods construct graph nodes using either static or dynamic features alone, resulting in incomplete visual representation and overlooking complementary semantics, 2) Most methods construct temporal graphs in a query-agnostic manner, leading to inefficient feature interaction within the temporal graph representation, and 3) Most methods often suffer from a single-granularity semantic matching, while direct training on complex temporal localization task may lead to slow convergence and suboptimal precision. To address these challenges, we propose Static and Dynamic Graph Alignment Network (SDGAN). First, SDGAN jointly exploits static and dynamic visual features to construct two complementary temporal graphs and performs Position-wise Nodes Alignment, enabling more expressive and robust visual representation. Second, SDGAN introduces Query-Clip Contrastive Learning and Adaptive Graph Modeling to explicitly align visual clips with their corresponding textual queries, yielding query-aware visual representations. Third, SDGAN incorporates multi-granularity temporal proposals within Progressive Easy-to-Hard Training Strategy, effectively bridging coarse-grained semantic localization and fine-grained temporal boundary refinement. Extensive experiments on three benchmark datasets demonstrate that SDGAN achieves superior performance across complex TVG scenarios. Codes and datasets are available at this https URL.

---


### 69. [ML-Bench&Guard: Policy-Grounded Multilingual Safety Benchmark and Guardrail for Large Language Models](https://arxiv.org/abs/2605.00689)

**<font color=#1a73e8>作者：</font>** Yunhan Zhao, Zhaorun Chen, Xingjun Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly deployed in cross-linguistic contexts, ensuring safety in diverse regulatory and cultural environments has become a critical challenge. However, existing multilingual benchmarks largely rely on general risk taxonomies and machine translation, which confines guardrail models to these predefined categories and hinders their ability to align with region-specific regulations and cultural nuances. To bridge these gaps, we introduce ML-Bench, a policy-grounded multilingual safety benchmark covering 14 languages. ML-Bench is constructed directly from regional regulations, where risk categories and fine-grained rules derived from jurisdiction-specific legal texts are directly used to guide the generation of multilingual safety data, enabling culturally and legally aligned evaluation across languages. Building on ML-Bench, we develop ML-Guard, a Diffusion Large Language Model (dLLM)-based guardrail model that supports multilingual safety judgment and policy-conditioned compliance assessment. ML-Guard has two variants, one 1.5B lightweight model for fast `safe/unsafe' checking and a more capable 7B model for customized compliance checking with detailed explanations. We conduct extensive experiments against 11 strong guardrail baselines across 6 existing multilingual safety benchmarks and our ML-Bench, and show that ML-Guard consistently outperforms prior methods. We hope that ML-Bench and ML-Guard can help advance the development of regulation-aware and culturally aligned multilingual guardrail systems.

---


### 70. [FinSafetyBench: Evaluating LLM Safety in Real-World Financial Scenarios](https://arxiv.org/abs/2605.00706)

**<font color=#1a73e8>作者：</font>** Yutao Hou, Yihan Jiang, Yuhan Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly applied in financial scenarios. However, they may produce harmful outputs, including facilitating illegal activities or unethical behavior, posing serious compliance risks. To systematically evaluate LLM safety in finance, we propose FinSafetyBench, a bilingual (English-Chinese) red-teaming benchmark designed to test an LLM's refusal of requests that violate financial compliance. Grounded in real-world financial crime cases and ethics standards, the benchmark comprises 14 subcategories spanning financial crimes and ethical violations. Through extensive experiments on general-purpose and finance-specialized LLMs under three representative attack settings, we identify critical vulnerabilities that allow adversarial prompts to bypass compliance safeguards. Further analysis reveals stronger susceptibility in Chinese contexts and highlights the limitations of prompt-level defenses against sophisticated or implicit manipulation strategies.

---


### 71. [To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling](https://arxiv.org/abs/2605.00737)

**<font color=#1a73e8>作者：</font>** Qinyuan Wu, Soumi Das, Mahsa Amani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI architectures augment LLMs with external tools, unlocking strong capabilities. However, tool use is not always beneficial; some calls may be redundant or even harmful. Effective tool use, therefore, hinges on a core LLM decision: whether to call or not call a tool, when performing a task. This decision is particularly challenging for web search tools, where the benefits of external information depend on the model's internal knowledge and its ability to integrate potentially noisy tool responses. We introduce a principled framework inspired by decision-making theory to evaluate web search tool-use decisions along three key factors: necessity, utility, and affordability. Our analysis combines two complementary lenses: a normative perspective that infers true need and utility from an optimal allocation of tool calls, and a descriptive perspective that infers the model's self-perceived need and utility from their observed behaviors. We find that models' perceived need and utility of tool calls are often misaligned with their true need and utility. Building on this framework, we train lightweight estimators of need and utility based on models' hidden states. Our estimators enable simple controllers that can improve decision quality and lead to stronger task performance than the self-perceived set up across three tasks and six models.

---


### 72. [Position: agentic AI orchestration should be Bayes-consistent](https://arxiv.org/abs/2605.00742)

**<font color=#1a73e8>作者：</font>** Theodore Papamarkou, Pierre Alquier, Matthias Bauer 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs excel at predictive tasks and complex reasoning tasks, but many high-value deployments rely on decisions under uncertainty, for example, which tool to call, which expert to consult, or how many resources to invest. While the usefulness and feasibility of Bayesian approaches remain unclear for LLM inference, this position paper argues that the control layer of an agentic AI system (that orchestrates LLMs and tools) is a clear case where Bayesian principles should shine. Bayesian decision theory provides a framework for agentic systems that can help to maintain beliefs over task-relevant latent quantities, to update these beliefs from observed agentic and human-AI interactions, and to choose actions. Making LLMs themselves explicitly Bayesian belief-updating engines remains computationally intensive and conceptually nontrivial as a general modeling target. In contrast, this paper argues that coherent decision-making requires Bayesian principles at the orchestration level of the agentic system, not necessarily the LLM agent parameters. This paper articulates practical properties for Bayesian control that fit modern agentic AI systems and human-AI collaboration, and provides concrete examples and design patterns to illustrate how calibrated beliefs and utility-aware policies can improve agentic AI orchestration.

---


### 73. [Make Your LVLM KV Cache More Lightweight](https://arxiv.org/abs/2605.00789)

**<font color=#1a73e8>作者：</font>** Xihao Chen, Yangyang Guo, Roger Zimmermann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Key-Value (KV) cache has become a de facto component of modern Large Vision-Language Models (LVLMs) for inference. While it enhances decoding efficiency in Large Language Models (LLMs), its direct adoption in LVLMs introduces substantial GPU memory overhead due to the large number of vision tokens processed during the prefill stage. To tackle this problem, we propose LightKV, a novel approach that reduces KV cache size by exploiting the redundancy among vision-token embeddings. Guided by text prompts, LightKV employs cross-modality message passing to aggregate informative messages across vision tokens and progressively compress them during prefill. This prompt-aware guidance distinguishes our method from prior vision-only compression strategies. We evaluate LightKV on eight open-source LVLMs across eight public benchmark datasets, e.g., MME and SeedBench. Experimental results demonstrate that with only 55% of the original vision tokens, LightKV (a) halves the vision-token KV cache size, (b) reduces computation by up to 40%, and (c) preserves general-purpose performance while significantly outperforming existing baselines.

---


### 74. [RunAgent: Interpreting Natural-Language Plans with Constraint-Guided Execution](https://arxiv.org/abs/2605.00798)

**<font color=#1a73e8>作者：</font>** Arunabh Srivastava, Mohammad A., Khojastepour 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Humans solve problems by executing targeted plans, yet large language models (LLMs) remain unreliable for structured workflow execution. We propose RunAgent, a multi-agent plan execution platform that interprets natural-language plans while enforcing stepwise execution through constraints and rubrics. RunAgent bridges the expressiveness of natural language with the determinism of programming via an agentic language with explicit control constructs (e.g., \texttt{IF}, \texttt{GOTO}, \texttt{FORALL}). Beyond verifying syntactic and semantic verification of the step output, which is performed based on the specific instruction of each step, RunAgent autonomously derives and validates constraints based on the description of the task and its instance at each step. RunAgent also dynamically selects among LLM-based reasoning, tool usage, and code generation and execution (e.g., in Python), and incorporates error correction mechanisms to ensure correctness. Finally, RunAgent filters the context history by retaining only relevant information during the execution of each step. Evaluations on Natural-plan and SciBench Datasets demonstrate that RunAgent outperforms baseline LLMs and state-of-the-art PlanGEN methods.

---


### 75. [GMGaze: MoE-Based Context-Aware Gaze Estimation with CLIP and Multiscale Transformer](https://arxiv.org/abs/2605.00799)

**<font color=#1a73e8>作者：</font>** Xinyuan Zhao, Yihang Wu, Ahmad Chaddad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaze estimation methods commonly use facial appearances to predict the direction of a person gaze. However, previous studies show three major challenges with convolutional neural network (CNN)-based, transformer-based, and contrastive language-image pre-training (CLIP)-based methods, including late fusion of image features, lack of factor-aware conditioning, and impractical capacity scaling. To address these challenges, we propose Globally-conditioned Multi-scale Gaze estimation (GMGaze), which leverages a multi-scale transformer architecture. Specifically, the model first introduces semantic prototype conditioning, which modulates the CLIP global image embedding using four learned prototype banks (i.e., illumination, background, head pose and appearance) to generate two complementary context-biased global tokens. These tokens, along with the CLIP patch and CNN tokens, are fused at the first layer. This early unified fusion prevents information loss common in late-stage merging. Finally, each token passes through sparse Mixture-of-Experts modules, providing conditional computational capacity without uniformly increasing dense parameters. For cross-domain adaptation, we incorporate an adversarial domain adaptation technique with a feature separation loss that encourages the two global tokens to remain de-correlated. Experiments using four public benchmarks (MPIIFaceGaze, EYEDIAP, Gaze360, and ETH-XGaze) show that GMGaze achieves mean angular errors of 2.49$^\circ$, 3.22$^\circ$, 10.16$^\circ$, and 1.44$^\circ$, respectively, outperforming previous baselines in all within-domain settings. In cross-domain evaluations, it provides state-of-the-art (SOTA) results on two standard transfer routes.

---


### 76. [Generating Statistical Charts with Validation-Driven LLM Workflows](https://arxiv.org/abs/2605.00800)

**<font color=#1a73e8>作者：</font>** Pavlin G. Poličar, Andraž Pevcin, Blaž Zupan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating diverse, readable statistical charts from tabular data remains challenging for LLMs, as many failures become apparent after rendering and are not detectable from data or code alone. Existing chart datasets also rarely provide fully aligned artifacts, such as executable code, dataset context, and question-answer pairs. We present a structured LLM-based workflow that decomposes chart generation into dataset screening, plot proposal, code synthesis, rendering, validation-driven refinement, description generation, and question-answer generation. By incorporating rendered-output validation, the workflow addresses visualization-specific failure modes such as readability and semantic mismatch. It treats chart generation as an inspectable process rather than a one-shot prompt-to-code task, retaining each chart with its code, dataset context, description, and question-answer pairs. Applied to UCI datasets, the workflow produces 1,500 charts from 74 datasets, spanning 24 chart families and paired with 30,003 question-answer pairs. We evaluate 16 multimodal LLMs (MLLMs) on these chart-question pairs. The results show that chart-syntax questions are nearly saturated, while value extraction, comparison, and reasoning remain more challenging, illustrating the workflow's utility for diagnostic studies of chart-grounded multimodal reasoning.

---


### 77. [Let ViT Speak: Generative Language-Image Pre-training](https://arxiv.org/abs/2605.00809)

**<font color=#1a73e8>作者：</font>** Yan Fang, Mengcheng Lan, Zilong Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we present \textbf{Gen}erative \textbf{L}anguage-\textbf{I}mage \textbf{P}re-training (GenLIP), a minimalist generative pretraining framework for Vision Transformers (ViTs) designed for multimodal large language models (MLLMs). To better align vision encoders with the autoregressive nature of LLMs, GenLIP trains a ViT to predict language tokens directly from visual tokens using a standard language modeling objective, without contrastive batch construction or an additional text decoder. This design offers three key advantages: (1) \textbf{Simplicity}: a single transformer jointly models visual and textual tokens; (2) \textbf{Scalability}: it scales effectively with both data and model size; and (3) \textbf{Performance}: it achieves competitive or superior results across diverse multimodal benchmarks. Trained on 8B samples from Recap-DataComp-1B, GenLIP matches or surpasses strong baselines despite using substantially less pretraining data. After continued pretraining on multi-resolution images at native aspect ratios, GenLIP further improves on detail-sensitive tasks such as OCR and chart understanding, making it a strong foundation for vision encoders in MLLMs.

---


### 78. [Persistent Visual Memory: Sustaining Perception for Deep Generation in LVLMs](https://arxiv.org/abs/2605.00814)

**<font color=#1a73e8>作者：</font>** Siyuan Huang, Xiaoye Qu, Yafu Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While autoregressive Large Vision-Language Models (LVLMs) demonstrate remarkable proficiency in multimodal tasks, they face a "Visual Signal Dilution" phenomenon, where the accumulation of textual history expands the attention partition function, causing visual attention to decay inversely with generated sequence length. To counteract this, we propose Persistent Visual Memory (PVM), a lightweight learnable module designed to ensure sustained, on-demand visual perception. Integrated as a parallel branch alongside the Feed-Forward Network (FFN) in LVLMs, PVM establishes a distance-agnostic retrieval pathway that directly provides visual embeddings for precise visual perception, thereby structurally mitigating the signal suppression inherent to deep generation. Extensive experiments on Qwen3-VL models demonstrate that PVM brings notable improvements with negligible parameter overhead, delivering consistent average accuracy gains across both 4B and 8B scales, particularly in complex reasoning tasks that demand persistent visual perception. Furthermore, in-depth analysis reveals that PVM can resist length-induced signal decay and accelerate internal prediction convergence.

---


### 79. [When LLMs Stop Following Steps: A Diagnostic Study of Procedural Execution in Language Models](https://arxiv.org/abs/2605.00817)

**<font color=#1a73e8>作者：</font>** Sailesh Panda, Pritam Kadasi, Abhishek Upperwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often achieve strong performance on reasoning benchmarks, but final-answer accuracy alone does not show whether they faithfully execute the procedure specified in a prompt. We study this question through a controlled diagnostic benchmark for procedural execution, where models are given a step-wise arithmetic algorithm and two numeric inputs, and must return the final computed value. The benchmark uses simple arithmetic operations but increases complexity through algorithm length and look-back dependencies over intermediate variables. Across 14 models and 55 datasets, average first-answer accuracy drops from 61% on 5-step procedures to 20% on 95-step procedures. Generation-level analysis shows that failures often involve missing answers, premature answers, self-correction after an initial error, under-executed traces, and hallucinated extra steps. These findings suggest that apparent reasoning ability can mask substantial weaknesses in faithful instruction execution.

---


> [!TIP]
> 当前位于：**51-79**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-79**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
