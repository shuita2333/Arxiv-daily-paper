# 📦 其他研究 | 2026年09月04日

> 本类共 **187** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-187](./part-04.md)

---

### 1. [DiDrive: A Risk-Aware Hierarchical Diffusion Framework for Safe Offline Reinforcement Learning in Autonomous Driving](https://arxiv.org/abs/2609.01609)

**<font color=#1a73e8>作者：</font>** Qisong Guo, Jingtang Chen, Zhilin Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While diffusion models effectively capture multimodal behavioral priors for autonomous driving, offline reinforcement learning (RL) policies remain susceptible to distribution shift, heavy-tailed risk signals, out-of-distribution (OOD) action generation, and high-dimensional state redundancy. To address these challenges, we propose DiDrive, a distribution-guided offline diffusion framework featuring two synergistic components: the Risk-Aware Hierarchical Diffusion (RHDif) architecture and the 3DICE policy optimization paradigm. In the state space, RHDif utilizes a low-level risk-gated encoder and a high-level contextual modulator to filter environmental redundancy and focus on safety-critical threats. In the action space, 3DICE mitigates OOD overestimation and gradient oscillation through in-sample calibrated guidance, spatiotemporal optimization, and ensemble-based candidate ranking. Evaluations on the CARLA benchmark demonstrate DiDrive's superiority over baselines like IQL, CQL, and Diffusion-QL, particularly in complex, high-density traffic scenarios with 60 vehicles, where it achieves an 85% success rate and a 4295.68 average reward, providing a robust pathway for safe autonomous driving decision-making.

---


### 2. [PRISM: An Agentic Multi-Model Architecture for Proactive Safety in Autonomous Transportation Systems](https://arxiv.org/abs/2609.01623)

**<font color=#1a73e8>作者：</font>** Joyjit Roy, Samaresh Kumar Singh, Sushanta Das  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Autonomous and intelligent transportation systems operate in complex urban environments where safety depends on interactions among vehicle behavior, environmental conditions, and vulnerable road users (VRUs) such as pedestrians and cyclists. Most advanced driver assistance systems (ADAS) employ reactive mechanisms that activate only after hazards have emerged, a critical limitation underscored by rising VRU fatalities in the United States.
This study introduces PRISM (Proactive Risk Intelligence and Safety Management), an agentic multi-model safety architecture that transitions from reactive crash avoidance to proactive, continuous risk management. PRISM employs inverse crash-probability modeling to convert binary crash classifiers into dynamic, interpretable safety scores. Three specialized models addressing trajectory kinematics, environmental risk, and VRU interaction operate concurrently, coordinated by a reasoning layer incorporating reinforcement learning, contextual memory, and feature-level attribution. The system provides graduated safety interventions across four tiers, from silent monitoring to emergency alerts.
Unlike rule-based systems with static thresholds, PRISM dynamically adjusts safety parameters in real time. Validated across 1,296 scenarios from three naturalistic driving datasets without dataset-specific retraining, the system yielded a mean safety score of 68 out of 100, classified 77.6% of scenarios as advisory, and flagged a near-miss rate of 3.8%, with 11% of scenarios escalating to intervention or emergency response. Feature attribution consistently identified trajectory risk and VRU proximity as primary safety factors. PRISM provides a unified, interpretable framework for proactive transportation safety with emphasis on VRU risk reduction in dense urban environments.

---


### 3. [Efficient Context-Limited Telescope Bibliography Classification for the WASP-2025 Shared Task Using SciBERT](https://arxiv.org/abs/2609.01647)

**<font color=#1a73e8>作者：</font>** Madhusudhana Naidu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The creation of telescope bibliographies is a crucial part of assessing the scientific impact of observatories and ensuring reproducibility in astronomy. This task involves identifying, categorizing, and linking scientific publications that reference or use specific telescopes. However, this process remains largely manual and resource intensive. In this work, we present an efficient SciBERT-based approach for automatic classification of scientific papers into four categories - science, instrumentation, mention, and not telescope. Despite strict context-length constraints (maximum 512 tokens) and limited compute resources, our approach achieved a macro F1 score of 0.89, ranking at the top of the WASP-2025 leaderboard. We analyze the effect of truncation and show that even with half the samples exceeding the token limit, SciBERT's domain alignment enables robust classification. We discuss trade-offs between truncation, chunking, and long-context models, providing insights into the efficiency frontier for scientific text curation.

---


### 4. [Private Computation Space: Experience with Trusted Multi-Cluster Federated Learning for Agriculture](https://arxiv.org/abs/2609.01667)

**<font color=#1a73e8>作者：</font>** Shuangyu Lei, Muhammad Salman Abid, Jacob Belding 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence has shown to help improve agricultural practices, yet adoption remains limited: 69% of U.S. farmers have privacy concerns with sharing their data, and these concerns must be addressed before adoption is widespread. While Federated Learning has been demonstrated to protect privacy at scale for other sectors, deploying a system for agriculture comes with its own set of challenges; the problem necessitates a system that can protect farmer data and identities while preserving model utility, runs on commodity hardware, and is resilient to fragile rural infrastructure. To address these concerns, we introduce the Private Computation Space (PCS), a deployed, open-source Machine Learning system to provision and process farmer data securely. We design a system tailored to an agricultural setting, with multi-cluster orchestration for reliability in rural areas with asynchronous Federated Learning (FL), Differential Privacy (DP), and Trusted Execution Environments (TEEs), to allow farms to participate in the framework while keeping their data private. We evaluate the system on two deployed workloads: monitoring nitrogen with living plant sensors in NY for six months and predicting evapotranspiration from weather stations in CA for ten months. Our evaluation finds a Dice Similarity Coefficient (DSC) of 0.71 and $R^2$ accuracy of 0.84 for the respective workloads, improving the worst single-site model accuracy by 22.4% and 9.1%, respectively, while preserving privacy.

---


### 5. [CliffRank: A Dual-Branch Framework for Activity-Cliff Ranking Prediction](https://arxiv.org/abs/2609.01673)

**<font color=#1a73e8>作者：</font>** Kewei Li, Rongying Zhang, Peiyu Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activity-cliff ranking remains difficult because local structural changes can cause large activity differences, while high-quality data that resolve the underlying mechanisms remain limited. To use available activity labels more effectively, we combine absolute-activity regression with ranking-consistency learning. CliffRank trains two parallel predictors with mean squared error, a thresholded listwise loss, and Pairwise Preference Consistency (PPC), which aligns relative ordering in the preference-probability space. On three antimicrobial peptide datasets, CliffRank with ESM2-t12 achieved the highest mean Spearman correlation of 0.5393 and mean Recall@50 of 21.4, although the leading method varied across individual datasets. On three small-molecule datasets, CliffRank with PNA, where PPC was activated after 120 epochs, achieved the highest mean Spearman correlation of 0.6890, while its mean Recall@50 of 30.4 matched that of ACANet-PNA. The PPC results also define its practical limits. Asymmetric initialization improved the MolCLR-GIN averages but did not improve every target. For PNA without pretrained weights, delayed PPC improved selected metrics, but no schedule was best for both mean Spearman correlation and mean Recall@50. Future work should evaluate more targets and antimicrobial peptide systems, develop adaptive PPC schedules, and incorporate protein or membrane context when available.

---


### 6. [Sim2Signal: Sim-to-Real Benchmarks for Traffic Signal Control](https://arxiv.org/abs/2609.01676)

**<font color=#1a73e8>作者：</font>** Ferdous Al Rafi, Susrik Mukherjee, Latika Liladhar Dekate 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning achieves strong traffic signal control performance in simulation, yet policies trained in simulators often fail once deployed in the real world, a failure known as the Sim-to-Real gap. When RL is applied to traffic signal control, this gap arises from several sources: sensing, action execution, traffic dynamics, and the control objective. Their relative impact and the reliability of existing Sim-to-Real mitigation methods remain insufficiently understood, and the field lacks a standard benchmark for systematically measuring the gap and evaluating mitigation methods. We present Sim2Signal, a benchmark that decomposes the Sim-to-Real gap into observation, action, transition, and reward gaps, corresponding to mismatches in the four components of the underlying MDP, and induces each gap in isolation under a shared protocol. We evaluate 18 mitigation methods on 2 base controllers, across 33 gap settings and 10 calibrated networks built from 5 real-world locations. We find that direct transfer consistently degrades performance across all four gap sources, but the severity of the degradation does not predict the effectiveness of mitigation. Instead, mitigation effectiveness depends strongly on the network and gap setting: outside the action gap, a method that helps in one case may fail in another. The most effective methods generally estimate what the gap changes, rather than make the policy insensitive through domain randomization or invariant representations. Our code is available at this https URL

---


