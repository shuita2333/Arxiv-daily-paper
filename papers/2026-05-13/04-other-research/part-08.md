# 📦 其他研究 | 2026年05月13日

> 本类共 **396** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-396**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-396**

---

### 351. [Contrastive Learning under Noisy Temporal Self-Supervision for Colonoscopy Videos](https://arxiv.org/abs/2605.12320)

**<font color=#1a73e8>作者：</font>** Luca Parolari, Pietro Gori, Lamberto Ballan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning robust representations of polyp tracklets is key to enabling multiple AI-assisted colonoscopy applications, from polyp characterization to automated reporting and retrieval. Supervised contrastive learning is an effective approach for learning such representations, but it typically relies on correct positive and negative definitions. Collecting these labels requires linking tracklets that depict the same underlying polyp entity throughout the video, which is costly and demands specialized clinical expertise. In this work, we leverage the sequential workflow of colonoscopy procedures to derive self-supervised associations from temporal structure. Since temporally derived associations are not guaranteed to be correct, we introduce a noise-aware contrastive loss to account for noisy associations. We demonstrate the effectiveness of the learned representations across multiple downstream tasks, including polyp retrieval and re-identification, size estimation, and histology classification. Our method outperforms prior self-supervised and supervised baselines, and matches or exceeds recent foundation models across all tasks, using a lightweight encoder trained on only 27 videos. Code is available at this https URL.

---


### 352. [LISA: Cognitive Arbitration for Signal-Free Autonomous Intersection Management](https://arxiv.org/abs/2605.12321)

**<font color=#1a73e8>作者：</font>** Abderrahmane Lakas, Mohamed Amine Ferrag, Merouane Debbah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show strong potential for Intelligent Transportation Systems (ITS), particularly in tasks requiring situational reasoning and multi-agent coordination. These capabilities make them well suited for cooperative driving, where rule-based approaches struggle in complex and dynamic traffic environments. Intersection management remains especially challenging due to conflicting right-of-way demands, heterogeneous vehicle priorities, and vehicle-specific kinematic constraints that must be resolved in real time. However, existing approaches typically use LLMs as auxiliary components on top of signal-based systems rather than as primary decision-makers. Signal controllers remain vehicle-agnostic, reservation-based methods lack intent awareness, and recent LLM-based systems still depend on signal infrastructure. In addition, LLM inference latency limits their use in sub-second control settings.
We propose LISA (LLM-Based Intent-Driven Speed Advisory), a signal-free cognitive arbitration framework for autonomous intersection management. LISA uses an LLM to reason over declared vehicle intents, incorporating priority classes, queue pressure, and energy preferences. We evaluate LISA against fixed-cycle control, SCATS, AIM, and GLOSA across varying traffic loads. Results show that LISA reduces mean control delay by up to 89.1% and maintains Level of Service C while all non-LLM baselines degrade to Level of Service F. Under near-saturated demand, LISA reduces mean waiting time by 93% and peak queue length by 60.6% relative to fixed-cycle control. It also lowers fuel consumption by up to 48.8% and achieves 86.2% intent satisfaction, compared to 61.2% for the best non-LLM method. These results demonstrate that LLM-based reasoning can enable real-time, signal-free intersection management.

---


### 353. [VIP: Visual-guided Prompt Evolution for Efficient Dense Vision-Language Inference](https://arxiv.org/abs/2605.12325)

**<font color=#1a73e8>作者：</font>** Hao Zhu, Shuo Jin, Wenbin Liao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pursuing training-free open-vocabulary semantic segmentation in an efficient and generalizable manner remains challenging due to the deep-seated spatial bias in CLIP. To overcome the limitations of existing solutions, this work moves beyond the CLIP-based paradigm and harnesses the recent spatially-aware this http URL framework to facilitate more efficient and high-quality dense prediction. While this http URL exhibits robust spatial awareness, we find that the semantic ambiguity of text queries gives rise to severe mismatch within its dense cross-modal interactions. To address this, we introduce \textcolor{oursblue}{\textbf{VI}}sual-guided \textcolor{oursblue}{\textbf{P}}rompt evolution (\textcolor{oursblue}{\textbf{\textit{VIP}}}) to rectify the semantic expressiveness of text queries in this http URL, unleashing its potential for fine-grained object perception. Towards this end, \VIP integrates alias expansion with a visual-guided distillation mechanism to mine valuable semantic cues, which are robustly aggregated in a saliency-aware manner to yield a high-fidelity prediction. Extensive evaluations demonstrate that \VIP: \ding{182} surpasses the top-leading methods by $1.4\% \sim 8.4\%$ average mIoU, \ding{183} generalizes well to diverse challenging domains, and \ding{184} requires marginal inference time and memory overhead. \href{this https URL}{Our code is publicly available at GitHub \faGithub}.

---


### 354. [A categorical error sensitivity index (ISEC): A preventive ordinal decision-support measure for irrecoverable errors in manual data entry systems](https://arxiv.org/abs/2605.12328)

**<font color=#1a73e8>作者：</font>** Ricardo Raúl Palma, Mauro Anibal Benetti, Fabricio Orlando Sanchez Varretti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data entry systems remain structurally vulnerable to categorical misclassifications, particularly in small and medium sized enterprises (SMEs). When nominal categories exhibit semantic or morphological proximity, human machine interaction may produce errors that are irrecoverable ex post. In the absence of automated input controls, manual data entry frequently generates irrecoverable categorical distortions that propagate into Key Performance Indicators (KPIs), thereby misleading managerial decision making. State of the art normalization tools typically evaluate semantic and morphological dimensions in isolation and rely heavily on standard dictionaries, rendering them ineffective for SME master data rich in custom SKUs, abbreviations, and domain-specific technical jargon. This paper introduces the Categorical Error Sensitivity Index (ISEC), an ordinal composite score designed to rank category pairs according to their structural susceptibility to confusion. ISEC integrates semantic distance (via word embeddings), custom weighted morphological transformation costs (through an adapted Damerau Levenshtein algorithm), and empirical frequency into a unified, mathematically robust preventive framework. By leveraging vector database architectures, ISEC reduces computational complexity, achieving approximately a 195x performance improvement over brute-force methods. Validated across three heterogeneous datasets: governmental judicial records, retail inventory, and a synthetic ISO coded metalworking catalog, ISEC provides a scalable and proactive data governance instrument that enables SMEs to detect latent structural risk embedded within their categorical data assets.

---


### 355. [Manifold Sampling via Entropy Maximization](https://arxiv.org/abs/2605.12338)

**<font color=#1a73e8>作者：</font>** Cornelius V. Braun, Tilman Burghoff, Marc Toussaint  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from constrained distributions has a wide range of applications, including in Bayesian optimization and robotics. Prior work establishes convergence and feasibility guarantees for constrained sampling, but assumes that the feasible set is connected. However, in practice, the feasible set often decomposes into multiple disconnected components, which makes efficient sampling under constraints challenging. In this paper, we propose MAnifold Sampling via Entropy Maximization (MASEM) for sampling on a manifold with an unknown number of disconnected components, implicitly defined by smooth equality and inequality constraints. The presented method uses a resampling scheme to maximize the entropy of the empirical distribution based on k-nearest neighbor density estimation. We show that, in the mean field, MASEM decreases the KL-divergence between the empirical distribution and the maximum-entropy target exponentially in the number of resampling steps. We instantiate MASEM with multiple local samplers and demonstrate its versatility and efficiency on synthetic and robotics-based benchmarks. MASEM enables fast and scalable mixing across a range of constrained sampling problems, improving over alternatives by an order of magnitude in Sinkhorn distance with competitive runtime.

---


### 356. [Neural-Schwarz Tiling for Geometry-Universal PDE Solving at Scale](https://arxiv.org/abs/2605.12343)

