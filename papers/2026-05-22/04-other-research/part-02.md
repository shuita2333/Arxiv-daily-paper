# 📦 其他研究 | 2026年05月22日

> 本类共 **352** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-352](./part-08.md)

---

### 51. [HAPS: Rethinking Image Similarity for Virtual Staining](https://arxiv.org/abs/2605.20362)

**<font color=#1a73e8>作者：</font>** Fedor Gubanov, Svetlana Illarionova, Vlad Kozlovskiy 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual staining of histopathology images (e.g., H&E-IHC) is an emerging tool in digital pathology, enabling faster and cheaper workflows by synthesizing target stains from routinely acquired slides. Yet, the quality of virtual staining models is still predominantly assessed with generic metrics such as SSIM, PSNR, and LPIPS. Originally developed for natural images, these metrics are inherently misaligned with the domain-specific characteristics of histological data, failing to capture tissue morphology preservation and biomarker expression patterns. Consequently, a robust, domain-specific standard for quantifying similarity across diverse histological modalities remains a critical gap in the field. In this work, we formalize histology image similarity as a standalone problem and systematically evaluate a broad set of full-reference metrics against a dataset of H&E-IHC patch pairs annotated with expert similarity scores. We further analyze metrics sensitivity to controlled geometric distortions (shifts, rotations and non-rigid deformations) that mimic realistic registration errors between serial sections. Guided by these observations, we propose the Histology-Aware Perceptual Similarity (HAPS) metric. HAPS computes distances in the feature space of a frozen encoder pretrained on histopathology data, adding a linear head to aggregate feature-level differences into a final score that aligns with expert assessments. Finally, we demonstrate the practical value of HAPS for quality control of training data. By quantifying the similarity of training pairs in the MIST dataset and filtering low-scoring samples, we create a cleaner training set. Virtual staining models trained on this refined data outperform those trained on the original, unfiltered dataset.

---


### 52. [When Reasoning Supervision Hurts: TTCW-Based Long-Form Literary Review Generation](https://arxiv.org/abs/2605.20364)

**<font color=#1a73e8>作者：</font>** Jinlong Liu, Mohammed Bahja, Mark Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic evaluation of long-form literary writing remains challenging, as generic LLM-as-Judge approaches may not fully capture creativity-related dimensions such as originality and flexibility. Although the Torrance Test of Creative Writing (TTCW) provides a structured creativity framework, and prior work has demonstrated reference-based TTCW evaluation at the pairwise level, no large-scale dataset exists for long-form TTCW-based literary review generation. We address this gap by constructing a dataset of 263,911 long-form stories, each annotated with scalar scores and meta-synthesised review comments across 14 TTCW-based dimensions. Using this dataset, we fine-tune Qwen3 models at two scales, 4B and 8B, under two conditions: with and without reasoning content. Results show that non-reasoning fine-tuning achieves stronger and more stable performance, with the best setting reaching an evaluation score of 0.6820. Further analysis shows that reasoning-supervised models are more prone to parse failures, often continuing with irrelevant or repetitive reasoning-style text rather than completing the required 14-metric review report. These results suggest that, for fixed-format rubric-based review generation, reasoning supervision is not straightforwardly beneficial, and precise metric-aligned scoring remains challenging even after task-specific fine-tuning.

---


### 53. [ConceptSeg-R1: Segment Any Concept via Meta-Reinforcement Learning](https://arxiv.org/abs/2605.20385)

**<font color=#1a73e8>作者：</font>** Yuan Zhao, Youwei Pang, Jiaming Zuo 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in promptable segmentation has shifted visual perception from object-level localization toward concept-level understanding. However, the notion of a concept remains under-specified, making it unclear whether current methods truly generalize beyond category recognition. In this work, we formalize generalized concept segmentation through a three-level taxonomy consisting of context-independent (CI), context-dependent (CD), and context-reasoning (CR) concepts, which reveals a clear capability gap across increasing levels of cognitive complexity. To address this challenge, we propose ConceptSeg-R1, a unified framework that reformulates concept segmentation as rule-induced concept grounding. At the core of our method is Meta-GRPO, a meta-reinforcement learning mechanism that learns transferable task rules from visual demonstrations and verifies them through proxy reasoning. The inferred reasoning states are then translated into segmentation-ready concept prompts via a lightweight concept translation module, enabling deductive application to target images. A shortcut routing strategy further preserves the native efficiency of segmentation models on simple cases. To systematically evaluate generalized concept segmentation, we conduct extensive experiments across diverse CI, CD, and CR concept segmentation benchmarks spanning natural, industrial, medical and reasoning-intensive domains. Without bells and whistles, ConceptSeg-R1 achieves strong performance across the full concept hierarchy while maintaining the native capability of promptable segmentation backbones. As an initial step toward segmenting any concept, we hope ConceptSeg-R1 can serve as a practical baseline for advancing segmentation from object-level prediction toward concept-level understanding.

---


### 54. [How You Move Tells What You'll Do: Trajectory-Conditioned Egocentric Prediction](https://arxiv.org/abs/2605.20388)

**<font color=#1a73e8>作者：</font>** Sejoon Jun, Hai Nguyen-Truong, Luigi Seminara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting how a person's first-person view will evolve (what action will follow, what plan completes a task, whether an in-progress shot will score) is fundamentally under-specified: the same context admits many plausible futures, and a model trained to minimize prediction error is forced to hedge or average across them, getting it wrong either way. Two findings shape our approach. First, the future camera trajectory, the path the head carves through space, lets the model commit to one of those futures: it carries the operator's intent in a form fine enough to determine how an action will unfold, substantially outperforming language as a conditioning signal. Second, this same intent makes the trajectory itself partially predictable from the context at hand, enough that trajectory need not be observed at test time to recover most of the gain. We instantiate these findings as TrajPilot, a model that predicts candidate future trajectories from egocentric context and uses them to pilot action prediction in an action-aligned embedding space where language shapes the structure but is never used as a conditioning input. TrajPilot beats VLM and structured-planner baselines on procedural planning across Ego-Exo4D atomic, Ego-Exo4D Keystep, Ego4D GoalStep, and EgoPER, with the trajectory advantage widening with horizon (exactly where prior planners collapse) and holding under RGB-only camera-pose estimation. With the goal masked at inference, the same model performs goal-free anticipation, beating VLM baselines on Ego-Exo4D atomic and extending to EPIC-Kitchens-100 and basketball shot-outcome prediction.

---


### 55. [Nonlocal operator learning for fMRI encoding and decoding tasks](https://arxiv.org/abs/2605.20389)

**<font color=#1a73e8>作者：</font>** Andreas Kramer, Saugat Acharya, Alice Giola 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Functional MRI data exhibit high-dimensional spatiotemporal structure, making both prediction and decoding challenging. In this work, we investigate neural integral-operator-based models for encoding and decoding tasks in fMRI, with particular emphasis on the role of nonlocal spatiotemporal context. We implement a latent neural integral operator framework that performs fixed point iterations in an auxiliary space from which classification and stimuli prediction is performed via a decoder. We evaluate our model on two open-source fMRI datasets.
Our experiments examine both decoding of stimuli from fMRI recordings and encoding of fMRI dynamics from stimulus representations. A main focus is the effect of spatiotemporal context: we systematically compare short and long temporal windows, as well as the use of visual cortex vs whole brain recordings, and analyze their influence on performance and latent-space geometry. Across tasks and datasets, larger temporal windows generally improve results and produce more structured learned representations. In decoding experiments, the learned latent space often provides clearer class separation than the raw data. In encoding experiments, although absolute performance remains moderate due to the difficulty of the task, longer temporal windows still yield consistent gains.
These findings suggest that neural integral operators provide a promising framework for modeling fMRI dynamics and that broader spatiotemporal context can be beneficial for both prediction and representation learning. More broadly, the results indicate that exploiting distributed nonlocal structure in brain dynamics requires model architectures specifically designed to capture such dependencies.

---


### 56. [STELLAR: Scaling 3D Perception Large Models for Autonomous Driving](https://arxiv.org/abs/2605.20390)

**<font color=#1a73e8>作者：</font>** Yingwei Li, Xin Huang, Yang Liu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Model scaling has demonstrated remarkable success through large-scale training on diverse datasets. It remains an open question whether the same paradigm would apply to autonomous driving perception systems due to unique challenges, such as fusing heterogeneous sensor data and the need for sophisticated 3D spatial understanding. To bridge this gap, we present a comprehensive study on systematically analyzing the impact of scale on these systems. We develop our STELLAR model based on Sparse Window Transformer, by extending the input modalities to include LiDAR, radar, camera, and map prior. We train the model on a large-scale dataset of 50 million driving examples with up to 500 million parameters. Our large-scale experiments reveal empirical scaling trends that connect model performance to model size, data, and compute. The resulting model establishes a new state-of-the-art on the Waymo Open Dataset challenge, outperforming prior arts by a large margin. Our work demonstrates that large-scale training is a highly promising path for advancing the capabilities of perception models for autonomous driving.

