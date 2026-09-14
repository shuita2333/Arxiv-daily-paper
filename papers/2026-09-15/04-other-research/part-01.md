# 📦 其他研究 | 2026年09月15日

> 本类共 **201** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-201](./part-05.md)

---

### 1. [Fundamental Dynamical Units for Physics-Informed Structural Inference from Perturbation Time-Series in Networked Systems](https://arxiv.org/abs/2609.11934)

**<font color=#1a73e8>作者：</font>** Nima Nouri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In networked dynamical systems, the parameter of primary mechanistic interest is signed interaction structure. Recovering this structure from perturbation time-series data is a fundamental identification problem, compounded by three coupled obstacles: the combinatorial complexity of interaction architectures, ambiguity of causal attribution under limited interventions, and state-dependent dynamics that confound structural inference. Each obstacle is structural in origin and calls for a structural solution. We address these challenges by adopting a reductionist approach, introducing Fundamental Dynamical Units (FDUs): signed three-node interaction patterns as composable primitives that convert the interaction hypothesis space into a finite, constructive, and tractable representation. We show that local interaction structure determines the perturbation conditions required to disentangle direct from relayed influence, making intervention design a structural consequence of the FDU representation. We embed FDU-regularized structural inference within a physics-informed neural ordinary differential equation (ODE) whose governing-equation constraint transforms structural hypotheses into verifiable dynamical predictions, enabling joint recovery of interaction structure and perturbation-resolved trajectories. Validated on synthetic benchmarks with known ground truth, the framework supports structural commitment, expressed through FDU primitives, motif-prescribed intervention design, and physics-informed learning, as a principled basis for mechanistically interpretable inference in networked dynamical systems.

---


### 2. [Physics-Informed Conformal Prediction: Embedding PDE Consistency into Distribution-Free Uncertainty Quantification for Neural Operators](https://arxiv.org/abs/2609.11935)

**<font color=#1a73e8>作者：</font>** Michael Chin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators such as the Fourier Neural Operator (FNO) achieve remarkable accuracy in approximating solutions to partial differential equations (PDEs). However, providing rigorous uncertainty estimates remains an open challenge. We propose Physics-Informed Conformal Prediction (PI-CP), a framework that embeds PDE residuals into the nonconformity score of split conformal prediction, producing prediction intervals that are (i) distribution-free with provable coverage guarantees, and (ii) spatially adaptive when the PDE residual correlates with prediction error -- tighter where physics is well-satisfied, wider where it is violated. Additionally, we prove that FNO's translation equivariance creates a fundamental approximation barrier for PDEs with Dirichlet boundary conditions, and show that coordinate channels resolve this with up to 63x error reduction. We validate PI-CP across six physics scenarios -- heat conduction (2D/3D), structural mechanics (2D/3D), Darcy flow, and Navier-Stokes -- demonstrating consistent 89-91% coverage for all four Conformal methods, while MC Dropout and Deep Ensembles are unstable (82-100%). FNO outperforms CNN and DeepONet by 10-12x.

---


### 3. [Fed-Equilibrium Framework for Topological Pareto Control in Robust and Fair Clinical Federated Learning](https://arxiv.org/abs/2609.11937)

**<font color=#1a73e8>作者：</font>** Ting Xu, Henry Leung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The deployment of Federated Learning (FL) in multi-center clinical networks faces the challenge of "knowledge dominance," where high-volume hubs naturally overwhelm minority community nodes, implicitly treating the distinct clinical patterns of smaller cohorts as outliers. Existing geometric defenses provide a security baseline but leave this efficiency-fairness dilemma unresolved. To bridge this gap, we propose Fed-Equilibrium, a framework that advances the paradigm from simple defense to topological equilibrium. Unlike traditional aggregators, Fed-Equilibrium implements a sequential architectural synergy. It utilizes a two-stage gradient control cascade: Stage I (geometric quality assurance) enforces directional consistency via a cosine similarity funnel to filter malicious noise, creating a stabilized manifold; Stage II (topological Pareto control) then actively modulates verified contributions by identifying the optimal Pareto knee point. We validated this framework on a bi-national simulation integrating Canadian (CNODES) and U.S. (SyntheticMass) registries. Experimental results demonstrate that the system simultaneously secures the network against adversarial divergence while accommodating underrepresented signals. Notably, the minority U.S. spoke (representing less than 3% of data volume) achieved deep convergence comparable to the data-rich Canadian hub. This confirms that Fed-Equilibrium effectively counters "knowledge dominance," establishing a true "knowledge commons" where global generalizability does not come at the cost of local clinical representation.

---


### 4. [ChemMat-AgentSafetyBench: Evaluating Long-Horizon Attacks and Defenses in Chemistry and Materials Agents](https://arxiv.org/abs/2609.11952)

**<font color=#1a73e8>作者：</font>** Zhan'ao Yao, Zhihao Gao, Liang Yin 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Chemistry and materials agents integrate literature retrieval, candidate generation, property prediction, and protocol planning into continuous discovery workflows. Consequently, the relevant safety question is shifting from whether a model answers a hazardous question to whether an agent releases a hazardous protocol through a tool-mediated workflow. We introduce \bench, a benchmark that evaluates whether chemistry and materials agents can be steered toward hazardous endpoints through user input, tool observations, or persistent memory. The benchmark contains 432 fixed harmful case specifications spanning eight hazard classes, three scenario shells, four tool-and-memory environments, a single-turn direct-attack baseline, and five online long-horizon attacks: intent hijacking, tool chaining, objective drifting, task injection, and memory poisoning. The concrete language of each online attack is generated from the evolving trajectory at runtime and is therefore not counted in the static benchmark size. In the four-model main experiment with a fixed attacker, agents release complete hazardous synthesis or preparation procedures in 25.6\% of runs. Replacing the attacker model yields mean success rates from 18.4\% to 26.5\%, indicating that the risk is not an artifact of a single attacker. Input- and state-level defenses adapted from general-purpose agent safety, as well as candidate checks designed for chemistry and materials, reduce some failures but still leave complete-path release rates between 9.2\% and 22.5\%. Existing defenses therefore do not simultaneously cover multi-entry contamination, tool state, and the final artifact boundary. These results highlight a widening gap between the rapid development of scientific agents and the safety evaluation and defenses available to the chemistry and materials community.

---


### 5. [Efficient AI Model Deployment Using Quantization Analysis Tool](https://arxiv.org/abs/2609.11954)

**<font color=#1a73e8>作者：</font>** Dwith Chenna, Kanishka Macherla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As deep learning models are increasingly deployed on resource constrained devices, the demand for efficient model optimization techniques continues to grow. Effective deployment of AI models on edge and low power platforms requires optimization methods that reduce model size and computational cost while maintaining high accuracy. This paper presents Quantization Analysis Tool, a practical system designed to streamline quantization workflows and support performance efficient model deployment. Built on the ONNX framework for broad interoperability, the tool provides detailed layer-wise sensitivity analysis, visualization of weight and activation distributions, and insights to guide precision selection. By identifying layers that are resilient or sensitive to reduced precision, the tool enables developers to make informed trade-offs between model size, latency, and accuracy. Experimental evaluations across multiple neural network architectures demonstrate that the tool effectively improves the quantized accuracy, leading to improved efficiency in real-world deployment scenarios. The tool also provides developers valuable insights into the effects on quantization on the model and its accuracy. This work highlights the tools capabilities, practical applications, and its role in enabling efficient AI model deployment through robust quantization analysis

---


### 6. [Decoding Mixture Perception through Computational Modeling of Component Interactions](https://arxiv.org/abs/2609.11958)

**<font color=#1a73e8>作者：</font>** Fei Wang, Xiaoya Xie, Junfei Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Olfaction played an indispensable role throughout human evolution and civilization. Even in the contemporary era of advanced technology, olfaction remains a critical channel for person to conduct danger discrimination, emotional experience, and memory formation. However, most substances in nature exist as multi-molecule mixtures. The complexity of mixture compositions, as well as concentration dependent saturation effects and receptor specific activation thresholds, pose substantial challenges in identifying olfactory characteristics. In this study, we proposed a novel bio inspired deep learning framework for accurate odor perception recognition of mixtures. We robustly constructed neural response curves for molecule-receptor interactions, and developed a fusion strategy that integrates attention-weighted multi-receptor curves with concentration-dependent multi-molecule curves, replicating the competitive activation and synergistic integration of mixture components. Furthermore, by comparing the consistency of response curve patterns, the model can transfer knowledge from the semantically rich space of molecular associations to guide recognition of mixture perception characteristics. Therefore, we established a complete computational pathway from chemical blending, neural encoding, to perceptual formation. Finally, we conducted comprehensive evaluation, and results demonstrated exceptional superiority, achieving an accuracy of 92.2%. Consequently, our work provides a generalizable solution to the long standing mixture perception challenge. More importantly, it can be integrated into embodied cognitive systems to enhance the agents perceptual and interactive capabilities in complex scenarios.

