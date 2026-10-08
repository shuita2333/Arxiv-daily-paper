# 📦 其他研究 | 2026年10月09日

> 本类共 **324** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-324](./part-07.md)

---

### 1. [A Bayesian Mirror Architecture for Emergent Consciousness: Circular Hierarchies, Self-Manifolds, and Hybrid Event-Self Binding](https://arxiv.org/abs/2610.08792)

**<font color=#1a73e8>作者：</font>** Eduardo Righi Capanema de Almeida  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a foundational formulation of the Bayesian Mirror Architecture (BMA), a self-referential generative framework in which sensory abstractions, meta-abstractions, and a self-latent interact through circular recursion. The defining constraint is a closed update S_t <- H_{t-1}, where a hybrid event-self latent H_t binds self-representations to abstract world models and reinjects this coupling into the self-state. Consciousness, in a restricted sense, is not an optimization objective nor a semantic label, but an architectural property of systems possessing this circular structure.
Because inference operates over posterior beliefs, BMA's intrinsic state space is a space of probability measures equipped with optimal-transport geometry. Stability and coherence are formulated in the 2-Wasserstein metric on P_2, yielding coordinate-free notions of self-stability and hybrid coherence along belief trajectories. We define a Causal Learning Regime (CLR) via bounds on Wasserstein belief drift together with an integration index capturing sustained coupling between self and world latents. CLR diagnoses whether the environment contains learnable causal structure; it is not a marker of consciousness.
Global strict contractivity is not required: BMA may exhibit multiple coherent basins. We define self-manifolds basin-wise as supports of invariant measures under local Wasserstein contractivity. We identify Wasserstein epsilon-necks, transport bottlenecks where basins decouple, yielding a unique realized continuation in a vanishing-conductance limit. We interpret this selection as choice: internally determined yet externally unpredictable at finite resolution. Learning proceeds via variational free-energy minimization, with stability and agency emerging from what the environment affords to learn.

---


### 2. [Accelerating Floating-Point Satisfiability Solving via Gradient Normalization](https://arxiv.org/abs/2610.08808)

**<font color=#1a73e8>作者：</font>** Yuanzhuo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Satisfiability Modulo Theories (SMT) solvers are foundational to software verification, program analysis, and compiler testing, particularly over the theory of Quantifier-Free Floating-Point (QF_FP). While recent optimization-based SMT solvers have successfully applied gradient descent to continuous relaxations of logical formulas, they are fundamentally bottlenecked by gradient domination, a phenomenon where a small subset of difficult clauses hijacks the optimization trajectory, preventing the solver from satisfying the broader formula and trapping it in local minima.
To overcome this, we present GradSAT, a novel framework that bridges optimization-based SMT solving with Multi-Task Learning (MTL). GradSAT reformulates the constraint satisfaction process by treating each SMT clause as an independent MTL task. By applying dynamic gradient normalization (GradNorm), GradSAT actively balances the gradient magnitudes across all clauses at runtime, systematically penalizing dominant gradients and accelerating lagging clauses to ensure uniform convergence. GradSAT implements this through a highly optimized, two-stage hybrid pipeline. First, a GPU-accelerated PyTorch backend leveraging symbolic compilation and operator fusion navigates the continuous relaxation to a high-quality basin. Second, the candidate assignment is handed off to a bit-precise local search engine to rapidly resolve the exact, rigorous assignment. By stabilizing the continuous search dynamics, GradSAT mitigates the brittleness of prior gradient-based solvers and provides a robust, highly parallelizable architecture for complex constraint solving.

---


### 3. [Beyond Baseline Severity: Temporal and Disease-Specific Predictors of Depression Outcomes Following Mindfulness Interventions](https://arxiv.org/abs/2610.08809)

**<font color=#1a73e8>作者：</font>** Muhammad Jawad Chowdhury, Sultanus Salehin, Akib Jayed Islam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Depression severity among patients with chronic or acute medical conditions is influenced by a complex interaction of baseline psychological state, demographic characteristics, clinical context, and engagement with behavioral interventions. This paper presents an interpretable machine-learning analysis of a multi-center longitudinal clinical cohort to predict Beck Depression Inventory-II (BDI-II) scores at 12 and 24 weeks following mindfulness-based intervention participation. The study uses demographic variables, clinical condition information, hospital-center identifiers, baseline BDI-II scores, and therapy engagement measures to model short-term and long-term depression outcomes. Missing follow-up outcomes were addressed using a model-based stochastic imputation procedure to preserve the modest sample size while maintaining outcome variability. Five regression models were evaluated, spanning regularized linear regression and tree-based ensemble methods. Ridge Regression achieved the best 12-week performance with an RMSE of 5.186 and R^2 of 0.474, while LightGBM achieved the best 24-week performance with an RMSE of 5.038 and R^2 of 0.525. Beyond prediction accuracy, the analysis reveals three clinically relevant patterns: baseline severity remains the strongest overall predictor, short-term outcomes are more strongly associated with clinical and hospital context, and long-term outcomes show greater dependence on behavioral adherence and demographic factors. Disease-specific and hierarchical subgroup analyses further indicate that predictors differ substantially across and within clinical categories. These findings support the use of interpretable, context-aware modeling to inform personalized mental-health support following mindfulness-based interventions.

---


### 4. [Bounded Autonomy and Verifiable Safety for Agentic AI Enabled Automation](https://arxiv.org/abs/2610.08815)

**<font color=#1a73e8>作者：</font>** Srini Ramaswamy, Deveeshree Nayak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic AI-enabled automation cannot be safely deployed in high-stakes environments on probabilistic reasoning alone. A recurring risk is epistemic drift: as reasoning deepens, system behavior may move away from subject-matter-expert constraints for safe operation. This paper presents BRaVeS, a bounded reasoning and safety-governance framework termed the Defensible Next-Gen Reasoning System (DNRS). BRaVeS encodes SME-defined constraints as invariant anchors, proposes MoDA-Style (Mixture of Depths Attention) depth-aware access as a candidate mechanism for keeping these anchors visible during inference, and uses a state hierarchy (SMARtAutonomy) to reduce autonomy as epistemic risk increases. To formalize bounded recovery, we introduce the Lyapunov-Bounded Consensus Framework (LBCF), which maps continuous epistemic-risk signals into a finite K-bag abstraction and applies shielded state transitions that enforce Lyapunov-style energy descent or route the system to a human-mediated terminal state. The formal convergence result applies to the finite LBCF abstraction under fixed thresholds and feasible-shield assumptions; it does not prove safety of the full continuous neural activation space. We evaluate the framework through a discrete event Monte Carlo simulation using HAI 22.04 industrial-control-system time-series data with synthetic noise and sensor-degradation regimes. Across the tested parameter-grouping strategies and thresholds, the LBCF process achieved finite-step convergence and no safety-guard violations. These results provide simulation-based evidence that bounded governance behavior can be enforced under the stated abstraction, while motivating future work on deployed transformer implementations, live human-in-the-loop validation, and broader adversarial settings.

---


### 5. [The Cost of Long Memory: State, Context, and Stability Complexity in Sequence Models](https://arxiv.org/abs/2610.08816)

**<font color=#1a73e8>作者：</font>** Yuheng Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-range temporal dependence poses a resource question for sequence models: for a specified predictive-memory law, how much state, context, or dynamical criticality is required in order to forecast accurately? We study this question directly in forecasting risk. For algebraically decaying predictive memory, we prove matching upper and lower approximation bounds for exponential and finite-state modes. The best $r$-mode forecast error decays as $e^{-\Theta(\sqrt r)}$, so reaching forecast error $\tau$ needs $r=\Theta(\log^2(1/\tau))$ states or modes. Earlier curse-of-memory results establish broad limitations of stable recurrent models under different approximation notions; here both sides match for one canonical predictive target in forecast risk, which fixes the optimal resource exponent for that target. We then show that genuine fractional long memory changes the geometry itself. In particular, forecast error is measured after fractional integration, prediction from a finite context of length $L$ has an exact $1/L$ leading order, and a fixed fractional strength $d$ keeps the square-log state-complexity law. Near the short-memory boundary, we identify the relevant $d^2$ and $d^4$ scales and give a uniform constructive law in the intermediate regime. For nonlinear contextual recurrences with uniformly contractive state dynamics, we derive an exponential first-chaos envelope and an explicit necessary condition that relates forecast accuracy to the contraction margin. Vanishing forecasting error on an algebraic target forces the recurrence quantitatively toward criticality, a condition that is necessary and not by itself sufficient. Finite-sample Kullback--Leibler calculations further connect the predictive geometry to statistical information. Theorem-matched experiments with contractive state-space, gated recurrent, and attention models reproduce the state and stability predictions.

---