### 7. [Reinforcement Learning and Rule-Based Peer-to-Peer Pricing in Residential PV-BES Communities](https://arxiv.org/abs/2609.01680)

**<font color=#1a73e8>作者：</font>** Pablo Benalcazar, Maciej Kalka, Wilian Guamán 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper compares rule-based and learning-based pricing mechanisms for peer-to-peer (P2P) electricity trading in residential photovoltaic communities. The rule-based benchmarks comprise bill-sharing as an ex post allocation mechanism, the mid-market rate, and supply-demand-ratio pricing. The reinforcement-learning (RL) formulation is implemented through a Deep Q-Network and evaluated under multiplier-based and learnable SDR-shaped pricing, with a fixed-parameter SDR variant as a non-learning control. Performance is assessed through community savings together with complementary financial and operational indicators. In the base PV-only configuration, the rule-based benchmarks outperform the best RL policy. With battery energy storage, evaluated for the RL policies only, community savings under the best RL policy increase from EUR 734.23 to EUR 978.52. Across the learning-based modes and in both configurations, SDR-shaped pricing outperforms the multiplier-based parameterization considered. The results indicate that rule-based pricing remains highly competitive wherever the two families are compared directly, and that storage substantially improves the learning-based outcomes under this accounting, while the distribution of benefits remains heterogeneous across households.

---


### 8. [FORGE: Forward-Only Test-Time Adaptation for Integer-Only Vision Models on Microcontrollers](https://arxiv.org/abs/2609.01683)

**<font color=#1a73e8>作者：</font>** Muhammad Rehan, Haider Ali, Muhammad Ali Munir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision models deployed on microcontrollers (MCUs) are quantized to integer-only arithmetic and run in inference-only runtimes that do not carry the machinery backpropagation needs: the standard tool for adapting a model to the distribution shift (sensor noise, blur, lighting) it meets in the field. Existing forward-only test-time adaptation (TTA) methods either run only on server- or edge-GPU-class models (not true microcontroller integer execution), or require the batch-normalization (BN) layers that integer deployment fuses away. We present a forward-only TTA method that operates on deployed, BN-folded, integer-only convolutional networks. The key observation is that fusing BN into the preceding convolution, a mandatory step for integer inference, destroys the statistics that normalization-based adaptation relies on. We restore adaptation by re-normalizing each folded convolution's per-channel output to its clean training statistics, using only forward-pass estimates. The method (i) recovers most of gradient-based TENT's accuracy gain (+20.9 vs. +24.9 points) and matches forward-only BN adaptation, while being the only method that runs on a folded integer-only model; (ii) needs to adapt only 3 of 21 layers (selected without seeing the test corruptions) to recover 93% of the benefit; (iii) survives single-sample streaming with a batch-size-scaled momentum; and (iv) generalizes across three datasets (up to 200 classes) and two architectures. We validate bit-exact int8 convolution execution and deploy on an ESP32-S3, where, measured with a Nordic PPK2 power profiler, the forward-only adaptation (a lightweight fp32 recalibration around the int8 convolutions) costs only 8.3 mJ (6.8% of inference energy) and 21.9 ms on the deployed SIMD-optimized model: forward-only adaptation is cheap on a real microcontroller.

---


### 9. [Meta-ethics and AI: exploring the novel meta-ethical questions in the era of AI](https://arxiv.org/abs/2609.01685)

**<font color=#1a73e8>作者：</font>** Shang Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the development of artificial intelligence (AI), the landscape of meta-ethics, which has largely centred on human ethics, faces pressures that may significantly reconfigure it. In particular, if future AI systems were to exhibit sufficiently integrated capacities for moral reasoning, moral intentionality, and moral reflection, novel meta-ethical questions would arise concerning what I call "AI's own ethics", as distinct from ethical principles merely imposed on AI by human designers. This paper offers a conditional and methodological framework for identifying the questions that would emerge if such AI systems were to arise. On that basis, the paper distinguishes four domains of meta-ethical inquiry in the era of AI: questions about the nature of human ethics from the human perspective; questions about the nature of AI's own ethics from the human perspective; questions about the nature of human ethics from the AI perspective; and questions about the nature of AI's own ethics from the AI perspective. The paper then considers how some existing mainstream meta-ethical theories (such as cognitivism and non-cognitivism, error theory and success theory, relativism, and objective realism) might illuminate these domains, while arguing that many familiar human-centred formulations of those theories may not transfer straightforwardly to AI cases without substantial revision. The overall conclusion is that the emergence of AI's own ethics would place significant pressure on current frameworks and may require substantial refinement, reconstruction, or reconceptualisation.

---


### 10. [Median-of-Means as an Extremal Convex Estimator and a Nonconvex Route to the Trimmed Oracle](https://arxiv.org/abs/2609.01689)

**<font color=#1a73e8>作者：</font>** Angshul Majumdar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We revisit median-of-means estimation from a deterministic optimization viewpoint and develop a family of block-Lp estimators for robust learning with heavy-tailed and adversarially corrupted data. In a block contamination model with at least a fraction 1 minus epsilon of good blocks, we first show that every convex block M-estimator has worst-case robustness constant at least 1 divided by 1 minus 2 epsilon. This matches the classical median-of-means bound and proves that the trimmed-block oracle constant 1 divided by 1 minus epsilon cannot be attained within the convex class. We then introduce a nonconvex block-Lp family for p between 0 and 1 and derive finite-sample deterministic robustness bounds for all global minimizers. As p decreases from 1 toward 0, these bounds continuously approach the trimmed-block oracle constant. For sufficiently small p, the global minimizers coincide with those of the oracle under a mild separation condition. We also show that the block-Lp objectives have a benign landscape, with all local minima remaining close to the truth and no bad basins. Combining these results with block-level concentration yields sub-Gaussian deviation bounds under finite 2 plus delta moments and high-dimensional extensions to robust mean estimation and sparse regression.

---


### 11. [VirSqueezer: Generating Realistic Deformations and Squeezing Dynamics in VR from Fine-Grained Squeezing Controls](https://arxiv.org/abs/2609.01698)

**<font color=#1a73e8>作者：</font>** Qian Zhang, Xiaoming Chen, Xiaorui Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Squeezing is one of the most natural forms of hand manipulation, inherently involving fine-grained, temporally evolving, per-finger flexion. In VR content creation, squeezing plays a unique role in enabling particular visual effects such as localized deformations and dynamic behaviors, e.g., bursting a Coke can or juicing a fruit, thereby expanding the expressive possibilities of VR content. However, existing techniques, such as 3D Gaussian splatting-based methods and diffusion-based video generation models, are limited in their ability to simulate fine-grained virtual squeezing effects. We introduce VirSqueezer, a framework designed to generate both localized deformations (primary effects) and complex squeezing dynamics, such as rupture and overflow (secondary effects). VirSqueezer captures squeezing control signals using a SenseGlove and provides the user with inferred resistance force feedback during the squeezing process. By estimating object contact areas, inferring physical properties, and simulating physical responses, VirSqueezer computes conditions that guide generation models for visual effect generation, ensuring both visual coherence and temporal synchronization with the simulation. Consequently, VirSqueezer enables the generation of physically realistic visual effects directly from continuous, fine-grained squeezing control signals. Our extensive evaluation demonstrates VirSqueezer's ability to reproduce realistic localized deformations, generate convincing visual dynamics, and maintain consistency in fine-grained squeezing controls.

---


### 12. [Tri-Band Channel Measurement-Enabled Multi-Layer Digital Twin for Terahertz Wireless Data Centers](https://arxiv.org/abs/2609.01699)

**<font color=#1a73e8>作者：</font>** Mingjie Zhu, Ziming Yu, Guangjian Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid growth of AI computing has driven increasing demands for flexible and high-capacity data-center interconnections. Owing to its ultra-wide bandwidth and high spatial reuse capability, terahertz (THz) communication has emerged as a promising solution for future wireless data centers, while digital twins (DTs) enable efficient wireless planning and real-time optimization. In this work, a measurement-driven multi-layer DT framework is proposed for THz wireless data centers, where the physical, channel, evaluation, and manipulation layers are progressively constructed from bottom to top. First, extensive channel measurements are conducted at 140, 220, and 300 GHz to characterize frequency-dependent propagation behaviors. Based on the tri-band measurements, a measurement-calibrated physical twin is established by jointly optimizing the geometry, material, antenna, and hybrid propagation models. On top of the physical twin, a line-of-sight (LoS)-aware implicit neural field is developed to construct an AI channel twin for efficient channel reconstruction. The proposed AI twin learns location-dependent channel statistics from the calibrated twin, enabling real-time prediction of received power and LoS probability. Building upon the reconstructed channel field, a system-level evaluation layer is derived to analyze coverage and interference for both AP-to-rack and rack-to-rack communications. Experimental results show that the proposed AI twin achieves lower power reconstruction error than existing neural-field baselines while maintaining real-time inference capability. Moreover, the ceiling-mounted AP deployment achieves over 90% coverage under a 10 dB signal-to-interference-plus-noise ratio (SINR) threshold, demonstrating the effectiveness of the proposed DT framework for THz wireless data-center planning and optimization.

