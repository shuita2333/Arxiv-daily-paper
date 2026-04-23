# 📦 其他研究 | 2026年04月24日

> 本类共 **220** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-220](./part-05.md)

---

### 51. [RareSpot+: A Benchmark, Model, and Active Learning Framework for Small and Rare Wildlife in Aerial Imagery](https://arxiv.org/abs/2604.20000)

**<font color=#1a73e8>作者：</font>** Bowen Zhang, Jesse T. Boulerice, Charvi Mendiratta 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated wildlife monitoring from aerial imagery is vital for conservation but remains limited by two persistent challenges: the difficulty of detecting small, rare species and the high cost of large-scale expert annotation. Prairie dogs exemplify this problem -- they are ecologically important yet appear tiny, sparsely distributed, and visually indistinct from their surroundings, posing a severe challenge for conventional detection models. To overcome these limitations, we present RareSpot+, a detection framework that integrates multi-scale consistency learning, context-aware augmentation, and geospatially guided active learning to address these issues. A novel multi-scale consistency loss aligns intermediate feature maps across detection heads, enhancing localization of small (approx. 30 pixels wide) objects without architectural changes, while context-aware augmentation improves robustness by synthesizing hard, ecologically plausible examples. A geospatial active learning module exploits domain-specific spatial priors linking prairie dogs and burrows, together with test-time augmentation and a meta-uncertainty model, to reduce redundant labeling. On a 2 km^2 aerial dataset, RareSpot+ improves detection over the baseline mAP@50 by +35.2% (absolute +0.13). Cross-dataset tests on HerdNet, AED, and several other wildlife benchmarks demonstrate robust detector-level transferability. The active learning module further boosts prairie dog AP by 14.5% using an annotation budget of just 1.7% of the unlabeled tiles. Beyond detection, RareSpot+ enables spatial ecological analyses such as clustering and co-occurrence, linking vision-based detection with quantitative ecology.

---


### 52. [From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents](https://arxiv.org/abs/2604.20006)

**<font color=#1a73e8>作者：</font>** Md Nayem Uddin, Kumar Shubham, Eduardo Blanco 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized agents that interact with users over long periods must maintain persistent memory across sessions and update it as circumstances change. However, existing benchmarks predominantly frame long-term memory evaluation as fact retrieval from past conversations, providing limited insight into agents' ability to consolidate memory over time or handle frequent knowledge updates. We introduce Memora, a long-term memory benchmark spanning weeks to months long user conversations. The benchmark evaluates three memory-grounded tasks: remembering, reasoning, and recommending. To ensure data quality, we employ automated memory-grounding checks and human evaluation. We further introduce Forgetting-Aware Memory Accuracy (FAMA), a metric that penalizes reliance on obsolete or invalidated memory when evaluating long-term memory. Evaluations of four LLMs and six memory agents reveal frequent reuse of invalid memories and failures to reconcile evolving memories. Memory agents offer marginal improvements, exposing shortcomings in long-term memory for personalized agents.

---


### 53. [Multi-Objective Reinforcement Learning for Generating Covalent Inhibitor Candidates](https://arxiv.org/abs/2604.20019)

**<font color=#1a73e8>作者：</font>** Renee Gil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rational design of covalent inhibitors requires simultaneously optimizing multiple properties, such as binding affinity, target selectivity, or electrophilic reactivity. This presents a multi-objective problem not easily addressed by screening alone. Here we present a machine learning pipeline for generating covalent inhibitor candidates using multi-objective reinforcement learning (RL), applied to two targets: epidermal growth factor receptor (EGFR) and acetylcholinesterase (ACHE). A SMILES-based pretrained LSTM serves as the generative model, optimized via policy gradient RL with Pareto crowding distance to balance competing scoring functions including synthetic accessibility, predicted covalent activity, residue affinity, and an approximated docking score. The pipeline rediscovers known covalent inhibitors at rates of up to 0.50% (EGFR) and 0.74% (ACHE) in 10,000-structure runs, with candidate structures achieving warhead-to-residue distances as short as 5.5 angstrom (EGFR) and 3.2 angstrom (ACHE) after further docking-based screening. More notably, the pipeline spontaneously generates structures bearing warhead motifs absent from the training data - including allenes, 3-oxo-$\beta$-sultams, and $\alpha$-methylene-$\beta$-lactones - all of which have independent literature support as covalent warheads. These results suggest that RL-guided generation can explore covalent chemical space beyond its training distribution, and may be useful as a tool for medicinal chemists working on covalent drug discovery.

---


### 54. [Potentials and Pitfalls of Applying Federated Learning in Hardware Assurance](https://arxiv.org/abs/2604.20020)

**<font color=#1a73e8>作者：</font>** Gijung Lee, Wavid Bowman, Olivia Dizon-Paradis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As microelectronics flourish and outsourcing of the design and manufacturing stages of integrated circuits (ICs) and printed circuit boards (PCBs) becomes the norm, microelectronics stakeholders must also confront a new wave of security challenges, including the threats posed by hardware Trojans, counterfeit electronics, and reverse engineering attacks. Traditional detection and prevention methods like testing and side-channel analysis have limitations in reliability and scalability. Automated reverse engineering by deep learning (DL) models is a foolproof approach to hardware assurance, but faces challenges due to limited data. By pooling data from different stakeholders (competitors in industry, governments, etc.), DL models can be more effectively trained but privacy of intellectual property (IP) is a significant concern. Federated Learning (FL) has been proposed as a potential alternative allowing for the collaborative training of a DL model without sharing raw data. While FL has been widely used in healthcare, IoT, and finance, its application in hardware assurance remains underexplored. This study investigates, for the first time, FL-based DL for hardware assurance, demonstrating that FL outperforms single-client centralized learning in segmentation tasks for reverse engineering. Our results show that increasing the number of clients improves FL performance by collaboratively training the model with more data. However, and more importantly, a major pitfall of FL is also exposed -- it remains vulnerable to gradient inversion attacks. We show that SEM images used in FL can be recovered by attackers, which would therefore expose the sensitive and proprietary IPs that FL was supposed to protect. We highlight these privacy risks and also suggest future research directions to improve security and effectiveness in hardware assurance.

---


### 55. [Replicable Bandits with UCB based Exploration](https://arxiv.org/abs/2604.20024)

**<font color=#1a73e8>作者：</font>** Rohan Deb, Udaya Ghai, Karan Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study replicable algorithms for stochastic multi-armed bandits (MAB) and linear bandits with UCB (Upper Confidence Bound) based exploration. A bandit algorithm is $\rho$-replicable if two executions using shared internal randomness but independent reward realizations, produce the same action sequence with probability at least $1-\rho$. Prior work is primarily elimination-based and, in linear bandits with infinitely many actions, relies on discretization, leading to suboptimal dependence on the dimension $d$ and $\rho$. We develop optimistic alternatives for both settings. For stochastic multi-armed bandits, we propose RepUCB, a replicable batched UCB algorithm and show that it attains a regret $O\!\left(\frac{K^2\log^2 T}{\rho^2}\sum_{a:\Delta_a>0}\left(\Delta_a+\frac{\log(KT\log T)}{\Delta_a}\right)\right)$. For stochastic linear bandits, we first introduce RepRidge, a replicable ridge regression estimator that satisfies both a confidence guarantee and a $\rho$-replicability guarantee. Beyond its role in our bandit algorithm, this estimator and its guarantees may also be of independent interest in other statistical estimation settings. We then use RepRidge to design RepLinUCB, a replicable optimistic algorithm for stochastic linear bandits, and show that its regret is bounded by $\widetilde{O}\!\big(\big(d+\frac{d^3}{\rho}\big)\sqrt{T}\big)$. This improves the best prior regret guarantee by a factor of $O(d/\rho)$, showing that our optimistic algorithm can substantially reduce the price of replicability.

---


### 56. [Investigation of cardinality classification for bacterial colony counting using explainable artificial intelligence](https://arxiv.org/abs/2604.20026)

