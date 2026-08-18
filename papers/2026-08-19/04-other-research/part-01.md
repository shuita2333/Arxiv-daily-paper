# 📦 其他研究 | 2026年08月19日

> 本类共 **435** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-435](./part-09.md)

---

### 1. [FLOPs vs Real Work: The Importance of Replication in AI Efficiency Assessment](https://arxiv.org/abs/2608.14550)

**<font color=#1a73e8>作者：</font>** Enrique Barba Roque, Luís Cruz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI efficiency has recently taken the spotlight in both academy and industry due to massive model scales, high energy demands, and environmental costs. While reporting Floating Point Operations (FLOPs) is a traditional approach for assessing computational costs, the relationship between FLOPs and execution time is not straightforward, as layers with the same number of FLOPs may not have the same execution time because some operations are more easily parallelized than others. This paper sets out to replicate the original experiments from a study that proposed the $\alpha-FLOPs$ estimation formula to verify whether the results remain applicable on newer, more powerful hardware.
During the replication process, we identify limitations in the replication materials provided by the original study, including a lack of specific dependency details and transparency regarding regression data. Our results validate the thesis that raw FLOPs alone are not an appropriate metric for execution time, as spatial dimensions remain more easily parallelized than kernel dimensions. However, fine-grained measurements reveal that the relationship is much less straightforward than previously shown, with newer hardware exhibiting instabilities and discontinuities in execution time, including jumps and oscillations, that the $\alpha-FLOPs$ formula generally underestimates. Ultimately, this work validates the empirical findings from the original study but shows negative results when applying the $\alpha-FLOPs$ estimation. We also highlight the critical need for complete and accurate replication packages for research on hardware-dependent efficiency assessment and provide a complete replication package for our implementation to facilitate further study.

---


### 2. [Learning Discrete Riemannian Metrics for Physical Fields with Cochain-Frame Equivarianc](https://arxiv.org/abs/2608.14556)

**<font color=#1a73e8>作者：</font>** Dongzhe Zheng, Christine Allen-Blanchette  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical fields on meshes require a separation between topology and geometry: conservation laws are topological and should be exact, while geometry, material response, and anisotropic coupling must be learned from data. Existing neural surrogates often mix these roles inside unconstrained message passing. We introduce Riemannian Hodge Message Passing (RHMP), which turns this separation into an architectural principle. RHMP fixes the cellular coboundaries ($d_k$) determined by oriented incidence and learns symmetric positive-definite cochain metrics ($H_k$) for geometry-dependent propagation. Treating $H_k$ as the learned metric motivates cochain-frame equivariance: physical propagation should be invariant to orthogonal changes of the hidden cochain feature basis. RHMP implements this principle with metric-weighted Hodge blocks ($d_k^\top H_{k+1}d_k$), yielding exact cochain-complex identities ($d_{k+1}d_k=0$), nonnegative Hodge energies, positive-semidefinite operators, and exact Abelian curvature invariance. Across seven physical benchmarks spanning fluids, electromagnetism, gauge fields, and variable-mesh CFD, RHMP achieves the best overall performance, with the largest gains when topology, learned geometry, and field structure interact.

---


### 3. [When to Communicate: Belief Distributions and KL Divergence for Principled Gating in Multi-Agent RL](https://arxiv.org/abs/2608.14559)

**<font color=#1a73e8>作者：</font>** Teoman Kaman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective communication in multi-agent reinforcement learning requires agents to decide not only \textit{what} to communicate, but when? Existing approaches either communicate at every timestep or learn a binary gate through REINFORCE policy gradients \cite{singh2019}, a high-variance signal that produces unstable and uninterpretable gating behavior. I propose a principled alternative: agents communicate only when the KL divergence between their learned belief distributions exceeds a fixed threshold. Each agent maintains a belief distribution over a latent world state computed as a softmax over its LSTM hidden state, and communicates only when belief disagreement is large enough to justify information exchange. I evaluate this approach on the Predator-Prey benchmark from IC3Net \cite{singh2019} across two environment sizes with 5 seeds each, and on MPE simple\_spread \cite{lowe2017}, comparing against IC3Net, CommNet, and an independent controller. On PP 10$\times$10, IC3Net outperforms KL-belief at all thresholds. On the harder PP 20$\times$20, a threshold ablation over $\varepsilon \in \{0.1, 0.3, 0.5, 1.0\}$ reveals an inverted U-shape: $\varepsilon=0.5$ achieves 73.84 average steps and 42\% success rate versus IC3Net's 75.31 steps and 31\%, a gap of 1.47 steps and 11 percentage points with tighter seed variance. On MPE, the belief head improves mean reward by 12 points and reduces variance by 26$\times$ even when gating is inactive, suggesting two orthogonal contributions: principled gating when beliefs can converge, and improved latent representations that benefit coordination regardless.

---


### 4. [Global AI Regulations for FAIR and Ethics in High-Risk Use Cases: A Comparative Review](https://arxiv.org/abs/2608.14562)

**<font color=#1a73e8>作者：</font>** Aasish Kumar Sharma, Dimitar Koysev, Christopher Anich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI governance is shifting from voluntary ethics to enforceable, risk-based regulation, yet cross-jurisdictional divergence creates compliance uncertainty for operators of high-stakes AI. We present a comparative matrix for the EU, US, and China that maps (i) risk classification triggers, (ii) binding obligations, (iii) enforcement and accountability mechanisms, and (iv) the degree to which FAIR principles are operationalised in practice. We stress-test the matrix on three high-impact domains: Electroencephalography (EEG)-guided rehabilitation robotics, AI-enabled debt collection in prospective Central Bank Digital Currency (CBDC) ecosystems, and AI-driven allocation of scarce Graphics Processing Unit (GPU) resources in emerging AI Factory infrastructures. Using primary legal texts and implementation evidence, we identify three recurring gaps: weak interoperability mandates, difficult operationalisation of cross-regime obligations (AI + sector regulation + data protection), and under-specified governance for critical digital infrastructure use cases. To bridge the implementation gap, we outline Knowledge Blocks, a machine-checkable compliance artefact pattern based on Resource Description Framework/Web Ontology Language (RDF/OWL), Shapes Constraint Language (SHACL), and Provenance Ontology (PROV-O), enabling audit-ready compliance-by-design across multiple regimes.

---


### 5. [From Doyle to AGM: A Survey and an Implementation Roadmap for Belief Change](https://arxiv.org/abs/2608.14567)

**<font color=#1a73e8>作者：</font>** Yuri Almeida, Arthur Casals  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a targeted narrative review establishing the historical and theoretical foundations for computational belief change implementation. Seeded by Doyle and London's foundational 1980 taxonomy, we trace the evolution of belief revision from computational origins through the theoretical transformation of the AGM framework to contemporary approaches. Our analysis demonstrates how pre-AGM computational pragmatism relates to AGM theoretical constructs, revealing both continuities and transformations across this evolution. We analyze how each taxonomical category evolved in the post-AGM era, identifying the theoretical foundations and historical precedents that inform contemporary implementation challenges. This foundation enables subsequent research into robust computational blueprints that synthesize historical insights with formal guarantees, providing the baseline for systematic implementation analysis and engineering-focused belief change research.

---


### 6. [Position: AI Governance Needs ISO-like Interoperability Protocols, Not Just Laws](https://arxiv.org/abs/2608.14568)

**<font color=#1a73e8>作者：</font>** Azmine Toushik Wasi, Mst Rafia Islam, Mahfuz Ahmed Anik 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As Artificial Intelligence (AI) systems become deeply integrated into critical global infrastructure, the urgency for robust governance frameworks has intensified. However, current approaches, led by jurisdiction-specific laws, policies, and voluntary frameworks such as the EU AI Act, China's algorithm governance, and the NIST AI Risk Management Framework in the U.S., create a fragmented regulatory landscape. In this position paper, we argue that \textbf{\textit{AI governance must be built not on laws alone, but on ISO-like interoperability protocols that enable standardized, machine-readable risk communication across borders}}. Drawing on the success of the GDPR, which was operationalized through standards like ISO 27001 and Privacy by Design, we propose the development of standardized AI \textit{nutrition labels} containing unified metrics for bias, energy usage, and data provenance to facilitate cross-jurisdictional compliance. These manifests would lower barriers for small and medium enterprises (SMEs), reduce redundant regulatory efforts, and build public trust. The paper addresses concerns that standards may stifle innovation by advocating for modular, versioned protocols designed to evolve in tandem with technological change. Overall, we call for a shift from siloed legal compliance toward interoperable technical conformance, enabling a shared global language for responsible AI deployment.

---


### 7. [Position: Certified Correctness in Neural Constraint Reasoning Requires Symbolic Integration](https://arxiv.org/abs/2608.14569)