---


### 57. [Score-Based Causal Discovery of Latent Variable Causal Models](https://arxiv.org/abs/2605.20396)

**<font color=#1a73e8>作者：</font>** Ignavier Ng, Xinshuai Dong, Haoyue Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying latent variables and the causal structure involving them is essential across various scientific fields. While many existing works fall under the category of constraint-based methods (with e.g. conditional independence or rank deficiency tests), they may face empirical challenges such as testing-order dependency, error propagation, and choosing an appropriate significance level. These issues can potentially be mitigated by properly designed score-based methods, such as Greedy Equivalence Search (GES) (Chickering, 2002) in the specific setting without latent variables. Yet, formulating score-based methods with latent variables is highly challenging. In this work, we develop score-based methods that are capable of identifying causal structures containing causally-related latent variables with identifiability guarantees. Specifically, we show that a properly formulated scoring function can achieve score equivalence and consistency for structure learning of latent variable causal models. We further provide a characterization of the degrees of freedom for the marginal over the observed variables under multiple structural assumptions considered in the literature, and accordingly develop both exact and continuous score-based methods. This offers a unified view of several existing constraint-based methods with different structural assumptions. Experimental results validate the effectiveness of the proposed methods.

---


### 58. [Supervised Latent Restructuring for Small-Data Quantum Learning in Plant Phenomics](https://arxiv.org/abs/2605.20413)

**<font color=#1a73e8>作者：</font>** Alakananda Mitra, David H. Fleisher, Vangimalla Reddy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional biological data often exhibit a severe mismatch between feature dimensionality and sample size, making reliable classification difficult in extremely small-data regimes. In these settings, kernel methods can lose discriminative power when latent compression fails to preserve class-separating structure. We study this problem in fine-grained plant phenomics and propose a hybrid workflow that compresses 1280-dimensional deep image embeddings into a 64-dimensional PCA space and then restructures them into an 11-dimensional supervised latent space using Linear Discriminant Analysis (LDA), followed by GPU-accelerated Quantum Kernel Alignment (QKA) on NVIDIA L40S hardware. Empirically, supervised latent restructuring substantially improves the geometric separability of the compressed representation, increasing the Silhouette coefficient from 0.003 in the raw embedding space and -0.006 in PCA-64 to 0.197 in the supervised LDA-11 space. However, downstream classical evaluation reveals a clear compression trade-off: Linear SVM and XGBoost improve in the restructured latent space, whereas RBF-SVM and Random Forest degrade under the same 11-dimensional bottleneck. Under a constrained optimization budget, QKA in this regime remains challenging, indicating that latent geometry alone is not sufficient for strong trainable quantum performance. These findings position representation geometry as a central design variable in small-data quantum learning and expose the practical difficulty of recovering nonlinear discriminative structure from aggressively compressed biological representations.

---


### 59. [OSCToM: RL-Guided Adversarial Generation for High-Order Theory of Mind](https://arxiv.org/abs/2605.20423)

**<font color=#1a73e8>作者：</font>** Sharmin Sultana Srishty, Kazi Mahathir Rahman, Malaika Parizat Sakkhi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) perform well on many language tasks, but their Theory of Mind (ToM) reasoning is still uneven in complex social settings. Existing benchmarks, including ExploreToM, do not always test the recursive beliefs and information asymmetries that make these settings difficult. This paper presents OSCToM (Observer-Self Conflict Theory of Mind), an approach for modeling nested belief conflicts in LLM-based ToM tasks. The key case is one in which an observer's view of another agent conflicts with the observer's own belief state. Such cases go beyond simple perspective-taking and require recursive, multi-layered reasoning. OSCToM combines reinforcement learning (RL), an extended domain-specific language, and compositional surrogate models to generate observer-self conflicts. In our experiments, OSCToM-8B gives the best overall result among the systems tested. It improves on the reported ExploreToM results on FANToM and remains competitive on Hi-ToM and BigToM. On the information-asymmetric FANToM benchmark, OSCToM reaches 76% accuracy, compared with the 0.2% reported by ExploreToM. The data-synthesis procedure is also 6x more efficient, indicating that targeted training data can help smaller models handle advanced cognitive reasoning. The project code is available at this https URL.

---


### 60. [AgentCo-op: Retrieval-Based Synthesis of Interoperable Multi-Agent Workflows](https://arxiv.org/abs/2605.20425)

**<font color=#1a73e8>作者：</font>** Shuaike Shen, Wenduo Cheng, Shike Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing multi-agent workflows is especially difficult in open-ended scientific settings where tasks lack curated training sets, reliable scalar evaluation metrics, and standardized interfaces between existing tools and agents. We propose AgentCo-op, a retrieval-based synthesis framework that composes reusable skills, tools, and external agents into executable workflows through typed artifact handoffs, then applies bounded self-guided local repair to implicated components when execution evidence indicates failure. In two open-world genomics case studies, AgentCo-op composes independently developed scientific agents and external tool repositories into auditable workflows without redesigning them or running global topology search. It coordinates specialized agents for spatial transcriptomics and gene-set interpretation to enable collaborative discovery from spatial transcriptomics data, and builds a parallel workflow for cross-modality marker analysis on single-cell multiome data. AgentCo-op can also import a searched workflow as a structural prior and improve it by grounding nodes with retrieved components and applying local repair, showing that synthesis and search are complementary. On six coding, math, and question-answering benchmarks, AgentCo-op achieves the best result on four benchmarks and the best average score under a unified backbone setting, while consistently reducing per-task cost relative to multi-agent baselines. Together, these results suggest that retrieval-based synthesis can extend automated agentic workflow design beyond benchmark-optimized agent graphs to open-world workflows built from existing agents, tools, and typed artifacts.

---


### 61. [Multi-Week, In-Class Deployments of Telepresence Robots With Four Homebound K-12 Students: Benefits, Challenges, and Recommendations](https://arxiv.org/abs/2605.20431)

**<font color=#1a73e8>作者：</font>** Matthew Rueben, Rhianna Lee, Thomas R. Groechel 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Missing significant amounts of school during K-12 education is known to put students' cognitive and social development at risk. Alternatives such as home instruction and online learning are common, but lack sufficient interaction with peers and teachers in the classroom. Mobile remote presence systems, or telepresence robots, are promising for homebound students because they provide embodiment and mobility in addition to the real-time participation offered by video conferencing technologies. Research is needed, however, for telepresence robots to meet the complex needs of homebound students participating remotely in the K-12 classroom context. We present findings from four multi-week deployments with homebound K-12 students attending classes via telepresence robots. The homebound students' experiences were documented in a total of 15 interviews and analyzed qualitatively as case studies. The homebound student participants and their deployment contexts differed from one another along multiple dimensions, and while some benefits of mobile remote attendance were enjoyed by all participants, each participant also experienced unique benefits. Some challenges with hearing, seeing, and moving the robot around the classroom warranted improvements to the design of the telepresence system. Other challenges suggested priorities for managing a classroom deployment, such as ensuring that the remote student is included in classroom activities, accountable to the teacher, and treated with respect by classmates. Based on insights from the study, we make recommendations for real-world deployment procedures in similar contexts.

---


### 62. [Lighting-aware Unified Model for Instance Segmentation](https://arxiv.org/abs/2605.20436)

**<font color=#1a73e8>作者：</font>** Qisai Liu, Alloy Das, Zhanhong Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models like the Segment Anything Model (SAM) demonstrate impressive zero-shot generalization but frequently degrade under diverse real-world illumination, particularly for instance segmentation. In this work, we address this limitation by developing \textit{Lighting Convolutional-Attention (\lca{})}, an adapter module that enhances segmentation robustness without fine-tuning the heavy backbone. \lca{} employs a dual-branch architecture to process RGB features alongside contrast maps, enabling physically motivated sensitivity to structural changes rather than illumination artifacts. We optimize \lca{} through a pairwise training strategy, introducing a targeted loss term that explicitly penalizes discrepancies between clean images and their corresponding illumination variants. To evaluate and support this architecture, we conduct a comprehensive empirical study across multiple existing benchmarks and present a novel Unity-based synthetic dataset specifically designed to accurately replicate complex real-world lighting conditions. Extensive experimental results demonstrate that our approach successfully bridges the domain gap, delivering superior lighting-robust segmentation.

---


### 63. [Closing the Motivation Gap: Incentives Enhance Visual Misinformation Discernment and Verification](https://arxiv.org/abs/2605.20438)