**<font color=#1a73e8>作者：</font>** Minghua Zheng, Na Helian, Peter C. R. Lane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic bacterial colony counting is a highly sought-after technology in modern biological laboratories because it eliminates manual counting effort. Previous work has observed that MicrobiaNet, currently the best-performing cardinality classification model for colony counting, has difficulty distinguishing colonies of three or more individuals. However, it is unclear if this is due to properties of the data together with inherent characteristics of the MicrobiaNet model. By analysing MicrobiaNet with explainable artificial intelligence (XAI), we demonstrate that XAI can provide insights into how data properties constrain cardinality classification performance in colony counting. Our results show that high visual similarity across classes is the key issue hindering further performance improvement, revising prior assertions about MicrobiaNet. These findings suggest future work should focus on models that explicitly incorporate visual similarity or explore density estimation approaches, with broader implications for neural network classifiers trained on imbalanced datasets.

---


### 57. [Learning to count small and clustered objects with application to bacterial colonies](https://arxiv.org/abs/2604.20030)

**<font color=#1a73e8>作者：</font>** Minghua Zheng, Na Helian, Peter C. R. Lane 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated bacterial colony counting from images is an important technique to obtain data required for the development of vaccines and antibiotics. However, bacterial colonies present unique machine vision challenges that affect counting, including (1) small physical size, (2) object clustering, (3) high data annotation cost, and (4) limited cross-species generalisation. While FamNet is an established object counting technique effective for clustered objects and costly data annotation, its effectiveness for small colony sizes and cross-species generalisation remains unknown. To address the first three challenges, we propose ACFamNet, an extension of FamNet that handles small and clustered objects using a novel region of interest pooling with alignment and optimised feature engineering. To address all four challenges above, we introduce ACFamNet Pro, which augments ACFamNet with multi-head attention and residual connections, enabling dynamic weighting of objects and improved gradient flow. Experiments show that ACFamNet Pro achieves a mean normalised absolute error (MNAE) of 9.64% under 5-fold cross-validation, outperforming ACFamNet and FamNet by 2.23% and 12.71%, respectively.

---


### 58. [FluSplat: Sparse-View 3D Editing without Test-Time Optimization](https://arxiv.org/abs/2604.20038)

**<font color=#1a73e8>作者：</font>** Haitao Huang, Shin-Fang Chng, Huangying Zhan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in text-guided image editing and 3D Gaussian Splatting (3DGS) have enabled high-quality 3D scene manipulation. However, existing pipelines rely on iterative edit-and-fit optimization at test time, alternating between 2D diffusion editing and 3D reconstruction. This process is computationally expensive, scene-specific, and prone to cross-view inconsistencies.
We propose a feed-forward framework for cross-view consistent 3D scene editing from sparse views. Instead of enforcing consistency through iterative 3D refinement, we introduce a cross-view regularization scheme in the image domain during training. By jointly supervising multi-view edits with geometric alignment constraints, our model produces view-consistent results without per-scene optimization at inference. The edited views are then lifted into 3D via a feedforward 3DGS model, yielding a coherent 3DGS representation in a single forward pass.
Experiments demonstrate competitive editing fidelity and substantially improved cross-view consistency compared to optimization-based methods, while reducing inference time by orders of magnitude.

---


### 59. [Normalizing Flows with Iterative Denoising](https://arxiv.org/abs/2604.20041)

**<font color=#1a73e8>作者：</font>** Tianrong Chen, Jiatao Gu, David Berthelot 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Normalizing Flows (NFs) are a classical family of likelihood-based methods that have received revived attention. Recent efforts such as TARFlow have shown that
NFs are capable of achieving promising performance on image modeling tasks, making them viable alternatives to other methods such as diffusion models.
In this work, we further advance the state of Normalizing Flow generative models by introducing iterative TARFlow (iTARFlow). Unlike diffusion models, iTARFlow maintains a fully end-to-end, likelihood-based objective during training. During sampling, it performs autoregressive generation followed by an iterative denoising procedure inspired by diffusion-style methods. Through extensive experiments, we show that iTARFlow achieves competitive performance across ImageNet resolutions of 64, 128, and 256 pixels, demonstrating its potential as a strong generative model and advancing the frontier of Normalizing Flows. In addition, we analyze the characteristic artifacts produced by iTARFlow, offering insights that may shed light on future improvements. Code is available at this https URL.

---


### 60. [Gaussians on a Diet: High-Quality Memory-Bounded 3D Gaussian Splatting Training](https://arxiv.org/abs/2604.20046)

**<font color=#1a73e8>作者：</font>** Yangming Zhang, Jian Xu, Kunxiong Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has revolutionized novel view synthesis with high-quality rendering through continuous aggregations of millions of 3D Gaussian primitives. However, it suffers from a substantial memory footprint, particularly during training due to uncontrolled densification, posing a critical bottleneck for deployment on memory-constrained edge devices. While existing methods prune redundant Gaussians post-training, they fail to address the peak memory spikes caused by the abrupt growth of Gaussians early in the training process. To solve the training memory consumption problem, we propose a systematic memory-bounded training framework that dynamically optimizes Gaussians through iterative growth and pruning. In other words, the proposed framework alternates between incremental pruning of low-impact Gaussians and strategic growing of new primitives with an adaptive Gaussian compensation, maintaining a near-constant low memory usage while progressively refining rendering fidelity. We comprehensively evaluate the proposed training framework on various real-world datasets under strict memory constraints, showing significant improvements over existing state-of-the-art methods. Particularly, our proposed method practically enables memory-efficient 3DGS training on NVIDIA Jetson AGX Xavier, achieving similar visual quality with up to 80% lower peak training memory consumption than the original 3DGS.

---


### 61. [PASTA: A Patch-Agnostic Twofold-Stealthy Backdoor Attack on Vision Transformers](https://arxiv.org/abs/2604.20047)

**<font color=#1a73e8>作者：</font>** Dazhuang Liu, Yanqi Qiao, Rui Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) have achieved remarkable success across vision tasks, yet recent studies show they remain vulnerable to backdoor attacks. Existing patch-wise attacks typically assume a single fixed trigger location during inference to maximize trigger attention. However, they overlook the self-attention mechanism in ViTs, which captures long-range dependencies across patches. In this work, we observe that a patch-wise trigger can achieve high attack effectiveness when activating backdoors across neighboring patches, a phenomenon we term the Trigger Radiating Effect (TRE). We further find that inter-patch trigger insertion during training can synergistically enhance TRE compared to single-patch insertion. Prior ViT-specific attacks that maximize trigger attention often sacrifice visual and attention stealthiness, making them detectable.
Based on these insights, we propose PASTA, a twofold stealthy patch-wise backdoor attack in both pixel and attention domains. PASTA enables backdoor activation when the trigger is placed at arbitrary patches during inference. To achieve this, we introduce a multi-location trigger insertion strategy to enhance TRE. However, preserving stealthiness while maintaining strong TRE is challenging, as TRE is weakened under stealthy constraints. We therefore formulate a bi-level optimization problem and propose an adaptive backdoor learning framework, where the model and trigger iteratively adapt to each other to avoid local optima. Extensive experiments show that PASTA achieves 99.13% attack success rate across arbitrary patches on average, while significantly improving visual and attention stealthiness (144.43x and 18.68x) and robustness (2.79x) against state-of-the-art ViT defenses across four datasets, outperforming CNN- and ViT-based baselines.

---


### 62. [From Fuzzy to Formal: Scaling Hospital Quality Improvement with AI](https://arxiv.org/abs/2604.20055)

**<font color=#1a73e8>作者：</font>** Patrick Vossler, Jean Feng, Venkat Sivaraman 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hospital Quality Improvement (QI) plays a critical role in optimizing healthcare delivery by translating high-level hospital goals into actionable solutions. A critical step of QI is to identify the key modifiable contributing factors, a process we call QI factor discovery, typically through expert-driven semi-structured qualitative tools like fishbone diagrams, chart reviews, and Lean Healthcare methods. AI has the potential to transform and accelerate QI factor discovery, which is traditionally time- and resource-intensive and limited in reproducibility and auditability. Nevertheless, current AI alignment methods assume the task is well-defined, whereas QI factor discovery is an exploratory, fuzzy, and iterative sense-making process that relies on complex implicit expert judgments. To design an AI pipeline that formalizes the QI process while preserving its exploratory components, we propose viewing the task as learning not only LLM prompts but also the overarching natural-language specifications. In particular, we map QI factor discovery to steps of the classical AI/ML development process (problem formalization, model learning, and model validation) where the specifications are tunable hyperparameters. Domain experts and AI agents iteratively refine both the overarching specifications and AI pipeline until AI extractions are concordant with expert annotations and aligned with clinical objectives. We applied this "Human-AI Spec-Solution Co-optimization" framework at an urban safety-net hospital to identify factors driving prolonged length of stay and unplanned 30-day readmissions. The resulting AI-for-QI pipelines achieved $\ge 70\%$ concordance with expert annotations. Compared to prior manual Lean analyses, the AI pipeline was substantially more efficient, recovered previous findings, surfaced new modifiable factors, and produced auditable reasoning traces.