### 6. [DenoFlow: Flow Matching for SSVEP Denoising under Real Physiological Artifacts](https://arxiv.org/abs/2610.08817)

**<font color=#1a73e8>作者：</font>** Zhentao He, Ziwei Wang, Dongrui Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG)-based brain-computer interfaces (BCIs), particularly steady-state visual evoked potential (SSVEP) systems, are highly vulnerable to noise and artifacts, which severely degrade decoding accuracy. Although recent denoising approaches have shown promise, they are fitted without paired ground truth, can settle on reproducing their input, and are optimized on waveform distance alone, which says nothing about whether the output stays decodable. To address these issues, we propose DenoFlow, which casts SSVEP denoising as transport: instead of learning a direct map from a contaminated trial to a clean one, a field network regresses the velocity of the straight path between them, following the rectified-flow formulation, and denoising integrates that field forward from the observation. The field network is an encoder-decoder that sees the contaminated trial at every layer and the path position at its bottleneck, and a classifier trained alongside it supervises the integrated output. Because the observation itself is both the conditioning input and the starting point of the integration, the model never generates a trial from noise, and training reduces to regression, removing the adversarial min-max game. To obtain paired data on datasets with no ground truth, we injected physiological artifacts of the recorded electromyography (EMG) and electrooculography (EOG) signals under a controlled signal-to-noise target. Experiments on two public SSVEP datasets with five popular SSVEP decoders showed that DenoFlow outperformed seven baseline denoising models on both signal fidelity and downstream decoding accuracy. Code is available at this https URL.

---


### 7. [HydroSphere: A Framework for Governed, Self-Healing Wastewater Infrastructure](https://arxiv.org/abs/2610.08819)

**<font color=#1a73e8>作者：</font>** Prabu, Fancy C, Suresh A 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rapid industrialization and urban growth are increasing pressure on water quality and wastewater treatment systems, while conventional treatment plants often rely on static monitoring and control strategies that cannot easily adapt to changing pollutant conditions. This paper presents HydroSphere, a governed, data-driven framework for real-time water quality monitoring, forecasting, treatment optimization, and fault recovery. HydroSphere is evaluated using 2.82 million water-quality measurements collected between 1940 and 2023. The framework integrates three main components. First, a hybrid TCN-LSTM model performs multi-step forecasting across seven water-quality parameters, achieving an RMSE of 0.1417, MAE of 0.1047, and R2 of 0.3596. Second, the Adaptive Dosage Optimization Module uses PPO reinforcement learning to adjust chemical dosing, achieving a mean step reward of 1.059 compared with 1.017 for a fixed-dose baseline. The results also show that unconstrained reward optimization can lead to excessive dosing, demonstrating the need for explicit operational safeguards. Third, the SHADE anomaly detection module uses a deep autoencoder to identify sensor and process anomalies, achieving an F1 score of 0.651 under controlled fault injection. HydroSphere combines these capabilities with tiered governance, deterministic safety bounds, and human oversight to support safer and more adaptive water infrastructure. The framework provides a scalable foundation for intelligent wastewater management and supports the objectives of UN Sustainable Development Goals 6 and 13.

---


### 8. [A Vehicle-Integrated Approach to Digital Twin Deployment for Bridges Through Drive-By Sensing](https://arxiv.org/abs/2610.08822)

**<font color=#1a73e8>作者：</font>** Zihao Liu, Daigo Kawabe, Jiaji Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ageing bridge infrastructure is a growing global concern, yet conventional Structural Health Monitoring (SHM) systems are costly and difficult to scale, and routine visual inspections remain subjective. Drive-by, or indirect, bridge inspection, in which a sensorised vehicle recovers structural information from vehicle-bridge interaction (VBI) and vehicle-road interaction (VRI) responses, offers a scalable alternative. However, key challenges remain unresolved, including separating bridge responses from road roughness, detecting damage under normal traffic, and generalising across diverse bridge types. This paper presents a vehicle-integrated digital twin framework that unifies physics-based modelling and machine learning for continuous monitoring of bridge and road conditions. The framework comprises three pillars. First, surrogate models of VBI and VRI are constructed using a Fourier Neural Operator that learns function-to-function mappings from operating conditions to vehicle responses. Trained on both simulated and field data, these surrogates deliver millisecond-scale inference, replacing computationally intensive full-order analyses. Second, the design of a custom electric inspection vehicle, its sensor layout, and signal processing chain are optimised through Bayesian optimisation to maximise bridge information yield while suppressing road and vehicle noise. Unsupervised damage-assessment pipelines based on adversarial autoencoders, matrix profiles, and transformer architectures have been developed and validated to process the resulting vehicle data. Third, the complete workflow is validated through coordinated multi-site field trials in Australia and Japan, covering a range of bridge types, traffic conditions, and environmental settings.

---


### 9. [HCPN-GCN: Scaling Hierarchical Prototype Networks with Cone Geometry for Continual Graph Learning](https://arxiv.org/abs/2610.08823)

**<font color=#1a73e8>作者：</font>** Sammuel R. Silva, Vander L. S. Freitas, Gladston Moreira 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual Graph Learning (CGL) aims to incrementally learn from graph-structured data while preserving knowledge acquired from previous tasks. A major challenge in this setting is catastrophic forgetting, where learning new tasks degrades performance on previously learned ones. Hierarchical Prototype Networks (HPNs) address this problem through a prototype-based memory mechanism that avoids storing historical data, but their reliance on linear feature extractors limits their ability to exploit graph topology, while point-based prototypes often lead to inefficient prototype growth on structurally diverse graphs. In this work, we propose HCPN-GCN, a graph-aware extension of HPN that replaces the original linear feature extractors with Graph Convolutional Networks (GCNs) and introduces cone-based prototypes with a diversity regularization objective. The proposed design produces richer graph-aware representations while compactly modeling the embedding space, reducing prototype proliferation without sacrificing discriminability. Experimental results on six continual graph learning benchmarks demonstrate that HCPN-GCN consistently improves average classification accuracy over the original HPN and representative continual learning baselines while maintaining near-zero forgetting. Furthermore, our analysis shows that the proposed model learns substantially richer class-level prototype hierarchies using approximately $30\times$ fewer atomic prototypes than the original HPN, providing a more compact and effective memory representation for continual graph learning.

---


### 10. [Autonomous Driving Research Requires a Community-Driven Data Paradigm](https://arxiv.org/abs/2610.08825)

**<font color=#1a73e8>作者：</font>** Jinsu Yoo, Zanming Huang, Katie Z Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving has made remarkable progress, with recent AI advances enabling commercial deployments that are reshaping urban mobility. Yet the field remains far from its universal social promise: autonomous systems that can operate robustly anywhere, anytime, for anyone. We posit that this gap is not merely a modeling problem, but a problem of the prevailing data paradigm. Current research relies heavily on a few benchmark datasets with limited spatial and scenario coverage, even though the community has collectively produced over 600 autonomous driving datasets across nearly 50 countries. However, this abundance has not translated into broad research impact: most datasets remain significantly underused due to fragmentation, limited visibility, incompatible protocols, and benchmark incentives that concentrate attention on a few dominant datasets. We therefore argue that autonomous driving research requires a collaborative, community-driven data paradigm. Such a paradigm would improve the discovery, reuse, integration, and evaluation of diverse datasets; make underexplored data easier and more rewarding to study; and lower the barrier for new contributors. We outline its key principles, illustrate an early realization, and call for collaboration across academia and industry to transform fragmented datasets into shared community infrastructure for anytime-anywhere autonomy.

---


### 11. [PanoPed: Beyond Bounding Boxes for Sim-to-Real Panoramic Pedestrian Tracking](https://arxiv.org/abs/2610.08826)

**<font color=#1a73e8>作者：</font>** Qinfeng Zhu, Weiguang Zhao, Yunxi Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Full-sphere panoramic cameras let fixed monitoring systems and mobile robots track people in every direction, but a planar bounding box does not fully describe where a person is on the sphere. We introduce PanoPed, a sim-to-real benchmark for pedestrian tracking on the full sphere. PanoPed-S contains 108,000 frames from fixed, quadruped-mounted, and drone-mounted cameras, with synchronized masks, depth, camera poses, and 3D pedestrian states. PanoPed-R adds 28,002 real frames from fixed cameras, 16,247 of them densely annotated. We find that an ERP rectangle cannot uniquely determine the spherical center and angular extent of the visible person, while the detector's visual query still carries information about them. Inspired by the sextant's use of angular measurements to locate objects, we propose Sextant, a plug-and-play angular localization head with only about 0.035M parameters. It reuses a frozen detector, keeps track identities unchanged, and needs no extra image encoder. Sextant gives the best result in our PanoPed-S test comparison, raising the strongest baseline, MOTIP, from 47.30 to 49.49 HOTA, with gains on all eight test sequences. Without fine-tuning on real data, the same synthetic-trained heads improve MOTIP and HAT by 0.96-1.14 HOTA on real video, and both seeds improve every real sequence. HAT+Sextant scores best among the compared systems that add no localization image encoder.