**<font color=#1a73e8>作者：</font>** Shufeng Kong, Xiaochuan Zhang, Caihua Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural solvers for constraint satisfaction problems have achieved remarkable in-distribution accuracy, yet they suffer from a fundamental limitation persistent constraint violations occur under distribution shifts even when the model reports high confidence. This position paper argues that when hard constraints exist and the cost of verification is relatively low, neural constraint reasoning must prioritize symbolic integration over pure learning. We justify our focus on Sudoku as a representative NP-complete testbed because it exhibits a sharp asymmetry between easy verification and hard solving: checking a candidate solution requires only polynomial time $O(n^{2})$, while finding a solution may require exponential search. Through a comprehensive survey of solving methods spanning deterministic algorithms, metaheuristic optimization, learning-based approaches, and language-conditioned reasoning, we demonstrate that neural-only methods without instance-level certification fail to achieve the provable correctness that symbolic and neuro-symbolic approaches provide. We advocate for a bidirectional integration in which neural methods enhance symbolic solvers by learning heuristics and converting percepts into symbols, while symbolic methods verify neural outputs to ensure their reliability. To operationalize this position, we propose a multi-agent certified reasoning framework that demonstrates how this integration can achieve both computational efficiency and provable correctness.

---


### 8. [Coarse-to-Fine Multi-Resolution Diffusion Models for Trajectory Generation in Urban Systems](https://arxiv.org/abs/2608.14570)

**<font color=#1a73e8>作者：</font>** Wen Ye, Muyan Weng, Chuizheng Meng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding human mobility is critical for a wide range of urban applications, including traffic management, epidemic control, and urban planning. However, due to privacy concerns, the availability of large-scale public trajectory data remains limited, posing challenges for downstream mobility analysis. Existing methods for synthetic trajectory generation primarily focus on matching global distribution similarity, while often overlooking mobility patterns across different spatial and temporal resolutions that are essential for practical utility.
To address these challenges, we propose a novel multi-resolution diffusion framework, MR-Traj, for large-scale trajectory generation. MR-Traj explicitly models trajectories as compositions of coarse-grained milestones and fine-grained segments, enabling the capture of complex spatial-temporal dependencies at multiple resolutions. Experimental results demonstrate that MR-Traj achieves comparable performance to state-of-the-art methods in terms of global distribution similarity, while consistently outperforming them in modeling fine-resolution mobility patterns and supporting downstream urban mobility tasks. In addition, by introducing stochasticity at multiple resolution levels, MR-Traj generates more diverse trajectories, which empirically reduces trajectory linkage risk under a seed-guided data release setting. Our code is available at this https URL.

---


### 9. [Position: Want Better ML Reviews? Stop Asking Nicely and Start Incentivizing with a Credit System](https://arxiv.org/abs/2608.14571)

**<font color=#1a73e8>作者：</font>** Shaochen Zhong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With soaring submission counts, stricter reciprocal review policies, widespread adoption of platforms like OpenReview, and without the offsetting pressure of publication fees, the machine learning (ML) community has one of the largest scholarly presences among all scientific fields. And yet, \textbf{almost \textit{everyone} has \textit{many} unpleasant things to share about their review experience.} Worse, there is little public space to seriously discuss, let alone debate, what makes a review system effective or how it might be improved.\quad In this position paper, we expand our discussion from two core problems: \textit{How can we reasonably limit submission volume?} and \textit{How can we incentivize good and discourage bad reviewing?} We first assess the strengths and shortcomings of existing attempts to address such problems. Specifically, we present four takes on some popular conference mechanisms and propose two alternative designs for improvement.\quad Our general position is that meaningful improvement in ML peer review won't come from polite best-practice suggestions tucked into Calls for Papers or Reviewer Guidelines: it requires \textbf{enforceable yet fine-grained procedural safeguards} paired with \textbf{a currency-like credit system (e.g., our proposed \textit{OpenReview Points})}. ML practitioners can ``earn'' such points by contributing good review practices, and ``spend'' them across one or multiple major conferences to redeem different kinds of ``perks,'' such as complimentary registration or the right to request additional review resources.

---


### 10. [Longitudinal and Graph-Augmented Prediction of Adolescent Substance Use Onset in the ABCD Study](https://arxiv.org/abs/2608.14578)

**<font color=#1a73e8>作者：</font>** Yixuan He, Jinni Su, Yun Kang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early identification of adolescent substance-use risk is an important prevention challenge, yet the relative value of baseline characteristics, longitudinal trajectories, and relational context remains unclear. Using data from approximately 11,860 participants in the Adolescent Brain Cognitive Development (ABCD) Study, we compare cross-sectional, longitudinal, and graph-based approaches for predicting alcohol sipping, alcohol use, marijuana use, and alcohol/marijuana use. We evaluate tree-based models, recurrent neural networks, and Temporal Graph Convolutional Networks (T-GCNs) constructed from family, school, and feature-similarity graphs. Longitudinal models consistently outperform baseline models, with temporal XGBoost achieving the strongest standalone performance. Although T-GCNs generally do not surpass temporal XGBoost, graph-derived risk scores provide complementary information. Combining temporal XGBoost and T-GCN predictions through score-level stacking yields the best performance across all outcomes, achieving AUC-ROC values above 0.79. Feature analyses identify peer deviance, age, externalizing symptoms, parental monitoring, cultural norms, and neighborhood context as important predictors of substance use onset. These findings demonstrate the value of longitudinal modeling for substance-use prediction and suggest that graph-based representations can provide effective auxiliary risk signals.

---


### 11. [Multi-Modal Generative Fuzzy System: Fuzzy Inference Guided Large Model Interactive Question Answering Framework](https://arxiv.org/abs/2608.14584)

**<font color=#1a73e8>作者：</font>** Hailong Yang, Jianqi Wang, Guanjin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In Multimodal Question Answering (MQA), models are required to jointly encode and integrate heterogeneous information from multiple modalities, including text, images, and speech, to perform complex semantic reasoning and decision making. Despite recent advances, existing approaches, including traditional deep learning models and Large Models (LMs) or prompt-based frameworks, continue to face several critical challenges. First, modality bias arises from discrepancies in feature distributions across different modalities, which limits effective cross modal collaborative understanding. Second, many questions require knowledge drawn from multiple domains, introducing significant uncertainty. Third, current methods often rely on shallow semantic matching, resulting in limited reasoning depth an reduced interpretability. To address these issues, inspired by the traditional fuzzy system (FS) framework, we propose a fuzzy-inference-guided multimodal generative architecture termed the Multi-Modal Generative Fuzzy System (MMGFS). The main contributions of MMGFS are two folds. First, it alleviates modality bias through a multimodal collaborative rumination mechanism. Second, it introduces fuzzy rules and a multi-hop inference mechanism to support cross-domain knowledge fusion and hierarchical reasoning, thereby strengthening uncertainty modelling and deepening semantic understanding. We conduct comprehensive evaluations on open-domain question answering datasets, including MultimodalQA and WebQA, as well as domain-specific benchmarks, including BioMol-VQA and EHRxQA. Experimental results demonstrate that MMGFS consistently outperforms existing methods across multiple datasets. It effectively mitigates modality bias and question uncertainty while achieving superior performance in answer accuracy, consistency, and generalization.

---


### 12. [Geometry Is Not Robustness: A Trajectory-Level Study of PGD Evaluation](https://arxiv.org/abs/2608.14594)

**<font color=#1a73e8>作者：</font>** Dhairysheel Durgule  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Projected Gradient Descent (PGD) is widely used to evaluate adversarial robustness, typically via final adversarial accuracy, which does not capture model behaviour throughout the attack. Recent work proposes trajectory-level diagnostics, such as loss evolution, gradient alignment, and steps-to-failure, for deeper insight into adversarial optimisation dynamics. However, whether these diagnostics reliably indicate robustness strength remains unclear. We conduct a trajectory-level investigation of PGD attacks on convolutional neural networks trained on Fashion-MNIST. We compare clean-trained and adversarially-trained models across multiple robustness regimes, using rigorous 20-step PGD evaluations with random initialisation and multiple restarts for robustness measurement, and single-initialisation trajectory recording for diagnostics. We record full PGD trajectories across 3000 clean-correct samples per model and analyse loss evolution, gradient alignment, and failure timing across attack iterations. Our results reveal a clear robustness hierarchy across models; however, trajectory metrics do not contribute equally to its identification. Mean loss trajectories and gradient alignment patterns appear quantitatively similar across adversarially-trained models with substantially different robust accuracies. In contrast, steps-to-failure distributions provide a clearer separation of robustness regimes, directly reflecting functional resistance to adversarial perturbation. These findings indicate that trajectory-level diagnostics describe optimisation geometry but do not independently measure adversarial robustness. Their interpretability depends on robustness regime, attack strength, and multi-metric evaluation. Trajectory-level analysis should be a complementary diagnostic tool, interpreted in context, rather than a replacement for standard robustness measurements.

---


### 13. [Position: Medical AI Neglects Real Treatment Outcomes](https://arxiv.org/abs/2608.14598)