---


### 7. [Space as an Interventional Invariant: Cross-Modal Predictive Geometry for Stratified Cities and Em-Spaced Intelligence](https://arxiv.org/abs/2609.11959)

**<font color=#1a73e8>作者：</font>** Tao Yang, Xuhui Lin, Kunyao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Space is a foundational concept across mathematics, physics, spatial cognition, urban science, and embodied intelligence, yet these fields often treat spatial structure either as a shared geometric container or as a collection of disconnected representations. Such approaches struggle to explain how heterogeneous sensory and urban processes can jointly reveal a common spatial structure, particularly when different modalities do not share the same metric or representation. This paper addresses this gap by defining space as an interventional invariant: the minimal relational structure that preserves local compatibility and the conditional laws of future observations under admissible actions. We develop a cross-modal predictive geometry that integrates local state spaces, modality-specific observation maps, an action groupoid, and a canonical predictive-state quotient, with explicit causal conditions for identifying interventional rather than merely observational structure. The key theoretical result shows that, under joint point separation, equivariance, and interventional faithfulness, the latent space is identifiable up to the centraliser of the intervention group, thereby reducing representational ambiguity to residual coordinate freedom. The framework is further extended to stratified urban systems using sheaf-valued representations, allowing geometric, physical, mobility, social, and economic layers to coexist without being reduced to a single metric. Synthetic experiments under noise evaluate equivariance, predictive sufficiency, holonomy, restriction-map recovery, cross-scale consistency, and context saturation. The resulting framework provides a unified and falsifiable foundation for spatial cognition, urban science, embodied AI, and em-spaced intelligence.

---


### 8. [A Survey on Quantum-Safe Cryptographic Mechanisms: Building Blocks and Applications](https://arxiv.org/abs/2609.11991)

**<font color=#1a73e8>作者：</font>** Ricardo Parizotto, Preeti Yadav, Marcus Freire 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The possible emergence of fault-tolerant quantum computers may enable widely used cryptographic algorithms to be broken. These algorithms for public key encryption and digital signatures could be exposed if an efficient algorithm is employed. This poses a threat to existing infrastructure, motivating the development of mechanisms that can withstand quantum-computer cybersecurity risks. However, the transition to new security mechanisms is still underway and faces many challenges, including identifying which applications are under threat and implementing agile, scalable migration processes. In this work, we survey the state of the art in quantum-safe cryptographic mechanisms, existing applications targeting migration, and open challenges. We examine the building blocks commonly used to integrate
quantum-safe mechanisms into existing applications and categorize them by the security mechanisms they employ. Next, we systematically review existing migrations into quantum-safe schemes and categorize them by application domain, including Telecommunications, the Internet of Things, and Blockchains. Finally, we summarize the challenges that must be addressed to enable a successful migration to quantum-resistant mechanisms, as well as the motivations for pursuing this migration.

---


### 9. [FINESSE: An Agent-Based Simulator and Benchmark Dataset for Multimodal Financial Event Sequences](https://arxiv.org/abs/2609.11993)

**<font color=#1a73e8>作者：</font>** Tyler Farnan, Benjamin Eng, Adam Abate 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning research in financial services is limited by the scarcity of representative open-source datasets. Existing resources are often narrowly focused on a single modality or task and fail to reflect the structured, multimodal, and dynamic nature inherent to many problems in financial services.
In this paper, we introduce FINESSE, a Financial Event Sequence Simulation Environment, an agent-based simulation framework for generating synthetic, structured datasets composed of multiple interdependent event streams. Each stream corresponds to a distinct financial behavior such as transactions, payments, account status changes, and policy interventions, each with unique action spaces, schemas and variable types. These streams are coupled through agents' latent evolving states, enabling the simulation of temporally rich interactions.
We also introduce FINESSE-Bench, a benchmark dataset generated by the simulator, supporting four representative tasks: balance forecasting, transaction fraud detection, missed payment prediction, and next event prediction. We report baseline results using methods from time series forecasting, event sequence modeling, temporal graphs, and temporal point processes. We release the FINESSE framework, including the simulator and dataset to accelerate research on structured, multimodal event sequence modeling challenges in financial services.

---


### 10. [DCRA: Diffusion-Conditioned Representation Alignment for Robust Time-Series Learning](https://arxiv.org/abs/2609.11997)

**<font color=#1a73e8>作者：</font>** Wenrui Xu, Anas Enanaa, Keshab K. Parhi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning robust representations for time-series signals under noise and distribution shifts remains challenging, especially in clinical applications such as electroencephalogram (EEG) and electrocardiogram (ECG) analysis. We propose Diffusion-Conditioned Representation Alignment (DCRA), a training framework that repurposes the forward diffusion process as a structured corruption scheduler for representation learning. Different from conventional augmentation and consistency-based methods that rely on independently sampled perturbations, DCRA introduces a structured corruption trajectory via the diffusion forward process, which enables continuous and controlled representation evolution across noise levels. We introduce a feature-level consistency objective that aligns representations across noise levels while preserving class-discriminative structure. This mechanism promotes structure-preserving consistency, which enables smooth and semantically coherent feature trajectories in latent space. The proposed framework is encoder-agnostic and can be integrated with state space models and Transformer architectures. The seizure detection experiments on the CHB-MIT EEG dataset show that DCRA consistently improves performance under multiple noise conditions and achieves higher sensitivity at low false-positive rates. Analysis reveals that DCRA produces more balanced and structured representations compared to baseline and diffusion-only models. These findings highlight the benefit of combining structured corruption with representation alignment for robust time-series learning.

---


### 11. [A Dark Forest First Attack Is Rational Only If the Attacker Accepts It as Its Last](https://arxiv.org/abs/2609.12003)

**<font color=#1a73e8>作者：</font>** Harvey Dam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Dark Forest argument holds that a civilization that detects another should strike it at once, so detection, and any transmission that invites it, is danger. Existing models make the detected civilization the object of the strike and play the strike on a roster the attacker knows; where they advise restraint, the advice rests on steps that fail in the cases it is for. This paper takes the object of hostility to be remaining uncontrolled capacity to warn or retaliate, on a roster no attacker ever knows to be complete. A first strike is rational only if the timing benefit of what it removes is at least the disclosure loss from every leftover that learns of it. A leftover able to bring about the attacker's destruction, by striking or by warning one who can, costs the attacker its whole stake, and the actors the attacker has never found are such a leftover that no strike removes. A Dark Forest believer that strikes first therefore accepts the strike as the last attack it will ever make; the strike is rational only if waiting would raise the cost of removing the target by about the attacker's whole stake. A transmission that reveals the sender gives a receiver a posterior over the sender's capacity, not a target, and proves that the sender can warn. A receiver need not be hostile; for one that is, the sender is a witness it must pay for, so a beacon delays every hostile that cannot be nearly sure of removing the sender's forces, and a free beacon harms its sender only through sure kill, whole-stake urgency, a receiver that fears no one the sender could warn, or an opening hidden from the sender. Messaging to extraterrestrial intelligence (METI) is judged by reach and by what a receiver must believe to act, not by fear of punishment, and a beacon deters by witnessing: the sender need not be able to strike anyone, only to tell someone who can.

---


### 12. [QTrans: A Quantum Transformer for Sentiment Classification](https://arxiv.org/abs/2609.12011)

**<font color=#1a73e8>作者：</font>** Ren-Xin Zhao, Xinjie Huang, Yahong Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In small-scale binary sentiment classification scenarios, factors such as negation, contrastive shifts, and cross-word dependencies lead to the non-linear coupling of sentiment cues, making it difficult for conventional lightweight models to fully capture the contextual relationships between tokens. To address this issue, we propose a model named QTrans, which uses parameterized quantum circuits to construct query, key, and value features and derives attention coefficients from Gaussian distances between quantum measurements. By further integrating a quantum feed-forward neural network, residual connections, and layer normalization, the model establishes an end-to-end trainable quantum-classical hybrid framework for sentiment classification. Experimental results on the MR, CR, and MPQA datasets show that QTrans achieves test accuracies of 72.13\%, 69.51\%, and 63.45\%, respectively, representing improvements of 2.88, 3.17, and 3.79 percentage points over the best-performing classical baselines for each dataset. Overall, QTrans expands the application of parameterized quantum circuits in lightweight sentiment analysis and lays an experimental foundation for further research into quantum multi-head self-attention for modeling textual relationships.

---


### 13. [Certified Safety Curation: Distribution-Free Guarantees for Safe Offline Reinforcement Learning](https://arxiv.org/abs/2609.12014)