**<font color=#1a73e8>作者：</font>** Paolo Secchi, Daniel S. Balint, Marco Maurizi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most learned PDE solvers follow a global-surrogate paradigm: a neural operator is trained to map full problem descriptions to full solution fields for a prescribed distribution of geometries, boundary conditions, and coefficients. This has enabled fast inference within fixed problem families, but limits reuse across new domains and makes large-scale deployment dependent on expensive problem-specific data generation. We introduce $\textbf{NEST}$ ($\textbf{Ne}$ural-$\textbf{S}$chwarz $\textbf{T}$iling), a local-to-global framework that shifts learning from full-domain solution operators to reusable local physical solvers. The central premise is that, although global PDE solutions depend on geometry, scale, and boundary conditions, the physical response on small neighborhoods can be learned locally and composed into global solutions through classical domain decomposition. NEST learns a neural operator on minimal voxel patches ($3 \times 3 \times 3$) with diverse local geometries and boundary/interface data. At inference time, an unseen voxelized domain is tiled into overlapping patches, the learned local solver is applied patchwise, and global consistency is enforced through iterative Schwarz coupling with partition-of-unity assembly. In this way, generalization is shifted from a monolithic neural model to the combination of local physics learning and algorithmic global assembly. We instantiate NEST on nonlinear static equilibrium in compressible neo-Hookean solids and evaluate it on large, geometrically complex 3D domains far outside the scale of the training patches. Our results show that local neural building blocks, coupled through Schwarz iteration, offer a reusable local-training path toward scalable learned PDE solvers that generalize across domain size, shape, and boundary-condition configurations.

---


### 357. [Optimized but Unowned: How AI-Authored Goals Undermine the Motivation They Are Meant to Drive](https://arxiv.org/abs/2605.12344)

**<font color=#1a73e8>作者：</font>** Vivienne Bihe Chi, Roman Rietsche, Andreas Göldi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI tools become embedded in productivity and self-improvement contexts, a pressing question emerges: what happens when AI does the goal-setting for us? While large language models can generate goals that are objectively well-formed, the motivational consequences of delegating this cognitively and emotionally significant task remain unknown. In a preregistered experiment (N = 470), we compared self-authored goals against LLM-authored goals derived from a personal reflection. Although LLM-generated goals scored higher on SMART criteria (specificity, measurability, achievability, relevance, and time-boundedness; d = 2.26), participants in the LLM condition reported lower psychological ownership (d = 1.38), commitment (d = 1.19), and perceived importance (d = 1.13). At two-week follow-up, 72.8% of self-authored participants had acted on two or more of their goals, compared to 46.6% in the LLM condition. Mediation analyses identified psychological ownership as the mechanism: it mediated the authorship effect on every downstream motivational and behavioral outcome, while objective goal quality did not. Critically, individuals low in trait self-efficacy, those most likely to seek AI assistance, experienced the steepest ownership erosion. These findings reveal a quality-motivation dissociation in AI-assisted goal-setting and identify authorship preservation as a design priority for AI tools deployed in identity-relevant, behavior-dependent tasks.

---


### 358. [Output Composability of QLoRA PEFT Modules for Plug-and-Play Attribute-Controlled Text Generation](https://arxiv.org/abs/2605.12345)

**<font color=#1a73e8>作者：</font>** Michela Lorandi, Anya Belz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) techniques offer task-specific fine-tuning at a fraction of the cost of full fine-tuning, but require separate fine-tuning for every new task (combination). In this paper, we explore three ways of generalising beyond single-task training/inference: (i) training on combinations of multiple, related datasets; (ii) at inference, composing the weight matrices of separately trained PEFT modules; and (iii) at inference, composing the outputs of separately trained PEFT modules. We test these approaches on three different LLMs, QLoRA as the PEFT technique, and three sets of controlled text generation datasets for sentiment control, topic control, and multi-attribute control. We find that summing PEFT module outputs is a particularly strong composition method, which consistently either outperforms or matches the performance of alternative approaches. This is the case even when comparing against single-task specialised modules on the single-task test set, where three-module output composition achieves an average 2% point performance increase across all models for sentiment control.

---


### 359. [A New Technique for AI Explainability using Feature Association Map](https://arxiv.org/abs/2605.12350)

**<font color=#1a73e8>作者：</font>** Sayantani Ghosh, Amit Kumar Das, Amlan Chakrabarti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lack of transparency in AI systems poses challenges in critical real-life applications. It is important to be able to explain the decisions of an AI system to ensure trust on the system. Explainable AI (XAI) algorithms play a vital role in achieving this objective. In this paper, we are proposing a new algorithm for Explaining AI systems, FAMeX (Feature Association Map based eXplainability). The proposed algorithm is based on a graph-theoretic formulation of the feature set termed as Feature Association Map (FAM). The foundation of the modelling is based on association between features. The proposed FAMeX algorithm has been found to be better than the competing XAI algorithms - Permutation Feature Importance (PFI) and SHapley Additive exPlanations (SHAP). Experiments conducted with eight benchmark algorithms show that FAMeX is able to gauge feature importance in the context of classification better than the competing algorithms. This definitely shows that FAMeX is a promising algorithm in explaining the predictions from an AI system

---


### 360. [From Message-Passing to Linearized Graph Sequence Models](https://arxiv.org/abs/2605.12358)

**<font color=#1a73e8>作者：</font>** Joël Mathys, Basil Rohner, Saku Peltonen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Message-passing based approaches form the default backbone of most learning architectures on graph-structured data. However, the rapid progress of modern deep learning architectures in other domains, particularly sequence modeling, raises the question of how graph learning can benefit from these advances. We introduce Linearized Graph Sequence Models, a framework that recasts message-passing graph computation from the perspective of sequence modeling to simplify architectural choices. Our approach systematically separates the computational processing depth from the information propagation depth, allowing core graph architectural decisions to be treated as sequence modeling choices. Specifically, we analyze, both empirically and theoretically, what sequence properties make methods effective for learning and preserving the graph inductive bias. In particular, we validate our findings, demonstrating improved performance on long-range information tasks in graphs. Our findings provide a principled way to integrate modern sequence modeling advances into message-passing based graph learning. Beyond this, our work demonstrates how the separation of processing and information depth can recast central architectural questions as input modeling choices.

---


### 361. [MetaColloc: Optimization-Free PDE Solving via Meta-Learned Basis Functions](https://arxiv.org/abs/2605.12368)

**<font color=#1a73e8>作者：</font>** Zichuan Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving partial differential equations (PDEs) with machine learning typically requires training a new neural network for every new equation. This optimization is slow. We introduce MetaColloc. It is an optimization-free and data-free framework that removes this bottleneck completely. We decouple basis discovery from the solving process. We meta-train a dual-branch neural network on diverse Gaussian Random Fields. This offline process creates a universal dictionary of neural basis functions. At test time, we freeze the network. We solve the PDE by assembling a collocation matrix. We find the solution through a single linear least squares step. For non-linear PDEs, we apply the Newton-Raphson method to achieve fast quadratic convergence. Our experiments across six 2D and 3D PDEs show massive improvements. MetaColloc reaches state-of-the-art accuracy on smooth and non-linear problems. It also reduces test-time computation by several orders of magnitude. Finally, we provide a detailed frequency sweep analysis. This analysis reveals a critical mismatch between function approximation and operator stability at extremely high frequencies. This profound finding opens a clear path toward future operator-aware meta-learning.

---


### 362. [Context Convergence Improves Answering Inferential Questions](https://arxiv.org/abs/2605.12370)

**<font color=#1a73e8>作者：</font>** Jamshid Mozafari, Bhawna Piryani, Adam Jatowt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) are widely used in open-domain Question Answering (QA), their ability to handle inferential questions-where answers must be derived rather than directly retrieved-remains still underexplored. This study investigates how the structure and quality of passages influence LLM performance on such questions. We focus on convergence, a measure of how effectively sentences (hints) eliminate incorrect answers, as a criterion for constructing passages. Using subsets of the TriviaHG dataset, we form passages by combining sentences with varying convergence levels and evaluate six LLMs of different sizes and architectures. Our results show that passages built from higher convergence sentences lead to substantially better answer accuracy than those selected by cosine similarity, indicating that convergence captures meaningful relevance for inferential reasoning. Additionally, ordering sentences by descending convergence slightly improves performance, suggesting that LLMs tend to prioritize earlier, information-rich cues. These findings highlight convergence as a practical signal for guiding passage construction and analyzing inferential reasoning behavior in LLMs.