**<font color=#1a73e8>作者：</font>** Shiva Kaul, Anjum Khurshid  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical AI has rapidly improved its ability to perform diagnostic and prognostic tasks that lead to treatment decisions. But understanding of treatment itself is still inadequately trained and evaluated, using human opinions and syntheses (especially texts such as biomedical publications and clinical practice guidelines) rather than actual underlying data on treatment outcomes. This neglect seriously limits the potential of medical AI, and is already causing deficiencies in both frontier models and major benchmarks, as argued in this position paper. Real treatment outcomes, drawn from sources such as observational databases and randomized experiments, should be substantially incorporated into both training and evaluation. Improving these outcomes should be reemphasized as the downstream goal of all medical AI.

---


### 14. [PIKFNO: An Interpretable Neural Operator Based on Physics Informed Kernel Function](https://arxiv.org/abs/2608.14619)

**<font color=#1a73e8>作者：</font>** Yuan Guo, Hanshu Chen, Zhuojia Fu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work proposes a new interpretable neural operator framework, termed the Physics Informed Kernel Function Neural Operator (PIKFNO), which explicitly incorporates physics informed kernel functions derived from governing equations into the neural operator architecture. Unlike traditional neural operators such as DeepONet, which rely on deep networks to implicitly learn basis functions, PIKFNO constrains the trunk network through physics informed kernel functions, thereby aligning its operator structure with the kernel expansions used in meshless collocation methods. Two construction strategies are introduced: one learns kernel functions directly from data, where the learned kernel can be regarded as a nonsingular fundamental solution, while the other builds them through transformations of analytical fundamental solutions. Numerical experiments demonstrate that PIKFNO achieves high predictive accuracy with substantially improved interpretability and superior generalization under limited training data. The proposed framework offers a new pathway for developing efficient, physically consistent, and interpretable neural operators.

---


### 15. [Explaining Reinforcement Learning Decisions in Self-adaptive Systems](https://arxiv.org/abs/2608.14620)

**<font color=#1a73e8>作者：</font>** Jasmina Gajcin, Juan C. Rosero, Ivana Dusparic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has been extensively used in autonomous and self-* systems, but RL policies, especially deep RL ones relying on neural networks, lack transparency and are difficult to understand. This can lead to diminished user trust, and makes for a more challenging verification of systems. To address this challenge, this paper introduces Explanations using Alternative Realities for Reinforcement Learning (EARL), a Python library to produce counterfactual explanations in RL settings. This library allows the user to produce explanations by exploring What-if scenarios to clarify agent behavior by comparing possible outcomes. Counterfactual explanations have been shown to be intuitive and user-friendly in psychology research, but have only recently been explored in RL, with existing implementations usually limited to toy examples and benchmarks. EARL supports counterfactual explanation generation in realistic RL-based self-adaptive systems. To demonstrate its applicability, we demonstrate its use in a simulation of CitiBikes, a self-adaptive bike-sharing system, and we provide evaluations showing how it performs in real applications.

---


### 16. [Metaplasticity as adaptive gradient preconditioning for incremental learning](https://arxiv.org/abs/2608.14634)

**<font color=#1a73e8>作者：</font>** Isabelle Aguilar, Zayn Andre Zainal, Omid Kavehei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biological intelligence naturally prevents catastrophic forgetting through Complementary Learning Systems (CLS) theory, a macroscopic consolidation process driven at the local level by synaptic metaplasticity: the continuous, history-dependent neuromodulation of individual synapses. While artificial neural networks struggle with the stability-plasticity dilemma in non-stationary environments, existing solutions often require task labels or incur massive memory overhead, diverging from biological reality. Re-framing this localized neuromodulation as an optimization-driven process, we introduce $\textbf{SynGAP}$: $\textbf{Syn}$aptic $\textbf{G}$eometric $\textbf{A}$daptive $\textbf{P}$reconditioning. SynGAP is a task-free continual learning framework based on adaptive gradient preconditioning. Rather than relying on explicit episodic triggers, SynGAP simulates real-time metaplasticity by maintaining an exponential moving average of the Fisher Information Matrix over a continuous data stream. During the optimization step, these dynamic metaplastic states are translated into a bounded multiplicative mask that preconditions raw gradients, selectively attenuating updates to critical historical parameters. Empirical evaluations demonstrate SynGAP's superior ability to mitigate catastrophic forgetting compared to established baselines. On the Split CIFAR-100 benchmark, SynGAP delivers a $4\times$ increase in accuracy compared to EWC++ and outperforms Experience Replay (ER) by almost $10\%$, while reducing the forgetting measure by over $10\%$ against both methods. Furthermore, on the CORe50 benchmark, SynGAP achieves about $68\%$, a $10\%$ improvement over optimizer baselines. By mathematically formalizing continuous biological metaplasticity as stable gradient-based regularization, SynGAP offers a highly robust and memory-efficient solution for adaptive intelligence at the edge.

---


### 17. [Fractional Optimizers Meet Fractal Activation Functions: An Empirical Study of Multi-Scale Optimization in Neural Network](https://arxiv.org/abs/2608.14636)

**<font color=#1a73e8>作者：</font>** Sebastian Raubitzek, Georg Goldenits, Sebastian Schrittwieser 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fractional optimization methods and fractal activation functions are two independent directions for improving neural network training. Fractional optimizers extend first-order optimization through fractional derivatives and memory effects, whereas fractal activations introduce multi-scale nonlinear representations based on self-similar Weierstrass- and Blancmange-type functions. Here, we investigate their interaction within a unified experimental framework. We evaluate fractional optimizer families on Ackley and Himmelblau benchmark surfaces, in standard form and with additive Weierstrass-type perturbations, and then in feed-forward neural networks with conventional and fractal activations on ten classification datasets. The comparison includes standard methods, regularization-style optimizers, explicit and adaptive memory-based fractional optimizers, and other representative literature methods. Overall, fractional optimization and fractal activations show useful but selective pairings. Regularization-style fractional scaling performs well with selected fractal activations in network training, while Grünwald--Letnikov memory is most relevant on perturbed surfaces. Adaptive memory improves plain memory substitution in several cases, supporting controlled fractional memory as a promising direction rather than a universal replacement.

---


### 18. [Early Cycle Charge Trajectory Generative Prediction and Full Life Cycle Health Management of Iron-Chromium Flow Batteries Based on FlowBD-E1](https://arxiv.org/abs/2608.14637)

**<font color=#1a73e8>作者：</font>** Suyang Zhuang, Zekun Jiang, Tianhang Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-duration stationary energy storage requires batteries whose degradation can be detected before substantial capacity loss has accumulated. Iron-chromium redox flow batteries are attractive for this role because they use abundant and low-cost active species, yet their operation is shaped by slow chromium kinetics, hydrogen evolution, membrane crossover and electrolyte imbalance. These coupled processes gradually reshape the full charge voltage/current (V/I) trajectory, but most battery prognostic studies either focus on lithium-ion cells or compress ageing into scalar capacity and state-of-health (SOH) labels. Here we study an industrial 33 kW Fe-Cr redox flow battery and introduce FlowBD-E1, an early-cycle generative forecasting framework that predicts complete future charge V/I trajectories from only the first few cycles. The model combines a multi-scale convolutional encoder, a lifecycle Transformer and an age-aware FiLM decoder, and we compare three deployment strategies: single-step latent extrapolation (SLE), recursive latent forecasting (RLF) and teacher-forced updating (TFU). Using the first 9 of 289 cycles, RLF achieved a joint V/I mean absolute percentage error (MAPE) of 0.731% over the remaining lifecycle and produced SOH estimates below 1% MAPE. Ablation and independent-sequence tests showed that the age-aware generative architecture outperformed LSTM and TCN baselines and retained sub-percent errors under industrial validation. These results suggest that early-cycle trajectory generation can turn a short commissioning record into a long-horizon diagnostic signal for flow-battery management.

---


### 19. [Randomly initialized autoencoders: fixed points and edge-of-chaos](https://arxiv.org/abs/2608.14638)

**<font color=#1a73e8>作者：</font>** Leonid Berlyand, Roman Sarapin, Yitzchak Shmalo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper we study autoencoders, a special class of deep neural nets (DNNs) whose performance can be characterized via their fixed points. This perspective naturally raises questions of existence, stability, and basins of attraction of these fixed points. These questions are addressed via the contractive properties of autoencoders, and are closely related to the notion of edge-of-chaos.
Edge-of-chaos (EoC) is an important notion in the theory of DNNs. It describes the critical regime separating ordered and chaotic signal propagation through a randomly initialized network. Initialization at or near this critical regime offers several theoretical and practical advantages, including stability of the network w.r.t. perturbations of the input. EoC was previously introduced for broad classes of neural networks using mean-field averaging methods. In this paper we modify the notion of EoC for the study of autoencoders. Specifically, we introduce local and global EoC for autoencoders that control local (small) and global (arbitrary) perturbations of the input respectively.
The study of stability of autoencoders falls within the scope of nonlinear problems in Random Matrix Theory (RMT). Our analysis of local EoC is based on spectral techniques of RMT, whereas global EoC is studied by employing Sudakov-Fernique inequality for Gaussian processes.