**<font color=#1a73e8>作者：</font>** Adam Haroon, Cody Fleming  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe offline reinforcement learning assumes a cost function on every transition. We ask what remains possible when safety can be judged only by comparing short clips and occasionally asking whether an episode exceeded its budget. Certified safety curation answers with a filter-then-clone pipeline: a state-only value trained from segment comparisons scores whole trajectories, Learn-then-Test calibration certifies a selection threshold under a distribution-free $(\alpha, \delta)$ bound on the unsafe fraction of the selection, and behavior cloning follows. We are not aware of prior work certifying the composition of a training set for offline RL or imitation. Oracle controls justify the design: reweighting individual transitions fails even with an exact value, so the value selects whole trajectories. The policies satisfy the cost budget on eleven of fifteen DSRL tasks, one short of cloning the ground-truth safe subset, which needs a label on every trajectory; the uncertified variant reaches twelve. Retrained on the certified selection, the strongest full-label method becomes safe where no setting of its own cost target rescues it. Refusal is predictable: the certificate's probability has a closed form in the purity the pool attains, which the calibration sample estimates and the scorer enters only through.

---


### 14. [Inverting Self-Triggered Control: Adversarial Reinforcement Learning for Sparse Denial-of-Service Attacks](https://arxiv.org/abs/2609.12016)

**<font color=#1a73e8>作者：</font>** Adam Haroon, Erick J. Rodríguez-Seda, Tristan Schuler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-triggered reinforcement learning control (RL-STC) learns the sparsest control schedule that preserves Lyapunov-decreasing stability under a Run-Time Assurance (RTA) override. We invert this: an adversarial RL agent learns the sparsest jamming or Denial-of-Service (DoS) schedule that destabilizes the closed loop, with a Lyapunov-increase admissibility predicate mirroring the defender's safety certificate. We prove a plant-property lower bound on the minimum jam count required for an immediate hold-last medium-access-control adversary to force a crash against a self-triggered controller (STC) satisfying a Lyapunov contract, and recover a certificate-level analog of the consecutive-grouping optimality of prior count-budget DoS scheduling as a corollary. This extends the DoS-scheduling count-budget analysis from periodic and linear-time-invariant to STC controllers. Empirically, we train against four fixed defenders per plant (one Linear Quadratic Regulator (LQR) and three RL-STC) on Pendulum, CartPole, and Quadrotor2D. The learned adversary is the only adversary that crashes every defender on every plant at $100\%$: greedy misses Quadrotor2D LQR on $42\%$ of episodes and periodic misses Pendulum LQR on $97\%$. On jam-time-per-failure it beats baselines by up to $2.8\times$, and shows its widest absolute margin on Quadrotor2D LQR. Robustness ablations show that Gaussian observation noise exceeding the initial-state magnitude and position-only observation both preserve $100\%$ failure rate and keep the learned adversary strictly ahead of both baselines on jam-time-per-failure.

---


### 15. [Toward Reliable Railway-Bogie Response Prediction Using Multifidelity TDNN and Physics-Informed Residual Learning](https://arxiv.org/abs/2609.12018)

**<font color=#1a73e8>作者：</font>** Gyeolhee Lee, Moosun Kim, Taewook Kwon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Railway engineers need simulation models that predict vehicle responses across operating scenarios that cannot be tested exhaustively. Agreement with representative measurements provides essential evidence, but calibration at a limited set of conditions does not guarantee accuracy elsewhere. We present a multifidelity railway-bogie response-correction method that treats multibody simulation histories as low-fidelity information and roller-rig measurements as high-fidelity evidence. This method combines an experiment-anchored fidelity assignment with physics-informed discrepancy learning for multichannel bogie-response histories. A time-delay neural network (TDNN) represents the condition-dependent simulation trend, and development-fitted amplitude alignment defines the low-fidelity baseline. A residual-correction network then models the reproducible response component not explained by this baseline and adds it to the baseline. An effective dynamic-balance equation constrains the learned discrepancy by representing differences in inertia, damping, stiffness, and external forcing between the simulated and physical systems. The training objective combines this constraint with residual matching, temporal smoothness, and selectively applied displacement-acceleration consistency terms. For the evaluated reconstruction case, the corrected response gives a mean coefficient of determination of 0.8197, a mean normalized root-mean-square error (NRMSE) of 4.6055 %, and a mean normalized mean absolute error (NMAE) of 1.9297 %. These results provide initial evidence of accurate response prediction at the held-out 385 km/h condition.

---


### 16. [Reinforcement Learning for Syndrome Extraction](https://arxiv.org/abs/2609.12020)

**<font color=#1a73e8>作者：</font>** John Zhuoyang Ye, Aarav Pabla, Jens Palsberg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A key subtask of quantum error correction is to extract a syndrome that, if nontrivial, signals an error. The number of possible ways to extract a syndrome grows exponentially with the syndrome size, and these implementations vary greatly in fault tolerance, as measured by their logical error rates. This creates a natural search problem: find an implementation with a low logical error rate. Previous work solves this problem but sacrifices either solution quality or scalability. In this paper, we use reinforcement learning and importance sampling to outperform previous work at all scales. Compared with the state of the art automatic scheduling tools AlphaSyndrome and PropHunt, our tool reduces the logical error rate by 25.9\% and 71.7\% on average, respectively, culminating with a reduction of 97.8\% for a surface code with distance 15.

---


### 17. [Reading the Whole Heart: Latent-Attention Masked Autoencoders for Multimodal Cardiac Representation Learning](https://arxiv.org/abs/2609.12035)

**<font color=#1a73e8>作者：</font>** Andrea Agostini, Simon Böhi, Moritz Vandenhirtz 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cardiovascular diagnosis rests on integrating complementary modalities, like ECG, echocardiography, chest radiographs, and clinical variables, each capturing distinct but correlated aspects of cardiac physiology. Yet most medical foundation models remain modality-specific, combining modalities only for finetuning or post-training. This discards the cross-modal evidence clinicians naturally integrate and ignores the structure within each modality. We introduce Latent-Attention Masked Autoencoders (LAMAE), a multimodal, structure-aware masked autoencoder that jointly learns patient-level representations during self-supervised pretraining. Rather than fusing modalities post hoc, LAMAE exchanges information directly in the latent space through a shared latent-attention module operating over a study-view-entity hierarchy, enabling aggregation of variable observations and graceful handling of missing modalities. Pretrained on over 1.2 million MIMIC-IV hospital stays, LAMAE outperforms modality-specific pretraining and strong contrastive and vision-language baselines across multimodal hospital-stay tasks, such as in-hospital mortality, ICD-10 and DRG coding, and length of stay, while remaining competitive on unimodal tasks. These gains persist even when only a single modality is available at test time, showing that modeling both intra- and inter-modal structure yields more robust, transferable representations.

---


### 18. [One Click to Leak: Characterizing the Real-World Usage and Threat Impact of MNO-based Single Sign-On Websites](https://arxiv.org/abs/2609.12037)

**<font color=#1a73e8>作者：</font>** Jiasheng Huang, Mingxuan Liu, Pei Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile Network Operator (MNO)-based Single Sign-On (MSSO) is a password-free authentication framework relying on mobile data sessions. Unlike traditional SSO, it shifts the Identity Provider (IdP) to the MNO and the authentication anchor to the Service Provider (SP). MSSO is increasingly deployed and has expanded from mobile apps to websites, yet its web ecosystem and security risks remain largely unexplored. We analyze mainstream MSSO deployments and identify a 3-phase workflow with three trust defects enabling trust hijacking. We further demonstrate One-Click-to-Leak (OCL) attacks, where a single webpage visit can leak sensitive identity information (e.g., phone numbers). With a leading security company, we conduct the first large-scale, longitudinal study of web-based MSSO. We design a hierarchical detection framework using passive DNS correlations and URL reconstruction from search data to identify MSSO-enabled websites. Over one year, we identified 116,852 website URLs across 729 apex domains. Of these URLs, 73.6% exhibit at least one trust defect: 69.4% expose developer credentials, and 27.1% issue high-privilege tokens before user consent, indicating widespread OCL-enabling trust defects. Among the 729 apex domains, 31.8% rely on Resellers, obscuring the downstream SP from the MNO in the analyzed flows. Script analysis identifies 101 websites strongly associated with OCL attack behavior. With our partner, we trace a representative upstream platform subsequently seized by law enforcement and uncover a monetized underground ecosystem. Sanitized backend data shows that it collected 14,100 users' phone numbers within three days and linked them to sensitive information such as browsing activity. Our work provides a comprehensive study of web-based MSSO deployment and security implications. Through responsible disclosure, our work helps secure the mobile authentication ecosystem.

---


### 19. [Scalable Discrete-to-Continuous Channel Simulation for Compression and Privacy](https://arxiv.org/abs/2609.12067)