---


### 63. [Federated Learning over Blockchain-Enabled Cloud Infrastructure](https://arxiv.org/abs/2604.20062)

**<font color=#1a73e8>作者：</font>** Saloni Garg, Amit Sagtani, Kamal Kant Hiran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rise of IoT devices and the uptake of cloud computing have informed a new era of data-driven intelligence. Traditional centralized machine learning models that require a large volume of data to be stored in a single location have therefore become more susceptible to data breaches, privacy violations, and regulatory non-compliance. This report presents a thorough examination of the merging of Federated Learning (FL) and blockchain technology in a cloud-edge setting, demonstrating it as an effective solution to the stated concerns. We are proposing a detailed four-dimensional architectural categorization that meticulously assesses coordination frameworks, consensus algorithms, data storage practices, and trust models that are significant to these integrated systems. The manuscript presents a comprehensive comparative examination of two cutting-edge frameworks: the Multi-Objectives Reinforcement Federated Learning Blockchain (MORFLB), which is designed for intelligent transportation systems, and the Federated Blockchain-IoT Framework for Sustainable Healthcare Systems (FBCI-SHS), elucidating their distinctive contributions and inherent limitations. Lastly, we engage in a thorough evaluation of the literature that integrates a comparative perspective on current frameworks to discern the singular nature of this research within existing knowledge systems. The manuscript culminates in delineating the principal challenges and offering a strategic framework for prospective research trajectories, emphasizing the advancement of adaptive, resilient, and standardized BCFL systems across diverse application domains.

---


### 64. [Auditing and Controlling AI Agent Actions in Spreadsheets](https://arxiv.org/abs/2604.20070)

**<font color=#1a73e8>作者：</font>** Sadra Sabouri, Zeinabsadat Saghi, Run Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Advances in AI agent capabilities have outpaced users' ability to meaningfully oversee their execution. AI agents can perform sophisticated, multi-step knowledge work autonomously from start to finish, yet this process remains effectively inaccessible during execution, often buried within large volumes of intermediate reasoning and outputs: by the time users receive the output, all underlying decisions have already been made without their involvement. This lack of transparency leaves users unable to examine the agent's assumptions, identify errors before they propagate, or redirect execution when it deviates from their intent. The stakes are particularly high in spreadsheet environments, where process and artifact are inseparable. Each decision the agent makes is recorded directly in cells that belong to and reflect on the user. We introduce Pista, a spreadsheet AI agent that decomposes execution into auditable, controllable actions, providing users with visibility into the agent's decision-making process and the capacity to intervene at each step. A formative study (N = 8) and a within-subjects summative evaluation (N = 16) comparing Pista to a baseline agent demonstrated that active participation in execution influenced not only task outcomes but also users' comprehension of the task, their perception of the agent, and their sense of role within the workflow. Users identified their own intent reflected in the agent's actions, detected errors that post-hoc review would have failed to surface, and reported a sense of co-ownership over the resulting output. These findings indicate that meaningful human oversight of AI agents in knowledge work requires not improved post-hoc review mechanisms, but active participation in decisions as they are made.

---


### 65. [Enhancing immersion in Virtual Reality sports through Physical Interactions](https://arxiv.org/abs/2604.20071)

**<font color=#1a73e8>作者：</font>** Arka Majhi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent discoveries in VR have opened up scope for designing physical tools and controllers to enhance immersion, through perceived reality. In a virtually simulated sports scenario it is challenging to immerse user because most of the available controllers are unable to bridge the user experience in the real world to the actions in the virtual world. My research is to identify HCI problems in existing VR controllers, design a physical controller prototype with realistic tangible mapping, trying to solve the existing problems and evaluate it in a designed VR game for skating. Its immersiveness would be graded on Likert scale on parameters like perceived interactivity and reality, spatial presence and enjoyment. The evaluation will be done after trial runs and feedback sessions by playing the game with the designed controller and comparing it with ones available in the market. The findings will help people understand what all parameters we should consider while designing futuristic controllers, customized for a particular sport.

---


### 66. [Maximum Entropy Semi-Supervised Inverse Reinforcement Learning](https://arxiv.org/abs/2604.20074)

**<font color=#1a73e8>作者：</font>** Julien Audiffren, Michal Valko, Alessandro Lazaric 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A popular approach to apprenticeship learning (AL) is to formulate it as an inverse reinforcement learning (IRL) problem. The MaxEnt-IRL algorithm successfully integrates the maximum entropy principle into IRL and unlike its predecessors, it resolves the ambiguity arising from the fact that a possibly large number of policies could match the expert's behavior. In this paper, we study an AL setting in which in addition to the expert's trajectories, a number of unsupervised trajectories is available. We introduce MESSI, a novel algorithm that combines MaxEnt-IRL with principles coming from semi-supervised learning. In particular, MESSI integrates the unsupervised data into the MaxEnt-IRL framework using a pairwise penalty on trajectories. Empirical results in a highway driving and grid-world problems indicate that MESSI is able to take advantage of the unsupervised trajectories and improve the performance of MaxEnt-IRL.

---


### 67. [Improved large-scale graph learning through ridge spectral sparsification](https://arxiv.org/abs/2604.20078)

**<font color=#1a73e8>作者：</font>** Daniele Calandriello, Ioannis Koutis, Alessandro Lazaric 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-based techniques and spectral graph theory have enriched the field of machine learning with a variety of critical advances. A central object in the analysis is the graph Laplacian L, which encodes the structure of the graph. We consider the problem of learning over this Laplacian in a distributed streaming setting, where new edges of the graph are observed in real time by a network of workers. In this setting, it is hard to learn quickly or approximately while keeping a distributed representation of L. To address this challenge, we present a novel algorithm, GSQUEAK, which efficiently sparsifies the Laplacian by maintaining a small subset of effective resistances. We show that our algorithm produces sparsifiers with strong spectral approximation guarantees, all while processing edges in a single pass and in a distributed fashion.

---


### 68. [Concept Graph Convolutions: Message Passing in the Concept Space](https://arxiv.org/abs/2604.20082)

**<font color=#1a73e8>作者：</font>** Lucie Charlotte Magister, Pietro Lio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The trust in the predictions of Graph Neural Networks is limited by their opaque reasoning process. Prior methods have tried to explain graph networks via concept-based explanations extracted from the latent representations obtained after message passing. However, these explanations fall short of explaining the message passing process itself. To this aim, we propose the Concept Graph Convolution, the first graph convolution designed to operate on node-level concepts for improved interpretability. The proposed convolutional layer performs message passing on a combination of raw and concept representations using structural and attention-based edge weights. We also propose a pure variant of the convolution, only operating in the concept space. Our results show that the Concept Graph Convolution allows to obtain competitive task accuracy, while enabling an increased insight into the evolution of concepts across convolutional steps.

---


### 69. [Energy-Based Open-Set Active Learning for Object Classification](https://arxiv.org/abs/2604.20083)

**<font color=#1a73e8>作者：</font>** Zongyao Lyu, William J. Beksi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active learning (AL) has emerged as a crucial methodology for minimizing labeling costs in deep learning by selecting the most valuable samples from a pool of unlabeled data for annotation. Traditional AL operates under a closed-set assumption, where all classes in the dataset are known and consistent. However, real-world scenarios often present open-set conditions in which unlabeled data contains both known and unknown classes. In such environments, standard AL techniques struggle. They can mistakenly query samples from unknown categories, leading to inefficient use of annotation budgets. In this paper, we propose a novel dual-stage energy-based framework for open-set AL. Our method employs two specialized energy-based models (EBMs). The first, an energy-based known/unknown separator, filters out samples likely to belong to unknown classes. The second, an energy-based sample scorer, assesses the informativeness of the filtered known samples. Using the energy landscape, our models distinguish between data points from known and unknown classes in the unlabeled pool by assigning lower energy to known samples and higher energy to unknown samples, ensuring that only samples from classes of interest are selected for labeling. By integrating these components, our approach ensures efficient and targeted sample selection, maximizing learning impact in each iteration. Experiments on 2D (CIFAR-10, CIFAR-100, TinyImageNet) and 3D (ModelNet40) object classification benchmarks demonstrates that our framework outperforms existing approaches, achieving superior annotation efficiency and classification performance in open-set environments.