---


### 13. [Generative Diffusion Surrogates with Analytical Variance Schedule](https://arxiv.org/abs/2609.01705)

**<font color=#1a73e8>作者：</font>** Patrick Reichherzer, Gianluca Gregori, David N. Hosking 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic transport describes physical systems in which an initially structured distribution spreads under unresolved forcing, scattering, or heterogeneous media. Useful surrogates for such systems should be probabilistic, time-resolved, and able to represent non-Gaussian distributional structure. Generative diffusion models, which corrupt data with Gaussian noise and learn a reverse flow back to structured states, have these properties. Their noise schedules, however, are usually chosen heuristically: image and audio generation---the canonical use cases---provide no physical clock. In transport, by contrast, the variance, or mean-square displacement, is often known from macroscopic theory or empirical scaling even when the full distribution is not. Here we prescribe the forward noising rate as the time derivative of this variance, turning generative time into a calibrated transport clock. The variance path is enforced by construction, while the learned score field represents how non-Gaussian structure inherited from entrance data is smoothed along that path, requiring no intermediate-time physical transport data. For ballistic-to-diffusive transport in turbulent plasmas, the surrogate matches test-particle distributions, reproduces the laboratory-measured variance scale, and tracks the simulated kurtosis evolution without schedule tuning, enabling calibrated emulation and likelihood-based inference.

---


### 14. [Hearing the Whispers: Black-Box Membership Inference Attacks on Finetuned TTS Models](https://arxiv.org/abs/2609.01723)

**<font color=#1a73e8>作者：</font>** Kunlin Cai, Kaiyuan Zhang, Zihang Xiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Text-to-Speech (TTS) foundation models are increasingly fine-tuned on private datasets to synthesize highly personalized voices, introducing severe privacy risks by exposing both biometric identities and sensitive speech content. Existing black-box membership inference attacks (MIAs) follow a two-stage pipeline of query generation and representation engineering, both of which face unique challenges when adapted to TTS. For query generation, dual conditioning on synthesis text and reference speech creates a large and underexplored query design space with no established criterion for identifying an effective query. For representation engineering, the multi-level speech characteristics and temporal variability of speech make low-level representations and direct comparisons inadequate for capturing membership signals. To address these challenges, we present the first black-box MIA framework explicitly tailored to TTS models at both the speaker and record levels. For query generation, we characterize the feasible query space and establish two criteria, scorable extent and memorization elicitation, for evaluating five representative queries, identifying recitation as the strongest. For representation engineering, we obtain multi-level speech representations from embedding models and temporally align the generated and target audio for fine-grained comparison. Evaluations across three state-of-the-art TTS models (CosyVoice2, F5-TTS, and XTTS-v2) fine-tuned on two benchmark datasets (VCTK and British Dialect) reveal severe privacy leakage: speaker-level AUC remains above 0.80 and approaches 1.0 in the strongest settings, while record-level AUC ranges from 0.80 to 0.90 and remains effective even in challenging scenarios where both members and non-members are of the same speakers. We further identify speech characteristics associated with disproportionate vulnerability to memorization.

---


### 15. [RecKAN: Kolmogorov-Arnold Networks with a Learnable Recursive Polynomial Basis](https://arxiv.org/abs/2609.01729)

**<font color=#1a73e8>作者：</font>** Amirhosein Azarpour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov--Arnold Networks (KANs) replace the fixed scalar weights of a standard network with learnable univariate functions on each edge, but existing variants still fix the \emph{basis} that those functions are built from: B-splines, Chebyshev polynomials, wavelets, or Jacobi polynomials, and learn only the combination weights over it. We introduce RecKAN, which instead defines the basis itself by a second order polynomial recurrence, $R_{n+1}(x) = (ax^2+bx+c)R_n(x) + (dx+e)R_{n-1}(x)$, whose five coefficients are learned jointly with the network. We show this recurrence recovers several classical polynomial families including both kinds of Chebyshev polynomials, Fibonacci, Pell, and Jacobsthal polynomials as special cases, and prove that its degree grows linearly in $n$ exactly on the sub-family containing all of them, giving a concrete sense in which the learned basis can move beyond any fixed classical choice. Across multiple benchmark datasets spanning image, text, biomedical time series classification, and time series forecasting, RecKAN outperforms three parameter-matched KAN baselines (Chebyshev, Jacobi, and spline based) on all classification tasks and achieves the lowest MSE on the ETTh1 forecasting benchmark. Additionally, when used as a classifier head with a convolutional backbone, RecKAN achieves higher accuracy than standard MLP heads on Fashion MNIST, CIFAR-10, and SVHN. On a synthetic function fitting benchmark it tracks a sharply oscillatory target that a parameter comparable MLP under fits. We further show that the learned recurrence coefficients are interpretable: on the task requiring the most local structure, training moves the basis away from the linear degree growth regime that contains every classical family we identify, consistent with our theoretical analysis of what that structural shift enables.

---


### 16. [SpeakPay: Domain-Adaptive LoRA Fine-Tuning of Whisper for Low-Resource Nepali Financial Speech Recognition](https://arxiv.org/abs/2609.01737)

**<font color=#1a73e8>作者：</font>** Biraj Subedi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mobile payment applications in Nepal are graphically mediated and largely inaccessible to visually impaired users. This paper presents SpeakPay, a voice-first digital wallet, and documents the central technical contribution: a controlled study of domain adaptation for low-resource financial speech recognition. We introduce NepFinSpeech-403, a 403-utterance dataset of Nepali financial voice commands (send, load, and balance operations spanning 237 unique numerals), and fine-tune Whisper large-v2 with LoRA. On the held-out test set, the domain-adapted model reduces Word Error Rate from 129.95% (zero-shot baseline) to 42.58% --- a 67.2% relative reduction --- and improves Devanagari numeral recognition accuracy from 0.0% to 73.9%. We find that word-level metrics understate the practical task-level impact: domain adaptation improves the Transaction Success Rate from 1.67% to 33.33%, a roughly 20x gain. The improvement is consistent at the individual-utterance level (sign test, $p < 10^{-17}$) and across all command types. A data efficiency analysis shows that as few as 100 domain-specific utterances are sufficient to halve the zero-shot WER, with performance plateauing around 300 examples. Error analysis reveals systematic numeral confusion patterns (zero insertion/deletion, prefix hallucination) that account for the majority of remaining transaction failures. The trained system is deployed as a publicly accessible voice-first web application. All code, dataset, model weights, and this paper are released at this https URL.

---


### 17. [UAV Thermal Imagery for Inert Ordnance Screening: Multi Campaign Dataset Development,Object Detection, and Practical Recommendations](https://arxiv.org/abs/2609.01738)

**<font color=#1a73e8>作者：</font>** Chad Melton, PhD., Annabelle Kelton  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unexploded ordnance (UXO) continues to restrict civilian access, agricultural activity, infrastructure recovery, and environmental remediation in contaminated areas around the world. This study created a multi campaign UAV thermal image data set of inert ordnance, developed a labeled image set from collected imagery, tested object detection models, and identified practical considerations for humanitarian mine action and demining applications. Data were collected during four field campaigns in Tennessee under summer and winter conditions using inert mines, munitions, and other ordnance placed in short grass, tall vegetation, gravel, mulch, rock, compost, and compacted surfaces. Thermal imagery was collected under flight altitutes of 33 m and 15 m. The final source inventory contained 5,855 thermal image label pairs, including 918 positive images and 4,937 background images. After retaining all positive images and downsampling background images, the 33 m dataset contained 420 training and 106 validation images, while the 15 m dataset contained 629 training and 157 validation images. YOLOV11l and RT-DETR-R50 algorithms were trained and evaluated to develop an automated candidate detection model. Practical recommendations include collecting thermal and RGB imagery together, incorporating varied surfaces and background only imagery, considering periods following changes in solar exposure, balancing survey coverage against target pixel representation, calibrating models with representative local data, and retaining qualified human review. The intended use is screening and prioritization for follow on technical survey or EOD assessment, and not a standalone clearance.

---


### 18. [ZipTok3D: High-Fidelity 3D Tokenization with Compact Token Prefixes](https://arxiv.org/abs/2609.01740)