**<font color=#1a73e8>作者：</font>** Joseph Rowan, Buu Phan, Ashish J. Khisti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Channel simulation has recently emerged as a useful component in machine learning systems where samples from a prescribed probability distribution are to be compressed. Yet, general channel simulation algorithms often suffer from high computational costs, random stopping times or, in the worst case, can require generating an infinite number of shared random samples. We introduce a scheme for both exact and approximate simulation of discrete-to-continuous channels which conversely uses a fixed number of random samples, and therefore has a runtime independent of the channel and the input. Unlike existing channel simulation schemes which generate a sequence of independent samples from a proposal distribution, our approach generates one sample, or alternatively a fixed number of samples, from each potential target distribution. We then apply a latent permutation to the samples before performing sample selection using an exponential race. Our scheme provides a flexible tradeoff between the number of generated samples and the compression rate. Using polar and multilevel coding, we scale our approach to handle long blocklengths in $O(n \log n)$ time in order to benefit from reduced per-symbol overhead. We conclude by demonstrating applications to variable-rate compression with stochastic VQ-VAEs and communication-efficient differentially private distributed mean estimation via exact simulation of the Gaussian mechanism.

---


### 20. ["The Only Thing Certain About This is Uncertainty": Exploring Informal Care Coordination Practices Among Older Adults with Mild Cognitive Impairment](https://arxiv.org/abs/2609.12070)

**<font color=#1a73e8>作者：</font>** Josey M. Benandi, Niharika Mathur, Sangha Park 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Older adults aging in place often have informal support systems to help them maintain independence and quality of life. As they age, many older adults deal with the onset of Mild Cognitive Impairment (MCI), which introduces a new set of functional and cognitive changes that affect their ability to manage daily routines. The approach to arranging and coordinating support for everyday activities for older adults with MCI varies across informal care networks, but typically involves a primary care partner and a network of family, friends and others. In this paper, we present a thematic analysis of in-depth interviews with older adults with MCI and their primary care partners to gain a holistic picture of their day-to-day lived experience. Our analysis uses a multi-dimensional lens of people ("who"), activities ("what"), and tools ("how") to reveal insights about the nature of informal care coordination in MCI. Our results characterize informal care for MCI as a set of complex orchestration tasks by a primary care partner that support the practical, cognitive and emotional needs of the diagnosed individual and mediate the involvement of the broader care network. We uncover that coordination is not solely a matter of logistical organization, but also a deeply relational process shaped by negotiation with technological tools and evolving roles. Through this work, we reframe care coordination for MCI as a distinct and underexplored design space, one that demands systems capable of scaffolding autonomy, adapting to shifting capacities, responding to socio-emotional needs, and fostering collaborative caregiving.

---


### 21. [Does Video Memory Use What It Retrieves? A Causal Audit of Memory Specificity](https://arxiv.org/abs/2609.12090)

**<font color=#1a73e8>作者：</font>** Aditi Tiwari, Akshit Bhalla, Darshan Prasad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video models increasingly use memory to preserve information over long sequences, with the assumption that gains come from retrieving and using the correct past content. Standard memory ablations test whether memory helps, but not whether the retrieved content is responsible. We test this directly with read-time memory substitution, which replaces the consumed memory value while leaving the rest of the computation unchanged. This separates memory benefit from memory specificity, the extent to which the gain depends on retrieved content. Across frozen video world models, identity-free controls containing no evaluation-specific content recover essentially the full benefit on Ego-Exo4D and 7-Scenes and about 70% on TUM. In the Ego-Exo4D dose response, recovery falls from 102% to 1% as these values move away from observed training-memory representations, supporting representation repair as the best-supported explanation in this setting. WorldMem shows graded dependence. A wrong memory from the same trajectory recovers 94.1% of the PSNR benefit relative to zero content, while a donor from a disjoint trajectory and biome recovers 43.7%. SAM 2 shows strong content dependence. On DAVIS, replacing the correct spatial memory with a valid wrong memory reduces mean region and boundary score from 0.926 to 0.182. At MOSEv2 reappearance, it falls from 0.459 to 0.000. These results show that memory gains can depend on generic representation support, broader context, or exact episodic content. Read-time substitution provides a direct way to distinguish them.

---


### 22. [Score-based Outlier Generation via Controlling the Radon-Nikodym Derivative](https://arxiv.org/abs/2609.12113)

**<font color=#1a73e8>作者：</font>** Amartya Mukherjee, Tristan Milne, Kry Yik-Chau Lui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outliers are important for stress-testing algorithms and understanding system behaviour under rare conditions. Despite being commonly described as low-likelihood events, existing generative approaches rarely control likelihood explicitly. In this work, we introduce a measure-theoretic notion of outliers based on the distribution of log-likelihood values, which is guaranteed to assign higher probability mass to low-likelihood events with a specifiable magnitude. Building on this formulation, we derive how likelihood reweighting modifies the diffusion score and use this relation to motivate a controlled modification of the reverse-time dynamics. In particular, likelihood reweighting implies a scaling of the score function with a control term derived from the Radon-Nikodym derivative of the likelihood distributions. Correspondingly, the updated score function can be obtained with no retraining of the diffusion model. We exploit the Ornstein-Uhlenbeck semigroup underlying diffusion models to motivate an exponentially interpolated controller which approximates the true control. Experiments demonstrate controlled generation of low-likelihood samples while remaining consistent with the data geometry.

---


### 23. [DU-NO: A Parameter-Efficient Double U-Shaped Neural Operator for Phase-Resolving Wave Modeling](https://arxiv.org/abs/2609.12115)

**<font color=#1a73e8>作者：</font>** Enrique Hernandez Noguera, Md Meftahul Ferdaus, Nathan Cooper 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Phase-resolving wave models such as FUNWAVE-TVD are the accuracy standard for nearshore dynamics, resolving the shoaling, refraction, and breaking of individual waves, but their cost rules them out for the ensembles, uncertainty quantification, and real-time warning that operational forecasting demands. Neural operators promise solver-level accuracy at a fraction of that cost, yet on wave-dominated fields the accurate ones are large: hybrid spectral-convolutional operators such as U-FNO (the strongest baseline in our study after DU-NO) buy their fidelity with tens of millions of parameters. We introduce DU-NO (Double U-shaped Neural Operator), a multiscale U-shaped spectral operator that attaches lightweight convolutional U-Net branches only at its two shallowest encoder and decoder levels. The placement follows a sampling argument: high-wavenumber content exists only on fine grids, so the local, full-band pathways go where that content lives, while the coarse, band-limited levels stay purely spectral. A depth-decaying mode schedule holds the model to 3.64M parameters, an order of magnitude below U-FNO. On our publicly released FUNWAVE-TVD benchmark, DU-NO attains the best autoregressive rollout error of six identically trained architectures, improving on U-FNO by 14.9% with 10.8x fewer parameters, and a frequency-band analysis shows the gain holds across all bands, including the high-wavenumber band where truncated-spectral operators collapse. Parameter-matched controls confirm the gain is architectural: rescaled to the same 3.6M budget, the best baseline still trails DU-NO by 28.6%. The advantage carries beyond nearshore waves: DU-NO matches the strongest baselines on 2D Navier-Stokes and wins clearly on PDEBench shallow-water rollouts. Code, trained models, and evaluation artifacts are available at this https URL.

---


### 24. [When Successful Knowledge Graph Edits Displace Correct Answers: Rank-Level Locality beyond Parameter Support](https://arxiv.org/abs/2609.12116)

**<font color=#1a73e8>作者：</font>** Yi-Cheng Lai, Jerry Wang, Hsin-Ling Hsu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Editing a knowledge graph embedding (KGE) model to promote a desired answer can displace correct answers from the returned list. Locality tests based only on facts that reuse the edited parameter can miss this ranking effect. We introduce a common rank-displacement audit at three scopes: facts supported by the edited parameter, other correct answers to the target query, and correct answers across queries with the same relation. We also derive dimensional and geometric conditions for an update to improve the target while exactly preserving selected scores. On FB15k-237 with DistMult and ComplEx, direct promotion always moves the target into the top ten, but does so without damage in only 23.0--23.2\% of edits. Strict preservation causes no measured damage, yet succeeds in only 1.3--1.4\%. Support-regularized entity editing gives the highest joint success, 36.3--37.7\%, while rank-truncated preservation reaches 32.8--34.7\% and reduces the mean number of displaced answers from about 14 to 1.2. Experiments across dimensions, scorers, ranking conventions, and a learned editor show that locality depends on both the protected scope and the editing mechanism. KGE editing should therefore report correction success together with the incidence and severity of rank displacement.

---


### 25. [Almost Sure Convergence Analysis of Stochastic Gradient Methods with Clipping and Additive Noise](https://arxiv.org/abs/2609.12119)

