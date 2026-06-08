# 📦 其他研究 | 2026年06月09日

> 本类共 **199** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-199**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-199**

---

### 151. [Reconstructing Multi-Decadal Forest Disturbances: A Spatio-Temporal Transformer Approach](https://arxiv.org/abs/2606.07249)

**<font color=#1a73e8>作者：</font>** Linus Scheibenreif, Anton Raichuk, Maxim Neumann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate monitoring of forest disturbances is essential for understanding carbon dynamics and land management, yet traditional approaches typically rely on pixel-wise analysis of satellite time-series, ignoring spatial context. We present a deep learning framework that maps 38 years (1984-2022) of forest disturbance across the contiguous United States by modeling temporal trajectories and spatial neighborhoods simultaneously. By leveraging a vision transformer architecture, our approach effectively filters noise from weak supervision signals to produce spatially coherent disturbance maps. We perform exhaustive evaluations across multiple satellites (Landsat, Sentinel-1, Sentinel-2) and temporal windows (38 years and the more recent 6 years), validating performance against a novel, manually annotated validation dataset (n=300) and independent fire perimeter dataset (n=706). The results highlight the complexity of the task: while our spatio-temporal model demonstrates high precision (up to 98.2% for +-1 year detection on MTBS and up to 71.3% on the CONUS validation datasets, with F1-scores up to 75.8% and 47.3%, respectively) and effectively reduces spatial artifacts, it exhibits performance trade-offs across different disturbance regimes compared to pixel-wise baselines. Our method offers a promising foundation for consistent forest monitoring.

---


### 152. [TOPSIS-RAD: Ranking According to Desires](https://arxiv.org/abs/2606.07253)

**<font color=#1a73e8>作者：</font>** Leonardo Fernandes Costa, Helder Gomes Costa, Diogo Lima 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional TOPSIS derives its reference points -- the Positive Ideal Solution ($PIS$) and Negative Ideal Solution ($NIS$) -- from the observed alternative set, making rankings susceptible to misalignment with decision-maker (DM) requirements, sensitivity to outlier performances, and rank reversal. This paper proposes TOPSIS-RAD, which addresses these issues by incorporating two arrays of DM-defined reference levels. Vetoed Performance Levels ($VPL$) exclude non-viable alternatives before normalisation, preventing them from distorting the ranking frontiers. Desired Performance Levels ($DPL$) cap performances at the DM's desired level before normalisation, anchoring the $PIS$ in explicit aspirations rather than dataset extremes. Three toy examples demonstrate each mechanism: $VPL$ reshapes normalisation boundaries by removing a non-viable alternative; fixed $DPL$ frontiers stabilise rankings by limiting the influence of performances well above the desired level. The method preserves the familiar distance-based structure of TOPSIS while grounding the ranking in stable, DM-specified boundaries. Limitations and future research directions are also discussed.

---


### 153. [A Held-Out Transition-Pair Falsifier for Long-Horizon Non-Abelian State Tracking](https://arxiv.org/abs/2606.07254)

**<font color=#1a73e8>作者：</font>** Jeonghoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State tracking exposes a sharp limitation of sequence models: the relevant signal is often not a summary of observed tokens, but an ordered latent state that evolves through non-commutative transformations. We introduce a held-out transition-pair falsifier for finite non-Abelian group tracking. The protocol forbids selected ordered generator pairs during training and requires the same local patterns during evaluation, blocking one direct local-transition memorization pathway. In a controlled $S_3 \times S_3$ benchmark, a projected recurrent state model trained only on length-8 sequences produces error-free final-state predictions (perfect 250/250 per horizon) through evaluation horizons up to 1,048,576 tokens across five seeds. Matched native-readout baselines, including bag, GRU, and a single-configuration structured state-space model, remain near floor under the same protocol. Projection-matched GRU, structured SSM, and bag baselines equipped with analogous finite-group prototype readouts also remain near chance under the same split. Mechanism diagnostics show that hard projection coincides with low homomorphism error, low state-consistency drift, and non-trivial commutator separation, while softened projection collapses final-state accuracy. Clean-split audits verify zero verbatim reduced-word overlap and zero structural-template overlap between training and evaluation partitions. The evidence is scoped to this controlled finite-group falsifier rather than to a general architecture ranking. Within that regime, explicit projected non-commutative state composition acts as a useful inductive bias for long-horizon hidden-state tracking.

---


### 154. [Where Rectified Flows Leak: Characterising Membership Signals Along the Interpolation Path](https://arxiv.org/abs/2606.07271)

**<font color=#1a73e8>作者：</font>** Thomas Sesmat, Gabriel Meseguer-Brocal, Geoffroy Peeters  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding what generative models retain from training data remains challenging, with implications for copyright and privacy. Beyond verbatim reproduction, models can encode subtler traces of their training data that never surface in their outputs yet remain exploitable. We study this regime for Rectified Flows, which are increasingly used in deployed generative systems. We analyse the interpolation path $X_\lambda = (1-\lambda)X_0 + \lambda X_1$ that defines the Rectified Flow training. We show that a gap exists between the reconstruction of train and test data that follows a bell-shaped curve over $\lambda$, wich accumulates during training, while the validation metrics remain stable. The signal has a maximum whose location we derive in closed form under Gaussian assumptions. We validate these predictions on both audio and images and show that the bell-shaped structure is universal, while the peak prediction holds when our assumptions are satisfied. As a proof of concept, we exploit this specific $\lambda$-resolved structure to perform a Membership Inference Attack, distinguishing members of the training set from non-members.

---


### 155. [Geometric-Aware Hypergraph Reasoning for Novel Class Discovery in Point Cloud Segmentation](https://arxiv.org/abs/2606.07280)

**<font color=#1a73e8>作者：</font>** Zihao Zhang, Aming Wu, Yang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel class discovery in point cloud segmentation aims to transfer knowledge from known classes to automatically identify and segment unlabeled novel classes in point clouds. Existing methods mainly rely on pairwise associations for class assignment and novel class reasoning, which limits their ability to capture complex relationships among known and novel classes and may lead to inaccurate semantic segmentation. To address this issue, we introduce a hypergraph-based framework that models high-order associations among classes and enables collaborative reasoning from known classes to novel classes beyond traditional pairwise relations. Moreover, existing methods tend to focus on semantic feature extraction while paying insufficient attention to geometric information in point clouds. To better exploit spatial structure, we propose Geometric-Aware Prototypes to enhance the representation of class-level geometric cues. By propagating geometric information through hyperedges, the proposed method improves the understanding of spatial distributions across classes and leads to more accurate segmentation. Experiments on the SemanticKITTI and SemanticPOSS datasets demonstrate the effectiveness and superiority of our method.

---


### 156. [Rethinking IoT Intrusion Detection: Augmenting Routing Metrics with Radio Features](https://arxiv.org/abs/2606.07282)

**<font color=#1a73e8>作者：</font>** Yichang Sun, Andreas Johnsson, Sourasekhar Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning-based intrusion detection systems (IDS) for RPL-based IoT networks often rely solely on routing layer features, which provide only a partial view of network behaviour. In this work, we investigate whether incorporating Transmit (TX) and Receive (RX) radio features alongside the standard RPL feature set can improve detection performance in an LSTM-based IDS. We evaluate the proposed approach across three different attack types, namely DIS-Flooding, Local Repair, and Worst Parent under varying network sizes. The results show that incorporating TX and RX improves the IDS's overall detection performance by up to ~4% in F1-score compared with using routing-layer features alone, with the most notable gain observed for the Worst Parent attack.

---


### 157. [A Model of Integrated Information Processing in Human-AI Interaction](https://arxiv.org/abs/2606.07283)