**<font color=#1a73e8>作者：</font>** Mingda Lin, Weijie Wang, Zeyu Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compact token sequences are essential for efficient 3D generation. However, existing 3D tokenizers typically organize latent representations either over spatial regions or as fixed-size sets of global tokens, both suffering sharp reconstruction degradation when compressed to extremely low token budgets. In this paper, we present ZipTok3D, a 3D tokenizer designed for high-fidelity reconstruction from extremely short token sequences. Its key idea is to organize object geometry into progressively informative global-token prefixes and unfold these compact representations through iterative decoding. Specifically, nested dropout randomly truncates the latent sequence after encoding during training and requires each retained prefix to reconstruct the complete object, thereby prioritizing essential geometric information in the leading tokens. The decoder then repeatedly applies a parameter-shared Transformer block to recover fine-grained geometry from each prefix without a separate generative sampling stage. With the same token dimension, ZipTok3D achieves reconstruction quality comparable to the 32-token COD-VAE baseline using only one token on ShapeNet and four on TRELLIS, yielding $32\times$ and $8\times$ shorter token sequences, respectively.

---


### 19. [When Can a Machine Trust a Statute? A Survival Certificate for Machine-Extracted Legal Logic](https://arxiv.org/abs/2609.01741)

**<font color=#1a73e8>作者：</font>** Surya Saka  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Statutes are increasingly parsed by machines before people read them, and the parsers disagree: on Missouri's statutes, two independently written extractors diverge on numeric-threshold presence at a false-negative rate of 0.43. We ask what formal logic survives such noise. We build a passive survival certificate for the Duquenne-Guigues implication basis of machine-extracted statutory contexts: per-attribute inter-extractor disagreement is measured, replayed against the basis in 1,000 Monte Carlo trials, and an implication is certified only when a one-sided Wilson 95% lower bound on survival reaches 0.95; every certified implication carries premise spans and a minimal counterexample. On 29,365 Missouri sections and 502 Indian central-Act sections, the preregistered held-out gate passes (10 statute families across 7 Titles exact; 16 across 11 with 5% tolerance), yet under one globally deployed error model 93.2% of held-out chapters fall below the informativeness floor, and a 2x2 factorial assigns that to calibration-rate transfer, not selection. The certificate is usable but fragile: deploy it per-chapter-calibrated or error-tolerant. Code, data products, and the audit trail, including one retracted claim, are released.

---


### 20. [Evidential Deep Learning for Multi-Modal Anti-UAV Detection](https://arxiv.org/abs/2609.01742)

**<font color=#1a73e8>作者：</font>** Dmitry Golovchits, Seyed Sahand Mohammadi Ziabari, Ali Mohammed Mansoor Alsahag  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anti-UAV systems increasingly fuse multiple sensors, yet their detection heads provide no per-modality reliability signal. This study evaluates whether evidential deep learning (EDL) heads, Dempster-Shafer (DS) evidence fusion, and uncertainty-driven temporal sensor gating improve anti-UAV detection through a controlled ablation on three benchmarks: thermal tracking (AntiUAV600), RGB-audio-RF classification (TRIDENT), and RGB-IR tracking (MM-UAV). The EDL training objective improves accuracy over retrained sigmoid baselines (+5.9 percentage points in accuracy and a tripled tracker-on-absent rate in E1; +4.8 percentage points in classification accuracy in E2, surviving a clip-clustered bootstrap, p = 0.011) and ranks classification errors substantially better (entropy UAUC approximately 0.94 vs. 0.51). The remaining components do not support their respective hypotheses. DS fusion does not outperform simple probability averaging. Dirichlet vacuity adds no ranking power beyond predictive entropy and inverts at the detection level, where extreme background imbalance causes it to encode class membership rather than error likelihood, a failure also observed for entropy and sigmoid confidence. Temporal gating preserves accuracy only when nearly inactive and yields no realised latency saving on shared-backbone hardware. The benefit of evidential learning therefore arises primarily from its training objective rather than its uncertainty estimate; a crop-level control further localises the detection-level breakdown to anchor-level evaluation rather than the learned representation.

---


### 21. [SCULPT: Training Edge Vision Models for Post-Training Quantization Readiness](https://arxiv.org/abs/2609.01743)

**<font color=#1a73e8>作者：</font>** Bharadwaj Kavuri, Sourav Babu-PK, Varadhraj Ellapan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Edge vision models are difficult to deploy on resource-constrained hardware, making low-bit post-training quantization (PTQ) attractive. In practice, standard FP32 training often produces heavy-tailed activation distributions whose outliers destabilize activation quantization: preserving the full range wastes quantization bins on rare extremes, while aggressive clipping causes information loss. Existing solutions typically rely on quantization-aware training (QAT), which adds training complexity and bit-width coupling, or advanced PTQ procedures that repair the model after training.
We present SCULPT (Statistical Clipping and Uniform Loss for Post-Training), a training-time method that improves PTQ readiness during ordinary FP32 fine-tuning. SCULPT combines a topology-aware activation regularizer that suppresses quantization-hostile skewness and kurtosis with a stable percentile-based clipping mechanism that learns deployment-ready activation bounds. Unlike QAT, SCULPT does not simulate quantization during optimization; unlike post hoc outlier-repair PTQ methods, it does not require runtime activation transformations. The learned clipping bounds can be exported directly into a standard PTQ workflow for low-bit deployment, including INT8 and lower-bit settings such as W4A8.

---


### 22. [CAT-Flow: Curvature-Adaptive sTeps for Flow Matching](https://arxiv.org/abs/2609.01746)

**<font color=#1a73e8>作者：</font>** Qinchan Li, Pedro Cisneros-Velarde, Keru Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow Matching has emerged as a leading framework for generative modeling, powering state-of-the-art systems such as FLUX and Stable Diffusion 3.5. However, the iterative nature of its ODE-based sampling process creates a fundamental efficiency bottleneck: the quality of generated samples is highly sensitive to the choice of step-sizes, and current models typically require 20 to 30 steps for good quality. In this work, we propose two lightweight, training-free algorithms, CAT-OV and CAT-OT that adapt step-sizes at inference time based on a novel connection between Flow Matching sampling and gradient flow. Our algorithms are computed efficiently by not requiring additional neural function evaluations. Specifically, CAT-OT estimates curvature over time via a finite-difference approximation of the time-derivative of the vector field, while CAT-OV approximates curvature over the state space via a gradient of the vector field. Under suitable conditions, both methods have truncation error bounds of constant order. Empirically, CAT-OV and CAT-OT outperform existing step-size heuristics in image quality metrics across four text- to-image Flow Matching models, reducing the number of generation steps required to reach comparable quality by up to 40%.

---


### 23. [Swin Meets EfficientNet: Lightweight Architectures for GAN-Based Face Forensics](https://arxiv.org/abs/2609.01749)

**<font color=#1a73e8>作者：</font>** Sejuti Basu, Ashima Sood, Vijay Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern generative models, such as GANs, diffusion architectures, and autoregressive systems, now produce facial images that are nearly indistinguishable from authentic photographs. This capability makes detecting forged images increasingly difficult, raising serious concerns about identity theft, fraud, and misinformation campaigns. Our research focuses specifically on GAN-generated synthetic faces, which underpin many face-centric deepfakes, and investigates efficient detection approaches using image analysis alone. Existing detection systems rely heavily on either convolutional neural networks (CNNs) or global vision transformers. While CNNs excel at identifying texture-based local features, they struggle with broader contextual understanding. Traditional Vision Transformer (ViT) models can capture long-range structures effectively, but demand substantial computational resources. Our work explores Swin-Transformer-based architectures across three implementations: a compact Swin Transformer trained from the ground up, ImageNet-1K pre-trained Swin-Tiny and Swin-Small models adapted for binary classification, and a novel hybrid combining EfficientNet-B0's convolutional processing with a Swin Transformer backend. We evaluated all models using the 140K Real and Fake Faces dataset, which includes StyleGAN-generated fake faces alongside authentic images from Flickr and DFDC, with balanced splits for training, validation, and testing. The EfficientNetB0+Swin hybrid achieved 99% accuracy and a 99.44% recall on 5,000 test images, outperforming both pure Swin variants and a previous CNN-only baseline on this dataset. Our results suggest that combining hierarchical CNN features with shifted-window self-attention provides an efficient and computationally lightweight method for detecting GAN-generated synthetic faces.

---


### 24. [A Study of Conditional Diffusion Models for Open-Loop Control under Dry Friction and Stiction](https://arxiv.org/abs/2609.01756)

