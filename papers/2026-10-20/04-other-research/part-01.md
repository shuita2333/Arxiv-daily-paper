# 📦 其他研究 | 2026年10月20日

> 本类共 **213** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-213](./part-05.md)

---

### 1. [Trust but Verify: Designing Region-Inhomogeneous Forward Dynamics for Discrete Diffusion](https://arxiv.org/abs/2610.22380)

**<font color=#1a73e8>作者：</font>** Gunmay Jhingran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion treats the forward process as a design space; discrete language diffusion often uses absorbing corruption, leaving context fully trusted throughout generation. This makes trust binary: corrupted context is copied as ground truth, propagating errors into generated spans. We reopen this design space by combining absorbing and uniform-mixing kernels with region-dependent rates. Missing positions follow absorbing dynamics, while context undergoes low-rate random substitution, exposing the model to observed but uncertain tokens during training. At inference, a heuristic sampler re-injects noise into suspicious context under an annealed intensity and freezes context updates late in the trajectory. An 8,000-step finetune of a pretrained 170M-parameter masked diffusion model takes under five hours on a 6 GB laptop GPU. The base model assigns roughly 50% probability to observed tokens even when they are uniform-random garbage. For uniform-random corruption, finetuning detects corrupted context with 0.96 recall and 0.91 precision, improves infill token-F1 by 3.8 points at 10% corruption and 6.4 points at 20%, and removes the accuracy dip next to corruptions. Clean conditioning shows no measurable regression, with a false-edit rate below 0.4%. Gains for plausible corruptions are weaker: about 0.5 F1 points at 10% corruption, without statistical significance. Our results suggest that detectability and damage depend jointly on departure from the data conditional: nearby noise is hard to detect and semantically mild, while distant noise is conspicuous and destructive. We interpret absorbing diffusion as the infinite-contrast limit of a trust axis, analogous to the signal-to-noise gap between known and unknown regions in diffusion inpainting. In our setting of a 170M model and a single text domain, intermediate trust is reached by changing forward dynamics rather than architecture.

---


### 2. [From Events to Reasoning: Hierarchical Rule Composition over Explicit States](https://arxiv.org/abs/2610.22403)

**<font color=#1a73e8>作者：</font>** Cheng Lyu, Xueqi Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What a reasoning system emits is a conclusion; what it owes is a justification. Producing one requires every operation to be admissible on the facts actually available, the dependencies of intermediate results to survive to the end of the path, and the path to be revised when a premise changes. We present the Event Reasoning System (ERS), in which the reasoning state is an explicit event graph. Semantic features nominate candidate objects and rule bindings, and declared rule and task conditions decide which may execute, so candidates that violate the represented period, unit, or evidence constraints cannot enter an accepted reasoning path. Low-level rules provide reusable local transformations, and recursively composable high-level control rules organize subgoals and legal paths under the current goal, information gaps, and budget; a finite library is thereby rebound into paths never stored as complete solutions. We formalize admissible transitions, task-dependent control, compositional expressivity, dependency-preserving revision, and the gap between reachable solutions and those a budgeted controller finds. On structured-event graphs, ERS builds dependency chains of up to twelve steps, cuts irrelevant executed domain operations from 32 to 0 as lookahead grows to 16, and produces no unsupported target output across 24 negative cases; with rules frozen, it passes 12/12 focused checks comprising nine accepted derivations involving unseen input/path combinations and three justified refusals, as well as 6/6 fact-change cases. On fourteen jointly solved development tasks, the recorded dynamic subgoal configuration uses 51.6% less inference wall-clock time than single-level global control under their respective frozen settings.

---


### 3. [Sensitivity Analysis of Decision Rules in an Agent-Based Agro-Ecological Model](https://arxiv.org/abs/2610.22420)

**<font color=#1a73e8>作者：</font>** Benjamin Pianet, Baptiste Lesquoy, Paul Saves 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent-based models are well-suited for modelling agro-ecological systems for decision-making, yet turning their simulations into actionable insight requires identifying which decisions actually drive the behaviours. In such a context, sensitivity analysis stumbles upon a structural feature of many complex systems: the parameters are not a flat vector but a decision tree in which many parameters appear only when a higher-level choice activates them. Classical global sensitivity analysis presupposes independent inputs over a fixed Cartesian product and is ill-posed on such a branched space and biased by construction. We instead treat the structure of the decisions as a first-class modelling object. Using advanced surrogate modelling techniques, we encode the crop-management itinerary of the high-resolution agro-ecological modelling platform MAELIA as a hierarchical design space featuring both categorical and numerical variables. We propose a novel dedicated method to analyse this kind of hierarchical space, a random-forest-supervised HSIC-ANOVA, which ranks main effects and interactions natively on the tree while placing rarely and always active decisions on an equal footing. We show how, when applied to simulation outputs such as nitrogen leaching, soil organic carbon variation, and yield predictions, it can deliver an interpretable, decision-oriented reading.

---


### 4. [CGDT-CESN: Correlation-Guided and Dynamics-Trained Clustered Echo State Network for Multivariate Time-Series Prediction](https://arxiv.org/abs/2610.22430)

**<font color=#1a73e8>作者：</font>** Hariharan Srinivasan, Masoom Bhargava, Sayan Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of multivariate time series requires models that simultaneously capture variable-specific dynamics and cross-variable interactions. In this work, a Correlation-Guided and Dynamics-Trained Clustered Echo State Network (CGDT-CESN) is proposed, which comprises a modular reservoir architecture with each cluster distinctly specializing in one of the variables in the multivariate time series. An innovative reservoir design is proposed in which inter-cluster connections are enabled by empirically observed correlations among variables, providing a data-driven coupling mechanism. Apart from conventional readout training, inter-cluster connection weights informed by correlations are trained, which in turn allows the reservoir to capture time-varying cross-variable dependencies without sacrificing computational efficiency and further improves forecasting accuracy. The prediction performance of CGDT-CESN is found to be superior to that of the conventional ESN when evaluated on two fundamentally different datasets: Twitter information cascade evolution and solar wind forecasting. Also, the improvement in performance is preserved across multiple prediction horizons, even when presented with a low volume of data. By unifying cluster-specific specialization with learned inter-variable coupling, CGDT-CESN offers a principled, data-driven route to multivariate time series prediction.

---


### 5. [BOLT: Multi-Bottleneck Bound-Guided Learning for Flexible Job-Shop Scheduling with Time Lags and Resource-Coupled Transport](https://arxiv.org/abs/2610.22433)

**<font color=#1a73e8>作者：</font>** Ziheng Zhang, Wei Zhang, Yunyi Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flexible job-shop scheduling becomes resource-coupled when a scarce vehicle fleet moves jobs between stations, because the schedule sets the transport waits. BOLT (bound-oriented learning for transport-coupled scheduling) builds a lower bound from chain, machine-capacity, and fleet-capacity relaxations. The bound equals the makespan at termination, so its per-step changes form a reward that sums to a constant minus the makespan. Because it never exceeds the attainable makespan, each candidate's bound increase is a proven rise of the makespan floor, which the policy reads as a price. The root bound certifies a completed schedule's suboptimality gap without a solver. On industry-motivated 10-module prefabricated-construction instances, explicit transport coupling outperforms a transport-penalty policy in every tested cell where loaded moves occupy at least 66% of fleet time and in none at or below 56%. Across five zero-shot 50- and 80-module production batches, BOLT outperforms the best dispatching-rule pair on four and the penalty policy on the three with long moves. In the three-vehicle 80-module batch, its mean makespan is 13.0% below the best pair and 4.2% below an hour-budget constraint-programming solver whose proven gap averages 34%. BOLT decides in 2.3-5.9 ms per event on one processor core and re-plans a disruption in seconds.

---


### 6. [TRACE: Transformer Residual Activation Codebook Encoding for Communication-efficient Distributed Edge Inference](https://arxiv.org/abs/2610.22435)

**<font color=#1a73e8>作者：</font>** Muhammad Azlan Qazi, Alexandros Iosifidis, Qi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributed Transformer inference across co-located edge devices is fundamentally communication-bound, as exchanging activations between sequence-parallel partitions dominates inference latency under commodity edge bandwidths. Existing compression schemes reduce this cost but retain a structural bottleneck: the received data must still undergo key/value projection before attention can proceed, serializing computation behind communication. This paper presents Transformer Residual Activation Codebook Encoding (Trace), a framework that addresses these limitations. Trace places a Vector Quantizer (VQ) at the post-attention residual of every Transformer layer and precomputes codebook-indexed key/value representations. During inference, exchanged activations are encoded into compact codebook indices, allowing receivers to directly recover keys and values through table lookup instead of executing the downstream computations required to derive them. By eliminating the received data downstream computation, Trace enables communication--computation overlap and reduces a key latency bottleneck in distributed Transformer inference. A hierarchical clustering further structures the learned codebook into a multi-resolution hierarchy, enabling runtime adaptation of the communication bitrate without retraining. The framework supports two operating variants: one prioritizing accuracy and the other balancing accuracy and efficiency through buffer-compatible quantization. Experiments on ViT-Base (ImageNet-1K and CIFAR-100) and ViViT-B (UCF-101) show that Trace achieves up to 1.89% higher accuracy and up to 1.27x end-to-end inference speedup compared with the state-of-the-art VQ-based distributed inference framework. Compared with uncompressed sequence-parallel inference, Trace reduces communication overhead by up to 22,624x.