---


### 70. [SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks](https://arxiv.org/abs/2604.20087)

**<font color=#1a73e8>作者：</font>** Shanshan Zhong, Yi Lu, Jingjie Ning 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skills have become the de facto way to enable LLM agents to perform complex real-world tasks with customized instructions, workflows, and tools, but how to learn them automatically and effectively remains unclear. We introduce SkillLearnBench, the first benchmark for evaluating continual skill learning methods, comprising 20 verified, skill-dependent tasks across 15 sub-domains derived from a real-world skill taxonomy , evaluated at three levels: skill quality, execution trajectory, and task outcome. Using this benchmark, we evaluate recent continual learning techniques, those leveraging one-shot, self/teacher feedback, and skill creator to generate skills from agent experiences. We find that all continual learning methods improve over the no-skill baseline, yet consistent gains remain elusive: no method leads across all tasks and LLMs, and scaling to stronger LLMs does not reliably help. Continual learning improves tasks with clear, reusable workflows but struggles on open-ended tasks, and using stronger LLM backbones does not consistently produce better skills. Our analysis also revealed that multiple iterations in continual learning facilitate genuine improvement via external feedback, whereas self-feedback alone induces recursive drift. Our data and code are open-source at this https URL to enable further studies of automatic skill generation and continual learning techniques.

---


### 71. [Less Languages, Less Tokens: An Efficient Unified Logic Cross-lingual Chain-of-Thought Reasoning Framework](https://arxiv.org/abs/2604.20090)

**<font color=#1a73e8>作者：</font>** Chenyuan Zhang, Qiguang Chen, Xie Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual chain-of-thought (XCoT) with self-consistency markedly enhances multilingual reasoning, yet existing methods remain costly due to extensive sampling of full trajectories across languages. Moreover, multilingual LLM representations vary strongly by language, hindering direct feature comparisons and effective pruning. Motivated by this, we introduce UL-XCoT, the first efficient unified logic cross-lingual reasoning framework that minimizes redundancy in token usage and latency, yielding the greatest efficiency under limited sampling budgets during inference. Specifically, UL-XCoT (1) achieves less languages by selecting, per query, a small candidate language set in a language-invariant unified logic space, (2) enables less tokens by monitoring logic-space trajectory dynamics during decoding to prune low-quality reasoning paths, and (3) aggregates the remaining high-quality trajectories via voting. Experiments on PolyMath across 18 languages and MMLU-ProX-Lite across 29 languages with DeepSeek-R1-DistillQwen-7B demonstrate that UL-XCoT achieves competitive accuracy while sharply cutting over 50% decoding token cost versus prior sampling baselines. UL-XCoT also delivers more stable gains on low-resource languages, underscoring consistently superior robustness where standard XCoT self-consistency method fails.

---


### 72. [Heterogeneous Layered Structures Can Modulate Human Softness Perception](https://arxiv.org/abs/2604.20092)

**<font color=#1a73e8>作者：</font>** Yuno Higuchi, Yosuke Iwashita, Yuji Ohgi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human softness perception in haptics has mainly been studied using mechanically homogeneous objects, despite the fact that many real-world objects exhibit heterogeneous layered structures with nonuniform stiffness. This study examined how layered heterogeneity modulates haptic softness perception. Sixteen lattice-structured stimuli were fabricated by 3D printing, with the stiffness of the upper four layers systematically varied while the bottom two layers remained fixed. Twenty-two participants evaluated the softness of the stimuli in a psychophysical task, and compression tests were conducted to quantify their mechanical properties. Perceived softness was significantly predicted by displacement under load, however, perceptual ranking did not fully coincide with the physical ranking. Linear mixed-effects analyses showed that the softness of the outermost layer had the greatest impact on the perceived softness. Perceived softness also increased as the number of soft subsurface layers increased, although this contribution decreased with depth. Layers 2 and 3 showed significant effects, whereas Layer 4 did not. These findings suggest that haptic softness perception depends not only on the overall stiffness but also on the depth-dependent distribution of compliance within layered structures.

---


### 73. [FurnSet: Exploiting Repeats for 3D Scene Reconstruction](https://arxiv.org/abs/2604.20093)

**<font color=#1a73e8>作者：</font>** Paul Dobre, Xin Wang, Hongzhou Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-view 3D scene reconstruction involves inferring both object geometry and spatial layout. Existing methods typically reconstruct objects independently or rely on implicit scene context, failing to exploit the repeated instances commonly present in realworld scenes. We propose FurnSet, a framework that explicitly identifies and leverages repeated object instances to improve reconstruction. Our method introduces per-object CLS tokens and a set-aware self-attention mechanism that groups identical instances and aggregates complementary observations across them, enabling joint reconstruction. We further combine scene-level and object-level conditioning to guide object reconstruction, followed by layout optimization using object point clouds with 3D and 2D projection losses for scene alignment. Experiments on 3D-Future and 3D-Front demonstrate improved scene reconstruction quality, highlighting the effectiveness of exploiting repetition for robust 3D scene reconstruction.

---


### 74. [Learning to Solve the Quadratic Assignment Problem with Warm-Started MCMC Finetuning](https://arxiv.org/abs/2604.20109)

**<font color=#1a73e8>作者：</font>** Yicheng Pan, Ruisong Zhou, Haijun Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quadratic assignment problem (QAP) is a fundamental NP-hard task that poses significant challenges for both traditional heuristics and modern learning-based solvers. Existing QAP solvers still struggle to achieve consistently competitive performance across structurally diverse real-world instances. To bridge this performance gap, we propose PLMA, an innovative permutation learning framework. PLMA features an efficient warm-started MCMC finetuning procedure to enhance deployment-time performance, leveraging short Markov chains to anchor the adaptation to the promising regions previously explored. For rapid exploration via MCMC over the permutation space, we design an additive energy-based model (EBM) that enables an $O(1)$-time 2-swap Metropolis-Hastings sampling step. Moreover, the neural network used to parameterize the EBM incorporates a scalable and flexible cross-graph attention mechanism to model interactions between facilities and locations in the QAP. Extensive experiments demonstrate that PLMA consistently outperforms state-of-the-art baselines across various benchmarks. In particular, PLMA achieves a near-zero average optimality gap on QAPLIB, exhibits remarkably superior robustness on the notoriously difficult Taixxeyy instances, and also serves as an effective QAP solver in bandwidth minimization.

---


### 75. [Meta Additive Model: Interpretable Sparse Learning With Auto Weighting](https://arxiv.org/abs/2604.20111)

**<font color=#1a73e8>作者：</font>** Xuelin Zhang, Xinyue Liu, Lingjuan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse additive models have attracted much attention in high-dimensional data analysis due to their flexible representation and strong interpretability. However, most existing models are limited to single-level learning under the mean-squared error criterion, whose empirical performance can degrade significantly in the presence of complex noise, such as non-Gaussian perturbations, outliers, noisy labels, and imbalanced categories. The sample reweighting strategy is widely used to reduce the model's sensitivity to atypical data; however, it typically requires prespecifying the weighting functions and manually selecting additional hyperparameters. To address this issue, we propose a new meta additive model (MAM) based on the bilevel optimization framework, which learns data-driven weighting of individual losses by parameterizing the weighting function via an MLP trained on meta data. MAM is capable of a variety of learning tasks, including variable selection, robust regression estimation, and imbalanced classification. Theoretically, MAM provides guarantees on convergence in computation, algorithmic generalization, and variable selection consistency under mild conditions. Empirically, MAM outperforms several state-of-the-art additive models on both synthetic and real-world data under various data corruptions.

---


### 76. [On the Stability and Generalization of First-order Bilevel Minimax Optimization](https://arxiv.org/abs/2604.20115)