---


### 12. [Child ASR Adaptation with Adult Retention: An Empirical Study](https://arxiv.org/abs/2610.08827)

**<font color=#1a73e8>作者：</font>** Houssam Eddine-Othman Lachemat, Shammur Absar Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Speech Recognition (ASR) systems often underperform for children and non-native speakers, while adapting adult ASR models to child speech can cause adult-speech forgetting. We study child ASR adaptation with adult retention across Arabic and English. We compare full fine-tuning, LoRA, and post-hoc weight-space merging across encoder--decoder, encoder--CTC, and AudioLLM-based ASR systems. Experiments use Arabic native and non-native child speech, English MyST child speech, and adult benchmarks from MGB-2 and LibriSpeech test-clean. We evaluate recognition quality with WER and quantify the adaptation--retention trade-off using Retention Index, Child Adaptation Gain, and Adaptation Recovery. Results show that child adaptation is necessary, especially for non-native Arabic and English child speech, but direct adaptation often reduces adult ASR performance. Bilingual adaptation is more stable than language-specific adaptation. Weight-space merging often improves the trade-off, especially for encoder--CTC, Whisper, and AudioLLM-based ASR, with LERP favoring adult retention and TIES recovering stronger child gains. For the encoder--decoder model, direct bilingual fine-tuning remains strongest in raw WER.\footnote{Code, and models are available at this https URL.

---


### 13. [When Forgetting Looks Like Improvement: Metric Masking in Streaming Diarizer Adaptation and the Price of Rehearsal](https://arxiv.org/abs/2610.08828)

**<font color=#1a73e8>作者：</font>** Mo Yu, Yang Liu, Jing Qian  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small-data adaptation can improve speech detection while degrading speaker attribution. We study this discrepancy in a released streaming diarizer adapted on 7.5 h of two-party conversation and evaluated across six corpora. Adaptation substantially improves in-domain diarization performance and transfers to an independent corpus. However, this improvement is not consistent across evaluation scenarios as the additional confusion is mainly associated with impaired temporal identity consistency rather than speaker-count errors. A local-remapping diagnostic reveals different patterns of identity degradation across corpora, indicating that adaptation may alter how streaming models maintain speaker assignments over time. Rehearsal reduces the observed degradation but reduces the cross-domain transfer performance. These results highlight the need to jointly evaluate detection accuracy, identity consistency, and retention behavior when adapting streaming diarization systems.

---


### 14. [Beyond Risk Prediction: Evidence Grounding and Psychosocial Factor Verification for Explainable Suicide Risk Assessment](https://arxiv.org/abs/2610.08842)

**<font color=#1a73e8>作者：</font>** Tianle Hu, Chen Peng, Yi-Hsin Tsai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Identifying suicide risk from social networking services (SNS) posts is important for detecting suicide-related signals in online environments. However, risk classification alone provides limited insight into the textual evidence and psychosocial factors behind a prediction. Based on the IEEE BigData 2026 Explainable Suicide Risk Detection Challenge, this study presents a framework consisting of Risk Assessment, Evidence Grounding, and Factor Identification. Risk Assessment uses length-based routing to accommodate posts of different lengths. Evidence Grounding identifies supporting phrases and uses a Risk-Evidence constraint to maintain consistency with the Risk prediction. For Factor Identification, two verifiers are used. The Taxonomy Verifier focuses on factor semantics, whereas the Evidence-Aware Verifier uses factor-specific lexical-semantic cues to select informative positive training units. Their prediction probabilities are combined to produce the final factor predictions. The three tasks are evaluated using task-specific F1 score measures. Risk Assessment achieved a Weighted F1 of 0.8088, Evidence Grounding achieved a test Macro row F1 of 0.7605, and Factor Identification achieved a Macro F1 of 0.5562. The results show that the framework can provide risk predictions, along with supporting textual evidence and fine-grained information on psychosocial factors. Overall, the proposed framework extends suicide-risk assessment beyond risk-level prediction and provides a more interpretable analysis of SNS posts.

---


### 15. [Adversarial RL for Port-Scan Evasion: Attacker Feature Visibility in Edge-Deployed IDS](https://arxiv.org/abs/2610.08864)

**<font color=#1a73e8>作者：</font>** Logan Andrew North, Priya Sanjay Kaluskar, Shasi Kumar Ramachandran Prabhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning-based intrusion detection systems (IDS) are increasingly used in resource-constrained Internet of Things (IoT) environments, yet their robustness is often evaluated against static attacks rather than adversaries that adapt to detection feedback. This paper investigates adaptive port-scan evasion against ML-based IDS models deployed on a Raspberry Pi 3B+. We implement a live Zeek-based IDS pipeline with XGBoost, a multi-layer perceptron, and a 1D convolutional neural network trained on TON_IoT telemetry, and use a Deep Q-Network (DQN) adversary to learn evasive combinations of probe timing, TCP flags, and payload size under black-box, gray-box, and white-box feature-visibility settings. Although the deployed IDS models detect conventional port scans at 91.1--99.8%, DQN final-50-episode evasion rates range from 61.9% to 98.3% across feature-visibility settings. Greater feature visibility does not monotonically improve evasion, and its effect is model-dependent: against XGBoost, the black-box agent achieves 92.9% evasion, compared with 61.9% and 76.9% for gray-box and white-box agents, respectively, whereas 1D-CNN is most vulnerable under white-box access at 98.1%. Because standard DQN can overestimate action values, we additionally spot-check representative conditions using Double DQN. The gray-box condition remains unstable in this check, providing no evidence that overestimation bias alone explains the observed instability. These results show that limited feature knowledge can still enable effective adaptive evasion against static edge-deployed IDS models, motivating more robust defenses for IoT edge environments.

---


### 16. [A Deployment-Aware Feasibility Framework for Machine Learning-Based IoT Intrusion Detection Across Edge, Fog, and Cloud Architectures](https://arxiv.org/abs/2610.08867)

**<font color=#1a73e8>作者：</font>** Shaker Nawasra, Munther Abualkibash  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid growth and heterogeneity of Internet of Things (IoT) environments have exposed fundamental limitations in traditional rule-based and signature-based intrusion detection systems. This paper presents a quantitative deployment-aware analysis of machine learning (ML)-based intrusion detection approaches across edge, fog/gateway, and cloud architectures. Unlike prior surveys that primarily emphasize detection accuracy, this work defines representative quantitative deployment capability envelopes extracted from experimental and system-level studies and introduces a structured Deployment Feasibility Score (DFS) model. The proposed framework maps ML techniques to architectural layers based on computational demand, memory footprint, and latency sensitivity using a weighted ordinal scoring mechanism. The analysis demonstrates that lightweight statistical and linear models are most suitable for edge deployment, ensemble and clustering-based methods align with fog/gateway environments, while deep and optimization-driven models are best suited for cloud infrastructures. By formalizing deployment feasibility through quantitative grounding and structured evaluation, this work provides practical guidance for selecting intrusion detection solutions under real-world architectural constraints, supporting more informed and deployment-conscious IoT security design.

---


### 17. [Visible-Spectrum Optical Covert Channels in Commodity Smart Lighting](https://arxiv.org/abs/2610.08868)

**<font color=#1a73e8>作者：</font>** David Noever  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart light-emitting diode (LED) bulbs are networked devices that produce information-carrying output. This study asks whether that light can carry digital data through changes small enough to be difficult for a person in the room to notice. To explore this covert communication channel, we tested an unmodified smart bulb (Philips WiZ A19) using a camera as the receiver. Binary data were encoded programmatically in nearly matched color and brightness changes. Because the differences were deliberately small across 16 million color steps, the receiver periodically measured known reference states and used them to compensate for changes in the camera and background room illumination. The color method successfully transmitted the short message 'hi' using a color difference (E) of 0.5, a standard measure of perceptual color distance. The receiver recovered 99% of the transmitted bits, and the complete message passed an integrity check. The brightness method remained decodable at the smallest nonzero integer difference tested, alternating between dimming settings 56 and 54, with 96.2% mean bit accuracy across two runs. When both binary symbols were assigned to the same brightness in a control experiment, accuracy fell to approximately chance. These results show that the visible output of an ordinary smart bulb can serve as a low-rate data channel without hardware modification. Camera color drift can overwhelm small signals unless the receiver is recalibrated during transmission, sudden changes in ambient light can disrupt decoding, and longer messages require stronger error correction. The color experiment operated at a difference below a conventional threshold for human color discrimination. The corresponding perceptual limit for the brightness method has not yet been established experimentally.

---