**<font color=#1a73e8>作者：</font>** Eric Aislan Antonelo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have recently emerged as expressive generative priors for planning and control. This paper studies Action Diffusion, an action-sequence diffusion formulation used as an open-loop proposal distribution for a point-mass system with dry friction and stiction. In this benchmark, motion starts only when the applied input exceeds a static-friction threshold, so effective controls occupy a small and temporally structured subset of the action-sequence space. A compact conditional 1D U-Net generates bounded control sequences conditioned on initial and target states. We compare it with uniform random shooting, random shooting from the same structured dataset prior, and the Cross-Entropy Method (CEM). Results show that Action Diffusion reduces terminal error and stuck steps, especially in low-sample regimes. These results indicate that conditional diffusion provides an effective mechanism for generating temporally coherent control sequences that overcome stiction by conditioning and recombining structured control primitives from the training prior for state-to-state open-loop control.

---


### 25. [Toward Explainable and Policy-Aware AI for Carbon Credit Price Prediction: A Research Framework for Emerging Carbon Markets](https://arxiv.org/abs/2609.01765)

**<font color=#1a73e8>作者：</font>** Summaiya Unnisa Begum, Mohammed Nadeem Ullah, Mohammed Abdul Ghani Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Carbon markets put a price on emissions, yet that price remains hard to forecast. Work in this area clusters on the EU and Chinese schemes, compresses regulatory text into a sentiment score, and reports accuracy without calibration or explanation stability. We distil ten recurring gaps into an impact-feasibility matrix and propose EPA-CarbonNet, a six-layer architecture that fuses market series with policy text by cross-attention and calibrated intervals alongside policy-attributed explanations. We then build and test it on eleven years of daily S and P carbon index data. The findings are largely negative, and reported as measured: a random walk beats the model on five-day RMSE (0.0365 against 0.0475), SHAP rankings agree at rho = 0.54 across resampled backgrounds, and policy attention never coincides with documented regulatory events. Directional accuracy, at 58.6 percent, leads every baseline. Code, data documentation and all result artifacts are available at this https URL

---


### 26. [Emergence of Fibrations, Compression, and Symmetry Breaking in Artificial Neural Networks](https://arxiv.org/abs/2609.01768)

**<font color=#1a73e8>作者：</font>** Osvaldo M Velarde, Lucas C Parra, Alireza Hashemi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial neural networks are often regarded as powerful yet opaque black boxes. Here, we demonstrate that learning in deep neural networks generates local symmetries known in graph theory as fibrations and coverings. We prove that covering symmetries are stable attractors of stochastic gradient descent. Consistent with this theory, we report the emergence of covering symmetries across major network architectures, including multilayer, convolutional, recurrent, and transformer networks. Exploiting these symmetries enables drastic model compression - reducing networks to 17% of their original size without sacrificing performance. Furthermore, controlled breaking of covering symmetry overcomes the loss of plasticity, achieving state-of-the-art performance in continual learning. The theoretical results provide a new foundation for AI systems based on symmetries that convert black boxes into interpretable colored graphs and enable more efficient inference and lifelong learning.

---


### 27. [Allocate Before You Embed: Adaptive Visual Input Allocation for Video Embeddings](https://arxiv.org/abs/2609.01778)

**<font color=#1a73e8>作者：</font>** Song Jin, Zhongtao Jiang, Chenglei Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale video retrieval requires embedding models to encode long and diverse videos under tight visual-input and inference budgets. Existing methods typically sample a small, fixed set of frames at their original resolution, limiting temporal coverage and ignoring frame importance. Our empirical analysis shows that expanding temporal coverage improves retrieval even under a fixed visual-input budget. Gains are larger when the original per-frame resolution is preserved, highlighting the complementary roles of temporal coverage and spatial fidelity. Motivated by this finding, we propose AllocEmbed, an allocate-then-embed framework that reallocates a fixed visual-input budget across more frames. A lightweight allocator uses low-cost previews to assign frame-wise resolutions before the embedding backbone, preserving more detail where it most benefits retrieval while reducing visual cost elsewhere. We further introduce Retrieval-Driven Policy Optimization (RDPO), which learns the allocator directly from retrieval feedback using a rank-validated similarity gap and a confidence-guided efficiency incentive. Operating entirely before the backbone, AllocEmbed integrates with existing retrieval systems without modifying the embedding model or downstream pipeline. Experiments on the MMEB-V2 V-QA and V-RET tasks and our LongRet benchmark show that AllocEmbed achieves the best overall retrieval performance among the evaluated budget-matched methods and transfers across embedding backbones. Our code is publicly available at this https URL.

---


### 28. [Ten Architectures, One Error: Shared Failure Modes in Hyperspectral Classification under Spatially Disjoint Evaluation](https://arxiv.org/abs/2609.01786)

**<font color=#1a73e8>作者：</font>** Ehsan Faghih, Fatemeh Ashrafi, Marguerite Moore 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral image classification still relies heavily on random pixel splits within a single scene. The Salinas dataset, randomly split, is among the most widely used datasets for comparing different architectures. However, under a random split method, a large fraction of test pixels fall immediately adjacent to a training pixel, which inflates reported accuracy. This work introduces a leakage-free evaluation protocol linking spatial separation to the model's receptive field. Applying this protocol across ten different architectures, including classical, spectral, spectral-spatial, transformer, vision-backbone, and state-space families, shows that Macro-F1 drops by 0.147 on average and model rankings change by as many as five places. Furthermore, leakage-free evaluation limits which architectures can be tested on a given benchmark. Since each partition supports patches only within a finite radius, reporting this radius alongside the receptive field is essential for fair comparison. In addition, this study reveals that all ten architectures misclassify largely the same pixels, pointing to a spectral ambiguity in the data that none of them resolves.

---


### 29. [CoViT: Instance-Correspondence Contrastive Learning for Vision Transformer](https://arxiv.org/abs/2609.01787)

**<font color=#1a73e8>作者：</font>** Yisen Wang, Zhirong Wu, Limin Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViT) excel in semantic understanding but fail to discriminate between object instances (e.g., identical embeddings for two dogs), limiting their use in instance-level tasks such as object detection and instance segmentation. We propose Contrastive Vision Transformer (CoViT), a self-supervised learning framework that injects instance-awareness into ViT through geometry-guided contrastive learning. CoViT uniquely coordinates ViT's attention maps and embeddings by constructing triplets: (1) Attention-guided masking: Refine multi-head attention via adaptive thresholding and morphological operations to generate instance masks, identifying foreground anchors; (2) Hardest contrastive mining: For each anchor, computing pairwise embedding similarities to select the intra-instance hardest positive (least similar patch within its mask) and inter-instance hardest negative (most similar patch from other instances), with intra-instance regions masked during negative search. These triplets drive a contrastive loss that simultaneously compresses intra-instance variance and expands inter-instance margins, forcing ViT to discern subtle geometric and appearance differences between instances. CoViT consistently achieves stable performance gains of over 2 AP points across multiple instance-level perception tasks by using ViT as backbone architecture. Notably, CoViT requires no extra decoders or labels, demonstrating that a pure ViT can learn instance-aware representations via inherent attention priors and targeted contrastive constraints. Code and models will be released.

---


### 30. [DESA-TTA: Dynamic EMA and Source Anchoring for Test-Time Adaptation](https://arxiv.org/abs/2609.01795)

**<font color=#1a73e8>作者：</font>** Atif Belal, Lilian Hollard, Marco Pedersoli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language object detectors (VLODs) achieve strong zero-shot performance but remain vulnerable to distribution shifts during deployment. Mean-teacher methods for test-time adaptation (TTA) can improve robustness by updating a student model using teacher-generated pseudo-labels. However, mean-teacher TTA is highly sensitive to the choice of a fixed exponential moving average (EMA) coefficient for teacher updates, and repeated optimization with noisy pseudo-labels can cause cumulative student drift. We propose Dynamic EMA and Source Anchoring for TTA (DESA-TTA), a low-overhead method that jointly regulates teacher updates and student drift through dynamic temporal averaging and source anchoring. Dynamic temporal averaging estimates teacher uncertainty from pseudo-label confidence and box density and uses it to select a sample-wise EMA coefficient within bounds determined by teacher parameter drift. Source anchoring partially restores the updated student parameters toward their pretrained values, with the anchoring strength increasing according to student drift. Experiments across diverse distribution shifts and two VLOD architectures show consistent improvements over existing TTA methods. On VOC-C, DESA-TTA improves AP$_{50}$ by 14.5 points over zero-shot inference while achieving 55\% higher inference throughput than the previous state-of-the-art TTA method for YOLO-World. Our code: this https URL

---


### 31. [Improved Automatic Target Recognition in Synthetic Aperture Sonar Imagery Using Large Deep Neural Networks](https://arxiv.org/abs/2609.01800)