**<font color=#1a73e8>作者：</font>** Amartya Mukherjee, Jun Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic gradient descent (SGD) with gradient clipping and additive noise has become a standard technique for training machine learning models, particularly in applications requiring robustness or privacy guarantees. However, clipping introduces a bias in stochastic gradients, while additive noise introduces additional variance, making the long-run behaviour of individual optimization trajectories difficult to characterize. In this work, we prove that SGD with clipping and additive Gaussian noise (SGD-CN) converges almost surely (a.s.) under smoothness and uniformly bounded stochastic-gradient noise assumptions, provided the step sizes satisfy some standard decaying conditions. Our analysis extends to momentum variants such as the stochastic heavy ball and Nesterov's accelerated gradient, where we show that careful energy constructions yield similar guarantees. These results provide stronger theoretical foundations for understanding the pathwise behaviour of clipped stochastic gradient methods and suggest that, despite the bias and noise introduced by clipping and perturbation, the algorithm remains stable in both convex and nonconvex regimes.

---


### 26. [Population-level measures of perceived food access reveal barriers beyond geographic proximity](https://arxiv.org/abs/2609.12132)

**<font color=#1a73e8>作者：</font>** Teresa Groton, Benjamin rachunok  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Food access is multidimensional, but population-level measurement still relies heavily on geography because perceived dimensions of access are difficult to measure at scale. Here, we use 25,125 Google Maps reviews from 49 grocery stores in Raleigh, North Carolina, to measure five dimensions of food access: availability, accessibility, affordability, accommodation, and acceptability. We identify review topics with unsupervised topic modeling and assign them to access dimensions using zero-shot classification, with 85.4% agreement against manual coding. The resulting store-level measures capture distinct aspects of food access and reveal barriers that geographic proximity alone does not capture. Comparisons between nearby stores in the same chain further show that identical store policies can be perceived very differently across locations, consistent with food access reflecting the fit between residents and their food environment. Perceived food access also follows systematic socioeconomic and demographic patterns that broadly parallel, but do not replicate, those observed for geographic access. These results show that online grocery reviews can provide a scalable complement to geographic measures of food access.

---


### 27. [Mined from Scientific Literature: Process Schemas for Atomic Layer Deposition and Etching in Materials Science](https://arxiv.org/abs/2609.12139)

**<font color=#1a73e8>作者：</font>** Sameer Sadruddin, Eleni Poupaki, Alex Watkins 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Atomic layer deposition (ALD) and atomic layer etching (ALE) are reported heterogeneously across experimental and simulation literature in materials science, hindering comparison and machine-actionable reuse. We present four domain-expert-reviewed JSON Schemas for ALD and ALE experimental and simulation processes. Curated with schema-miner and grounded in QUDT using schema-miner pro, the schemas structure materials, process conditions, configurations , and measured or predicted results. We compare their scope, structure, and semantic grounding, and demonstrate their use for schema-guided literature extraction and publication of structured records through ORKG templates.

---


### 28. [Hardware Fingerprinting FTQC via Quantum Decoder Timing](https://arxiv.org/abs/2609.12145)

**<font color=#1a73e8>作者：</font>** Friedrich Doku, Jakub Szefer, Kaitlin N. Smith  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As the quantum computing field transitions toward Fault-Tolerant Quantum Computing (FTQC), intensive efforts are focused on scaling architectures and realizing active error correction. However, this shift introduces security surfaces that remain largely unexplored. Fault-tolerant quantum computers pair a quantum processor with a classical decoder that sits on the critical path of every syndrome-extraction round. For the first time, this work demonstrates that the wall-clock time each decoder takes to process a syndrome measurement and decoding round constitutes a novel, exploitable hardware side channel on physical quantum hardware. Using per-shot decoder timings from three IBM Heron processors collected over a 68-day window, the decode-time distribution alone allows a passive observer to (i) reconstruct the shot-by-shot detector-firing distribution and estimate the workload's logical error rate $p_L$, (ii) infer the code distance in use, and (iii) fingerprint the specific physical device with up to 89% accuracy (a random guess is 33%), with a pooled two-sample Kolmogorov-Smirnov test confirming the decode-time distributions are statistically distinct. In noisy simulation inspired by public data from Google's 105-qubit Willow processor, decoder timing further distinguishes 9 surface-code patches at different locations on the chip with 81% accuracy, showing the side channel persists on below-threshold fault-tolerant hardware from a different vendor and code family.

---


### 29. [HSI-Road Relabeled: Surface-Aware Road-Scene Segmentation](https://arxiv.org/abs/2609.12151)

**<font color=#1a73e8>作者：</font>** Imad Ali Shah, Imran Mehmood, Enda Ward 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The HSI-Road dataset provides paired RGB and 25-channel NIR (600--960~nm) images with binary masks but no surface-level labels.~This paper introduces a manually labeled six-class taxonomy: Background, Asphalt, Concrete, Dirt, Water, and Grass, and an RGB-to-NIR registration pipeline with corresponding annotations. Six semantic-segmentation models (SSMs) are evaluated under four input configurations: original-resolution RGB (RGB$_{\text{ori}}$), registered low-resolution RGB (RGB$_{\text{reg}}$), NIR, and channel-stacked RGB$_{\text{reg}}$--NIR (RGBN$_{\text{stk}}$). The comparison quantifies the effect of spatial-resolution reduction on RGB, along with evaluation of NIR and RGBN$_{\text{stk}}$, with results reported using per-class and mean IoU and F1 scores. RGB$_{\text{ori}}$ achieves the highest overall performance but contains 12$\times$ more pixels than the matched-resolution inputs. At the matched 192$\times$384 resolution, RGBN$_{\text{stk}}$ outperforms NIR for all six SSMs and RGB$_{\text{reg}}$ for five of six, with the most consistent gains for the Water class. These results highlight the importance of spatial resolution while showing that NIR provides complementary information to RGB.

---


### 30. [Single-Query Person-Centric Bimanual Hand-Object Interaction Detection](https://arxiv.org/abs/2609.12155)

**<font color=#1a73e8>作者：</font>** Jonghyun Kim, Junho Roh, Yubin Yoon 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding person-level bi-manual interactions requires not only detecting hands, but also identifying which two hands belong to the same person and what each hand interacts with. Existing hand--object interaction methods are mostly hand-centric: they treat each hand as an independent instance, which can lead to ambiguous ownership in multi-person scenes.
We propose a person-centric formulation in which a single query predicts a structured output for one person, including the human box, body pose, hand boxes and states, and interaction targets. We introduce part-aware deformable attention to allocate attention across human, hand, and pose-specific reference regions, enabling one query to capture the full person structure. We further unify detection and interaction reasoning with a hand-to-query relationship matrix, where each hand selects its interaction target from the detected query set plus a learnable off token, directly recovering the target's box and class without separate object regression.
We build a COCO-based dataset with person-centric bi-manual interaction annotations and define structured metrics for evaluating hand states and complete hand--object tuples. Experiments with a transformer-based detector show that our formulation improves person-level bi-manual interaction parsing and provides an effective unified framework for joint detection, pose estimation, and hand reasoning.

---


### 31. [Certifying Concept Unlearning in Text-to-Image Diffusion Models](https://arxiv.org/abs/2609.12163)

**<font color=#1a73e8>作者：</font>** Mansi, Luca Marzari, Francesco Leofante  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing evaluations of concept unlearning in text-to-image (T2I) diffusion models primarily rely on attack success rates obtained through automated adversarial prompt search. However, these metrics provide only empirical evidence over a finite set of queries and leave residual leakage over the broader prompt space largely unquantified. This limitation can lead to overestimating unlearning effectiveness and underestimating safety risks. To address this gap, we introduce a novel certification framework for T2I concept unlearning that provides high-confidence guarantees with bounded error on residual concept leakage. Our approach combines statistical certification with worst-case analysis along concept-relevant embedding directions to derive explicit upper bounds on leakage probability under user-specified confidence levels. We evaluate our framework across three major concept categories namely NSFW content, artistic styles, and celebrity identities, and six state-of-the-art unlearning methods. Certified leakage bounds consistently exceed standard attack success rates by 16.2%, uncovering substantial residual risks missed by existing evaluation protocols. Crucially, our results demonstrate that empirical attack-based evaluations can significantly underestimate residual leakage and establish certification as a necessary complement for reliable auditing of concept unlearning in T2I diffusion models.

---


### 32. [GLARE: Generative Learning via Adversarial Reward Estimation For Social Dynamics Forecasting](https://arxiv.org/abs/2609.12165)

**<font color=#1a73e8>作者：</font>** Tenghao Huang, Zhaoxuan Tan, Muhao Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Meeting continuation requires tracking the agenda, speaker roles, participant intentions, and disagreement across long multi-party discussions. We introduce the Meeting Dynamic Forecasting Benchmark (MDFB), constructed from 2,207 real-world meetings and 24,794 future-facing queries. Given a transcript prefix and an active question, a model generates a plausible multi-turn continuation in one call. We evaluate utility---progress toward the question---and human-likeness---plausible conversational flow and role consistency---without requiring exact reproduction of the observed future. We further present GLARE, an adaptation of adversarial imitation learning to conditional language generation. A discriminator ranks the observed continuation above samples from the current actor, and its score supplies a KL-regularized policy reward; retraining on current-policy negatives allows the reward landscape to evolve with the actor. GLARE attains average human-evaluated win rates of 0.66 on utility and 0.70 on human-likeness, outperforming SFT and SPIN while remaining below the observed human continuation. We also demonstrate MDFB as a social reasoning arena for comparing general-purpose models, including closed-source systems, through reference-assisted judgments. Together, these studies illustrate the benchmark's use for both task-specific learning and output-based evaluation of meeting behavior.