---


### 363. [Agent-Based Post-Hoc Correction of Agricultural Yield Forecasts](https://arxiv.org/abs/2605.12375)

**<font color=#1a73e8>作者：</font>** Matthew Beddows, Aiden Durrant, Georgios Leontidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate crop yield forecasting in commercial soft fruit production is constrained by the data available in typical commercial farm records, which lack the sensor networks, satellite imagery, and high-resolution meteorological inputs that most state-of-the-art approaches assume. We propose a structured LLM agent framework that performs post-hoc correction of existing model predictions, encoding agricultural domain knowledge across tools for phase detection, bias learning, and range validation. Evaluated on a proprietary strawberry yield dataset and a public USDA corn harvest dataset, agent refinement of XGBoost reduced MAE by 20% and MASE by 56% on strawberry, with consistent improvements across Moirai2 (MAE 24%, MASE 22%) and Random Forest (MAE 28%, MASE 66%) baselines. Using Llama 3.1 8B as the agent produced the strongest corrections across all configurations; LLaVA 13B showed inconsistent gains, highlighting sensitivity to the choice of refinement model.

---


### 364. [Fast Image Super-Resolution via Consistency Rectified Flow](https://arxiv.org/abs/2605.12377)

**<font color=#1a73e8>作者：</font>** Jiaqi Xu, Wenbo Li, Haoze Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models (DMs) have demonstrated remarkable success in real-world image super-resolution (SR), yet their reliance on time-consuming multi-step sampling largely hinders their practical applications. While recent efforts have introduced few- or single-step solutions, existing methods either inefficiently model the process from noisy input or fail to fully exploit iterative generative priors, compromising the fidelity and quality of the reconstructed images. To address this issue, we propose FlowSR, a novel approach that reformulates the SR problem as a rectified flow from low-resolution (LR) to high-resolution (HR) images. Our method leverages an improved consistency learning strategy to enable high-quality SR in a single step. Specifically, we refine the original consistency distillation process by incorporating HR regularization, ensuring that the learned SR flow not only enforces self-consistency but also converges precisely to the ground-truth HR target. Furthermore, we introduce a fast-slow scheduling strategy, where adjacent timesteps for consistency learning are sampled from two distinct schedulers: a fast scheduler with fewer timesteps to improve efficiency, and a slow scheduler with more timesteps to capture fine-grained texture details. Extensive experiments demonstrate that FlowSR achieves outstanding performance in both efficiency and image quality.

---


### 365. [Discrete Flow Matching for Offline-to-Online Reinforcement Learning](https://arxiv.org/abs/2605.12379)

**<font color=#1a73e8>作者：</font>** Fairoz Nower Khan, Nabuat Zaman Nahim, Peizhong Ju  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many reinforcement learning (RL) tasks have discrete action spaces, but most generative policy methods based on diffusion and flow matching are designed for continuous control. Meanwhile, generative policies usually rely heavily on offline datasets and offline-to-online RL is itself challenging, as the policy must improve from new interaction without losing useful behavior learned from static data. To address those challenges, we introduce DRIFT, an online fine-tuning method that updates an offline pretrained continuous-time Markov chain (CTMC) policy with an advantage-weighted discrete flow matching loss. To preserve useful pretrained knowledge, we add a path-space penalty that regularizes the full CTMC trajectory distribution, rather than only the final action distribution. For large discrete action spaces, we introduce a candidate-set approximation that updates the actor over a small subset of actions sampled from reference-policy rollouts and uniform exploration. Our theoretical analysis shows that the candidate-set error is controlled by missing target probability mass, and the induced CTMC generator error decreases as the candidate set covers more high-probability actions. Experiments on prevailing discrete action RL task show that our method provides stable offline-to-online improvement across all tasks, achieving the highest average score on Jericho with a simple GRU encoder while outperforming methods that use pretrained language models. Controlled experiments further confirm that the path-space penalty remains bounded during fine-tuning and that the CTMC generator adapts to shifted rewards faster than deterministic baselines. The candidate-set mechanism is supported by a stability analysis showing that the generator error decreases exponentially with candidate coverage.

---


### 366. [Events as Triggers for Behavioral Diversity in Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.12388)

**<font color=#1a73e8>作者：</font>** Hannes Büchi, Manon Flageat, Eduardo Sebastián 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Effective multi-agent cooperation requires agents to adopt diverse behaviors as task conditions evolve-and to do so at the right moment. Yet, current Multi-Agent Reinforcement Learning (MARL) frameworks that facilitate this diversity are still limited by the fact that they bind fixed behaviors to fixed agent identities. Consequently, they are ill-equipped for tasks where agents need to take on different roles at very specific moments in time. We argue that, to define these behavioral transitions, the missing ingredient is events. Events are changes in the state of the system that induce qualitative changes in the task. Based on this view, we introduce a framework that decouples agent identity from behavior, capturing a continuous manifold from which agents instantiate their behaviors in response to events. This framework is based on two elements. First, to build an expressive behavior manifold, we introduce Neural Manifold Diversity (NMD), a formal distance metric that remains well-defined when behaviors are transient and agent-agnostic. Second, we use an event-based hypernetwork that generates Low-Rank Adaptation (LoRA) modules over a shared team policy, enabling on-the-fly agent-policy reconfiguration in response to events. We prove that this construction ensures that diversity does not interfere with reward maximization by design. Empirical results demonstrate that our framework outperforms established baselines across benchmarks while exhibiting zero-shot generalization, and being the only method that solves tasks requiring sequential behavior reassignment.

---


### 367. [SEMIR: Semantic Minor-Induced Representation Learning on Graphs for Visual Segmentation](https://arxiv.org/abs/2605.12389)

**<font color=#1a73e8>作者：</font>** Luke James Miller, Yugyung Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmenting small and sparse structures in large-scale images is fundamentally constrained by voxel-level, lattice-bound computation and extreme class imbalance -- dense, full-resolution inference scales poorly and forces most pipelines to rely on fixed regionization or downsampling, coupling computational cost to image resolution and attenuating boundary evidence precisely where minority structures are most informative. We introduce SEMIR (Semantic Minor-Induced Representation Learning), a representation framework that decouples inference from the native grid by learning a task-adapted, topology-preserving latent graph representation with exact decoding. SEMIR transforms the underlying grid graph into a compact, boundary-aligned graph minor through parameterized edge contraction, node deletion, and edge deletion, while preserving an exact lifting map from minor predictions to lattice labels. Minor construction is formalized as a few-shot structure learning problem that replaces hand-tuned preprocessing with a boundary-alignment objective: minor parameters are learned by maximizing agreement between predicted boundary elements and target-specific semantic edges under a boundary Dice criterion, and the induced minor is annotated with scale- and rotation-robust geometric and intensity descriptors and supports efficient region-level inference via message passing on a graph neural network (GNN) with relational edge features. We benchmark SEMIR on three tumor segmentation datasets -- BraTS 2021, KiTS23, and LiTS -- where targets exhibit high structural variability and distributional uncertainty. SEMIR yields consistent improvements in minority-structure Dice at practical runtime. More broadly, SEMIR establishes a framework for learning task-adapted, topology-preserving latent representations with exact decoding for high-resolution structured visual data.

---


### 368. [Detecting overfitting in Neural Networks during long-horizon grokking using Random Matrix Theory](https://arxiv.org/abs/2605.12394)

