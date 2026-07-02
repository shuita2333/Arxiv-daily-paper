# 🧠 大模型相关研究 | 2026年07月03日

> 本类共 **110** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-110](./part-03.md)

---

### 51. [Measuring Dead Directions: Decomposing and Classifying Singular Structure off Canonical Alignment](https://arxiv.org/abs/2607.00603)

**<font color=#1a73e8>作者：</font>** Tejas Pradeep Shirodkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We give a descent-free, alignment-free measurement of singular structure on trained networks. At a single frozen checkpoint the read recovers the order $k$ of each dead direction from the directional-Fisher rate, the master invariant from which the per-direction learning coefficient $1/(2k)$ follows exactly, in whatever basis the optimizer left. The same read classifies each direction, separating a genuine singularity, whose order the architecture fixes, from a flat gauge symmetry; the directional-Fisher magnitude settles the cases the order cannot. A pluggable detector supplies the directions for transformer, convolutional, and normalisation layers. The read recovers the architecture-predicted order across constructed cells and trained networks, including a fine-tuned vision transformer whose dead structure is the LayerNorm-kernel gauge and a from-scratch one whose compressed MLP forms a node-death at its activation order. Where the singular structure enumerates, the per-direction orders assemble, through the typed intersection of the loci, into the global coefficient $(\lambda, m)$ matching the closed form. The method removes the canonical-alignment and descent preconditions of the underlying rate result, turning order-recovery into a deterministic, architecture-general reading. We then map its reach into the Watanabe triple: the order determines the universal singular fluctuation $\nu(k)$, though a trained network's realized $\nu$ falls below it as the live structure absorbs the dead direction's data fluctuation, and the multiplicity recovers from the dominant structure under a single-locus assumption.

---


### 52. [Auditing Forgetting in Limited Memory Language Models](https://arxiv.org/abs/2607.00605)

**<font color=#1a73e8>作者：</font>** Arya Raeesi, Hanna Roed  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Limited Memory Language Models (LMLMs) externalize factual knowledge to a database to enable deletion-based unlearning without retraining. Existing evaluations measure post-deletion correctness in aggregate and cannot tell whether a deleted fact persists through residual parametric memory, alternative retrieval paths, or near-neighbor retrieval artifacts. We propose a causal auditing framework that holds the model fixed and varies the database state at inference time across three interventions: FULL, DEL-ON, and DEL-OFF. The framework decomposes post-deletion behavior into parametric leakage L(f), retrieval-mediated correctness R(f), and a retrieval artifact rate grounded in the inference-time retrieval trace. We apply it to 12,228 alias-closure deletions across thirteen databases, including four adversarial topologies (Base, Alias, Noise, Collision) we construct in three domains, and six prompt formulations. Parametric leakage is near zero in every variant and every prompt style: the model rarely returns the deleted answer in the absence of retrieval. The residual that does survive lives in the retrieval graph: retrieval-mediated correctness and the retrieval artifact rate match within rounding everywhere, so post-deletion correctness is, in our audit, predominantly reconstituted from near-neighbor retrieval. This residual ranges from 0.7% on the released LMLM database to 13.6% on the most adversarial variant, and prompt formulation does not independently control how much of a deleted fact survives. These results suggest that, for this class of LMLM and deletion procedure, the unlearning boundary is drawn primarily by the database administrator rather than by the model.

---


### 53. [Retrieved Images as Visual Thought: Training-Free Multimodal In-Context Learning for the Open-vs-Closed Gap](https://arxiv.org/abs/2607.00606)

**<font color=#1a73e8>作者：</font>** Bingchen Huang, Zhiling Wang, Yifu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work on Thinking with Images makes vision a dynamic part of reasoning, but does so through generation: the model invokes external tools, synthesizes code, or imagines new imagery, each at the cost of a tool protocol, brittle code, or an expensive training pipeline. A fourth route makes vision dynamic without generating anything, by retrieving labeled exemplar images and reasoning over them, yet it remains underexplored despite being train-free. We present ReVisIT, a train-free framework that realizes this retrieval-based route by treating each retrieved image-label pair as a unit of visual thought. ReVisIT combines structured class definitions, per-query multimodal retrieval of exemplars, and alternating user/assistant injection of those exemplars before joint multi-attribute decoding, and degrades gracefully to whichever components a task admits. On VL-ICL Bench Fast Open MiniImageNet, Qwen3-VL-30B-A3B with ReVisIT reaches 98.5% at 4-shot, statistically indistinguishable from the 72B LLaVA-OneVision SOTA (98.7%) on this near-saturated task at about 1/2.4 the parameters, while the same backbone without the scaffold sits at chance. The turns layer alone adds 26.1 points to GPT-4.1 on free-form concept induction (Bongard-OpenWorld), and the full stack yields a 4-6 point macro gain across three backbones on MAAC-Bench, a new license-clean 27-class, 5-attribute benchmark, significant by paired bootstrap on the curator-derived attributes. Component analysis shows that retrieval-plus-turns is the universal lever while structured definitions are need-adaptive, and that 83% of the retrieval gain comes from retrieval quality rather than from the presence of exemplars. MAAC-Bench is released with a rubric-grounded LLM verification protocol that replaces author spot-check on subjective attributes.

---


### 54. [AGI Maze as a Benchmark Framework for World-Modeling Agents](https://arxiv.org/abs/2607.00627)

**<font color=#1a73e8>作者：</font>** Alexey Potapov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are powerful pattern-completion systems, but their default operating mode - predicting the next token from a static context - does not reliably produce persistent, manipulable representations of an external world. Many tasks that look like "reasoning" in text become substantially harder once the environment is partially observable, stateful, and requires memory and structured hypotheses about hidden state. AGI Maze is a lightweight framework for building such environments without requiring high-dimensional sensory inputs. It provides a family of grid-based maze tasks with a clean API and multiple difficulty regimes. The goal is to create benchmarks where agents must learn and use world state representations, not just infer a local rule over readily provided observations. We provide an initial evaluation of several vanilla LLMs on simple mazes showing that they fail to represent mazes internally at LLM inference time. We also introduce a baseline agent, which is allowed to use its message history as a working memory to construct descriptions of observations at agentic runtime. Although this can improve performance, it is still insufficient for an LLM agent to reliably solve even small mazes within a step budget that is more than enough for humans.

---


### 55. [Linguistic Relative Policy Optimization for Video Anomaly Reasoning](https://arxiv.org/abs/2607.00654)

**<font color=#1a73e8>作者：</font>** Jiaxu Leng, Jiankang Zheng, Mengjingcheng Mo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly detection (VAD) with multimodal large language models has shown strong potential, yet most existing methods still depend on large-scale annotations or expert-designed priors, limiting their ability to acquire anomaly knowledge with as little human intervention as possible. To address this, we propose Linguistic Relative Policy Optimization (LRPO), which distills group-relative semantic advantages from multiple reasoning trajectories into a linguistically expressed anomaly experience prior, and adapts the model by injecting this prior into the context to steer its output distribution without any parameter updates. LRPO builds two complementary experience representations: general experience captures transferable anomaly preferences across scenarios, while scenario experience models context-dependent anomaly rules for targeted refinement. To further improve the learned experience, we introduce an anomaly alignment reward that guides trajectory optimization to match human risk preferences and reinforce temporally grounded reasoning. Extensive experiments on XD-Violence, UCF-Crime, and UBnormal demonstrate that LRPO significantly outperforms existing state-of-the-art methods under tuning-free settings.

---


### 56. [YOMI-Bench: A Benchmark for Evaluating Kanji Reading and Phonological Understanding of LLMs for Japanese](https://arxiv.org/abs/2607.00664)

**<font color=#1a73e8>作者：</font>** Ryota Mibayashi, Hiroya Takamura, Hitomi Yanaka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose YOMI-Bench, a benchmark for evaluating kanji reading and phonological understanding of large language models (LLMs) for Japanese. In Japanese, a single kanji character often has multiple possible readings, making it difficult to infer the correct reading from surface-level text alone. Due to these linguistic characteristics, it is empirically known that LLMs exhibit low performance in kanji reading for Japanese. The proposed YOMI-Bench consists of four tasks specifically designed to evaluate kanji reading performance in Japanese. In our evaluation using YOMI-Bench, we assessed one multilingual open LLM, four Japanese-specific open LLMs, and five commercial LLMs. As a result, we found that even Japanese-specific models show low performance, and that commercial models also perform poorly on generation tasks that require consideration of kanji readings.

---


### 57. [AdaBoosting Text Prompts for Vision-Language Models](https://arxiv.org/abs/2607.00684)