**<font color=#1a73e8>作者：</font>** C.J. Moore, Alex Hurt, Jordan Malof  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic Target Recognition (ATR) in Synthetic Aperture Sonar (SAS) is a task largely dominated by deep neural networks (DNNs). Most SAS-ATR models use convolutional neural network (CNN) architectures whereas transformer-based architectures have had much less representation in the literature despite being state of the art in general computer vision (CV) research. Additionally, researchers have had mixed results in attempting to overcome challenges presented by a scarcity of labeled training data by using methods such as data augmentation and the use of pretrained weights from a variety of imaging modalities. In this work, we compare the performance of modern CNN and transformer-based DNNs to determine which architecture and training configurations elicit the highest performance in SAS-ATR. We investigate how network size, architecture, pretraining method, data augmentation and other forms of regularization affect SAS-ATR performance with a focus on producing the highest-performing model and providing a roadmap for training state-of-the-art SAS-ATR models.

---


### 32. [D-FROST: Decentralized Federated pRompt-tuning via Optimal tranSporT for Non-IID and Imbalanced Data](https://arxiv.org/abs/2609.01802)

**<font color=#1a73e8>作者：</font>** Quan Minh Nguyen, Hoang M. Ngo, Trong Nghia Hoang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prompt tuning provides a parameter-efficient way to adapt foundation models (FMs) by freezing the pretrained backbone and updating only a small set of learnable prompts. This property makes prompt tuning especially suitable for decentralized federated learning (DFL), where exchanging full-model updates can be prohibitively expensive. However, prompt tuning in DFL introduces new challenges. Prompt sets learned from heterogeneous local data may not be index-wise aligned, making standard decentralized averaging unsuitable. In addition, the algorithm should be theoretically guaranteed to achieve consensus and make progress toward the shared objective. In this work, we provide the first study of prompt tuning in DFL. We formulate decentralized prompt tuning as a Wasserstein-based optimization problem over prompt measures, which captures the set-valued structure of prompts. We then propose D-FROST, an optimal-transport-based (OT-based) decentralized prompt-tuning algorithm that merges neighborhood prompts into compact representative prompt sets through transportation-based matching. We further analyze D-FROST by bounding the Wasserstein consensus error across clients, and establishing convergence of the network-level prompt barycenter to a neighborhood of stationarity. Experiments under heterogeneous client data demonstrate the effectiveness of D-FROST for decentralized prompt tuning.

---


### 33. [Consistency as Regularization for Unsupervised Shadow Removal](https://arxiv.org/abs/2609.01806)

**<font color=#1a73e8>作者：</font>** Anh-Kiet Duong, Petra Gomez-Krämer, Jean-Michel Carozza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shadow removal is an important preprocessing step for many vision tasks, yet existing supervised methods require paired shadow and shadow-free images, while unsupervised approaches often still rely on shadow masks or shadow-free references. We propose ShadowCLR, an unsupervised framework that learns shadow removal directly from shadow images. Our key observation is that shadows vary across observations while the underlying scene content remains largely consistent. We therefore use consistency across shadow observations as regularization, encouraging the model to recover scene-consistent appearance while suppressing shadow-specific variations. Global and local consistency further enable us to explore visually related images, learn from imperfectly aligned observations, and focus the representation on shared scene information. Experiments on multiple benchmarks show that ShadowCLR achieves competitive and often superior performance over state-of-the-art unsupervised methods, demonstrating that consistency can provide regularization for shadow removal without shadow masks or shadow-free images.

---


### 34. [Integrated Laser Scanning and Image-Based Topology Optimization Techniques for Detection and Quantification of Visible and Subsurface Structural Defects](https://arxiv.org/abs/2609.01808)

**<font color=#1a73e8>作者：</font>** Mehrdad Shafiei Dizaji, Devin Harris  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable characterization of structural defects requires methods capable of resolving both directly observable surface damage and damage that is not visible from the inspected surface. This study presents two complementary non-contact, vision-based approaches for the detection and quantitative characterization of defects in structural components. The first approach employs high-resolution laser scanning to generate three-dimensional (3D) point clouds of damaged steel specimens. Comparative processing of measured and reference point clouds is used to localize damaged regions, quantify geometric loss, and transfer the measured defect geometry to a finite element representation. The second approach combines full-field surface deformation measurements obtained using three-dimensional digital image correlation (3D-DIC) with finite element model updating and topology optimization. In this inverse framework, measured surface response is used to infer subsurface abnormalities through their influence on the spatial distribution of structural response. Experimental steel-beam specimens containing controlled smooth defects and randomly distributed defects are used to evaluate the approaches. Comparisons with milling-based ground-truth measurements demonstrate that both methods can identify and quantify defect geometry, while providing complementary information for visible and subsurface damage assessment. The combined framework establishes a pathway toward high-fidelity, non-contact structural condition assessment and model updating for components with complex and irregular damage.

---


### 35. [When Does Information Sharing Improve Decentralized Discovery? Aggregation, Independent Rescue, and Equilibrium Selection](https://arxiv.org/abs/2609.01814)

**<font color=#1a73e8>作者：</font>** Yohei Nakajima  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Information sharing can improve a pooled estimate while eliminating independent rescue actions. This paper separates those effects in exact finite discovery models. A centralized action-budget profile shows that equal one-person accuracy can coexist with different portfolio values. Under a registered incremental-sharing protocol, a sharing step improves discovery exactly when pooled residual error contracts faster than an independent rescue attempt. Exact bounded registries exhibit compression, aggregation, neutral curves, and a bounded zero mixed class. In a two-agent Bayesian game with a hidden mixture of common and independent signal sources, the registered selected equilibrium yields a strict positive sharing interval at signal accuracy 3/5, while alternative equilibria show that the result is selection-dependent rather than universal. The models are synthetic and finite; no human or organizational data are used.

---


### 36. [Kirin: Animal Motion Generation from In-the-Wild Video](https://arxiv.org/abs/2609.01823)

**<font color=#1a73e8>作者：</font>** Brian Nlong Zhao, Zhuoyang Pan, James M. Rehg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding animal motion is fundamental to modeling animal behavior and biomechanics, yet progress in this area lags far behind human motion research due to the scarcity of high-quality motion data. While human motion can be captured in controlled environments, it is impractical for most animal species, resulting in small, domain-limited datasets that restrict downstream applications such as animation. To address this challenge, we introduce Kirin, a framework that reconstructs motion from video, learns motion priors at scale, and generates realistic motion that can be directly applied to animated assets. Using large collections of in-the-wild animal videos, we reconstruct 3D motion sequences and pair them with captions to create AiM3D, the first large-scale dataset offering aligned video-text-motion tuples for quadruped animals. Building on this dataset, we develop a visual-guided motion generation model that conditions on both text and image to guide the generation of realistic motion across diverse animal species. Finally, by leveraging an off-the-shelf image-to-3D model, we automatically rig and animate 3D meshes using generated motion, producing ready-to-render animated animals. Together, our dataset and framework establish a new foundation for large-scale, text and image conditioned animal motion generation and animation. Project page: this https URL.

---


### 37. [SliceBridge: context-consistent repair of corrupted slice intervals in T1-weighted MRI](https://arxiv.org/abs/2609.01827)

**<font color=#1a73e8>作者：</font>** Jiheng Li, Michael E. Kim, Trent Schwartz 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structural magnetic resonance imaging (MRI) images are sometimes corrupted over a contiguous set of slices, where acquisition, motion, hardware, or reconstruction effects leave a single slice or short interval inconsistent with its neighbors while the rest of the image remains usable. Such localized corruption can bias downstream morphometric analysis, yet discarding or reacquiring an otherwise usable image is costly. We formulate this as an image restoration problem: given the location of the affected interval, reconstruct those slices from the surrounding anatomical and imaging context. We propose SliceBridge, a framework for restoring corrupted slice intervals in T1-weighted MRI using rectified flow matching conditioned on the surrounding intact slices and their relative slice positions. Through-plane consistency is encouraged by coupling the slices within the interval through interval-correlated initial noise, a shared flow time, and synchronized sampling. The restored interval is then inserted back, leaving all other slices unchanged. We trained and validated the model on 9,877 T1-weighted brain MRI volumes from four datasets and evaluated it on 581 external subjects using clean interval withholding and controlled corruptions. Compared with a matched model that reconstructed target slices independently, SliceBridge reduced error in slice-to-slice changes within repaired intervals by 32.9%-41.3% across interval lengths and achieved higher SSIM at every interval length. In controlled-corruption cases, SliceBridge reduced the median error in regional brain volume estimates produced by a downstream segmentation model from 1.95% in corrupted volumes to 1.05%.

---


### 38. [Differential Games for Compositional Handling of Competing Control Tasks](https://arxiv.org/abs/2609.01838)