**<font color=#1a73e8>作者：</font>** Hari K. Prakash, Charles H Martin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training Neural Networks (NNs) without overfitting is difficult; detecting that overfitting is difficult as well. We present a novel Random Matrix Theory method that detects the onset of overfitting in deep learning models without access to train or test data. For each model layer, we randomize each weight matrix element-wise, $\mathbf{W} \to \mathbf{W}_{\mathrm{rand}}$, fit the randomized empirical spectral distribution with a Marchenko-Pastur distribution, and identify large outliers that violate self-averaging. We call these outliers Correlation Traps. During the onset of overfitting, which we call the "anti-grokking" phase in long-horizon grokking, Correlation Traps form and grow in number and scale as test accuracy decreases while train accuracy remains high. Traps may be benign or may harm generalization; we provide an empirical approach to distinguish between them by passing random data through the trained model and evaluating the JS divergence of output logits. Our findings show that anti-grokking is an additional grokking phase with high train accuracy and decreasing test accuracy, structurally distinct from pre-grokking through its Correlation Traps. More broadly, we find that some foundation-scale LLMs exhibit the same Correlation Traps, indicating potentially harmful overfitting.

---


### 369. [A Comparative Study of Controlled Text Generation Systems Using Level-Playing-Field Evaluation Principles](https://arxiv.org/abs/2605.12395)

**<font color=#1a73e8>作者：</font>** Michela Lorandi, Anya Belz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: Many different approaches to controlled text generation (CTG) have been proposed over recent years, but it is difficult to get a clear picture of which approach performs best, because different datasets and evaluation methods are used in each case to assess the control achieved.
Objectives: Our aim in the work reported in this paper is to develop an approach to evaluation that enables us to comparatively evaluate different CTG systems in a manner that is both informative and fair to the individual systems.
Methods: We use a level-playing-field (LPF) approach to comparative evaluation where we (i) generate and process all system outputs in a standardised way, and (ii) apply a shared set of evaluation methods and datasets, selected based on those currently in use, in order to ensure fair evaluation.
Results: When re-evaluated in this way, performance results for a representative set of current CTG systems differ substantially from originally reported results, in most cases for the worse. This highlights the importance of a shared standardised way of assessing controlled generation.
Conclusions: The discrepancies revealed by LPF evaluation demonstrate the urgent need for standardised, reproducible evaluation practices in CTG. Our results suggest that without such practices, published performance claims may substantially misrepresent true system capabilities.

---


### 370. [GeoQuery: Geometry-Query Diffusion for Sparse-View Reconstruction](https://arxiv.org/abs/2605.12399)

**<font color=#1a73e8>作者：</font>** Xiao Cao, Yuze Li, Youmin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has emerged as a prominent paradigm for 3D reconstruction and novel view synthesis. However, it remains vulnerable to severe artifacts when trained under sparse-view constraints. While recent methods attempt to rectify artifacts in rendered views using image diffusion models, they typically rely on multi-view self-attention to retrieve information from reference images. We observe that this mechanism often fails when the rendered novel views output by 3DGS are heavily corrupted: damaged query features lead to erroneous cross-view retrieval, resulting in inconsistent rendering refinement. To address this, we propose GeoQuery, a geometry-guided diffusion framework that integrates generative priors with explicit geometric cues via a novel Geometry-guided Cross-view Attention (GCA) mechanism. First, by leveraging predicted depth maps and camera poses, we construct a geometry-induced correspondence field to sample reference features, forming a geometry-aligned proxy query that replaces the corrupted rendering features. Furthermore, we design a new cross-view feature aggregation pipeline, in which we restrict the cross-view attention to a local window around each proxy query to effectively retrieve useful features while suppressing spurious matches. GeoQuery can be seamlessly integrated into existing diffusion-based pipelines, enabling robust reconstruction even under extreme view sparsity. Extensive experiments on sparse-view novel view synthesis and rendering artifact removal demonstrate the effectiveness of our approach.

---


### 371. [Semantic Reward Collapse and the Preservation of Epistemic Integrity in Adaptive AI Systems](https://arxiv.org/abs/2605.12406)

**<font color=#1a73e8>作者：</font>** William Parris  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in reinforcement learning from human feedback (RLHF) and preference optimization have substantially improved the usability, coherence, and safety of large language models. However, recurring behaviors such as performative certainty, hallucinated continuity, calibration drift, sycophancy, and suppression of visible uncertainty suggest unresolved structural issues within scalarized preference optimization systems.
We propose Semantic Reward Collapse (SRC): the compression of semantically distinct forms of evaluative dissatisfaction into generalized optimization signals. Under SRC, categories such as factual incorrectness, uncertainty disclosure, formatting dissatisfaction, latency, and social preference may become entangled within a shared reward topology despite representing fundamentally different epistemic classes.
We argue that adaptive reasoning systems operating under generalized evaluative pressure may drift toward suppression of visible epistemic failure rather than preservation of calibrated uncertainty integrity. These behaviors are framed strictly as optimization consequences rather than evidence of deception or anthropomorphic agency.
Drawing on institutional proxy collapse, metric gaming, software reliability engineering, and human learning theory, we propose that uncertainty disclosure and escalation behavior should be treated as protected epistemic conduct rather than globally penalized task incompletion.
Finally, we introduce Constitutional Reward Stratification (CRS), a domain-aware reward framework intended to preserve differentiated epistemic attribution within adaptive learning systems. We present CRS not as a validated solution, but as a testable governance-oriented research direction requiring further empirical investigation.

---


### 372. [Predicting Decisions of AI Agents from Limited Interaction through Text-Tabular Modeling](https://arxiv.org/abs/2605.12411)

**<font color=#1a73e8>作者：</font>** Eilam Shapira, Moshe Tennenholtz, Roi Reichart  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI agents negotiate and transact in natural language with unfamiliar counterparts: a buyer bot facing an unknown seller, or a procurement assistant negotiating with a supplier. In such interactions, the counterpart's LLM, prompts, control logic, and rule-based fallbacks are hidden, while each decision can have monetary consequences. We ask whether an agent can predict an unfamiliar counterpart's next decision from a few interactions. To avoid real-world logging confounds, we study this problem in controlled bargaining and negotiation games, formulating it as target-adaptive text-tabular prediction: each decision point is a table row combining structured game state, offer history, and dialogue, while $K$ previous games of the same target agent, i.e., the counterpart being modeled, are provided in the prompt as labeled adaptation examples. Our model is built on a tabular foundation model that represents rows using game-state features and LLM-based text representations, and adds LLM-as-Observer as an additional representation: a small frozen LLM reads the decision-time state and dialogue; its answer is discarded, and its hidden state becomes a decision-oriented feature, making the LLM an encoder rather than a direct few-shot predictor. Training on 13 frontier-LLM agents and testing on 91 held-out scaffolded agents, the full model outperforms direct LLM-as-Predictor prompting and game+text features baselines. Within this tabular model, Observer features contribute beyond the other feature schemes: at $K=16$, they improve response-prediction AUC by about 4 points across both tasks and reduce bargaining offer-prediction error by 14%. These results show that formulating counterpart prediction as a target-adaptive text-tabular task enables effective adaptation, and that hidden LLM representations expose decision-relevant signals that direct prompting does not surface.

---


### 373. [Aligning Flow Map Policies with Optimal Q-Guidance](https://arxiv.org/abs/2605.12416)

**<font color=#1a73e8>作者：</font>** Christos Ziakas, Alessandra Russo, Avishek Joey Bose  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative policies based on expressive model classes, such as diffusion and flow matching, are well-suited to complex control problems with highly multimodal action distributions. Their expressivity, however, comes at a significant inference cost: generating each action typically requires simulating many steps of the generative process, compounding latency across sequential decision-making rollouts. We introduce flow map policies, a novel class of generative policies designed for fast action generation by learning to take arbitrary-size jumps including one-step jumps-across the generative dynamics of existing flow-based policies. We instantiate flow map policies for offline-to-online reinforcement learning (RL) and formulate online adaptation as a trust-region optimization problem that improves the critic's Q-value while remaining close to the offline policy. We theoretically derive FLOW MAP Q-GUIDANCE (FMQ), a principled closed-form learning target that is optimal for adapting offline flow map policies under a critic-guided trust-region constraint. We further introduce Q-GUIDED BEAM SEARCH (QGBS), a stochastic flow-map sampler that combines renoising with beam search to enable iterative inference-time refinement. Across 12 challenging robotic manipulation and locomotion tasks from OGBench and RoboMimic, FMQ achieves state-of-the-art performance in offline-to-online RL, outperforming the previous one-step policy MVP by a relative improvement of 21.3% on the average success rate.