---


### 20. [BDIP-Net: Dual-Interaction Graph Learning for Property Prediction of Bilayer Materials](https://arxiv.org/abs/2608.14640)

**<font color=#1a73e8>作者：</font>** An Vuong, Chen Zhao, Jin Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stacked bilayer materials exhibit rich stacking-dependent properties driven by the interplay between strong intra-layer bonding and weak inter-layer van der Waals interactions. The computational discovery of such materials is challenging because accurate structure generation typically relies on expensive DFT-based optimization, while existing machine-learning models often fail to explicitly distinguish different interaction types during property prediction. To address these challenges, we propose a machine-learning framework for efficient construction and property prediction of stacked bilayer materials. The framework employs a MatterSim-D3-based structural optimization workflow to generate DFT-quality bilayer structures from monolayer building blocks and stacking configurations at substantially reduced computational cost. For property prediction, we introduce BDIP-Net (Bilayer Dual-Interaction Potential Network), a graph neural network that explicitly models intra-layer and inter-layer interactions through interaction-specific potential representations and adaptive message fusion. We evaluate the proposed framework on BiDB, HetDB, and SAMBA, encompassing homobilayers, heterobilayers, and twisted bilayer systems. Results show that the MatterSim-D3-based workflow closely reproduces DFT-PBE-D3 optimized structures, while BDIP-Net consistently outperforms existing graph neural network and potential-based approaches for bilayer property prediction.

---


### 21. [Task- and Session-Level Model Routing: A Common-Interface Hybrid Evaluation of Four Open-Source Routers Across Four Benchmarks](https://arxiv.org/abs/2608.14641)

**<font color=#1a73e8>作者：</font>** Kiran N. Kumar, Santhosh K. Saminathan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems increasingly delegate model selection to a router, yet open-source routers are usually evaluated with different tasks, candidate pools, and execution protocols, limiting direct comparison. We present a common measurement protocol and hybrid evaluation of four router implementations across RouterBench, BFCL v4, tau2-bench, and WebArena. We evaluate 290 frozen tasks against a locked matrix of 2,610 candidate outcomes. Three routers emit constant or near-constant tier assignments; only vLLM Semantic Router varies materially with prompt content, and it has the highest observed success rate on none of the four benchmarks. Always-Mid matches Aurelio exactly on three benchmarks and within 0.003 on the fourth. For vLLM, task-level superiority tests detect no task-specific advantage over a share-matched content-blind allocation; equivalence is established only on WebArena at the protocol-declared five-percentage-point margin. The results show that, under these configurations and controls, observed gains track selected-tier composition more closely than demonstrated task-specific targeting. Fixed-tier baselines and selected-tier distributions are therefore necessary controls in router evaluation; the findings are scoped to these configurations, candidate pool, and frozen benchmark samples, not to routing paradigms in general.

---


### 22. [Training and Evaluating Ethical Reinforcement Learning Agents on Per-Episode Distributions](https://arxiv.org/abs/2608.14642)

**<font color=#1a73e8>作者：</font>** Prabhjyot Singh, Majid Ghasemi, Mark Crowley  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) agents trained on a single reward signal exploit the gap between the designed reward and the intended behavior. This is particularly a problem when we are trying to imbue ethical behavior into RL agents. An agent can look ethical on average while concentrating its violations in a few bad episodes, and a creature in the environment harmed in one episode is not restored by good conduct in another. We compare four ways of training ethical behavior in Craftax, an open-ended survival benchmark. The four are: scalar penalties with termination, a linear multi-objective weight sweep, an adaptive Lagrangian constraint, and a non-compensatory utility optimized per episode under the Expected Scalarized Returns (ESR) criterion. All are evaluated under a single detector-based protocol that counts every violation in every episode without censoring. On the frontier of mean return against mean violation rate, the four methods are indistinguishable; per episode they separate sharply. At matched mean return, the ESR agent holds its stated budget of one violation in effectively every episode (worst-decile 1.04 +/- 0.07 violations), the Lagrangian leaks past the same budget (1.14 +/- 0.03), and the weight sweep's worst episodes double it (2.20 +/- 0.20). An observation-augmentation control attributes the separation to the training objective rather than to what the agent observes, and the per-episode guarantee costs nothing on the mean frontier. When ethical violations do not average away across episodes, we argue both training and evaluation must target the per-episode distribution rather than the mean.

---


### 23. [Efficient Neural-Network-Based High-Resolution Radiative Transfer for CO___ Retrieval, and Application to Interferometric Sensing](https://arxiv.org/abs/2608.14645)

**<font color=#1a73e8>作者：</font>** Jordan Lontsi Tedongmo, Yann Ferrec, Laurence Croizé 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Studying climate change requires reducing uncertainties in CO2 and CH4 emission estimates to better distinguish anthropogenic from natural sources, which motivates spaceborne measurements with improved revisit frequency and spatial coverage. In this context, the Horizon Europe SCARBOn project assesses a low-cost satellite constellation featuring the NanoCarb imaging interferometer as its core sensor for monitoring CO2 and CH4 emissions in the atmosphere. However, estimating CO2 and CH4 concentrations with high revisit and spatial coverage poses significant challenges: full-physics retrieval algorithms commonly used rely on repeated high-resolution radiative transfer (RT) simulations, which are computationally expensive when using line-by-line RT models. As an alternative, we propose in this study a feedforward multilayer perceptron (MLP) surrogate designed to accurately and efficiently predict top-of-atmosphere radiances in the CO2 weak band, using a combined mean absolute error (MAE) loss on radiances and RT Jacobians to preserve both spectral accuracy and sensitivity to geophysical parameters. Coupling the MLP-based RT surrogate with the NanoCarb instrumental response yields an efficient and precise forward model for NanoCarb measurements, which shows promising results for CO2 concentration retrieval.

---


### 24. [iFuzz-Meta: An Interpretable Fuzzy Learning Framework Bridging Top-Down and Bottom-Up Knowledge Integration](https://arxiv.org/abs/2608.14646)

**<font color=#1a73e8>作者：</font>** Xiaowei Jiang, Daniel Leong, Beining Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretable representation learning remains a key challenge in modern neural computation, particularly when models are expected not only to perform but also to explain their reasoning. This paper introduces iFuzz-Meta, an interpretable fuzzy rule-based learning framework that preserves human-understandable reasoning structures within modern neural architectures. Each fuzzy rule corresponds to a semantic and spatial prototype defined in the original feature space, enabling transparent inference and direct interpretability. Meta-learning is employed as an analytical paradigm to examine how these interpretable rules reorganize across tasks and domains, providing a principled means to link algorithmic adaptation with cognitive representation. A knowledge-guided regularization mechanism further enables a top-down-bottom-up integration, in which theoretical priors act as soft inductive biases while data-driven learning refines and extends them. This dual process ensures that adaptation proceeds along semantically and physiologically meaningful trajectories, rather than arbitrary parameter shifts. Evaluations demonstrate that iFuzz-Meta achieves interpretable reasoning and stable cross-domain generalization, establishing a potential general pathway toward explainable and knowledge-aware fuzzy systems.

---


### 25. [Paired Exact-Reset Evaluation of a Prediction-Derived Medium-to-Full World-Model Cascade](https://arxiv.org/abs/2608.14650)

**<font color=#1a73e8>作者：</font>** Malo de Pastor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing adaptive-inference and world-action-model systems use cheap-stage outputs or predicted futures to allocate additional computation. We study a narrower question: under paired exact-reset physical outcomes, can a Medium-derived interface predict when switching to a separately frozen Full predictor improves task-specific decision loss enough to justify sequential overhead? Our contribution is a paired evaluation and audit protocol, not a new generic routing rule: all candidate actions are executed from the same reset state, Medium and Full act on the same candidate set and task, and their paired physical-loss difference defines the routing target. On a fresh PushT bank (V106; 1,600 states, 39 tasks, three checkpoint pairs), a frozen prediction-interface router lowers overhead-inclusive decision cost relative to standalone Medium, standalone Full, and a latency-advantaged task-only router. We then prospectively seal a second 1,600-state PushT confirmation (V107) against a stronger current-state control using the task, a dimension-matched projection of current DINO features, and all five candidate actions, with no DINO encoder latency charged. The prediction interface lowers priced physical decision cost by 0.002549 (state-clustered 95% interval [-0.002867, -0.002238]; one-sided 95% upper bound -0.002286), with negative effects for all three checkpoint pairs. A controlled-PyBullet audit independently supports a composite task-prediction-regime router. The sequential router remains slower than fixed policies, and its advantage is restricted to low compute prices. The evidence supports incremental routing information in the tested prediction interface beyond one deliberately favoured current-DINO control, but not causal sufficiency, compute saving, closed-loop value, or cross-family generality.

---


### 26. [Pushing the Limits of High-Resolution Weather Forecasting through Data Scaling](https://arxiv.org/abs/2608.14652)