**<font color=#1a73e8>作者：</font>** Seokhee Jin, Changhwan Sung, Sunung Mun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The classification accuracy of pretrained Vision-Language Models (VLMs) relies on the quality of the text prompts. Handcrafted templates and Large Language Model (LLM)-generated descriptions not only make predictions more interpretable, but also enable reuse of the same prompts across heterogeneous VLMs. Recent works construct task-adapted text prompts with a small number of labeled images. However, existing few-shot text prompting methods do not explicitly focus on misclassified examples during prompt construction, leading to only marginal improvements even as more shots become available. To fully exploit few-shot supervision, we propose Text Prompt Boosting (TPB), an AdaBoost-inspired framework that treats each text-prompt-based classifier as a weak learner and sequentially aggregates them into a strong ensemble by explicitly targeting hard, misclassified examples. Extensive experiments show that TPB preserves task-intrinsic, model-agnostic cues in text space, enabling robust cross-model transfer. Across eleven classification benchmarks, TPB improves accuracy on the source model and preserves shot-driven gains when transferred to larger, more capable VLMs, where existing methods struggle to sustain such improvements.

---


### 58. [M2Note: Continual Evolution of Vision Language Models via Mistake Notebook Learning](https://arxiv.org/abs/2607.00685)

**<font color=#1a73e8>作者：</font>** Haiwen Li, Jing Tang, Rui Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) have demonstrated remarkable capabilities in multimodal reasoning tasks, yet they still suffer from recurring failures, such as skipping key visual checks, misapplying domain rules, and hallucinating unsupported concepts. Most existing solutions rely on supervised fine-tuning (SFT) and reinforcement learning (RL), which are expensive to iterate and can be brittle under distribution shift. To this end, we propose Multimodal Mistake Notebook Learning (M2Note), a training-free continual evolution framework that externalizes learning into an editable memory. M2Note transforms failed trajectories into compact subject-guidance notes: the subject summarizes the underlying domain and concept, while the guidance provides actionable verification steps that can be reused in future inference. At test time, M2Note retrieves relevant notes via multimodal retrieval-augmented generation (RAG) and appends them to the model context, steering reasoning away from previously observed pitfalls. To stabilize continual evolution, we adopt batch-level post-verification with rollback, which commits notebook edits only if they improve performance on the same batch, reducing noisy updates and preventing regressions. M2Note supports both self-evolving, where the same VLM acts as solver and supervisor, and cross-model evolving, where a stronger supervisor guides a weaker solver, enabling capability transfer without weight updates. Experiments on six multimodal reasoning benchmarks show consistent improvements across domains and backbones, while achieving strong cost and sample efficiency and remaining complementary to Chain-of-Thought (CoT) prompting.

---


### 59. [Self-GC: Self-Governing Context for Long-Horizon LLM Agents](https://arxiv.org/abs/2607.00692)

**<font color=#1a73e8>作者：</font>** Xubin Hao, Hongjin Meng, Xin Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents accumulate tool results, files, plans, and user constraints that are too structured to be treated as a disposable text suffix. Current systems mostly rely on in-run heuristics such as chronological pruning and tool-output masking, or on final self-summary near a context limit. Heuristics are cheap but blind to future dependencies; summaries preserve narrative state but often hide exact evidence, locators, and editable artifacts. We present Self-GC, where GC denotes self-governing context while deliberately echoing garbage collection: the system does not merely reclaim unused tokens, but governs the lifecycle of agent context objects. Self-GC turns user turns, tool spans, and skill state into indexed objects; asks a side-channel planner to propose fold, mask, and prune actions; and lets the harness enforce recoverable sidecars, safe commit boundaries, and cache-aware commit. On a 33-session Hard Set, Self-GC prunes 43.95% of prefix tokens while leaving 84.85% of future continuations unaffected, compared with no-impact rates of 54.55% to 69.70% for heuristic baselines. On a 332-session production-derived suite, three planner backbones reach no-impact rates of 91.27% to 94.58%, while baselines remain at 77.71% to 87.46%. In production, an online account-level split reduces daytime average input tokens by 10% to 15%, with peak reductions near 20%. These results point to context management as runtime lifecycle control over indexed, recoverable objects rather than post hoc text cleanup.

---


### 60. [Self-conditioned Flow Map Language Models via Fixed-point Flows](https://arxiv.org/abs/2607.00714)

**<font color=#1a73e8>作者：</font>** Jaehoon Yoo, Wonjung Kim, Floor Eijkelboom 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-conditioning is a core technique that enhances continuous flow-based language models, where the model learns to denoise generated text by conditioning on its own denoising estimate. While empirically successful, its performance improvements are poorly understood. Moreover, there is growing interest in the use of few-step generators based on flow maps, for which how to leverage self-conditioning is unclear. Here, we show that flow language models with self-conditioning solve a fixed-point iteration that bootstraps the performance of the learned denoiser. We use this viewpoint to formulate fixed-point flows, a two-dimensional class of self-conditioned flows, where the first dimension represents the flow process and the second represents the fixed-point iteration. We show that fixed-point flows define valid flow maps, and show that they can be distilled from self-conditioned flow models by compressing both fixed-point iterations and the flow process, the former with fixed-point distillation and the latter with flow map distillation. Our resulting flow map language model, FMLM$^\star$, outperforms state-of-the-art self-conditioned models and few-step models in one- and few-step generation on OpenWebText. Code is available at this https URL.

---


### 61. [What Survives Into Context: A Diagnostic for Budget-Constrained Multi-Hop RAG and When Submodular Evidence Packing Improves It](https://arxiv.org/abs/2607.00725)

**<font color=#1a73e8>作者：</font>** Ananto Nayan Bala  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) under a fixed reader-context budget forces a selection problem: of the evidence retrieved, only a fraction can be shown to the reader. We argue that document recall -- the standard retrieval metric -- is the wrong quantity to optimize in this regime, and we make two contributions. First, as a general contribution, we introduce answer-in-context, a diagnostic that measures whether a gold answer survives as a contiguous span in the packed reader context (not the retrieved set). It predicts answer F1 better than recall (r=0.39-0.55 vs. about 0.31), separates answer quality roughly five-fold (0.60 vs. 0.12 on HotpotQA), and carries information beyond retrieval: it adds Delta R squared=0.17 over recall and shows a 4.6x EM gap even among questions where all gold was retrieved. We also confirm it interventionally: on 2WikiMultiHopQA a packing change that raises coverage but not answer-in-context yields no accuracy gain. Second, as a conditional contribution, we cast reader-context construction as budgeted monotone submodular maximization and build a packer that jointly optimizes relevance, query coverage, representativeness, and diversity. On HotpotQA with a 160-token budget and a 3B reader it beats a strong focused heuristic, MMR, and naive packing -- by up to +5.1 F1 at equal-or-lower token cost, across three seeds. Crucially, we map the scope of this win honestly: it requires the conjunction of (i) multi-hop complementary structure, (ii) retrieval that surfaces the evidence, (iii) a binding but not extreme budget, and (iv) a reader weak enough that evidence density, not reading capacity, is the bottleneck. A quantization-controlled reader-scale ladder (3B to 7B to 14B) shows the edge over the heuristic is absorbed by 7B and significantly reverses by 14B, while the diagnostic explains every boundary with a single variable.

---


### 62. [LLM-Guided ODE Discovery and Parameter Inference from Small-Cohort Aggregate Data](https://arxiv.org/abs/2607.00733)

**<font color=#1a73e8>作者：</font>** Hanning Yang, Meropi Karakioulaki, Lennart Purucker 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic modeling via ordinary differential equations (ODEs) provides interpretable descriptions of complex dynamics and enables inference of underlying mechanisms, which is particularly valuable in clinical settings. However, in rare diseases, both the structure and parameters of the model are typically unknown, while individual-level data is scarce, noisy, heterogeneous, and subject to privacy constraints. In such settings, population-level summary statistics provide a practical privacy-preserving data representation, while capturing heterogeneity further requires modeling parameters as distributions rather than fixed values. Yet no existing method jointly discovers ODE structure and refines parameter distributions solely from summary statistics. We present AgentODE, an end-to-end framework that addresses this gap. An LLM proposes candidate ODE structures, while a tool-augmented inference agent iteratively refines parameter distributions through a diagnosis--update loop, operating on population-level summary statistics alone. We evaluate AgentODE on three benchmark problems across different fields and two clinical datasets, including the rare disease recessive dystrophic epidermolysis bullosa (RDEB), with only 231 observations across 46 patients. AgentODE recovers functionally consistent ODE structures across all settings, and experiments on RDEB demonstrates that in sparse and noisy data settings reasoning from summary statistics promotes mechanistically principled structure discovery, whereas baselines with individual-level data access recover implausible structures despite better predictive performance. AgentODE opens new possibilities for mechanistic modeling of rare diseases directly from population-level summary statistics, where data scarcity and privacy constraints have traditionally limited such analyses.