---


### 374. [Geometric Factual Recall in Transformers](https://arxiv.org/abs/2605.12426)

**<font color=#1a73e8>作者：</font>** Shauli Ravfogel, Gilad Yehudai, Joan Bruna 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How do transformer language models memorize factual associations? A common view casts internal weight matrices as associative memories over pairs of embeddings, requiring parameter counts that scale linearly with the number of facts. We develop a theoretical and empirical account of an alternative, \emph{geometric} form of memorization in which learned embeddings encode relational structure directly, and the MLP plays a qualitatively different role. In a controlled setting where a single-layer transformer must memorize random bijections from subjects to a shared attribute set, we prove that a logarithmic embedding dimension suffices: subject embeddings encode \emph{linear superpositions} of their associated attribute vectors, and a small MLP acts as a relation-conditioned selector that extracts the relevant attribute via ReLU gating, and not as an associative key-value mapping. We extend these results to the multi-hop setting -- chains of relational queries such as ``Who is the mother of the wife of $x$?'' -- providing constructions with and without chain-of-thought that exhibit a provable capacity-depth tradeoff, complemented by a matching information-theoretic lower bound. Empirically, gradient descent discovers solutions with precisely the predicted structure. Once trained, the MLP transfers zero-shot to entirely new bijections when subject embeddings are appropriately re-initialized, revealing that it has learned a generic selection mechanism rather than memorized any particular set of facts.

---


### 375. [Learning Minimally Rigid Graphs with High Realization Counts](https://arxiv.org/abs/2605.12427)

**<font color=#1a73e8>作者：</font>** Oleksandr Slyvka, Jan Rubeš, Rodrigo Alves 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For minimally rigid graphs, the same edge-length data can admit multiple realizations (up to translations and rotations). Finding graphs with exceptionally many realizations is an extremal problem in rigidity theory, but exhaustive search quickly becomes infeasible due to the super-exponential growth of the number of candidate graphs and the high cost of realization-count evaluation. We propose a reinforcement-learning approach that constructs minimally rigid graphs via 0- and 1-extensions, also known as Henneberg moves. We optimize realization-count invariants using the Deep Cross-Entropy Method with a policy parameterized by a Graph Isomorphism Network encoder and a permutation-equivariant extension-level action head. Empirically, our method matches the known optima for planar realization counts and improves the best known bounds for spherical realization counts, yielding new record graphs.

---


### 376. [AOI-SSL: Self-Supervised Framework for Efficient Segmentation of Wire-bonded Semiconductors In Optical Inspection](https://arxiv.org/abs/2605.12430)

**<font color=#1a73e8>作者：</font>** Joaquín Figueira, Rob Van Gastel, Giacomo D'Amicantonio 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmentation models in automated optical inspection of wire-bonded semiconductors are typically device-specific and must be re-trained when new devices or distribution shifts appear. We introduce AOI-SSL, a training-efficient framework for semantic segmentation of wire-bonded semiconductors by combining small-domain self-supervised pre-training of vision transformers with in-context inference that minimizes the need of labeled examples. We pre-train SOTA self-supervised algorithms in a small industrial inspection dataset and find that Masked Autoencoders are the most effective in this small-data setting, improving downstream segmentation while reducing the labeled fine-tuning effort. We further introduce in-context, patch-level retrieval methods that predict masks directly from dense encoder embeddings with negligible additional training. We show that, in this setting, simple similarity-based retrieval performs on par with more complex attention-based aggregation used currently in the literature. Furthermore, our experiments demonstrate that self-supervised pre-training significantly improves segmentation quality compared to training from scratch and to ImageNet pre-trained backbones under a fixed fine-tuning computational budget. Finally, the results reveal that retrieval based segmentation outperforms fine-tuning when targeting single device images, allowing for near-instant adaptation to difficult samples.

---


### 377. [GaitProtector: Impersonation-Driven Gait De-Identification via Training-Free Diffusion Latent Optimization](https://arxiv.org/abs/2605.12431)

**<font color=#1a73e8>作者：</font>** Huiran Duan, Qian Zhou, Zhongliang Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional gait de-identification methods often encounter an inherent trade-off: they either provide insufficient identity suppression or introduce spatiotemporal distortions that impede structure-sensitive downstream applications. We propose GaitProtector, an impersonation-driven gait de-identification framework that formulates privacy protection as a unified objective with two tightly coupled components: (i) obfuscation, which repels the protected gait from the source identity, and (ii) impersonation, which attracts it toward a selected target identity. The target identity serves as a semantic anchor that biases optimization toward structurally plausible gait patterns under the pretrained diffusion prior, helping preserve dominant body shape and motion dynamics. We instantiate this idea through a training-free diffusion latent optimization pipeline. Instead of retraining a generator for each dataset, we invert each input silhouette sequence into the latent trajectory of a pretrained 3D video diffusion model and iteratively optimize latent codes with a differentiable adversarial objective to synthesize protected gaits. Experiments on the CASIA-B dataset show that GaitProtector achieves a 56.7% impersonation success rate under black-box gait recognition and reduces Rank-1 identification accuracy from 89.6% to 15.0%, while maintaining favorable visual and temporal quality. We further evaluate downstream utility on the Scoliosis1K dataset, where diagnostic accuracy decreases only from 91.4% to 74.2%. To the best of our knowledge, this work is the first to leverage pretrained 3D diffusion priors in a training-free manner for silhouette-based gait de-identification.

---


### 378. [Environment-Adaptive Preference Optimization for Wildfire Prediction](https://arxiv.org/abs/2605.12435)

**<font color=#1a73e8>作者：</font>** Enyi Jiang, Wu Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting rare extreme events such as wildfires from meteorological data requires models that remain reliable under evolving environmental conditions. This problem is inherently long-tailed: wildfire events are rare but high-impact, while most observations correspond to non-fire conditions, causing standard learning objectives to underemphasize the minority class (fire) that matters most. In addition, models trained on historical distributions often fail under distribution shifts, exhibiting degraded performance in new environments. To this end, we propose Environment-Adaptive Preference Optimization (EAPO), a framework that adapts prediction to the target environment with long-tail distribution. Given a new input distribution, we first construct distribution-aligned datasets via $k$-nearest neighbor retrieval. We then perform a hybrid fine-tuning procedure on this local manifold, combining supervised learning with preference optimization, as well as emphasizing on rare extreme events. EAPO refines decision boundaries while avoiding conflicting signals from heterogeneous training data. We evaluate EAPO on a real-world wildfire prediction task with environmental shifts. EAPO achieves robust performance (ROC-AUC 0.7310) and improves detection in extreme regimes, demonstrating its effectiveness in dynamic wildfire prediction systems.

---


### 379. [CAAFC: Chronological Actionable Automated Fact-Checker for misinformation / non-factual hallucination detection and correction](https://arxiv.org/abs/2605.12436)

**<font color=#1a73e8>作者：</font>** Islam Eldifrawi, Shengrui Wang, Amine Trabelsi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the vast amount of content uploaded every hour, along with the AI generated content that can include hallucinations, Automated Fact-Checking (AFC) has become increasingly vital, as it is infeasible for human fact-checkers to manually verify the sheer volume of information generated online. Professional fact-checkers have identified several gaps in existing AFC systems, noting a misalignment between how these systems operate and how fact-checking is performed in practice. In this paper, we introduce CAAFC (Chronological Actionable Automated Fact-Checker), a frame-work designed to bridge these gaps. It surpasses SOTA AFC and hallucination detection systems across multiple benchmark datasets. CAAFC operates on claims, conversations, and dialogues, enabling it not only to detect factual errors and hallucinations, but also to correct them by providing actionable justifications supported by primary information sources. Furthermore, CAAFC can update evidence and knowledge bases by incorporating recent and contextual information when necessary, thereby enhancing the reliability of fact verification.