**<font color=#1a73e8>作者：</font>** Joshua Shay Kricheli  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We introduce a novel Divide and Conquer control design methodology leveraging differential games in single-agent, multi-objective dynamical systems. The proposed framework associates each control objective with a virtual input and establishes a non-cooperative, finite or infinite horizon differential game among representative players. Each player optimizes a distinct virtual cost function tailored to its specific goal, the full system state, and the other virtual inputs, while accounting for the remaining players' optimal policies. By establishing a Nash Equilibrium for this game, we synthesize a composite controller that achieves a stable balance across competing objectives, providing control engineers with an intuitive and modular framework for parameter re-tuning throughout the design cycle. We provide formal mathematical derivations for both continuous-time and discrete-time dynamical systems, targeting large-scale single-agent applications where complex, dynamically conflicting control objectives make global weighting intractable. To demonstrate the methodology, we developed an open-source Python package implementing a novel numerical algorithm for solving Coupled Algebraic Riccati Equations arising in infinite-horizon differential games. We evaluate the approach on two benchmark case studies: an inverted pendulum on a cart and a non-linear hierarchically controlled quadrotor. The resulting closed-loop performance is compared against the classical Linear Quadratic Regulator (LQR) across various transient and steady-state control metrics, demonstrating superior trajectory tracking and robust multi-objective regulation.

---


### 39. [Import What You Need: Learning When and How to Augment EHR Graphs with External Knowledge](https://arxiv.org/abs/2609.01839)

**<font color=#1a73e8>作者：</font>** Chen Chen, Mohsen Nayebi Kerdabadi, Dongjie Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Longitudinal prediction from electronic health records (EHRs) is limited by the sparsity and irregularity in patient trajectories, and knowledge augmentation with external knowledge graphs (KGs) offers a promising way to alleviate these issues. However, most existing methods perform fixed, context-agnostic topology augmentation by adding the same KG nodes and edges regardless of a patient's evolving state. We propose ReTA, a Reinforcement learning-based dynamic Topology Augmentation framework that casts KG import as a per-visit, budget-aware policy. ReTA first constructs an offline refined pool of KG-grounded templates, then learns a policy to select one augment action per visit from three options: Soft Import, which enriches node features without modifying graph topology, Hard Import, which grafts a compact KG subgraph onto the visit graph to create message-passing shortcuts, and Skip, which leaves the visit unaugmented when the base encoder is already confident. To stabilize learning, ReTA employs a decoupled encoder that processes semantic and structural signals in separate channels and fuses them via adaptive gating. Experiments on MIMIC-III and MIMIC-IV across diagnosis prediction, mortality, and readmission show that ReTA consistently outperforms strong baselines while remaining efficient, transfers across datasets and knowledge graphs, and yields interpretable augmentation patterns. The robust gains under sparse supervision highlight the advantage of ReTA's dynamic decision to import knowledge, boosting accuracy while curbing costs.

---


### 40. [Cite or Decline: A Strict Course-Grounded Chatbot for STEM Lecture Videos](https://arxiv.org/abs/2609.01846)

**<font color=#1a73e8>作者：</font>** S M Masrur Ahmed, Jaspal Subhlok  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recorded lecture videos, often enhanced with search and summarization features, are a standard study resource. However, students cannot easily ask course specific questions or verify answers against an instructor's lecture. We report a semester-long deployment of VideoPoints platform with a retrieval-augmented chatbot that answers from course lecture materials and returns timestamped citations. The chatbot retrieves only from the active course, uses chapter summaries to guide transcript ranking, and returns clickable timestamped citations. Students used it for quick lookups and exam review. Across 833 messages, 70.5% included citations, none crossed a course boundary, and when no lecture evidence matched, the chatbot usually declined rather than answering. Among the users, citations were the most consistently useful feature, while practice-question generation was the strongest unmet request. We also evaluated the design on the real-world test split of EduVidQA, a public multimodal benchmark for lecture-video question answering. Our design improved correct-lecture retrieval by 6.3 percentage points over dense-only retrieval. Together, the results show that effective deployment depends on course isolation, supported citations, and alignment with students' study practices.

---


### 41. [SSAKG 2.0: An Open-Source Package for Structural Associative Sequence Memory and Context-Based Retrieval](https://arxiv.org/abs/2609.01849)

**<font color=#1a73e8>作者：</font>** Przemysław Stokłosa, Janusz A. Starzyk, Paweł Raif  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This article presents SSAKG 2.0, an open-source software package for constructing and operating Structural Sequential Associative Knowledge Graphs (SSAKGs). An SSAKG represents objects as graph vertices and ordered sequences as structural patterns of graph connections. The resulting sparse graph is used as an associative memory in which complete sequences can be reconstructed from a partial, unordered context.
Version 2.0 introduces new algorithms that exploit individual bits of computer memory to efficiently search graph connections. The package is implemented in Python, while performance-critical graph operations are implemented in C and exposed through a Python interface. This hybrid implementation provides a flexible high-level programming environment while reducing the memory and computational overhead associated with large sparse graphs.
The algorithms were evaluated using randomly generated numerical sequences, sequences derived from sentences in the NLTK corpus, and mRNA sequences. The experiments demonstrate the ability of the package to store and reconstruct sequences from partial contexts and provide a basis for evaluating the effects of graph density, sequence length, and memory size on retrieval performance.
SSAKG 2.0 is distributed under the Apache 2.0 open-source license. The package includes documentation and reproducible examples and is publicly available through GitHub and the Python Package Index (PyPI).

---


### 42. [Adversarial Vulnerabilities of Neural Biomarker Identification Systems](https://arxiv.org/abs/2609.01856)

**<font color=#1a73e8>作者：</font>** Polina Tapal, Bryce-Allen Bagley  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> There is growing interest in the proposed use of EEG signals as biometric credentials, but thus far there has been little research on the reliability and security of such biometrics. Prior adversarial tests have focused on deep-learning classifiers and assumed attackers have full access to the classifier model. This has left unexamined other, more popular categories of neural signature methods as well as the more realistic case of an adversary having only black-box access to a classifier. In this paper we develop a collection of adaptive attack algorithms which learn to fool an authentication system via targeted alterations of stolen EEG recordings, without requiring any knowledge of the authentication system itself. Tested on 6 public datasets spanning three recording conditions (reacting to visual stimuli, imagining hand movements, and resting), it reveals that different signaturing approaches vary significantly in their degrees of vulnerability to adversarial attacks. We show that vulnerability to spoofing attack is greatly impacted by the recording conditions, with significant variation depending on task at time of recording. Finally, we provide recommendations for improving neural signature biometrics based on the results of our adversarial testing.

---


### 43. [RAFT-DVC: Resolution-Aware Machine Learning-Based Digital Volume Correlation](https://arxiv.org/abs/2609.01876)

**<font color=#1a73e8>作者：</font>** Zixiang Tong, Lehu Bu, Jin Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital volume correlation (DVC) provides three-dimensional full-field displacement measurements from volumetric images, but how the internal resolution of a machine-learning-based DVC model affects accuracy and operating range remains poorly understood. Here, we present RAFT-DVC, a resolution-aware family of recurrent all-pairs field transforms (RAFT)-based DVC solvers with encoder downsampling factors s = 2, 4, and 8. Using a matched design, we find that the three solvers localize displacement to approximately 0.017 feature-grid voxel, giving an empirical raw-volume error scaling of approximately 0.017s voxel. The solvers exhibit complementary operating regimes governed jointly by displacement reach and volumetric-texture compatibility. Synthetic benchmarks show that RAFT-DVC achieves errors of the same order as tuned classical DVC under fine-texture, small-to-moderate-displacement conditions and becomes competitive or advantageous under coarse-texture, large-displacement conditions. Frequency-swept tests quantify deformation spatial resolution, while tiled inference enables dense estimation on large volumes. Evaluation on confocal volumetric images acquired during indentation illustrates the importance of matching solver operating regime to deformation magnitude and image texture. Tests on micro-CT images of elastomeric foam, despite training only on particle-labeled synthetic data, provide evidence of cross-texture transfer. We also identify coordinate-order inconsistencies in three-dimensional RAFT correlation sampling and introduce a non-cubic impulse test to verify sampler geometry independently of network training. Correcting the sampler improves native-input accuracy and generalization to unseen volume dimensions. Together, these results establish RAFT-DVC as a fast, resolution-aware framework for dense DVC with characterized accuracy and operating regimes.

---


### 44. [SignMatch: Matching Dictionary Signs to Continuous Sign Language Video](https://arxiv.org/abs/2609.01886)