---


### 63. [Foundation Model-driven Key Anatomy Frame Selection for Blind-sweep Ultrasound Fetal Birth Weight Estimation](https://arxiv.org/abs/2607.00745)

**<font color=#1a73e8>作者：</font>** Le Ou, Xiliang Zhu, Huanwen Liang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate fetal birth weight (FBW) estimation shortly before delivery is clinically valuable yet challenging due to its reliance on operator expertise, particularly in low-resource settings. To reduce this reliance, we study near-term birth-weight regression from blind-sweep ultrasound (US) videos acquired within 48 hours prior to delivery, with post-delivery weighing as ground truth. Accordingly, we propose a foundation model-driven key anatomy frame selection framework that enables accurate FBW regression despite the absence of plane constraints in blind sweeps. Our highlights are as follows: (1) We believe this is the first work to estimate FBW using blind-sweep US videos, enabling operator-independent assessment. (2) An Anatomy-Guided Frame Selection module equipped with a vision-language foundation model is proposed for keyframe collection in unconstrained sweeps. (3) A Redundancy-Aware Feature Compression module is designed to compress frame features while preserving task-relevant information, alleviating temporal redundancy. Extensively validated on prospectively collected data from 839 patients, our method achieves an MAE of 161.3 g, with 90.23% and 100% of cases falling within 10% and 15% absolute percentage error, outperforming typical Hadlock estimation and strong competitors. Codes are available at this https URL.

---


### 64. [Active Learning for Cascaded Object Detection: Balancing Coverage and Uncertainty in Table Extraction Pipelines](https://arxiv.org/abs/2607.00747)

**<font color=#1a73e8>作者：</font>** Eliott Thomas, Mickael Coustaty, Aurelie Joseph 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Table extraction from business documents relies on a cascaded pipeline where Table Detection (TD) first localizes tables and Table Structure Recognition (TSR) then recovers their internal layout. Building task-specific training sets for this pipeline is costly, particularly for TSR which requires fine-grained structural annotations. Active learning (AL) can reduce this annotation burden, yet most AL strategies are designed for single-model tasks and do not account for inter-stage dependencies in cascaded architectures. In this work, we present the first adaptation of Uncertainty Herding (UHerding), a hybrid coverage-uncertainty sampling method originally proposed for image classification, to cascaded object detection pipelines. We propose two pipeline-aware extensions that exploit the TD-to-TSR dependency: RankFusion adds dual-manifold coverage over both detection and structure representation spaces, while CAPA further incorporates stage-dependent gating and per-task uncertainty calibration. Extensive experiments across two public (PubTables-1M and FinTabNet) and two private table extraction datasets, with various annotation budgets (from 71 to 500 documents) show that UHerding generalizes well to table extraction, outperforming each baseline. Among pipeline-aware variants, RankFusion achieves higher expected gains but at the cost of greater variance, while CAPA emerges as the most consistent strategy, outperforming standard UHerding on three out of four datasets.

---


### 65. [MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression](https://arxiv.org/abs/2607.00760)

**<font color=#1a73e8>作者：</font>** Sheng Qiang, Ruiwei Chen, Yinpeng Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context LLM services now sustain prompts with hundreds of thousands to millions of tokens, making the key-value (KV) cache a first-order serving cost. Because the cache grows linearly with context length, it can exhaust GPU memory, force smaller batches, and reduce serving throughput. Prior KV cache compression techniques typically target only the sequence dimension or only the channel dimension, which leaves limited headroom as context windows scale. Compressing both dimensions promises higher memory reduction, but applying the two forms of compression directly leads to significant accuracy loss.
This paper introduces MosaicKV, a dynamic two-D (dimensional) KV cache compression system for extremely long-context serving. MosaicKV uses dynamic two-D compression to address the accuracy challenge, exploiting the non-uniform importance distribution of elements within the KV cache. Instead of applying one compression pattern globally, MosaicKV identifies important elements for each KV vector and selects compression strategies at the granularity of KV cache segments. To address the performance challenge, where fine-grained sparsity and compression management overhead can offset the gains from compression, MosaicKV introduces compressed KV cache management. This mechanism uses underutilized GPU and CPU resources to maintain compressed KV caches and accelerate attention computation.
Evaluation on an H800 GPU with multiple LLMs shows that MosaicKV delivers up to 16x attention speedup, 4.8x lower decode latency, and 7.3x higher throughput than the uncompressed baseline. At the same time, it reduces memory usage by 3x and incurs only 1.76% average accuracy loss on LongBench and RULER.

---


### 66. [ClinRAG-GRAPH: Clinical-prior Retrieval-Augmented Graph Model with Domain Adversarial Learning for Breast pCR Prediction](https://arxiv.org/abs/2607.00798)

**<font color=#1a73e8>作者：</font>** Yaofei Duan, Yuhao Huang, Tianyu Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neoadjuvant chemotherapy (NAC) response prediction is clinically important for treatment stratification in breast cancer. However, robust pre-treatment pathological complete response (pCR) prediction remains challenging due to insufficient cross-modal modeling, multicenter imaging heterogeneity, and weak evidence-grounded interpretability. We propose ClinRAG-GRAPH, a Clinically informed Retrieval-Augmented Generation Graph framework, for pre-treatment pCR prediction from DCE-MRI, structured clinical variables, and biopsy-derived pathological biomarkers. ClinRAG-GRAPH constructs an intra-patient clinical-prior graph and applies a prior-guided relation-aware graph convolutional network for structured multimodal representation learning. To improve cross-center robustness, we introduce a dual-branch domain-adversarial learning strategy to suppress protocol-related MRI bias while preserving pCR-relevant features. To enhance interpretability, we further incorporate large language model (LLM)-driven subgraph RAG module that retrieves clinically analogous historical cases and integrates retrieved evidence for pCR inference. We assemble a large-scale multicenter NAC breast cancer cohort for extensive validation, drawing from two public sources and three in-house this http URL show that ClinRAG-GRAPH achieves AUCs of 0.815 on the internal test set and 0.774/0.712 on two external test sets, demonstrating robust pre-treatment pCR prediction across centers. The code is available at the anonymized this https URL.

---


### 67. [Local Motion Matters: A Deconstruct-Recompose Paradigm for Reinforcement Learning Pre-training from Videos](https://arxiv.org/abs/2607.00808)

**<font color=#1a73e8>作者：</font>** Jinwen Wang, Youfang Lin, Xiaobo Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-training on large-scale videos to improve reinforcement learning efficiency is promising yet remains challenging. Existing methods typically treat the agent as an indivisible entity, modeling motion patterns globally. Such global modeling is tightly coupled with the morphology, hindering transfer across domains. In contrast, despite the vast disparity in global motions, the local components exhibit similar motion patterns across different agents. Building on this insight, we propose a novel Deconstruct-Recompose Paradigm (DRP) for learning transferable local motion representations. Specifically, in the Deconstruct phase, we identify multiple local points and track their frame-wise motions, defining each as an Atomic Action. We introduce a Dual-Attention Encoder (DAE) to learn local motion representations from these Atomic Actions, capturing their spatiotemporal relationships. In the Recompose phase, we compose local motion representations with a learnable Motion Aggregation Token [MAT] via latent dynamics model learning. Additionally, an adapter bridges local motion and downstream action-specific dynamics to accelerate policy learning. Extensive experiments demonstrate that our method effectively transfers to diverse robotic control and manipulation tasks, significantly improving sample efficiency and performance.

---


### 68. [From Pixels to Temporal Correlations: Learning Informative Representations for Reinforcement Learning Pre-training](https://arxiv.org/abs/2607.00811)

**<font color=#1a73e8>作者：</font>** Jinwen Wang, Youfang Lin, Xiaobo Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised pre-training on large-scale datasets has demonstrated significant potential for improving the sample efficiency and performance of Reinforcement Learning (RL). Given the large-scale action-free internet videos, existing methods utilize single-step transition prediction and image reconstruction to learn representations. However, these methods prefer to preserve large-proportion stationary information in the pixel space, neglecting small but crucial information. To preserve enough information in the representation, it is essential to pay equal attention to each element in videos. Specifically, we propose a temporal correlation space to distinguish each element. For implementation, we introduce the Multi-scale Temporal Contrastive Learning (MTCL) method to model multi-scale temporal correlations separately. This approach can balance the attention of different elements and yield more informative representations, effectively supporting policy learning in various downstream tasks. Experimental results demonstrate that our method improves sample efficiency and asymptotic performance across various downstream tasks.

---


### 69. [Towards High-Resolution Visual Perception via Hierarchical Entity Exploration](https://arxiv.org/abs/2607.00816)