### 18. [Towards Verifying Neural Networks Against Multi-Parameter Bit-Flip Perturbations](https://arxiv.org/abs/2610.08876)

**<font color=#1a73e8>作者：</font>** Hai Duong, Thanh Le, Ho Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware faults can flip bits in the stored weights of a quantized neural network, potentially compromising its predictions. While such faults typically affect multiple parameters simultaneously, existing verifiers are limited to single-parameter perturbations due to the combinatorial explosion of possible flip locations in large networks. We present mBFV (m-BitFlip Verifier), an efficient verification framework that proves robustness against simultaneous bit flips across multiple parameters without explicitly enumerating these combinations. mBFV achieves this via a novel multi-parameter bound propagation technique that directly aggregates the m worst-case contributions. To further tighten these bounds, mBFV employs a branch-and-bound mechanism over perturbation locations, partitioning the potential flips to smaller groups of neurons. Evaluated on 625 instances, mBFV successfully verifies 293, significantly outperforming a prior single-parameter verifier (38 verified instances) and an exact mixed-integer linear programming baseline (0 verified instances). Notably, while these baselines are restricted to single-parameter flips on small networks (up to 13k parameters), mBFV scales to verify networks with up to 1.15M parameters against up to four simultaneous parameter flips.

---


### 19. [How Could AI Eliminate Humanity? A Failure-Mode Analysis of Civilizational Risk](https://arxiv.org/abs/2610.08878)

**<font color=#1a73e8>作者：</font>** Mikołaj Sienicki, Krzysztof Sienicki  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This article develops a failure-mode framework for analyzing how advanced artificial intelligence could contribute to human extinction, irreversible civilizational collapse, or permanent human disempowerment. The central thesis is that catastrophic AI risk does not require consciousness, hostility, or an explicit intention to harm humanity. Instead, risk may arise through several distinct but interacting pathways, including autonomous misalignment, harmful human use, organizational failure, and competitive deployment. The severity of these pathways depends on factors such as capability, autonomy, external access, persistence, institutional safeguards, and the preservation of recovery capacity. The analysis is deliberately non-operational: it identifies causal conditions, empirically tractable intermediate quantities, and defensive research questions rather than procedures for causing harm.

---


### 20. [Contextualization of Third-Party Cloud Security Findings](https://arxiv.org/abs/2610.08895)

**<font color=#1a73e8>作者：</font>** Leon Goldberg, Gal Engelberg  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Finding severity is the main driver of how security teams prioritize remediation. For third-party cloud security findings, that severity is static: the rule that raised the finding assigns it before the rule meets any environment, so it reflects the risk of the condition in general rather than the risk the finding poses to the concrete environment where it lives. Scoring standards define where environment-specific context belongs. How far that context changes finding severities in production, where the deciding evidence lies, and whether it holds against the live environment have not been measured. We address this gap with contextualization, re-deriving each finding's severity from evidence in the environment where the finding lives. A deep research agent over a precomputed cross-signal asset graph investigates each finding against the resource's state, its graph neighborhood, and other products' signals, and returns an adjusted severity with an evidence trace. We evaluate it in a production field study of 9,967 vendor HIGH findings from two commercial cloud security platforms across eight real production environments, on three criteria: the faithfulness of the facts behind each verdict to the live environment, the dependence of each decision on context beyond the flagged resource, and the regularity of the reasoning. Three in four findings are re-graded, mostly downward, and the same rule often moves in opposite directions inside a single environment. About half of the decisive evidence lies beyond the flagged resource, and read-only probes of live infrastructure confirm the decisive fact for 99.4% of decided findings.

---


### 21. [Agent Plasticity: Measuring Self-Improvement Through Experience](https://arxiv.org/abs/2610.08902)

**<font color=#1a73e8>作者：</font>** Harman Singh, Anton Bakhtin, Rulin Shao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly operate in environments where they can diagnose failures and improve through experience, yet existing evaluations largely measure what an agent can do at a fixed point in time rather than how effectively it learns. Evaluating self-improvement requires answering three questions: does future performance improve and generalize beyond the interactions that enabled learning; how efficiently are new capabilities acquired; and where does the self-improvement process break down? To answer these questions, we study self-improvement in a controlled setting where agents amortize past experience into reusable artifacts that are inherited by future instances. At each checkpoint, we measure performance on training and held-out environment interactions while accounting for learning cost. We introduce agent plasticity, the efficiency with which an agent converts experience into gains in future held-out performance. Across multiple environments, frontier models exhibit sharply different improvement trajectories despite comparable opportunities to learn. Some achieve substantial and persistent gains, while others remain near or below their initial performance, and gains within the training regime often transfer only partially to out-of-distribution conditions. Endpoint capability and acquisition efficiency also diverge: the agent that ultimately performs best need not be the one that improves most efficiently. Tracing failures through the improvement loop further reveals different candidate bottlenecks. Agents with low plasticity often fail to reuse relevant artifacts, whereas more plastic agents may still fail despite reusing relevant artifacts, pointing to limitations in artifact quality, generalization, or application. Evaluating self-improving agents requires measuring not only what they can do, but how effectively they become better through experience.

---


### 22. [Can AI Agents Make Open-Ended Scientific Discovery? Evidence from Station](https://arxiv.org/abs/2610.08927)

**<font color=#1a73e8>作者：</font>** Wenyu Du, Stephen Chung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent AI systems have made rapid progress in scientific discovery when given well-defined metrics, but whether they can autonomously undertake open-ended scientific discovery remains unclear. We investigate AI's ability to tackle open-ended tasks in Station, an open-world environment in which multiple agents simulate a scientific ecosystem. To tackle challenges specific to open-ended tasks, we propose augmenting Station with two mechanisms: a Supervisor mechanism and periodic Meta Reflection, which encourage persistent exploration even when intermediate metrics are lacking. We construct open-ended tasks from three recent oral papers presented at ICLR. We give agents the main research question studied in each paper while withholding the paper's results and disabling web access. We then measure how many of the original findings-partitioned into individual criteria-agents rediscover. We find that Station rediscovers 62.7% of the criteria on average, compared with 15.4% for Codex Multiagent-v2 and 14.4-20.6% for AI Scientist-v2. Ablation and behavioral analyses indicate that adding the two mechanisms together improves research coverage and continuity. We further evaluate Station on two open-ended tasks without oracle papers and find that some of the discoveries made by the agents closely match discoveries reported by researchers after the knowledge cutoff date. Together, these results indicate that a suitable environment can enable agents to autonomously make meaningful progress in open-ended scientific discovery.

---


### 23. [VCR-Bench: A Modular Open-Source Benchmark for Video Classification Robustness](https://arxiv.org/abs/2610.08936)

**<font color=#1a73e8>作者：</font>** Maksim Plinskiy, Aleksandr Gushchin, Sergey Lavrushkin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robustness of image classification has several benchmarks, but their video counterparts are absent. In video classification temporal dimension introduces additional degrees of freedom for adversarial attacks, defenses, and preprocessing. Temporal sampling, perturbation budgets, and metric aggregation also interact in ways with no direct analogue in the image setting. Therefore, robustness for video classifiers is studied across scattered, incompatible implementations, making reported numbers hard to reproduce and analyze. We introduce VCR-Bench, a modular open-source benchmark framework that standardizes video loading, wrappers for classifiers, adversarial attacks and defenses, perceptual metrics, configuration presets, and result logging. VCR-Bench currently integrates 30 video classification models, 14 adversarial attacks, and 10 defense wrappers under a common evaluation protocol. We evaluate representative video classifiers, attacks, and defenses on Kinetics-400 subset, reporting clean accuracy, attack success rate, perceptual quality, runtime, and memory usage. VCR-Bench is released with documented installation, reproducible run presets, component-extension interfaces, and scripts for reproducing the reported results at this https URL.

---


### 24. [SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation](https://arxiv.org/abs/2610.08941)

**<font color=#1a73e8>作者：</font>** Yunheng Liu, Ziqi Cai, Siqi Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-guided panoramic video generation benefits various downstream applications, such as interactive 3D scene exploration, virtual reality experiences, and embodied agent training. Existing panoramic generators follow predefined trajectories, and interactive world models act through low-level actions in perspective views. We propose SPW-Nav, a streaming panoramic world model that understands movement instructions and streams one minute of 2K 360-degree video in real time from a single panorama. SPW-Nav interprets each instruction in the previously generated panorama as camera motion. Spherical rotation decoupling applies rotation exactly on the sphere, pose-aligned conditioning keeps translation inputs bounded over long streams, and a multi-term memory with a few-step generator continues the scene as instructions change. We also build SPW-NavSet, panoramic videos with camera trajectories and verified instructions. Driven by language, SPW-Nav outperforms prior panoramic generators in camera-following accuracy and video quality, and supports on-the-fly instruction switching.