**<font color=#1a73e8>作者：</font>** Tim Schrills. Thomas Franke  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> For Human-AI Interaction (HAII) research to move forward, theoretical work linking psychological mechanisms to interface design is needed. Such work should extend rather than replace established HCI and automation research, adapting to the increasing autonomy and agency of AI systems. Building on prior frameworks focused on roles and levels in human interaction with automation, a gap remains from a psychological view: a task-centered, process-oriented account that links mechanisms of action regulation to concrete design and evaluation levers for human-AI coupling, expressed in a unified vocabulary for human and machine. Moreover, existing models may describe how a system is designed (e.g., function allocation in automation) but fall short in showing how this design affects human behavior. We present the Integrated Information Processing (IIP) model, a task-centered, cybernetic model that conceptualizes humans, machines, and their joint activity as coupled control loops. The IIP model uses a unified modeling language for human and artificial agents, making psychological models of action regulation accessible for AI system design. As a core feature, we argue that efficacy within a shared task is characterized by three integration qualities, input adequacy, reference consonance, and output operativity, which critically influence benchmarks of human-centeredness such as transparency and controllability. The model maps interface choices (e.g., XAI techniques) to theory-driven expectations of user behavior, guiding interface design and evaluation. To this end, we present (1) a continuity-preserving theoretical discourse that extends HAII to agency in AI; (2) the IIP model with three information-processing qualities; and (3) applications of the IIP model to exemplary use cases demonstrating implications for interface design.

---


### 158. [ExMesh: EXplicit Mesh Reconstruction with Topology Adaptation](https://arxiv.org/abs/2606.07288)

**<font color=#1a73e8>作者：</font>** Chuanjin Fan, Lifan Wu, Wenjie Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing surface meshes from multi-view images has remained a core challenge in recent years. Most existing methods, whether implicit or explicit, depend on intermediate representations and post-processing steps like Marching Cubes or TSDF fusion, often resulting in artifacts and fragmented geometry. Directly optimizing explicit meshes is a promising approach. However, it presents two critical challenges. The first is how to adaptively refine mesh topology to capture detail without introducing degenerate faces. The second is how to maintain consistent UV coordinates for high-fidelity texturing as the mesh structure evolves. To overcome these, we propose ExMesh, a novel framework that directly optimizes explicit meshes by integrating differentiable optimization with discrete topology updates. Specifically, we introduce an adaptive vertex splitting and merging strategy, along with real-time UV maintenance, to enable coarse-to-fine optimization while preserving geometric integrity. To our knowledge, ExMesh is the first framework to seamlessly integrate discrete topology operations into a continuous differentiable optimization pipeline. Extensive experiments demonstrate that ExMesh achieves a balance among accuracy, computational efficiency, and mesh conciseness.

---


### 159. [Closed-Form Spectral Regularization for Multi-Task Model Merging](https://arxiv.org/abs/2606.07289)

**<font color=#1a73e8>作者：</font>** Yongxian Wei, Runxi Cheng, Xingxuan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging combines several independently fine-tuned experts into a single multi-task model without any training data, reducing the storage, serving, and decentralized-development costs of large foundation models. State-of-the-art merging methods formulate merging as a layer-wise quadratic interference minimization problem. Although this problem admits an exact closed-form pseudoinverse solution, that solution underperforms hundreds of iterations of gradient descent in practice. The iterative loop dominates the cost of the pipeline, yet its effectiveness has remained unexplained. We revisit this regime and show that the iterative solver does not primarily act as an optimizer; rather, it serves as an implicit spectral regularizer for an ill-posed normal equation, where small-eigenvalue directions of the per-layer interference operator amplify proxy noise. Building on this finding, we formalize multi-task model merging as a noisy linear inverse problem and propose a spectral filtering estimator parameterized by a per-direction filter. We instantiate this estimator with SWUDI, a closed-form method that combines a soft exponential filter, which matches the gradient-flow trajectory of iterative descent, with a hard top-K truncation that suppresses noise-amplifying small-eigenvalue directions. Furthermore, we propose SWUDI-A, an adaptive variant that replaces the global rank hyperparameter with per-layer rank rules, further improving robustness across architectures. Both variants share a single symmetric eigendecomposition per linear layer and require no training data or optimizer state. Across four general benchmarks and a multimodal merging benchmark spanning VQA, Geometry, Chart, OCR, Grounding, and modality merging, our proposed spectral solvers match or outperform state-of-the-art merging methods. Crucially, they reduce wall-clock time by 28-72x and peak GPU memory by up to 50%.

---


### 160. [Trio: Learning Time-Series Forecasting with Temporal-Spatial-Sample Attention and Structural Causal Priors](https://arxiv.org/abs/2606.07291)

**<font color=#1a73e8>作者：</font>** Tao Chen, Yexu Zhou, Zhi Gong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time-series forecasting requires models to reason over temporal dynamics, cross-variable dependencies, and historical input-output correspondences. Recent Prior-Data Fitted Networks (PFNs) suggest that synthetic tasks can be useful for learning transferable inference behavior. However, directly transferring this paradigm to time-series forecasting remains difficult, since temporal order, dynamic lags, and recurring historical patterns are not naturally captured by ordinary tabular priors. Motivated by this observation, we propose Trio, a sample-aware time-series forecasting architecture based on Temporal-Spatial-Sample attention. Temporal attention captures within-window dynamics, spatial attention models inter-variable dependencies, and sample attention retrieves relevant historical lookback-future pairs to guide the current prediction. Rather than claiming a fully general PFN-style forecaster, our goal is to study how historical input-output examples can be explicitly organized and reused within a forecasting model. We further introduce a Time-Series Structural Causal Model (TS-SCM) generator to create structured synthetic forecasting tasks with dynamic lags, cross-variable interactions, noise, feedback, and distributional drift. Experiments on synthetic, industrial, and public benchmarks show that the proposed architecture improves forecasting performance. Exploratory zero-shot experiments further suggest that TS-SCM-generated tasks may provide useful structural priors, while fully general PFN-style time-series forecasting remains an open problem.

---


### 161. [DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning](https://arxiv.org/abs/2606.07299)

**<font color=#1a73e8>作者：</font>** Lingyong Yan, Can Xu, Yukun Zhao 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep Research (DR) has emerged as a new agentic paradigm to tackle complex, open-ended research tasks, demanding systems that can iteratively frame problems, acquire evidence, verify sources, and synthesize long-form reports. In practice, however, current DR systems are constrained by four interrelated limitations: long-horizon planning over an underspecified scope, the bottleneck of decomposing and scheduling such tasks within a single agent, hallucination risk in long-form synthesis, and limited process auditability. This technical report presents DuMate-DeepResearch, a multi-agent DR framework built on the Qianfan Agent Foundry. The framework decouples the Agent Core, which handles task understanding, planning, and scheduling, from an extensible Tool Ecosystem for retrieval, evidence acquisition, and report rendering, making every intermediate decision and tool invocation explicitly traceable. Building on this infrastructure, DuMate-DeepResearch further introduces three mechanisms: (i) a graph-based dynamic planning strategy expands the research roadmap coarse-to-fine and continuously revises it through reflection, re-planning, backtracking, and parallel branching; (ii) a recursive two-level execution design delegates each complex search sub-task to an inner Search Agent that runs its own planning loop, isolating noisy retrieval and stabilizing long-horizon execution; (iii) a rubric-based test-time optimization mechanism dynamically generates task-specific quality criteria and uses them as live reasoning scaffolds for evidence-grounded synthesis and adaptive stopping. Across two deep research benchmarks, DuMate-DeepResearch establishes new state-of-the-art results: the best overall score (58.03%) on DeepResearch Bench, and the best overall score (61.95%) on DeepResearch Bench II while ranking first in information recall and analysis.

---


### 162. [Off-Policy Evaluation with Strategic Agents via Local Disclosure](https://arxiv.org/abs/2606.07308)