---


### 7. [Generative adversarial networks with Monte Carlo dropout uncertainty quantification for structural health monitoring: Fibre Bragg grating data augmentation comparison in Hawk T1A aircraft](https://arxiv.org/abs/2610.22436)

**<font color=#1a73e8>作者：</font>** Alvaro Peiro, Marios Impraimakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The signal generation capabilities of a novel data augmentation framework are examined in aerospace structures. First, the framework learns class-conditional temporal and spectral characteristics of the measured structural responses. It uses conditional generative adversarial network training and Monte Carlo dropout uncertainty quantification as a Bayesian approximation. This step enables stochastic signal synthesis and uncertainty quantification. Second, the generated responses are rigorously compared against experimental measurements across time, frequency, uncertainty, variability, and feature domains to assess physical realism, statistical consistency, and distributional fidelity. Finally, the synthetic data are evaluated to determine whether they should be incorporated into a supervised damage classification workflow. The framework is validated on the full-scale benchmark dataset from a BAE Systems Hawk T1A aircraft tested at the University of Sheffield's Structural Dynamics Laboratory for Verification and Validation. The test involves acceleration, fibre Bragg grating strain, and nonlinear dynamic response measurements. The results demonstrate that the model accurately captures dominant structural dynamics, it guides on signal use for classification improvement based on uncertainty characteristics, and it provides meaningful uncertainty estimates linked to signal complexity and excitation characteristics. Importantly, the framework offers a realistic generative modelling plan as a robust digital twin component for data-driven structural health monitoring, supporting resilient decision-making for condition assessment in safety-critical aerospace systems.

---


### 8. [CF-NODE: Counterfactual Spatial Node Intervention for Test-Time Adaptation Under Domain Shift, Evaluated Across Five Diabetic Retinopathy Datasets](https://arxiv.org/abs/2610.22437)

**<font color=#1a73e8>作者：</font>** Sabarish G, Deepak Parashar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated fundus-based diabetic retinopathy (DR) grading can substantially expand screening capacity, but source-trained models degrade sharply across different cameras, clinics, and patient populations. Existing test-time adaptation methods depend on entropy minimization or target information accumulated from image batches and streams. These mechanisms can reinforce confidently incorrect predictions and break down when clinical images arrive independently. We introduce CF-NODE, a novel counterfactual test-time adaptation framework for cross- domain DR grading. Instead of trusting prediction confidence or estimating a target distribution, CF-NODE asks how each prediction responds under a controlled intervention on the evidence supporting it. CF-NODE ranks internal spatial nodes using model-derived attention, feature magnitude, and node-set similarity, progressively attenuates the highest-ranked nodes, and uses the stability of the resulting expected-grade response to apply a bounded calibration of the predicted grade distribution. The framework is fully frozen and adapts every image independently using only geometric views and a fixed source-derived prior, requiring no target-derived information or model updates. We evaluate CF-NODE on five external DR datasets under repeated-seed evaluation against TENT, EATA, SAR, and T3A. CF-NODE outperforms all four methods with statistically significant improvements over the second-best method, improves AUC on every target domain, and attains the highest average AUC and macro-F1, delivering stronger grade discrimination together with more balanced recognition across DR severity levels. These results demonstrate that counterfactual intervention sensitivity provides consistent and deployment-ready domain robustness for single-image clinical inference.

---


### 9. [Sparse Autoencoders Can Induce Local Geometry for Mitigating Catastrophic Forgetting](https://arxiv.org/abs/2610.22439)

**<font color=#1a73e8>作者：</font>** Kamil Faber, Katarzyna Filus, Łukasz Pawela  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting remains a challenge in supervised continual learning, as adapting to new tasks causes representation drift and loss of previously learned information. This raises the question of which representational changes should be constrained while preserving plasticity. We therefore introduce Sparse Autoencoder Geometric Anchoring (SAGA), which converts a Sparse Autoencoder (SAE) trained at each task boundary into local, low-rank constraints on representation drift. Replay examples specify where the constraints apply, while leading right singular directions of the encoder Jacobian specify which changes are penalized. The resulting geometry is input dependent and can be retained without keeping the SAE for subsequent tasks' training. We establish its local relation to latent code matching, define its spectral truncation error, and derive a conditional bound on frozen-readout drift. With replay and snapshot history, the method achieves the highest mean Class-IL accuracy and lowest mean forgetting among the evaluated ER, DER++, ER-ACE, and SGD baselines on three pretrained ViT-B/16 benchmarks, with accuracy gains of 12.15, 4.79, and 3.22 percentage points over the strongest conventional baseline on CIFAR-100, CUB-200, and ImageNet-R, respectively. From scratch results are more mixed, while rank ablations and geometry controls show that SAE-induced low-rank geometry offers useful stability-plasticity trade-offs.

---


### 10. [Null Controls Are Necessary but Not Sufficient: Evaluating Acceptance Guards for Scientific Discovery and Interpretability](https://arxiv.org/abs/2610.22445)

**<font color=#1a73e8>作者：</font>** Tianyu Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated discovery systems propose scientific explanations and test which to accept. Does passing a test establish the intended claim? We develop four executable operations for changing physical descriptions: identifying redundancies (L1), coarse-graining dynamics (L2), transferring structure (L3), and inferring missing quantities from conservation imbalances (L4). We evaluate these operations and three interpretability settings through null acceptance (NAR), positive acceptance (PAR), and consequence agreement (CAR).
A reduction mapping every state to zero predicts its own future perfectly. It passes closure on 96% of 129 public chaotic systems despite retaining no dynamical variation. An independent observable-preservation test rejects it throughout. On controlled benchmarks, the combined criteria accept 24/24 genuine reductions and reject 72/72 nulls. The other operations distinguish symmetries from redundancies, validate transfers, and reject spurious conservation imbalances. In language and ESM-2 protein models, linear CKA remains unchanged when a proposed correspondence is randomly rotated, whereas localized interventions distinguish genuine mappings from tested nulls. In sparse autoencoders, enrichment rejects all 16 tested nulls, yet independent ablation supports 45% of evaluable enriched features, compared with 0.5% of matched controls.
These results reveal two acceptance gaps: descriptive tests can accept scientifically empty candidates, and accepted candidates can lack independently verified consequences. Reliable automated discovery requires evaluating both what a test accepts and the scientific consequences it establishes. Code and data: this https URL.

---


### 11. [Learnable Splines for Unstructured Neural Operators](https://arxiv.org/abs/2610.22446)

**<font color=#1a73e8>作者：</font>** Vignesh Gopakumar, Zhuoyuan Wang, Ander Gray 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural operators approximate solution operators of partial differential equations at a fraction of the cost of numerical solvers. Efficient grid-based architectures such as the Fourier neural operator (FNO) assume uniform rectangular grids, whereas engineering simulations use large, irregular, and locally refined meshes. We introduce L-SplineFNO, a memory-efficient neural operator that couples an FNO backbone with a sparse, learnable tensor-product B-spline transfer between unstructured meshes and a latent Cartesian grid. A local normalised scatter avoids the geometry-dependent solve of analytic spline transformation while preserving compact support, partition of unity, and spline smoothness by construction. The neural operator, conditioned on global design and operating parameters, learns the mapping of geometry to the field solution. Across six three-dimensional engineering benchmarks, L-SplineFNO achieves strong predictive accuracy while requiring substantially less memory and compute than baseline operators, scaling to 26.6 million nodes in training and 46 million in inference on a single A100 GPU. It also supports zero-shot super-resolution and efficient closed-form spatial derivatives. Uniquely, the analytic spline decoder yields rigorous prediction bounds over continuous space and uncertain parameters, via Bernstein convex hulls and Taylor models, demonstrated on a 29.2-million-node MAST-U tokamak model.

---


### 12. [Capital Costs Protect the Network: Mining Gap Dynamics in Proof-of-Work Blockchains Under a Stochastic Mempool](https://arxiv.org/abs/2610.22451)