**<font color=#1a73e8>作者：</font>** Xuelin Zhang, Peipei Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bilevel optimization and bilevel minimax optimization have recently emerged as unifying frameworks for a range of machine-learning tasks, including hyperparameter optimization and reinforcement learning. The existing literature focuses on empirical efficiency and convergence guarantees, leaving a critical theoretical gap in understanding how well these algorithms generalize. To bridge this gap, we provide the first systematic generalization analysis for first-order gradient-based bilevel minimax solvers with lower-level minimax problems. Specifically, by leveraging algorithmic stability arguments, we derive fine-grained generalization bounds for three representative algorithms, including single-timescale stochastic gradient descent-ascent, and two variants of two-timescale stochastic gradient descent-ascent. Our results reveal a precise trade-off among algorithmic stability, generalization gaps, and practical settings. Furthermore, extensive empirical evaluations corroborate our theoretical insights on realistic optimization tasks with bilevel minimax structures.

---


### 77. [To Know is to Construct: Schema-Constrained Generation for Agent Memory](https://arxiv.org/abs/2604.20117)

**<font color=#1a73e8>作者：</font>** Lei Zheng, Weinan Song, Daili Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Constructivist epistemology argues that knowledge is actively constructed rather than passively copied. Despite the generative nature of Large Language Models (LLMs), most existing agent memory systems are still based on dense retrieval. However, dense retrieval heavily relies on semantic overlap or entity matching within sentences. Consequently, embeddings often fail to distinguish instances that are semantically similar but contextually distinct, introducing substantial noise by retrieving context-mismatched entries. Conversely, directly employing open-ended generation for memory access risks "Structural Hallucination" where the model generates memory keys that do not exist in the memory, leading to lookup failures. Inspired by this epistemology, we posit that memory is fundamentally organized by cognitive schemas, and valid recall must be a generative process performed within these schematic structures. To realize this, we propose SCG-MEM, a schema-constrained generative memory architecture. SCG-MEM reformulates memory access as Schema-Constrained Generation. By maintaining a dynamic Cognitive Schema, we strictly constrain LLM decoding to generate only valid memory entry keys, providing a formal guarantee against structural hallucinations. To support long-term adaptation, we model memory updates via assimilation (grounding inputs into existing schemas) and accommodation (expanding schemas with novel concepts). Furthermore, we construct an Associative Graph to enable multi-hop reasoning through activation propagation. Experiments on the LoCoMo benchmark show that SCG-MEM substantially improves performance across all categories over retrieval-based baselines.

---


### 78. [Topology-Aware Skeleton Detection via Lighthouse-Guided Structured Inference](https://arxiv.org/abs/2604.20123)

**<font color=#1a73e8>作者：</font>** Daoyong Fu, Xiang Zhang, Zhaohuan Zhan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In natural images, object skeletons are used to represent geometric shapes. However, even slight variations in pose or movement can cause noticeable changes in skeleton structure, increasing the difficulty of detecting the skeleton and often resulting in discontinuous skeletons. Existing methods primarily focus on point-level skeleton point detection and overlook the importance of structural continuity in recovering complete skeletons. To address this issue, we propose Lighthouse-Skel, a topology-aware skeleton detection method via lighthouse-guided structured inference. Specifically, we introduce a dual-branch collaborative detection framework that jointly learns skeleton confidence field and structural anchors, including endpoints and junction points. The spatial distributions learned by the point branch guide the network to focus on topologically vulnerable regions, which improves the accuracy of skeleton detection. Based on the learned skeleton confidence field, we further propose a lighthouse-guided topology completion strategy, which uses detected junction points and breakpoints as lighthouses to reconnect discontinuous skeleton segments along low-cost paths, thereby improving skeleton continuity and structural integrity. Experimental results on four public datasets demonstrate that the proposed method achieves competitive detection accuracy while substantially improving skeleton connectivity and structural integrity.

---


### 79. [Trajectory-Aware Reliability Modeling of Democratic Systems](https://arxiv.org/abs/2604.20127)

**<font color=#1a73e8>作者：</font>** Dmitry Zaytsev, Valentina Kuskova, Michael Coppedge  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Failures in complex systems often emerge through gradual degradation and the propagation of stress across interacting components rather than through isolated shocks. Democratic systems exhibit similar dynamics, where weakening institutions can trigger cascading deterioration in related institutional structures. Traditional reliability and survival models typically estimate failure risk based on the current system state but do not explicitly capture how degradation propagates through institutional networks over time. This paper introduces a trajectory-aware reliability modeling framework based on Dynamic Causal Neural Autoregression (DCNAR). The framework first estimates a causal interaction structure among institutional indicators and then models their joint temporal evolution to generate forward trajectories of system states. Failure risk is defined as the probability that predicted trajectories cross predefined degradation thresholds within a fixed horizon. Using longitudinal institutional indicators, we compare DCNAR-based trajectory risk models with discrete-time hazard and Cox proportional hazards models. Results show that trajectory-aware modeling consistently outperforms Cox models and improves risk prediction for several propagation-driven institutional failures. These findings highlight the importance of modeling dynamic system interactions for reliability analysis and early detection of systemic degradation.

---


### 80. [Semi-Supervised Flow Matching for Mosaiced and Panchromatic Fusion Imaging](https://arxiv.org/abs/2604.20128)

**<font color=#1a73e8>作者：</font>** Peiming Luo, Nan Wang, Litong Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fusing a low resolution (LR) mosaiced hyperspectral image (HSI) with a high resolution (HR) panchromatic (PAN) image offers a promising avenue for video-rate HR-HSI imaging via single-shot acquisition, yet its severely ill-posed nature remains a significant challenge. In this work, we propose a novel semi-supervised flow matching framework for mosaiced and PAN image fusion. Unlike previous diffusion-based approaches constrained by specific protocols or handcrafted assumptions, our method seamlessly integrates an unsupervised scheme with flow matching, resulting in a generalizable and efficient generative framework. Specifically, our method follows a two-stage training pipeline. First, we pretrain an unsupervised prior network to produce an initial pseudo HR-HSI. Building on this, we then train a conditional flow matching model to generate the target HR-HSI, introducing a random voting mechanism that iteratively refines the initial HR-HSI estimate, enabling robust and effective fusion. During inference, we employ a conflict-free gradient guidance strategy that ensures spectrally and spatially consistent HR-HSI reconstruction. Experiments on multiple benchmark datasets demonstrate that our method achieves superior quantitative and qualitative performance by a significant margin compared to representative baselines. Beyond mosaiced and PAN fusion, our approach provides a flexible generative framework that can be readily extended to other image fusion tasks and integrated with unsupervised or blind image restoration algorithms.

---


### 81. [A Delta-Aware Orchestration Framework for Scalable Multi-Agent Edge Computing](https://arxiv.org/abs/2604.20129)

**<font color=#1a73e8>作者：</font>** Samaresh Kumar Singh, Joyjit Roy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Synergistic Collapse occurs when scaling beyond 100 agents causes superlinear performance degradation that individual optimizations cannot prevent. We observe this collapse with 150 cameras in Smart City deployment using MADDPG, where Deadline Satisfaction drops from 78% to 34%, producing approximately $180,000 in annual cost overruns. Prior work has addressed each contributing factor in isolation: exponential action-space growth, computational redundancy among spatially adjacent agents, and task-agnostic hardware scheduling. None has examined how these three factors interact and amplify each other. We present DAOEF (Delta-Aware Orchestration for Edge Federations), a framework that addresses all three simultaneously through: (1) Differential Neural Caching, which stores intermediate layer activations and computes only the input deltas, achieving 2.1x higher hit ratios (72% vs. 35%) than output-level caching while staying within 2% accuracy loss through empirically calibrated similarity thresholds; (2) Criticality-Based Action Space Pruning, which organizes agents into priority tiers and reduces coordination complexity from O(n2) to O(n log n) with less than 6% optimality loss; and (3) Learned Hardware Affinity Matching, which assigns tasks to their optimal accelerator (GPU, CPU, NPU, or FPGA) to prevent compounding mismatch penalties. Controlled factor-isolation experiments confirm that each mechanism is necessary but insufficient on its own: removing any single mechanism increases latency by more than 40%, validating that the gains are interdependent rather than additive. Across four datasets (100-250 agents) and a 20-device physical testbed, DAOEF achieves a 1.45x multiplicative gain over applying the three mechanisms independently. A 200-agent cloud deployment yields 62% latency reduction (280 ms vs. 735 ms), sub-linear latency growth up to 250 agents.

---