**<font color=#1a73e8>作者：</font>** Ziyu Ma, Shidong Yang, Yuxiang Ji 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution (HR) image perception remains a key challenge in multimodal large language models (MLLMs), as fine-grained details are often lost when the image is processed as a whole. Existing methods either require training to teach models where to look or heuristically divide the image into fixed regions, both of which struggle to generalize in complex HR scenes. In this work, we propose Hierarchical Entity Exploration (HEE), a training-free and model-agnostic framework that transforms static image understanding into dynamic, query-guided entity exploration. HEE first evaluates each region using a dual scoring mechanism to determine whether it already contains sufficient evidence to answer the question. If not, it applies object detection within the most promising region to extract fine-grained entities, clusters them into coherent subregions, and organizes them into a multi-level semantic hierarchy for deeper exploration. When deeper regions still fail to yield confident answers, a confidence-guided backtracking mechanism revisits alternative paths to ensure adaptive perception. Extensive results show that HEE outperforms training-free methods like ZoomEye and RAP in both accuracy and efficiency on two complex HR benchmarks (Visual Probe and HR-Bench), across different MLLMs such as Qwen2.5-VL and LLaVA-OneVision. Moreover, HEE demonstrates generalization on the MME-RealWorld benchmark.

---


### 70. [MetaHOPE: A Metaphor-Oriented Evaluation Framework for Analysing MT and LLM Translation Errors](https://arxiv.org/abs/2607.00848)

**<font color=#1a73e8>作者：</font>** Jiahui Liang, Lifeng Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this opinion paper, we propose MetaHOPE, an error severity-aware annotation framework for evaluating metaphor translations. Metaphors present challenges for machine translation (MT) and natural language understanding and processing (NLU, NLP), because it presents the features of semantic complexity, contextual dependency, and cultural embeddings that can lead to ambiguity issues for NLP models. To investigate how state-of-the-art NLP models perform on translating metaphors, we select three representative systems, i.e., GoogleMT, GPT5.4, and Hunyuan-7b as Neural MT (NMT) models and LLMs. We used two human-annotated metaphor corpora, including VUAMC and PSUCMC for English-to-Chinese and Chinese-to-English translation purposes. The original corpora we used are monolingual, where we carried out error annotation using the MetaHOPE framework, and also produced the human post-edited gold reference for bilingual use as a new resource. We believe the MetaHOPE evaluation framework for metaphor translation annotation, the parallel corpora resources, and the error analysis on SOTA automatic translation models can be useful and shed some light for the field of metaphor translation study. We share our resources publicly upon paper acceptance.

---


### 71. [Recovering Input Text from Hidden States: Study of Gradient-Based Inversion of Decoder-Only Language Models](https://arxiv.org/abs/2607.00852)

**<font color=#1a73e8>作者：</font>** Mikołaj Słowikowski, Maciej Witold Majewski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work studies the hidden-state inversion problem: recovering the original input token sequence of a decoder-only language model from its last-layer hidden states. Rather than treating inversion as a one-shot reconstruction, we study it as a continuous embedding-space optimisation in which a soft proxy is driven towards the leaked target without any hard-token projection during the search, and a token is committed only once, at the end of the inner loop. This design choice has two consequences which are the main focus of this paper. First, keeping the optimisation entirely in continuous space exposes a rich set of internal signals: rank trajectories of the ground-truth token, per-position loss curves, and a discrete loss measured at commit time. Second, the discrete loss allows assessing the correctness of recovery via cumulative discrete loss. We further analyse which tokens break the reconstructions and find a sharp categorical asymmetry: space-prefixed, high-frequency function words in dense regions of the embedding matrix dominate the failures, while content-bearing tokens are recovered almost perfectly. On 10-token C4 prompts the exact-match rate rises from 66.9% to 97.5% (mean similarity 0.994) as the candidate window is widened, confirming that most errors are recoverable near-misses rather than genuine ambiguities. A comparison with the released SIPIT reference situates these findings: per-step hard projection is faster, but the continuous formulation is what makes the optimisation observable and its failures detectable. The results show that last-layer hidden states of GPT-2 are as sensitive as the original text.

---


### 72. [CAT: Confidence-Adaptive Thinking for Efficient Reasoning of Large Reasoning Models](https://arxiv.org/abs/2607.00862)

**<font color=#1a73e8>作者：</font>** Qizhi Jiang, Shuo Wang, Pei Ke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) have achieved remarkable success on complex tasks by leveraging long chain-of-thought (CoT) trajectories, yet they frequently exhibit overthinking on simple queries, resulting in significant token overhead and reduced inference efficiency. However, existing compression methods predominantly apply uniform length reduction or rely on coarse-grained difficulty estimation, often leading to performance degradation on difficult problems. To address this limitation, we propose Confidence-Adaptive Thinking (CAT), a framework that incorporates the model's intrinsic self-certainty signals as confidence into the preference optimization process, which autonomously modulates reasoning lengths based on problem difficulty. Experimental results show that CAT consistently outperforms state-of-the-art baselines on reasoning accuracy across multiple benchmarks on different base models. Our work enables LRMs to effectively compress confident responses while deliberating on uncertain ones, offering a potentially robust solution for balancing accuracy and latency in practical industrial scenarios.

---


### 73. [OmniView-Space: Reinforcing Spatial Reasoning via Multi-Perspective Spatial Mapping](https://arxiv.org/abs/2607.00881)

**<font color=#1a73e8>作者：</font>** Xudong Li, Mengdan Zhang, Peixian Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence remains a persistent challenge for Multimodal Large Language Models (MLLMs), as it requires coherent spatial scene representations beyond basic object recognition. Existing methods typically build such representations through textual reasoning or 3D reconstruction. However, they often falter during multi-step reasoning, particularly when required to dynamically re-anchor evidence to the specific camera-, object-, or direction-centric reference frames demanded by complex queries. To address this, we propose OmniView-Space, a framework designed to maintain spatial consistency through multimodal egocentric evidence. Our approach consists of three core components: (1) Multi-Perspective Spatial Mapping (MPSM), which re-anchors reconstructed geometry into a query-aligned visual cognitive map and a textual spatial graph; (2) Tool-Guided Egocentric Reasoning, an interleaved policy trained to actively select the ego anchor required by the query and request the corresponding MPSM evidence; and (3) Cognitive-Map Distillation, which uses MPSM-generated trajectories and ego-frame rewards to train the model to reason with self-generated cognitive maps. Experiments on single- and multi-image spatial reasoning benchmarks show that OmniView-Space achieves state-of-the-art performance. Furthermore, the distilled model maintains this performance while reducing reliance on external geometry pipelines.

---


### 74. [MultiSynt/MT: Trillion-Token Multi-Parallel Pre-Training Data Translated Across 36 Languages](https://arxiv.org/abs/2607.00890)

**<font color=#1a73e8>作者：</font>** Maximilian Idahl, Jörg Tiedemann, Sampo Pyysalo 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open web-scale pre-training corpora remain concentrated in English, limiting multilingual LLM development. We introduce MultiSynt/MT, an open synthetic parallel corpus with approximately 4.8 trillion target-language tokens across 36 European languages, produced by translating 100 billion high-quality Nemotron-CC tokens with Tower+ and OPUS-MT/HPLT-MT systems. For many medium- and lower-resource European languages, this is the largest openly available pre-training resource. On a broad multilingual benchmark suite, reference LLMs trained on MultiSynt/MT reach the final score of HPLT 2.0, a native-data baseline, using roughly 72% fewer pre-training tokens, and outperform it by approximately 15% relative at a matched 100B-token training budget. Our analyses also identify evaluation blind spots: standard multiple-choice benchmarks miss translation-quality differences that a fluency-sensitive LLM-as-judge evaluation cleanly recovers on the trained LLMs (with no fluency deficit in MultiSynt itself), and Norwegian idiomatic and culturally grounded tasks remain better served by native data. We release the corpus, including row-aligned translations from multiple systems, to support controlled research on multilingual pre-training data and evaluation.

---


### 75. [Beyond Document Grounding: Span-Level Hallucination Detection over Code, Tool Output, and Documents](https://arxiv.org/abs/2607.00895)

**<font color=#1a73e8>作者：</font>** Ádám Kovács, Bowei He, Xue Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination detection for retrieval-augmented generation (RAG) is usually evaluated on natural-language document evidence. However, grounded generation systems increasingly rely on structured inputs: source code, developer-tool output, markdown documents, tables, and repository metadata. We introduce a unified benchmark for span-level hallucination detection over code, tool output, structured documents, and existing natural-language RAG datasets. The benchmark is built by starting from grounded correct answers, injecting localized hallucinations with exact character labels, and validating the code test split with evidence-based review. Our fine-tuned Qwen3.5-2B detector reaches 0.689 span-F1 on the unified test set and 0.60 on the code-agent source, where it substantially outperforms LettuceDetect-large (0.17) and the strongest zero-shot LLM judges we evaluated (at most 0.22). The same model remains competitive on established natural-language benchmarks, with 81.8 RAGTruth example-F1 and 0.724 English PsiloQA IoU.