**<font color=#1a73e8>作者：</font>** Kiet Q. H. Vo, Abbavaram Gowtham Reddy, Julian Rodemann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study off-policy evaluation (OPE) under strategic behavior where decision subjects (or agents) respond to a decision maker's policy by strategically modifying their covariates. Such behavior induces a policy-dependent covariate shift, breaking the standard assumption in existing methods that covariates are exogenous to the policy. Related work addresses this challenge by imposing strong assumptions such as repeated interactions or full knowledge of agents' response behavior, substantially limiting its applicability to OPE. In contrast, we consider a one-shot OPE setting where the decision maker has only partial knowledge of the agents' response behavior. Our key insight is that disclosing local information through post-hoc explanations reveals agents' pre-strategic covariates prior to adaptation, mitigating the information loss induced by strategic behavior. Leveraging this structure, we estimate a statistical model for the agents' responses and construct a doubly robust estimator for policy value. By assuming that the agents' cost sensitivity follows a conditional log-normal distribution, we establish consistency of the proposed estimator and validate our approach empirically. More broadly, our results highlight how interaction design can mitigate information asymmetry by revealing otherwise hidden structure in agents' strategic responses.

---


### 163. [CULTURESCORE: Evaluating Cultural Faithfulness in Video Generation Models](https://arxiv.org/abs/2606.07311)

**<font color=#1a73e8>作者：</font>** Anku Rani, Wei Dai, Shravan Nayak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As video generation models like Veo 3.1 and LTX-2 advance, their ability to accurately represent diverse global cultures remains a critical yet understudied frontier. Current metrics, such as VideoScore, only measure visual quality but offer no mechanism for assessing cultural faithfulness. Consequently, a model that replaces a Namaste with a handshake receives the same score as one that generates the gesture correctly. We propose CultureScore, a compositional evaluation framework that decomposes cultural faithfulness into three granular dimensions: Identity (who is represented), Context (culturally localized background), and Behavior (normative gestures and interactions). We operationalize this framework through an evaluation suite spanning 10 countries, yielding 6,180 generated videos across three state-of-the-art models. Our evaluation reveals that no current model achieves culturally faithful video generation: the best-performing model reaches only 56.8\% overall CultureScore, with Behavior the most challenging dimension, which remains below 52\% across all models. Furthermore, human preference rankings align directionally with CultureScore but are inverted relative to VideoScore; the highest-scoring model on visual quality was ranked last by annotators, underscoring that cultural faithfulness is an essential criterion for equitable video generation.

---


### 164. [SV-Detect: AI-generated Text Detection with Steering Vectors](https://arxiv.org/abs/2606.07313)

**<font color=#1a73e8>作者：</font>** Mikhail Vishnyakov, Tatiana Gaintseva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting machine-generated text is especially difficult under distribution shift, such as transfer across domains, source models, and editing attacks. We propose a fake-text detector based on steering vectors extracted from the hidden representations of a frozen language model. At each layer, we construct a direction that separates human-written from machine-generated text, and represent each input by its layer-wise alignment with these directions. A lightweight classifier trained on these projection features yields the final detection score. Our method achieves strong performance both in-distribution and under distribution shift, including across domains, source models, and machine-editing transformations such as polishing and rewriting. Interpretation analyses show that the learned directions align with recognizable stylistic cues while capturing substantial additional signal beyond surface features. These results position fake-text detection as a representation-space probing problem and show that steering vectors provide a simple and effective solution.

---


### 165. [AnchorWorld: Embodied Egocentric World Simulation with View-based Evolution Customization](https://arxiv.org/abs/2606.07326)

**<font color=#1a73e8>作者：</font>** Yu Li, Menghan Xia, Gongye Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite being a pivotal frontier, interactive world modeling remains underexplored in terms of the versatile controllability required by practical scenarios. To bridge this gap, we present AnchorWorld, a framework that advances egocentric simulation through enhanced interaction integrity and a flexible mechanism for world customization. First, we utilize 3D human motion as the primary interaction modality. To complement the out-of-view or truncated body parts in egocentric views, we introduce an auxiliary training supervision that incorporates exogenous viewpoints decoupled from the agent's first-person sensorium. It allows the model to observe the agent's full-body positioning relative to the environment, facilitating a more robust spatial grounding of human-world interactions. Furthermore, we propose a simple yet effective mechanism for customizing self-evolving worlds. This is achieved by defining anchor views within a unified world coordinate system, coupled with textual descriptions dictating the dynamic evolution of local scenes. Experimental results show that AnchorWorld significantly outperforms state-of-the-art baselines, while ablation studies validate the effectiveness of our key designs. Notably, our customization scheme exhibits promising spatio-temporal geometric consistency and adheres strictly to the prescribed evolutionary dynamics.

---


### 166. [Varifold Moment Invariants for Sustainable and Explainable Contour Feature Extraction](https://arxiv.org/abs/2606.07333)

**<font color=#1a73e8>作者：</font>** G. Longari, J.-C. Alvarez Paiva, A.B. Tumpach  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Varifold Moments Invariants (VMI) as a unifying framework for many previously introduced Moment Invariants. These invariants are deeply related to other contour features that are invariant under translations and rotations, like Extended Gaussian Image, Elliptic Fourier Descriptors or Shape Distributions. The advantage of the varifold approach to moments consists in being able to combine the geometry of the region, its boundary, and the family of lines tangent to it, in order to create a substantial number of invariant features with high discriminating power and clear geometric meaning. By coupling our VMI feature extraction with the light feature classifiers Random Forest or Multi-Layer-Perceptron, we outperform state-of-the-art approaches based on contours, while decreasing drastically the computational cost to the point of allowing our algorithm to run on light devices. We tested our approach on classification tasks on a large number of widely-used datasets of various types (leaves, objects, cells) and achieved high accuracy with a low number of geometrically interpretable features.

---


### 167. [VeriDrive: Verifiable Counterfactual Supervision for Cost-Efficient Vision-Language Planning](https://arxiv.org/abs/2606.07338)

**<font color=#1a73e8>作者：</font>** Zikai Zhang, Hubert P. H. Shum, Toby P. Breckon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language driving models increasingly use reasoning supervision to bridge perception, prediction, and planning, but existing driving rationales are often free-form and expensive to generate with frontier models. We present VeriDrive, a framework for constructing planning-oriented, verifiable counterfactual supervision. VeriDrive converts driving reasoning into a structured Perception-Evaluation-Revision chain that grounds key objects in future motion, evaluates alternative ego trajectories with rule-checkable evidence, revises risky intent toward expert behavior, and produces final planning targets. To scale data construction, VeriDrive combines local generation with validator-guided selective correction, escalating only invalid or difficult samples. We build the VeriDrive dataset on nuScenes and train under the Omni-Q protocol. Controlled open-loop experiments show that VeriDrive improves L2, Collision, and Intersection over OmniDrive while reducing logged token usage, generation time, and actual paid LLM/VLM cost. These results show that auditable intermediate fields and structured revision targets can improve vision-language planning supervision under realistic annotation budgets. Code, prompts, and validator scripts are coming soon and will be released after the review process.

---


### 168. [SleepExplain: Explainable Non-Rapid Eye Movement and Rapid Eye Movement Sleep Stage Classification from EEG Signal](https://arxiv.org/abs/2606.07351)

**<font color=#1a73e8>作者：</font>** Rafsan Jany, Md. Hamjajul Ashmafee, Iqram Hussain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classification of sleep stages is one of the most important diagnostic approaches for a variety of sleep-related disorders. Electroencephalography (EEG) is regarded as a powerful tool for examining the association between neurological effects and sleep phases since it correctly identifies sleep-related neurological alterations. During Non-Rapid Eye Movement (NREM) and Rapid Eye Movement (REM) sleep phases, a number of nerve and bodily functions are affected and therefore hold an important role both in their functionalities. This work aims to classify NREM and REM sleep stages from sleep EEG data and present a noble SleepExplain model, an explainable NREM and REM sleep stage classification to explain its predictions. In this work, sleep stages were classified using Random Forest, XGBoost, and Gradient Boosting ensemble classification models. Overall, we obtained an accuracy of 92.54% (Random Forest), 94.25% (Gradient Boosting), and 94.30% (XGBoost). For explainable classification model, we utilized a game theoretic approach, SHAP (SHapley Addictive exPlanations) to offer a convincing explanation for the prediction.