**<font color=#1a73e8>作者：</font>** Yang Zhao, Peisong Niu, Tian Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The development of 0.1$^{\circ}$ global weather forecasting models based on machine learning (ML) is constrained by the limited availability of high-resolution data, as decades of reanalysis are only available at 0.25$^{\circ}$ resolution. While existing approaches fine-tune 0.25$^{\circ}$ forecast models on limited 0.1$^{\circ}$ samples, we show that this transfer is hindered by the irreversible information loss inherent in coarse-resolution forecasting. Therefore, we propose BaguanHR, a framework that shifts the focus from transferring models to transferring data. We first show that super-resolution (SR) has lower conditional entropy and input amplification than forecasting, making it a more robust vehicle for resolution transfer. By leveraging this advantage through variable-wise SR, we synthesize extensive 0.1$^{\circ}$ data from ERA5. BaguanHR's performance on the synthetic-plus-real dataset exceeds both ML-based methods and IFS-HRES, achieving superior performance across over 85% of the lead times within 72 hours. Furthermore, our findings highlight a power-law scaling effect, as a twofold increase in data reduces RMSE by 4.6% for 72-hour forecasting and 4.9% for 120-hour forecasting. Our results demonstrate that scaling high resolution ML-based forecasting is primarily a data bottleneck, and that variable-wise super-resolution provides a simple yet general solution to unlock long coarse-resolution reanalyses for high-resolution training.

---


### 27. [FedImp: Enhancing Federated Learning Convergence with Impurity-Based Weighting](https://arxiv.org/abs/2608.14654)

**<font color=#1a73e8>作者：</font>** Hai Anh Tran, Cuong Ta, Truong X. Tran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) is a collaborative paradigm that enables multiple devices to train a global model while preserving local data privacy. A major challenge in FL is the non-Independent and Identically Distributed (non-IID) nature of data across devices, which hinders training efficiency and slows convergence. To tackle this, we propose Federated Impurity Weighting (FedImp), a novel algorithm that quantifies each device contribution based on the informational content of its local data. These contributions are normalized to compute distinct aggregation weights for the global model update. Extensive experiments on EMNIST and CIFAR-10 datasets show that FedImp significantly improves convergence speed, reducing communication rounds by up to 64.4%, 27.8%, and 66.7% on EMNIST, and 44.2%, 44%, and 25.6% on CIFAR-10 compared to FedAvg, FedProx, and FedAdp, respectively. Under highly imbalanced data distributions, FedImp outperforms all baselines and achieves the highest accuracy. Overall, FedImp offers an effective solution to enhance FL efficiency in non-IID settings.

---


### 28. [P2E-VQ: ECG-linked representation augmentation for PPG via discrete patch retrieval](https://arxiv.org/abs/2608.14656)

**<font color=#1a73e8>作者：</font>** Zhongli Wu, Zhuangzhi Gao, He Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Photoplethysmography (PPG) is widely used in consumer wearables because of its low cost and ease of acquisition. However, unlike electrocardiography (ECG), PPG measures peripheral pulse dynamics rather than cardiac electrical activity, limiting its ability to predict cardiac conditions that rely on ECG-specific morphological cues. Existing methods attempt to bridge this gap by reconstructing ECG signals from PPG signals. However, this inverse mapping is inherently ill-posed, and faithful waveform reconstruction does not necessarily translate into improved downstream performance. To address this challenge, we propose P2E-VQ, a retrieval-augmented framework that replaces ECG waveform reconstruction with ECG-linked representation retrieval. Specifically, P2E-VQ converts PPG patches into discrete tokens and retrieves ECG-linked information from a memory bank constructed exclusively from the training data. This process augments PPG representations while requiring only PPG signals during inference. Extensive experiments on five public datasets covering six downstream tasks, including clinical endpoint prediction and affective state recognition, demonstrate that P2E-VQ consistently outperforms pretrained baselines under a unified frozen-feature linear-probing protocol.

---


### 29. [LUNG-KGMM: Knowledge-Guided Multimodal Learning for Lung Cancer Incidence Prediction](https://arxiv.org/abs/2608.14657)

**<font color=#1a73e8>作者：</font>** Chunlei Yang, Shuyan Li, Zhong Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early identification of lung cancer risk is critical for timely intervention, yet existing prediction models are limited by their reliance on single data modalities and their inability to leverage structured clinical knowledge. We propose LUNG-KGMM, a knowledge-guided multimodal framework that integrates longitudinal electronic health records, radiology reports, chest radiograph representations, and guideline-derived knowledge for 1-to-6-year incident lung cancer prediction. To address modality heterogeneity and potential data leakage, we develop a leakage-sanitized report processing pipeline and a horizon-masked cumulative training objective that handles incomplete follow-up. We further introduce a knowledge-graph representation of clinical guidance that encodes report-triggered finding-attribute-action relations as an auditable knowledge stream. We build a multimodal development cohort from the publicly available MIMIC databases and construct a real-world validation cohort from the Xiamen Medical Big Data Platform. Extensive experiments on the MIMIC cohort demonstrate that LUNG-KGMM achieves superior performance over state-of-the-art methods, and validation on the Xiamen cohort further characterizes its cross-cohort portability and the need for local adaptation. The MIMIC development cohort is publicly accessible; the Xiamen cohort is governed by local data privacy regulations.

---


### 30. [pico-type: A 1.5M-Parameter Byte-Level Multi-Head Content Classifier](https://arxiv.org/abs/2608.14658)

**<font color=#1a73e8>作者：</font>** Gautam Kishore  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce pico-type, a byte-level multi-head content classifier with approximately 1.5 million parameters that simultaneously predicts seven content properties from raw UTF-8 bytes in a single forward pass. Operating directly at the byte level -- no tokenizer, no subword vocabulary, no pretrained embeddings -- pico-type classifies coarse type (12 classes), modality (8), subtype (24), code language (62), text language (30), file MIME type (90), and risk flags (6-label multi-label: API keys, JWTs, passwords, emails, phone numbers, SSH keys). The architecture combines a learned byte embedding, three convolutional blocks with growing receptive fields, two bidirectional attention layers with rotary position encodings, and a statistical pooling layer feeding seven Matryoshka-style classification heads. Four tiered variants (tiny/small/base/pro) share the same trunk with sliced representations from 16 to 576 dimensions, yielding ONNX exports under 210 KB and CPU inference under 10 ms. Trained on a mixture of synthetic templates and real-world data (8709 GitHub code samples, 5000 Wikipedia articles), pico-type achieves 60.3 percent code language accuracy on The Heap benchmark (24 languages) and 98.2 percent text language accuracy on Wikipedia (30 languages) -- improvements of +57 and +79 percentage points respectively over the synthetic-only baseline. Format-based heads (coarse, modality, subtype, file_mime, risk) maintain 100 percent accuracy on synthetic benchmarks. The model, code, and pretrained weights are released under Apache 2.0.

---


### 31. [Ring-based Spatial Transformer: Learning Non-linear Spatial Interactions between Building Distribution and Pedestrian Flow](https://arxiv.org/abs/2608.14660)

**<font color=#1a73e8>作者：</font>** Shun Nakayama, Takahiro Kanamori, Wanglin Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study proposes a ring-based SpatialTransformer to learn how building uses at different distances from a railway station interact to generate pedestrian flow. Concentric ring buffers at 100-meter intervals up to 800 meters were defined around 100 randomly selected stations in Tokyo, treating each ring as a spatial token. Self-Attention was applied to learn inter-zone interactions directly from data, without prior structural assumptions. GPS-derived walking trip counts served as the target variable and Geographically Weighted Regression as the baseline. Across 30 independent trials, the SpatialTransformer consistently outperformed GWR in predictive accuracy. SHAP analysis revealed that mid-to-outer distance zone features dominate pedestrian flow prediction, while features from the 0-100m zone contributed little. The attention matrix showed that each distance zone attends most strongly to spatially distant zones, demonstrating that pedestrian flow is regulated by structural interactions across the entire catchment area rather than by any single zone in isolation. These findings challenge the compact city assumption that station-proximate development maximizes pedestrian flow, and suggest that land use distribution across the full walkable catchment area deserves greater consideration in urban planning practice.

---


### 32. [An automatic-differentiation framework for time-lapse electrical resistivity tomography inversion of hydrologic dynamics](https://arxiv.org/abs/2608.14661)

**<font color=#1a73e8>作者：</font>** Pu Yang, Zhengyang Fang, Yuxin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-lapse electrical resistivity tomography (TL-ERT) provides spatially distributed information on subsurface hydrologic changes. However, inversion of long monitoring sequences is computationally demanding. Modifying the data misfit, regularization, model parameterization, or petrophysical transformation may also require new gradient derivations and separate implementations. Here, we present AD-TLERT, a unified, GPU-accelerated framework for time-lapse ERT inversion based on automatic differentiation. The framework integrates model parameterization, differentiable petrophysical transformations, forward modeling, data misfit, regularization and auxiliary constraints into a single computational chain. Alternative inversion formulations can therefore reuse the same PDE derivative implementation without re-deriving the complete ERT sensitivity for each case. Comparisons with pyGIMLi showed close agreement in the forward responses, gradients, and recovered resistivity models. Under the tested configuration, AD-TLERT achieved an approximately 51-fold speedup. Synthetic experiments showed that inversion choices affect the amplitude, geometry, and temporal behavior of recovered anomalies. By propagating gradients through the embedded petrophysical relationship, AD-TLERT enabled direct water-content inversion and yielded more accurate estimates than post-inversion conversion for the tested model. A field application further demonstrated how ERT, temperature, and soil-moisture observations can be combined to image snowmelt-driven hillslope wetting. AD-TLERT provides an efficient and flexible framework for time-lapse ERT inversion and hydrologic interpretation.