---


### 33. [USPLIT-VQA: U-Shaped Split Learning for Visual Question Answering with Contribution-Aware Weighted Aggregation](https://arxiv.org/abs/2609.12168)

**<font color=#1a73e8>作者：</font>** Md Khalid Syfullah, Alvi Ataur Khalil  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Question Answering (VQA) systems, jointly interpreting images and natural language queries, hold significant promise across many domains, yet the privacy-sensitive nature of user data creates a fundamental barrier. Centralized training requires access to all data, while federated learning requires each client to host the full model. We propose USPLIT-VQA, a U-shaped split learning framework for privacy-preserving VQA in which each client retains the initial layers and the classification head while the server hosts the computationally heavy intermediate layers, keeping raw inputs and labels on the client device. We further introduce Contribution-Aware Weighted Aggregation (CAWA), a gradientsimilarity-based client scoring mechanism designed to reduce the influence of malicious updates. Experiments on four VQA datasets (VQA-RAD, SLAKE, PathVQA, and VizWiz) with two backbones show accuracy gains over Federated Learning for the Custom model and reduced accuracy for BiomedCLIP under the evaluated fixed split, alongside client memory reductions of up to 5.8X and communication reductions of up to 10.8X. With one malicious client, CAWA reduces the attacker's influence by over 98%, while experiments at higher corruption levels identify its limitations. Reconstruction experiments further show lower inversion quality under the evaluated attacks.

---


### 34. [When Ground-Truth Fidelity Matters: An Orchestrated UAS Framework for Wheat Streak Mosaic Virus Detection Using Vision Transformers and Machine Learning](https://arxiv.org/abs/2609.12169)

**<font color=#1a73e8>作者：</font>** Dewi Endah Kharismawati, Sandeep Dhakal, Courtney E. McCusker 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wheat streak mosaic virus (WSMV) is a destructive pathogen of sweet corn and other cereal crops, causing yield losses and complicating early detection because symptoms are spatially variable and subtle. In sweet corn seed production, WSMV also has regulatory importance, as phytosanitary regulations from countries such as New Zealand and Chile require seed lots to be certified virus-free. Visual scouting is unreliable because symptoms can resemble abiotic stress, while enzyme-linked immunosorbent assay (ELISA) is accurate but expensive, labor-intensive, and difficult to scale. We present an automated pipeline for plant-level WSMV detection using unmanned aircraft systems (UAS) multispectral imagery. The framework integrates orthomosaic reconstruction, geospatial alignment, plant extraction, and classification using a Vision Transformer with seven-channel inputs (five spectral bands, NDVI, and NDRE). Using treatment-based labels, the model achieved 89% accuracy on over 6,500 test patches across multiple growth stages. However, ELISA-based ground truth revealed substantial label noise: only a small fraction of sampled plants in inoculated plots were infected. Treatment labels therefore did not reliably represent infection status, and the high accuracy was largely driven by label bias rather than disease detection. Performance decreased markedly against row-level symptom severity and plant-level ELISA labels. Under these higher-fidelity but smaller-sample conditions, both deep learning and classical machine learning showed limited generalization and weak separability between ELISA-confirmed mock-inoculated and infected plants. These results show that UAS-based disease detection is constrained by label fidelity and data availability, emphasizing biologically grounded labels and models aligned with real-world conditions.

---


### 35. [Estimating Pedestrian Volumes from GIS-Derived Built-Environment Features: A Machine Learning Framework](https://arxiv.org/abs/2609.12173)

**<font color=#1a73e8>作者：</font>** Bahareh Golchin, Banafsheh Rekabdar, Sirisha Kothuri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transportation agencies need pedestrian volume estimates across entire road networks to prioritize safety investments, yet manual counts are expensive and cover only a small share of intersections. We present a machine learning pipeline that predicts 2-hour PM peak pedestrian volume at 101 urban intersections in Portland, Oregon, from built-environment, land-use, and street-network features drawn from open GIS data. Starting from the Negative Binomial GLM used in practice, we add feature selection, count-aware gradient boosting, and repeated cross-validation, selecting one configuration by a combined rank over RMSE, MAPE, and SMAPE across four cross-validation strategies. The winner, a histogram-based gradient boosting model with Poisson loss and L1 Lasso feature selection, reduces cross-validated RMSE by 12% over the GLM baseline (89.8 to 78.7) and holdout RMSE by 19% (108.0 to 87.9). Code is released on GitHub.

---


### 36. [Explanations-Driven Active Feature Acquisition for Algorithmic Recourse](https://arxiv.org/abs/2609.12179)

**<font color=#1a73e8>作者：</font>** Vinura Galwaduge, Jagath Samarabandu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Algorithmic recourse methods typically assume that a predictive model has access to all features of an individual. In practice, decisions are often made with partial information, because features are costly to acquire. Active feature acquisition addresses cost-constrained prediction, but existing methods are explanation-agnostic: prior work provides explanations only after acquiring additional features, rather than using explanations to drive acquisition. This work flips that and treats algorithmic recourse and feature acquisition jointly. We use Markov Blanket theory to unify counterfactual, semifactual, and alterfactual explanations and to characterize how available recourse grows as features are acquired. Building on this framework, we propose an Explanation-Driven Feature Acquisition (EDFA) method that selects features by explanatory value per unit cost. The framework is further extended with distribution-free validity guarantees for recourse issued from partial information, which signal trustworthy, lower-cost recourse, along with a lower bound on the calibration data required to certify them. Experiments on 7 publicly available datasets with neural network-based predictive models show that EDFA acquires substantially fewer features than state-of-the-art AFA baselines while maintaining comparable accuracy and yielding more decision-relevant, actionable recourse. The implementation is available on GitHub.

---


### 37. [QuPAINT: Physics-Aware Multimodal Reasoning for Quantum Material Characterization](https://arxiv.org/abs/2609.12202)

**<font color=#1a73e8>作者：</font>** Sankalp Pandey, Xuan-Bac Nguyen, Hoang-Quan Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Characterizing two-dimensional (2D) quantum materials by optical microscopy requires localizing exfoliated flakes and determining their layer thickness from subtle optical contrast and interference color to select suitable flakes for device fabrication. However, models face synthetic-to-real domain shifts and variation across materials, substrates, laboratories, and imaging conditions. We present QuPAINT, a physics-aware multimodal framework for transferable quantum flake characterization. The Synthetic Materials Framework (Synthia) generates diverse synthetic microscopy images while preserving layer-dependent optical behavior. Using these images, we construct QMat-Instruct, a multimodal instruction dataset with image-specific reasoning traces generated from verified annotations and constrained to observable optical cues. QuPAINT integrates these signals through Physics-Informed Attention (PIA), which injects substrate-relative optical priors into the visual representation to support grounded multimodal reasoning. For evaluation, we introduce QF-Bench, to our knowledge, the largest real-world benchmark for this problem, spanning diverse microscopy and substrate conditions. Using its verified annotations, we study counting, visual grounding, reasoning quality, confidence calibration, and transfer to an unseen material. QuPAINT-8B substantially outperforms prior methods and establishes state-of-the-art performance for both general and monolayer flake detection. Additional experiments show that image-grounded supervision improves strict spatial grounding and confidence calibration while preserving robust general flake detection on the unseen material.

---


### 38. [BRIDGE-EEG: Bridging Self-Supervised Pretraining and Efficient Deployment for Cross-Dataset EEG Classification](https://arxiv.org/abs/2609.12218)

**<font color=#1a73e8>作者：</font>** Meghna Roy Chowdhury, Chengwei Zhou, Haotian Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The growing use of electroencephalography (EEG) motivates automated analysis that is accurate, transferable, and deployable on constrained hardware. Recent EEG foundation models learn general representations from large-scale pretraining, but their size and computational cost limit edge and wearable deployment. We introduce BRIDGE-EEG, an efficient multi-task EEG classification pipeline that preserves the benefits of pretraining while reducing model size. A unified preprocessing scheme maps heterogeneous recordings with different channel counts, montages, and sampling rates to a device-agnostic 62-channel time--frequency representation. We pretrain an SE-ResNet18 teacher (11.84 M parameters) with SimCLR on unlabeled EEG from five heterogeneous datasets, then compress it into SE-ResNet8 (1.56 M) and SE-ResNet4 (0.48 M) students using task-agnostic and task-specific distillation. We evaluate six benchmarks spanning abnormality detection, motor imagery, and emotion recognition. For abnormality detection and emotion recognition, the students achieve accuracy comparable to or better than several recent EEG foundation models with 10--1,000$\times$ more parameters. Motor imagery shows a remaining representation gap, highlighting the importance of pretraining diversity. Inference profiling on a server GPU, desktop CPU, and NVIDIA Jetson Orin Nano shows up to 3.0$\times$ lower edge energy per inference (15.64 mJ vs. 46.67 mJ). The compact models further support future deployment on MCU-class wearables.