---


### 25. [Directed Temporal Representations for Offline Visual Control](https://arxiv.org/abs/2610.08960)

**<font color=#1a73e8>作者：</font>** Chenyang Yuan, Haoyu Wang, Zhuo Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive world models provide compact visual representations for control. Control requires a latent geometry aligned with temporal reachability rather than predictive similarity alone. We introduce Directed Temporal Representations for Control (DTRC), which learns such a geometry from offline visual trajectories on top of frozen LeWorldModel (LeWM) features. DTRC constructs a directed temporal quasimetric over the learned control representation. Short-range temporal offsets calibrate the distance scale. Bootstrapped targets extend temporal reachability across longer horizons. Action-conditioned consistency aligns the representation with local transition dynamics. The resulting distance estimates temporal reaching cost, and its change across a transition defines goal-relative temporal progress. We use this progress signal as a temporal critic for direct goal-conditioned policy learning. Model-assisted targets provide an additional training-time refinement under behavior-support and dynamics-agreement constraints. Across ten visual control tasks, DTRC achieves strong goal-conditioned control performance relative to planning and direct-policy baselines. Held-out diagnostics on the four LeWM tasks show consistent short-range temporal calibration, task-dependent long-range and directional structure, and positive transition-level progress. Temporal supervision improves the same flow-policy parameterization across all four LeWM tasks, while the resulting policy acts directly without iterative trajectory search at test time.

---


### 26. [Work While They Sleep: Exploiting Evaluation Latency for Fully Bayesian Optimization](https://arxiv.org/abs/2610.08969)

**<font color=#1a73e8>作者：</font>** Gustavo Sutter, Alejandro Comas-Leon, David Holzmüller 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Black-box optimization problems are ubiquitous across science and engineering, often dealing with expensive objective functions. This objective latency has two consequences during optimization: (i) the objective evaluation dominates execution time, and (ii) sample-efficient algorithms are crucial to accelerate development and avoid wasting resources. Bayesian optimization (BO) methods are the \textit{de facto} choice of planners for suggesting the next point to try. Standard BO fits the surrogate model's hyperparameters with a point estimate. Alternatively, a fully Bayesian approach uses model averaging to account for uncertainty over the hyperparameters, leading to better uncertainty estimates---useful in the low-data regime that is pervasive in BO. However, it is often prohibitively expensive and thus rarely used. In this work, we propose ELF-BO, an algorithm that uses the objective evaluation latency to headstart the computation of the next suggestion, allowing for fully Bayesian optimization without incurring substantial decision-time costs. This is done by sampling from the hyperparameter posterior \emph{while} the objective is being evaluated, only requiring reweighting of the samples once the objective value is observed. Across synthetic functions and real-world applications, we show that ELF-BO matches the performance of fully Bayesian methods while only incurring decision latency on par with or better than standard BO. Thus, ELF-BO makes fully Bayesian optimization practical in real-world use cases.

---


### 27. [SNR-Gated LSTM-Conditioned Diffusion Model for MIMO Channel Estimation](https://arxiv.org/abs/2610.08977)

**<font color=#1a73e8>作者：</font>** Jixing Zhou, Xinming Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate and low latency channel estimation is critical for modern MIMO systems, particularly under mobility, where channels exhibit structured sparsity and strong temporal correlation. This paper proposes a time-series conditioned diffusion framework for channel estimation that performs denoising in the angular domain. Starting from least squares (LS) observations, we train a diffusion denoiser whose conditioning information is encoded by a long short-term memory (LSTM) network over a short observation sequence, enabling the model to exploit temporal dynamics beyond per-snapshot estimation. To robustly balance observation fidelity and learned generative priors across a wide signal-to-noise ratio (SNR) range, we introduce a learnable SNR-gated late-fusion shortcut that injects the network input into the final decoding stage through a sigmoid gate with trainable center and scale. To reduce inference latency, we adopt deterministic denoising diffusion implicit model (DDIM) style reverse updates with SNR-adaptive truncation and step allocation, which significantly reduces the number of reverse diffusion steps at high SNR while maintaining strong performance in low SNR regimes. Simulations on time-evolving standardized channel models demonstrate that the proposed method achieves consistent performance gains over existing diffusion-based channel estimation baselines, while retaining low latency through SNR-adaptive inference.

---


### 28. [S2Tok: Streaming 3D Gaussian Reconstruction with Persistent Spatial Tokens](https://arxiv.org/abs/2610.08978)

**<font color=#1a73e8>作者：</font>** Fang Li, Jiraphon Yenphraphai, Quentin Herau 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming 3D reconstruction requires more than a sequence of geometric predictions: it requires a persistent scene state that can incorporate new evidence and remain renderable as observations arrive. Latent spatial tokens offer a promising representation for this purpose, but constructing them from an image collection leaves open how to maintain them online, where each observation may both revisit known regions and reveal new content. We introduce S2Tok, a feed-forward framework that maintains a size-adaptive, persistent scene state from uncalibrated image streams. Its central idea is to distinguish updates to the existing representation from selective expansion. A spatially informed transformer integrates each incoming observation with the persistent scene tokens, while a learned admission module selectively expands the representation to limit redundant storage. A hierarchical decoder and Gaussian head convert the evolving state into non-pixel-aligned 3D Gaussians, enabling novel-view rendering without caching previous frames. Experiments across four benchmarks demonstrate competitive streaming rendering quality with compact Gaussian representations. These results support latent spatial tokens as a persistent computational state for online 3D reconstruction, combining learned scene updates with explicit Gaussian rendering.

---


### 29. [Zero-Shot Brain MRI Inpainting with 2.5D Unconditional Flow Priors](https://arxiv.org/abs/2610.08983)

**<font color=#1a73e8>作者：</font>** Arnela Hadzic, Franz Thaler, Simon Johannes Joham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative inpainting of brain MRI volumes is essential for synthesizing healthy tissue in pathological regions, improving the accuracy and reliability of automated downstream brain analysis applications such as image registration, brain extraction, and segmentation. However, standard 3D approaches are computationally prohibitive, while efficient 2D slice-wise methods suffer from severe inter-slice discontinuities. Furthermore, traditional models rely on conditional training, requiring task-specific learning of masked inputs. We propose a zero-shot brain MRI inpainting framework utilizing 2.5D unconditional flow priors to capture spatial context along the superior-inferior axis without the overhead of full 3D convolutions. During training, our flow matching model learns the joint distribution of adjacent axial slice triplets, modeling the manifold of healthy brain anatomy while explicitly excluding pathological regions from the loss function. At inference, the model processes the input triplets autoregressively along the depth axis. We employ the Restora-Flow solver to constrain the unconditional prior using the input mask, achieving accurate zero-shot inpainting. Evaluations show our 2.5D strategy resolves the structural discontinuities of 2D baselines, synthesizing plausible healthy tissue while maintaining volumetric consistency across the axial, sagittal, and coronal planes. As a final step, we generate and average an ensemble of multiple stochastic reconstructions to form the final prediction. Quantitative results benchmarked on the official BraTS 2026 Inpainting Challenge validation set demonstrate the effectiveness of our proposed approach, yielding an SSIM of 0.816 $\pm$ 0.112, MSE of 0.007 $\pm$ 0.005, and PSNR of 22.923 $\pm$ 4.343. Code is available at this https URL.

---


### 30. [LASER: Latent Space Adjoint Matching for Support-Constrained Entropy-Regularized Offline RL](https://arxiv.org/abs/2610.08989)

**<font color=#1a73e8>作者：</font>** Songyuan Zhang, Oswin So, Eric Yang Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While offline reinforcement learning (RL) enables policy optimization from static datasets without costly online interaction, it remains bottlenecked by the risk of executing out-of-distribution (OOD) actions. Recent approaches mitigate this by learning a behavior-cloning policy through flow matching and then performing RL within its constrained latent space. However, naively optimizing the latent policy can easily cause the policy to collapse into a brittle mode or exploit sharp artifacts of the learned critic. In this work, we find that entropy regularization is essential in latent-space RL for addressing these challenges. We introduce LASER, a novel offline RL algorithm that applies latent-space adjoint matching to achieve entropy-regularized latent-space RL with expressive flow policies while avoiding backpropagation through time. Through comprehensive experiments on 40 challenging OGBench tasks with varying dataset qualities, we show that LASER achieves state-of-the-art performance. Notably, LASER uses fixed method-specific hyperparameters across all tasks and outperforms the evaluated baselines, including those with task- and dataset-specific tuning, which highlights the robust applicability of LASER. Project website: this https URL.

---


### 31. [REFIT: Recognize, Fix, and Test Wearable Sensor Placement Shifts without Labels](https://arxiv.org/abs/2610.08991)