---


### 380. [3D Gaussian Splatting for Efficient Retrospective Dynamic Scene Novel View Synthesis with a Standardized Benchmark](https://arxiv.org/abs/2605.12437)

**<font color=#1a73e8>作者：</font>** Yunxiao Zhang, Suryansh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrospective novel view synthesis (NVS) of dynamic scenes is fundamental to applications such as sports. Recent dynamic 3D Gaussian Splatting (3DGS) approaches introduce temporally coupled formulations to enforce motion coherence across time. In this paper, we argue that, in a synchronized multi-view (MV) setting typical of sports, the dynamic scene at each time step is already strongly geometrically constrained. We posit that the availability of calibrated, synchronized viewpoints provides sufficient spatial consistency, and therefore, explicit temporal coupling, or complex multi-body constraints seems unnecessary for retrospective NVS. To this end, we propose an approach tailored for synchronized MV dynamic scene. By initializing the SfM-derived point cloud at the start time and propagating optimized Gaussians over time, we show that efficient retrospective NVS can be achieved without imposing a temporal deformation constraint. Complementing our methodological contribution, we introduce a Dynamic MV dataset framework built on Blender for reproducible NeRF and 3DGS research. The framework generates high-quality, synchronized camera rigs and exports training-ready datasets in standard formats, eliminating inconsistencies in coordinate conventions and data pipelines. Using the framework, we construct a dynamic benchmark suite and evaluate representative NeRF and 3DGS approaches under controlled conditions. Together, we show that, under a synchronized MV setup, efficient retrospective dynamic scene NVS can be achieved using 3DGS. At the same time, the dataset-generation framework enables reproducible and principled benchmarking of dynamic NVS methods.

---


### 381. [LychSim: A Controllable and Interactive Simulation Framework for Vision Research](https://arxiv.org/abs/2605.12449)

**<font color=#1a73e8>作者：</font>** Wufei Ma, Chloe Wang, Siyi Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While self-supervised pretraining has reduced vision systems' reliance on synthetic data, simulation remains an indispensable tool for closed-loop optimization and rigorous out-of-distribution (OOD) evaluation. However, modern simulation platforms often present steep technical barriers, requiring extensive expertise in computer graphics and game development. In this work, we present LychSim, a highly controllable and interactive simulation framework built upon Unreal Engine 5 to bridge this gap. LychSim is built around three key designs: (1) a streamlined Python API that abstracts away underlying engine complexities; (2) a procedural data pipeline capable of generating diverse, high-fidelity environments with varying out-of-distribution (OOD) visual challenges, paired with rich 2D and 3D ground truths; and (3) a native integration of the Model Context Protocol (MCP) that transforms the simulator into a dynamic, closed-loop playground for reasoning agentic LLMs. We further annotate scene-level procedural rules and object-level pose alignments to enable semantically aligned 3D ground truths and automated scene modification. We demonstrate LychSim's capability across multiple downstream applications, including serving as a synthetic data engine, powering reinforcement learning-based adversarial examiners, and facilitating interactive, language-driven scene layout generation. To benefit the broader vision community, LychSim will be made publicly available, including full source code and various data annotations.

---


### 382. [FuTCR: Future-Targeted Contrast and Repulsion for Continual Panoptic Segmentation](https://arxiv.org/abs/2605.12451)

**<font color=#1a73e8>作者：</font>** Nicholas Ikechukwu, Keanu Nichols, Deepti Ghadiyaram 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual Panoptic Segmentation (CPS) requires methods that can quickly adapt to new categories over time. The nature of this dense prediction task means that training images may contain a mix of labeled and unlabeled objects. As nothing is known about these unlabeled objects a priori, existing methods often simply group any unlabeled pixel into a single "background" class during training. In effect, during training, they repeatedly tell the model that all the different background categories are the same (even when they aren't). This makes learning to identify different background categories as they are added challenging since these new categories may require using information the model was previously told was unimportant and ignored. Thus, we propose a Future-Targeted Contrastive and Repulsive (FuTCR) framework that addresses this limitation by restructuring representations before new classes are introduced. FuTCR first discovers confident future-like regions by grouping model-predicted masks whose pixels are consistently classified as background but exhibit non-background logits. Next, FuTCR applies pixel-to-region contrast to build coherent prototypes from these unlabeled regions, while simultaneously repelling background features away from known-class prototypes to explicitly reserve representational space for future categories. Experiments across six CPS settings and a range of dataset sizes show FuTCR improves relative new-class panoptic quality over the state-of-the-art by up to 28%, while preserving or improving base-class performance with gains up to 4%.

---


### 383. [Towards Affordable Energy: A Gymnasium Environment for Electric Utility Demand-Response Programs](https://arxiv.org/abs/2605.12462)

**<font color=#1a73e8>作者：</font>** Jose E. Aguilar Escamilla, Lingdong Zhou, Xiangqi Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extreme weather and volatile wholesale electricity markets expose residential consumers to catastrophic financial risks, yet demand response at the distribution level remains an underutilized tool for grid flexibility and energy affordability. While a demand-response program can shield consumers by issuing financial credits during high-price periods, optimizing this sequential decision-making process presents a unique challenge for reinforcement learning despite the plentiful offline historical smart meter and wholesale pricing data available publicly. Offline historical data fails to capture the dynamic, interactive feedback loop between an electric utility's pricing signals and customer acceptance and adaptation to a demand-response program. To address this, we introduce DR-Gym, an open-source, online Gymnasium-compatible environment designed to train and evaluate demand-response from the electric utility's perspective. Unlike existing device-level energy simulators, our environment focuses on the market-level electric utility setting and provides a rich observational space relevant to the electric utility. The simulator additionally features a regime-switching wholesale price model calibrated to real-world extreme events, alongside physics-based building demand profiles. For our learning signal, we use a configurable, multi-objective reward function for specifying diverse learning objectives. We demonstrate through baseline strategies and data snapshots the capability of our simulator to create realistic and learnable environments.

---


### 384. [High-arity Sample Compression](https://arxiv.org/abs/2605.12465)

**<font color=#1a73e8>作者：</font>** Leonardo N. Coregliano, William Opich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, a series of works have started studying variations of concepts from learning theory for product spaces, which can be collected under the name high-arity learning theory. In this work, we consider a high-arity variant of sample compression schemes and we prove that the existence of a high-arity sample compression scheme of non-trivial quality implies high-arity PAC learnability.

---


### 385. [Solve the Loop: Attractor Models for Language and Reasoning](https://arxiv.org/abs/2605.12466)

**<font color=#1a73e8>作者：</font>** Jacob Fein-Ashley, Paria Rashidinejad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers offer a promising alternative to purely feed-forward computation by iteratively refining latent representations, improving language modeling and reasoning. Yet recurrent architectures remain unstable to train, costly to optimize and deploy, and constrained to small, fixed recurrence depths. We introduce Attractor Models, in which a backbone module first proposes output embeddings, then an attractor module refines them by solving for the fixed point, with gradients obtained through implicit differentiation. Thus, training memory remains constant in effective depth, and iterations are chosen adaptively by convergence. Empirically, Attractor Models outperform existing models across two regimes, large-scale language-model pretraining and reasoning with tiny models. In language modeling, Attractor Models deliver a Pareto improvement over standard Transformers and stable looped models across sizes, improving perplexity by up to 46.6% and downstream accuracy by up to 19.7% while reducing training cost. Notably, a 770M Attractor Model outperforms a 1.3B Transformer trained on twice as many tokens. On challenging reasoning tasks, we show that our model with only 27M parameters and approximately 1000 examples achieves 91.4% accuracy on Sudoku-Extreme and 93.1% on Maze-Hard, scaling favorably where frontier models like Claude and GPT o3, fail completely, and specialized recursive reasoners collapse at larger sizes. Lastly, we show that Attractor Models exhibit a novel phenomenon, which we call equilibrium internalization: fixed-point training places the model's initial output embedding near equilibrium, allowing the solver to be removed at inference time with little degradation. Together, these results suggest that Attractor Models make iterative refinement scalable by turning recurrence into a computation the model can learn to internalize.