---


### 169. [Spatial-Temporal Decoupled Adapter for Micro-gesture Online Recognition](https://arxiv.org/abs/2606.07355)

**<font color=#1a73e8>作者：</font>** Xucheng Shen, Kun Li, Fei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-gesture online recognition aims to temporally localize and classify subtle gestures in untrimmed videos. Owing to their extremely short duration, low motion amplitude, and ambiguous visual cues, capturing discriminative spatiotemporal representations remains highly challenging. Existing parameter-efficient adapters typically employ a single branch to model spatial and temporal cues jointly, which may fail to capture the fine-grained patterns of micro-gestures. To address this limitation, we propose a Spatial-Temporal Decoupled Adapter that decomposes video adaptation into independent temporal and spatial branches via lightweight depthwise convolutions. In addition, to address the long-tail distribution problem in the benchmark dataset, we introduce Adaptive Soft Balanced Augmentation, which dynamically allocates augmentation intensity based on class rarity and learning difficulty, without manual thresholds. Our method achieves an F1 score of 0.43808, ranking 1st in Track 2 of the 4th EI-MiGA-IJCAI Challenge.

---


### 170. [On the Shoulders of Giants: Empowering Automated Smart Contract Auditing via the GiAnt Corpus](https://arxiv.org/abs/2606.07363)

**<font color=#1a73e8>作者：</font>** Xiaoting Zhang, Zhipeng Gao, Yiran Lv 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> High-quality smart contract auditing datasets are crucial for evaluating security tools and advancing smart contract security research. Two major limitations of existing datasets are the manual-induced scalability bottleneck and the deficiency in data granularity and diversity. To address these limitations, we propose GiANT, an automated framework designed to curate smart contract auditing datasets by distilling vulnerability insights from real-world auditing reports. GiANT employs a divide-and-conquer strategy coupled with the Chain-of-Thought technique to extract structured vulnerability information from Code4rena reports, followed by an LLM-as-a-judge mechanism to perform rigorous quality assurance. To evaluate GiANT's effectiveness, we run it on 388 real-world audit reports and generate the GiAnt Corpus comprising 7,711 vulnerability findings across five severity levels. Manual assessment of the dataset demonstrates exceptional reliability in information extraction, achieving a mean quality score of $4.76\pm0.37$ (out of 5) with inter-rater agreement $\kappa$ of 0.88. We further validate the practicality of our dataset by benchmarking 4 state-of-the-art LLMs on vulnerability detection, code summarization, mitigation recommendation, and automated gas optimization tasks, to establish performance baselines, thereby providing a valuable data foundation for future research in automated smart contract auditing.

---


### 171. [Dash2Sim: Closed-Loop Driving Simulation from in-the-wild Dashcam Videos](https://arxiv.org/abs/2606.07366)

**<font color=#1a73e8>作者：</font>** Anurag Ghosh, Francesco Pittaluga, Khiem Vuong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-driving simulations typically rely on data collected in a small number of cities or on hand-authored synthetic scenarios. Dashcam videos cover a far broader range of locations and situations, including rare or long-tailed scenarios. They are considered less usable for simulation because it is difficult to recover accurate 4D scenes from monocular in-the-wild videos. Work zones are one such class of long-tailed situations that dashcams capture. We present Dash2Sim, a framework that turns in-the-wild monocular dashcam videos into metric, geo-referenced 4D driving logs compatible with existing simulators, and verifies eachone against an independently maintained map without annotations. We apply Dash2Sim to a large video corpus to create the ROADWork4D benchmark dataset, which spans 4,244 scenes with 2.7M 3D objects across 17 cities. On a verified subset ROADWork4D-CL (2,201 scenes), we study privileged closed-loop planners and find that work zone scenarios are difficult: while rule-based and hybrid planners generalize better than learning-based ones, all fall short, failing to make the lane changes that temporary work zone channels require. Beyond planning, dense depth recovered by Dash2Sim improves novel-view synthesis quality by up to 19% on perceptual metrics, suggesting its potential to provide rich conditioning for closed-loop sensor simulation from monocular videos.

---


### 172. [Mitosis Detection in the Wild: Multi-Tumor and Context-Aware Generalization in the MIDOG 2025 Challenge](https://arxiv.org/abs/2606.07368)

**<font color=#1a73e8>作者：</font>** Marc Aubreville, Jonas Ammeling, Sweta Banerjee 等 67 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated mitosis detection is a well-established task in computational pathology. While previous benchmarks focused on scanner-induced domain shift, clinical "real-world" application requires models to be robust across the vast variance to be expected in the histological landscape. The MItosis DOmain Generalization (MIDOG) 2025 challenge was designed to evaluate algorithmic performance across unprecedented biological and contextual diversity. We curated a test dataset of 365 cases, encompassing 12 distinct human, canine and feline tumor types, digitized across multiple scanning platforms. Moving beyond hand-selected hotspots, the challenge required detection also in random tissue areas (representative of the whole slide detection situation) and challenging areas (areas rich in hard negatives). In the second track, we introduced the classification of atypical mitotic figures (AMFs). There were 18 teams submitting to the detection track, with F1 scores ranging up to 0.740. In the AMF detection track, we had 21 submissions with balanced accuracy values up to 0.908. Our analysis reveals that while most models perform reliably in traditional hotspots, significant performance degradation occurs in challenging ROIs, where false positive rates tripled. Furthermore, performance varied significantly across the 12 tumor types, highlighting "blind spots" in current state-of-the-art architectures when encountering rare or highly pleomorphic malignancies. Moreover, we evaluated the effectiveness of ensembling and found a mean increases of 1.5 and 1.3 percentage points in F1 score and balanced accuracy, respectively. In contrast, TTA showed no relevant improvement. MIDOG 2025 demonstrates that "in the wild" mitosis detection remains a significant hurdle. The transition from hotspot-only evaluation to a multi-contextual framework provides a more realistic proxy for clinical reliability.

---


### 173. [Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests](https://arxiv.org/abs/2606.07379)

**<font color=#1a73e8>作者：</font>** Thanawat Lodkaew, Johannes Ackermann, Soichiro Nishimori 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A growing failure mode in agent evaluation and training is that models can achieve high evaluation scores by exploiting shortcuts instead of solving the intended task, producing deceptive performance. This makes evaluation scores unreliable as measures of true task-solving ability. We propose CapCode, a framework for constructing coding datasets with randomized tests whose best achievable non-cheating performance is deliberately capped below one. This capped-performance design gives evaluation scores a clearer interpretation: scores substantially above the cap are implausible and therefore provide evidence of cheating. To prevent cheating, we propose CapReward, a reward design based on the CapCode principle to discourage optimization beyond the cap. Experiments across multiple datasets show that CapCode detects cheating while preserving performance ranking of models, and CapReward reduces cheating behavior, yielding models that better follow the intended task specification.

---


### 174. [Covariance Shrinkage via Stochastic Interpolation](https://arxiv.org/abs/2606.07382)

**<font color=#1a73e8>作者：</font>** Mathieu Chalvidal, Florentin Coeurdoux, Eric Vanden-Eijnden  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We recast classical shrinkage of high-dimensional covariance estimators as empirical risk minimization over a parametric stochastic interpolant between a source and a target distribution. This formalism recovers known shrinkage estimators as special cases and reveals three distinct mechanisms for reducing statistical risk: (i) Scheduling: the interpolant schedule determines the class of admissible covariances, and hence the achievable risk. (ii) Flow maps and couplings: whereas naive constructions amount to assuming independence between the distributions, specific coupling structures (e.g., solutions of optimal transport problems) can lower the empirical risk. Moreover, non-linear flow maps realizing such couplings free the interpolant covariance from the eigenbasis of the empirical estimate, enabling eigenvector regularization. (iii) Early stopping: estimators defined by integrating a regressed vector field afford an additional bias-variance trade-off through approximation of the true interpolant distribution. We then propose a neural estimator of the interpolant, together with an upper bound on its quadratic risk in terms of the interpolant approximation error, and validate both on synthetic experiments. Finally, we apply the estimator to real neuroimaging data, demonstrating the additional regularization power this approach offers in practice.