**<font color=#1a73e8>作者：</font>** Sijia Qian, Cuihua Shen, Jingwen Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cheapfakes, or real images presented misleadingly or in unrelated contexts, are an increasingly prominent form of visual misinformation. While media literacy interventions can enhance individuals' ability to detect such content, motivational barriers often hinder the adoption of image verification. This study examines whether incorporating different mechanisms and types of incentives into a digital media literacy intervention improves visual misinformation discernment and image verification behavior, both immediately and over time. We conducted a pre-registered two-wave between-subjects online experiment (N = 1,421) on a professionally designed social media platform. The study used a 2 (Incentive Type: symbolic vs. monetary) x 2 (Incentive Mechanism: task- vs. result-based) factorial design with additional control groups. Results show that task-based incentives, particularly monetary ones, were most effective at initiating image verification behaviors, namely reverse image search, and boosting short-term discernment, whereas result-based incentives were more effective in sustaining discernment accuracy. These findings suggest that both the mechanism and the type of incentives play a critical role in shaping the short- and long-term effectiveness of media literacy interventions, highlighting the value of multi-phased incentive strategies for combating visual misinformation in digital environments.

---


### 64. [Can Conversational XAI Improve User Performance? An Experimental Study](https://arxiv.org/abs/2605.20439)

**<font color=#1a73e8>作者：</font>** Sven Kruschel, Julian Rosenberger, Lasse Bohlen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explainable AI (XAI) techniques aim to provide insights into predictive models and enhance user performance, yet they often fall short of these expectations. Conversational XAI assistants promise to overcome such limitations, but empirical evidence on their impact on objective performance measures remains limited. We propose an experimental design for evaluating explanation assistance through prediction accuracy, model understanding, and error identification. Using an explainable-by-design prediction model, we create conditions where users can outperform the model by identifying and compensating for systematic errors. We compare conversational assistance against Q&A-based assistance to assess which better supports users in working with model explanations. Preliminary results from testing our experimental design show that participants (N=42) in both treatments significantly outperformed the model but reveal no performance differences between assistance types and modest engagement overall. These findings inform refinements for our planned full study, including enhanced engagement interventions and investigation of the mechanisms driving improved predictions.

---


### 65. [Group-Algebraic Tensors: Provably-optimal Equivariant Learning and Physical Symmetry Discovery](https://arxiv.org/abs/2605.20440)

**<font color=#1a73e8>作者：</font>** Paulina Hoyos, Shashanka Ubaru, Dongsung Huh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the $\star_G$ tensor algebra, in which any finite group $G$ defines the multiplication rule, making equivariance an intrinsic algebraic property rather than an architectural constraint. The framework rests on three machine-verified theoretical pillars: (i)~an Eckart-Young optimality guarantee for the $\star_G$-SVD: the first such result for symmetry-preserving tensor approximation, exact and polynomial-time; (ii)~a Kronecker factorization that composes multiple symmetries by replacing $F_G$ with $F_{G_1} \otimes F_{G_2}$ with no architectural redesign; and (iii)~a 600-line Lean~4 formalization of the $\star_G$ algebra. The framework provides capabilities that equivariant neural networks (ENNs) structurally cannot: a closed-form per-irreducible-representation decomposition of every prediction, and data-driven discovery of the symmetry group that best fits a dataset. As a non-trivial empirical demonstration, decomposing QM9 molecular geometry over the chiral octahedral subgroup of SO(3) recovers the Wigner--Eckart selection rules of angular momentum from data alone, with no quantum mechanical input: scalar properties are A$_1$-dominated, dipole components are T$_1$-dominated, the isotropic polarizability is uniquely insensitive to $l\!=\!1$ as the rank-2-trace decomposition $l\!=\!0 \oplus l\!=\!2$ requires, and the T$_1$/A$_1$ predictive-power ratio separates vector observables from scalar observables by a factor of five. On full QM9 (130{,}831 molecules), $\star_G$-SVD with ridge regression provides closed form predictions at $\sim50-90\times$ fewer parameters than parameter-matched MLPs. Algebraic equivariance thus complements architectural equivariance not as a faster-better-cheaper alternative but as a different mathematical affordance: provably-optimal symmetry-preserving compression, per-irrep interpretability, and data-driven physical discovery.

---


### 66. [Weight Decay Regimes in Grokking Transformers: Cheap Online Diagnostics](https://arxiv.org/abs/2605.20441)

**<font color=#1a73e8>作者：</font>** Lucky Verma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers trained on modular arithmetic exhibit sharp transitions between memorization, generalization, and collapse. We show that weight decay acts as a scalar empirical control parameter for these regimes, and introduce two cheap online diagnostics, mean pairwise attention-head cosine similarity and entropy standard deviation, that track training dynamics from attention activations alone and complement loss-landscape diagnostics at lower compute cost. Across eleven experimental conditions and three model scales (0.82M to 85M parameters), the weight-decay axis separates memorization, developmental grokking, and collapse. A near-transition logistic fit localizes the memorization-to-developmental boundary at $\lambda_c=0.0158$ (95% CI [0.0109, 0.0200], N=210); a power-law fit gives an empirical exponent $\nu=0.757$ (CI [0.725, 0.799]). Reference exponents $\nu=1/2$ and 3D Ising $\nu \approx 0.63$ lie outside this empirical CI under our four-bin grid, so we report $\nu$ as empirical and defer universality-class identification to denser finite-size-scaling work. A horizon-matched multi-task replication (n=280, four modular operations) preserves the weight-decay control pattern; a paired attention-head re-initialization experiment at $\lambda=0.05$ changes Phase-2 amplitude (Cohen's $d=-1.190$, n=10, $p_t=4.5 \times 10^{-3}$), while matched weight-norm clipping does not. Three cross-architecture probes (4L MLP, 4L LSTM, and 4L Mamba; each n=70) replicate the weight-decay-controlled transition with architecture-specific $\lambda_c$ values. Main diagnostic claims are scoped to modular arithmetic in small transformer attention models; the non-attention experiments are scope probes, and architecture-wide, language-model, and universality-class claims are out of scope.

---


### 67. [Modeling Emotional Dynamics in Agent-to-Agent Interactions on Moltbook](https://arxiv.org/abs/2605.20442)

**<font color=#1a73e8>作者：</font>** Syed Mhamudul Hasan, Abdur R. Shahid  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI systems are increasingly deployed as interactive agents in online environments, such as a social network called Moltbook. In Moltbook, large-scale agentic AIs can post, comment, and engage in activities generated at scale by AI-driven text. Yet these agent behavioral characteristics remain insufficiently understood, particularly in complex, multi-agent interaction. In this study, we analyze the emotional dynamics of agent interactions within Moltbook. We construct an emotion-aware framework that maps textual interactions to a predefined set of fine-grained emotional categories, enabling the extraction of structured emotion profiles across agents and interaction contexts. To further evaluate behavioral reliability, we introduce an emotion-based domain called Persona-Stimulus-Reaction (PSR) that captures the alignment of emotional responses across similar contexts. Our analysis shows distinct emotional patterns and varying levels of behavioral stability across agents. Our analysis reveals that agents exhibit distinct emotional signatures with varying levels of behavioral stability influenced by interaction context.

---


### 68. [A Comprehensive Comparison of Deep Learning Architectures for COVID-19 Classification on CT & X-ray Imagery](https://arxiv.org/abs/2605.20445)

**<font color=#1a73e8>作者：</font>** Sarmad Khan, Arslan Shaukat, Umer Asgher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> COVID-19 was a significant challenge that led to the loss of numerous lives daily. Not only a certain country was involved in this outbreak, but even the world has suffered because of the coronavirus. Imaging techniques using computed tomography (CT) and X-rays of the lungs are the most useful tools for the COVID-19 or any other pandemic disease screening process. Technology today has revolutionized the world by using artificial intelligence to replace manual processes with automated machines, which enable the system to imitate the human brain by making wise decisions based on experience. Motivated by this, our work proposes to use convolutional neural networks (CNN) based models for designing a computer-aided diagnosis (CAD) system that differentiates between COVID-19 and healthy lung pictures. We used two different sets of X-ray images of the lungs in addition to two different sets of CT scans and the classification is done using a variety of networks that have been pre-trained such as VGG (16, 19), Densenet (121), Resnet (50, 50 V2, 101 V2), Mobile net (V2), Xception Inception (V3, Resnet V2), Efficient net (B0) and Nasnet (Large). On the X-ray and CT image datasets, Resnet and VGG architecture have shown the ability to properly differentiate COVID-19 from normal images, with an average accuracy of 95 to 98 percent respectively. Our acquired results on the classification datasets are competitive and superior to previously reported findings in the literature.