**<font color=#1a73e8>作者：</font>** Hasan Selçuk Kılıç, Nail Akar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Proof-of-Work blockchains increasingly rely on transaction fees to keep miners engaged as block subsidies decline. An immediate outcome of this is that miners may sit idle at the start of a round until enough high-fee transactions accumulate in order to make mining worthwhile. This idle period is known as the mining gap. We model the high-fee transaction backlog as a Lindley-type recursion under a two-tier fee market and use its stationary distribution to characterize the mining gap. Under Bitcoin's difficulty-adjustment mechanism, the expected gap grows strictly with the hashpower active on the network and consumes the entire round as that hashpower grows without bound. A free-entry condition determines a unique long-run equilibrium hashpower. Capital cost caps the equilibrium hashpower and prevents the mining gap from occupying the entire round. We further characterize how the block subsidy, transaction fees, and operating cost shape the equilibrium hashpower and the mining gap.

---


### 13. [Erase the Mark, Preserve the Motion: Temporally Consistent Removal of Video Watermarks](https://arxiv.org/abs/2610.22457)

**<font color=#1a73e8>作者：</font>** Yifan Liao, Zhen Sun, Zhicong Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generation have increased the demand for reliable watermarking for copyright protection, yet the robustness of video watermarks against removal attacks remains underexplored. Most watermark-removal methods originate from the image domain: signal optimization injects imperceptible pixel-domain perturbations, whereas generative resynthesis produces a visually similar instance through diffusion synthesis. When extended to videos, the former introduces temporally varying noise that causes visible flickering, while the latter regenerates fine-grained structures inconsistently across frames, leading to structural motion inconsistency. To evaluate video watermark robustness, we propose PoseRegen, a pose-consistent reconstruction framework that removes watermarks while preserving the original content and motion. PoseRegen first applies a temporally shared viewpoint transformation to disrupt watermark-bearing spatial patterns and then jointly reconstructs the transformed sequence with a pose-conditioned video model. A frozen video DiT processes the complete sequence with its reference-video latent, and full-sequence Flow Matching supervision keeps identity and background consistent across frames. To further preserve motion structure, we introduce a lightweight Pose-Conditioned Motion Consistency Adapter that adapts the frozen backbone to temporally ordered pose guidance and constrains body-part trajectories throughout reconstruction. Experiments on eleven video watermarking schemes show that PoseRegen reduces the average bit accuracy to 0.505, near random guessing, while outperforming the strongest baseline by 9.34% on motion-related VBench metrics. These results reveal a practical vulnerability of current video watermarks and highlight the need to evaluate robustness jointly with temporal and motion quality.

---


### 14. [Everyone's a little bit racist: a novel ML backdoor attack in black-box mode](https://arxiv.org/abs/2610.22459)

**<font color=#1a73e8>作者：</font>** Michele Cerrta, Gabriele Costa  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoors are among the most impactful attacks against Machine Learning (ML), yet most existing methods assume some form of training-time poisoning or direct model manipulation. This is often considered sufficient to assume that existing systems are not exposed to actual risks. In this paper, we introduce Backdoor-as-a-Service, a model-agnostic, fully black-box technique that, instead of installing a backdoor, activates it in the form of a latent secondary task leveraging on an already present behavior. Our tool uses genetic search to discover input transformations that induce systematic output differences aligned with an attacker-defined task, without modifying training data, architecture, or weights. We verify our approach against two targets. First, we target a MNIST digits classifier that we coerce into implementing a binary letter-recognition task. Then, we attack a production-grade NSFW classifier using face-specific perturbations to turn it into a proxy for demographic-group classification. In both cases, our method successfully enables the target backdoor. Finally, we discuss the existing countermeasures to assess the actual risk for the deployed systems.

---


### 15. [Author-in-the-loop Agentic Reproducibility Auditing for a Machine Learning Conference](https://arxiv.org/abs/2610.22465)

**<font color=#1a73e8>作者：</font>** Yukun Dong, Linjun Zhang, Tian Zheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reproducibility checks during peer review require a shared understanding of what authors' code is expected to reproduce. We present an author-in-the-loop collaborative audit that makes author declarations explicit inputs to an AI agent's investigation and assessment. A structured checklist records reproduction instructions and limitations; a two-stage workflow on GitHub connects agent checks to author clarification, revision, and agent reassessment. The agent separately assesses whether results have been reproduced and whether authors need to provide clarification or make repairs, while human reviewers approve requests and decide whether concerns are resolved. We deployed the system across 36 conference papers and 133 experimental tables and figures, raising 20 issues after human review. Further checks supported closing all the issues, although full reproduction remained unverified in some cases. We further compared repeated audits with complete and blank checklists to examine how author declarations shaped the agent's investigation and assessment. Our work contributes a collaborative workflow and agent design that use author knowledge to guide reproducibility auditing. The conference deployment provides empirical evidence that this approach can help identify and address reproducibility problems through collaboration among authors, agents, and reviewers.

---


### 16. [Generative Value Classifier](https://arxiv.org/abs/2610.22497)

**<font color=#1a73e8>作者：</font>** Alexander Swerdlow, Perry Dong, Chelsea Finn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Q-learning is premised on learning a function to predict the value of a state-action pair, with the goal of using such a function to guide policy improvement. Most approaches learn this function from scratch using scalar or distributional return targets. This discriminative approach leaves another source of supervision for learning representations unused: the actions themselves. Rather than directly predict the return of a state-action pair, we ask the reverse question: how likely is the action under each possible return? This perspective provides a critic whose generative component is a return-conditioned policy, which can share the actor's architecture. Training this policy supervises the critic with every action rather than with returns alone, and a squared-error loss anchors the critic's Q-value to the bootstrapped target. We evaluate our approach on both offline and online RL tasks and show gains over leading discriminative methods, including distributional RL methods.

---


### 17. [KFS$^4$LAM: Adaptive KeyFrame Selection with Structure-Aware Mapping for Endoscopic Gaussian Splatting SLAM](https://arxiv.org/abs/2610.22505)

**<font color=#1a73e8>作者：</font>** Xinwei Ju, Zhehua Mao, Tianyi Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian-splatting Simultaneous Localization and Mapping (SLAM) augments conventional SLAM with a dense, renderable 3D scene representation, enabling high-quality reconstruction and novel-view synthesis. However, its localization, reconstruction, and rendering performance depends strongly on which observations are retained for mapping. Existing systems commonly rely on fixed temporal intervals or simple pose- and overlap-based criteria for keyframe selection. In colonoscopy, non-uniform camera motion, repetitive anatomy, specularities, and visual artifacts can make these criteria unreliable, leading to either redundant keyframes or missed informative viewpoints. We present KFS$^4$LAM (KeyFrame Selection with Structure-aware mapping for endoscopic Gaussian Splatting SLAM), which couples motion-guided adaptive keyframe selection with structurally supervised mapping and restricted temporal deformation. Accumulated motion guides adaptive keyframe selection, with complementary cues suppressing redundant or unreliable candidates. Density-aware mapping with anatomical contour supervision (colon folds) emphasizes structurally informative regions, while restricted temporal deformation accommodates local tissue dynamics without unconstrained geometric drift. We evaluate KFS$^4$LAM against Gaussian-SLAM baselines on C3VD and C3VD-v2, together with cross-backbone and component ablations. KFS$^4$LAM achieves strong overall performance across trajectory, rendering, and depth metrics, with pronounced gains on more challenging C3VD-v2 dataset. In the matched comparison with SplaTAM on C3VD-v2, it reduces rotational relative pose error by 20.3% and depth RMSE by 38.4%, while improving PSNR by 0.78 dB. Cross-backbone experiments further show that the framework is not tied to a single underlying SLAM architecture. Code and visualization results are available at this https URL.

---


### 18. [RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI Agents](https://arxiv.org/abs/2610.22507)

**<font color=#1a73e8>作者：</font>** Yunqi Liu, Peiyu Wang, Bingli Wang 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Command-line interface (CLI) agents increasingly execute longer-horizon tasks, yet existing benchmarks either assume that user instructions remain fixed throughout execution or evaluate task outcomes without capturing runtime collaboration quality. In this paper, we present REALCLI, a paired benchmark that unifies the evaluation of task execution and human-agent collaboration quality on realistic CLI tasks. To comprehensively measure collaboration, REALCLI builds a five-dimensional framework, operationalized into 22 sub-dimensions and 51 interaction scenario templates. REALCLI provides two modes for paired comparison: REALCLI-EXEC supplies complete specifications upfront, whereas REALCLI-COLLAB introduces a scripted user that delivers progressive information, corrections, constraint revisions, and authorization decisions. Evaluations reveal profound capability gaps in frontier agents: the best configuration attains an average score of only 49.2%, and when evaluated by the joint collaboration score ($J_{\mathrm{collab}}$), the peak performance reaches merely 37.6%. These results show that task effectiveness diverges sharply from collaboration quality, with models consistently struggling in steerability, trust calibration, and safety boundary management. REALCLI provides a rigorous, reproducible foundation for measuring and advancing collaborative CLI agents.