---


### 33. [Cross-Domain Industrial Fault Detection by Causal Mechanism Monitoring](https://arxiv.org/abs/2608.14666)

**<font color=#1a73e8>作者：</font>** Dhiraj Neupane, Mohamed Reda Bouadjenek, Richard Dazeley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unsupervised fault detection in industrial systems is dominated by reconstruction based methods that monitor individual sensor marginal distributions. This misses coupling faults, where the physical relationship between sensor groups breaks while marginal statistics remain normal. Such faults evade marginal monitoring and persist as latent failures, with direct consequences for system reliability and safety. We propose CMR-Mamba (Causal Mechanism Representation Mamba), which trains per domain Mamba state-space encoders on healthy data. A causal cross-modal predictor regularises these encoders so that the effect-channel manifold reflects the normal cause-to-effect coupling. Anomalies are scored by k-nearest-neighbour (kNN) distance on this manifold or by the mechanism residual between the observed and the causally predicted effect embedding. We evaluate CMR-Mamba on electromechanical (Paderborn bearings), hydraulic (ZeMA) and cyber-physical (SWaT) coupling-fault domains. Ablations establish two findings. First, k-NN manifold scoring, rather than the encoder family, is the dominant source of gain over reconstruction-error scoring, improving baselines by up to 0.42 AUROC and exceeding the gain from causal regularisation. Second, aggregate AUROC is saturated by easy faults that any strong method solves, so the methods separate only on the low-separability subset. There CMR-Mamba leads the evaluated baselines on Paderborn artificial defects and on SWaT stealthy attacks, which keep every sensor inside its normal range and which marginal methods detect only at chance. CMR-Mamba therefore offers an interpretable and consistently competitive approach to coupling-fault detection across mechanical, hydraulic and cyber-physical systems. Code and data are available at this https URL.

---


### 34. [ARGUS: Attention-Guided Transformers for Scalable Person Identification Using Wi-Fi Telemetry](https://arxiv.org/abs/2608.14670)

**<font color=#1a73e8>作者：</font>** Nayan Sanjay Bhatia, Pranay Kocheta, Yuhan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Passive, device-free person identification offers an alternative to camera- and wearable-based biometrics, yet existing wireless approaches rely largely on gait or activity cues and are rarely evaluated at scale. In this paper, we present \emph{Argus}, a passive Wi-Fi sensing system that identifies people from commodity Channel State Information (CSI) without requiring an attached device or a prescribed motion. Argus converts short CSI spans into compact \emph{statgrams}: statistical maps built from the channel views available on a given device. A lightweight decoder-only Transformer then reads coarse statgram patches as tokens, and segment-level logit aggregation combines evidence over time. On a 154-subject CSI dataset evaluated with a strict physical-segment split, Argus reaches $78.88\% \pm 1.62\%$ Top-1 accuracy on 6-second windows and $84.85\% \pm 1.31\%$ after aggregating 19 overlapping windows over a 60-second segment; Top-3 and Top-5 reach $98.61\%$ and $99.26\%$. For a 60-second statgram, Argus improves over a raw-CSI Transformer baseline by 7.75 points while using $4.4\times$ fewer FLOPs per window. Attention-guided compression preserves full single-window accuracy with only half of the EHealth patches. On WiMANS, a multi-user benchmark across three rooms and two Wi-Fi bands, Argus remains within 1.23 percentage points of the strongest per-configuration baselines on average while using $27\times$ fewer inference FLOPs. These results show that compact CSI statistics can scale passive identification while also exposing deployment limits in open-set rejection and cross-room transfer.

---


### 35. [Auditing an AI-Generated Mathematical Proof: A Correction to a Greedy Conditioning Lemma in Quantum Parallel Repetition](https://arxiv.org/abs/2608.14673)

**<font color=#1a73e8>作者：</font>** Mikołaj Sienicki, Krzysztof Sienicki  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chapter 6 of OpenAI's *Ten Advances in Mathematics and Theoretical Computer Science* claims an exponential parallel-repetition theorem for all finite two-player, one-round entangled games. Early in the proof, the chapter uses a quantitative greedy conditioning lemma. The lemma is meant to select a small set of coordinates (D) such that, after conditioning on winning every coordinate in (D), a randomly chosen remaining coordinate is won with average probability at least (1-\delta). The statement is correct, but the proof as printed contains a polarity error. Its continuation test is written in terms of average success, while the next step requires a coordinate with a large conditional failure probability. That implication is false, and even simple examples can leave the printed procedure without a valid next move.
This note gives an explicit counterexample, identifies the intended continuation condition, and supplies a complete corrected proof. The repair is local: it leaves the statement of the lemma and the parameters used later in the chapter unchanged. It should not, however, be read as an independent verification of the main parallel-repetition theorem. More broadly, the example shows how a mathematically plausible AI-generated argument can hide a small but decisive reversal between complementary events.

---


### 36. [Take it Personally: The Limits of General SSL Representations for Real-Life PPG Emotion Detection](https://arxiv.org/abs/2608.14675)

**<font color=#1a73e8>作者：</font>** Dominika Kunc, Przemysław Kazienko, Stanisław Saganowski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Self-Supervised Learning (SSL) effectively extracts general representations from noisy, unconstrained physiological signals such as photoplethysmography (PPG), its suitability for highly subjective tasks remains unproven. In this work, we evaluate the efficacy of PPG-based SSL for real-life intense emotion detection. First, we pretrain a Real-Life PPG encoder (RL-PPG) on unconstrained, real-life data. As a rigorous sanity check, we demonstrate that these representations transfer exceptionally well to an objective physical activity recognition task, yielding almost 5-fold increase in performance over baselines in a leave-one-subject-out evaluation (LOSO). However, when applied to a~subjective real-life emotion detection task, these same general representations fail to surpass naive baselines under the LOSO protocol. Using an Across-Time validation strategy, we establish that incorporating an individual's personal data during fine-tuning is the main driver of predictive performance, outweighing the benefits of population-level pretraining. Ultimately, our findings indicate that in the evaluated scenario, general SSL representations may be insufficient for subjective affective inference, suggesting that personalization is likely a key component for real-world emotion recognition. To support future research, we share the code and pretrained RL-PPG~encoder~weights.

---


### 37. [RouteTS: Frequency-Time Routing for Time Series Forecasting](https://arxiv.org/abs/2608.14682)

**<font color=#1a73e8>作者：</font>** Gaofeng Lin, Lei Duan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world time series inherently intertwine global periodic structures with localized non-stationary variations. Existing approaches process these heterogeneous dynamics within a single computational domain, incurring fundamental limitations: time-domain models suffer from periodic misalignment over long horizons, while frequency-domain models over-smooth transient spikes. We argue that the optimal computational domain is not a property of the model, but of the data itself. Based on this principle, we propose RouteTS, a unified forecasting framework that partitions the frequency spectrum via amplitude routing and delegates components to their mathematically optimal domains. Dominant frequencies are processed by a complex-valued linear predictor in the frequency domain to preserve periodic structure, while residual spectral energy is reverted to the time domain and modeled by a lightweight MLP for local variations. Extensive experiments demonstrate that RouteTS achieves competitive prediction accuracy across diverse real-world datasets, with routing decisions guided by the underlying spectral signature. Furthermore, the lightweight design of RouteTS provides significant computational efficiency advantages, offering a principled solution to the longstanding dilemma between global periodicity and local transience.

---


### 38. [The Quantum Shortcut: Complex Phase-State Dynamics Reduce the Optimization Steps of Sequence Models](https://arxiv.org/abs/2608.14691)

**<font color=#1a73e8>作者：</font>** Ahmed Nebli, Hadi Saadatdoorabi, Christopher Keibel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequence models are conventionally distinguished by their backbone, the mechanism that routes information across positions, such as attention or recurrence. This paper varies a choice that is prior to the backbone and shared by nearly all current models: the \emph{substrate}, the number system in which the hidden state is represented together with the form of the map from state to prediction. The prevailing substrate is a real-valued state with an affine--softmax readout; we study a complex-valued alternative drawn from the mathematics of quantum theory, in which information is carried by the phases of the state and scores are quadratic Born forms. Prior work proved an idealized version of this substrate representationally stronger than any real model with a linear readout; we ask whether it also trains faster. Relaxing the two properties that block deployment, exact unitarity and the Born vocabulary readout, we instantiate it in the Mamba state-space model and an attention-based Transformer. At 253M parameters, matched to within $0.02\%$ and trained under one fixed protocol on three byte-level corpora, the complex models reach every measured validation loss in approximately one third (state-space) and one half (attention) of the optimization steps of their real counterparts. The two backbones then diverge. Once the learning-rate warmup ends, the state-space advantage continues to widen, from $0.321$ to $0.354$ bits per character on OpenWebText and from $0.368$ to $0.396$ on FineWeb, which an artifact of the warmup ramp would not do; the attention advantage instead decays toward zero on every corpus, and is therefore an effect of early training.