---


### 76. [Beyond Activation Alignment:The Alignment-Diversity Tradeoff in Task-Aware LLM Quantization](https://arxiv.org/abs/2607.00908)

**<font color=#1a73e8>作者：</font>** Fei Wang, Chao Xue, Taoran Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-precision quantization (MPQ) has become a key technique for deploying large language models under stringent memory and compute constraints. We first identify a phenomenon that we term the Perplexity Illusion: layers ranked as important by perplexity-based sensitivity show little rank correlation with those that are most influential for complex reasoning performance, with Kendall $\tau \approx 0$ in our analysis. We further reveal an Alignment-Diversity Tradeoff: using only target-task calibration data can degrade post-quantization performance, whereas incorporating general-domain data stabilizes sensitivity estimation and improves robustness across tasks. Based on these observations, we propose TASA (Task-Aware Sensitivity Analysis), a two-level framework that jointly optimizes calibration-data composition and mixed-precision bit allocation. Specifically, TASA searches for a calibration-data mixture using a training-free gradient-trace alignment criterion, and then aggregates perplexity and reasoning-oriented sensitivity signals to guide both inter-layer and intra-layer bit allocation. Experiments on LLaMA-3-8B and Qwen2.5-7B reveal a precision inversion: appropriately allocated 3.5-bit models can match or surpass less task-aware 4-bit baselines. At an average precision of 3.5 bits, TASA matches or outperforms several competitive 4-bit uniform baselines in aggregate accuracy, and improves over the strongest W3 baseline on GSM8K by more than 20 absolute points on LLaMA-3-8B. These results show that calibration-data composition substantially affects task-sensitive quantization, a factor underexplored in prior work.

---


### 77. [Calibrating the Instrument: Controllability of an LLM-Driven Synthetic Population](https://arxiv.org/abs/2607.00910)

**<font color=#1a73e8>作者：</font>** Mirko Degli Esposti  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Generative Synthetic Populations (GSP) -- the convergence of population synthesis, agent-based modelling, and LLM agents -- are attracting growing interest for urban simulation and institutional communication research. Before any GSP instrument is used on a real population, a more basic question must be answered: does it respond to stimuli of known valence in an ordered, replicable, group-structured way? We call this controllability. We ask not whether a synthetic population tracks humans, but whether it tracks itself: whether the latent structure we impose on it is recovered in its own responses. This internal-validity question is logically prior to any claim about external validity, just as characterising an instrument's response function must precede using it to test a theory. We report SIVE (Synthetic Instrument Validation Experiment): a fictional municipality (Montelago) with 120 synthetic personas of known latent structure, exposed to seven conditions spanning strongly positive to strongly negative institutional communications about a water network. Seven pre-registered criteria, evaluated across a temperature sweep, jointly assess fidelity, stability, noise floor, specificity, sensitivity, and ordering. All seven pass at every temperature. A central finding turns a calibration failure into a diagnostic success: a message designed as "weakly positive" was identified by the instrument as functionally negative, traced to unresolved problems, uncertainty, and institutional passivity in its text; a redesigned version restored the expected ordering and interacts with agents' latent trust in unanticipated ways. A noise sub-experiment shows the instrument's intrinsic noise is roughly half the cross-agent estimate and stable across temperatures. Individual trajectories reveal coherent micro-dynamics that summary statistics obscure. Full data are available via an interactive explorer.

---


### 78. [Valdi: Value Diffusion World Models](https://arxiv.org/abs/2607.00917)

**<font color=#1a73e8>作者：</font>** Christopher Lindenberg, Kashyap Chitta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models can enable Model Predictive Control (MPC), but this requires dynamics prediction that is both fast enough for online use and expressive enough to represent uncertain futures. Diffusion models offer a natural mechanism for modeling uncertain dynamics, yet their iterative inference procedure makes them difficult to use for low-latency latent planning. We bridge this gap with Value Diffusion World Models (Valdi), combining end-to-end online training for MPC with a latent diffusion dynamics model. In preliminary experiments on the CarRacing environment, we show that Valdi, using a single diffusion step at both training and inference, matches a deterministic MLP baseline. Our experiments expose a trade-off between predictive multimodality and control performance in this setup. Code is available at this https URL.

---


### 79. [Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis Generation through Conceptual Recombination](https://arxiv.org/abs/2607.00924)

**<font color=#1a73e8>作者：</font>** Subhadeep Pal, Shashwat Sourav, Tirthankar Ghosal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accelerating materials discovery requires AI systems that can generate scientifically valid hypotheses through multi-step, domain-grounded reasoning. Standard large language models often produce fluent but weakly traceable responses to open-ended materials design problems, making it difficult to determine whether final answers are supported by coherent intermediate reasoning. We develop Graph-PRefLexOR, a family of graph-native reasoning models fine-tuned with Group Relative Policy Optimization (GRPO) to organize reasoning into explicit phases for mechanism exploration, graph construction, pattern extraction, and hypothesis synthesis. This design links neural language generation with symbolic relational structure, enabling causal connections to be constructed, inspected, and reused. On 100 open-ended questions from materials science and mechanics literature, Graph-PRefLexOR achieves 40-65% improvements over corresponding base models, with the largest gains in reasoning traceability. Embedding analyses show broader semantic exploration and approximately 2-3 times greater semantic diversity than baselines. Semantic backtracking and layer-wise hidden-state analyses further show stronger alignment between structured reasoning and final answers. Finally, test-time graph expansion reveals that additional compute primarily increases long-range conceptual recombination within a bounded semantic space, rather than simply expanding semantic coverage. These results establish graph-native reinforcement learning as a pathway toward interpretable AI systems for scientific hypothesis generation in materials design and other scientific applications.

---


### 80. [Post-Training Pruning for Diffusion Transformers](https://arxiv.org/abs/2607.00927)

**<font color=#1a73e8>作者：</font>** Chengzhi Hu, Xuewen Liu, Jing Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have demonstrated impressive performance in image generation but suffer from substantial computational overhead and resource consumption. Post-training pruning offers a promising solution; however, due to DiTs' unique architectural design and parameter distribution, traditional pruning methods are inapplicable, leading to significant performance degradation. Specifically, prior methods developed for LLMs, which derive metrics through a series of approximations, amplify the relative contribution of weights in the saliency metric. In addition, weights in DiTs exhibit significantly larger magnitudes than those in LLMs. Moreover, existing pruning granularity overlooks variations in model structures. In this paper, we propose DiT-Pruning, which improves pruning performance by introducing customized saliency criteria and pruning granularity. We design a novel metric that balances the contributions of weights and activations from an energy-based perspective, enabling more effective identification of important elements. Furthermore, we observe distinct clustering patterns in the two-dimensional weight space. Accordingly, we adopt a clustering-aware pruning granularity, enabling effective sparse allocation. Extensive evaluations on various DiTs show that our method consistently preserves image quality, especially under high sparsity. For FLUX.1-dev at 512x512 resolution on MJHQ, DiT-Pruning achieves only a 0.001 loss in CLIP score at 50% sparsity, dramatically outperforming recent pruning methods.

---


### 81. [Persona Non Grata: LLM Persona-Driven Generations in MCQA are Unstable in Distinct Dimensions](https://arxiv.org/abs/2607.00937)

**<font color=#1a73e8>作者：</font>** César Guerra-Solano, Xiang Lorraine Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persona-driven generations (PDGs) have seen prolific use in research and industry applications, where a large language model (LLM) takes on a 'persona' while completing some task. While persona expressed through free-form text (like dialogue) has substantial work investigating stability or consistency, relatively, persona expressed in non-text-heavy outputs (like in multiple-choice question answering, or MCQA) is often overlooked. We work to address this gap, seeking to understand the instability of LLM PDGs in MCQA tasks. We develop three metrics investigating the performance, outcome, and question correctness stability, evaluating three distinct dimensions. Using these metrics, we find that instability varies consistently between model families and model size, and across question domains, with math/commonsense questions leading to greater instability. We also find task prompt format introduces more prediction instability than other hyperparameters, like temperature. Finally, we find that instability is related to task accuracy, and using our instability metrics, find different experimental settings that result in different best and worst personas for tasks, despite their similarity. This reveals the importance of checking hyperparameter instability in PDGs.

---


### 82. [Quantifying the Affective Gap: A Zero-Shot Evaluation of LLMs on Fine-Grained Emotion Taxonomies](https://arxiv.org/abs/2607.00968)