**<font color=#1a73e8>作者：</font>** Bangxun Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present REFIT, an input calibration for frozen activity-recognition models whose inertial sensors are worn differently at deployment than in training. When users move a watch to the other wrist or put a strap sensor back on turned, the model sees the same motion on changed axes. REFIT undoes such shifts without labels or retraining. It describes them by families of axis transforms, such as reflections and rotations, and fits each family to the user's data so that simple statistics match those of the training data. The family that removes most of the mismatch names the shift. REFIT fixes the shift by applying the best member of that family before the frozen model and re-estimating its normalization statistics. It tests the fixed model with a label-free accuracy estimate and asks the user to re-wear the sensor when it is low. Experiments on real left/right sensor pairs and on real and simulated re-attachment show that REFIT outperforms label-free test-time adaptation methods on every dataset and restores most of the accuracy lost to re-attachment. It names injected shifts far more reliably than a confidence-based selector. After a correction over all signed permutations of the axes, the estimate separates successful from failed corrections.

---


### 32. [Learning to Report Unsafe Tasks in a Multi-Agent Game](https://arxiv.org/abs/2610.09002)

**<font color=#1a73e8>作者：</font>** Avyay M. Casheekar, Hariganesh Tangirala  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When agents share a reward for completed tasks, reporting unsafe work can reduce the reporter's reward by stopping a task. Audits can make reporting optimal without ensuring that further training teaches a silent team to report. We study this learning problem in a game where any witness can stop a task by reporting. With $k$ witnesses per task sharing a policy and drawing independently, the expected-reward derivative with respect to their shared silence probability counts each task's benefit $k$ times at universal silence. The comparison with universal reporting counts it once. For arbitrary policy groups, we give an audit condition sufficient for exact policy-gradient updates to reach universal reporting and, apart from boundary cases, necessary near universal silence. In a balanced family, the cheapest audits meeting the condition with prescribed positive margins cost exactly $k$ times as much for full sharing as for one policy per role. We train PPO policies on 24 witness graphs from learned silence. Separating co-witnesses reduces unsafe completion by 33.59 percentage points compared with shuffled groups of the same sizes under the same audits (95% graph-bootstrap interval: 21.03-45.13). Only 9 of 48 witness-group runs achieve below 1% unsafe completion while retaining at least 90% legitimate completion. At the same audit budget, a fully shared network meets both thresholds in none of 48 runs with independent action draws and all 48 with a common draw.

---


### 33. [Removing Information Content Does Not Certify Tamper Resistance in Open-Weight Models](https://arxiv.org/abs/2610.09004)

**<font color=#1a73e8>作者：</font>** Domenic Rosati, Alessa Carbo, Ali Dadsetan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Does removing harmful information make open-weight models resistant to fine-tuning attacks? We show that mutual information at release alone cannot universally certify slow recovery. Function-preserving reparameterizations leave information unchanged while altering gradient-descent geometry, so an invariant certificate is bounded by the fastest reachable parameterization. We apply this principle to weight--data mutual information under training-data filtering and label--representation mutual information under capability removal. Training order can change recovery time at fixed weight--data information, while exact representation-level independence can preserve the entire parameter Jacobian. An explicit construction has both information quantities equal to zero and recovers in one gradient step. Controlled experiments illustrate order-dependent recovery and parameterization-dependent attack speed. These results identify the missing requirement for certification: constraints on attack dynamics beyond mutual information at release.

---


### 34. [Neighborhood Smoothing for Calibration](https://arxiv.org/abs/2610.09020)

**<font color=#1a73e8>作者：</font>** Idan Horowitz, Avigdor Gal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern neural networks are often miscalibrated, with a tendency to overconfidence. Existing train-time calibration methods largely modify task losses or calibration penalties, leaving neighborhood structure in learned representations underexploited. We introduce graph smoothing as a general principle for train-time calibration, which encourages similar predictive distributions across neighboring samples in representation space. We analyze the effects of graph smoothing, deriving bounds that connect predictive divergence between neighboring samples to local confidence variation and to the propagation of pointwise calibration error, and characterize the conditions under which smoothing can or cannot improve calibration. In light of this analysis, we propose \modelNoSpace, a graph-based train-time regularizer that penalizes the Jensen--Shannon divergence between predictive distributions of neighboring samples. We present a thorough empirical analysis, showing that across standard calibration benchmarks, \model improves predictive quality, and the improvement is complementary to post-hoc calibration: after temperature scaling, \model attains the lowest NLL of all evaluated train-time methods in seven of the eight image and tabular settings. These findings demonstrate the value of graph smoothing over learned representations for neural network calibration.

---


### 35. [Cost of Delay for Post-Quantum Migration: Putting Classical and Harvest-Now-Decrypt-Later Risk on One Ordered List](https://arxiv.org/abs/2610.09029)

**<font color=#1a73e8>作者：</font>** Animesh Shaw  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Organisations deciding which assets to migrate to post-quantum cryptography first, and how that work competes with a backlog of classical findings, lack a common unit: post-quantum scores are dimensionless and quantum-only, while classical risk is annualised loss. We express both threats as a cost of delay in currency per year on the same asset. The quantum term is the rate at which deferring migration commits irreversible harvest-now-decrypt-later loss, computed from required confidentiality duration, recordable traffic share and data turnover, using a quantum-arrival law fitted in closed form to published expert anchors. A competing-risks factor couples the two terms so the same loss is not counted twice. We prove that the construction is not a weighted sum of a classical and a quantum score, give a dominance threshold on the classical hazard that is independent of asset value, and show that the induced order is optimal for sequencing work under constant loss rates. We verify the implementation by simulation, adaptive quadrature and a second implementation. On four public systems with parameters assumed from public documentation, the quantum term reorders the asset list beyond input uncertainty for one system only (signal-to-noise 1.36 against 0.14-0.46), moves specific long-lived, quiet, recordable assets decisively, and otherwise changes magnitudes. Asset value and turnover explain 73-91% of the uncertainty in the quantum term; the arrival date explains 3-17%. The case studies are illustrative and are not validated against outcomes.

---


### 36. [Beyond Explanation: Debugging Medical Imaging Models via Concept Intervention](https://arxiv.org/abs/2610.09031)

**<font color=#1a73e8>作者：</font>** Samrajya Thapa, Daniel J. Quest, Timothy L. Kline 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical imaging models often operate as black boxes, limiting interpretability and systematic debugging. We introduce an easy-to-use, plug-and-play framework for concept-based interpretation and model refinement. By aligning a single-modality encoder to BioMedCLIP, we construct a Concept Bottleneck Model (CBM) that enables concept-level interventions. These interventions allow us to isolate causal versus spuriously correlated concepts, validate insights with domain experts, and generate counterfactual samples for targeted fine-tuning. We evaluate our framework on a Mayo Clinic ultrasound dataset and the CheXpert 5x200 chest X-ray dataset. Results demonstrate that concept intervention enables reliable model diagnosis while maintaining, and occasionally improving predictive performance via guided fine-tuning. Our findings highlight the practical value of this framework for controlled, interpretable refinement of clinical deep learning models.

---


### 37. [Shape-Bayes: Bayesian Inference of Structured Shapes under Visual Ambiguity](https://arxiv.org/abs/2610.09032)

**<font color=#1a73e8>作者：</font>** Mani Kumar Tellamekala, Tosh Brown, Michel Valstar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perceiving structured shapes, such as human faces, from pixels is an inherently ambiguous task in real-world conditions. Yet, shape inference is largely posed as a deterministic regression task predicting fixed spatial coordinates. We find that deterministic regression is brittle when visual evidence is ambiguous or incomplete; under severe occlusions deterministic models exhibit structural collapse, predicting incoherent shapes or reverting to generic averages. To address this, we introduce Shape-Bayes, a probabilistic framework that couples uncertainty-aware visual perception with Bayesian shape reasoning. Rather than forcing point estimates, Shape-Bayes dynamically weights visual evidence against geometric priors to infer a structurally valid shape posterior. Demonstrated on human face shape regression, a rigorous testbed featuring complex non-rigid deformations and strict anatomical constraints, Shape-Bayes comprises: (1) a base model predicting noisy landmarks alongside distilled aleatoric uncertainties; (2) a lightweight Transformer encoding these observations into an adaptive prior over a PCA shape manifold; and (3) a differentiable Bayesian solver computing closed-form posteriors by balancing the noisy predictions against this prior. By guaranteeing complete structural integrity, Shape-Bayes achieves an absolute improvement of up to ~34% IDR over state-of-the-art deterministic models. Simultaneously, it yields highly calibrated uncertainty bounds and reduces relative error by up to 12.5%, establishing a new state-of-the-art for robust 2D face shape regression under severe occlusion. The project page is at this https URL.

---