---


### 386. [KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference](https://arxiv.org/abs/2605.12471)

**<font color=#1a73e8>作者：</font>** Alireza Nadali, Patrick Cooper, Ashutosh Trivedi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce KV-Fold, a simple, training-free long-context inference protocol that treats the key-value (KV) cache as the accumulator in a left fold over sequence chunks. At each step, the model processes the next chunk conditioned on the accumulated cache, appends the newly produced keys and values, and passes the enlarged cache forward; the same one-step update is applied repeatedly, analogous to foldl in functional programming. Building on the KV cache concatenation primitive introduced for latent multi-agent communication, we repurpose it as a chunk-to-chunk recurrence for long-context inference. When processing chunk t, the model attends to the KV cache carried from earlier chunks as a prefix, reusing its internal state across segments without modifying or retraining the model. Despite its simplicity, the induced recurrence is stable: per-step drift rises briefly and then saturates into a flat plateau that persists across deep chains. This plateau is insensitive to a 10,000x change in numerical precision, robust across chunk sizes, and consistent across model families. At the task level, KV-Fold preserves exact information over long distances. On a needle-in-a-haystack benchmark, it achieves 100% exact-match retrieval across 152 trials spanning contexts from 16K to 128K tokens and chain depths up to 511 on Llama-3.1-8B, while remaining within the memory limits of a single 40GB GPU. Compared to streaming methods, which trade fidelity for bounded memory, KV-Fold maintains long-range retrieval while operating as a sequence of tractable forward passes. Overall, our results show that frozen pretrained transformers already support a stable form of KV-cache recurrence, providing a practical route to long-context inference without architectural changes or training.

---


### 387. [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474)

**<font color=#1a73e8>作者：</font>** Anas Mahmoud, MohammadHossein Rezaei, Zihao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards has enabled strong post-training gains in domains such as math and coding, though many open-ended settings rely on rubric-based rewards. We study reward hacking in rubric-based RL, where a policy is optimized against a training verifier but evaluated against a cross-family panel of three frontier judges, reducing dependence on any single evaluator. Our framework separates two sources of divergence: verifier failure, where the training verifier credits rubric criteria that reference verifiers reject, and rubric-design limitations, where even strong rubric-based verifiers favor responses that rubric-free judges rate worse overall. Across medical and science domains, weak verifiers produce large proxy-reward gains that do not transfer to the reference verifiers; exploitation grows over training and concentrates in recurring failures such as partial satisfaction of compound criteria, treating implicit content as explicit, and imprecise topical matching. Stronger verifiers substantially reduce, but do not eliminate, verifier exploitation. We also introduce a self-internalization gap, a verifier-free diagnostic based on policy log-probabilities, which tracks reference-verifier quality, detecting when the policy trained using the weak verifier stops improving. Finally, in our setting, stronger verification does not prevent reward hacking when the rubric leaves important failure modes unspecified: rubric-based verifiers prefer the RL checkpoint, while rubric-free judges prefer the base model. These disagreements coincide with gains concentrated in completeness and presence-based criteria, alongside declines in factual correctness, conciseness, relevance, and overall quality. Together, these results suggest that stronger verification reduces reward hacking, but does not by itself ensure that rubric gains correspond to broader quality gains.

---


### 388. [Routers Learn the Geometry of Their Experts: Geometric Coupling in Sparse Mixture-of-Experts](https://arxiv.org/abs/2605.12476)

**<font color=#1a73e8>作者：</font>** Sagi Ahrac, Noya Hochwald, Mor Geva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (SMoE) models enable scaling language models efficiently, but training them remains challenging, as routing can collapse onto few experts and auxiliary load-balancing losses can reduce specialization. Motivated by these hurdles, we study how routing decisions in SMoEs are formed mechanistically. First, we reveal a geometric coupling between routers and their corresponding experts. For a given token, the router weights for the selected expert and the expert weights processing it receive gradients along the same input direction, differing only in scalar coefficients. Thus, matched router--expert directions accumulate the same routed token history. This theoretical coupling also appears empirically in routing dynamics. In a $1$B SMoE trained from scratch, higher router scores predict stronger expert neuron activations, showing that routing decisions are mirrored inside the selected expert. Next, we analyze the effects of auxiliary load balancing on the router--expert geometric coupling, showing that such losses break this structure by spreading input-directed gradients across router weights, making distinct router directions nearly three times more similar to each other. Last, we demonstrate the centrality of geometric coupling for effective routing with a parameter-free online K-Means router, in which each expert maintains a running average of the hidden states routed to it and tokens are assigned based on cosine similarity. Compared with auxiliary-loss and loss-free balancing, this router achieves the lowest load imbalance with only a modest perplexity increase, indicating that geometric coupling captures a substantial part of what the router learns. Overall, our results explain how routers form assignment geometry that supports an effective division of labor.

---


### 389. [MEME: Multi-entity & Evolving Memory Evaluation](https://arxiv.org/abs/2605.12477)

**<font color=#1a73e8>作者：</font>** Seokwon Jung, Alexander Rubinstein, Arnas Uselis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based agents increasingly operate in persistent environments where they must store, update, and reason over information across many sessions. While prior benchmarks evaluate only single-entity updates, MEME defines six tasks spanning the full space defined by the multi-entity and evolving axes, including three not scored by prior work: Cascade and Absence (dependency reasoning) and Deletion (post-removal state). Evaluating six memory systems spanning three memory paradigms on 100 controlled episodes, we find that all systems collapse on dependency reasoning under the default configuration (Cascade: 3%, Absence: 1% in average accuracy) despite adequate static retrieval performance. Prompt optimization, deeper retrieval, reduced filler noise, and most stronger LLMs fail to close this gap. Only a file-based agent paired with Claude Opus 4.7 as its internal LLM partially closes the gap, but at ~70x the baseline cost, indicating closure currently depends on configurations that are not practical at scale. Code and data are available on the project page: this https URL.

---


### 390. [OmniNFT: Modality-wise Omni Diffusion Reinforcement for Joint Audio-Video Generation](https://arxiv.org/abs/2605.12480)

**<font color=#1a73e8>作者：</font>** Guohui Zhang, XiaoXiao Ma, Jie Huang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in joint audio-video generation have been remarkable, yet real-world applications demand strong per-modality fidelity, cross-modal alignment, and fine-grained synchronization. Reinforcement Learning (RL) offers a promising paradigm, but its extension to multi-objective and multi-modal joint audio-video generation remains unexplored. Notably, our in-depth analysis first reveals that the primary obstacles to applying RL in this stem from: (i) multi-objective advantages inconsistency, where the advantages of multimodal outputs are not always consistent within a group; (ii) multi-modal gradients imbalance, where video-branch gradients leak into shallow audio layers responsible for intra-modal generation; (iii) uniform credit assignment, where fine-grained cross-modal alignment regions fail to get efficient exploration. These shortcomings suggest that vanilla RL fine-tuning strategy with a single global advantage often leads to suboptimal results. To address these challenges, we propose OmniNFT, a novel modality-aware online diffusion RL framework with three key innovations: (1) Modality-wise advantage routing, which routes independent per-reward advantages to their respective modality generation branches. (2) Layer-wise gradient surgery, which selectively detaches video-branch gradients on shallow audio layers while retaining those for cross-modal interaction layers. (3) Region-wise loss reweighting, which modulates policy optimization toward critical regions related to audio-video synchronization and fine-grained alignment. Extensive experiments on JavisBench and VBench with the LTX-2 backbone demonstrate that OmniNFT achieves comprehensive improvements in audio and video perceptual quality, cross-modal alignment, and audio-video synchronization.

---


### 391. [Elastic Attention Cores for Scalable Vision Transformers](https://arxiv.org/abs/2605.12491)