**<font color=#1a73e8>作者：</font>** Lawrence Obiuwevwi, Krzysztof J. Rechowicz, Jessica M. Johnson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion recognition in natural language is a foundational challenge in affective computing, with critical implications for human-computer interaction, mental health support, and conversational AI. This paper presents a rigorous, unified zero-shot evaluation of three leading commercial large language models: Claude (claude-sonnet-4-6), ChatGPT (GPT-5.4), and Gemini (gemini-2.5-flash). The models were queried through their respective production APIs as of April 2026 on a fine-grained 13-class emotion classification task. Using a stratified 1,000-sentence sample from the boltuix/emotions dataset, which comprises 131,306 sentences across 13 categories, a single uniform prompt with no exemplars was applied identically across all models. Gemini achieves the highest accuracy (39.9%) and macro-F1 score (0.363), followed by GPT-5.4 (38.8%, macro-F1 = 0.291) and Claude (38.0%, macro-F1 = 0.159). All models excel on sarcasm and desire while consistently failing on love, confusion, and shame. McNemar tests reveal no statistically significant pairwise differences (p > 0.10), suggesting convergence at a shared zero-shot ceiling. Claude's markedly lower macro-F1 score exposes a class-imbalance prediction bias. These findings highlight the current limitations of frontier AI systems in zero-shot fine-grained emotion classification.

---


### 83. [Bayesian Uncertainty Propagation for Agentic RAG Pipelines: A Proof-of-Concept Study on Multi-Hop Question Answering](https://arxiv.org/abs/2607.00972)

**<font color=#1a73e8>作者：</font>** Louis Donaldson, Connor Walker, Koorosh Aslansefat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trustworthy deployment of Agentic Retrieval-Augmented Generation (RAG) systems requires mechanisms for estimating when multi-stage reasoning pipelines may fail. This paper presents an uncertainty-aware Agentic Retrieval-Augmented Generation (RAG) framework in which planner, evaluator and generator stages produce uncertainty signals derived from semantic divergence and generator self-evaluation. These signals are propagated through a Bayesian Network (BN) to estimate system-level uncertainty and provide node-level indicators of potential failure points across the workflow. The approach is evaluated on StrategyQA and HotpotQA using GPT-3.5-Turbo and GPT-4.1-Nano, with Area Under the Receiver Operating Characteristic Curve (AUROC), Area Under the Accuracy-Rejection Curve (AUARC), Expected Calibration Error (ECE), and Brier Score used to assess discrimination, selective prediction and calibration. Results show that Bayesian propagation is more effective on HotpotQA, where uncertainty accumulates across multi-hop reasoning stages, while StrategyQA exposes limitations caused by miscalibration and unreliable upstream signals. The study positions Bayesian uncertainty propagation as a promising but preliminary mechanism for monitoring Agentic RAG systems, with future validation required in industrial domains such as Offshore Wind (OSW) maintenance decision support.

---


### 84. [SenseWalk: Agent-Based Semantic Trajectory Simulation Powered by Large Language Models in Zoned Environments](https://arxiv.org/abs/2607.00989)

**<font color=#1a73e8>作者：</font>** Ziyue Lin, Xinhang Xie, Kangyi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Semantic trajectory analysis has recently emerged as an approach for modeling human movement by capturing implicit patterns and behaviors through semantic information (e.g., visitors' profiles and goals) beyond raw spatial paths to better understand why people move in certain ways. However, analyzing semantic trajectories in real-world scenarios remains challenging, as collecting high-quality data is costly and often lacks rich semantic information. Meanwhile, existing simulation tools require substantial technical expertise, which makes them difficult for practitioners to adopt. To address these limitations, the paper proposes ${SenseWalk}$, an interactive system that supports simulating semantic trajectories by LLM-powered agents. We develop a simulation workflow that combines LLMs and the social force model to balance physical plausibility and semantic coherence. A user-friendly interface is designed to facilitate users in customizing the simulation configuration and analyzing simulation outputs. We also conduct a quantitative experiment to evaluate the effectiveness of our simulation workflow, and a user study (n=12) to assess the usefulness and efficiency of our system.

---


### 85. [Foundation Models vs. Radiomics for Lung Computed Tomography: A Benchmark of Feature Extractors, Classification Heads, and Segmentation Choices](https://arxiv.org/abs/2607.01001)

**<font color=#1a73e8>作者：</font>** Nils Neukirch, Martin Maurer, Nils Strodthoff  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiomics is the established approach for CT-based lung cancer phenotyping, yet comparisons with foundation models rarely isolate contributions of feature extractor, classification head, and segmentation choice, or test cross-cohort robustness. We benchmark five feature extractors (Curia, Curia-2, DINOv3, Radiomics2D, Radiomics3D), seven classification heads (TabPFN, TabICL, XGBoost, CatBoost, Random Forest, logistic regression, Ridge), and three segmentation regimes on five tasks: tumor volume and stage classification, 2-year survival prediction, histology classification, and age prediction. Models are trained on LUNG1 (n=338) and evaluated on an internal test set (n=84) and the external LUNG2 cohort (n=211), with worst-case cross-cohort performance as the primary metric. The dominant design factor is task-dependent: segmentation drives volume and stage classification, while classifier choice drives survival, histology, and age prediction. Radiomics is competitive for tumor volume, tumor stage and survival (partly due to label-derivation effects for the former); Curia variants reach comparable peak scores for survival; DINOv3 falls slightly short across tasks. Patch and slice aggregation have negligible impact. We recommend Curia with tumor segmentation and a CatBoost head as a safe default, achieving the best mean rank across the three primary clinical tasks, though task-specific selection consistently outperforms any cross-task default. When tumor delineations are unavailable, Curia-2 with lung segmentation and logistic regression offers a competitive alternative. All pipelines use a two-stage design suited to small cohort sizes where end-to-end fine-tuning would risk overfitting.

---


### 86. [Understanding Large Language Models](https://arxiv.org/abs/2607.01006)

**<font color=#1a73e8>作者：</font>** Yannik Keller, Thomas Eisenmann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) represent one of the most significant advances in AI and natural language processing in recent years. Still, many pressing questions about their mechanisms, capabilities, and relationship to human cognition remain highly debated. This chapter aims to outline our current understanding of LLMs by discussing recent evidence on emerging capabilities and their mechanistic implementation within processing layers. We begin with a concise overview of the Transformer architecture, emphasizing how the attention mechanism enables training on massive datasets, allowing LLMs to function as generalist rather than specialized models. Next, we examine emergent LLM capabilities that appear to resemble aspects of human cognition, including symbolic reasoning, theory of mind, and deception strategies. Several studies provide evidence that LLMs can solve tasks previously thought to require human-like cognition. Other studies reveal insightful failure cases that shed light on the differences between human and LLM cognition. Alongside these findings, we review explainable AI approaches ranging from neuron activation analysis to circuit tracing. In the final section, we address current debates concerning what LLMs genuinely understand versus what they merely appear to understand. Prominent arguments against AI anthropomorphism point to the simplicity of LLM training objectives, claiming that LLM behavior is better explained by pattern memorization of training data than by genuine cognition. We argue that this standpoint is guided by misconceptions about optimization processes and cognitive capacity, and advocate for a more nuanced discussion of LLM cognition that neither dismisses the differences between humans and LLMs nor precludes the possibility of AI cognition through overly simplistic reductionist arguments.

---


### 87. [The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology](https://arxiv.org/abs/2607.01033)

**<font color=#1a73e8>作者：</font>** Andrzej Szablewski, Gabriel Konar-Steenberg, Raffaello Fornasiere 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model organisms (MOs) - language models trained to exhibit undesired or unnatural behaviours - are frequently used as testbeds for evaluating white-box interpretability techniques. Current MOs are typically constructed via post-hoc supervised fine-tuning (SFT) on behavioural transcripts or synthetic documents. Prior research has shown that interpretability methods can easily identify hidden behaviours in these MOs. However, recent work suggests that such post-hoc training methods may make interpretability unrealistically easy. We investigate this claim by constructing a suite of 54 $\verb|OLMo2-1B|$- and $\verb|gemma-3-1b-it|$-based MOs trained with seven different techniques, including standard post-hoc SFT, post-hoc DPO, and more realistic integration of MO data into the OLMo post-training DPO phase. We use these MO variants to benchmark activation oracles, activation steering, logit lens, and sparse autoencoders. Our findings show that (i) MO interpretability depends strongly on training objective, target behaviour, model architecture, and training data generation pipeline; (ii) substantial variance remains even after controlling for differences in the strength of target behaviour expression; and (iii) our more realistic $\textit{integrated training}$ often yields less interpretable MOs than standard post-hoc methods. Our results cast substantial doubt on the validity of current MOs as interpretability proxies.

---