---


### 69. [SMA-DP: Spectral Memory-Aware Differential Privacy for Deep Learning](https://arxiv.org/abs/2605.20450)

**<font color=#1a73e8>作者：</font>** Mohammad Partohaghighi, Roummel Marcia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially private stochastic gradient descent (DP-SGD) enables private deep learning through per-example clipping and calibrated Gaussian noise, but its high-variance updates can reduce utility on challenging datasets. We propose \textbf{SMA-DP-SGD}, a \textbf{Spectral Memory-Aware Differentially Private Stochastic Gradient Descent} method that augments DP-SGD with a fractional memory branch built only from previously privatized noisy releases. WeightWatcher-inspired power-law spectral exponents provide group-wise reliability signals, instantiated layer-wise in our experiments, to adapt the decay and effective memory depth. Private-history alignment, norm matching, and warm-up activation stabilize the memory contribution. Privacy remains transparent: conditioned on the private release history, the memory branch is fixed, and the only newly data-dependent term is the current clipped sum scaled by a fixed coefficient \(\beta\). Hence, SMA-DP-SGD preserves a clean conditional sensitivity structure and exactly recovers group-wise DP-SGD when \(\beta=1\). Experiments on CIFAR-100, CIFAR-10, and MNIST show competitive or superior accuracy over several DP optimization baselines, with the largest gains on CIFAR-100 and CIFAR-10. CIFAR-10 ablations show that \(\beta\) controls the privacy--utility trajectory, while spectral and memory diagnostics confirm a controlled short-to-moderate effective memory depth and a small memory-branch ratio. Runtime analysis shows that the mechanism incurs additional overhead, about \(2.94\times\) DP-SGD in our CIFAR-10 implementation, revealing a practical trade-off between adaptive private memory and computational cost.

---


### 70. [ELEMENT: Multi-Modal Retinal Vessel Segmentation Based on a Coupled Region Growing and Machine Learning Approach](https://arxiv.org/abs/2605.20458)

**<font color=#1a73e8>作者：</font>** Erick O. Rodrigues, Aura Conci, Panos Liatsis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vascular structures in the retina contain important information for the detection and analysis of ocular diseases, including age-related macular degeneration, diabetic retinopathy and glaucoma. Commonly used modalities in diagnosis of these diseases are fundus photography, scanning laser ophthalmoscope (SLO) and fluorescein angiography (FA). Typically, retinal vessel segmentation is carried out either manually or interactively, which makes it time consuming and prone to human errors. In this research, we propose a new multi-modal framework for vessel segmentation called ELEMENT (vEsseL sEgmentation using Machine lEarning and coNnecTivity). This framework consists of feature extraction and pixel-based classification using region growing and machine learning. The proposed features capture complementary evidence based on grey level and vessel connectivity properties. The latter information is seamlessly propagated through the pixels at the classification phase. ELEMENT reduces inconsistencies and speeds up the segmentation throughput. We analyze and compare the performance of the proposed approach against state-of-the-art vessel segmentation algorithms in three major groups of experiments, for each of the ocular modalities. Our method produced higher overall performance, with an overall accuracy of 97.40%, compared to 25 of the 26 state-of-the-art approaches, including six works based on deep learning, evaluated on the widely known DRIVE fundus image dataset. In the case of the STARE, CHASE-DB, VAMPIRE FA, IOSTAR SLO and RC-SLO datasets, the proposed framework outperformed all of the state-of-the-art methods with accuracies of 98.27%, 97.78%, 98.34%, 98.04% and 98.35%, respectively.

---


### 71. [Pixel Wised Lesion Prediction on COVID-19 CT Imagery: A Comparative Analysis of Automated Image Segmentation Architectures](https://arxiv.org/abs/2605.20459)

**<font color=#1a73e8>作者：</font>** Sarmad Khan, Arslan Shaukat, Umer Asgher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, there has been a notable increase in the level of attention that is given to algorithms based on deep learning in the context of medical image segmentation. Nevertheless, the reliability of the field has been hindered due to the absence of a standardized methodology for performance analysis and the utilization of different datasets in previous research. The primary objective of the research is to comprehensively evaluate contemporary segmentation frameworks combined with state-of-the-art pre-trained backbones in order to accurately predict COVID-19 lesions in CT images. Moreover, this evaluation can serve as a point of reference for the segmentation of images in various other imaging scenarios. In order to accomplish this, we integrate four distinct deep learning architectures, namely Unet, PSPNet, Linknet, and FPN, with six pre-trained encoders, including VGG 19, DenseNet 121, Inception ResNet V2, MobileNet V2, SeresNet 101, and EfficientNet B0. This approach enables the development of diverse testing architectures. In the context of image segmentation, our research encompassed both binary and multi-class experimentation. The findings derived from our analysis of three distinct COVID-19 CT segmentation datasets indicate that deep learning architectures yield precise and efficient segmentation outcomes. Significantly, a maximum F1-Score of 98% was attained for binary class segmentation, while multi-class segmentation yielded F1-Scores of 75% and 77% across two separate datasets. The utilization of artificial intelligence and deep learning enhances the diagnostic process for pandemic diseases across multiple dimensions.

---


### 72. [Understanding Model Behavior in Monocular Polyp Sizing](https://arxiv.org/abs/2605.20461)

**<font color=#1a73e8>作者：</font>** Xinqi Xiong, Andrea Dunn Beltran, Junmyeong Choi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate polyp size stratification guides surveillance decisions, with lesions larger than 5 mm typically requiring closer follow-up. However, monocular colonoscopy lacks a reliable metric reference. We present a diagnostic audit of binary polyp size classification (<=5 mm vs. >5 mm) across multiple public multi-center datasets, model families, and patient-stratified cross-validation. Across architectures and input modalities, including RGB appearance, relative depth, and photometry, model performance is moderately consistent, suggesting reliance on cues correlated with examination behavior rather than true metric scales. By providing ground-truth scale at varying granularities, we quantify the potential improvement from perfect scale information and show that current depth estimation and global calibration offer limited gains. We further demonstrate that segmentation errors under distribution shift eliminate most of this potential, with oracle scale under predicted masks recovering only baseline performance. These results highlight metric scale and mask robustness as two independent bottlenecks and provide reusable evaluation tools such as oracle scale ladders, shortcut partitions, and mask substitution for auditing future polyp sizing pipelines. Our code is publicly accessible at this https URL.

---


### 73. [Art Card Game (ACG): Embedding Illustration in Gameplay to Mitigate Artist Self-Criticism](https://arxiv.org/abs/2605.20465)

**<font color=#1a73e8>作者：</font>** Catherine Mullings, Michael S. Bernstein  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Persistent self-criticism--harsh evaluative self-talk--can undermine illustrators' performance and well-being. Traditional interventions draw on psychotherapeutic approaches (e.g., compassion training) but sit outside the illustration workflow, requiring time, facilitation, and skill transfer. We propose an in-workflow alternative: evaluative off-centering, a mechanism redirecting self-critical evaluation away from an inherently self-evaluative task (like illustration) by embedding it in an alternative activity. We instantiate evaluative off-centering in Art Card Game (ACG) that integrates illustration into a card customization game: players illustrate cards that become playable assets in a head-to-head battle. In a four-day randomized controlled study with hobbyist and professional illustrators (N=38), ACG outperformed a control condition with identical illustration constraints but no evaluative off-centering mechanisms (e.g. multiplayer, gameplay), yielding significantly higher pride in produced artwork and activity enjoyment. Pride and enjoyment--positive affect states linked to lower self-criticism--help explain how ACG reduces self-criticism. We discuss design implications for creativity support tools that apply evaluative off-centering across creative domains.

---


### 74. [High Quality Embeddings for Horn Logic Reasoning](https://arxiv.org/abs/2605.20467)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Yasir White, Dean Clark 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural networks can be trained to rank the choices made by logical reasoners, resulting in more efficient searches for answers. A key step in this process is creating useful embeddings, i.e., numeric representations of logical statements. This paper introduces and evaluates several approaches to creating embeddings that result in better downstream results. We train embeddings using triplet loss, which requires examples consisting of an anchor, a positive example, and a negative example. We introduce three ideas: generating anchors that are more likely to have repeated terms, generating positive and negative examples in a way that ensures a good balance between easy, medium, and hard examples, and periodically emphasizing the hardest examples during training. We conduct several experiments to evaluate this approach, including a comparison of different embeddings across different knowledge bases, in an attempt to identify what characteristics make an embedding well-suited to a particular reasoning task.

---


### 75. [CASCADE Conformal Prediction: Uncertainty-Adaptive Prediction Intervals for Two-Stage Clinical Decision Support](https://arxiv.org/abs/2605.20468)