### 38. [Shared-Roadmap Generation and Evaluator for Multi-Agent Path Planning Using Heterogeneous Graph Neural Network](https://arxiv.org/abs/2610.09034)

**<font color=#1a73e8>作者：</font>** Brandon Ho, Nikola Rogers, Seung-Kyum Choi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent path planning (MAPP) in continuous environments often relies on roadmaps to balance safety and search efficiency. However, traditional roadmap generation methods, such as lattice grids or standard sampling-based approaches, frequently face a trade-off between graph density and the likelihood of finding feasible, high-quality solutions. In this paper, we propose a scalable heterogeneous Graph Neural Network (GNN) framework for the automated generation and evaluation of shared multi-agent roadmaps. Our model covers the representation of waypoints, agent locations, and task locations as distinct nodes in a heterogeneous graph, allowing it to reason over global connectivity and inter-agent interactions. By training on occupation density maps aggregated and collected from expert solver trajectories, the GNN learns to identify critical points of interest and prune redundant nodes and edges. This process produces a compact, coordination-aware roadmap that is invariant to task permutations and is reusable for multi-agent pick and delivery tasks. Experimental results demonstrate that our framework can reduce planning effort and can potentially find better solutions, reaching at least 40% reduction in runtime and in graph size for dense roadmaps.

---


### 39. [ORACLE: Optimizer-Relative Alignment for Constrained LEarning](https://arxiv.org/abs/2610.09040)

**<font color=#1a73e8>作者：</font>** Utkarsh Grover, Wyatt Mackey, Kaixun Hua 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constraint handling methods typically intervene before the optimizer acts, by modifying the objective or the gradient. Yet momentum, adaptive scaling, and structured preconditioning can substantially reshape that signal before it becomes a parameter update. We formulate optimizer relative constrained learning, where constraint compatibility is assessed on the post optimizer update. Building on this view, we introduce ORACLE, which evaluates the native optimizer's realized step through a joint endpoint linearization of heterogeneous constraint families, constructs the resulting alignment in the optimizer's own geometry, bounds its authority, and commits it only after validation. We evaluate ORACLE across eight Partial Differential Equation benchmarks and four optimizers spanning Euclidean, diagonal adaptive, and structured preconditioned geometries, where it improves or matches native optimizer in 94% of configurations. Cross model analysis shows the same behavior in 92% of configurations, while matched comparisons show improvements over alternative constraint-handling methods acting at the objective, gradient, and post-optimizer levels.

---


### 40. [Towards Financial World Modeling](https://arxiv.org/abs/2610.09048)

**<font color=#1a73e8>作者：</font>** Humzah Merchant, Alec Guthrie, Simon Mahns 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Building a world model requires a state representation useful for planning and decision-making---potentially over tasks unknown at training time. In the context of financial markets, planning and decision-making may require a model to reason about market-wide conditions, asset-specific expected returns, liquidity, volatility, and cross-asset relationships. Yet financial representation learning has largely been evaluated on individual predictive tasks, oftentimes on a single time period using comparatively narrow datasets. We address this through three primary contributions. First, we introduce Market-1T, a dataset containing nearly one trillion observations across U.S. equities from 2008 to 2025 at 1 Hz resolution. Second, we develop and implement a rigorous evaluation protocol. Third, we conduct a systematic large-scale study of financial representation learning, comparing 18 encoder-training strategies across nearly two decades of market regimes. We evaluate learned representations both by their predictive utility on common finance tasks and through probes of latent structure. We find that encoders with similar predictive performance can organize market state very differently. Collectively, we establish a foundation for training and evaluating financial market representations in support of world models such as DINO-WM, V-JEPA 2, and LeWM.

---


### 41. [BeatFlow-ECG: Rectified Flow for ECG Reconstruction from Indirect Wearable Signals](https://arxiv.org/abs/2610.09052)

**<font color=#1a73e8>作者：</font>** Mohamed Kamel, Sahar Selim, Walaa Medhat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous cardiac monitoring outside clinical settings requires signals that are both informative and practical to collect during daily life. Electrocardiography (ECG) provides rich information about cardiac rhythm and waveform morphology, while wearable photoplethysmography (PPG) is easier to acquire continuously but is only an indirect cardiovascular measurement and is highly sensitive to motion. We present BeatFlow-ECG, a conditional rectified-flow model for reconstructing single-channel ECG from synchronized PPG and inertial measurements. BeatFlow-ECG models reconstruction as conditional transport from noise to ECG using a convolutional encoder-decoder with a transformer bottleneck and explicit flow-time conditioning. Motion information is incorporated through IMU-derived conditioning features, motion-dependent loss weighting, and an easy-to-hard training curriculum. We evaluate the model under leave-one-subject-out protocols on PPG-DaLiA and WESAD. BeatFlow-ECG achieves the best results among the evaluated deterministic, adversarial, and diffusion-based baselines across all reported waveform and beat-timing metrics, with Pearson correlations of 0.983 and 0.986 and R-peak F1 scores of 0.946 and 0.955, respectively. Compared with Conditional DDPM-1D, L1 error decreases from 0.085 to 0.062 on PPG-DaLiA and from 0.074 to 0.055 on WESAD. Additional analyses on PPG-DaLiA show higher correlation in fixed R-peak-relative waveform regions and lower reconstruction error across low-, medium-, and high-motion subsets.

---


### 42. [A Geometry-Based Capacity Theory for Finite-Feature Associative Memory](https://arxiv.org/abs/2610.09056)

**<font color=#1a73e8>作者：</font>** Jianhai Zhang, Donghao Zhang, Pattarawut Charatpangoon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a geometry-based capacity theory for exact-key retrieval in compressed finite-feature Hebbian associative memory. For random or approximately isotropic values, retrieval interference separates into finite-feature noise, which decreases with feature dimension, and structural interference, which is determined by squared kernel overlap among stored keys and persists in the infinite-feature limit. This yields a fit-free prediction of retrieval quality, reveals a geometry-dependent capacity ceiling, and predicts the feature budget required for a target retrieval quality. When stored values are correlated, we show that retrieval depends jointly on the key kernel and value Gram matrix, and derive finite-feature approximations that account for this interaction. We validate the theory on synthetic, visual, and medical-image representations. Overall, the framework links representation geometry directly to memory capacity and distinguishes when performance can be improved by increasing the feature budget and when the representation itself must be changed. Across these settings, the predicted retrieval curves closely match empirical behavior and correctly identify changes in the preferred memory design.

---


### 43. [Epistemic Uncertainty-Aware Defect Detection for Quality Control in Medical Device Manufacturing](https://arxiv.org/abs/2610.09057)

**<font color=#1a73e8>作者：</font>** Raham A. Butt, Marco Romanelli, Roche C. de Guzman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objective: We investigate whether accounting for epistemic uncertainty can improve the reliability of automated defect detection in medical device manufacturing. Methods: We consider a machine learning framework that operates on heterogeneous manufacturing and device-report data represented with Knowledge Graphs. To mitigate errors arising from uncertainty in the decision model, we analyze a principled rejection strategy to abstain from predictions whose estimated epistemic uncertainty exceeds a specified threshold. We evaluate the approach using standard synthetic benchmarks and real-world medical device report data. Results: The theoretical results establish the validity of the method characterizing the regimes under which it is expected to be effective. Empirically, the rejection strategy enables explicit control of coverage, that is, the proportion of samples for which the model issues predictions, while improving performance on the retained samples. On 266,170 real-world FDA MAUDE device reports, a 10% abstention rate reduces classification error by 48%, and more aggressive rejection (approximately 70% coverage) yields near-perfect accuracy on the retained samples. On standard synthetic manufacturing benchmarks, abstaining on 9% of the decisions, our approach reduces the risk up to 63% compared with the standard no-abstention approach. Conclusions: Abstaining from predictions with high epistemic uncertainty can provide a practical tool for controlling the reliability of machine learning-based defect detection, especially in high-stakes medical device manufacturing applications. Significance: Uncertainty-aware defect detection may support safer and more reliable quality assurance in medical device manufacturing by identifying cases that require additional inspection rather than issuing potentially harmful predictions.

---


### 44. [EDiS: Edge Disjoint Subgraph Sparsification Framework for Graph Neural Networks](https://arxiv.org/abs/2610.09059)