---


### 175. [Making the Most of Limited Data: Score-Aware Training for Text-to-Music Generation](https://arxiv.org/abs/2606.07387)

**<font color=#1a73e8>作者：</font>** Yun-Chen Cheng, Tzu-Hung Huang, Chih-Pin Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-of-the-art text-to-music generation systems rely on massive proprietary datasets and industrial-scale compute, making it impossible to disentangle architectural contributions from resource advantages. We propose \textit{score-aware training}, which treats audio-caption alignment score as a direct supervision signal throughout the pipeline. Rather than discarding low-scoring segments, we repurpose them via a CLAP-conditioned Beta noise timestep schedule that routes them to high-noise training regimes, acting as an effective implicit regularizer. Complementarily, segment-level filtering removes the most misaligned examples, and a two-stage caption procedure bridges the distribution gap between verbose training captions and concise inference prompts. A REPA auxiliary loss further transfers structured semantic knowledge from pretrained CLAP and MuQ encoders without additional data. Our 450M-parameter FluxAudio-based system, submitted to the ICME 2026 ATTM Grand Challenge Efficiency Track, ranked 2nd across both tracks in the objective evaluation and 3rd in the Efficiency Track in the final MOS evaluation.

---


### 176. [Mind the Gap: Disentangling Performance Bottlenecks in Video Instance Segmentation](https://arxiv.org/abs/2606.07394)

**<font color=#1a73e8>作者：</font>** Danial Hamdi, Fardin Ayar, Mahdi Javanmardi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In Video Instance Segmentation (VIS), classification, segmentation, and tracking objectives are jointly evaluated, but their individual contributions to performance loss remain opaque. We introduce a diagnostic framework that formulates identity and class assignment as an Integer Linear Program (ILP), yielding a model-agnostic oracle that hierarchically isolates each error source. Applied to seven VIS methods spanning online and offline paradigms across YouTube-VIS 2019/2021 and a diagnostic subset of OVIS, our analysis reveals a consistent picture. Tracking instability is a critical bottleneck for online methods, with gaps exceeding 20 AP under heavy occlusion, and grows sharply with video length and instance density. While semantic classification contributes meaningfully on standard benchmarks, its impact becomes negligible where tracking fails most. Although stronger backbones substantially lift default scores, they leave AP tracking gaps largely intact, confirming that temporal fragility is algorithmic rather than purely representational. To complement the oracle, we introduce TrackLens, a visual tool that translates gap magnitude into observable, query-level failure modes. Together, these tools provide a systematic foundation for targeting VIS's core challenge: robust long-term temporal association.

---


### 177. [Generative Modeling of Discrete Latent Structures via Dynamic Policy Gradients](https://arxiv.org/abs/2606.07400)

**<font color=#1a73e8>作者：</font>** Stefan Ivanovic, Ge Liu, Mohammed El-Kebir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many scientific problems require inferring unobserved mechanistic latent states from indirect observations. While classical approaches, including expectation maximization, do not scale to combinatorially large spaces, deep learning approaches such as variational autoencoders typically form artificial latent states rather than reconstructing the mechanistic ground-truth states. Here, we introduce GReinSS, a policy learning framework that uses dynamically rescaled rewards to learn latent state distributions that maximize the observed data likelihood. We show that GReinSS accurately reconstructs simulated latent sets and latent graphs, outperforming alternative policy learning and generative modeling baselines. Additionally, GReinSS reconstructs isoforms from real short-read RNA sequencing data that better match isoforms detected by orthogonal long-read sequencing than the standard RSEM algorithm. Overall, GReinSS is a principled and practically effective approach for generative modeling and inference of combinatorial latent states from indirect observations.

---


### 178. [RealDocBench: A Benchmark for Field-Level QA and Layout Understanding on Real-World Regulated Documents](https://arxiv.org/abs/2606.07401)

**<font color=#1a73e8>作者：</font>** Ameya Joshi, Joon Kim, Gus Eggert 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Document parsing systems are increasingly deployed in high-stakes, regulated workflows such as mortgage underwriting, financial reporting, supply-chain logistics, and clinical records. Yet most public benchmarks evaluate parsers on clean academic layouts or synthetic prose, and report a single OCR or markdown-level similarity score. Such documents and metrics correlate poorly with what downstream agents actually need: the correct value for a specific field on a messy real-world page. We introduce RealDocBench, a two-track benchmark built from real regulated documents. The QA track contains 1,356 field-level questions over 581 documents spanning four domains, where each question is paired with a typed gold_dict of key-to-value answers and parsers are scored on both per-field and strict per-question accuracy. The layout track contains 1,500 human-verified page images annotated with COCO-style bounding boxes under a nine-class public taxonomy, scored with a Hungarian matcher that includes adjacency-aware split/merge recovery. We evaluate eighteen systems, spanning commercial parsing APIs, general-purpose VLMs, and open-source OCR models, under a uniform extraction-and-scoring protocol, and report accuracy alongside per-page cost and cache-busted latency. RealDocBench exposes a wide performance spread that single-number benchmarks hide, a persistently hard medical sub-domain, and sharp cost/latency trade-offs across operating points. We release the datasets, parser adapters, and evaluation harness to support reproducible, field-level comparison of document parsing systems.

---


### 179. [Sparsely gated tiny linear experts](https://arxiv.org/abs/2606.07414)

**<font color=#1a73e8>作者：</font>** Simon Schug  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparsity allows scaling model parameters without proportionally increasing computational cost. While mixture of experts (MoE) models are made increasingly sparse, individual experts typically remain large and dense. Here, we demonstrate that further increasing sparsity by shrinking each expert to consist of a single neuron and selecting a tiny fraction of many available neurons can improve compute efficiency and interpretability. Counterintuitively, the key to achieving both is removing the nonlinearity typically applied to the experts, resulting in a network of sparsely gated linear neurons (sgatlin). In an isoflop comparison, we find that replacing all transformer feedforward layers with sgatlin improves perplexity in language models across different compute budgets. At the same time, the sparsity and linearity of the resulting feedforward circuits present new opportunities for model interpretability. In a small-scale case study, we demonstrate that feedforward circuits in sgatlin can be interpreted without having to train additional replacement models. We find that they form semantically structured clusters and are causally implicated in factual recall. Our findings paint a possible path towards compute-efficient and interpretable transformer feedforward layers.

---


### 180. [Video-Based Prediction of In-Flight Particle Characteristics in Atmospheric Plasma Spraying](https://arxiv.org/abs/2606.07416)

**<font color=#1a73e8>作者：</font>** Abhijeet Praveen, Sareh Soleimani, Cormac Cureton 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Atmospheric plasma spraying (APS) is a widely used coating process in which in-flight particle temperature and velocity strongly influence coating quality. However, these particle characteristics are difficult to monitor continuously during operation, motivating the development of non-invasive data-driven diagnostic methods. In this work, we investigate the predictive potential of high-speed video observations of the plasma plume for estimating in-flight particle characteristics in APS. We introduce three different video-derived feature representations and evaluate them using Tabular Prior-Data Fitted Networks (TabPFN), convolutional neural networks (CNN), and classical regression baselines including Random Forest, Gradient Boosting, Support Vector Regression, and XGBoost. Experiments are conducted using grouped leave-one-out cross-validation on 126 labeled pre- and post-spray video recordings from 63 APS spray runs. Across the engineered feature experiments, TabPFN achieves the most consistent performance for temperature prediction, reaching R2 = 0.86 using the combined feature representation. CNN models particularly perform stronger for velocity prediction, achieving R2 of 0.81. In addition, we evaluate models operating directly on raw video frames using pretrained CNNs and find that the highest performance is achieved by a pretrained CNN with a regression head with R2 of 0.90 and 0.82 for temperature and velocity, respectively. The results demonstrate that video-derived plume information provides a promising and scalable foundation for non-invasive APS diagnostics and real-time process monitoring.