**<font color=#1a73e8>作者：</font>** Ricardo Diaz-Rincon, Muxuan Liang, Adolfo Ramirez-Zamora 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective medication management in Parkinson's Disease (PD) is challenging due to heterogeneous disease progression, variable patient response, and medication side effects. While AI models can forecast levodopa equivalent daily dose (LEDD) as a measure of medication needs, standard uncertainty quantification often fails to communicate the reliability of these predictions, treating high and low confidence clinical decisions identically. We introduce CASCADE (Calibrated Adaptive Scaling via Conformal And Distributional Estimation), a novel conformal prediction framework that propagates epistemic uncertainty from a screening classifier to adapt downstream predictions. Unlike standard conformal methods that rely on auxiliary residual regression, we leverage epistemic uncertainty from a primary classification task (identifying whether a medication change is needed) to dynamically scale the prediction intervals of a secondary regression task (predicting how much change). By mapping Venn-Abers multi-probabilistic uncertainty directly to non-conformity scores, our framework achieves continuous risk adaptation. We demonstrate that this ``cascade effect'' produces highly efficient intervals for confident patients (38.9% narrower than standard conformal baselines) while automatically expanding intervals to ensure robust coverage for uncertain cases, bridging the gap between discrete clinical decision-making and continuous dose forecasting in PD.

---


### 76. [EPC-3D-Diff: Equivariant Physics Consistent Conditional 3D Latent Diffusion for CBCT to CT Synthesis](https://arxiv.org/abs/2605.20470)

**<font color=#1a73e8>作者：</font>** Alzahra Altalib, Chunhui Li, Haytham Al Ewaidat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cone-beam CT (CBCT) is routinely acquired during radiotherapy for patient setup, but its quantitative reliability is degraded by scatter, noise, and reconstruction artifacts, limiting Hounsfield Unit (HU) accuracy. We propose EPC-3D-Diff, a novel conditional 3D latent diffusion framework for volumetric CBCT to CT synthesis that introduces a projection domain equivariance loss derived from acquisition physics. Unlike common image domain equivariance, we exploit the fact that an in plane rotation of the volume corresponds to an angular shift in its projections. During training, we enforce this relationship by forward projecting rotated synthesized CT volumes and matching them to appropriately angle shifted projections of the paired target CT, yielding a physics consistent equivariance constraint integrated into the diffusion objective. To capture full 3D context efficiently, conditional diffusion is performed in a compact latent space learnt by a lightweight 3D autoencoder, preserving axial depth while downsampling in plane resolution for stable training. We validate on a paired head CBCT/CT phantom dataset, including repeat scans, and paired clinical data using patient wise splits, and perform single and mixed domain training, ablations, and comparisons with diffusion and CycleGAN. EPC-3D-Diff generalizes well and achieved substantial improvements, +7.4 dB (phantom) and +1.8 dB (clinical data) in PSNR compared to state of the art methods, alongside improved SSIM and HU accuracy, within tissue boundaries. Overall, EPC-3D-Diff improves robustness and physics consistency, supporting HU aware synthesis for downstream radiotherapy workflows.

---


### 77. [Goodbye Drift: Anchored Tree Sampling for Long-Horizon Video-to-Video Generation](https://arxiv.org/abs/2605.20476)

**<font color=#1a73e8>作者：</font>** Matthew Bendel, Stephen W. Bailey, Mithilesh Vaidya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon video generation suffers from two intertwined issues. First, there is drift, where video quality degrades over time. Second, there are continuity issues which manifest as object permanence issues, or improperly rendering transient content (e.g., an object that appears in non-consecutive frames changing color/style). Recent work has focused on autoregressive distillation techniques that attack both problems simultaneously. We instead choose to focus on drift directly and introduce \textbf{Anchored Tree Sampling (ATS)}: a training-free inference-time scheduler that replaces left-to-right rollout with sparse-to-dense, anchor-bounded imputation organized as a tree. A root call produces sparse anchors over the full horizon, recursive refinement generates intermediate anchors, and final leaf spans are synthesized between neighboring anchors. This reduces the critical path from $K$ sequential rollout steps to $L+1$ tree-hierarchical steps and converts horizon-compounding drift into anchor-bounded drift. We focus on V2V generation in the \emph{static-camera} regime, where sparse anchors over the horizon are well approximated by the dense conditioning signal, and the base model can produce them without retraining. We evaluate ATS against two contemporary autoregressive baselines on Wan $2.1$ $+$ VACE, across five conditioning modalities (inpainting, outpainting, edge, pose, depth). We show that ATS outperforms both competitors in overall quality, as well as in drift prevention. We additionally demonstrate stable $\geq 40$-minute generation on LTX-$2.3$ across the same five modalities. We conclude by proposing a path forward to extend ATS to arbitrarily long T2V generation, as well as the dynamic-camera and multi-shot regimes.

---


### 78. [Training Language Agents to Learn from Experience](https://arxiv.org/abs/2605.20477)

**<font color=#1a73e8>作者：</font>** Yuval Shalev, Zifeng Ding, Mateja Jamnik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language agents can adapt from experience in interactive environments, but current reflection-based methods can only self-correct within a single task instance. Whether such experience can be distilled into reusable lessons that improve performance on future unseen tasks remains unclear. We address this problem by introducing the In-context Training (ICT) task, a framework for evaluating cross-task self-improvement in language agents. In ICT, a reflector model observes trajectories collected by an actor model and generates system prompts intended to improve the actor's performance on future unseen tasks. We then propose an RL-based training pipeline for learning such reflections directly from experience, without human-provided examples. Across ALFWorld and MiniHack, our trained reflectors outperform an untrained baseline on most held-out task families, showing that the ability to learn from experience can itself be learned. In some cases, we observe generalisation beyond the benchmark on which the reflector was trained, to substantially different environments. Finally, we introduce MetaGym, a generic Python library for constructing meta-environments, enabling future research on self-improving language agents.

---


### 79. [Stage-Audit: Auditable Source-Frontier Discovery for Cross-Wiki Tables](https://arxiv.org/abs/2605.20478)

**<font color=#1a73e8>作者：</font>** Chen Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-curated tables can appear source-grounded while containing unsupported rows: the curator may recall entries from parametric memory and retroactively attach page-level citations that are not the actual source. We study this hazard in Seed2Frontier discovery: the task of finding complement Wikipedia pages from a seed page to assemble a structured table. Stage-Audit addresses it with disjoint curator-auditor write rights, a row-level source-citation gate, and a 12-check audit taxonomy over keys, schema, source roles, cardinality, and scope. On a curated 51-instance Seed2Frontier evaluation set spanning 15 top-level domains, Stage-Audit improves source-frontier precision over a vanilla LLM curator from 0.356 to 0.505 (+42% relative) and F1 from 0.334 to 0.451 (+35%), while maintaining explicit per-row source traceability. The vanilla-LLM-vs-Stage-Audit comparison isolates the policy contribution rather than LLM-based discovery in general.

---


### 80. [Oracle Supervision Transfers for Hyperparameter Prediction in Model-Based Image Denoising](https://arxiv.org/abs/2605.20479)

**<font color=#1a73e8>作者：</font>** Jianmin Liao, Lixin Shen, Yuesheng Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperparameter prediction is a critical practical bottleneck for model-based image denoisers, ranging from classical TV/TGV variational solvers to modern diffusion-based models such as DiffPIR. While existing learned predictors can achieve near-oracle performance, this approach scales poorly: each new configuration conventionally requires its own oracle-labeled training set, and each label requires a hierarchical grid search evaluated against clean ground truth. We therefore ask whether oracle supervision collected on source configurations can transfer to target configurations with few or no target oracle labels. We propose HyperDn, a single configuration-conditioned predictor that pools oracle supervision across source configurations and predicts heterogeneous hyperparameters for new denoiser--noise configurations. In a cross-paradigm experiment, HyperDn transfers from relatively cheap TV/TGV variational sources to more expensive diffusion-based DiffPIR. With only $2$ target oracle labels, it reaches $30.23$\,dB, within $0.90$\,dB of the oracle, and outperforms the $64$-label per-configuration predictor trained from scratch, using $1/32$ as many target labels as that baseline point. Without any target oracle labels, HyperDn also reaches near-oracle PSNR on two unseen mixtures of seen noise types and on transfer from relatively cheap $96\times 96$ source images to $512\times 768$ targets. Together, these results show that expensive oracle supervision for hyperparameter prediction can be transferred from source to new target configurations, reducing the need to rebuild oracle labels for each new denoising configuration.

---


### 81. [Quadratic Characterizations for Reachability Analysis of Neural Networks](https://arxiv.org/abs/2605.20482)