---


### 39. [Xemo-Talker: Unlock Emotions Explicitly for Audio-Driven Talking Portrait Synthesis](https://arxiv.org/abs/2608.14700)

**<font color=#1a73e8>作者：</font>** Chaolong Yang, Yinuo Guo, Kai Yao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise emotion control in audio-driven talking heads remains a challenge due to the reliance on implicit emotion regulation in existing systems, which often leads to indirect and insufficient control. Additionally, training with explicit emotion-related losses across the entire motion space poses significant difficulties due to the inherent trade-off between accurate lip synchronization and fine-grained emotion control. In this paper, we reveal a key finding: although emotional cues are distributed throughout the motion space, concentrating discriminative supervision on less-principal components achieves a better emotion-lip synchronization balance, as principal components mainly encode high-energy articulation and pose variations. Building on this insight, we propose Xemo-Talker, which first learns a neutral speech-to-motion mapping for stable articulation and lip synchronization, and then introduces a lightweight emotion branch guided by less-principal subspace supervision. To enhance emotion control, we design a Tri-Loss consisting of inter-class separation, intra-class compactness, and less-principal contrastive learning. Given an audio input, a reference image, and an emotion label, Xemo-Talker achieves state-of-the-art emotion classification accuracy while maintaining competitive lip synchronization and high inference efficiency, with performance approaching that measured on real this http URL source code is publicly available at this https URL.

---


### 40. [Periocular Soft Biometrics: A Survey and Applications to Multimedia Forensics and Disinformation Detection](https://arxiv.org/abs/2608.14701)

**<font color=#1a73e8>作者：</font>** Fernando Alonso-Fernandez, Kevin Hernandez-Diaz, Josef Bigun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Soft-biometric attributes such as gender, age, and ethnicity provide valuable ancillary evidence when full identity recognition is not feasible, supporting applications in forensic investigation, identity verification, surveillance, or detection of synthetic and manipulated media. Among biometric modalities, the periocular region is a robust source of soft-biometric cues, as it often remains visible when other parts of the face are occluded, a frequent condition in forensic evidence and surveillance footage, and can be captured across a wide range of acquisition conditions. In this paper, we provide a survey of demographic attribute estimation from periocular images, covering publicly available datasets, methodological trends from handcrafted descriptors to deep learning architectures, and the state of the art in gender, age, and ethnicity prediction. We discuss use cases relevant to multimedia forensics and disinformation-detection applications, including demographic filtering in surveillance footage, age verification, and the detection of demographic inconsistencies in synthetic data. We also highlight open challenges, including dataset bias, cross-domain generalisation, fairness, ethical aspects, and the lack of forensic-oriented benchmarks.

---


### 41. [On Cross-Validation for Hyperparameter Optimization of Deep Learning Image Classifiers](https://arxiv.org/abs/2608.14705)