---


### 181. [DisPOSE: Projected Polystochastic Diffusion for Self-Supervised Multi-View 3D Human Pose Estimation](https://arxiv.org/abs/2606.07419)

**<font color=#1a73e8>作者：</font>** Tony Danjun Wang, Tolga Birdal, Nassir Navab  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering 3D human poses for multiple individuals from different camera views is a fundamental bottleneck for analyzing interacting behaviors. Existing self-supervised approaches leverage synthetic catalogues of 3D poses; however, this leads to poor generalization in real-world scenarios due to distribution shifts. We therefore introduce DisPOSE, a self-supervised framework that approximates the inherently discrete multi-view person-assignment problem as a generative diffusion process over the space of polystochastic tensors. By employing differentiable Sinkhorn projections during denoising, our model learns to guide solutions toward valid and feasible assignments based on 2D image priors. The complete 3D skeletons of localized individuals are then regressed using a Hypergraph-Convolutional Decoder that explicitly models relational structures and articulated joints across multiple views. The proposed approach outperforms current state-of-the-art self-supervised methods on standard datasets and demonstrates strong performance on a newly proposed benchmark featuring highly occluded scenes from surgical operating rooms. Our diffusion-based localization demonstrates high label efficiency, retaining 99% of its performance with only 10% of the pseudo-labels. Notably, disentangling the assignment and root regression components while maintaining differentiability makes DisPOSE nearly agnostic to different camera arrangements.

---


### 182. [Lost in Migration: Exposing Android Framework Vulnerabilities in Parallel Java-Kotlin Implementations](https://arxiv.org/abs/2606.07420)

**<font color=#1a73e8>作者：</font>** Rui Li, Wenrui Diao, Debin Gao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Android has adopted Kotlin alongside Java across apps and core system components. During this shift, we observe parallel implementations in the Android Open Source Project (AOSP) where the same component is implemented in both Java and Kotlin. In principle, their functional purposes are identical. In practice, subtle semantic divergences can appear. Such divergences are not vulnerabilities by themselves, but they provide useful clues that may reveal flaws in surrounding enforcement logic. To the best of our knowledge, this paper presents the first systematic study of Java-Kotlin parallel implementations in the Android framework and examines their security implications. We design and build ParaDroid, an analysis framework that identifies parallel methods at scale and compares their behaviors. ParaDroid normalizes code into a bytecode-level intermediate representation, reconstructs class-to-source mappings, and uses large language models to reason about method semantics and identify behavioral divergences. Evaluated on AOSP Android 14-16, ParaDroid identified 329 parallel method pairs and 37 vulnerable divergences. We responsibly disclosed the exploitable issues to the Android Security Team. Three vulnerabilities and two bugs have been confirmed, and two CVE IDs have been assigned. Our results demonstrate that parallel Java-Kotlin code paths provide a practical surface for discovering security flaws in modern Android.

---


### 183. [Discovering Multiscale Deep Formulas in Complex Systems via Neural-Guided Lambda Calculus](https://arxiv.org/abs/2606.07426)

**<font color=#1a73e8>作者：</font>** Hanqiao Yu, Shusen Yang, Xuebin Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fundamental problem in science is identifying underlying patterns of complex systems in the form of concise mathematical formulas. Current Artificial Intelligence (AI)-based methods have shown strong performance in single-scale systems, yet remain limited in identifying scale-specific formulas in multiscale complex systems. We present Deflex, an end-to-end AI method to automatically extract multiscale formulas with potentially different forms, including invariants and distributions, from complex systems. Deflex consists of two subsystems named Deflexformer and Deflexpressor. Deflexpressor is a lambda-calculus symbolic regression model for higher-order formulas. Deflexformer is a decomposable deep energy model for learning unified representations across scales. Deflexpressor generates synthetic data to pre-train Deflexformer, which then guides formula discovery by decoupling multiscale latent relationships. Across six representative complex systems with diverse behaviors, Deflex achieves up to 7-fold higher efficiency than the state-of-the-art methods while enabling automated multiscale discovery. Our work could be a useful tool for scientific discovery across disciplines.

---


### 184. [OpenGlass: Open-Source Smart Glasses for On-Device Event-Based Gesture Recognition](https://arxiv.org/abs/2606.07431)

**<font color=#1a73e8>作者：</font>** Pietro Bonazzi, Julian Moosmann, Ahmet Celik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Smart eyewear enables unobtrusive, context-aware interaction through multimodal sensors and on-device intelligence, but is severely limited by power, memory, and compute constraints in a compact form factor. Open-hardware platforms supporting event-based vision and embedded ML at this scale are rare. This work introduces an open-source smart glasses platform for rapid prototyping of novel sensors and algorithms. Its modular design uses a flexible FPC interposer to support both event-based and frame-based cameras without full PCB redesign. A hardware-software co-designed power management system combines a configurable PMIC with event-driven wake-up via an nRF5340 coordinator, keeping the GAP9 RISC-V SoC powered down between inferences. The prototype achieves up to 11.8 hours of continuous on-device ML from a 200 mAh battery. As a demonstration, an egocentric hand gesture recognition pipeline was evaluated on the LynX dataset using polarity-separated event histograms from a Prophesee GENX320 camera. R(2+1)D achieved the best cross-subject accuracy of 83.94\% (macro F1 = 0.781) under leave-two-subjects-out validation, with 33.9 ms end-to-end latency on the GAP9. Temporal augmentation and removal of ambiguous classes provided the largest gains (+8.9 pp). All hardware designs, firmware, and models are released open source.

---


### 185. [The Lipreading Gap: Do VSR Models Perceive Visual Speech Like Human Lipreaders?](https://arxiv.org/abs/2606.07435)

**<font color=#1a73e8>作者：</font>** Rishabh Jain, Naomi Harte  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual speech recognition (VSR) models now surpass human lipreaders on benchmarks, but do such gains establish human-like visual speech perception? To explore this, we compare three VSR systems with human baselines on the MaFI word-level lipreading dataset using word, character, phoneme, and viseme-level metrics. Although models achieve higher overall accuracy, they succeed and fail on different words than humans. A text-only n-gram baseline given only a few initial phonemes rivals human lipreading. VSR word-level errors are consistently better explained by training word frequency than by the visual informativeness of words. Viseme accuracies, confusion matrices and human-model correlations further show that models gain most on visemes humans find hardest, and show much weaker dependence on visual clarity. Our work demonstrates that VSR systems rely primarily on language cues from training data rather than visual perception, failing to bind visual features into meaningful words.

---


### 186. [Verifiable and Confidential DNN Inference on Low-End Edge Devices](https://arxiv.org/abs/2606.07470)

**<font color=#1a73e8>作者：</font>** Mohamed Khalil Kiri, Ivan De Oliveira Nunes, Aurélien Francillon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deploying deep neural network (DNN) inference on low-end edge devices raises two key challenges: protecting model confidentiality against a potentially compromised edge system and enabling verifiable inference without incurring prohibitive overhead. Existing approaches either house partial models and inference software within trusted execution environments (TEEs), resulting in high cost and an application-dependent trusted computing base (TCB), or execute in untrusted environments, providing little security.
In this work, we present VECODI, a framework for verifiable and confidential DNN inference on constrained edge devices. At its core, VECODI introduces SHANGRI-LA, a new execution abstraction on TrustZone-M TEEs that establishes a third runtime environment with privileges strictly between the Secure and Non-Secure Worlds. VECODI leverages SHANGRI-LA to execute untrusted inference code in the Non-Secure World while using minimal application-agnostic Secure-World support to protect model confidentiality and enable verifiability (with respect to proper execution of inference code and model parameters) of inference results. We realize VECODI on a real-world NUCLEO-L552ZE-Q development board and open-source its prototype. Our results show VECODI's small TCB, memory footprint, and runtime overhead, making it a practical option for secure inference in low-end edge devices.