---


### 19. [TriSAR-3D and PaintFusion: A Novel Trimodal LiDAR-RGB-Thermal Dataset and Method for 3D Person Detection in Search and Rescue](https://arxiv.org/abs/2610.22509)

**<font color=#1a73e8>作者：</font>** Markus Kramer, Jan Wachenfeld, Oskar von Stryk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable 3D person detection is important for rescue robotics to give first responders situational awareness. Yet most multimodal 3D detection research targets automotive scenarios in which pedestrians mostly appear in a narrow range of upright, near-road poses. It is therefore unclear how much of the reported performance transfers to rescue settings, as a person may be lying, partially occluded, or in unstructured indoor and outdoor environments. To investigate this gap, we introduce TriSAR-3D, a multimodal person detection dataset recorded with a high-resolution 128-channel LiDAR, an RGB camera, and a thermal camera. It captures varied poses in indoor as well as outdoor locations at different times of day to study their influence on 3D object detector performance. Furthermore, we propose a novel trimodal 3D detection pipeline, PaintFusion, that fuses PointPainting-based evidence using a simple MLP. We show that the derived method reaches 65.4 AP@50 and thereby outperforms strong LiDAR-only (CenterPoint, 53.4), RGB+LiDAR (BEVFusion, 60.5), and adapted trimodal (Tri-BEVFusion, 60.7) baselines on the dataset. At the same time, it is substantially faster than other fusion-based methods such as BEVFusion, with a per-frame latency of 51.6 ms compared to 101 ms. Additionally, we test how the performance of different 3D object detectors generalizes to unseen pose categories. Removing lying instances from training data collapses the lying-pose AP@50 to near zero across all evaluated detectors. The results indicate that dataset diversity exerts a large effect on 3D object detection performance. The dataset and code are available at this https URL.

---


### 20. [Learning smooth dynamics via Kinematic Interpolants](https://arxiv.org/abs/2610.22519)

**<font color=#1a73e8>作者：</font>** Yiheng, Jiang, Youssef Marzouk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring dynamics from real-world experimental data is inherently ambiguous, as many plausible dynamical systems can explain the same positional observations at measurement times. For higher fidelity modeling of applications ranging from single-cell RNA to vortex dynamics and even flocking of birds, scientific observables increasingly also include velocity estimates that serve to resolve this issue. However, incorporating this rich information in a scalable manner, free of simulation or unnecessary approximations, has remained a difficult challenge. In this paper, we introduce Kinematic Interpolants (KI), a novel framework that extends the seminal methodology of stochastic interpolants to infer nonlinear dynamics across multiple snapshots in phase space, i.e., observables with position and velocity measurements. Empirically, we demonstrate that across several scientific datasets, KI achieves superior reconstruction of the underlying dynamics compared to existing baselines while requiring only a fraction of the training time.

---


### 21. [Learning the Shared Latent Structure of Cryo-EM Inverse Problems](https://arxiv.org/abs/2610.22523)

**<font color=#1a73e8>作者：</font>** Nithin Chalapathi, Theo Sternlieb, Ethan Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding biomolecular function requires characterizing three-dimensional structure and conformational variability, for which cryogenic electron microscopy (cryo-EM) is a powerful tool. Cryo-EM produces noisy two-dimensional particle images in which molecular structure, particle pose, and imaging conditions are jointly encoded. Recovering biological information from these observations spans inverse problems including pose estimation, heterogeneity analysis, and reconstruction. These tasks are usually addressed independently despite shared protein structure and image formation, motivating a common representation across inverse problems. Since biologically meaningful differences may be spatially localized, we study self-distillation with complementary global and masked patch objectives. Because experimental dataset discrimination can reflect acquisition-specific cues, we develop controlled synthetic and experimental evaluations and find that structural discrimination benefits from dense spatial features. We introduce the EMber family of vision transformers, pre-trained on >50 million experimental particle images from 214 EMPIAR datasets together with simulated projections from 268,000 molecular assemblies. EMber improves upon existing methods at conformational and compositional discrimination by 14.85 and 14.26 percentage points, estimates conformational populations to within 1.59pp error with a linear probe, and produces particle assignments yielding reference-quality reconstructions in fewer epochs. We demonstrate how to learn representations that capture biological information for use across multiple cryo-EM inverse problems.

---


### 22. [alkhder at AlexandriaX-2026: Context-Aware English-to-Dialectal Arabic Dialogue Translation with QLoRA-Fine-Tuned NileChat-3B](https://arxiv.org/abs/2610.22525)

**<font color=#1a73e8>作者：</font>** Hasan Alkhder, Maher Pasa, Maria Hanini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes team Alkhder's submission to Subtask 1 of the AlexandriaX-2026 shared task, which asks systems to translate English dialogue turns into thirteen Arabic dialects. We fine-tune NileChat-3B-Base with QLoRA on the Alexandria parallel dialogue corpus, training one set of adapter weights for all dialects. Each turn is translated conditioned on the target country and dialect, the domain, the participant roles, the speaker-addressee gender direction, and the preceding dialogue context. At inference, conversations are translated autoregressively and the model is fed its own previous outputs back as context without using any gold target-side test information. Under the constrained track, using only Alexandria data, it trains in about one hour and translates the private test set in under two hours. The system reaches a country-macro-averaged spBLEU of 20.36 and chrF++ of 36.64 on both tracks.

---


### 23. [FlashControl: One-Step Controllable Generator via Distillation-Friendly Single-Stream Teachers](https://arxiv.org/abs/2610.22537)

**<font color=#1a73e8>作者：</font>** Ngan Nguyen, Dung Nguyen, Quan Dao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have become a leading approach in visual generative modeling, particularly effective in text-to-image and controllable generation. Their main drawback is slow inference as it requires many sampling steps. While recent distillation methods enable one-step text-to-image generation, extending these techniques to controllable generation is still challenging. Existing controllable models, such as ControlNet, rely on dual-branch design that make distillation difficult. In this work, we adopt a simpler strategy. Instead of adding extra conditional branches, we finetune a selected subset of layers in the original text-to-image diffusion model to directly enable controllable generation. This results in DeltaControl, a single-flow, multi-step diffusion model capable of supporting spatial-condition generation while matching the performance of dual-branch approaches. Building on this teacher model, we further apply step-distillation to obtain FlashControl, a one-step model capable of spatial controllable generation with a single forward pass.

---


### 24. [CFC26: Building Evaluations for Deployment in Sonar-Based Fish Counting](https://arxiv.org/abs/2610.22549)

**<font color=#1a73e8>作者：</font>** Madison Van Horn, Suzanne Stathatos, Sevan Brodjian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate counts of fish populations are essential for monitoring ecosystems and making decisions for conservation, harvest limits, and river management. In many field deployments, these counts are obtained from sonar videos that experts must inspect manually, making large-scale monitoring slow, expensive, and difficult. Automated counting systems have been proposed as a scalable alternative, but so far this promise has been difficult to realize in deployment. Developing evaluations that better reflect real-world deployment conditions will help close this gap and drive improvements in counting performance in practice. To achieve this, we propose Caltech Fish Counting 2026 (CFC26), a new dataset with improved evaluation protocols that simulate deployment to seen and novel rivers, testing in-distribution and out-of-distribution performance. We expand the CFC22 dataset to eleven deployment locations across nine Pacific salmon river systems from Alaska to Northern California, capturing a broader geographical and ecological range of data. We additionally introduce two new evaluation metrics for counting, nMNE and nMANE, that mirror the operational workflow that experts use and help surface errors that frame-level detection metrics do not capture. Using these metrics, we reveal previously-concealed directional bias in upstream vs downstream counts, which would have direct and significant ecological implications if undetected. The dataset and code are publicly available on CaltechDATA and GitHub.

---


### 25. [FRACTAL: A Self-Similar Multi-Agent Orchestration Architecture with Formal Communication, Convergence, and Depth Bounds](https://arxiv.org/abs/2610.22561)