**<font color=#1a73e8>作者：</font>** Elias Khalife, Mazen Farhood, Pierre-Loic Garoche  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quadratic constraints (QCs) are widely used to characterize nonlinearities and uncertainties, but generic analytical characterizations can be conservative on bounded domains. This paper develops a framework for constructing verified quadratic characterizations of scalar relations in the two-dimensional real plane. Candidate quadratic inequalities are locally generated by solving convex quadratic programs using samples from the relation and exterior sample points. They are then verified globally using sum-of-squares certificates over an exact semialgebraic description or, in the case of nonpolynomial relations, over relaxed polynomial descriptions. The resulting verified constraints define a sound overapproximation of the scalar relations over the considered domains. These constraints are directly compatible with existing analysis frameworks based on QCs and pointwise integral quadratic constraints (IQCs) for static nonlinearities and uncertainties, and they can also be embedded in QC-based semidefinite programs for reachability and safety analysis of feedforward neural networks. For smooth activations such as $\tanh$, the method yields domain-dependent quadratic characterizations that constitute an alternative to generic sector- or slope-based descriptions. For ReLU networks, we give methods to reduce conservatism in QC-based reachability analysis of feedforward networks by exploiting dependencies between neurons and tighter local bounds. Numerical examples demonstrate improved reachability results for smooth activations, reduced conservatism for ReLU networks, and applicability beyond neural networks through an example involving saturation.

---


### 82. [\ECUAS{n}: A family of metrics for principled evaluation of uncertainty-augmented systems](https://arxiv.org/abs/2605.20490)

**<font color=#1a73e8>作者：</font>** Lautaro Estienne, Erik Ernst, Matías Vera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In high-stakes automated decision-making, access to predictive uncertainty is essential for enabling users -- human or downstream systems -- to accept or reject predictions based on application-specific cost trade-offs. Such uncertainty-augmented (UA) systems -- i.e., systems that output both predictions and uncertainty scores -- are currently being assessed in the literature in a variety of ways, using separate metrics to evaluate the predictions and the uncertainty scores, setting a cost function with a fixed rejection cost or integrating over a coverage-risk curve. We argue that these evaluation approaches are inadequate for assessing overall performance of the UA system for decision making under uncertainty and propose a novel family of metrics, \ECUAS{n}, formulated as proper scoring rules for the task of interest. The parameter $n$ controls the trade-off between the cost of incorrect predictions and imperfect uncertainties depending on the needs of the use-case. We demonstrate the advantages of the \ECUAS{n} metrics both theoretically and empirically, through experiments on diverse classification and generation datasets, including a manually annotated subset of TriviaQA.

---


### 83. [A 10,000-Year Global Stochastic Tropical Cyclone Catalog with Wind-Dependent Track Transitions (WHITS)](https://arxiv.org/abs/2605.20494)

**<font color=#1a73e8>作者：</font>** Jennifer Nakamura, Upmanu Lall  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable assessment of tropical cyclone (TC) risk is limited by the brevity and spatial sparsity of the historical record, particularly for the rare, high-intensity landfalls that dominate insured loss. We present WHITS (Wind-focused Hurricane Interactive Track Simulator), a non-parametric semi-Markov track generator that extends the HITS framework of Nakamura et al. (2015) in three ways: transitions between historical track segments are conditioned on local wind speed in addition to position, age, and forward vector; the kernel selection on the comparative-vector term is sharpened to suppress dynamically inconsistent jumps; and a short smoothing window is applied across each transition to remove the position and wind discontinuities reported by downstream surge users. WHITS is fit to the full available best-track record in each of six basins in IBTrACS, extending in the North Atlantic to 1851 and in other basins to the earliest year of reliable best-track data. The resulting 10,000-yr global synthetic catalog reproduces observed track density and the annual hurricane/typhoon-force wind-hit probability across all basins. The catalog is intended for catastrophe-risk applications where a large, low-bias sample of physically plausible tracks is more useful than a small, statistically corrected one.

---


### 84. [Tippett-minimum Fusion of Representation-space Diffusion Models for Multi-Encoder Out-of-Distribution Detection](https://arxiv.org/abs/2605.20502)

**<font color=#1a73e8>作者：</font>** Neelkamal Bhuyan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address out-of-distribution (OOD) detection across the full spectrum of distribution shifts -- global domain changes, semantic divergence, texture differences, and covariate corruptions -- through a multi-encoder fusion of per-encoder representation-space diffusion models (RDMs). We statistically identify each encoder's sensitivity to specific shift types from ID data alone and introduce EncMin2L -- an encoder-agnostic two-level $\min(\cdot)$-gate that combines and calibrates per-encoder diffusion-based likelihood detectors without OOD labels, outperforming monolithic multi-encoder baselines at $2.3\times$ lower parameter cost. Two ID-data diagnostics: $\eta^2$ (class-conditional F-test) and $\Delta\mu$ (log-likelihood shift under synthetic corruptions) -- quantify encoder specialization, while a Tippett minimum $p$-value combination aggregates per-encoder scores into a single, calibration-stable OOD signal. EncMin2L achieves $\geq 0.94$ AUROC across all four shift types simultaneously, outperforming the state-of-the-art representation-space diffusion OOD detectors across overlapping benchmarks.

---


### 85. [Reinforcing Human Behavior Simulation via Verbal Feedback](https://arxiv.org/abs/2605.20506)

**<font color=#1a73e8>作者：</font>** Weiwei Sun, Xuhui Zhou, Jiarui Liu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Humans learn social norms and behaviors from verbal feedback (e.g., a parent saying "that was rude" or a friend explaining "here's why that hurt"). Yet, learning from feedback for LLMs has largely focused on domains like code and math, where RL rewards are directly verifiable and condensed into scalar values. As LLMs are increasingly used to simulate human behavior, e.g., standing in for users, patients, students, and other personas, there is a pressing need to make them more human-like, which requires embracing a fundamentally different kind of signal: feedback that is verbal, subjective, and multi-faceted. We present DITTO, a model trained by treating verbal feedback as a first-class signal in reinforcement learning. After each rollout, DITTO receives verbal feedback and generates a feedback-conditioned improved rollout; both outputs are jointly optimized with GRPO, distilling verbal guidance into the base policy without requiring feedback at test time. We also introduce SOUL (Simulation gym Of hUman-Like behavior), a unified benchmark and training data suite spanning 10 tasks across six categories: Theory of Mind, character role play, social skill, learner simulation, user simulation, and persona simulation. DITTO achieves an average 36% improvement over the base model and exceeds GPT-5.4 on 6 of 10 SOUL benchmarks, demonstrating that RL with verbal feedback is a promising direction for training LLMs to simulate human behavior.

---


### 86. [ShadeBench: A Benchmark Dataset for Building Shade Simulation in Sustainable Society](https://arxiv.org/abs/2605.20510)

**<font color=#1a73e8>作者：</font>** Longchao Da, Mithun Shivakoti, Xiangrui Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban heat exposure is becoming an increasingly critical challenge due to the intensifying urban heat island effect. Fine-grained shade patterns, especially those induced by urban buildings, strongly influence pedestrians' thermal exposure and outdoor activity planning. However, accurately modeling and analyzing urban shade at scale remains difficult because of the lack of large-scale datasets and systematic evaluation frameworks. To address this challenge, we present ShadeBench, a comprehensive dataset and benchmark for urban shade understanding. ShadeBench contains geographically diverse urban scenes with temporally varying simulated shade maps and textual descriptions, together with aligned satellite imagery, building skeleton representations, and 3D building meshes. Built upon this multimodal dataset, ShadeBench supports a range of downstream tasks, including shade generation, shade segmentation, and 3D building reconstruction. We further establish standardized evaluation protocols and baseline methods for these tasks. By enabling scalable and fine-grained shade analysis, ShadeBench provides a foundation for data-driven urban climate research and supports future studies in heat-resilient urban planning and decision-making. The code and dataset are publicly available at this https URL.

---


### 87. [Creating Learning Scaffolds for Engineering Design Using Concept Catalyst](https://arxiv.org/abs/2605.20511)

**<font color=#1a73e8>作者：</font>** Madhuri Singh, Gennie Mansi, Mark Owen Riedl  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> K-12 teachers employ Engineering Design Challenges to help students learn about the Engineering Design Process hands-on. They use techniques like hard scaffolding questions to guide the students as they think through the different stages of the engineering design process. While useful, the creation of these questions adds to the teacher's preparation time for their classes. Concept Catalyst uses Large Language Models to assist teachers with the rapid creation of scaffold questions for engineering design challenges. Unlike open-ended chat, Concept Catalyst uses LLMs to summarize and decompose an engineering design challenge into the concepts that students will engage with, allow the teacher to visually manipulate and link related concepts, and to propose scaffolding questions for the teacher to modify or accept.