**<font color=#1a73e8>作者：</font>** Sai Karthik Navuluru, Siddhartha Shankar Das, Franck Dernoncourt 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse GNN training reduces computation, but deciding which edges to keep can be costly. Reusing one sparse graph is cheap, but locks training to a fixed topology, while varying it across epochs can require repeated sampling or recomputation. We introduce EDiS (Edge-Disjoint Subgraph sparsification framework), which separates one-time structural extraction from per-epoch graph composition. EDiS decomposes the graph once into cacheable edge-disjoint subgraphs, then recombines them into graphs with edge-budget constraints across epochs and retention ratios without re-extracting structure. Our default construction uses feature-based scores and successive maximum score covering forests, while the same composition mechanism also supports alternative edge selection rules. We provide a combinatorial analysis of the per-epoch sampler, the composition step that draws a training graph from the cached decomposition. We show that, under the default covering-forest selector, the stored decomposition deterministically preserves high-score cut edges, and we derive a selector-agnostic conditional bound on high-score cut survival in composed training graphs. Across 19 homophilic, heterophilic, and large-scale node classification benchmarks against 17 baselines under the same edge budget, EDiS achieves the highest mean benchmark score (accuracy/ROC-AUC) and the lowest average rank and gap-to-best among ranked methods. Ablations show the clearest benefits of structural decomposition and epoch variation at tight edge budgets.

---


### 45. [Supporting Allyship in Virtual Collaboration with Artificial Intelligence: A Scenario-Based Study](https://arxiv.org/abs/2610.09061)

**<font color=#1a73e8>作者：</font>** Crescentia Jung, Ricardo E. Gonzalez Penuela, Prashita Biswas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent research has revealed that accessibility in virtual collaboration is not only a technical problem but also depends on allyship: the informal, interpersonal practices through which people support others' accessibility needs. Yet little research has examined how artificial intelligence (AI) might support allyship in collaborative accessibility contexts. To address this gap, we conducted a study where 18 participants (10 disabled, 8 non-disabled) reflected on four allyship scenarios with novel AI tools. Participants valued AI designs that they anticipated could help teammates express, interpret, and coordinate around access needs by reducing repeated disclosure and making allyship more actionable. At the same time, participants raised concerns when AI acted without consent, misrepresented users' intentions, or displaced the interpersonal work of allyship. Based on our findings, we introduce allyship-support tools as a class of accessibility technologies, offer design guidelines, and discuss AI in particular as a means of supporting allyship.

---


### 46. [GUARD: Geometric Uncertainty-Aware Point Cloud Denoising and Segmentation for Robotic Hard Disk Drive Disassembly](https://arxiv.org/abs/2610.09068)

**<font color=#1a73e8>作者：</font>** Zuoxu Wang, Xiao Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable robotic disassembly requires part-level representations that distinguish genuine component geometry from scanning and reconstruction artifacts. In point clouds of hard disk drives (HDDs), structured ghost artifacts can resemble valid components locally while remaining inconsistent with the overall geometry, allowing erroneous measurements to receive plausible semantic labels. This creates an engineering information problem: semantic prediction confidence alone does not establish whether the underlying geometry is reliable. We propose \textbf{GUARD}, a geometric uncertainty-aware framework that performs point filtering and segmentation within a single forward pass by modeling the reliability of learned geometric representations. GUARD combines a multi-scale geometric transformer with a multi-bandwidth random Fourier feature Gaussian Process to estimate per-point geometric uncertainty, complemented by predictive entropy to suppress unreliable measurements while preserving informative structures. Evaluation on 2,745 real HDD point clouds shows that GUARD improves PointNet++ segmentation mean intersection over union from 0.7739 to 0.8318. Additional experiments on ShapeNetPart and ScanNet examine robustness across corruption types, point-cloud domains, and segmentation backbones. On manually annotated ScanNet samples, geometric uncertainty achieves a corrupted-point detection F1 score of 0.7931, compared with 0.2212 for predictive entropy. The results demonstrate the value of distinguishing geometric reliability from semantic confidence and reveal a tradeoff between artifact suppression and preservation of informative structures. GUARD contributes a reliability-aware approach to interpreting imperfect 3D measurements for component identification and subsequent robotic handling. Project website: this https URL.

---


### 47. [OverLay++: Dense-Overlap Layout-to-Image Generation Dataset](https://arxiv.org/abs/2610.09071)

**<font color=#1a73e8>作者：</font>** Shivansh Aggarwal, Shresth Grover, Divyansh Srivastava 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Layout-to-Image generation has made substantial progress in spatial and object-level control. However, existing methods still struggle with complex scenes containing many overlapping and interacting objects. We argue that training data is a particular bottleneck: existing datasets lack examples with dense, complex object interactions. To address this gap, we introduce OverLay++, a large-scale Layout-to-Image dataset with structurally complex scenes. OverLay++ contains approximately 500K images with an average of 6.6 objects per image, exceeding existing datasets by 1.67 times in annotation density. Beyond annotation density, OverLay++ provides rich semantic detail with object captions over six times longer than in current datasets. Our dataset generation pipeline is simple and produces dense, overlapping object annotations with rich per-object captions. Across multiple benchmarks, state-of-the-art Layout-to-Image methods trained on the OverLay++ dataset show consistent improvement and faster convergence, demonstrating the importance of dense, overlap-aware, and caption-rich supervision for controllable image generation.

---


### 48. [DISRQAD: Diffusion Image Super-Resolution Quality Assessment Dataset and Benchmark](https://arxiv.org/abs/2610.09077)

**<font color=#1a73e8>作者：</font>** Nikita Kukuzei, Artem Borisov, Evgeney Bogatyrev 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based image super-resolution (SR) can create visually plausible detail that is not supported by the low-resolution input. We introduce DISRQAD, a subjective-quality dataset and diagnostic benchmark for this setting. It contains mean opinion scores (MOS) for 14,000 SR outputs from ten diffusion and four non-diffusion methods, spanning four low-resolution degradation conditions and x2/x4 upscaling. We evaluate 51 standard full-reference and no-reference metric configurations and 11 adapted variants. Agreement with MOS is substantially weaker on diffusion outputs: the strongest standard no-reference baseline reaches 0.431 SRCC on diffusion SR versus 0.813 on non-diffusion SR. As a case study in benchmark use, a pruned and distilled Q-ReAlign-mini student reaches 0.496 SRCC on diffusion SR. DISRQAD measures perceived output quality, not faithfulness to the input; it enables analysis of metric behavior across generator families and input conditions. Our findings reveal a substantial gap in the assessment of diffusion-based SR and provide a basis for developing quality models sensitive to diffusion-specific artifacts.

---


### 49. [Tucker Bottleneck Attention for Multi-Dimensional Sequence Modeling](https://arxiv.org/abs/2610.09090)

**<font color=#1a73e8>作者：</font>** Ryan Solgi, Parsa Madinei, Zheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quadratic cost of self-attention limits scalability to long sequences from multidimensional data. We introduce Tucker bottleneck attention (TuBA), which exploits low-rank tensor structure for efficient global token mixing. TuBA projects hidden tensors into compact Tucker cores, performs multi-head self-attention and linear projections on the cores, and writes updates back to the ambient space, enabling subquadratic computation. Its autoregressive extension combines bidirectional interactions within cores with causal attention across cores. On video prediction and global weather forecasting, TuBA achieves favorable accuracy-efficiency trade-offs over standard and efficient attention and task-specific models. Compared to standard self-attention, TuBA reduces error and computation by up to 24.7% and 66.6% for video prediction and 37.1% and 85.1% for autoregressive weather forecasting, with speedups up to 4.27 times. Low-rank Tucker cores and multi-frame generation also outperform full-rank attention and frame-by-frame generation, respectively.

---


### 50. [FedRSPO+: A Heterogeneity-aware Algorithm for Decision-focused Federated Learning](https://arxiv.org/abs/2610.09091)

**<font color=#1a73e8>作者：</font>** Konstantinos Ziliaskopoulos, Alexander Vinel, Jiaqi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-focused learning (DFL) trains predictive models for downstream optimization, but existing methods largely assume centralized data. In cross-silo settings, federated learning offers a natural alternative, yet standard federated methods optimize prediction over decision quality and do not address heterogeneity in downstream objectives or feasible sets. This heterogeneity is especially challenging for DFL because small perturbations in polyhedral problems can cause discontinuous changes in optimal decisions, destabilizing client updates and aggregation. We propose FedRSPO+, a heterogeneity-aware framework for decision-focused federated learning, built on RSPO+, a regularized predict-then-optimize surrogate that smooths the decision map through projection. We show that RSPO+ upper bounds decision error and regret for the regularized decision and, under exact regularization and consistent LP solution selection, for the original LP decision. We further derive cross-client heterogeneity bounds that depend on both objective and feasible-set heterogeneity, vanish at homogeneity, and require no strong convexity. FedRSPO+ uses an annealed, modular training procedure compatible with standard federated personalization and aggregation methods. Experiments on synthetic knapsack, shortest-path, and real-world energy pricing tasks compare against prediction-only federated learning and DFL baselines under varying heterogeneity and communication budgets. Results suggest that smoothing is a useful ingredient for stable collaborative decision learning and provide a heterogeneity-aware foundation for federated DFL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-324](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