**<font color=#1a73e8>作者：</font>** Ohad Dan, Abhinav Taliyan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present FRACTAL, a self-similar multi-agent architecture for recursive goal decomposition, in which the same five-component organizational pattern -- Orchestrator, Ensemble, Knowledge Ledger, Decision Maker, Meta-Observer -- recurs at every level of a decomposition tree. We make four formal contributions: (1) a communication bound showing intra-node cost is linear in ensemble size and round count (O(kr)) under a two-phase blind-proposal/stress-test protocol, versus quadratic cost for free-form debate, with an explicit, stated assumption on fixed evaluator count; (2) a two-mode orchestration criterion separating generative and evaluative phases via a measurable diversity-saturation threshold; (3) a supermajority convergence guarantee with explicit probability bounds at stated agreement levels, and a formal depth bound under an operationalized goal-complexity measure; (4) a Bayesian inter-layer escalation mechanism unifying hysteresis and contract-breach signaling under one posterior update. We illustrate the architecture's execution qualitatively on a worked example and a multi-layer case study; we do not report quantitative performance claims in this paper, and we explicitly discuss the formal and inductive-bias limitations of the model, including an unimplemented but architecture-compatible direction toward bounded self-improvement. We use "fractal" as an architectural metaphor for self-similarity, not a measured mathematical property. Empirical validation of the architecture's comparative performance is left to future work.

---


### 26. [Deterministic Bounds on Accuracy and Stability of Metric-Space Regression and Classification](https://arxiv.org/abs/2610.22564)

**<font color=#1a73e8>作者：</font>** Nina Maria Gottschling, Jakob Gawlikowski, Michele Caprio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven approaches often face ambiguity in datasets due to sensor or target noise, insufficient information, and noise in the input data. While best-fit machine learning methods can accommodate such noise through uncertainty estimates, they are prone to overfitting and it is challenging to quantify ambiguity of the relation between inputs and targets. We introduce a geometric framework that quantifies this ambiguity through the average kernel size, computed with data-dependent, i.e. model-independent, feasible sets derived from worst-case input and target noise. The framework provides computable, deterministic, non-asymptotic bounds on the best achievable empirical error and accuracy for a finite, constructed dataset, independent of the predictive model class, and applies to regression and classification with pseudo-metric input spaces and metric target spaces. The ambiguity of the input-target relation implies three consequences: an empirical error floor, an accuracy-stability trade-off, and, under standard probabilistic assumptions, a strictly positive distribution-training error gap when training below the accuracy bounds. Under standard Borel assumptions for Euclidean norms, the distributional analogue of the average kernel size is related to Bayes risk as it reduces to the optimal distribution root-mean-squared error times the square root of two. Experiments spanning tabular regression, image regression and classification datasets yield nontrivial bounds on the best achievable empirical error and accuracy on a constructed dataset, alongside descriptive comparisons with model performance on the original datasets. The bounds provide a computable, model-independent reference scale on the constructed dataset and comparisons with model performance on the original dataset are descriptive.

---


### 27. [Coverage Cliffs in Off-Policy Quantile Certification](https://arxiv.org/abs/2610.22565)

**<font color=#1a73e8>作者：</font>** Pauline Bourigault, Emmanuelle Bourigault  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study when logged contextual-bandit data can certify an upper tail quantile for a policy selected from the same sample. We construct a PAC-Bayes Bernstein lower-confidence envelope for the target cumulative distribution function (CDF), simultaneous over a predeclared threshold grid and all data-dependent posteriors. The resulting procedure, TailCert, uses the envelope's first crossing of level p to return an atom-safe upper confidence bound on the selected posterior's pooled p-quantile (or inconclusive). It can also be used to select a policy under a certified tail constraint. The concentration ingredients are standard; the main theoretical contribution is a matched finite-class certification boundary comparing full logs with their joint weighted CDF indicators at a fixed threshold. On an explicit rare-action class, the required sample size grows linearly with the overlap factor W, logarithmically with policy-search and confidence complexity, and quadratically with the inverse CDF safety margin; the upper and lower bounds agree up to constants in the stated regime. On this class, the CDF reduction hides which actions exceeded the budget; retaining action counts restores the full-log rate. Simulations verify the predicted search-complexity shift, winner's-curse failure of naive reuse, and the power cost of splitting.

---


### 28. [Seeing Seizures: A Large-Scale Empirical Study of Video and EEG Deep Learning for Automated Rodent Seizure Detection and Severity Grading](https://arxiv.org/abs/2610.22566)

**<font color=#1a73e8>作者：</font>** Alloy Das, Shreyan Ganguly, Nyzil Massey 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Manual annotation of synchronized video and EEG recordings is a bottleneck in preclinical seizure research. We present an empirical study of seizure detection and behavioral severity grading using 24,131 paired clips from 601 sessions across 20 rats in a soman-induced epilepsy model. Ten video architectures and seven single-channel EEG models are evaluated independently on binary detection and three- and five-class severity tasks. In the session-exclusive reference comparison, R(2+1)D-18 and GRU achieve detection macro-F1 scores of 0.968 and 0.974, respectively; for five-class grading, the corresponding scores are 0.657 and 0.560. Subject-exclusive evaluation reduces five-class macro-F1 to 0.475 for video and 0.404 for EEG, highlighting the difficulty of grading unseen animals. Temporal-sampling experiments demonstrate the value of multiple frames, while detection performance varies relatively little across the evaluated video architectures. A separate video-only binary-detection evaluation on RodEpil achieves a mean seizure-class F1 of 0.979 after uniform re-encoding to reduce identified class-correlated encoding cues. The study characterizes existing models for behavior-defined severity labels under the evaluated protocol, motivating further investigation of expert-assisted annotation workflows. Our code and github page is available here.

---


### 29. [Who Do Perspectivist Models Predict Well? Annotator Agreement, Sparsity, and Performance](https://arxiv.org/abs/2610.22567)

**<font color=#1a73e8>作者：</font>** London Lowmanstone IV, Vaagishwaran Sivakumar, Anwesha Samaddar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Successful completion of perspectivist natural language processing (NLP) annotation tasks requires algorithms to be aligned across diverse perspectives in order to predict how different humans will rate text. This work studies how the performance of such algorithms varies for annotators who behave differently than others, either by providing annotations that diverge from others' responses or by providing fewer annotations altogether. To aid with characterizing model performance, we curate the largest collection to date of perspectivist NLP datasets with ordinal annotations. After evaluating multiple classes of perspectivist algorithms across each of the datasets, we model the relationship between individual annotator idiosyncrasy and algorithm performance. In general, we find that algorithms perform better on annotators who tend to agree with others, but that annotator response rate does not have a statistically significant positive correlation with algorithm performance.

---


### 30. [Structure-Aware Spatial Kernels for Gaussian Process Distributed Port-Hamiltonian Systems](https://arxiv.org/abs/2610.22575)

**<font color=#1a73e8>作者：</font>** Tianyi Yang, Thomas Beckers  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian process distributed port-Hamiltonian systems (GP-dPHS) enable data-driven modeling of distributed dynamical systems while preserving their physical structure. However, standard stationary kernels can be inefficient for spatially heterogeneous systems because they neither exploit known input invariances nor reflect structured spatial dependencies. We address this limitation with a structure-aware kernel design that removes irrelevant state coordinates and decouples state and spatial dependencies through a tensor-product covariance. This modular construction allows qualitative knowledge of spatial heterogeneity to be incorporated by selecting an appropriate spatial kernel without requiring an analytical description of the underlying profile. Numerical experiments on a nonlinear string with periodic, smoothly varying, and semi-piecewise stiffness profiles demonstrate that structural decoupling consistently improves reconstruction accuracy, while profile-matched spatial kernels yield substantially larger gains in force-field and trajectory reconstruction.

---


### 31. [Can SOLARBURST go silicon? A systematic analysis on software supply chain attacks for VLSI design flows](https://arxiv.org/abs/2610.22580)

**<font color=#1a73e8>作者：</font>** Fabiha Hashmat, Zeren Li, Santiago Torres-Arias  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An attacker targeting the software supply chain (SWSC) of VLSI tools can fully subvert the VLSI design pipeline through purely software level compromises. However, cur- rent literature on both SWSC and VLSI hardware security has not explored how software can be used to subvert the security of the VLSI design flow. In order to bridge this gap, this paper presents a systematic analysis of the vulnerable surface of VLSI from a SWSC standpoint. We carry this anal- ysis through three major activities. First, we did an empirical analysis of VLSI software suites, focusing on their software composition, security features, and tool interactions within the VLSI design flow. Second, we develop a VLSI-SWSC attack taxonomy model that links software supply chain at- tacks and their mechanisms to the VLSI attacks they enable, the design-flow stages they affect, and their resulting security outcomes, allowing us to identify 717 possible new attacks, including 60 high feasibility attacks supported by evidence collected in our empirical analysis. Third, we identify what possible security outcomes can be achieved by an attacker from these attacks and produce a comprehensive VLSI SWSC threat model. We evaluate the feasibility of the attacks identi- fied by our taxonomy across VLSI design stages and assess existing defenses to determine which attacks are mitigated and which remain unaddressed. In addition, we present case studies using a reference VLSI design flow consisting of open- source VLSI tools and highlight attacks identified through our taxonomy on the VLSI SWSC uniquely from a software perspective.