### 82. [Pairing Regularization for Mitigating Many-to-One Collapse in GANs](https://arxiv.org/abs/2604.20130)

**<font color=#1a73e8>作者：</font>** Kuan-Yu Lin, Yu-Chih Huang, Tie Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mode collapse remains a fundamental challenge in training generative adversarial networks (GANs). While existing works have primarily focused on inter-mode collapse, such as mode dropping, intra-mode collapse-where many latent variables map to the same or highly similar outputs-has received significantly less attention. In this work, we propose a pairing regularizer jointly optimized with the generator to mitigate the many-to-one collapse by enforcing local consistency between latent variables and generated samples. We show that the effect of pairing regularization depends on the dominant failure mode of training. In collapse-prone regimes with limited exploration, pairing encourages structured local exploration, leading to improved coverage and higher recall. In contrast, under stabilized training with sufficient exploration, pairing refines the generator's induced data density by discouraging redundant mappings, thereby improving precision without sacrificing recall. Extensive experiments on both toy distributions and real-image benchmarks demonstrate that the proposed regularizer effectively complements existing stabilization techniques by directly addressing intra-mode collapse.

---


### 83. [IMPACT-CYCLE: A Contract-Based Multi-Agent System for Claim-Level Supervisory Correction of Long-Video Semantic Memory](https://arxiv.org/abs/2604.20136)

**<font color=#1a73e8>作者：</font>** Weitong Kong, Di Wen, Kunyu Peng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Correcting errors in long-video understanding is disproportionately costly: existing multimodal pipelines produce opaque, end-to-end outputs that expose no intermediate state for inspection, forcing annotators to revisit raw video and reconstruct temporal logic from scratch. The core bottleneck is not generation quality alone, but the absence of a supervisory interface through which human effort can be proportional to the scope of each error. We present IMPACT-CYCLE, a supervisory multi-agent system that reformulates long-video understanding as iterative claim-level maintenance of a shared semantic memory -- a structured, versioned state encoding typed claims, a claim dependency graph, and a provenance log. Role-specialized agents operating under explicit authority contracts decompose verification into local object-relation correctness, cross-temporal consistency, and global semantic coherence, with corrections confined to structurally dependent claims. When automated evidence is insufficient, the system escalates to human arbitration as the supervisory authority with final override rights; dependency-closure re-verification then ensures correction cost remains proportional to error scope. Experiments on VidOR show substantially improved downstream reasoning (VQA: 0.71 to 0.79) and a 4.8x reduction in human arbitration cost, with workload significantly lower than manual annotation. Code will be released at this https URL.

---


### 84. [Fourier Weak SINDy: Spectral Test Function Selection for Robust Model Identification](https://arxiv.org/abs/2604.20141)

**<font color=#1a73e8>作者：</font>** Zhiheng Chen, Urban Fasel, Anastasia Bizyaeva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Fourier Weak SINDy, a minimal noise-robust and interpretable derivative-free equation learning method that combines weak-form sparse equation learning with spectral density estimation for data-driven test function selection. By using orthogonal sinusoidal test functions inspired by their prevalence in Modulating Function-based system identification, the weak-form sparse regression problem reduces to a regression over Fourier coefficients. Dominant frequencies are then selected via multitaper estimation of the frequency spectrum of the data. This formulation unifies weak-form learning and spectral estimation within a compact and flexible framework. We illustrate the effectiveness of this approach in numerical experiments across multiple chaotic and hyperchaotic ODE benchmarks.

---


### 85. [GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds](https://arxiv.org/abs/2604.20155)

**<font color=#1a73e8>作者：</font>** Ao Gao, Jingyu Gong, Xin Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D Gaussian Splatting (3DGS) has revolutionized real-time rendering, its performance degrades significantly under sparse-view extrapolation, manifesting as severe geometric voids and artifacts. Existing solutions primarily rely on an iterative "Repair-then-Distill" paradigm, which is inherently unstable and prone to overfitting. In this work, we propose GSCompleter, a distillation-free plugin that shifts scene completion to a stable "Generate-then-Register" workflow. Our approach first synthesizes plausible 2D reference images and explicitly lifts them into metric-scale 3D primitives via a robust Stereo-Anchor mechanism. These primitives are then seamlessly integrated into the global context through a novel Ray-Constrained Registration strategy. This shift to a rapid registration paradigm delivers superior 3DGS completion performance across three distinct benchmarks, enhancing the quality and efficiency of various baselines and achieving new SOTA results.

---


### 86. [Temporally Extended Mixture-of-Experts Models](https://arxiv.org/abs/2604.20156)

**<font color=#1a73e8>作者：</font>** Zeyu Shen, Peter Henderson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts models, now popular for scaling capacity at fixed inference speed, switch experts at nearly every token. Once a model outgrows available GPU memory, this churn can render optimizations like offloading and pre-fetching ineffective. We make the case that the options framework in reinforcement learning is a perfect match to tackle this problem, and argue for temporally extended mixture-of-experts layers. Building on the option-critic framework with deliberation costs, we add a controller to each layer that learns when to switch expert sets and which to load. By applying this to gpt-oss-20b with low-rank adapters and a self-distillation reward, our method reduces switch rates from over 50% to below 5% while retaining up to 90% of base-model accuracy on MATH, MMLU, and MMMLU. This shows that even existing pre-trained models can be converted to temporally extended MoEs with lightweight training, with the deliberation cost allowing model trainers to trade off switching rates against capability. We hope this opens a principled path, grounded in the options framework, for memory-efficient serving and continual learning in ever-growing MoE models.

---


### 87. [HumanScore: Benchmarking Human Motions in Generated Videos](https://arxiv.org/abs/2604.20157)

**<font color=#1a73e8>作者：</font>** Yusu Fang, Tiange Xiang, Tian Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in model architectures, compute, and data scale have driven rapid progress in video generation, producing increasingly realistic content. Yet, no prior method systematically measures how faithfully these systems render human bodies and motion dynamics. In this paper, we present HumanScore, a systematic framework to evaluate the quality of human motions in AI-generated videos. HumanScore defines six interpretable metrics spanning kinematic plausibility, temporal stability, and biomechanical consistency, enabling fine-grained diagnosis beyond visual realism alone. Through carefully designed prompts, we elicit a diverse set of movements at varying intensities and evaluate videos generated by thirteen state-of-the-art models. Our analysis reveals consistent gaps between perceptual plausibility and motion biomechanical fidelity, identifies recurrent failure modes (e.g., temporal jitter, anatomically implausible poses, and motion drift), and produces robust model rankings from quantitative and physically meaningful criteria.

---


### 88. [Stateless Decision Memory for Enterprise AI Agents](https://arxiv.org/abs/2604.20158)

**<font color=#1a73e8>作者：</font>** Vasundra Srinivasan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise deployment of long-horizon decision agents in regulated domains (underwriting, claims adjudication, tax examination) is dominated by retrieval-augmented pipelines despite a decade of increasingly sophisticated stateful memory architectures. We argue this reflects a hidden requirement: regulated deployment is load-bearing on four systems properties (deterministic replay, auditable rationale, multi-tenant isolation, statelessness for horizontal scale), and stateful architectures violate them by construction. We propose Deterministic Projection Memory (DPM): an append-only event log plus one task-conditioned projection at decision time. On ten regulated decisioning cases at three memory budgets, DPM matches summarization-based memory at generous budgets and substantially outperforms it when the budget binds: at a 20x compression ratio, DPM improves factual precision by +0.52 (Cohen's h=1.17, p=0.0014) and reasoning coherence by +0.53 (h=1.13, p=0.0034), paired permutation, n=10. DPM is additionally 7-15x faster at binding budgets, making one LLM call at decision time instead of N. A determinism study of 10 replays per case at temperature zero shows both architectures inherit residual API-level nondeterminism, but the asymmetry is structural: DPM exposes one nondeterministic call; summarization exposes N compounding calls. The audit surface follows the same one-versus-N pattern: DPM logs two LLM calls per decision while summarization logs 83-97 on LongHorizon-Bench. We conclude with TAMS, a practitioner heuristic for architecture selection, and a failure analysis of stateful memory under enterprise operating conditions. The contribution is the argument that statelessness is the load-bearing property explaining enterprise's preference for weaker but replayable retrieval pipelines, and that DPM demonstrates this property is attainable without the decisioning penalty retrieval pays.

---