### 88. [Behavior-Adaptive Conversational Agents: Toward a Fluid Personality Framework](https://arxiv.org/abs/2607.01034)

**<font color=#1a73e8>作者：</font>** Hasibur Rahman, Smit Desai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based conversational agents (CAs) are now ubiquitous, creating new opportunities for AI-mediated behavior change. Their capacity to project nuanced personalities and adopt diverse metaphorical roles raises a design question: how should an agent's persona and personality be calibrated to the moment? Recent evidence suggests that (i) moderate personality expression outperforms low or high extremes on trust, enjoyment, and intention to adopt in goal-oriented tasks, and (ii) context-appropriate metaphors outperform static one-note assistants on user experience and uptake. Yet most CAs still fix both persona and style, risking misalignment when dynamics, urgency, and formality vary, for example in medical information seeking, fitness coaching, and reflective learning. We propose a Fluid Personality Framework that jointly adapts (1) the agent's metaphorical persona, such as coach, tutor, librarian, or tool, and (2) its personality expression intensity, low, medium, or high, as a function of task context, user goals and traits, and situational urgency. We sketch the framework and its core design dimensions.

---


### 89. [Conversable Complexity: Agentic LLM Collectives as Interpretable Substrates](https://arxiv.org/abs/2607.01047)

**<font color=#1a73e8>作者：</font>** Elias Najarro, Ane Espeseth, Eleni Nisioti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Complexity and interpretability rarely coincide: systems rich enough for complex behaviours to emerge are usually too opaque to question, while transparent ones are too simple for anything complex to emerge. A single large language model (LLM) is a static artefact, hardly exhibiting any of the emergent properties we associate with life. This changes through interaction: populations of LLMs display emergent dynamics absent from isolated models. Furthermore, LLMs can be endowed with persistent memory, tools and shared skills, and the capacity to initiate actions unprompted, i.e., turning LLMs agentic. In this paper, we argue that such collectives of agents can serve as a computational substrate for Artificial Life (ALife) research. Critically, since the agents communicate in natural language, their collective behaviour can be directly interrogated by examining textual traces and asking the agents themselves. We outline the notion of interpretability in language-model research and extend it for collectives of agents. Lastly, we survey recent examples of agentic LLM collectives that already instantiate the idea of agentic substrates, from controlled experiments to deployments in the wild.

---


### 90. [GenAU: Language-Grounded Industrial Anomaly Understanding with Vision-Language Models](https://arxiv.org/abs/2607.01049)

**<font color=#1a73e8>作者：</font>** Hongkuan Zhou, Tristan Rehm, Nadeem Nazer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial inspection requires more than binary anomaly detection: a practical system should determine whether an anomaly exists, localize the defective region, identify the defect type, and provide interpretable visual evidence. Existing CLIP-based methods detect and localize anomalies well but offer limited language-level defect understanding, while instruction-tuned vision-language models can describe defects but do not natively produce pixel-level masks. We introduce GenAU, a Generalist vision-language framework for industrial Anomaly Understanding that unifies image-level detection, pixel-level segmentation, multi-type anomaly detection, and defect analysis in a single instruction-following model. GenAU augments a vision-language model with two segmentation tokens, [SEG_defect] and [SEG_normal], whose hidden states act as language-grounded queries over multi-scale visual features for pixel-level localization; the image-level score fuses this map with the decoder's textual normal/defect decision, while the language decoder produces structured defect-aware responses. Trained with a joint language-modeling and segmentation objective, GenAU covers all four tasks within one architecture and recipe, adding zero-shot multi-type detection and language-grounded defect analysis at a quantified cost to detection and segmentation. Across cross-dataset benchmarks, GenAU attains the strongest image-level detection among CLIP-based zero-shot methods on VisA and Real-IAD, with segmentation approaching but not surpassing specialized CLIP baselines.

---


### 91. [GeoSearcher: Anchor-Guided Progressive Reasoning for Remote Sensing Visual Grounding with Process Supervision](https://arxiv.org/abs/2607.01050)

**<font color=#1a73e8>作者：</font>** Dianyu Wang, Yidan Zhang, Peirong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs) have shown strong cross-modal understanding and coordinate generation abilities in visual grounding. However, transferring these abilities to remote sensing visual grounding (RSVG) remains challenging. High-resolution remote sensing images usually cover large-scale scenes, where targets are often extremely small and surrounded by numerous visually similar distractors. Meanwhile, queries often contain multiple clues, such as reference objects, spatial relations, and target attributes. Existing MLLM-based methods usually formulate RSVG as one-step coordinate generation, which may lead to unstable predictions for small-object localization and complex queries. To address these challenges, we propose GeoSearcher, which reformulates RSVG as an anchor-guided progressive reasoning process and realizes it through two coupled stages: Anchor-Centric Reasoning Supervised Fine-Tuning (ACR-SFT) and Process-Faithful Group Relative Policy Optimization (PF-GRPO). In ACR-SFT, anchor-centric reasoning data are used to teach the model to represent key visual clues as anchors and progressively integrate location, relational, and attribute clues around them. In PF-GRPO, Process-Aware Reward (PAR) and Reasoning-Informative Sample Selector (RISS) further optimize this reasoning behavior by jointly evaluating key reasoning steps and target localization, while focusing training on samples that are more beneficial for improving progressive reasoning. Through this design, GeoSearcher transforms large-scale visual search into a more constrained local reasoning process. Extensive experiments on DIOR-RSVG, OPT-RSVG, and VRS-Bench show that GeoSearcher outperforms existing state-of-the-art methods. The project will be released at this https URL.

---


### 92. [Agentic generation of verifiable rules for deterministic, self-expanding reaction classification](https://arxiv.org/abs/2607.01061)

**<font color=#1a73e8>作者：</font>** Daniel Armstrong, Maarten Dobbelaere, Valentas Olikauskas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-assisted synthesis planning breaks target molecules into accessible precursors using large libraries of reaction rules that assign each transformation a deterministic, interpretable label. But chemistry is long-tailed, making manual encoding intractable, and existing tools rely on fixed rulesets that cannot adapt to new chemistries. Here we present a fully automated pipeline in which a multi-agent framework of large language models (LLMs) classifies reactions and writes the rules themselves across 665,901 US patent reactions, generating each rule under a verification loop that tests it against the corpus. It expands a standard taxonomy from 68 to 14,073 classes without human curation. With a lightweight fingerprint classifier, it classifies 97.7\% of unseen reactions, matching a leading proprietary classifier while resolving chemistry more finely and extending on demand to chemistry outside its training distribution. The result is a living reactivity database and a general route to turning generative models into reliable, self-expanding symbolic systems.

---


### 93. [GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache](https://arxiv.org/abs/2607.01065)

**<font color=#1a73e8>作者：</font>** Soosung Kim, Minjae Park, Eui-Young Chung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The deployment of Large Language Models (LLMs) with extended context windows is increasingly constrained by the linear growth of Key-Value (KV) cache memory. Vector Quantization (VQ), particularly Residual Quantization (RQ), is a promising approach for pushing KV cache storage toward the sub-1-bit regime by progressively encoding residuals with small codebooks. However, most VQ methods still rely on standard $\ell_2$ $K$-means as the core codebook-learning primitive. We identify a subtle high-dimensional issue of this primitive: Euclidean centroid averaging can induce centroid shrinkage, which weakens the angular alignment term in the $\ell_2$ distortion and makes directional preservation harder. To address this issue, we propose Gain-Shape $K$-means (GSKM), a drop-in replacement for $K$-means that improves directional fidelity while matching, and in some regimes improving, $\ell_2$ distortion. We then build Gain-Shape Residual Quantization (GSRQ) by incorporating a weighted extension of GSKM into an RQ pipeline. On LLaMA-3-8B, GSRQ substantially improves over strong KV cache quantization baselines across bit rates. At 1-bit, it improves the average accuracy across LongBench tasks from 11.34 to 33.54, a gain of 22.20 percentage points over VQLLM.

---


### 94. [Message Passing Enables Efficient Reasoning](https://arxiv.org/abs/2607.01077)

**<font color=#1a73e8>作者：</font>** Xuecheng Liu, Daman Arora, Gokul Swamy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While inference-time scaling has improved the reasoning abilities of large language models (LLMs), the need to generate long chains-of-thought (CoTs) is a computational bottleneck. Thus, in contrast to sequential scaling methods like CoT, recent parallel scaling techniques instead use fork and join (FJ) primitives to divide work across multiple LLM threads. However, in the fork-join paradigm, threads are typically transient and do not communicate pointwise with one another which limits scalability. To tackle this, we introduce Message Passing Language Models (MPLMs), a framework for LLM reasoning in which threads communicate directly via lightweight send and receive primitives. MPLMs enable efficient scaling through two key mechanisms: (1) reduced communication costs, achieved by avoiding redundant context sharing, and (2) preemption, which allows threads to terminate early based on partial information from their peers.
We demonstrate the promise of MPLMs on 3 classes of tasks. First, on Sudoku puzzles, we show that MPLMs require an asymptotically smaller context than both serial CoT and parallel FJ. We then fine-tune a single model to solve 25 x 25 puzzles that remain challenging for standard CoT and FJ approaches, as well as frontier reasoning models without tools. Second, on 3-SAT puzzles, the capability of preemption allows termination of unpromising branches, which results in improved efficiency. Finally, we show that appropriately prompted large pre-trained models follow the MPLM protocol, achieving competitive results on long-context question answering relative to popular fork-join approaches.