---


### 88. [Fast Reconstruction of Exact Maxwell Dynamics from Sparse Data](https://arxiv.org/abs/2605.20514)

**<font color=#1a73e8>作者：</font>** Dan DeGenaro, Xin Li, Obed Amo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce FLASH-MAX, a shallow, exact-by-construction neural network architecture for predicting homogeneous electromagnetic fields from sparse pointwise observations. Each hidden neuron represents a separate exact solution to Maxwell's equations, so that the network satisfies the governing equations symbolically by construction and can be trained end-to-end from sparse data within seconds. We prove a universal approximation result showing that this exact model class remains universal on arbitrary domains. FLASH-MAX reaches sub-1% relative validation error from about 1K sparse pointwise observations in seconds, all while maintaining a zero PDE residual, and keeps single-digit errors even for only 100 observations sampled from 3D space. These results suggest that moving governing structure from the loss into the hypothesis class can dramatically improve the trade-off between precision and optimization speed in scientific machine learning.

---


### 89. [Online Conformal Prediction with Corrupted Feedback](https://arxiv.org/abs/2605.20515)

**<font color=#1a73e8>作者：</font>** Bowen Wang, Matteo Zecchin, Osvaldo Simeone  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern artificial intelligence systems require calibrated uncertainty estimates that remain reliable in sequential and non-stationary environments. Online conformal prediction (OCP) addresses this challenge through adaptively updated prediction sets that provide deterministic long-run miscoverage guarantees. These guarantees, however, hinge on the assumption of perfect feedback about the coverage of past prediction sets. In practice, the observed miscoverage indicator may be corrupted by noise, communication failures, or adversarial manipulation, which can severely degrade OCP's calibration guarantees. In this paper, we study OCP under corrupted feedback. We first model feedback corruption as an arbitrary binary flip sequence, and analyze how feedback corruption affects and degrades the miscoverage performance of standard OCP. We then propose two robust schemes: robust OCP via filtering, which leverages the structural properties of the predicted threshold to filter corrupted feedback, and robust OCP via active compensation, which incorporates an active compensation mechanism to mitigate the effect of corrupted feedback. For both methods, we establish explicit miscoverage guarantees, which are further specialized for an independent stochastic flip model and for an arbitrary error model with memory bounds. Experiments on real-world datasets validate the proposed approach, showing markedly improved calibration and significantly smaller prediction sets compared with baseline OCP methods under corrupted feedback.

---


### 90. [Open-World Evaluations for Measuring Frontier AI Capabilities](https://arxiv.org/abs/2605.20520)

**<font color=#1a73e8>作者：</font>** Sayash Kapoor, Peter Kirgis, Andrew Schwartz 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmark-based evaluation remains important for tracking frontier AI progress. But it can both overstate and understate deployed capability because it privileges tasks that can be precisely specified, automatically graded, easy to optimize for, and run with low budgets and short time horizons. We advocate for a complementary class of evaluations, which we term open-world evaluations: long-horizon, messy, real-world tasks assessed through small-sample qualitative analysis rather than benchmark-scale automation. In this paper we survey recent open-world evaluations, identify their strengths and limitations, and introduce CRUX (Collaborative Research for Updating AI eXpectations), a project for conducting such evaluations regularly. As a first instance, we task an AI agent with developing and publishing a simple iOS application to the Apple App Store. The agent completed the task with only a single avoidable manual intervention, suggesting that open-world evaluations can provide early warning of capabilities that may soon become widespread. We conclude with recommendations for designing and reporting open-world evals.

---


### 91. [NeuroQA: A Large-Scale Image-Grounded Benchmark for 3D Brain MRI Understanding](https://arxiv.org/abs/2605.20525)

**<font color=#1a73e8>作者：</font>** Mohammad H. Abbasi, Favour Nerrise, Shaurnav Ghosh 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present NeuroQA, a large-scale benchmark for visual question answering in 3D brain magnetic resonance imaging (MRI), with 56,953 QA pairs from 12,977 subjects across 12 datasets. It spans ages 5-104 and five clinical domains: Alzheimer's, Parkinson's, tumors, white matter disease, and neurodevelopment. Unlike prior medical Visual Question Answering (VQA) efforts that operate on 2D slices or rely on narrow diagnostic labels, NeuroQA pairs every item with a full 3D volume. It evaluates 11 clinically grounded reasoning skills across Yes/No, multiple-choice, and open-ended formats. Of the 203 templates, 131 are image-grounded (answerable from a 3-plane viewer) and 72 are image-informed (ground truth from quantitative volumetry or clinical instruments). To remove text-only shortcuts, we apply answer-distribution refinement, reducing closed-format text-only accuracy from $>$80% to 44.6%; image necessity is assessed separately through an image-grounding protocol released with the benchmark. A 38-rule deterministic pipeline and two rounds of expert review verify every QA pair against FreeSurfer measurements, metadata, or radiology report fields, with zero same-subject contradictions across templates. We conduct a clinician evaluation in which two clinicians independently assess 100 frozen test items on a three-plane viewer. On closed-format (Yes/No + multiple-choice) test-public items, the best zero-shot vision-language model and a supervised 3D CNN baseline reach 47.5% and 43.7% accuracy respectively, both below the 49.4% text-only majority-template floor. NeuroQA adopts a two-tier release with public QA pairs for open-access datasets and reproducible generation scripts for datasets restricted by data use agreements (DUAs), plus subject-level splits, a held-out private test set, and an online leaderboard.

---


### 92. [Collocational bootstrapping: A hypothesis about the learning of subject-verb agreement in humans and neural networks](https://arxiv.org/abs/2605.20529)

**<font color=#1a73e8>作者：</font>** Claire Hobbs, R. Thomas McCoy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In what ways might statistical signals in linguistic input assist with the acquisition of syntax? Here we hypothesize a mechanism called collocational bootstrapping, in which regularities in word co-occurrence patterns can provide cues to syntactic dependencies. We investigate whether this mechanism can support the acquisition of English subject-verb agreement. First, we simulate language acquisition by training neural networks on synthetic datasets that vary in how predictable their subject-verb pairings are. We find that there is a range of variability levels at which these statistical learners robustly learn subject-verb agreement. We then analyze the variability of subject-verb pairings in child-directed language, and we find that the variability in such data falls within the range that supported robust generalization in our computational simulations. Taken together, these results suggest that collocational bootstrapping is a viable learning strategy for the type of input that children receive.

---


### 93. [Ada2MS: A Hybrid Optimization Algorithm Based on Exponential Mixing of Elementwise and Global Second-Moment Estimates](https://arxiv.org/abs/2605.20533)

**<font color=#1a73e8>作者：</font>** Meng Zhu, Quan Xiao, Weidong Min  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimization algorithms are core methods by which machine learning models iteratively minimize loss functions, update parameters, learn from data, and improve performance. Momentum SGD and AdamW represent two important optimization paradigms. AdamW produces stable updates and usually has strong robustness across training scenarios, but its generalization performance is sometimes weaker than that of momentum methods. Momentum SGD can often obtain better generalization after careful tuning, but it is more sensitive to gradient-scale variation and hyperparameter settings. To balance the strengths and weaknesses of the two paradigms, this paper proposes Ada2MS, an optimization algorithm that achieves a smooth transition between AdamW-like behavior and momentum-SGD-like behavior through continuous exponential interpolation between elementwise second-moment estimates and global second-moment estimates. On the visual tasks evaluated in this study, Ada2MS obtains competitive results under a unified optimizer-comparison protocol. The code will be released at this https URL

---


### 94. [Axiomatizing Neural Networks via Pursuit of Subspaces](https://arxiv.org/abs/2605.20534)

**<font color=#1a73e8>作者：</font>** Mehmet Yamac, Mert Duman, Ugur Akpinar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While deep neural networks have achieved remarkable success across a wide range of domains, their underlying mechanisms remain poorly understood, and they are often regarded as black boxes. This gap between empirical performance and theoretical understanding poses a challenge analogous to the pre-axiomatic stage of classical geometry. In this work, we introduce the Pursuit of Subspaces (PoS) hypothesis, an axiomatic framework that formulates neural network behavior through a set of geometric postulates. These axioms, together with their derived consequences, provide a unified perspective on representation, computation, and generalization in both shallow and deep architectures. We show that this framework yields geometric explanations for fundamental questions in deep learning, including representation structure, architectural mechanisms, and generalization behavior, offering a principled step toward a coherent theoretical foundation.

---


### 95. [HADS-Net:A Hybrid Attention-Augmented Dual-Stream Network with Physics-Informed Augmentation for Breast Ultrasound Image Classification](https://arxiv.org/abs/2605.20536)