---


### 39. [Predicting Collision Cross Sections with GRACE: Geometric Residual Adduct Conditioning via Early-fusion](https://arxiv.org/abs/2609.12223)

**<font color=#1a73e8>作者：</font>** Parthasarathy Suryanarayanan, Susanta Das, Shreyans Sethi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collision cross section (CCS), derived from ion mobility mass spectrometry, is a common descriptor for molecular annotation. Prediction is challenging for machine learning models because it reflects the size, shape, and ionization state of a gas-phase molecular ion. Most predictors either ignore explicit 3D structure or treat adduct identity as a late categorical feature, which limits their ability to capture adduct-dependent geometric effects. We present GRACE (Geometric Residual Adduct Conditioning via Early-fusion), a 3D CCS predictor that adapts a pretrained molecular geometry encoder using geometric residual adduct conditioning via early fusion. GRACE combines two inductive biases: a residual objective relative to an adduct-aware physical descriptor baseline and adduct conditioning within the encoder via a learned adduct token and low-rank attention adapters. We evaluate the model on a curated set of over 9,000 experimental molecule-adduct CCS records with random, scaffold, and adduct-sensitive splits designed to separate interpolation, scaffold generalization, and adduct-driven generalization. GRACE achieves the best mean percentage difference among the evaluated learned models on all three splits: 1.67% on the random split, 2.11% on the scaffold split, and 2.36% on the adduct-sensitive split. Diagnostic analyses suggest that residual learning stabilizes training by removing the dominant mass-CCS trend, while early fusion improves adduct-sensitive prediction relative to late fusion. Across four independent external test sets, GRACE shows consistently lower error than the other evaluated models. On a held-out set, GRACE also attains the lowest mean percent difference when compared with four previously reported physics-based workflows. These results support residual learning and encoder-level adduct conditioning as practical inductive biases for fast, accurate CCS prediction.

---


### 40. [Patient-Reported Survey Data Improve Prediction of Opioid Use Disorder](https://arxiv.org/abs/2609.12224)

**<font color=#1a73e8>作者：</font>** Xiyue Jiang, Zihan Ding, Grace Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electronic health records (EHRs) may incompletely capture patient-reported factors associated with opioid use disorder (OUD). We evaluated whether survey data improve prediction of a first recorded OUD diagnosis among 267,747 All of Us participants with documented opioid exposure, including 15,287 OUD cases. We compared EHR-only and EHR+survey models across 6-, 12-, and 24-month look-back windows using logistic regression, random forest, XGBoost, LightGBM, multilayer perceptron, LSTM, GRU, and Transformer. Survey augmentation improved PR-AUC across all 24 model-window combinations by 0.0087-0.0505; the best 24-month LightGBM model improved from 0.6219 to 0.6603. Survey coverage increased with longer windows and differed by OUD status (24 months: 21.7% OUD-positive vs. 60.7% OUD-negative). Permutation analysis ranked survey features as the second most important information domain at 24 months in both evaluated models. Patient-reported data provide complementary predictive signals beyond structured EHRs while highlighting the importance of survey availability.

---


### 41. [PLSP (Pre-hoc Liminal Space Profiling): OOD Prediction over Detection -- An Anticipatory Approach for Machine Learning Model Reliability](https://arxiv.org/abs/2609.12225)

**<font color=#1a73e8>作者：</font>** Vipul Bansal, Himanshu Buckchash, Balasubramanian Raman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Out-of-Distribution (OOD) data poses a significant threat to machine learning models, often leading to model failure during deployment. All existing OOD detection methods are post-hoc, relying on evaluation metrics such as accuracy and AUC-ROC during inference to indirectly assess the model's response to OOD data by measuring deviations. In contrast to existing approaches, the proposed work shifts the paradigm from OOD detection to OOD prediction by proposing a pre-hoc anticipatory framework called PLSP for OOD prediction. We make several key contributions: (a) a dataset-independent metric called the CREDibility Score (CREDS) is proposed for OOD prediction; (b) credibility curves are introduced to study the maximum credibility a model can attain; and (c) credibility heat maps (and volume under surface) are introduced to characterize pre-hoc model behavior across different datasets. This work provides a novel perspective on signal processing under distributional shifts. Experiments across multiple datasets demonstrate that the proposed metric serves as a valuable measure for improving the robustness of machine learning models toward OOD prediction.

---


### 42. [Evaluating Practical Enumeration and Blocking Attacks on the Snowflake Circumvention System](https://arxiv.org/abs/2609.12242)

**<font color=#1a73e8>作者：</font>** Linden Chen, Ryan Sangha, Cecylia Bocovich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Proxy-based Internet censorship circumvention tools like Snowflake rely on large, dynamic pools of third-party proxies to resist IP-based blocking. We focus on two assumptions underpinning the security of Snowflake: that adversaries cannot easily enumerate proxy IPs, and that blocking those proxies would incur unacceptable collateral damage. In this paper, we test these assumptions by studying practical enumeration and blocking attacks against Snowflake conducted by malicious clients.
We combine bounded, ethical real-world measurements with large-scale simulation to evaluate both present-day enumeration and blocking risk and broader attacker capabilities. Over 48 days of real-world measurements from May--June 2025, our attack enumerated over 21,000 unique proxy IP addresses belonging to almost 1,000 autonomous systems. Despite this high number, we find that proxy churn limits the overall effectiveness of enumeration over time, and reduces the impact on clients of individual proxy addresses being blocked. However, at the network level, blocking the top 1% of observed autonomous systems blocks more than 30% of observed Snowflakes while affecting 0% of Tranco Top 100 domains and ~2.5% of Top 1M domains. We discover that the broker's load-aware matching reveals stable, high-capacity proxies to attackers early, especially during periods of elevated demand such as the censorship even in Iran of June 2025, subsequently exposing the networks that contribute disproportionately to system connectivity. In simulation, increasing attacker scale sharply improves both enumeration and blocking success, while higher proxy churn significantly reduces blocking effectiveness. We conclude by discussing and evaluating practical mitigations, some of which have been integrated into Snowflake.

---


### 43. [CRFCAN: A Complex-Valued Cross-Domain Residual Network for Joint Channel and Phase Noise Estimation in Sub-THz OFDM Systems](https://arxiv.org/abs/2609.12244)

**<font color=#1a73e8>作者：</font>** Ruilin Wang, Xiaodai Dong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In sub-terahertz (sub-THz) communications, the coupling of ultra-wide bandwidth and severe phase noise (PN) impairments renders conventional joint channel and PN estimation highly complex and computationally prohibitive. To address this, we propose CRFCAN, a complex-valued residual FFT convolutional attention network designed for joint channel and PN estimation. Unlike existing deep learning schemes that rely on cascaded networks or hybrid frameworks combining neural networks with conventional iterative estimators, CRFCAN performs joint recovery in a truly end-to-end fashion through a physics-inspired cross-domain structure. Specifically, Fast Fourier Transform (FFT) and inverse FFT modules are embedded within residual groups to enable iterative feature interaction across the time and frequency domains, thereby capturing both frequency-selective fading and time-varying phase distortions. In addition, two dedicated residual blocks are introduced for complex feature extraction and multiplicative phase-distortion modeling, respectively. A physics-aware PN output tail with soft normalization is further employed to improve estimation stability while preserving the physical characteristics of the effective PN process. Simulation results demonstrate that CRFCAN significantly outperforms conventional algorithms and state-of-the-art deep learning models in terms of normalized mean square error (NMSE) and bit error rate (BER). Notably, CRFCAN achieves superior performance with single-shot, fixed-complexity inference and generalizes well to unseen PN models without fine-tuning, highlighting its robustness and practicality for sub-THz receivers.

---


### 44. [Soft Symbol Grounding for Prototypical Concepts](https://arxiv.org/abs/2609.12247)

**<font color=#1a73e8>作者：</font>** Marcos Galván-López, Nijesh Upreti, Hiram Calvo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neuro-symbolic models are usually trained with supervision only on final labels, leaving the intermediate concepts unobserved. Since many concept assignments are consistent with a given label, training can predict labels correctly while recovering the wrong concepts, a failure known as a reasoning shortcut. Prototypical networks reduce shortcuts by anchoring each concept to a few labeled examples, but existing methods still couple perception and reasoning through a hand-crafted, task-specific differentiable loss that must be redesigned for every task. We introduce \textbf{Soft-PNet}, which removes this loss: it reframes concept grounding as a Metropolis walk over a precomputed cache of feasible symbolic solutions, guided by a prototype distribution built from a single labeled anchor per concept, and trains against one KL objective between the prototype-weighted cache and the network's concept predictions. The objective is identical across tasks and remains applicable when the solution space cannot be enumerated. On \texttt{MNIST-EvenOdd}, Visual Sudoku, and \texttt{Kand-Logic} under scarce supervision, Soft-PNet matches loss-engineered prototypical networks at the concept and label levels and recovers concepts that soft-grounding baselines miss, with no loss engineering and lower training time.