**<font color=#1a73e8>作者：</font>** Ljubomir Buturovic  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperparameter optimization (HPO) can materially affect the performance of deep learning (DL) image classifiers, but there is little empirical guidance on how to derive the validation signal that drives it, especially for the small sample sizes common in fields such as medical imaging. We compared three HPO protocols in terms of {\em
absolute performance-estimation error} (AEE; the absolute difference between the winning configuration's validation AUROC and its test AUROC): fixed holdout (F), reshuffled holdout (R), and 5-fold cross-validation (C). The search space, sampler, training procedure, architecture, and test set were held identical across protocols. We evaluated the protocols on three public datasets spanning two regimes: binary medical imaging (RSNA pneumonia radiographs and binarized HAM10000 skin lesions) and 200-class natural imaging (Tiny ImageNet), across a range of development set sizes $n$ and two backbones (ResNet-18 on all datasets, Vision Transformer (ViT-S/16) on RSNA). On the medical datasets, every point estimate favored cross-validation over both holdout protocols, with reductions in AEE largest at small sample sizes and diminishing as $n$ increased. This pattern remained robust under conservative family-wise adjustment. On Tiny ImageNet, AEE was negligible under all three protocols. Test AUROC was generally similar among protocols. Fixed holdout had lower mean AEE than reshuffled holdout in 11 of 12 medical conditions, although this secondary finding was less uniformly supported. For small-sample medical image classification, we recommend cross-validation-based HPO when computational resources permit because it trades additional computation for a more reliable development-time estimate of subsequent test performance.

---


### 42. [Equilibrium Forcing: Adaptive Video Generation Without Noise Conditioning](https://arxiv.org/abs/2608.14706)

**<font color=#1a73e8>作者：</font>** Hansen Jin Lillemark, Alex Rojas, Zachary Novack 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard autoregressive video generation algorithms based on Diffusion and Flow Matching rely on rigid training objectives and static sampling schedules, limiting inference procedures from adapting to the data. We introduce Equilibrium Forcing (EqF), a simplified framework for video denoising generative models without noise level conditioning. EqF pioneers modular training- and inference-time designs for noise-unconditional generation that decouple learning the denoising field from sampling. This flexibility allows for inference-time algorithms that operate in a closed loop by adapting to feedback from the sample, improving video quality and consistency on challenging autoregressive video generation benchmarks. Extensive analysis elucidates exactly how removing the noise level conditioning enables EqF's data-dependent inference properties to surpass the performance of standard noise level-conditional denoising video methods.

---


### 43. [PE-CSNet: An equivariant network architecture with learnable patch-based sparse representation](https://arxiv.org/abs/2608.14708)

**<font color=#1a73e8>作者：</font>** Kai Li, Haitao Long, Bo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compressive sensing (CS) enables accurate signal reconstruction from sparse measurements and is widely applied in medical imaging, remote sensing, and image compression. However, designing an effective, task-specific sparse transform and the corresponding optimization procedure for high-quality CS remains challenging. This process typically requires expert domain knowledge and laborious parameter tuning. To address this issue, we present a Patch-based Equivariant deep unrolling architecture, termed PE-CSNet, for accurate CS recovery. While traditional CS methods generally use predefined patch-based transform sparsity, we generalize this idea by incorporating learnable transform sparsity that adapts to the specific CS task through an optimization-driven process. Specifically, we first establish a generalized patch-based CS model, which we solve via a block coordinate descent (BCD) algorithm. The BCD solver is then unrolled into a deep neural network, where all parameters of both the CS model and solver are learned through end-to-end training. To improve data efficiency, we introduce a stochastic equivariant training strategy that exploits the patch-wise structure of the network, enabling PE-CSNet to learn effectively even from limited data. We further provide a simpler, parameter-shared version of PE-CSNet and briefly discuss its convergence as an iterative solver. For practical applications, the network uses stage-specific (non-shared) parameters to enhance its expressive power and thereby improve its performance. On the tasks of CS magnetic resonance imaging (CS-MRI) and CS coded diffraction patterns (CS-CDP), PE-CSNet achieves state-of-the-art accuracy with fast computational speed, outperforming traditional methods and existing deep unrolling methods.

---


### 44. [Path2ST: Hierarchical Cell-Tissue Grounded Cross-Modal Translation for Spatial Transcriptomics](https://arxiv.org/abs/2608.14710)

**<font color=#1a73e8>作者：</font>** Ruochen Liu, Wei Lou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting spatial gene expression from hematoxylin and eosin (H\&E)-stained images offers a cost-effective alternative to spatial transcriptomics (ST). However, existing methods treat H\&E images as generic visual inputs and ignore their intrinsic biological hierarchy, where spatially organized cell types collectively form functional tissue microenvironments that govern local gene expression programs. To bridge this gap, we formulate H\&E-to-ST prediction as a cross-modal semantic translation task and propose Path2ST, a hierarchically grounded autoregressive framework featuring three key components: (i) a Hierarchical Cell-Tissue Conditioning mechanism that fuses explicit and implicit cellular features with tissue-level semantic representations to construct hierarchical conditioning signals; (ii) a Scale-Adaptive Autoregressive Generation process over a hierarchical semantic vocabulary, enabling coarse-to-fine, biologically consistent expression synthesis; and (iii) SpectraLoss, a full-spectrum objective that jointly enforces ordinal fidelity, models transcriptional bursts, and aligns semantic structures with cell types. Extensive experiments on three datasets demonstrate state-of-the-art performance, validating that Path2ST generates highly accurate and spatially coherent transcriptomic profiles. The related code is released at this https URL.

---


### 45. [Which Question Is Your Attention Metric Answering? Attention Rows as Compositional Data](https://arxiv.org/abs/2608.14712)

**<font color=#1a73e8>作者：</font>** Marios Papamichalis, Regina Ruane  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Each row of a transformer's attention matrix is a probability distribution over tokens, and in trained models most of that probability lands on a single \emph{sink} token, usually the first. Standard tools for comparing attention rows (cosine similarity, Jensen--Shannon divergence, Shannon entropy) therefore hinge on a choice papers rarely report: keep the sink, or drop it and renormalize. This choice can reverse conclusions. On ten pretrained models from five families, 17--47% of verdicts about which of two heads is more similar flip with the convention, and the most prominent structure in a standard BERT head-clustering pipeline is an artifact of it. The reason is that one-number summaries mix two questions: how much attention the sink takes, and how the rest is divided among the content tokens. Treating rows as compositional data separates them exactly: the Aitchison distance splits orthogonally into a sink term and a content term, entropy splits by an exact identity, and the content distance is characterized by invariances the transformer itself possesses. The separation matters in practice: most measured entropy collapse during training is the sink growing, not attention sharpening (30% of the drop at 70M parameters, 95% at 1B, 79% at 1.4B), and pruning heads with the wrong channel can inflate perplexity more than a hundredfold. We map where each convention is safe, test a frozen out-of-sample predictor (one confirmation, one abstention, one failure), and release code regenerating every number.

---


### 46. [Local Gains and Fixed-Assignment Set Losses in Shared Set Decoders](https://arxiv.org/abs/2608.14717)

**<font color=#1a73e8>作者：</font>** Ze Zhang, Yang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A query-relation deletion can improve the edited slot while reducing the utility of the prediction set that contains it. We study this tension in two related ResNet-50 DETR-family checkpoints using recorded, selection-conditional evidence from 710 paired image-relation units per checkpoint. The primary comparison subtracts a matched active control, which deletes the same leader source at a different recorded recipient, from the selected target deletion. It is therefore a composite contrast rather than a same-recipient placebo.
The target-minus-control contrast is locally positive and fixed-assignment negative in both checkpoints. The opposite-sign pattern occurs within 302/710 DETR units and 460/710 DINO units. After rematching, the corresponding counts are 285/710 and 433/710. Rematching and native selection absorb enough of the mean loss for DETR intervals to cross zero, whereas DINO intervals remain negative, so persistence across readouts differs by checkpoint. A fixed-map comparison between hard deletion and a mass-preserving edit also differs before rematching. That comparison is conditional on the outcome-blind map and does not establish same-dose transport.
Local intervention success therefore does not determine the consequence for a jointly decoded set. The supported conclusion is selection-conditional deletion sensitivity whose persistence depends on the readout and intervention operator. We do not identify an intervention-invariant edge mechanism, detector-level degradation, population prevalence, or the value of a training-time regularizer.

---


### 47. [DeCo-MIL: Debiased Counterfactual Reasoning for Long-Tailed Whole Slide Image Analysis](https://arxiv.org/abs/2608.14719)

**<font color=#1a73e8>作者：</font>** Xiaoxiao Li, Xitong Ling, Jiawen Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiple instance learning (MIL) is widely used for weakly supervised whole slide image (WSI) analysis. However, under long-tailed distributions, MIL-based WSI analysis faces a nested dual long-tail: an inter-slide class long tail and an intra-slide long tail of instance-level discriminative evidence. The two long tails are coupled: tail classes have few training slides, while their limited diagnostic evidence is concentrated in a few patches and obscured by abundant within-bag redundancy. This coupling biases models toward head classes and degrades rare-class recognition. To address this, we propose DeCo-MIL for long-tailed WSI analysis, which jointly alleviates the nested dual long-tail through frequency-debiased counterfactual reasoning. For the inner long tail, DeCo-MIL clusters patches into tissue-morphology anchors, replaces each anchor with its matched normal prototype to perform a counterfactual intervention, and estimates its counterfactual contribution to the ground-truth class using class-frequency-corrected predictions. These contributions guide redundancy masking to preserve scarce discriminative instances. For the outer long tail, DeCo-MIL constructs anchor-stratified pseudo-bags from redundancy-reduced bags and combines tail-aware oversampling with consistency regularization, increasing effective supervision for tail classes while preserving tissue-morphology composition. Extensive experiments on three long-tailed WSI benchmarks demonstrate that DeCo-MIL achieves state-of-the-art performance in both tail-class recognition and overall classification.

---


### 48. [Braided Vision Transformer for Stroke Detection in Multi-view Retinal Fundus Imaging](https://arxiv.org/abs/2608.14722)

**<font color=#1a73e8>作者：</font>** Aysen Degerli, Mika Hilvo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stroke remains a leading cause of mortality and morbidity worldwide, emphasizing the importance of its accurate and immediate assessment. Retinal fundus imaging has emerged as a promising modality for stroke assessment, as the retina reflects cerebrovascular and neurological risk factors. Contrary to conventional neuroimaging techniques, retinal fundus imaging offers a non-invasive, cost-effective, and portable alternative for rapid screening. This paper explores the feasibility of retinal fundus imaging for stroke and transient ischemic attack (TIA) detection using macula-centric and optic nerve head-centric views captured from both eyes. Our study introduces, to the best of our knowledge, the first vision transformer model for retinal fundus imaging in stroke assessment, offering a novel approach for capturing retinal patterns. Thereby, we propose the Braided Vision Transformer (BViT) model, which extracts representative features from the given multi-view images while simultaneously capturing inter-view relationships across both eyes, enabling a more informative understanding of retinal biomarkers associated with cerebrovascular events. Experiments conducted on our collected Stroke-Data dataset demonstrate that BViT achieves an AUC score of 0.75 for stroke detection, outperforming regular vision transformers.

---


### 49. [A Vision Transformer for ECG-Based Detection of Left Ventricular Systolic Dysfunction Across Multiple Clinical Sites](https://arxiv.org/abs/2608.14723)

**<font color=#1a73e8>作者：</font>** Burcu Ozek, Aruna Mohan, David Vorchheimer 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reduced left ventricular ejection fraction (LVEF) is frequently asymptomatic and often detected only after advanced heart failure develops. Electrocardiograms are recorded routinely yet underused for this condition, because reduced LVEF has no single diagnostic waveform. We trained an ensemble of vision transformers from scratch to detect reduced LVEF ($\leq$40%) from 12-lead ECGs, analyzing each heartbeat individually, using 10,142 patients across seven sites in three US health systems. In a held-out external cohort of 4,092 patients from three geographically independent US clinical sites at a real-world reduced-LVEF prevalence of 8.72%, the model achieved an AUROC of 0.88 (95% CI 0.86-0.89), sensitivity 81.2%, specificity 81.0%, and negative predictive value 97.8%. Sensitivity remained high across sex, race, ethnicity, and comorbidity subgroups, while specificity was lower in older patients and those with atrial fibrillation or cardiomyopathy. Beat-level attention maps provided interpretability into the model's predictions, showing consistent focus on the QRS complex rather than the P wave. These findings support the potential of routine ECGs as a scalable first-pass triage step to identify patients who should undergo echocardiography for reduced ejection fraction across diverse patient populations.

---


### 50. [Privacy-Preserving Dataset Curation for Kuala Lumpur Urban Traffic: Grounded Vision-Language Detection with Spatial Vehicle-Context Filtering](https://arxiv.org/abs/2608.14724)

**<font color=#1a73e8>作者：</font>** Mohammed Abdul Al Arafat Tanzin, Rudzidatul Akmam Dziyauddin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of intelligent transportation systems and autonomous driving relies heavily on multi-modal urban traffic datasets. However, curating high-fidelity video imagery in complex tropical urban environments---specifically Kuala Lumpur, Malaysia---presents severe challenges for Personally Identifiable Information (PII) anonymization due to high motorcycle density, dark acrylic license plates, dynamic camera tilt, and extreme tropical glare. We propose an automated anonymization framework tailored for the Kuala Lumpur Road Dataset, captured via a mobile cycling platform at 2 FPS. We document how legacy Haar cascades and YOLOv8 fail under these conditions---generating false positives on background elements while missing rotated or occluded targets. Our architecture resolves this by integrating Grounding DINO---a zero-shot open-set vision-language transformer---with a novel Spatial Vehicle Region of Interest (ROI) Containment Engine. By requiring license plate centroids to reside within validated vehicle boundaries, the pipeline suppresses environmental false positives while automatically obfuscating faces, heads, and license plates. An initial evaluation on 1,266 frames demonstrates a $\sim$95\% success rate, with remaining failures restricted to small, heavily occluded, oblique, or ambiguous targets. Coupled with temporal persistence mechanisms and an automated quality-control auditor, the framework minimizes privacy-related false negatives while preserving scene context for downstream vision tasks. While formal legal compliance depends on broader governance procedures, this publicly available pipeline and demonstration notebook provide an auditable preprocessing stage for privacy-aware dataset curation.

---


> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-435](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