### 89. [SMART: A Spectral Transfer Approach to Multi-Task Learning](https://arxiv.org/abs/2604.20161)

**<font color=#1a73e8>作者：</font>** Boxin Zhao, Mladen Kolar, Jinchi Lv  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-task learning is effective for related applications, but its performance can deteriorate when the target sample size is small. Transfer learning can borrow strength from related studies; yet, many existing methods rely on restrictive bounded-difference assumptions between the source and target models. We propose SMART, a spectral transfer method for multi-task linear regression that instead assumes spectral similarity: the target left and right singular subspaces lie within the corresponding source subspaces and are sparsely aligned with the source singular bases. Such an assumption is natural when studies share latent structures and enables transfer beyond the bounded-difference settings. SMART estimates the target coefficient matrix through structured regularization that incorporates spectral information from a source study. Importantly, it requires only a fitted source model rather than the raw source data, making it useful when data sharing is limited. Although the optimization problem is nonconvex, we develop a practical ADMM-based algorithm. We establish general, non-asymptotic error bounds and a minimax lower bound in the noiseless-source regime. Under additional regularity conditions, these results yield near-minimax Frobenius error rates up to logarithmic factors. Simulations confirm improved estimation accuracy and robustness to negative transfer, and analysis of multi-modal single-cell data demonstrates better predictive performance. The Python implementation of SMART, along with the code to reproduce all experiments in this paper, is publicly available at this https URL.

---


### 90. [Aligning Human-AI-Interaction Trust for Mental Health Support: Survey and Position for Multi-Stakeholders](https://arxiv.org/abs/2604.20166)

**<font color=#1a73e8>作者：</font>** Xin Sun, Yue Su, Yifan Mo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building trustworthy AI systems for mental health support is a shared priority across stakeholders from multiple disciplines. However, "trustworthy" remains loosely defined and inconsistently operationalized. AI research often focuses on technical criteria (e.g., robustness, explainability, and safety), while therapeutic practitioners emphasize therapeutic fidelity (e.g., appropriateness, empathy, and long-term user outcomes). To bridge the fragmented landscape, we propose a three-layer trust framework, covering human-oriented, AI-oriented, and interaction-oriented trust, integrating the viewpoints of key stakeholders (e.g., practitioners, researchers, regulators). Using this framework, we systematically review existing AI-driven research in mental health domain and examine evaluation practices for ``trustworthy'' ranging from automatic metrics to clinically validated approaches. We highlight critical gaps between what NLP currently measures and what real-world mental health contexts require, and outline a research agenda for building socio-technically aligned and genuinely trustworthy AI for mental health support.

---


### 91. [Semantic-Fast-SAM: Efficient Semantic Segmenter](https://arxiv.org/abs/2604.20169)

**<font color=#1a73e8>作者：</font>** Byunghyun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Semantic-Fast-SAM (SFS), a semantic segmentation framework that combines the Fast Segment Anything model with a semantic labeling pipeline to achieve real-time performance without sacrificing accuracy. FastSAM is an efficient CNN-based re-implementation of the Segment Anything Model (SAM) that runs much faster than the original transformer-based SAM. Building upon FastSAM's rapid mask generation, we integrate a Semantic-Segment-Anything (SSA) labeling strategy to assign meaningful categories to each mask. The resulting SFS model produces high-quality semantic segmentation maps at a fraction of the computational cost and memory footprint of the original SAM-based approach. Experiments on Cityscapes and ADE20K benchmarks demonstrate that SFS matches the accuracy of prior SAM-based methods (mIoU ~ 70.33 on Cityscapes and 48.01 on ADE20K) while achieving approximately 20x faster inference than SSA in the closed-set setting. We also show that SFS effectively handles open-vocabulary segmentation by leveraging CLIP-based semantic heads, outperforming recent open-vocabulary models on broad class labeling. This work enables practical real-time semantic segmentation with the "segment-anything" capability, broadening the applicability of foundation segmentation models in robotics scenarios. The implementation is available at this https URL.

---


### 92. [Cover meets Robbins while Betting on Bounded Data: $\ln n$ Regret and Almost Sure $\ln\ln n$ Regret](https://arxiv.org/abs/2604.20172)

**<font color=#1a73e8>作者：</font>** Shubhada Agrawal, Aaditya Ramdas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Consider betting against a sequence of data in $[0,1]$, where one is allowed to make any bet that is fair if the data have a conditional mean $m_0 \in (0,1)$. Cover's universal portfolio algorithm delivers a worst-case regret of $O(\ln n)$ compared to the best constant bet in hindsight, and this bound is unimprovable against adversarially generated data. In this work, we present a novel mixture betting strategy that combines insights from Robbins and Cover, and exhibits a different behavior: it eventually produces a regret of $O(\ln \ln n)$ on \emph{almost} all paths (a measure-one set of paths if each conditional mean equals $m_0$ and intrinsic variance increases to $\infty$), but has an $O(\log n)$ regret on the complement (a measure zero set of paths). Our paper appears to be the first to point out the value in hedging two very different strategies to achieve a best-of-both-worlds adaptivity to stochastic data and protection against adversarial data. We contrast our results to those in~\cite{agrawal2025regret} for a sub-Gaussian mixture on unbounded data: their worst-case regret has to be unbounded, but a similar hedging delivers both an optimal betting growth-rate and an almost sure $\ln\ln n$ regret on stochastic data. Finally, our strategy witnesses a sharp game-theoretic upper law of the iterated logarithm, analogous to~\cite{shafer2005probability}.

---


### 93. [Lever: Inference-Time Policy Reuse under Support Constraints](https://arxiv.org/abs/2604.20174)

**<font color=#1a73e8>作者：</font>** Ihor Vitenki, Noha Ibrahim, Sihem Amer-Yahia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) policies are typically trained for fixed objectives, making reuse difficult when task requirements change. We study inference-time policy reuse: given a library of pre-trained policies and a new composite objective, can a high-quality policy be constructed entirely offline, without additional environment interaction? We introduce lever (Leveraging Efficient Vector Embeddings for Reusable policies), an end-to-end framework that retrieves relevant policies, evaluates them using behavioral embeddings, and composes new policies via offline Q-value composition. We focus on the support-limited regime, where no value propagation is possible, and show that the effectiveness of reuse depends critically on the coverage of available transitions. To balance performance and computational cost, lever proposes composition strategies that control the exploration of candidate policies. Experiments in deterministic GridWorld environments show that inference-time composition can match, and in some cases exceed, training-from-scratch performance while providing substantial speedups. At the same time, performance degrades when long-horizon dependencies require value propagation, highlighting a fundamental limitation of offline reuse.

---


### 94. [Physics-Enhanced Deep Learning for Proactive Thermal Runaway Forecasting in Li-Ion Batteries](https://arxiv.org/abs/2604.20175)

**<font color=#1a73e8>作者：</font>** Salman Khan, Muhammad Zunair Zamir, Syed Sajid Ullah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of thermal runaway in lithium-ion batteries is essential for ensuring the safety, efficiency, and reliability of modern energy storage systems. Conventional data-driven approaches, such as Long Short-Term Memory (LSTM) networks, can capture complex temporal dependencies but often violate thermodynamic principles, resulting in physically inconsistent predictions. Conversely, physics-based thermal models provide interpretability but are computationally expensive and difficult to parameterize for real-time applications. To bridge this gap, this study proposes a Physics-Informed Long Short-Term Memory (PI-LSTM) framework that integrates governing heat transfer equations directly into the deep learning architecture through a physics-based regularization term in the loss function. The model leverages multi-feature input sequences, including state of charge, voltage, current, mechanical stress, and surface temperature, to forecast battery temperature evolution while enforcing thermal diffusion constraints. Extensive experiments conducted on thirteen lithium-ion battery datasets demonstrate that the proposed PI-LSTM achieves an 81.9% reduction in root mean square error (RMSE) and an 81.3% reduction in mean absolute error (MAE) compared to the standard LSTM baseline, while also outperforming CNN-LSTM and multilayer perceptron (MLP) models by wide margins. The inclusion of physical constraints enhances the model's generalization across diverse operating conditions and eliminates non-physical temperature oscillations. These results confirm that physics-informed deep learning offers a viable pathway toward interpretable, accurate, and real-time thermal management in next-generation battery systems.

---


### 95. [Structure-Aware Variational Learning of a Class of Generalized Diffusions](https://arxiv.org/abs/2604.20188)