---


### 32. [Noise-Robust Forced Alignment for Spontaneous Speech](https://arxiv.org/abs/2610.22583)

**<font color=#1a73e8>作者：</font>** Laurin Wagner, Mario Zusag  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that forced aligners degrade on spontaneous, noisy real-world speech, and that fillers, laughter, and disfluencies corrupt word boundaries, impacting many downstream applications. We revisit the classical GMM-HMM aligner with upsampled WavLM features instead of MFCCs, explicit phone units for fillers and non-lexical vocal events trained on verbatim-annotated spontaneous speech, and a discriminative projection fitted on clean and noise-corrupted feature pairs to improve robustness. The pipeline is self-bootstrapped from 149h of curated audio without manual or external boundary targets. On conversational (Buckeye) and disfluent (FluencyBank) speech it reaches word-boundary MAEs of 20.6 and 76.9ms, 19% and 17% lower than the strongest of ten baselines. Catastrophic misalignments (>200ms) are 2.7 times rarer than Montreal Forced Aligners (MFA) best model even after widening MFA's search beam, which we show removes a large pruning artifact from its conversational error; event units halve the error next to laughter, while being meaningfully more robust than existing aligners.

---


### 33. [Initiating Removal from Operational Symptoms in Federated Vehicular Networks](https://arxiv.org/abs/2610.22584)

**<font color=#1a73e8>作者：</font>** Zihao Ding, Jun Huang, Qiang Duan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Connected vehicles train a driving model through federated learning (FL) and drive with it, so a faulty contribution often surfaces only as a delayed symptom on the road. Federated unlearning (FU) assumes that a removal request names what to forget. A symptom names no vehicle or round, and aggregation has already spread its cause across the fleet. We propose \underline{A}ggregation-\underline{T}ime \underline{O}perational-evidence \underline{N}eutralization of \underline{E}ffects (\method{}), which makes unlearning a term of the FL aggregation rule. \method{} projects everyday driving errors and reported symptoms onto a subspace spanned by recent global increments. It propagates the surviving effect of every contribution with curvature estimated from these increments and scores all contributions in one backward pass. A two-tier correction suppresses suspected effects in every round and eliminates confirmed ones after a one-round probe. We prove that backward scoring matches forward scoring and that the elimination is exact when training is flat outside the subspace. On three driving datasets, \method{} leaves 43\% to 61\% less residual harm than the strongest baseline in eight of nine settings while staying within 0.36 points of full retraining in utility.

---


### 34. [Mitigating Demographic Disparities in Explanation-Human Alignment via Rationale Regularization](https://arxiv.org/abs/2610.22586)

**<font color=#1a73e8>作者：</font>** Suryansh Talukdar, Taha Sarwat, Jonathan Rusert  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study explanation fairness in hate speech detection. High classification performance does not always mean that a model produces equally plausible explanations for different demographic groups. Using the HateXplain dataset, we introduce Plausibility-EFG, a metric that measures the largest difference in explanation plausibility across demographic groups by comparing model-generated token attributions with human-annotated rationales. We evaluate BERT, RoBERTa, and ADV-RoBERTa, an adversarially trained model, using Integrated Gradients and SHAP. Our results show that ADV-RoBERTa improves classification performance and alignment between explanations and human rationales while reducing explanation disparities across demographic groups. These improvements are observed with both attribution methods and remain consistent across training, validation, and test splits. We also show that reducing prediction-level bias alone does not eliminate disparities in explanations, suggesting that predictive fairness and explanation fairness are related but distinct objectives. Finally, our fairness-performance analysis shows that stronger adversarial regularization can further reduce Plausibility-EFG, although it may cause a small decrease in macro-F1. Overall, this work presents explanation fairness as an important objective in hate speech moderation and introduces Fair-REF, a framework designed to reduce disparities in model explanations across demographic groups.

---


### 35. [Flat Loss, Evolving Features: Grokking in Modular Addition](https://arxiv.org/abs/2610.22593)

**<font color=#1a73e8>作者：</font>** Akash Kumar, Karthik Sankaranarayanan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can a network keep learning while its training cross-entropy stays nearly flat at a positive level? We show that it can. On modular addition, a standard testbed for grokking, ReLU networks trained with supported-Polar hidden updates, normalized output-layer updates and weight decay can keep 100% training accuracy while their hidden features change and held-out accuracy rises from zero to above 90%, at relatively flat training cross-entropy. Correct classification need not minimize cross-entropy, which still depends on prediction confidence. We prove this coexistence for one-hidden-layer networks in two finite-window theorems from constructed initializations: one gives a constant gain in the Fourier fraction of the hidden features, and the other holds at arbitrarily low positive loss, where a readout refitted on the training data generalizes before the network. Experiments from random initialization show the same coexistence on a window fixed in advance, and in deeper networks held-out accuracy also rises over post-hoc windows with a net increase in training cross-entropy. With a last-layer rate set per training fraction and head decay scaled with the prime, deeper networks at p=47 and 61 meet a criterion on post-hoc windows, fixed in advance, in nearly all fresh runs. A one-block transformer trained with the same updates and a slowly decaying output gain keeps every training pair correct at every logged checkpoint while its training cross-entropy rises and its held-out accuracy approaches one; with two blocks this holds through the held-out rise, after which training pairs begin to flip. A plateau in training loss need not be a plateau in learning. Code: this https URL.

---


### 36. [Diagnosing GNN Failure Modes with Layer-Wise Probe Entropy](https://arxiv.org/abs/2610.22595)

**<font color=#1a73e8>作者：</font>** Shanzi Bao, Mar Gonzàlez I Català, Pietro Liò  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) are typically evaluated only at their final layer, obscuring how task-relevant information evolves during message passing. We introduce a post-hoc diagnostic that freezes a trained GNN, fits an independent linear probe to each layer, and tracks probe accuracy alongside normalized predictive entropy. Across real and synthetic graph settings, layer-wise probe entropy distinguishes beneficial, neutral, and harmful smoothing, a capability not demonstrated by existing geometric measures. Moreover, by comparing shallow and deep models, we show that the onset of entropy degradation separates the two main GNN failure modes: structural mismatch under heterophily, which appears from the earliest layers even in shallow models, and excessive-depth oversmoothing, which emerges only as propagation depth increases. These results establish probe-entropy trajectories as a tool for analyzing information flow in GNNs and motivate future work on adaptive depth selection and early-exit mechanisms.

---


### 37. [Rarity of Singletons Matters & Supplementary Materials](https://arxiv.org/abs/2610.22604)

**<font color=#1a73e8>作者：</font>** Pragatheeswaran Vipulanandan, Kamal Premaratne, Dilip Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating missing-mass and unseen-species counts from finite samples relies heavily on rare-event occupancy statistics, particularly singletons. In small-sample regimes, these statistics can be highly variable, making classical estimators sensitive to sampling fluctuations and potentially unreliable. We propose a fragility-aware (FA) framework that explicitly quantifies this sensitivity and adaptively regularizes conventional missing-mass and unseen-species estimators. Using singleton-based fragility measures derived from probability mass and occupancy counts, we formulate an entropy--Kullback--Leibler (KL) optimization that adjusts the reliance on base estimates according to their fragility. The resulting objectives are strictly concave, admit unique closed-form solutions, and require no Poissonization or asymptotic approximations. The framework provides a lightweight correction to classical estimators, including Good--Turing and Good--Toulmin, while reducing reliance on potentially unstable rare-event statistics. Across 360 experimental configurations spanning synthetic distributions and real-world language corpora, our method remains competitive in stable regimes while improving estimation accuracy and stability in fragmented, long-tailed, and small-sample settings. The findings demonstrate that accounting for the fragility of rare observations can improve the reliability of inference about unobserved species and their associated probability mass.

---


### 38. [Three LiDARs, Twenty-Five Datasets: Cross-Source Generalization in Tree-Species Recognition](https://arxiv.org/abs/2610.22606)