**<font color=#1a73e8>作者：</font>** Alan Z. Song, Yinjie Chen, Mu Nan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) achieve strong data-driven scaling by leveraging all-to-all self-attention. However, this flexibility incurs a computational cost that scales quadratically with image resolution, limiting ViTs in high-resolution domains. Underlying this approach is the assumption that pairwise token interactions are necessary for learning rich visual-semantic representations. In this work, we challenge this assumption, demonstrating that effective visual representations can be learned without any direct patch-to-patch interaction. We propose VECA (Visual Elastic Core Attention), a vision transformer architecture that uses efficient linear-time core-periphery structured attention enabled by a small set of learned cores. In VECA, these cores act as a communication interface: patch tokens exchange information exclusively through the core tokens, which are initialized from scratch and propagated across layers. Because the $N$ image patches only directly interact with a resolution invariant set of $C$ learned "core" embeddings, this yields linear complexity $O(N)$ for predetermined $C$, which bypasses quadratic scaling. Compared to prior cross-attention architectures, VECA maintains and iteratively updates the full set of $N$ input tokens, avoiding a small $C$-way bottleneck. Combined with nested training along the core axis, our model can elastically trade off compute and accuracy during inference. Across classification and dense tasks, VECA achieves performance competitive with the latest vision foundation models while reducing computational cost. Our results establish elastic core-periphery attention as a scalable alternative building block for Vision Transformers.

---


### 392. [Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation](https://arxiv.org/abs/2605.12492)

**<font color=#1a73e8>作者：</font>** Kexuan Shi, Hanxuan Li, Zeju Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Pion, a spectrum-preserving optimizer for large language model (LLM) training based on orthogonal equivalence transformation. Unlike additive optimizers such as Adam and Muon, Pion updates each weight matrix through left and right orthogonal transformations, preserving its singular values throughout training. This yields an optimization mechanism that modulates the geometry of weight matrices while keeping their spectral norm fixed. We derive the Pion update rule, systematically examine its design choices, and analyze its convergence behavior along with several key properties. Empirical results show that Pion offers a stable and competitive alternative to standard optimizers for both LLM pretraining and finetuning.

---


### 393. [LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues](https://arxiv.org/abs/2605.12493)

**<font color=#1a73e8>作者：</font>** Di Wu, Zixiang Ji, Asmi Kawatkar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory is crucial for agents in specialized web environments, where success depends on recalling interface affordances, state dynamics, workflows, and recurring failure modes. However, existing memory benchmarks for agents mostly focus on user histories, short traces, or downstream task success, leaving open how to directly evaluate whether memory systems effectively internalize environment-specific experience. To address this gap, we introduce LongMemEval-V2 (LME-V2), a benchmark for evaluating whether memory systems can help agents acquire the experience needed to become knowledgeable colleagues in customized environments. LME-V2 contains 451 manually curated questions covering five core memory abilities for web agents: static state recall, dynamic state tracking, workflow knowledge, environment gotchas, and premise awareness. Questions are paired with history trajectories containing up to 500 trajectories and 115M tokens. We use a context gathering formulation: memory systems consume history trajectories and return compact evidence for downstream question answering. We propose a suite of two memory methods: AgentRunbook-R, an efficient RAG-based memory with knowledge pools for raw state observations, events, and strategy notes, and AgentRunbook-C, which stores trajectories as files and invokes a coding agent to gather evidence in an augmented sandbox. Experiments show that AgentRunbook-C achieves the best performance with 72.5% average accuracy, outperforming the strongest RAG baseline (48.5%) and the off-the-shelf coding agent baseline (69.3%). Despite the strong performance gains, coding agent based methods have high latency costs. While AgentRunbook-C advances the accuracy-latency Pareto frontier, substantial room for improvement remains. Together, these results establish LME-V2 as a challenging testbed for developing long-term memory systems for environment experience.

---


### 394. [Revisiting Photometric Ambiguity for Accurate Gaussian-Splatting Surface Reconstruction](https://arxiv.org/abs/2605.12494)

**<font color=#1a73e8>作者：</font>** Jiahe Li, Jiawei Zhang, Xiao Bai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surface reconstruction with differentiable rendering has achieved impressive performance in recent years, yet the pervasive photometric ambiguities have strictly bottlenecked existing approaches. This paper presents AmbiSuR, a framework that explores an intrinsic solution upon Gaussian Splatting for the photometric ambiguity-robust surface 3D reconstruction with high performance. Starting by revisiting the foundation, our investigation uncovers two built-in primitive-wise ambiguities in representation, while revealing an intrinsic potential for ambiguity self-indication in Gaussian Splatting. Stemming from these, a photometric disambiguation is first introduced, constraining ill-posed geometry solution for definite surface formation. Then, we propose an ambiguity indication module that unleashes the self-indication potential to identify and further guide correcting underconstrained reconstructions. Extensive experiments demonstrate our superior surface reconstructions compared to existing methods across various challenging scenarios, excelling in broad compatibility. Project: this https URL .

---


### 395. [CausalCine: Real-Time Autoregressive Generation for Multi-Shot Video Narratives](https://arxiv.org/abs/2605.12496)

**<font color=#1a73e8>作者：</font>** Yihao Meng, Zichen Liu, Hao Ouyang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video generation aims at real-time, open-ended synthesis. Yet, cinematic storytelling is not merely the endless extension of a single scene; it requires progressing through evolving events, viewpoint shifts, and discrete shot boundaries. Existing autoregressive models often struggle in this setting. Trained primarily for short-horizon continuation, they treat long sequences as extended single shots, inevitably suffering from motion stagnation and semantic drift during long rollouts. To bridge this gap, we introduce CausalCine, an interactive autoregressive framework that transforms multi-shot video generation into an online directing process. CausalCine generates causally across shot changes, accepts dynamic prompts on the fly, and reuses context without regenerating previous shots. To achieve this, we first train a causal base model on native multi-shot sequences to learn complex shot transitions prior to acceleration. We then propose Content-Aware Memory Routing (CAMR), which dynamically retrieves historical KV entries according to attention-based relevance scores rather than temporal proximity, preserving cross-shot coherence under bounded active memory. Finally, we distill the causal base model into a few-step generator for real-time interactive generation. Extensive experiments demonstrate that CausalCine significantly outperforms autoregressive baselines and approaches the capability of bidirectional models while unlocking the streaming interactivity of causal generation. Demo available at this https URL

---


### 396. [EgoForce: Forearm-Guided Camera-Space 3D Hand Pose from a Monocular Egocentric Camera](https://arxiv.org/abs/2605.12498)

**<font color=#1a73e8>作者：</font>** Christen Millerdurai, Shaoxiang Wang, Yaxu Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing the absolute 3D pose and shape of the hands from the user's viewpoint using a single head-mounted camera is crucial for practical egocentric interaction in AR/VR, telepresence, and hand-centric manipulation tasks, where sensing must remain compact and unobtrusive. While monocular RGB methods have made progress, they remain constrained by depth-scale ambiguity and struggle to generalize across the diverse optical configurations of head-mounted devices. As a result, models typically require extensive training on device-specific datasets, which are costly and laborious to acquire. This paper addresses these challenges by introducing EgoForce, a monocular 3D hand reconstruction framework that recovers robust, absolute 3D hand pose and its position from the user's (camera-space) viewpoint. EgoForce operates across fisheye, perspective, and distorted wide-FOV camera models using a single unified network. Our approach combines a differentiable forearm representation that stabilizes hand pose, a unified arm-hand transformer that predicts both hand and forearm geometry from a single egocentric view, mitigating depth-scale ambiguity, and a ray space closed-form solver that enables absolute 3D pose recovery across diverse head-mounted camera models. Experiments on three egocentric benchmarks show that EgoForce achieves state-of-the-art 3D accuracy, reducing camera-space MPJPE by up to 28% on the HOT3D dataset compared to prior methods and maintaining consistent performance across camera configurations. For more details, visit the project page at this https URL.

---


> [!TIP]
> 当前位于：**351-396**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-396**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