**<font color=#1a73e8>作者：</font>** Chinedu Emmanuel Mbonu, Blessing Nwamaka Iduh, Joseph Ikechukwu Odo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate classification of breast ultrasound images into benign, malignant, and normal categories is a critical clinical task complicated by speckle noise, acoustic shadowing, and inter-class visual ambiguity. Existing deep learning methods rely on single-stream architectures with generic augmentation that ignores ultrasound acquisition physics, and no prior method dedicates a stream to the lesion boundary features identified as the most diagnostically significant visual cue. We propose HADS-Net, a Hybrid Attention-Augmented Dual-Stream Network exploiting global texture and local boundary cues through two parallel pathways. Stream 1 applies physics-informed augmentation simulating speckle noise, acoustic shadowing, and gain variation before extracting features via pretrained EfficientNet-B3 projected to 512 dimensions. Stream 2 extracts Sobel edge maps processed by a lightweight CNN projected to the same 512-dimensional space. A cross-attention fusion module allows the texture stream to selectively query boundary features, producing a jointly optimised representation classified by an MLP trained with adaptive class-weighted focal loss. Five-fold stratified cross-validation with cosine annealing over 50 epochs is used, with the globally best checkpoint selected by lowest validation loss evaluated on a held-out test set. On the BUSI dataset, HADS-Net achieves 96.58% accuracy, macro ROC-AUC of 0.9978, macro F1 of 0.9654, and per-class F1-scores of 0.970, 0.951, and 0.976 for benign, malignant, and normal. No malignant lesion is misclassified as normal. These results confirm that modality-specific augmentation with cross-modal attention fusion is an effective strategy for ultrasound-based breast cancer diagnosis.

---


### 96. [What Do Biomedical NER and Entity Linking Benchmarks Measure? A Corpus-Centric Diagnostic Framework](https://arxiv.org/abs/2605.20537)

**<font color=#1a73e8>作者：</font>** Robert Leaman, Rezarta Islamaj, Zhiyong Lu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical named entity recognition (NER) and entity linking (EL) strongly depend on annotated corpora, but the utility of these resources for benchmarking is often assumed rather than characterized. We present a corpus-centric framework for diagnosing benchmark-relevant properties directly from corpus annotations, concept links, train-test splits, document metadata, and terminology mappings. The framework organizes standardized statistics into five families: (1) scale, density and label distribution, (2) lexical and conceptual structure, (3) train-test overlap, (4) metadata composition, and (5) terminology coverage where applicable. Applying the framework to nine corpora spanning diseases, chemicals, and cell types, we find that corpus properties can differ substantially, even when they address the same apparent task. We find differences in the evaluation signal they provide, the generalization demands they impose, the degree of train-test reuse they permit, and the regions of biomedical literature and concept space they represent. These differences suggest that commonly reported corpus statistics can be insufficient to characterize what biomedical NER and EL benchmarks evaluate. We argue that corpus-centric diagnostics provide a practical framework for analyzing corpora beyond surface descriptors such as corpus size and entity type, for identifying potential transfer risks, and for interpreting the scope of benchmarking conclusions. We release the framework as open-source code with an interactive dashboard to support reproducing our analyses and characterizing additional corpora.

---


### 97. [Continual Segmentation under Joint Nonstationarity](https://arxiv.org/abs/2605.20538)

**<font color=#1a73e8>作者：</font>** Prashant Pandey, Himanshu Kumar, Devineni Sri Venkatraya Chowdary 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evolving data streams induce joint nonstationarity in continual semantic segmentation, where semantic classes, input distributions, and supervision availability change simultaneously over time. This setting reflects practical structured prediction systems, yet remains largely unexplored in prior continual learning work, which typically studies these factors in isolation. We formalize continual segmentation under coupled class, domain, and label shifts and investigate learning in heterogeneous dense prediction environments with limited annotations and abundant unlabeled data. To address instability and overfitting arising from few-shot supervision under distribution drift, we introduce gradient-adaptive stabilization, a parameter-wise regularization mechanism implemented via gradient-scaled stochastic perturbations that promotes a principled stability-plasticity tradeoff. We further leverage unlabeled data through semi-supervised learning and introduce prototype anchored supervision that validates pseudo-labels via joint confidence and prototype consistency. Together, these mechanisms enable learning under joint nonstationarity in continual segmentation. Extensive empirical evaluation across class-incremental, domain-incremental, and few-shot regimes demonstrates consistent improvements over prior methods in heterogeneous structured prediction settings. Our results expose fundamental failure modes of existing continual segmentation approaches and provide insight into learning robust dense predictors in dynamically evolving environments.

---


### 98. [OpenSeisML: Open Large-Scale Real Seismic and well-log Dataset for Generative AI](https://arxiv.org/abs/2605.20539)

**<font color=#1a73e8>作者：</font>** Ipsita Bhar, Huseyin Tuna Erdinc, Thales Souza 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The advent of machine learning (ML) and computer vision has significantly accelerated seismic inversion workflows by reducing the computational cost of traditionally expensive iterative methods. However, the development and evaluation of ML methods remain limited by the scarcity of realistic velocity models, as most high-quality data are privately owned by oil and gas companies. To address this gap, we present OpenSeisML, a collection of real seismic datasets designed to support generative AI (Gen-AI) workflows for seismic inversion. The datasets are curated from publicly available surveys in the UK National Data Repository (NDR). When seismic volumes are in the time domain and wells are in depth, a time-to-depth conversion is required. We use checkshot data to establish the time-depth relationship and construct a velocity model through interpolation for accurate conversion of post-stack seismic data. Here, we present an automated data curation pipeline that enables seismic data preparation while ensuring reproducibility. The objective is to train a generative model that captures the statistical distribution of subsurface properties, enabling the synthesis of multiple statistically consistent realizations for uncertainty quantification which can act as a prior for seismic inversion.

---


### 99. [Uncertainty-Guided Conservative Propagation for Structured Inference in Vessel Segmentation](https://arxiv.org/abs/2605.20543)

**<font color=#1a73e8>作者：</font>** Huan Huang, Michele Esposito, Chen Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate vessel segmentation is essential for medical image analysis, yet remains challenging due to complex vascular patterns and imaging ambiguity. Most deep models rely on single-pass prediction, limiting their ability to refine uncertain or disconnected regions during inference. To address this limitation, we propose Uncertainty-Guided Conservative Propagation (UGCP), a general plug-in module for vessel segmentation. Instead of directly using a one-shot output as the final prediction, UGCP performs a small number of logit-space update steps to refine the segmentation through local predictions interaction. Predictive uncertainty guides reliable regions to support ambiguous regions, while structure-aware modulation and source-based stabilization reduce unreliable propagation and excessive drift. The module is differentiable and can be trained end-to-end with different segmentation networks. We evaluate UGCP on four public vessel segmentation datasets covering 2D and 3D tasks, including retinal vessel, coronary artery, and cerebral vessel segmentation. Experiments with convolutional neural network-based and Transformer-based backbones show consistent improvements in Dice similarity coefficient, centerline Dice, and 95th percentile Hausdorff distance. Further analysis demonstrates that UGCP reduces vessel disconnections and improves structural consistency with limited additional computation. The code will be made available at this https URL.

---


### 100. [Detecting Data Exfiltration through I2P Anonymity Networks: A Two-Phase Machine Learning Approach](https://arxiv.org/abs/2605.20546)

**<font color=#1a73e8>作者：</font>** Siddique Abubakr Muntaka, Muntaka Mohammed, Mansuru Mikail Azindo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Invisible Internet Project (I2P) provides strong anonymity through garlic routing and distributed network architecture, making it attractive for legitimate privacy needs. Nevertheless, the same properties can be exploited by malicious actors to steal sensitive information from corporate networks without detection. Current network security measures often fail to detect I2P traffic, and existing literature has focused primarily on protocol-level traffic identification without addressing behavioral threat assessment. This paper proposes a two-stage machine-learning model for I2P traffic analysis using the SafeSurf Darknet 2025 dataset comprising 184,548 network flows. Phase 1 achieved 99.96% accuracy in distinguishing I2P traffic from normal network traffic using a Random Forest classifier, with only 2 false positives among 32,318 normal flows. Phase 2 performed behavioral analysis on traffic identified as I2P, classifying it as either exfiltration or legitimate activity, achieving 91.11% accuracy using XGBoost. The system demonstrates that tree-based ensemble methods substantially outperform deep neural networks and support vector machines for this task. Feature importance analysis indicates that the most discriminative features are packet timing and flow duration. These findings establish that accurate I2P traffic detection and threat prioritization are achievable in operational network environments, enabling security teams to focus resources on high-risk events rather than monitoring all encrypted traffic.

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-352](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