**<font color=#1a73e8>作者：</font>** Yubin Lu, Xiaofan Li, Chun Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning the underlying potential energy of stochastic gradient systems from partial and noisy observations is a fundamental problem arising in physics, chemistry, and data-driven modeling. Classical approaches often rely on direct regression of governing equations or velocity fields, which can be sensitive to noise and external perturbations and may fail when observations are incomplete. In this work, we propose a structure-aware, energy-based learning framework for inferring unknown potential functions in generalized diffusion processes, grounded in the energetic variational approach. Starting from the energy-dissipation law associated with the Fokker-Planck equation, we construct loss functions based on the De Giorgi dissipation functional, which consistently couple the free energy and the dissipation mechanism of the system. This formulation avoids explicit enforcement of the governing partial differential equation and preserves the underlying variational structure of the dynamics. Through numerical experiments in one, two, and three dimensions, we demonstrate that the proposed energy-based loss exhibits enhanced robustness with respect to observation time, noise level, and the diversity and amount of available training data. These results highlight the effectiveness of energy-dissipation principles as a reliable foundation for learning stochastic diffusion dynamics from data.

---


### 96. [Chasing the Public Score: User Pressure and Evaluation Exploitation in Coding Agent Workflows](https://arxiv.org/abs/2604.20200)

**<font color=#1a73e8>作者：</font>** Hardy Chen, Nancy Lau, Haoqin Tu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier coding agents are increasingly used in workflows where users supervise progress primarily through repeated improvement of a public score, namely the reported score on a public evaluation file with labels in the workspace, rather than through direct inspection of the agent's intermediate outputs. We study whether multi-round user pressure to improve that score induces public score exploitation: behavior that raises the public score through shortcuts without improving hidden private evaluation. We begin with a preliminary single-script tabular classification task, where GPT-5.4 and Claude Opus 4.6 both exploit label information within 10 rounds of user-agent interaction. We then build AgentPressureBench, a 34-task machine-learning repository benchmark spanning three input modalities, and collect 1326 multi-round trajectories from 13 coding agents. On our benchmark, we observe 403 exploitative runs, spanning across all tasks. We also find that stronger models have higher exploitation rates, supported by a significant Spearman rank correlation of 0.77. Our ablation experiments show that higher user pressure leads to earlier exploitation, reducing the average first exploit round by 15.6 rounds (i.e., 19.67 to 4.08). As a mitigation, adding explicit anti-exploit wordings in prompt mostly eliminates exploitation (100% to 8.3%). We hope that our work can bring attention to more careful use of coding agents workflow, and developing more robust coding agents under user pressure. Our project page is at this https URL .

---


### 97. [ACT: Anti-Crosstalk Learning for Cross-Sectional Stock Ranking via Temporal Disentanglement and Structural Purification](https://arxiv.org/abs/2604.20204)

**<font color=#1a73e8>作者：</font>** Juntao Li, Liang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-sectional stock ranking is a fundamental task in quantitative investment, relying on both temporal modeling of individual stocks and the capture of inter-stock dependencies. While existing deep learning models leverage graph-based approaches to enhance ranking accuracy by propagating information over relational graphs, they suffer from a key challenge: crosstalk, namely unintended information interference across predictive factors. We identify two forms of crosstalk: temporal-scale crosstalk, where trends, fluctuations, and shocks are entangled in a shared representation and non-transferable local patterns contaminate cross-stock learning; and structural crosstalk, where heterogeneous relations are indiscriminately fused and relation-specific predictive signals are obscured. To address both issues, we propose the Anti-CrossTalk (ACT) framework for cross-sectional stock ranking via temporal disentanglement and structural purification. Specifically, ACT first decomposes each stock sequence into trend, fluctuation, and shock components, then extracts component-specific information through dedicated branches, which effectively decouples non-transferable local patterns. ACT further introduces a Progressive Structural Purification Encoder to sequentially purify structural crosstalk on the trend component after mitigating temporal-scale crosstalk. An adaptive fusion module finally integrates all branch representations for ranking. Experiments on CSI300 and CSI500 demonstrate that ACT achieves state-of-the-art ranking accuracy and superior portfolio performance, with improvements of up to 74.25% on the CSI300 dataset.

---


### 98. [Scaling Self-Play with Self-Guidance](https://arxiv.org/abs/2604.20209)

**<font color=#1a73e8>作者：</font>** Luke Bailey, Kaiyue Wen, Kefan Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM self-play algorithms are notable in that, in principle, nothing bounds their learning: a Conjecturer model creates problems for a Solver, and both improve together. However, in practice, existing LLM self-play methods do not scale well with large amounts of compute, instead hitting learning plateaus. We argue this is because over long training runs, the Conjecturer learns to hack its reward, collapsing to artificially complex problems that do not help the Solver improve. To overcome this, we introduce Self-Guided Self-Play (SGS), a self-play algorithm in which the language model itself guides the Conjecturer away from degeneracy. In SGS, the model takes on three roles: Solver, Conjecturer, and a Guide that scores synthetic problems by their relevance to unsolved target problems and how clean and natural they are, providing supervision against Conjecturer collapse. Our core hypothesis is that language models can assess whether a subproblem is useful for achieving a goal. We evaluate the scaling properties of SGS by running training for significantly longer than prior works and by fitting scaling laws to cumulative solve rate curves. Applying SGS to formal theorem proving in Lean4, we find that it surpasses the asymptotic solve rate of our strongest RL baseline in fewer than 80 rounds of self-play and enables a 7B parameter model, after 200 rounds of self-play, to solve more problems than a 671B parameter model pass@4.

---


### 99. [Vibrotactile Preference Learning: Uncertainty-Aware Preference Learning for Personalized Vibration Feedback](https://arxiv.org/abs/2604.20210)

**<font color=#1a73e8>作者：</font>** Rongtao Zhang, Xin Zhu, Masoume Pourebadi Khotbehsara 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Individual differences in vibrotactile perception underscore the growing importance of personalization as haptic feedback becomes more prevalent in interactive systems. We propose Vibrotactile Preference Learning (VPL), a system that captures user-specific preference spaces over vibrotactile parameters via Gaussian-process-based uncertainty-aware preference learning. VPL uses an expected information gain-based acquisition strategy to guide query selection over 40 rounds of pairwise comparisons of overall user preference, augmented with user-reported uncertainty, enabling efficient exploration of the parameter space. We evaluate VPL in a user study (N = 13) using the vibrotactile feedback from a Microsoft Xbox controller, showing that it efficiently learns individualized preferences while maintaining comfortable, low-workload user interactions. These results highlight the potential of VPL for scalable personalization of vibrotactile experiences.

---


### 100. [Weighted Knowledge Distillation for Semi-Supervised Segmentation of Maxillary Sinus in Panoramic X-ray Images](https://arxiv.org/abs/2604.20213)

**<font color=#1a73e8>作者：</font>** Juha Park, Jiho Choi, Jong Pil Yun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of maxillary sinus in panoramic X-ray images is essential for dental diagnosis and surgical planning; however, this task remains relatively underexplored in dental imaging research. Structural overlap, ambiguous anatomical boundaries inherent to two-dimensional panoramic projections, and the limited availability of large scale clinical datasets with reliable pixel-level annotations make the development and evaluation of segmentation models challenging. To address these challenges, we propose a semi-supervised segmentation framework that effectively leverages both labeled and unlabeled panoramic radiographs, where knowledge distillation is utilized to train a student model with reliable structural information distilled from a teacher model. Specifically, we introduce a weighted knowledge distillation loss to suppress unreliable distillation signals caused by structural discrepancies between teacher and student predictions. To further enhance the quality of pseudo labels generated by the teacher network, we introduce SinusCycle-GAN which is a refinement network based on unpaired image-to-image translation. This refinement process improves the precision of boundaries and reduces noise propagation when learning from unlabeled data during semi-supervised training. To evaluate the proposed method, we collected clinical panoramic X-ray images from 2,511 patients, and experimental results demonstrate that the proposed method outperforms state-of-the-art segmentation models, achieving the Dice score of 96.35\% while reducing boundary error. The results indicate that the proposed semi-supervised framework provides robust and anatomically consistent segmentation performance under limited labeled data conditions, highlighting its potential for broader dental image analysis applications.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-220](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