**<font color=#1a73e8>作者：</font>** Ryan Wong, Youngjoon Jang, Liliane Momeni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The objective of this paper is to match dictionary sign videos to corresponding signs in continuous signing videos, where a match is defined by the visual similarity alone - the handshape and motion relative to the body. To achieve this, we learn a prototype-structured sign embedding space from continuous video annotated with signs, where each learnable prototype corresponds to a sign class. Isolated dictionary videos are then mapped into this sign space, enabling the matching between dictionary exemplars and continuous sign instances. This design supports direct dictionary-guided sign matching through embedding similarity and naturally extends to unseen signs using only dictionary exemplars. Experiments on ASL-Citizen dictionary retrieval, ChaLearn OSLWL dictionary-to-continuous sign matching, and using BOBSL's CSLR2 evaluation for automatic sign annotation demonstrate strong generalisation across datasets, tasks and sign languages. Without benchmark-specific supervision, the learned representation transfers effectively across American, British, and Spanish Sign Languages, outperforming prior methods on all three benchmarks. Project page: this https URL

---


### 45. [TAPVid-MV: A Benchmark for Tracking Any Point in 3D Across Multiple Views](https://arxiv.org/abs/2609.01899)

**<font color=#1a73e8>作者：</font>** Skanda Koppula, Frano Rajic, Abdullah Faiz Ur Rahman 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-camera systems are increasingly practical for robotics, AR/VR, and autonomous driving because complementary views reduce depth ambiguity and preserve visibility under occlusion. Existing point-tracking benchmarks, however, focus on a single video or static multi-camera rigs. None test long-term 3D point tracking across several synchronized views under camera motion. We introduce TAPVid-MV (Tracking Any Point in Video across Multiple Views), the first benchmark for this setting. It contains a curated set of 284 sequences, 1,142 calibrated camera streams, and 109,769 point tracks across seven subsets spanning indoor and outdoor domains, from robotics and human activity to driving and synthetic procedural scenes. We obtain these trajectories using dataset-specific auxiliary modalities: sensor depth, LiDAR, SLAM and SfM points, human meshes, posed object meshes, and simulation. Every sequence and trajectory is visually verified by human annotators.
Across more than 30 baselines, no method comes close to solving the task. Surprisingly, existing multi-view point trackers do not consistently outperform monocular point trackers. By evaluating reconstruction and point tracking on the same datasets, TAPVid-MV helps distinguish errors in recovered geometry from errors in point correspondence. Through this joint analysis, we identify geometry recovery as a major bottleneck for accurate 3D point tracking. Beyond multi-view 3D point tracking, our released annotations support monocular 2D and 3D point tracking, future-trajectory prediction, and 4D reconstruction.

---


### 46. [The Ceiling Is in the Channel: Auditing Learner Gaps and Measurement Frontiers in Clinical Prediction](https://arxiv.org/abs/2609.01909)

**<font color=#1a73e8>作者：</font>** Sayeed Shafayet Chowdhury, Nusrat Jahan, Snehasis Mukhopadhyay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical prediction can saturate for two different reasons: a fitted learner may fail to extract available information, or the recorded variables may impose a population frontier. We separate these quantities through the \emph{learner gap} and the \emph{measurement-channel ceiling}. Optimal balanced accuracy is characterized by total-variation separation, yielding architecture invariance, a sharp partial-identification result under replacement contamination, a cross-fitted ceiling estimator, and exact conditions for multimodal decision improvement. We add two finite-sample diagnostics, namely a label-permutation optimism floor and an underfit curve, and validate the audit on three real cohorts: UCI readmission ($n=99{,}343$), BRFSS diabetes ($n=253{,}680$), and NHANES HbA1c ($n=10{,}219$). Well-tuned gradient boosting nearly reaches the estimated frontier in UCI and BRFSS, whereas deliberately or practically deficient learners retain large gaps. NHANES yields a null difference between questionnaire and measured marginal frontiers but a significant joint complementarity gain, refining the simplistic claim that an objective modality must dominate. Across all cohorts, modest AUROC gains coexist with substantially larger Bayes decision-flip rates, and several architectures estimate similar frontiers while their achieved balanced accuracy differs sharply. A PRISMA-guided synthesis of 104 clinical tasks then shows that the same channel-level regularities recur across more than 18 disease categories: a broad but non-universal structured-clinical region, diminishing same-channel gains across model families, and higher performance when measurement channels change. The framework converts saturation from an empirical observation into an auditable decision: improve the learner when headroom remains; improve measurement when it does not.

---


### 47. [Automated Maize Ear Phenotyping Using 3D Reconstructions](https://arxiv.org/abs/2609.01921)

**<font color=#1a73e8>作者：</font>** Ritwesh A. Kumar, Som Tripathi, Peja Matthews 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Maize kernel traits such as row number, kernels per row, and kernel size vary largely for genetic reasons and are consistently associated with regions of the genome that influence yield. Manual measurement of these traits, however, cannot keep pace with the volume of maize generated in a breeding program. To address this, we developed and validated a fully automated pipeline for extracting these traits from 3D point clouds of corn ears, built on a recently developed video-to-point-cloud platform. Raw video frames are processed through COLMAP and NeRF, the ear is isolated via density-based separation, and the point cloud is distance-calibrated to physical units. The calibrated ear point cloud was Z-axis aligned via PCA and cylindrically unwrapped to a 2D image. We enhanced contrast and performed zero-fine-tuning instance segmentation using Cellpose-SAM. A triple-juxtaposed unwrap strategy was used to prevent double-counting at the seam. The pipeline achieved kernel count R^2 = 0.921 (MAPE = 10.33%) and kernel row number within +-2 rows for 95.2% of ears (MAE = 0.75 rows) on a 168-ear held-out set from the 268-ear labeled dataset. The resulting multi-trait dataset has known genotype identity for each ear, positioning it for phenotype-to-genotype association analyses.

---


### 48. [Learning with Volterra Neural Networks: A System Theoretic Perspective](https://arxiv.org/abs/2609.01928)

**<font color=#1a73e8>作者：</font>** Haoyu Yun, Hamid Krim, Yufang Bao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Higher-order interaction components are important for signal, image, and video modeling, but explicit high-order operators often suffer from rapidly increasing parameter and computational costs. This paper presents kVNN, a learnable kernelized Volterra Neural operator for compact higher-order filtering. The motivation is to use kernelization to improve the efficiency of Volterra-type neural operators while providing a structured interpretation of their higher-order components. The proposed formulation combines the order-wise structure of Volterra filtering with learnable polynomial-kernel atoms, allowing different interaction orders to be represented by separate learnable centers and coefficients. This order-decoupled representation avoids explicit high-order tensor parameterization and can be implemented as a CNN-compatible layer. Experiments on representative vision tasks show that kVNN achieves a favorable accuracy--efficiency trade-off.

---


### 49. [OR-Transformer: Scaling Real-Time Decision-Making to 1,000 Items](https://arxiv.org/abs/2609.01933)

**<font color=#1a73e8>作者：</font>** Shuze Daniel Liu, David Simchi-Levi, Claire Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern supply chain operations can require coordinating replenishment across thousands of heterogeneous items under correlated stochastic demand, heterogeneous lead times, and shared fixed ordering costs, yielding observation spaces exceeding $10^4$ dimensions. At this scale, rolling-horizon stochastic mixed-integer linear programs (MILPs) become prohibitively slow, while standard reinforcement learning (RL) methods face increasingly challenging credit assignment in high-dimensional action spaces. We introduce OR-Transformer, a deep reinforcement learning framework for joint replenishment under stochastic demand, with an item-permutation-equivariant Transformer architecture and pathwise-gradient training through the inventory dynamics. Across problem sizes up to 1,024 inventory items, OR-Transformer increasingly outperforms learning-based and rolling-horizon MILP baselines as scale grows. It also reduces online decision-making time by over 4 million times relative to MILP solvers, enabling real-time, large-scale deep RL in supply chain operations.

---


### 50. [Bonded Recourse for Smart-Contract Settlement of Compensable Agent Side Effects](https://arxiv.org/abs/2609.01939)

**<font color=#1a73e8>作者：</font>** Laurent Bindschaedler, Quentin Botha, Christoph Siebenbrunner  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous agent runtimes execute tool actions that mutate databases, repositories, and cloud services across organizational boundaries. Authorization and local compensation cover pre-action admission and in-runtime rollback, but neither settles the residual harm left after a permitted action fails. We design Recourse, a smart-contract settlement protocol for compensable agent side effects that binds each admitted action to scope, recovery, evidence, payout, and collateral. Recourse separates ex ante eligibility from ex post objective settleability: typed receipts make objective residual claims computable under an optimistic-oracle challenge pattern, while subjective or incomplete claims route to ERC-792 arbitration or exclusion. We implement the contract suite, deploy it on Base Sepolia, build adapters against Postgres, Git, and cloud-compatible local sandboxes, and evaluate the system on a deterministic harness, sandbox traces, adversarial sweeps, and property-based fuzzing. Against authorization-only and local-compensation baselines, bonded coverage cuts uncompensated harm. The on-chain tier supplies neutral custody, public challenge, non-cooperative payout, and portable history under cross-organizational trust assumptions.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-187](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