**<font color=#1a73e8>作者：</font>** Jae Joong Lee, Bedrich Benes  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> FOR-species20K is the largest public LiDAR benchmark for tree-species classification, pooling 25 independently collected terrestrial, mobile, and airborne laser-scanning datasets across 33 species. We introduce a multi-resolution, multi-view ConvNeXtV2 model that improves official hidden-test accuracy from 79.5% to 85.0%, ranking first at the time of submission. We then examine what this score measures. Because the hidden test is species-balanced, its overall accuracy is more comparable to a macro metric than to accuracy under the public set's long-tailed distribution. Moreover, the official random split places every source dataset in both training and evaluation. A logistic probe recovers source identity from out-of-fold model probabilities with 69% accuracy, while geometric features identify the source above 90% within two widely shared species; 18 of the 33 species occur in only one source. Under a source-species-cell holdout, evaluated on 5,566 trees from eight eligible species that retain the same LiDAR-type training support in other sources, the unweighted species mean falls from 82% to 36%, and tree-weighted accuracy falls from 95% to 60%. Count-matched retraining and experiments with two alternative backbones indicate that this gap is not explained by reduced training support alone, while an external PureForest experiment shows a smaller but consistent grouped-split effect. These results establish the 85% leaderboard score as strong in-distribution performance, but not as an estimate of source-disjoint generalization, motivating balanced metrics and source-aware evaluation. The code is available at: this https URL

---


### 39. [Understanding Stability of Outer Nesterov Momentum on Stochastic Pseudo-Gradients](https://arxiv.org/abs/2610.22623)

**<font color=#1a73e8>作者：</font>** Nishant Sharma, Laura Gomezjurado Gonzalez, Ganesh Talluri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large neural networks are commonly trained across many workers, and communication between them is a major cost. Workers therefore take several local optimization steps before sending their net parameter displacements, or pseudo-gradients, to an outer optimizer, which often applies Nesterov momentum. We study how the outer momentum, the number of local steps and the averaging over workers control the training dynamics, and in particular their stability. For random quadratics, we derive an exact mean-square stability criterion in any dimension, which reveals that the inner batch size determines whether increasing the number of local steps eventually stabilizes or destabilizes the outer iteration. Moreover, while averaging the pseudo-gradients of independent workers can make larger outer momentum values admissible, the number of workers required for stability can grow exponentially with the number of local steps. Finally, we show that the mean-square dynamics governing stability can be probed directly at intermediate neural-network checkpoints using shared-minibatch perturbations. We test our theoretical findings across networks, and measure their consequences for training loss.

---


### 40. [StratFL: Countering Covert Model Poisoning Attacks with Strategic Federated Learning](https://arxiv.org/abs/2610.22626)

**<font color=#1a73e8>作者：</font>** Manoj Twarakavi, Venkata Sriram Siddhardh Nadendla  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advanced persistent threats (APTs) are a major concern in federated learning (FL) deployments in critical sectors such as healthcare, and finance. Traditional defense mechanisms fail to contain APTs due to their intermittent attacking behavior. This paper addresses a specific type of APT called covert model poisoning (CMP) where the attacker intermittently injects poisoned model updates in a covert manner. The interaction between the FL server and a CMP attacker is modeled as an imperfect repeated game where both players cannot observe each other's actions. A novel adversarial search algorithm called StratFL is designed alongside novel belief update algorithms at both the server and adversary. Experiments are designed using MNIST and CIFAR-10 datasets to evaluate and compare StratFL's performance against state-of-the-art methods. Empirical convergence of belief update algorithms is demonstrated across various security vignettes. At the same time, StratFL is found to exhibit an improved accuracy of 10% compared to state-of-the-art methods.

---


### 41. [Network-Wide Freeway Speed Nowcasting and Forecasting from Sparse Fixed Sensors with a Probe-Supervised Graph Convolutional Recurrent Network](https://arxiv.org/abs/2610.22630)

**<font color=#1a73e8>作者：</font>** Ran Tu, Zihao Li, Arash Mirzaei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic agencies need current and near-future speeds on every link of their network, but their fixed sensors cover only part of it. We study joint nowcasting and next-hour forecasting of hourly speeds on all 4{,}127 directional freeway links of the Dallas--Fort Worth region from sensors on 643 links (15.6%). Historical probe-vehicle data supervise every link in training; only sensor readings are used at inference. We call this setting probe-supervised sparse sensing. We propose GCRN+, a graph convolutional recurrent network that predicts deviations from a historical speed profile. It combines a parameter-free, direction-aware kernel interpolation of sensor anomalies, used as input features and as an output baseline, with a diffusion-convolutional GRU on the directed road graph, a low-rank adaptive graph and learnable link embeddings. It scales linearly with network size and trains on a CPU. Sensor readings are emulated from probe speeds, which isolates spatio-temporal inference from detector calibration. On four held-out test days, GCRN+ attains an RMSE of 2.21~mph for the current hour and 2.39~mph for the next hour on unsensored links, against 3.23~mph for the historical average. The best baselines that use the same interpolation features reach 2.53 and 2.75~mph. Adapted recent models without these features (STID, STAEformer, ImputeFormer, MoGERNN) reach at best 2.54 and 2.53~mph; this comparison is between complete pipelines rather than architectures. GCRN+ is best in every distance band except links not connected to any sensor through the road graph. Ablations within one recurrent backbone attribute most of the gain to the link embeddings and the adaptive graph, which can be trained because probe labels exist for every link. For congestion detection on unsensored links, recall rises from 77\% (historical average) and 86% (best competitor) to 89% at aprecision of 0.94.

---


### 42. [Alert-List Concordance for Evaluating Imputation Strategies in ICU Sepsis Prediction](https://arxiv.org/abs/2610.22635)

**<font color=#1a73e8>作者：</font>** Priyanka Siddappa, Muntaqim Ahmed Raju, Shifat Haider Al Amin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preprocessing is an under-measured reliability risk in clinical prediction: a model can keep a similar AUROC and still change who receives an alert. Imputation quality is commonly evaluated using reconstruction error or aggregate discrimination, neither of which directly measures agreement on which patients are flagged. At a matched alert rate, pipelines with similar aggregate performance can produce different patient lists. This question is especially relevant under the frequent, structured missingness of real ICU records. We therefore introduce alert-list concordance, which asks whether two pipelines identify the same high-risk patients, measured by the Jaccard similarity of their top-k% alert sets with patient-level bootstrap confidence intervals. On PhysioNet/CinC 2019 (40,336 patients, 71.9% missingness), we compare nine imputation strategies and a native-missingness baseline using a fixed XGBoost configuration, fitted and Platt-calibrated separately for each strategy. After Bonferroni correction, 22 of the 28 reconstruction-method pairs showed no statistically significant difference in patient-level AUROC, yet their alert lists overlap at Jaccard 0.518 to 0.750. Similar aggregate discrimination can therefore accompany different patient selections. ForwardFill is a separate outlier, pairing higher discrimination with the lowest overlap in the matrix, 0.40 to 0.45. The broad pattern holds within each hospital system and under six patient-level aggregation rules. At the row level, eight of ten methods fall within an AUROC range of 0.011. In this row-level pipeline, deep imputers did not outperform mean imputation on discrimination, and the sequential implementations cost 5 to 12 times mean imputation in total pipeline wall-clock time on our hardware.

---


### 43. [Inductive Learning of Concept Embeddings from Cross-Linguistic Colexification Patterns with Textual Attributes](https://arxiv.org/abs/2610.22638)

**<font color=#1a73e8>作者：</font>** Arne Rubehn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The advent of distributional semantics as a framework for computational semantics marked a paradigm shift in the nature of representations, by which meanings are represented as dense vectors commonly known as word embeddings. Computational approaches to historical or typological language comparison, on the other hand, still mostly rely on discrete representations, while the potential of embedding-based methods remains largely untapped in this context. Recent studies have proposed concept embeddings as a language-independent, onomasiological counterpart to word embeddings, based on networks of cross-linguistic colexification patterns. While the resulting concept embeddings reflect meaningful semantic properties and relations, they suffer from a lack of scalability, since they rely on transductive embedding approaches which only learn embeddings for nodes present in the training data. In this study, we present an inductive framework for learning concept embeddings, combining the structural properties of full and partial colexification networks with semantic information from short concept descriptions. This framework allows the embedding of unseen concepts based on a short definition. We show that the resulting concept embeddings correlate with various cross-linguistic measures of similarity or relatedness, while generalizing well to new concepts that were absent from the training data.

---


### 44. [Secondhand Stress: How Stressful Disclosures Affect Psychosocial Wellbeing in Online Graduate Admissions Communities](https://arxiv.org/abs/2610.22657)