---


### 187. [Unsupervised Continual Clustering via Forward-Backward Knowledge Distillation](https://arxiv.org/abs/2606.07474)

**<font color=#1a73e8>作者：</font>** Mohammadreza Sadeghi, Sareh Soleimani, Zihan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised Continual Learning (UCL) aims to enable neural networks to learn sequential tasks without labels or access to past data. A major challenge in this setting is Catastrophic Forgetting, where models forget previously learned tasks upon learning new ones. This challenge is amplified in UCL due to the absence of labels to guide learning and memory retention. Existing mitigation strategies, such as knowledge distillation and replay buffers, often raise memory and privacy concerns. Moreover, current UCL methods largely overlook clustering-specific objectives. To fill this gap, we introduce Unsupervised Continual Clustering (UCC) and propose Forward-Backward Knowledge Distillation for Continual Clustering (FBCC). FBCC employs a continual teacher network with a clustering projector and lightweight task-specific students. Through a dual-phase forward-backward distillation process, the teacher learns new clusters while preserving previously discovered cluster structure without storing past data. FBCC represents a pioneering approach to UCC, demonstrating improved clustering performance across sequential tasks. Experiments on four benchmark datasets demonstrate that FBCC consistently outperforms existing continual learning baselines in clustering accuracy while significantly reducing catastrophic forgetting.

---


### 188. [Drifting Models for Surrogate Flow Modeling](https://arxiv.org/abs/2606.07481)

**<font color=#1a73e8>作者：</font>** Chris R. Jung, Markus Dörr, Natalie Jüngling 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Computational Fluid Dynamics (CFD) provides high-fidelity flow fields for optimizing indoor environments, its computational cost limits rapid exploration. To solve this problem generative surrogates offer better distribution modeling than deterministic networks, but iterative sampling is slow. To enable high-quality, single-pass generation, we adapt the novel generative drifting framework to fluid mechanics. We introduce a conditional architecture that performs drifting in a learned VAE latent space and uses label-aware masking to align generated samples with their boundary conditions. Our label-conditioned model matches iterative diffusion in accuracy and flow consistency while running two orders of magnitude faster. Additionally, we propose a spatial-conditioning variant that establishes a promising path towards generalization to unseen geometries. Ultimately, conditional drifting serves as a highly efficient alternative to diffusion based approaches, unlocking real-time CFD surrogates where inference speed is critical.

---


### 189. [Network Recovery from Cascade Data: A Debiased Jacobian-Based Machine Learning Approach](https://arxiv.org/abs/2606.07483)

**<font color=#1a73e8>作者：</font>** Lei Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many important outcomes unfold as dynamic cascades, including product adoption, disease spread, financial distress, and information diffusion. A central challenge is to recover the hidden influence network behind these cascades. Existing methods typically assume a specific diffusion model, and their performance degrades substantially when that assumption is misspecified. We propose CascadeNet, a Jacobian-based machine learning framework for network recovery that does not require specifying a diffusion mechanism. The key idea is that the underlying influence structure can be characterized by the Jacobian of the one-step transition function. CascadeNet first constructs a flexible estimator of the transition function, and further applies Neyman-orthogonal debiasing via the Riesz representer, so that the debiased Jacobian is $\sqrt{n}$-consistent and asymptotically normal, enabling formal inference on the network structure. We validate CascadeNet in both a simulation exercise and a real-world empirical application. In simulations, where the data-generating process is known, CascadeNet achieves the highest network recovery accuracy across nine common data-generating processes. In an empirical application to COVID-19 transmission across Spain's 52 provinces, CascadeNet recovers transmission networks that are significantly correlated with the true inter-province mobility network, whereas networks recovered by baseline methods show no significant alignment with the ground truth.

---


### 190. [Modelling Opinion Dynamics at Scale with Deep MARL](https://arxiv.org/abs/2606.07487)

**<font color=#1a73e8>作者：</font>** Lukas Seier, Brandon Kaplowitz, Sebastian Towers 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Modelling opinion dynamics typically relies on hand-crafted local interaction rules to study emergent macroscopic phenomena such as consensus and polarisation. In contrast, multi-agent reinforcement learning (MARL) enables agents to learn such behaviours directly by optimising simple rewards. To explore the potential of MARL for opinion dynamics, we introduce a GPU-accelerated consensus and truth-finding game that scales to populations of up to 1000 agents, comparable to many real-world social sub-networks. To prevent unrealistic conventions, we extend other-play to general-sum social interactions. We next validate our model on a subset of the Bluesky network by recovering agent importance structures from graph topology alone via a learned attention layer, finding that highly conforming populations most closely match human data. In large social media networks such high levels of conformity significantly reduce collective accuracy and promote dishonest agents that lie to fit in. By contrast, small, dynamic hunter-gatherer networks are less affected; here, conformity can even improve collective agreement. This suggests a mismatch between evolved human conformity heuristics and modern social media environments as a potential contributor to misinformation.

---


### 191. [CoMetaPNS: Continually Meta-learning Personalized Neural Surrogates for Cardiac Electrophysiology Simulations](https://arxiv.org/abs/2606.07488)

**<font color=#1a73e8>作者：</font>** Ryan Missel, Xiajun Jiang, Linwei Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized virtual heart simulations face challenges in model personalization and computational cost. While neural surrogates offer state-of-the-art solutions, they typically address either efficient personalization or training generalizable models. Recent work reframes this by learning the process of personalizing a surrogate using limited subject-specific context data, through few-shot generative modeling with set-conditioned surrogates and meta-learned amortized inference. These methods, however, assume a static and diverse training distribution with known task identifiers. When new data becomes available, they require costly retraining with all prior data to avoid catastrophic forgetting - a phenomena where the model forgets earlier tasks when trained on new ones. This is a major limitation in clinical settings where often unlabeled data arrives sequentially and full retraining is infeasible. This paper presents a new continual meta-learning framework to achieve personalized neural surrogates able to not only continually integrate information but also identify whether incoming data stems from a known or unknown dynamics source. By leveraging a continual Bayesian Gaussian Mixture Model over a memory buffer, our framework can infer the identifiers and relationships of data over time - required for effective meta-learning. Empirical results on synthetic cardiac data demonstrate superior simulation forecasting, computational scalability, and resilience to catastrophic forgetting compared to existing baselines.

---


### 192. [How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope](https://arxiv.org/abs/2606.07489)

**<font color=#1a73e8>作者：</font>** Jeremy Yang, Kate Zyskowski, Noah Yonack 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier AI systems are bridging the gap between intelligence and utility by shifting from conversational assistants to autonomous agents that execute tasks end to end. Using production data from Perplexity's Search and Computer products, we study this transition by examining how AI agents accelerate and reshape knowledge work. Three key empirical findings emerge. First, using sessions with near-identical initial query pairs as natural experiments for the same underlying task attempted with both products, Computer performs 26 minutes of autonomous work per user session, versus 33 seconds for Search. Computer automates task decomposition and execution that Search users might otherwise manually orchestrate and implement. As a result, Computer shifts follow-up query distribution toward higher-order work such as verification and extension. Autonomy also increases execution quality, with per-query dissatisfaction rates 55% lower on Computer than on Search. Second, due to its autonomy advantage, Computer reduces completion time from 269 to 36 minutes on matched tasks, lowering estimated time and cost by 87% and 94%, respectively, compared to humans equipped with Search alone. Third, Computer changes the scope of work that users attempt: Computer queries more often cross occupational boundaries, require higher-order cognition, draw on broader expertise, take the form of composite tasks that bundle interdependent subtasks into a single query, and unlock work activities that are essentially absent from Search usage among the same users. Together, the evidence indicates that AI agents accelerate workflows, enhance output quality, reduce costs, and expand the breadth and depth of automated work.

---


### 193. [Second-Order Path Kernel Interpolation Formulas in Machine Learning](https://arxiv.org/abs/2606.07495)