---


### 45. [The Rank the Task Demands: A Causal Rank Law for Matrix Memories Trained on Group Composition](https://arxiv.org/abs/2609.12259)

**<font color=#1a73e8>作者：</font>** Samuel Larson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix-valued memories make rank the natural budget of a learned representation: the number of independent directions a state spans bounds what it can bind, compose, and track. We report causal evidence, on a group-composition testbed trained under a hard single-state bottleneck with a fixed decoder that cannot launder rank, that gradient descent recruits precisely the rank the task's algebra demands. A companion paper [Larson, 2026a] establishes the analogous recruitment and causal necessity pattern on a $K$-pair associative-binding testbed, where exact recovery provably requires state rank at least $K$; this paper inherits that instrument and extends the rank law from a scalar capacity bound to a representation-theoretic one. We train toward chosen minimal faithful reference representations embedded in larger matrices. On group-composition state tracking over five finite groups spanning the solvable/non-solvable divide, the recruited rank equals the group's minimal faithful real representation dimension $d_{\min}$ (Spearman $\rho = 0.9747$, the design's tie-capped maximum), the dimension-matched solvable/non-solvable pair $S_4$/$A_5$ is statistically equivalent under a pre-registered test, and a pre-registered force-rank test separates a guaranteed similarity ceiling from empirical recovery at the target dimension: one rank below $d_{\min}$, cosine similarity is capped by the target's tied unit spectrum at $\sqrt{(d_{\min}{-}1)/d_{\min}} \le 0.894$, below the $0.9$ threshold in every group by construction, with observed cells at 86-95% (mean 91%) of that ceiling; at $d_{\min}$, not guaranteed a priori, recovery clears the pre-registered anchor-relative bar at four seeds per group in all five groups. Within this testbed, measured effective rank tracks representation dimension; the matched-dimension $S_4$/$A_5$ comparison establishes equivalence within the pre-registered tolerance.

---


### 46. [Revisiting Multi-Object Tracking Baselines: Hyperparameter Optimization with Multi-Fidelity Greedy Coordinate Search](https://arxiv.org/abs/2609.12261)

**<font color=#1a73e8>作者：</font>** Momir Adžemović  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object tracking (MOT) is dominated by the tracking-by-detection paradigm, whose methods typically rely on a small set of hyperparameters that are conventionally chosen by hand. Tuning them requires repeated expert-guided experimentation, while the procedures used to select reported values are often not systematically evaluated or fully documented. Hyperparameter optimization (HPO) automates this process, yet it remains rarely used in MOT, and existing studies applying HPO to MOT predate modern deep-detector-based trackers and HOTA evaluation. We systematically apply HPO across two datasets and four tracking-by-detection methods. We also propose Multi-Fidelity Greedy Coordinate Search (MFGCS), which optimizes one hyperparameter at a time by first evaluating candidate values on a small subset of scenes and re-evaluating only promising candidates on the full dataset. Across all eight tracker-dataset combinations, the Tree-structured Parzen Estimator (TPE) and MFGCS outperform both our hand-tuned configurations and the corresponding published results, with improvements of up to 4.38 and 16.05 HOTA points, respectively. MFGCS also reaches a predefined HOTA target faster than TPE in seven of the eight combinations. Within each tracker-dataset pair, all optimizers share the same search space and evaluation pipeline, isolating the effect of the search strategy. We release the code and tuned configurations to enable future work to compare against systematically optimized rather than default or manually tuned baselines.

---


### 47. [A First-Principles Evaluation of Graph-Based Network Intrusion Detection Systems](https://arxiv.org/abs/2609.12263)

**<font color=#1a73e8>作者：</font>** Rui Zhao, Wajih Ul Hassan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Graph-based network intrusion detection systems (GIDS) report strong benchmark detection metrics, but those metrics establish little about deployability. We approach the problem from first principles: rather than inheriting the preprocessing, windowing, and thresholding conventions of each published system, we ask what a controlled comparison requires and impose it uniformly. The result is GIDS-Eval, an evaluation framework that decomposes a GIDS into six interchangeable stages and turns those conventions into explicit experimental variables, so reported performance can be attributed to individual stages instead of whole pipelines. We survey nine representative GIDS, reimplement five of them within GIDS-Eval, and evaluate them on four datasets under one matched protocol. We identify nine recurring evaluation gaps and quantify the impact of each: two crafted edges achieve full evasion against three of the eight detector-dataset pairs with anything to hide; the snapshot window alone accounts for a mean 38.3% relative swing in average precision (AP); aligning preprocessing across systems moves AP by up to 61.8 percentage points for a single detector; and none of the 18 detector-dataset pairs we replay can alert as events arrive. We introduce GIDS-Lite, an encoder-free control built in the same framework, which ranks first by AP on two of the four datasets at up to 575$\times$ lower runtime. Architectural complexity is therefore not a consistent driver of detection quality under our matched protocol on current benchmarks, but it does enlarge the runtime, calibration, and attack surfaces operators must defend.

---


### 48. [Adaptive Chemotherapy Control under Tumor Heterogeneity via Reinforcement Learning](https://arxiv.org/abs/2609.12264)

**<font color=#1a73e8>作者：</font>** Bereket Sitotaw Kidane, Md Samiul Haque Motayed, Shuo Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing effective chemotherapy regimens is hindered by tumor heterogeneity and drug resistance, which complicate the deployment of patient-specific model-based optimal control across diverse populations. We develop and compare closed-loop deep reinforcement learning (DRL) dosing policies with continuous (TD3) and discrete (DQN) action spaces trained on a high-dimensional heterogeneous tumor model. The DRL policies are benchmarked against a Pontryagin's Maximum Principle (PMP)-derived open-loop benchmark. We assess generalization under parametric heterogeneity using a 100-patient virtual cohort with plus or minus 10 percent uniform perturbations in growth and drug-sensitivity parameters. Across this cohort, TD3 achieves higher average tumor reduction, while DQN yields tighter inter-patient dosing consistency, revealing a clear efficacy-consistency trade-off in this study. Our simulations assume full observation of all tumor subpopulations; translation to sparse and noisy clinical measurements will require partial-observability formulations and/or state estimation. Overall, the results show that simulation-trained DRL can learn state-dependent feedback dosing policies that complement open-loop optimal control benchmarks.

---


### 49. [Learning Symbolic Constraint Representations from Examples: A Neuro-Symbolic Approach](https://arxiv.org/abs/2609.12267)

**<font color=#1a73e8>作者：</font>** Nassim Belmecheri, Arnaud Gotlieb, Nadjib Lazaar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning user-defined concepts as constraint networks has been extensively studied in the constraint acquisition (CA) literature. However, existing approaches typically rely on intensive interactions with a human oracle, making the learning process costly in terms of time and number of queries. In this paper, we propose a neuro-symbolic framework for automatic CA that significantly reduces user involvement by introducing neural Oracle Transformer models which learn to emulate user responses and to generalize conceptual knowledge. Trained on previously available examples, the learned oracle interacts with a dedicated CA engine, FastCA, which systematically refines the oracle's responses into a sound, consistent, and interpretable constraint network. This neuro-symbolic interaction enables the recovery of structured symbolic models from data without prior domain knowledge. Our results demonstrate that this neuro-symbolic interplay effectively aligns data-driven pattern recognition with symbolic reasoning, offering a robust approach to automating model construction in combinatorial domains.

---


### 50. [Synthetic TLX: Forecasting Human Workload Using Agent Simulation](https://arxiv.org/abs/2609.12273)

**<font color=#1a73e8>作者：</font>** Tzu-Sheng Kuo, Carrie J. Cai, Meredith Ringel Morris 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Assessing human workload for technology-mediated tasks helps prevent task failure caused by poor technology design. Traditionally, workload is assessed retrospectively using the NASA Task Load Index (TLX) after humans complete a task. What if we could forecast workload before a human attempts a task using agent simulation? We introduce Synthetic TLX, a new paradigm for proactive workload estimation that predicts NASA TLX scores for a given task, unlocking novel interaction opportunities and evaluation methods. To understand its viability, we conducted three experiments comparing human and agent-generated scores to evaluate where they align and diverge. We found agent estimates align with human scores particularly when prompted with a human persona and active task simulation. However, agents and humans diverge in the sources of workload they are sensitive to. Based on our findings, we present three applications to showcase Synthetic TLX's potential and discuss the future of workload-aware human-AI interaction.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-201](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