**<font color=#1a73e8>作者：</font>** Veda Duddu, Agam Goyal, Sabelle Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online communities provide spaces for individuals navigating stressful life transitions to disclose difficulties and seek peer support. Yet encountering others' distress may also have psychosocial implications for community members. Drawing on stress crossover theory, we examine how engagement with peer distress during graduate admissions is associated with subsequent psychosocial expression and participation, and whether similar associations extend through downstream interactions. We analyze 171,981 posts and 1,130,413 comments from two Reddit communities across three admissions cycles, using propensity-score stratification and baseline-adjusted comparisons. Users who engaged with distress disclosures during application preparation subsequently exhibited higher classifier-estimated anxiety, depression, and stress expression, alongside greater commenting activity and lexical redundancy. These associations recurred across admissions cycles, while no significant psychosocial associations were detected among downstream respondents interacting with previously exposed users. Our findings highlight how greater distress-related expression can coexist with continued community participation, while distinguishing direct engagement with distress disclosures from subsequent social contact. We discuss implications for designing online communities that preserve opportunities for self-disclosure and peer support while remaining attentive to the experiences of those encountering distress-related content.

---


### 45. [Gossip Agents: Reputation through Opinion Dynamics over Evolving Networks](https://arxiv.org/abs/2610.22674)

**<font color=#1a73e8>作者：</font>** Yutong Wu, Arlei Silva  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Sustained cooperation among self-interested learning agents is essential in many shared environments. Reputation systems are among the best-studied mechanisms for promoting such cooperation. Existing multi-agent reinforcement learning approaches, however, typically assume that reputation is either globally available to all agents or derived solely from an agent's own observations, leaving largely unexplored how reputational information propagates between agents. We study gossip, the exchange of information about third parties, as a mechanism for reputation diffusion over dynamic communication networks. Agents form private opinions from limited observations and exchange them with their neighbors following DeGroot opinion dynamics, while the communication network changes as agents interact and move. A tunable broadcast radius controls the reach of information, spanning private reputation, local gossip, and globally shared reputation. We study this framework in two \(n\)-player social dilemmas with distinct network dynamics: a Prisoner's Dilemma with randomly resampled interaction groups and Harvest, where communication neighborhoods emerge from agents' movements. Our results show that the reach of reputational information shapes cooperation in both environments. Moreover, in Harvest, reputation diffusion increases environmental rewards and leads to more peaceful and sustainable behavior.

---


### 46. [Deep Learning for Deepfake Image Detection: Comparative Model Evaluation and Gradient-Based Visual Attribution](https://arxiv.org/abs/2610.22676)

**<font color=#1a73e8>作者：</font>** Saad Korchi, Abderrahim Waga  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic facial imagery has made the distinction between authentic and generated content increasingly important for digital forensics and online trust. This study examines an explainable deep-learning workflow for image-level deepfake detection using two contrasting classification strategies: a compact convolutional model trained from scratch and an ImageNet-pretrained MobileNetV2 model adapted through two-stage transfer learning. Experiments were conducted with the balanced 140k Real and Fake Faces dataset, comprising 140,000 facial images. Under the recorded validation protocol, the augmented from-scratch model reached 84.15% accuracy (loss 0.3625), compared with 95.90% accuracy (loss 0.1074) for the fine-tuned pretrained model. Gradient-weighted class activation mapping (Grad-CAM) was used to visualize image regions associated with predictions, and a Flask-based prototype was developed for side-by-side inspection. These observations support the practical value of pretrained visual representations in the studied setting while underscoring the need to interpret validation performance alongside dataset provenance, explanation limitations, and evaluation scope. The reported results are validation results, not held-out test estimates.

---


### 47. [FlexUMM: Flexible Representation Learning for Unified Multimodal Models](https://arxiv.org/abs/2610.22682)

**<font color=#1a73e8>作者：</font>** Yinyi Luo, Haoyue Bai, Yi Ge 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) can integrate understanding and generation within a single backbone. However, it is commonly known that these two capabilities can cause conflicting representations, leading to a central question: how representation and computation should be shared across functionalities? Existing UMMs often rely on a largely fixed structure, where different inputs and functionalities follow the same depth and parameter-sharing pattern. We argue that this assumption is too restrictive: more effective unification requires sharing the computation that supports cross-functional communication while specializing the capacity that becomes task- or input-specific. We introduce FlexUMM, a flexible UMM framework that dynamically decides when to preserve shared computation, when to route specialized capacity, and when to stop further processing. Evidence shows that this flexible allocation improves UMMs along two complementary axes. It improves accuracy by reducing harmful competition between functionalities, and it improves efficiency by avoiding unnecessary computation once an input representation is sufficiently mature. Beyond simple architectural unification from the pre-trained models, FlexUMM works as a model-agnostic, functional plug-in to make existing UMMs more unified, stronger, and efficient. Code is available at: this https URL.

---


### 48. [Spectral Limits of Polynomial Graph Filters on the Long-Range Ising Model Benchmark](https://arxiv.org/abs/2610.22713)

**<font color=#1a73e8>作者：</font>** Amin Najafgholizadeh, Mohsen Afsharchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Long-Range Ising Model benchmark (LRIM) guarantees long-range dependence by construction: each label is the node's spin times the spin field convolved with a power-law coupling, so any model's distance from the target is measurable. We prove that a readout whose filter is a polynomial in the adjacency, the linear core of isotropic message passing and spectral graph networks, leaves an error floor that no degree lowers, because the target varies along a level set of the spectrum on which every such filter is constant. Computed exactly, the floor and the best filter of each degree predict two spectral networks adapted from published architectures to within a tenth of a decade. A filter escapes the floor only if it weighs separately the offsets the adjacency lumps together, and must still resolve the coupling across the whole lattice. A strided filter of about fifty coefficients does both: fitted to the training labels, its test error is 52 times below the best published network's. A dilated convolutional network beats the best published result at 256 nodes, matches it at 1,024, and gives the first in-domain results at the three larger sizes, while a Fourier neural operator with its standard modes falls further behind as the lattice grows. At its standard budget the dilated network stays two to four orders of magnitude short of a larger strided filter fitted to the labels. The analysis carries over to the benchmark's second coupling.

---


### 49. [HilbertGen-3D:Hilbert--Multifractal Conditioning for Topology-Aware 3D Generation](https://arxiv.org/abs/2610.22720)

**<font color=#1a73e8>作者：</font>** Ziyi Zhang, Shixuan Li, Yorie Nakahira 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity 3D generative modeling underpins game asset creation, medical imaging, and VR/AR environmental design, where geometric structure directly influences perception and decision-making. Diffusion models represent a powerful paradigm for point cloud generation. However, existing approaches rely heavily on local voxel or patch features and often miss global structural organization, and much less work has studied how global conditioning can be used to improve generation quality. In this paper, we introduce HilbertGen-3D, a novel topology-aware conditional diffusion framework based on Hilbert-Multifractal Conditioning (HMC). HMC computes multi-scale voxel measures, serializes them via a 3D Hilbert curve to expose structured spatial dependencies, and estimates the generalized fractal dimensions from scale-dependent partition functions. We encode these signals as global embeddings and multi-scale tokens, and inject them into a diffusion denoiser through an efficient bottleneck fusion module. Across the Chair, Airplane, and Car categories of ShapeNet, our two conditioning variants reduce the absolute deviation of 1-Nearest Neighbor Accuracy (1-NNA) from 50% by up to 8.90 percentage points and increase coverage by up to 5.88 percentage points relative to TopoDiT-3D. This shows that combining local density cues with global Hilbert-multifractal structure provides a simple and effective recipe for high-fidelity and diverse 3D generation.

---


### 50. [Improving OCR Accuracy Through Multi-Classifier Verification of Visually Similar Characters](https://arxiv.org/abs/2610.22726)

**<font color=#1a73e8>作者：</font>** Nuzhat Khan, Ab Al-Hadi Ab Rahman, Mohamad Anuar Kamaruddin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distinguishing visually similar characters is a persistent challenge for optical character recognition (OCR) systems, causing errors in critical applications of text digitization. While preprocessing techniques improve image quality and word-level post-processing corrects spelling errors, neither addresses character-level visual ambiguity, an intrinsic property of certain character pairs that limits even state-of-the-art OCR models. We present the Character Verification Model (CVM), a character-level post-processing framework that verifies and corrects ambiguous characters in OCR outputs using specialized binary classifiers trained on visually confusable pairs such as 'O'/'0', 'Z'/'2', and 'S'/'5'. CVM operates independently of dictionary validation, making it suitable for non-lexical data including serial numbers, alphanumeric codes, and license plates. Experiments on three OCR engines (Tesseract, EasyOCR, TrOCR) and ten fonts with low to high complexity demonstrate accuracy improvements of 3.95-14.81 percentage points, with an 87.3% correction rate for visually similar character errors and a false-correction rate of only 2.3%. The modular architecture integrates with existing OCR pipelines without modification to underlying recognition models.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-213](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