**<font color=#1a73e8>作者：</font>** Jin Guo, Roy Y. He, Jean-Michel Morel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how training data shape neural network predictions is a central problem in modern learning theory. In 2020, Pedro Domingos proposed an interpolation formula valid for every model learned by deterministic gradient descent. It expresses the model's prediction as an integral, along the optimization path, of a data-dependent kernel that aligns the model's gradients at the test and training data. Such a first-order characterization remains valid for models trained with batch-based stochastic optimization. In this paper, we develop second-order forms of these interpolation formulas. We show that the leading path-kernel interpolation is supplemented by a curvature-weighted interpolation term. For stochastic gradient descent, an additional sampling-induced component appears, coupling the curvature of the prediction with the covariance of mini-batch gradient noise. We also extend the representation to stochastic gradient descent with momentum, where the interpolation structure is preserved but with the weights modified by a memory-related factor. Moreover, we establish a concentration estimate for the terminal prediction, identifying the fluctuation scale around the expected second-order representation. Together, these results provide a refinement of the path-kernel interpretation of neural network prediction.

---


### 194. [Accelerated Decentralized Stochastic Gradient Descent for Strongly Convex Optimization](https://arxiv.org/abs/2606.07496)

**<font color=#1a73e8>作者：</font>** Ming Sun, Kun Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized stochastic optimization is a fundamental paradigm for large-scale learning over networks, where agents communicate only with their neighbors and no central coordinator is required. For strongly convex problems, communication efficiency is mainly determined by the condition number \(\kappa=L/\mu\) and the network spectral gap \(1-\beta\). Although deterministic decentralized methods can simultaneously achieve accelerated \(\sqrt{\kappa}\) and \(1/\sqrt{1-\beta}\) dependences, no existing stochastic method attains both improvements at once. In this paper, we propose \emph{Multi-Gossip Accelerated DSGD} (MG-ADSGD), a decentralized stochastic algorithm that combines Nesterov-type primal--dual extrapolation with multi-round fast gossip averaging. The key idea is to couple the gossip depth with the mini-batch size so that additional communication rounds simultaneously improve consensus accuracy and reduce gradient variance. We show that MG-ADSGD achieves the communication complexity \[ \widetilde{\mathcal O}\!\left( \frac{\sigma^2}{\mu n\epsilon}\log\frac{1}{\epsilon} +
\sqrt{\frac{\kappa}{1-\beta}}\log\frac{1}{\epsilon} \right), \] where \(\epsilon\) denotes the target accuracy, \(n\) is the number of nodes, and \(\sigma^2\) is the gradient variance. To the best of our knowledge, this bound yields the best currently available communication complexity for decentralized stochastic strongly convex optimization, up to logarithmic factors that are independent of $\epsilon$.

---


### 195. [Implicit Data Synthesis for Contrastive Unsupervised Data Augmentation](https://arxiv.org/abs/2606.07498)

**<font color=#1a73e8>作者：</font>** Patrick Kage, Trevor Hedges, N. Siddharth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific observations generate large quantities of unlabeled data which is laborious to hand-label, making unsupervised learning techniques valuable for processing datasets. Among these approaches, contrastive learning provides a convenient mechanism for extracting structural representations from unannotated datasets. For natural imagery, the general approach is to use a variety of data-space augmentation methods in order to generate synthetic samples; however, for scientific observations data-space perturbations can fundamentally alter the underlying data. Our proposed method is to generate contrastive samples by perturbing the network weights rather than the underlying data, thus more closely preserving the structure of the data. We demonstrate this technique using a SimCLR-based pipeline applied over radar observations of meteors, and show performance gains under matched protocols.

---


### 196. [Differences in Detection: Explainability Where it Matters](https://arxiv.org/abs/2606.07503)

**<font color=#1a73e8>作者：</font>** Johannes Theodoridis, Johannes Maucher, Andreas Schilling  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Differences in Detection (DnD), an intuitive method to compare two object detection models. Based on the same matching algorithm, it complements the standard metrics of mean Average Precision ($mAP$) and TIDE error analysis with the ability to compare two models directly. More specifically, we calculate the intersection of ground truth labels that are recognized by both models, followed by the corresponding difference sets and the complement set of ground truth labels that are missed by both models. The resulting comparison is more direct and intuitive than a comparison of independent summary statistics. It reveals individual and shared mistakes and becomes particularly interesting when combined with error types. In this case, the differences in detection errors can be analyzed naturally in a standard confusion matrix. While valuable in itself, we believe that one of the best applications of DnD is to guide explainability methods such as ODAM towards metric-relevant examples, grounded in structured subsets. The code for our method is available here: this https URL

---


### 197. [Streaming Video Generation with Streaming Force Control](https://arxiv.org/abs/2606.07508)

**<font color=#1a73e8>作者：</font>** Hanhui Wang, Yiming Xie, Haiwen Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce StreamForce, a streaming video generation framework that enables physically grounded control through continuous force inputs. Unlike prior video models that train separate models for different force types, assume fixed forces, or rely on non-causal processing, StreamForce is a causal and unified model that responds instantly and coherently to both local and global, time-varying forces. To achieve this, we design a unified force representation as a control signal and develop a distillation pipeline for force-controllable video generation. Our model combines autoregressive efficiency with force responsiveness, sustaining stable photometric and dynamic realism. StreamForce runs at up to 16.6 FPS on a single GPU, achieving state-of-the-art performance in both force adherence and motion realism. Project website: this https URL

---


### 198. [Agentopia: Long-Term Life Simulation and Learning in Agent Societies](https://arxiv.org/abs/2606.07513)

**<font color=#1a73e8>作者：</font>** Xintao Wang, Sirui Zheng, Hongqiu Wu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans learn from social life. Simulating this process with LLM-powered agents represents a promising research direction, raising a natural question: whether LLMs can learn from such simulated social experience to better understand and replicate human behavior. However, prior agent society simulations typically operate at the scale of days, limiting the depth of social interactions and long-term growth. In this paper, we study long-term life simulation and LLM learning in agent societies, with two goals: (1) investigating social behaviors that emerge from life-long simulation, and (2) developing anthropomorphic capabilities in LLMs, particularly intelligence in social life, through years of simulated social experience. Specifically, we present Agentopia, a comprehensive framework for long-term life simulation in multi-agent societies, where 100 agents autonomously pursue personal growth, develop social relationships, and fulfill their needs and goals over 10 simulated years. We define life reward to mirror human well-being, and leverage this reward to train LLMs via rejection sampling. Extensive experiments show that agents exhibit rich emergent social behaviors. Furthermore, life reward training effectively enhances the underlying LLM, which leads to improved agent well-being in simulation, and generalizes to downstream role-playing benchmarks with +15.6% improvement.

---


### 199. [UniSHARP: Universal Sharp Monocular View Synthesis](https://arxiv.org/abs/2606.07514)

**<font color=#1a73e8>作者：</font>** Meixi Song, Dizhe Zhang, Hao Ren 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we focus on extending SHARP, the popular photorealistic view synthesis method, for universal monocular rendering across a continuum of camera systems, from conventional perspective cameras to wide-field-of-view, fisheye and omnidirectional panoramic settings. To overcome the pinhole-specific assumptions of SHARP, our key idea is to align various images in a unified omnidirectional latent space. Thus, we propose UniSHARP, which performs implicit alignment in both feature and Gaussian spaces. Specifically, Gaussian primitives are arranged along rays and radial distances in a ray-based universal representation, while 2D semantic and 3D spatial features extracted from UniK3D-inspired encoders are jointly decoded to generate the complete Gaussian cloud. To comprehensively evaluate our method, we construct a benchmark covering diverse imaging systems across various scenes. The benchmark is further stratified by field of view (FoV) to enable fine-grained assessment of the universal monocular rendering task. Extensive experiments on the proposed benchmark demonstrate the effectiveness of UniSHARP, outperforming alternative methods by a large margin. The project page can be found at: this https URL

---


> [!TIP]
> 当前位于：**151-199**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-199**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