---


### 95. [Staleness-Learning Rate Scaling Laws for Asynchronous RLHF](https://arxiv.org/abs/2607.01083)

**<font color=#1a73e8>作者：</font>** Jingwei Song, Haofeng Xu, Jie Xiao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-throughput RLHF systems often decouple rollout generation from policy optimization, leading to the use of stale rollouts during learner updates. In this work, we study the effect of such staleness in asynchronous GRPO. We make the behavior policy explicit in the GRPO surrogate objective and distinguish between the surrogate-gradient mapping used by the learner and the true total derivative of a distribution-dependent population objective. Under assumptions of local boundedness, distributional smoothness, and behavior-policy smoothness, we show that stale rollouts introduce a per-step surrogate-gradient bias of order O(S * eta), where S denotes the maximum rollout lag and eta denotes the learning rate. We further derive a conditional collapse-time scaling law: when within-cycle drift remains below a batch-level clipping radius, collapse is governed primarily by cumulative learner drift T * eta; when the stale-rollout constraint is active, stability instead depends explicitly on S * eta. This yields a two-constraint stability condition eta << min{R_batch / (S * G_upd), R_crit / (T * G_upd)}, explaining why the maximum stable learning rate may appear weakly dependent on staleness in the horizon-limited regime.

---


### 96. [Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use](https://arxiv.org/abs/2607.01084)

**<font color=#1a73e8>作者：</font>** Song-Lin Lv, Weiming Wu, Rui Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Model (LLM) agents demonstrate proficiency in static benchmarks, their deployment in real-world scenarios is hindered by the dynamic nature of user queries, tool sets, and interaction dynamics. To address this generalization gap, we formalize OpenAgent (Tool-Use Agent in Open-World), a problem setting characterized by distributional shifts across query, action, observation, and domain dimensions. To systematically diagnose its impact, we construct a controlled sandbox environment where we define fine-grained environmental shifts across a four-tier hierarchy, Perception, Interaction, Reasoning, and Internalization, and conduct a comprehensive series of experiments. Our analysis yields a series of key insights, demonstrating that agents trained via both Supervised Fine-Tuning(SFT) and Reinforcement Learning suffer from varying degrees of performance degradation when confronting open environmental shifts. Building on these insights, we propose Perturbation-Augmented Fine-Tuning, a disturbance-based intervention strategy for SFT that lays the foundation for enhancing agent robustness and utility in realistic environments. Our code will be released at: https://github. com/LAMDA-NeSy/OpenAgent.

---


### 97. [LongVQUBench: Benchmarking Long-Term Video Quality Understanding of Vision-Language Models](https://arxiv.org/abs/2607.01086)

**<font color=#1a73e8>作者：</font>** Arpita Nema, Hanwei Zhu, Xi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The evaluation of long-term video quality understanding remains an open challenge for large vision-language models (LVLMs). Existing video quality benchmarks predominantly focus on short clips and isolated distortions, overlooking the temporal continuity, cumulative degradation, and reasoning complexity inherent in long-duration content. To address these limitations, we present LongVQUBench, a comprehensive benchmark for long-term video quality understanding. LongVQUBench contains over 1200 diverse videos spanning movies, documentaries, surveillance footage, egocentric recordings, and animated content, accompanied by 1500 multiple-choice and open-ended questions for validation and testing. To assess perceptual reasoning across different temporal scopes, we introduce three progressively complex evaluation levels: (i) local event quality understanding (LQU) for analyzing localized distortions; (ii) cross-event quality reasoning (CQR) for integrating multiple degraded events; and (iii) global quality understanding (GQU) for holistic perceptual evaluation over extended durations. Furthermore, a needle distortion question-answering (NDQA) paradigm is embedded across all three levels, where spatial or temporal artifacts are sparsely inserted to probe fine-grained detection and reasoning capabilities. Extensive experiments on 14 state-of-the-art LVLMs reveal significant performance degradation with increasing video length and reasoning depth, highlighting their limited capacity for long-range temporal integration and perceptual attribution. We envision LongVQUBench as a foundational step toward the systematic, hierarchical, and explainable evaluation of LVLMs' long-term video quality understanding.

---


### 98. [Clinician-Level Agreement Without Clinical Caution: LLM Evaluator Limits in Medical AI Benchmarking](https://arxiv.org/abs/2607.01103)

**<font color=#1a73e8>作者：</font>** William Philipp, Finn Fassbender, Thorsten Langer 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-response evaluation provides stronger clinical validity than multiple-choice benchmarks but creates a scoring bottleneck that motivates automated LLM-asa-Judge approaches. Whether such evaluators replicate clinical calibration and caution, however, remains untested. We introduce MedQADE, the first standardised open-response clinical benchmark for German, a major clinical language lacking native evaluation infrastructure, comprising 3,800 items annotated by ten practising physicians and nine Large Language Model (LLM) evaluators. The top-performing evaluator model, Gemini 3 Flash, reached alignment consistent with the physician ceiling (\k{appa} = 0.694 vs. \k{appa} = 0.709), though wide confidence intervals limit interpretation. Despite this statistical alignment, automated evaluators exhibited near-absent clinical metacognition: physicians scaled abstention with item difficulty, while frontier models assigned definitive scores in every case. We additionally quantified systematic lineage-dependent biases, where models preferentially scored architectural siblings, an effect independent of language. These results show that statistical alignment does not ensure clinical caution, and that evaluator independence requires explicit verification.

---


### 99. [CausalMix: Data Mixture as Causal Inference for Language Model Training](https://arxiv.org/abs/2607.01104)

**<font color=#1a73e8>作者：</font>** Zinan Tang, Yukun Zhang, Shaomian Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In Large Language Model (LLM) training, data mixing plays a pivotal role in determining model performance. Recent methods optimize mixture weights via proxy models, but they rely on the assumption of static data distributions. As a result, when the underlying data pool shifts, these methods require costly retraining from scratch. This limitation restricts their ability to scale seamlessly from small settings to larger data pools and model sizes. In this paper, we propose CausalMix to address this limitation by casting data mixture optimization as a causal inference problem. We formulate the statistical features of the data pool as covariates and the domain mixture as the treatment. After fitting a causal model on 512 runs of Qwen2.5-0.5B to estimate the Conditional Average Treatment Effect (CATE), we extrapolate the optimal mixture for an 800K data pool and apply it to train a 7B model. Furthermore, we successfully generalize the framework to long chain-of-thought data on Qwen3-4B-Base. By leveraging causal modeling to isolate confounding biases, CausalMix dynamically infers state-dependent optimal data mixtures. Extensive experiments show that the mixture guided by CausalMix consistently improves performance across multiple downstream tasks, outperforming RegMix and other baselines. In addition, we use the CATE Interpreter to provide visual analysis of the learned mixing strategy. Overall, CausalMix offers a causal and interpretable framework for optimizing LLM data mixtures.

---


### 100. [Towards Developing a Multimodal Chat Assistant for University Stakeholders: RAG-based Approach](https://arxiv.org/abs/2607.01115)

**<font color=#1a73e8>作者：</font>** Md Abu Hanif Shaikh, Abdullah Al Shafi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> University stakeholders often face difficulties in accessing timely and reliable information, especially in developing countries, where there are very few intelligent support systems. Existing rule-based chatbots are unable to handle complex, domain-specific queries and are not well-equipped to adapt to evolving institutional policies. As a fill-in-the-gap solution, we present the multimodal university chatbot with retrieval-augmented generation. The system combines the large language model with semantic retrieval to produce context-based responses from institution-centric resources, such as the university handbook. The system accepts text and image queries through the vision-language model and applies quantized inference for rapid deployment on constrained hardware. A scalable backend built with FastAPI, adjoined with a responsive frontend developed with this http URL, ensures real-time usability. Our multimodal evaluation demonstrates that the system maintains strong satisfaction scores across both text and image queries, despite increased response time for visual inputs. Furthermore, quantitative evaluation shows that hallucination is reduced from 31.7% to 6.6% in our proposed RAG-based system, confirming the effectiveness of retrieval grounding.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-110](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
