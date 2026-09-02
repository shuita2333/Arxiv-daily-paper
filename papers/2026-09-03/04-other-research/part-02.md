# 📦 其他研究 | 2026年09月03日

> 本类共 **236** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-236](./part-05.md)

---

### 51. [Adapting Without Gradients: Affine Statistics Transport and What Its Certificate Can Tell You](https://arxiv.org/abs/2609.00374)

**<font color=#1a73e8>作者：</font>** Salim Khazem, Ibrahim Mohamed Serouis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) typically assumes that model parameters can be updated at inference time. This assumption is restrictive for inference-only accelerators, frozen or third-party models, and memory-constrained deployments, and standard BatchNorm-based TTA configurations may also become inactive on architectures without BatchNorm. We study adaptation when the learned model must remain frozen. We introduce CASTER, a gradient-free method that stores source class statistics in a discriminative subspace, estimates a class-shared affine transformation from target-batch moments, and analytically transports the source class distributions before classification. CASTER requires no backward pass, optimizer state, or stored source feature bank. Across four backbones and seven datasets, it outperforms k-NN on identical frozen features in 27 of 28 backbone-dataset settings while retaining a median of 18x less state. Affine transport is not always reliable. On ImageNet-C, where batches contain only 64 samples for 1000 classes, unconditional transport loses 21.2 top-1 points. We therefore introduce an empirical residual-to-margin transportability certificate. Across 307 evaluation cells, every transport losing more than 10 points has certificate value above 3.9, although benign and destructive regimes are not perfectly separated. Gating converts an average $-3.35$-point effect of unconditional transport into a +1.69-point gain, and performance remains within 0.3 points of the best threshold over a broad threshold range. Finally, we show that this certificate is mechanism-specific: when applied to Tent, it accepts only $4.3\%$ of updates and preserves 0.6% of Tent's available gain. These results position CASTER as a lightweight adaptation mechanism for frozen-model deployment, together with an explicit account of when its safety signal is informative and when it is not.

---


### 52. [Neural means and kernel corrections for operator learning](https://arxiv.org/abs/2609.00389)

**<font color=#1a73e8>作者：</font>** Yitzchak Shmalo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We combine neural network means with exact Matérn kernel regressions of their residuals and of their learned features, and evaluate the pairing on two public emulation problems with published baselines: the structural-mechanics benchmark of de Hoop et al. and the OCO-2 radiative-transfer emulator of Lamminpää et al. On structural mechanics the combination reaches 4.55% test error, matching the best published architecture, and 5.38% against a published 6.49% in the low-data regime. On OCO-2 it improves on the published Gaussian-process emulator on that problem's own test points, outright on two of the three spectral bands; the same kernel that trails the network tenfold on the raw state overtakes it on the network's features, and we measure why (the target's squared native-space norm drops about fortyfold at fixed effective dimension) and prove the mechanism. Where the two families tie instead, the residuals of every architecture we train correlate above 0.86 and their shared component is flat in diversity and sample size, which reads the published plateau as a property of the data. Supporting results include a second-moment identity that predicts stacking outcomes from measured correlations, an optimal-recovery certificate, and a distribution-free coverage band, the only uncertainty signal that survives our tests.

---


### 53. [NeuroPriv: Adversarial Representation Learning for Privacy in Wearable EEG Systems](https://arxiv.org/abs/2609.00390)

**<font color=#1a73e8>作者：</font>** Sarmistha Sarna Gomasta, Bhawana Chhaglani, Prashant Shenoy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Wearable EEG systems may expose sensitive information beyond their intended health function, creating substantial risks to neuroprivacy. In this work, we show that commonly used EEG features can reveal participant identity and demographic attributes in addition to supporting the intended cognitive task. Wearable EEG is increasingly being explored for cognitive monitoring, neurological assessment, and longitudinal digital-health applications, yet many systems assume that transmitting compact spectral or spatial features instead of raw EEG provides sufficient privacy protection. Using EEGMAT as a motivating case study, we find that compact EEG features achieve a balanced accuracy of 0.788 for cognitive-state classification while enabling gender, age, and subject-identity inference with balanced accuracies of 0.858, 0.789, and 0.692, respectively. We further show that privacy-aware representation learning preserves task performance at 0.781 while reducing these inference accuracies to 0.563, 0.467, and 0.206. These findings motivate purpose-limited representations and explicit privacy auditing in wearable neurohealth systems.

---


### 54. [A Multi-Branch Feature Fusion Approach for Health Misinformation Detection and Propagation](https://arxiv.org/abs/2609.00403)

**<font color=#1a73e8>作者：</font>** Mkululi Sikosana, Sean Maudsley-Barton, Oluwaseun Ajao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a multi-branch fusion framework for detecting and characterising the propagation of health misinformation in online social networks (OSNs). Grounded in the Elaboration Likelihood Model (ELM) and the Theory of Planned Behaviour (TPB), the model fuses transformer-based semantics with rhetorical cues, stance representations, and psychologically motivated proxies in a unified multi-task architecture. In addition to binary classification, we introduce the Cognitive Propagation Score (CPS), an interpretable post-hoc auxiliary score computed from psychologically motivated, text-derived cues capturing argument complexity, emotional intensity, and content-derived virality potential, to support diffusion-risk reasoning when engagement ground truth is incomplete or unavailable. Experiments on three benchmark datasets, Constraint, COVID--19\_FNIR, and Monkeypox, show strong classification performance, achieving ROC--AUC up to 0.9999 on COVID--19\_FNIR, while propagation-oriented ranking achieves near-perfect agreement when engagement-derived supervision is available (Monkeypox, Spearman's $\rho = 0.9952$) and similarly high ranking alignment under proxy-based supervision on COVID--19\_FNIR ($\rho = 0.9954$). Compared with representative literature baselines, the fusion model improves detection on Constraint and COVID--19\_FNIR, while Monkeypox remains more challenging, reflecting domain- and signal-specific differences. Ablation analysis further indicates that psychological and rhetorical branches provide complementary gains beyond semantic embeddings. Overall, the framework bridges cognitive theory and neural modelling to improve transparency and to support scalable misinformation monitoring, with future work required to validate CPS against human-centred diffusion judgements.

---


### 55. [FocusBuddy: Encouraging Healthy Desk-Work Habits by Caring for a Virtual Pet on a Water Bottle](https://arxiv.org/abs/2609.00412)

**<font color=#1a73e8>作者：</font>** Mohamed Ouf, Rowan Hussein  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People who study or work at a desk sit for long uninterrupted periods and drink less water than they intend to. Software reminders address both problems but are easy to dismiss and easy to resent. We present FocusBuddy, a proof-of-concept fabric case that wraps a standard water bottle and houses a microcontroller, environmental sensors, and a small display showing a virtual pet. The pet's condition mirrors the user's self-care: drinking water feeds the pet, standing up to move plays with it, and refilling an empty bottle cleans it. Twenty undergraduate students used FocusBuddy for two weeks during their regular coursework and completed a written interview. Self-reported water intake rose from a median of 3 to 4 cups per day, movement episodes rose from 2 to 4 per day, and interviews surfaced two tensions: that wellness prompts must respect focused work, and that pet neglect can convert a wellness prompt into a source of guilt. We contribute the prototype, first-deployment evidence of healthy-direction shifts in self-reported habits, and design implications for emotionally framed wellness devices.

---


### 56. [How Temporal Correlations Shape Memory in Linear Recurrent Neural Networks](https://arxiv.org/abs/2609.00420)

**<font color=#1a73e8>作者：</font>** Arnol Manuel Fokam, Fasseu Sieyondji Akpevwoghene, Edem Fiifi Dawson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The linear recurrent neural network (LRNN) is a simple model for studying how much memory a network builds up as it trains. For uncorrelated inputs, earlier work found that training itself settles the network between keeping the past and reacting only to the present. Real sequences are correlated, and we solve the learning dynamics exactly for correlated inputs. In the solution, keeping the past carries a cost. The whole effect of correlation lands on that cost. This cost reduces to the earlier one when inputs are uncorrelated and grows once they are positively correlated. Three findings follow. (1) Correlation reshapes the course of learning, not only its end. Memory builds, overshoots, and is partly removed, and the settled network keeps less of the past. (2) Memory switches off at a threshold set by one number, how much each input resembles the one just before it. Neither sequence length nor longer-range correlation moves this threshold. Memory is worth keeping only when the task needs the previous input more than the current input already supplies it through correlation with the past. (3) The best network changes too. Zero error demands a feedthrough, a path that passes the current input straight to the network's output and remembers nothing, and training builds it unprompted when given one spare hidden dimension. Our work turns one property of the input into a prediction of whether a network learns memory and explains why correlated data turns recurrent networks into change detectors.

---


### 57. [ErgoAssist: Cognition-Aware Posture Feedback in Wearable Ergonomic Systems](https://arxiv.org/abs/2609.00440)

**<font color=#1a73e8>作者：</font>** Sarmistha Sarna Gomasta, Bhawana Chhaglani, VP Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Prolonged digital device use has made poor posture and musculoskeletal discomfort pervasive among knowl- edge workers. Existing ergonomic wearables rely solely on posture thresholds, frequently interrupting users during high-focus moments and leading to alert fatigue and abandonment. Yet posture and cognitive load are closely coupled, and most systems remain cognitively unaware. We present ErgoAssist, a head-worn ergonomic assistant that detects poor posture using IMU-based head tracking and estimates task-induced cognitive load using a consumer-grade EEG headband for continuous everyday use. In a controlled lab study, ErgoAssist achieves 81% posture classification and 90.2% task induced cognitive load estimation accuracy under leave-one-subject-out evaluation. In a preliminary real-time deployment, cognition-aware alerting reduces alert frequency by 81%, improves perceived usability by 43%, task performance by 25%, and improves posture correction rate by 38%, delivering fewer but better-timed interventions rather than merely suppressing alerts.

---


### 58. [CRAD: Class-wise Reliability-Aware Distillation for Decentralized Heterogeneous Federated Learning](https://arxiv.org/abs/2609.00446)

**<font color=#1a73e8>作者：</font>** Baraa Bilbeisi, Mengchen Fan, Baocheng Geng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional federated learning (FL) relies on parameter averaging, which forces clients to be doubly homogeneous: it demands an identical architecture and degrades under non-IID data. Real-world deployments usually break both assumptions. We sidestep both by building a decentralized knowledge distillation framework in which each client evaluates its peers' model snapshots on its own local data and distills from the resulting soft predictions. Because knowledge is transferred through the shared class posterior, clients are free to run different architectures; and because every teacher is evaluated on the student's own device, raw data never leaves the client, with no central server or public dataset required. Within this setting, we identify and address an under-examined problem: how to combine the peer teacher predictions. Existing methods, like uniform averaging, ignore how knowledge reliability varies across teachers and classes. We propose Class-wise Reliability-Aware Distillation (CRAD), which, per class, first discards teachers that disagree with the peer consensus and then takes a weighted average of the rest, weighting each teacher by its per-class reliability (precision, or inverse variance). Since the variance of an accuracy from $n$ samples scales as $1/n$, support enters automatically: among the teachers that survive filtering, a teacher is trusted for a class to the degree that it is both accurate and well-evidenced for it. On three image-classification benchmarks (CIFAR-10, CIFAR-100, and PathMNIST colon pathology), across heterogeneous architectures under severe non-IID skew, CRAD consistently outperforms competing methods in global accuracy.

---


### 59. [Instance-Guided Report Anchoring for Text-Free 3D Abnormality Segmentation in Chest CT](https://arxiv.org/abs/2609.00447)

**<font color=#1a73e8>作者：</font>** Zhenyu Bu, Haoyan Ding, Chushu Shen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D abnormality segmentation in chest CT requires dense spatial supervision, but obtaining expert voxel-level labels is costly. Radiology reports, however, are routinely generated during clinical interpretation and contain instance-specific descriptions that can provide additional guidance without new dense annotation. Existing vision-language grounding methods typically require report-derived findings at inference, making localization dependent on paired text and limiting each forward pass to a queried finding. We propose Instance-Guided Report Anchoring (IGRA), a model-agnostic module that preserves the correspondence between each annotated abnormality instance and the report finding that describes it. IGRA pools each instance representation and anchors it to the corresponding finding embedding during training; all text-related components are discarded at inference. We further reformulate free-text grounding on ReXGroundingCT as multi-label volumetric segmentation by merging same-category instances, allowing all abnormality categories to be predicted in one image-only forward pass. IGRA improves Dice by 22.5% over the strongest image-only baseline (30.93 vs. 25.25) and is comparable to VoxTell on the single-finding subset (30.29 vs. 30.43). Applied unchanged to four standard 3D segmentation backbones, IGRA improves Dice and hit rate across all architectures. Zero-shot evaluation on LIDC-IDRI, PleThora, and a private in-house dataset further shows consistent gains over image-only baselines.

---


### 60. [Toppling the Hierarchy in Byte-level Language Modeling](https://arxiv.org/abs/2609.00463)

**<font color=#1a73e8>作者：</font>** Lukas Edman, Alexander Fraser  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work examines recent byte-level models and their failure to perfectly manipulate characters. State-of-the-art byte-level models use a hierarchical structure, starting at the byte level, downsampling to the word level, and then upsampling back to bytes. While this improves training and inference efficiency, we find that the hierarchical design itself limits character-level understanding, with pure byte-level models consistently outperforming hierarchical variants on character manipulation tasks. Ablating transformer layers into attention and feed-forward components further reveals that byte-level attention is the primary mechanism driving this behavior. Together, our results provide an explanation for the character-level failures of hierarchical byte models and establish a clear trade-off between computational efficiency and fine-grained character understanding.

---


### 61. [Does Reasoning Mitigate Backdoor Attacks? A Neuro-Symbolic Perspective](https://arxiv.org/abs/2609.00464)

**<font color=#1a73e8>作者：</font>** Marco Antonio Corallo, Andrea Agiollo, Mauro Conti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Neuro-Symbolic (NeSy) AI has recently emerged as a novel paradigm to enable trustworthy AI, aiming at integrating sub-symbolic neural perception with grounded symbolic reasoning. The neuro-symbolic integration process that characterizes these models has been proven beneficial to achieve more transparent, explainable and efficient AI systems. Meanwhile, their properties under adversarial settings have been overlooked being frequently deemed robust-by-design. However, the neural-symbolic integration process they leverage constitutes an additional layer of complexity that may provide an attack entry-point. Therefore, in this paper, we claim that an in-depth investigation of the adversarial robustness of NeSy models is necessary and provide the first systematic evaluation of backdoor attacks against NeSy. To this end, we compare the most popular NeSy framework, namely DeepProbLog, against baseline neural networks across a total of eight backdoor settings and four reasoning tasks. Our experimental results show that while NeSy models are indeed more robust than their neural counterpart on average, their robustness vastly depend on the strictness of the reasoning process being enforced and its compatibility with the chosen adversarial target. The source code to reproduce our experiments is made available at this https URL.

---


### 62. [Higher Structures in Deep Learning](https://arxiv.org/abs/2609.00472)

**<font color=#1a73e8>作者：</font>** Michael L. Roberts, Carlos Zapata Carratalá. Nicholas J. Cooper, Lijun Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We provide an expository introduction on the importance of higher-arity tensor operations to deep learning. Then, we conduct a novel empirical investigation of higher-arity phenomenon in trained neural networks, introduce a hypergraphical generalization of the multilayer perceptron, and explore connections to evolutionary algorithms. We conclude with a discussion of promising directions for future research.

---


### 63. [Design principles to Increase Technology Self-efficacy for Older Australians with Mild Cognitive Impairment (MCI) and Older Carers](https://arxiv.org/abs/2609.00480)

**<font color=#1a73e8>作者：</font>** Snezna Bizilj Schmidt, Nathan D'Cunha, Stephen Isbel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The number of people with age related physical or cognitive impairments is increasing due to the worlds ageing population. Technology has the potential to support independent living, and to achieve aged and health service efficiencies, however, there are gaps in our understanding of factors that motivate technology adoption and ongoing use by older adults, especially those with cognitive impairments. This study aims to explore motivators and enablers for technology adoption and ongoing use by older Australians with mild cognitive impairment (MCI) and their carers, to identify technology design principles and guidelines that maximise adoption. Semi structured interviews were used to gather data about individual demographics, needs, priorities, lifestyle, challenges, and experiences with technology. Results of inductive, reflective, thematic analysis indicate that a desire for independence, autonomy and quality of life motivate use of technology, and perceived technology self-efficacy and IT literacy are enablers. The Protection Motivation Theory illustrates that constant technology change is a disabler for technology adoption and sustained use, because it lowers perceived technology self-efficacy and IT literacy, and reduces confidence to use technology. Two high-level technology design principles and related guidelines are proposed, grounded in theory and aligned with Banduras four sources of self-efficacy. These design principles and guidelines are intended to increase feelings of self-efficacy and confident use of technology, while also reducing adverse impacts of technological change and encouraging sustained technology adoption by older adults with MCI to support independent living and quality of life.

---


### 64. [AdaptNTK: Adaptive Uncertainty Quantification and Active Learning for Neural Network Potentials](https://arxiv.org/abs/2609.00488)

**<font color=#1a73e8>作者：</font>** Prajwal Ananth, Shuwen Yue  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning interatomic potentials bridge the gap between quantum chemical precision and classical computational speed, enabling molecular dynamics simulations with first-principles accuracy. Their reliability is often improved through active learning, which iteratively expands the training set by identifying uncertain, out-of-distribution configurations. Existing uncertainty-quantification methods often involve a trade-off between computational cost and reliability, and generally cannot account for redundancy as an acquisition batch is assembled. Here, we introduce AdaptNTK, a single-model framework that measures uncertainty as a regularized Mahalanobis distance in empirical neural tangent kernel (NTK) feature space. With the NTK features fixed during acquisition, the uncertainty depends on the acquired configurations but not their reference labels. This allows the uncertainty to be updated recursively after each selection without retraining, reducing redundancy within an acquisition batch. On held-out rMD17 data, AdaptNTK achieves the highest mean correlations with force errors (Spearman 0.68, Pearson 0.71) and matches a three-member ensemble in error retention. In active learning experiments, AdaptNTK achieves the lowest force errors across rMD17 and Transition-1X, with particularly strong performance on transition-state configurations in Transition-1X. AdaptNTK provides a 2.6-fold speedup per Transition-1X cycle relative to the ensemble, providing efficient single-model uncertainty estimation with sequential updates for data-efficient active learning.

---


### 65. [A hybrid quantum-classical neural network for learning to route](https://arxiv.org/abs/2609.00489)

**<font color=#1a73e8>作者：</font>** Marcus Rolf Peter Ritt, Alexsandro Santos da Rosa Júnior, Marcos Vinicius Reballo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work studies hybrid quantum-classical neural networks for learning routing heuristics. Specifically, this paper asks whether small quantum neural networks can replace parameter-heavy modules inside a competitive attention-based routing model while maintaining solution quality. For the capacitated vehicle routing problem, encoder feed-forward replacement emerges as the most promising design: it reduces the number of model parameters by 56.6% while keeping the hybrid model close to the classical neural baseline at small and medium instance sizes, although the gap grows for larger instances. This work also compares to classical routing algorithms, which remain highly competitive and often superior on the fixed Euclidean test sets. Our results therefore do not indicate quantum advantage or solver dominance, but identify encoder feed-forward replacement as a viable hybrid-module compression strategy for neural combinatorial optimization.

---


### 66. [UniScale: Exploring Unimanual Gesture Mapping Strategies for Gaze+Pinch-based Scaling Interaction](https://arxiv.org/abs/2609.00500)

**<font color=#1a73e8>作者：</font>** Kyoungwhan Mheen, Jinwook Kim, Sang Ho Yoon  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Object scaling serves as a fundamental spatial manipulation that enables complex and productive tasks in XR environments. This paper investigates unimanual scaling techniques for XR using gaze and hand interactions. We propose UniScale, a set of unimanual alternatives to the standard bimanual pinch, allowing users to scale objects while preserving hand availability for concurrent spatial manipulations. We design five distinct mapping strategies based on physical metaphors, exploring unimanual control that varies depth, angle, micro-gestures, and finger-distance input. We then compare these techniques against a standard bimanual baseline, in which users adjust the inter-hand distance via a bimanual pinch gesture. In a user study, we evaluate their effectiveness in a 3D object scaling task under both clutching and clutching-free conditions. The results indicate that while bimanual scaling relies on clutching for stable control, unimanual techniques excel in clutching-free conditions, significantly reducing physical hand movement. From the results, we derive valuable design implications for developing efficient 3D multimodal interactions in XR.

---


### 67. [GlitchLab: A Hardware-in-the-Loop Optimizer for Physical Fault Injection](https://arxiv.org/abs/2609.00502)

**<font color=#1a73e8>作者：</font>** Tanvir Hossain, Abhinav Mahadevan, Jasper Van Woudenberg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Physical fault injection can turn brief hardware disturbances into security failures such as key recovery, authentication bypass, and unintended control flow. Finding effective faults is difficult because many interacting parameters create a large search space, successful settings are sparse and target-dependent, and each hardware attempt provides limited feedback. Under fixed testing time, efficient search is therefore critical for assessing fault sensitivity.
We present GlitchLab, an online hardware-in-the-loop platform that treats delay as a timing gate, voltage and pulse duration as severity controls, and hardware outcomes as structured feedback. It implements RL-Q (Q-learning-based reinforcement learning), a structured bandit for discovery, and Structured-Outcome-Based Adaptive Search (SOBAS), a model-based policy for fault reproduction.
Both policies find a target fault in every AES, password, and control-flow campaign. On AES and control flow, they require 2-85x fewer attempts and 26-1,237x less time than the baselines; on password, both succeed while the baselines fail within 5,000 attempts. After discovery, SOBAS reproduces faults 7.3-21x more often, while RL-Q identifies 30% more distinct AES settings.

---


### 68. [Wave Function Backpropagation with Explicit Temporal-Interval Dynamics](https://arxiv.org/abs/2609.00503)

**<font color=#1a73e8>作者：</font>** Byunggu Yu, Justin Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conventional neural networks learn predominantly through affine transformations followed by nonlinear activations, while elapsed time is often treated as an auxiliary feature or assumed to be uniformly sampled. This paper introduces Wave Function Backpropagation (WFB), a wave-parameterized learning formulation in which neural responses are represented by learnable amplitude, wavenumber, angular frequency, and phase. The formulation associates an observed state with its temporal interval Delta t through the phase of a differentiable spatiotemporal wave. We derive standard WFB gradients and a spatial-curvature correction based on the Laplacian of the wave response. WFB is instantiated in a deliberately feed-forward trajectory predictor to provide a controlled proof of concept; sequence learning is outside the scope of the present evaluation. With motion features, STD-WFB using real intervals reduces average displacement error (ADE) by 20.4% relative to the original FFN baseline. In a new position-only evaluation that removes temporal leakage through precomputed velocity and acceleration, real-interval WFB reduces ADE by 10.4% relative to the original FFN and remains competitive with parameter-matched ReLU controls, obtaining 2.1% lower mean ADE than the matched FFN with explicit Delta t. Shuffled-interval WFB attains the lowest mean ADE, indicating that the present evidence supports the effectiveness of the wave representation but does not attribute the gain to interval alignment. These results establish WFB as a viable structured feed-forward learning formulation and define a clear basis for subsequent architectural studies.

---


### 69. [VATO: A Vortex-Force-Aware Transformer Operator for Unsteady Separated Aerofoil Flows](https://arxiv.org/abs/2609.00507)

**<font color=#1a73e8>作者：</font>** Xingxin Yang, Zhan Zhang, Yichen Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of unsteady separated flows is challenging because the aerodynamic loads depend on nonlinear separation and vortex-shedding dynamics. Although high-fidelity CFD resolves these mechanisms, its cost limits repeated use in design and control. Standard field-level surrogate training, however, does not distinguish the flow regions that contribute most strongly to the aerodynamic loads. We introduce VATO (Vortex-Force-Aware Transformer Operator), which couples the Vortex Force Map (VFM) method to a geometry-aware neural operator through two complementary mechanisms. VATO-S adds training-only supervision of the local VFM force-contribution field, with no increase in model size or inference cost. VATO-A uses VFM contribution and sensitivity fields to prioritise force-relevant source locations for residual cross attention. The methods are evaluated on unsteady CFD data for double-edged-plate aerofoils over 54 trajectories from nine geometries. Over lead times of 1-20~ms, VATO-S reduces velocity, pressure, and vorticity errors by 10.4\%, 1.0\%, and 15.6\%, respectively, while VATO-A achieves reductions of 15.8\%, 7.5\%, and 31.2\%. VATO-S gives the lowest VFM-derived drag error, whereas VATO-A gives the lowest pressure-derived lift and drag errors. Over lead times extending 50\% beyond the training range, VATO-A retains a 26.9\% reduction in vorticity error and larger improvements in all four force readouts, despite reduced gains in velocity and pressure. These results show that force-aware operator learning can improve both flow-field prediction and aerodynamic functional accuracy in unsteady separated flows.

---


### 70. [CoVer: Conflict-Aware Claim Verification](https://arxiv.org/abs/2609.00508)

**<font color=#1a73e8>作者：</font>** Shuning Zhang, Dai Shi, Bohao Chu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Social media fact-checking has long been challenged by evidence-level and aggregation-level conflicts, where erroneous evidence mimics authoritative news sources. To capture this challenge and support conflict verification tasks, we present ContraNote, a large-scale real-world dataset curated from X's Community Notes system. It includes 33,686 posts for evaluating evidence-level conflict resolution, and 54,474 instances for evaluating aggregation-level prioritization. Additionally, we propose CoVer, a factual adjudication framework with three-stage pipelines: evidence schema normalization, factual consensus and support verification. This prioritizes evidence over noise to prevent it from compromising the final verdict. Technical evaluations show that CoVer achieves strong performance compared with state-of-the-art baselines across ContraNote (86.0% Acc., 68.0% mac. F1, 64.5 bal. Acc. on Conflict; and 88.5% Acc., 88.5 mac. F1 and 89.2 bal. Acc. on Prioritization), CONFACT-HumC (88.4% Acc.) and CONFACT-ModC (89.4% Acc.).

---


### 71. [When the Algorithm Becomes the Brand Crisis: A Sociotechnical Theory of Distributed Responsibility and Accountable Transparency](https://arxiv.org/abs/2609.00510)

**<font color=#1a73e8>作者：</font>** Mohammad Saleh Torkestani, Taha Mansouri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence systems increasingly enact market-facing promises through chatbots, recommendation systems, automated decisions, and generative interfaces. Their failures, misuse, and misrepresentation raise a question that conventional brand-crisis models do not fully specify: how do stakeholders assign responsibility when technical causation, customer-facing control, and governance duties are distributed across an AI system, developer, deployer, vendor, and user? This conceptual paper develops a sociotechnical process theory from a structured, federated scoping synthesis of verified academic and primary sources. It distinguishes an AI/algorithmic incident from an AI-related organisational crisis and, in turn, from an AI-related organisational scandal. The framework proposes that incident configuration shapes actor-specific attribution; attribution informs capability, integrity, fairness, and relationship appraisals; and public moralisation may, but need not, escalate an incident into scandal. The theory offers a reconciliation of findings that algorithm involvement can buffer negative brand reactions in some settings while robot and chatbot failures can redirect responsibility to an associated firm in others. It introduces accountable transparency as a proposed response configuration that combines timely notice, an intelligible account, role-responsibility acknowledgement, remedy, evidence of correction, and recourse. The evidence supports conditional, proximal inferences about blame, trust, satisfaction, firm evaluation, and communication credibility more strongly than claims about durable reputation, brand equity, or market performance.

---


### 72. [Soft-Argmax for the Projective Plane via the Veronese Embedding](https://arxiv.org/abs/2609.00521)

**<font color=#1a73e8>作者：</font>** Benjamin El-Zein, Dominik Eckert, Paul Zech 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> From horizon detection to fibre structures in X-ray imaging, many vision tasks recover lines via peak detection in Hough space $H=S^1\times\mathbb{R}$, the domain of orientation-offset pairs $(\theta,\rho)$. Differentiable pipelines extract coordinates via \emph{soft-argmax}, a probability-weighted average that is only meaningful in a globally linear space. However, $(\theta,\rho)$ and $(\theta+\pi,-\rho)$ describe the same undirected line, so $H$ double-covers the space of undirected lines $H/\mathbb{Z}_2$: a Möbius strip, obtained by identifying each pair under $\mathbb{Z}_2$ action. Soft-argmax operates on the cover $H$, but since $H/\mathbb{Z}_2$ admits no linear structure, it tears geometrically adjacent lines apart. Thus we need a $\mathbb{Z}_2$-invariant embedding of lines into a linear space, on which soft-argmax is well-defined. We achieve this by parametrising lines via unit-norm homogeneous vectors $\ell=(1+\rho^2)^{-1/2}(\cos\theta,\sin\theta,-\rho)^{\top}\in\mathbb{R}^3$ and applying the Veronese map $v_2(\ell)=\ell\ell^{\top}$ that satisfies $v_2(\ell)=v_2(-\ell)$. This descends continuously to an embedding of the quotient $H/\mathbb{Z}_2$ into the linear space $\mathrm{Sym}^2(\mathbb{R}^3)$, where the antipodal ambiguity vanishes. Line extraction becomes a barycentre in $\mathrm{Sym}^2(\mathbb{R}^3)$, projected back via its leading eigenvector. We validate our \emph{Veronese soft-argmax} in a Hough transform-based network across all resolvable lines, confirming uniform and seam-free recovery. We further derive that the $L_2$-loss on isometrically weighted Veronese embeddings equals the squared chordal distance between lines in projective space, enabling a geometrically precise training objective.

---


### 73. [GenScale: A Benchmark for Relative Object Scale in Image Generation and Editing](https://arxiv.org/abs/2609.00525)

**<font color=#1a73e8>作者：</font>** Lingxiao Li, Max Whitton, Ledell Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image generation and editing systems can produce photorealistic, prompt-aligned images, but still often render familiar objects at implausible relative sizes. To measure this failure mode, we introduce GenScale, a benchmark and evaluation protocol for real-world relative object scale in image generation and editing. GenScale contains 900 image-level entries and 1,643 pairwise anchor-target scale relations across common-object generation, human-product generation with metric dimensions, and scale correction from failed generations. We further design a human-calibrated ordinal judge for scalable pairwise scale evaluation. Last but not the least, we introduce Rescale, a model-agnostic post-processing agent for localized scale correction without modifying the source generator. Experiments reveal that state-of-the-art image generators and editors cannot reliably observe relative scale yet, while Rescale consistently improves scale plausibility across generated and edited images. Together, GenScale establishes relative object scale as a distinct, measurable, and actionable capability for image generation systems.

---


### 74. [Learning Feasibility-Aware Latent Spaces for Preference-Based Exploration of Procedural Automotive Wheel Designs](https://arxiv.org/abs/2609.00527)

**<font color=#1a73e8>作者：</font>** Takashi Owaki, Yuki Koyama, Tomoyasu Nakano 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Intelligent design interfaces that rely on preference-based optimization are most useful when their suggestions are both meaningful to users and feasible within the target domain. Procedural models offer compact and editable design spaces, but their native parameters can be entangled and can generate many invalid outputs, causing human-in-the-loop optimizers to waste comparisons. We propose an interaction-oriented representation-learning pipeline for procedural models and study it in automotive wheel design. The method first screens procedurally generated samples using geometric rules and finite-element analysis, then learns a reduced latent space from the screened subset. We further introduce supervised functional alignment, which reserves selected latent dimensions for stiffness, strength-related stress response, or weight so that search can be biased toward functionally meaningful regions. Simulation experiments show that screened reduction improves target-shape retrieval and the feasibility rate of suggestions, whereas unscreened reduction degrades both. Additional simulations show that constraining search along learned functional dimensions accelerates exploration toward target functional properties. A controlled study with 40 participants further shows that a 5D feasibility-aware space yields higher shape similarity and more feasible suggestions than the original 9D procedural parameterization. These results suggest that, for intelligent user interfaces in engineering design, the representation exposed to the user is a central part of the interaction design, not merely a preprocessing step for the optimizer.

---


### 75. [Why Multi-Layer Message Passing Works: Completeness Theory for Graph Neural Network Interatomic Potentials](https://arxiv.org/abs/2609.00528)

**<font color=#1a73e8>作者：</font>** Pingbing Ming, Han Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove that the Hypergraph Neural Network, an invariant architecture with 3-body message passing, is a universal approximator for potential energy surfaces. Our main contribution is a multi-layer completeness theory. We show that $L$ layers of message passing on sparse, cutoff-based graphs achieve the same representational power as having access to the full $L$-hop neighborhood, provided the configurations are generic, satisfy an overlap condition and a connectivity condition. This provides the first rigorous justification for the common practice of using multi-layer message passing with a per-layer cutoff smaller than the physical interaction range, the setting used by virtually all practical graph neural network based machine-learned interatomic potentials. As immediate consequences, we show that both DPA3 and CHGNet architectures inherit universal approximation.

---


### 76. [DeSyR: A Decoupled Symbolic Recovery Framework with PINN-Guided Structure Search and Physics-Informed Coefficient Refinement](https://arxiv.org/abs/2609.00530)

**<font color=#1a73e8>作者：</font>** Pancheng Niu, Jun Guo, Qiaolin He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recovering compact explicit solutions from neural approximations is challenging when imperfect teacher data guide symbolic topology search and coefficient estimation. We present DeSyR, a decoupled symbolic recovery framework for differential equations. A physics-informed neural network guides repeated searches to construct candidate topologies with provisional constants. Once a topology is fixed, its coefficients are refined solely from the governing equation and prescribed constraints, followed by gated selection and verification. For linear fixed-topology parameterizations, we characterize teacher-error inheritance and show that finite-weight mixed data--physics fitting retains an $O(\beta^{-1})$ teacher-dependent contribution when the teacher error projects onto the model space. Under well-posedness, representability, zero-residual attainment, and discrete determinacy, physics-only refinement conditionally recovers exact coefficients; for nonlinear parameterizations, the corresponding guarantees are local. DeSyR is evaluated on 15 differential-equation problems across 18 configurations covering high-order, space--time, multidimensional, nonlinear, and coupled systems. A candidate-level audit yields a 99.23% convergence rate among free-parameter refits, while every selected refinement involving free coefficients converges. Configuration-level median refined relative $L_2$ errors are $2.31\times10^{-14}$ or lower. In same-topology comparisons, refinement reduces error by eight to fourteen orders of magnitude. These results show that an approximate neural teacher can guide topology discovery without imposing its error scale on final recovered coefficients, provided a target-capable topology is retained and physics-only refinement converges.

---


### 77. [GenONet: A Generative operator Network for High-Resolution Precipitation Nowcasting](https://arxiv.org/abs/2609.00544)

**<font color=#1a73e8>作者：</font>** Mohammad Kian Golkar, Luciano Alves de Oliveira, Mohammad Khanjani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-resolution precipitation nowcasting is critical for reducing the impacts of severe weather but remains difficult because of rapid storm evolution. Deep learning models have shown great promise for this task, but their predictive skill often deteriorates over longer forecast horizons. This leads to increasingly blurry forecasts that fail to capture the complex, non-linear evolution of storm systems. In order to address these limitations, we introduce Spatio-Temporal U-DeepONet (GenONet), a novel architecture for long-range precipitation forecasting up to 3 hours, specifically designed to produce sharp and physically consistent results. GenONet's architecture pioneers the use of a Deep Operator Network (DeepONet) as a generator within a Generative Adversarial Network (GAN) framework for this task. The DeepONet learns the continuous-time dynamics of precipitation, ensuring stability over long forecast horizons. Adversial training against a spatio-temporal discriminator compels the model to produce sharp, coherent forecasts, while a physics-informed loss regularizer, derived from the Moisture Conservation Equation, improves physical plausibility in our ablation setting. Quantitative evaluations show that our model achieves consistently higher scores on most of the metrics, especially for highintensity events and at longer lead times. Qualitatively, GenONet produces structurally coherent forecasts that maintain their integrity, whereas baseline models degrade into indistinct patterns. Finally, an ablation study confirms the benefit of this physics-informed loss, highlighting the strength of combining operator learning with adversarial training.

---


### 78. [Manifold-Aware General Coded Computing for Straggler-Resilient Distributed Computing](https://arxiv.org/abs/2609.00552)

**<font color=#1a73e8>作者：</font>** Parsa Moradi, Mohammad Ali Maddah-Ali  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing coded-computing designs do not explicitly exploit the intrinsic structure of the input data. In communication systems, statistical structure and redundancy are often removed through source coding (or compression) before channel coding is applied. This principle, however, does not transfer directly to coded computation. In many computational tasks, particularly in machine learning, the structure of the data is precisely what the computation seeks to exploit to infer outputs or learn meaningful patterns. Consequently, coded-computing schemes should preserve and leverage this structure in their code design, rather than ignoring or eliminating it through source coding.
This observation motivates a different perspective on code construction. In many channel-coding schemes, such as Reed-Solomon codes, coded symbols are generated by evaluating a low-dimensional algebraic representation at selected points. In contrast, many high-dimensional datasets naturally concentrate near low-dimensional manifolds. In this paper, we exploit this intrinsic geometry by designing coded samples that follow the natural manifold of the data, rather than imposing an artificial low-dimensional structure unrelated to the data distribution. Inspired by graph-based manifold learning, we propose a manifold-aware encoding strategy for general coded computing (GCC). Experiments on neural network inference and high-dimensional polynomial evaluation demonstrate that the proposed strategy consistently and significantly reduces the mean squared recovery error under straggling compared with standard GCC.

---


### 79. [EEG-VID: Task-Guided Latent Predictive Pretraining for EEG Decoding and Assistive Target Selection](https://arxiv.org/abs/2609.00566)

**<font color=#1a73e8>作者：</font>** Guanzhong Sun, Junyi Ma, Yuxuan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose EEG-VID, a task-guided latent predictive pretraining framework for EEG decoding under session and subject shifts. EEG-VID predicts future latent EEG states from recent history using an exponential-moving-average target encoder and weak task guidance, followed by supervised fine-tuning. Across VIG-48 and BCI Competition IV-2a/IV-2b, Stage 1 improves mean accuracy in 41 of 42 matched backbone-dataset-protocol comparisons, including all 12 leave-one-subject-out settings, with a maximum gain of 16.22 percentage points. On the 48-region cross-day VIG-48 task, EEG-VID achieves 6.52% Top-1 and 30.50% Top-5 accuracy. In a separate six-participant offline robot-scene study, candidate-constrained target selection reaches 40.24% versus a 25% chance level after subject-specific calibration. These results support task-guided latent prediction as a transferable pretraining strategy for EEG decoding and scene-constrained assistive target selection.

---


### 80. [GeoPAR: Large-Scale Multi-Agent Combinatorial Optimization with Geometry-Guided Parallel Autoregressive Learning](https://arxiv.org/abs/2609.00577)

**<font color=#1a73e8>作者：</font>** Wenjian Wu, Zesheng Jia, Jiaying Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent combinatorial optimization problems are notoriously challenging due to their NP-hard nature. Recent parallel autoregressive neural solvers improve inference efficiency by allowing agents to make decisions simultaneously, but their performance often degrades on large-scale instances. This is largely attributable to weak modeling of local geometric structures and the fact that conflicting task selections are handled only after action generation. To address these limitations, we propose GeoPAR, a geometry-guided parallel autoregressive reinforcement learning framework for scalable multi-agent combinatorial optimization. GeoPAR integrates three key components: (1) a projection-window sparse geometry mechanism that builds lightweight local candidate neighborhoods through multi-directional projections, (2) sparse edge-biased attention that injects these geometric relations into node representations, and (3) cache-guided conflict-aware assignment that reuses the geometric cache during decoding to suppress duplicate selections of exclusive tasks. Experiments on heterogeneous vehicle routing and open multi-depot pickup-and-delivery problems show that GeoPAR improves large-scale zero-shot generalization while substantially reducing rollout steps and maintaining efficient inference.

---


### 81. [Quit While You're Ahead: Quit for Efficient Candidate Generation in Machine Translation Reranking](https://arxiv.org/abs/2609.00588)

**<font color=#1a73e8>作者：</font>** Guangyu Chen, Boxuan Lyu, Hidetaka Kamigaito 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reranking methods, such as Minimum Bayes Risk (MBR) decoding and Quality Estimation (QE) reranking, are widely used in modern neural machine translation (NMT) to select an output from a set of candidate hypotheses. However, the performance gains come at the cost of high inference latency. Existing acceleration methods target MBR decoding and reduce only reranking computation, leaving QE reranking unaddressed and candidate generation---which can be the larger computational bottleneck---largely untouched. In this work, we propose Quit (Quantifying Uncertainty for Incremental Termination), a novel early-stopping strategy for the entire generation--reranking pipeline. Viewing candidate generation as a sequential decision under uncertainty, Quit incrementally generates and reranks candidates, stopping when the highest estimated quality in the candidate set stabilizes. Comprehensive experiments on three NMT models across 19 language pairs show that Quit yields end-to-end speedups of $1.47$--$2.66\times$ for MBR and $3.43$--$4.12\times$ for QE reranking while preserving translation quality within prespecified equivalence margins.

---


### 82. [BrainDiff: Longitudinal Report Generation for Multimodal Brain MRI](https://arxiv.org/abs/2609.00593)

**<font color=#1a73e8>作者：</font>** Krish Patel, Peirong Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neuroradiologists rarely read a brain MRI in isolation, yet automated brain-MRI report generation has been built almost entirely for single studies. Temporal analysis has been explored on chest radiography and chest CT, but to our knowledge, longitudinal reporting for brain MRI, where interval change is often subtle and spatially distributed, remains unaddressed. We present BrainDiff, the first longitudinal vision-language system for brain MRI. BrainDiff outperforms both frontier general-purpose and single-study neuroimaging models on the same patient pairs. Moreover, BrainDiff retains 91% of internal RadGraph-XL entity+relation F1 (rg_er) on an external, cross-hospital cohort. Beyond the system, we contribute three analyses. First, we identify two independent grounding levers: a counterfactual objective with prior-report dropout, which increases measured image reliance by ~47%, and a staged curriculum. Together, these interventions raise image reliance 2.5-fold from the baseline. Second, we provide a factorial over prior-report availability and image identity, isolating a visual contribution of +0.0387 rg_er, which grows when the prior report is withheld. Third, a cheap change-decodability test for candidate backbones shows that interval change is decodable far more weakly than single-study pathology (0.60 vs. 0.77 AUROC). Code is publicly available at this https URL.

---


### 83. [A Version Space Approach for Digital Circuit Analysis](https://arxiv.org/abs/2609.00609)

**<font color=#1a73e8>作者：</font>** Mitchell A. Thornton  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Many questions about a digital circuit take the same form. A hidden object is consistent with a set of observations, and one wants to know how many remain consistent and which observation to make next. The set of surviving candidates is the version space, and its size, on a logarithmic scale, measures how much the observations have settled. This paper develops the version-space view as one method and applies it to two circuit-analysis problems usually treated as unrelated. The first is probabilistic combinational equivalence checking, where the candidates are Boolean functions and the observations are modified-Haar spectral coefficients. A method proposed in 2002 posed this counting problem and solved only two special cases, leaving the general case an enumeration exponential in the number of observations. We close it. A reparameterization onto block sums turns the dependence among nested coefficients into locality, a sum--product recursion counts the surviving functions exactly in time polynomial in the truth-table size, closed forms follow for a single coefficient, a coefficient pair, and every ancestor-closed set, and the error of the independence approximation the 2002 work resorted to equals a computable lattice index. Every formula is checked against exhaustive enumeration and reproduces the 2002 tables. The second application is key counting for logic-locked netlists, where the candidates are keys and the observations are oracle responses. The same recursion, run over the gate-level factor graph, computes the number of keys still consistent with a set of queries; across seventy instances of the TrustHub obfuscation release the surviving entropy falls below the advertised key length every time. The two applications are one method: a witness supplies observations, each removes candidates, and the version space is counted exactly.

---


### 84. [Streaming4D: Accelerate 4D World Models via Block-wise Video Generation and Incremental Reconstruction](https://arxiv.org/abs/2609.00610)

**<font color=#1a73e8>作者：</font>** Xiaoyan Liu, Jiaxin Liu, Kangrui Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current 4D generation paradigms are often bottlenecked by a sequential decoupling design: video is generated first, followed by 3D reconstruction, leading to high interaction latency. This limits applications in interactive real-time scenarios. To this end, we propose \textbf{Streaming4D}, a tightly coupled synchronous pipeline that integrates block-wise autoregressive video generation with incremental 3D reconstruction. Unlike traditional frame-by-frame emission and delayed geometry recovery, Streaming4D generates temporal video blocks and immediately triggers reconstruction for each completed block, enabling parallel execution between synthesis and geometric updates. This approach allows the world representation to evolve online with the video stream, reducing feedback latency while preserving geometric fidelity. We instantiate \textbf{Streaming4D} using a Self-Forcing-style autoregressive generator and an incremental reconstruction backend. Experiments show consistent runtime improvements across resolutions on a single RTX 4090 (1.24$\times$ speedup), while maintaining high-quality 4D geometry and multi-view consistency.

---


### 85. [Beyond Landmark Extraction: A Framework for Robust Geometric Feature Construction in Structured Image Classification](https://arxiv.org/abs/2609.00634)

**<font color=#1a73e8>作者：</font>** Saravana Mauree, Sakshi Arya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Much of the literature on structured image recognition has disproportionately focused on the comparison of classification algorithms. Rather than investigating which classifier performs best, this paper instead asks: what should a classifier know before it ever makes a prediction? In structured vision problems such as gesture recognition, facial expression categorization, and medical image analysis, discriminative information lies less in individual pixels and more in spatial relationships between semantic parts. Raw pixel spaces are high-dimensional, sensitive to nuisance variation, and often obfuscate the geometric structures that make visual tasks interpretable. Landmark extraction provides one form of dimension reduction, but it does not by itself determine the information preserved. This paper studies the post-landmark feature map as the central object of analysis and proposes a systematic framework for constructing and interpreting landmark-derived representations as an, informed, feature-based ``dimension reduction'' step. Using static hand gesture recognition as a case study, we evaluate coordinate, distance, angle, and hybrid representations through perturbation and ablation experiments. The results show that visually variable data exposes substantial gaps between raw coordinate features and their geometrically invariant counterparts, while hybrid representations achieve the strongest overall performance by combining complementary geometric components. These findings frame feature construction as a fundamental modeling decision and ultimately suggests that the question of what representation should a classifier learn from is one worth asking. The code used for feature construction and evaluation is available at this https URL

---


### 86. [DramaChain Bench: An End-to-End Benchmark for Short-Drama Generation](https://arxiv.org/abs/2609.00646)

**<font color=#1a73e8>作者：</font>** Haoyuan Shi, Mingtao Chen, Shuo Jiang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Commercial short-drama production follows a multi-stage chain: script, storyboard, keyframe imagery, shot-level video, and the finished short drama. Most existing benchmarks evaluate solely the video-generation stage using pre-authored inputs instead of real upstream pipeline outputs. This leaves two critical questions unanswerable: whether each stage adheres to the original script intent (rather than only its immediate input prompt), and whether disparate shots remain coherent after assembly into multi-episode releases. We present DramaChain Bench, the first short-drama benchmark that evaluates every stage of the complete production chain. It is built upon three in-house systems sharing one dimension system, DramaChain Dimensions: five evaluation axes instantiated at every stage, resolving into 63 leaf dimensions. DramaChain Agent is calibrated against commercial short-drama platforms in both workflow and finished short-drama quality, enabling stage-wise fair comparison across models. DramaChain Labeling System has each of the 5,785 items scored independently by three professional annotators, with all defects spatio-temporally localised and selected from a predefined defect list. This process produces 17,488 valid scores and 255,925 traceable attribution records. The human annotations confirm that upstream defects cascade across the pipeline, demonstrating that final episode quality is not governed by video generation alone. DramaChain Agentic Judge then scores every leaf dimension automatically, gathering evidence over multiple agentic rounds before judging against a per-item checklist; it reproduces the model ranking at a mean PLCC of 0.918, enough to admit new models at no annotation cost.

---


### 87. [DK-GBMKKM: Dynamic Kernel-Space Granular-Ball Multiple Kernel $k$-Means Clustering](https://arxiv.org/abs/2609.00647)

**<font color=#1a73e8>作者：</font>** Xiaoyu Lian, Yuchao Zhang, Shuyin Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multiple kernel $k$-means integrates complementary nonlinear similarities by learning a combination of base kernels. Its pointwise optimization, however, is sensitive to noisy and boundary samples and repeatedly operates on sample-scale kernel matrices. Granular-ball representations organize local sample groups into mesoscopic units, but granular balls generated once in the input space may be inconsistent with the fused-kernel geometry that evolves during multiple kernel learning. We propose dynamic kernel-space granular-ball multiple kernel $k$-means (DK-GBMKKM). The method generates granular balls in the current fused kernel space and alternates kernel-weight learning with granular-ball membership updates, allowing the representation to adapt to changes in the fused-kernel geometry. A sample-size-weighted granular-ball kernel is further constructed to preserve the contributions of balls of different sizes, and its positive semidefiniteness and related equivalence properties are established. Experiments on 12 public datasets demonstrate the strong overall clustering performance of DK-GBMKKM. The code has been open-sourced for reproducibility: this https URL.

---


### 88. [DGNet: Dual-knowledge Guided Network for Infrared Small Target Detection](https://arxiv.org/abs/2609.00666)

**<font color=#1a73e8>作者：</font>** Chenglong Yu, Mingzhu Xu, Jing Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> InfRared Small Target Detection (IRSTD) is a prominent and challenging task in computer vision. In recent years, text-guided methods have significantly improved detection performance. However, they still suffer from two key limitations. First, a single text description simultaneously modeling both background and target leads to semantic entanglement, which contradicts the objective of background suppression and target enhancement. Second, reliance on image-specific textual prompts (requiring additional external models such as CLIP during inference) results in deployment constraints. To address these issues, we propose a novel Dual-knowledge Guided Network (DGNet) based on multiple generalizable texts. Specifically, we design a Prior-knowledge Wavelet Modulation (PWM) module, which leverages dual textual priors that separately characterize large-scale backgrounds and sparse targets to effectively disentangle and modulate entangled semantics in the frequency domain. Furthermore, we introduce a Consensus-knowledge Directional Alignment (CDA) loss, which models the initial state and the ideal target across samples as `complex background' and `bright target', respectively, thereby constructing a clear and unified directional optimization trajectory for the model. Extensive experiments on three public datasets demonstrate the superior performance of DGNet and the effectiveness of each component. The source code is available at this https URL.

---


### 89. [Automating Static Code Analysis Through CI/CD Pipeline Integration](https://arxiv.org/abs/2609.00676)

**<font color=#1a73e8>作者：</font>** Zachary Wadhams, Ann Marie Reinhold, Clemente Izurieta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the contemporary landscape of software devel-opment, securing sensitive data is paramount to safeguarding organizational reputation, preventing financial losses, and pro-tecting individuals from identity theft. This paper addresses the pervasive challenge of identifying and rectifying security vulnerabilities early in the development process, emphasizing the role of Static Application Security Testing (SAST) tools. While SAST tools play a crucial role in detecting vulnerabilities, widespread adoption has been hindered by usability issues, including high false positive rates and a lack of native pipeline support. This paper proposes a novel, generalized, and automated process for aggregating SAST tool outputs and integrating them into developers' familiar issue-tracking software. The process streamlines the identification and communication of security vulnerabilities during the development lifecycle, facilitating more efficient remediation efforts. We demonstrate the successful implementation of the proposed process with the SonarQube SAST tool in a GitLab-based development environment. Developers were positive about the structured implementation, real-time feedback, and proactive vulnerability management. However, despite some challenges such as a potential learning curve and tradeoffs between secure coding and workflow disruption, the overall positive impact on security awareness and responsiveness suggests that the proposed process holds promise in enhancing the security posture of software development practices

---


### 90. [HarmoCore: Functional Latent Diffusion for Sparse Reconstruction of Oscillatory Wave Fields](https://arxiv.org/abs/2609.00679)

**<font color=#1a73e8>作者：</font>** Lihao Chen, Xinyu Zhang, Panqi Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstructing oscillatory wave fields from scattered sensors is a severely underdetermined inverse problem. Beyond the challenges of general physical-field reconstruction, wave responses are complex-valued, frequency-sensitive, and highly oscillatory, while costly simulation and sensing often leave only extreme-sparse observations. Existing low-rank, operator, and diffusion approaches are largely designed for real-valued, smoother fields; dense pixel-space diffusion is particularly inefficient for oscillatory complex fields and difficult to scale to 3D. We propose HarmoCore, which places a generative prior in a compact, continuous, and structured wave-field latent. HarmoCore represents joint real--imaginary channels with Functional Tucker cores over shared continuous spatial bases, learns a frequency-conditioned core diffusion prior, and performs Diffusion Posterior Sampling directly in core space. At fixed sensor coordinates, the multilinear decoder induces an explicit likelihood guidance operator, avoiding dense pixel-space correction. Optional target-equation residual guidance further promotes physical consistency. Experiments on 2D Helmholtz, 2D synthetic wave fields, and 3D Helmholtz show substantial gains under 1%--2% sensing while remaining practical in three dimensions.

---


### 91. [Creative Generation via Multi-Agent Debate: Does Debate Suppress Diversity?](https://arxiv.org/abs/2609.00683)

**<font color=#1a73e8>作者：</font>** Tien Anh Nguyen, Khanh-Binh Nguyen, Van Dai Do 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Creative generation tasks, such as narrative writing and scientific ideation, demand both high-quality outputs and distinct responses across independent runs to maximize exploration. Multi-Agent Debate (MAD) has shown strong quality gains on factual and reasoning tasks, making it a natural candidate for creative generation. However, we find its convergence-driven design actively suppresses output diversity across independent runs, creating an inherent trade-off with creative tasks. We theoretically show that preserving diversity among agents within each debate session is a necessary condition for achieving diverse outputs across independent runs. Building on this finding, we propose Creative-MAD, which introduces two synergistic interventions to sustain agent divergence. Specifically, Cognitive Lens Assignment counters identity drift by anchoring each agent to a distinct and persistent cognitive mode, while Embedding-based Peer Selection counters majority pull by limiting each agent's context to its most semantically distant peers. Experiments across four creative benchmarks demonstrate that Creative-MAD significantly enhances both lexical and semantic diversity while maintaining MAD's output quality.

---


### 92. [Visual Framing for News Stance Detection via Image Generation](https://arxiv.org/abs/2609.00685)

**<font color=#1a73e8>作者：</font>** Dahyun Lee, Jiyoung Han, Kunwoo Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Article-level news stance detection aims to identify the perspective of news articles toward social issues. Despite advances in stance detection and its importance for trustworthy media environments, news articles pose distinct challenges because their stances are often implicit, subtly conveyed through journalistic framing, and embedded in long, structurally complex texts. To address these challenges, we introduce VFStance, which leverages visual framing to make implicit stance cues more explicit via image generation. In evaluation experiments, we demonstrate the effectiveness of VFStance over existing methods and the contribution of visual framing to its performance. Finally, a controlled user study (N=200) in a snippet-based news consumption setting further demonstrates that VFStance can make stance signals visually salient and highlights its potential use beyond automated stance detection.

---


### 93. [A Study of Hidden-State Optimization Order in Predictive Coding Networks](https://arxiv.org/abs/2609.00686)

**<font color=#1a73e8>作者：</font>** Xueyuan Li, Danilo Vasconcellos Vargas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Local learning methods offer an alternative to end-to-end backpropagation, but their unstructured local objectives can produce weak feature learning in deep networks. We study whether the order of hidden-state optimization can address this limitation. We propose a boundary-first inference schedule that partitions a model into chunks, first coordinates hidden states at chunk boundaries, and then refines representations within each chunk. We instantiate this schedule in predictive coding networks (PCNs), a local-learning framework in which hidden activities and prediction errors are explicitly exposed during inference. On CIFAR-10, the resulting boundary-first predictive-coding instantiation improves accuracy over standard predictive coding by $9.77\%$ under a standard parametrization and by $5.51\%$ under a $\mu$-parametrization. Diagnostic analyses further show more non-trivial early-layer updates, lower initial-to-final CKA, and more diverse layerwise gradients, consistent with stronger feature learning. These results support boundary-first, chunk-based inference as a practical design principle for predictive-coding training and motivate its study in broader local-learning systems.

---


### 94. [Verdict Instability of OOD Scores under Reference Resampling](https://arxiv.org/abs/2609.00691)

**<font color=#1a73e8>作者：</font>** Donghoon Lee, Shinjin Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc out-of-distribution detectors are fitted on a finite reference set, so every score they produce is an estimate. If we had chosen a different set, some verdicts would have moved. We measure that movement by resampling the reference set and recording the bootstrap standard deviation of the score, which we call verdict instability. It admits a closed form with no fitted parameters. The instability of a verdict is the within-class dispersion of the assigned class along the query's direction, divided by the square root of that class's reference count. That count is what separates verdict instability from the geometry of the score distribution, and it is identifiable only under class imbalance. Instability grows with the local dispersion. Far-OOD queries lie along the low-variance directions of an anisotropic embedding, so every distance-based score we test assigns its highest values to the verdicts that are most reproducible. Only estimators of local dispersion carry the sign a practitioner expects. We give a rule that predicts this sign for any score from a single label-free correlation, and abstention driven by a wrong-signed score turns out worse than abstention at random on every dataset we test.

---


### 95. [MUGEN: Generating Unlearnable Graph Examples for Multiple Learning Tasks](https://arxiv.org/abs/2609.00696)

**<font color=#1a73e8>作者：</font>** Ziyan Liu, Chengshuai Zhao, Huan Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph data across diverse domains can expose valuable relational information to unauthorized representation learning, creating a pressing need for protection against such misuse. Unlearnable examples offer a data-level defense by perturbing a training release so that models trained on it fail to generalize to clean data. Existing methods generate unlearnable graph examples for only a specified downstream task. Consequently, a release protected against one task may remain learnable for other plausible uses, including node classification, graph classification, and link prediction, which the data owner cannot anticipate. We introduce MUGEN, to our knowledge the first framework for generating unlearnable graph examples that jointly protect all enabled tasks. From one clean dataset, MUGEN produces a single feature-perturbed release that protects every enabled task through a shared GNN encoder and task-specific heads. We devise a Task-Aligned Separability Objective (TASO), which leverages task prediction and classwise separability to strengthen unlearnability and its transfer across GNN backbones and enabled tasks. We further introduce Type-Adaptive Perturbation (TAP), which tailors perturbation optimization to node-attribute type, with direct search over feasible hard flips that accept only loss-improving updates for discrete node attributes and customized gradient-based updates for continuous node features, thereby enabling strong unlearnability across both settings. Experiments across five benchmarks, four backends and three learning paradigms demonstrate that MUGEN generates transferable unlearnable graph examples across GNN backbones and all three tasks, and remains effective under adversarial training and data augmentation.

---


### 96. [PhantomCall: Evading ML Malware Detectors via Function Call Graph Perturbation](https://arxiv.org/abs/2609.00705)

**<font color=#1a73e8>作者：</font>** Md Ajwad Akil, Adrian Shuai Li, Imtiaz Karim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prior adversarial attacks on Windows PE malware detectors target raw bytes, PE headers, or intra-function control-flow graphs, leaving the function call graph (FCG) unexplored as an attack surface. Yet the FCG structure is an important feature in graph-based malware detectors. We present Phan- tomCall, a black-box attack that perturbs the FCG of Windows PE malware by injecting fully executable dummy functions at targeted call sites, adding new nodes and edges to both the CFG and FCG while preserving program semantics. We pair this structural perturbation with classifier-guided search and tunable injection parameters, effective across three archi- tecturally distinct classifiers. Evaluated on a 2025-collected Windows malware corpus against MalConv (raw-byte CNN), MalGraph (graph-based GNN), and SAFE+GNN (pure FCG GNN trained from scratch on a 2024 corpus) at two FPR thresholds, the best PhantomCall variant achieves 85-100% attack success rate across all configurations, exceeding prior state-of-the-art by up to 14.78 percentage points on MalGraph and 95.5 percentage points on SAFE+GNN, and generating evasive variants up to 2.9x faster on average across all targets. For MalConv and MalGraph, the majority of evasions require only a single call site modification, and 86-97% of evaluated evasive variants preserve the original malicious behavior in sandbox-based semantic testing across all configurations.

---


### 97. [Differentially Private Paired Table-Image Multimodal Synthesis](https://arxiv.org/abs/2609.00708)

**<font color=#1a73e8>作者：</font>** Kai Chen, Josephine Lamp, Somesh Jha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differentially private (DP) synthesis has been extensively studied for tabular and image data separately, yet many real-world datasets contain images paired with multivariate tabular records. Synthesizing such data is particularly challenging under DP, as the two modalities favor different private learning mechanisms while their dependence must also be preserved. To address this challenge, we propose DP-TabImage, a modality-specialized framework for private paired synthesis. DP-TabImage instantiates the factorization $p(x,y)=p_T(y)p_I(x\;|\;y)$ using a private Probabilistic Graphical Model for the multivariate table distribution and a table-conditioned diffusion model trained with DP-SGD for the conditional image distribution. To facilitate conditional learning under clipped and noisy gradients, we further pretrain the model on private table-image prototypes, pairing privately constructed attribute-conditioned images with tabular vectors derived from the already private tabular model at no additional privacy cost. Experiments on three real-world datasets show that DP-TabImage achieves a strong balance among tabular fidelity, image fidelity, and cross-modal alignment. Our analysis further reveals that visual warm-up primarily improves marginal image fidelity, whereas aligned table-image warm-up is critical for improving cross-modal correspondence. Our source code is available in the GitHub repository, this https URL.

---


### 98. [SoK: Motion Data Privacy in Extended Reality](https://arxiv.org/abs/2609.00711)

**<font color=#1a73e8>作者：</font>** Azim Ibragimov, Alina Vasina, Uliana Polshcha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Extended Reality (XR) provides immersive, interactive 3D experiences. To enable these experiences, the devices must track user motion so the system can respond to actions such as grabbing, looking at, or moving an object. However, motion tracking has raised privacy concerns since it records a person's motion patterns. These motion patterns have been studied extensively across various fields (i.e., gait identification and profiling) and have been shown to reveal sensitive information. With the adoption of XR, these patterns became easier to record and obtain than ever. This creates a fundamental privacy tension: motion tracking enables core XR functionality yet requires users to compromise their privacy. Prior systematization-of-knowledge (SoK) studies on XR privacy have examined the field broadly, with motion-related research distributed across several privacy domains rather than treated as a distinct area of study. However, XR motion privacy has gained significant momentum since the prior SoK, with the literature nearly quadrupling in size and thereby warranting a dedicated systematization of this topic. This SoK examines 134 relevant papers on privacy concerns in motion patterns recorded by XR headsets, including how adversaries can obtain users' motion patterns, the inferences they can draw from them, and methods for protecting users. Based on this review, we synthesize a taxonomy of motion modalities, representations, and inference risks; develop an XR motion threat model; systematize the attack and defense approaches in the XR motion literature; identify gaps in the literature; and provide guidelines for future studies evaluating motion privacy mechanisms. Together, our SoK clarifies the state of XR motion privacy and provides recommendations for future evaluations.

---


### 99. [EarthLD: Towards Unified Open-World Landslide Understanding via Vision-Language Guided Diffusion Models](https://arxiv.org/abs/2609.00712)

**<font color=#1a73e8>作者：</font>** Yuanchao Su, Lianru Gao, Mengying Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Landslides are widespread geological hazards, yet their automated detection and mapping in remote sensing imagery remain challenging because of their irregular morphology, ambiguous spectral signatures, and substantial domain shifts across imaging platforms. To overcome these challenges, we propose EarthLD, a vision-language-guided diffusion framework for open-world landslide understanding, enabling unified landslide recognition, mapping, and trigger interpretation. At its core, EarthLD formulates landslide understanding as a diffusion process that progressively infers the presence, spatial extent, and pixel-level boundaries of landslides from noisy latent representations. This probabilistic formulation enables the model to jointly perform image-level landslide recognition and mapping while characterizing predictive uncertainty. By integrating visual observations with contextual knowledge in the denoising process, EarthLD distinguishes diverse landslides from backgrounds, produces confidence-aware predictions for suspected regions, and maps landslide ranges. We additionally construct a global-scale open-world landslide benchmark by systematically harmonizing multiple publicly available remote sensing data collected by diverse institutions. Extensive experiments across regions, sensors, and triggering events demonstrate that EarthLD consistently outperforms existing landslide detection methods, highlighting its potential as a unified and robust solution for global geological-hazard monitoring and emergency response.

---


### 100. [Efficient and Robust Absolute Pose Estimation via Gravity-Prior-Driven Transformation Decoupling and Pose Refinement](https://arxiv.org/abs/2609.00713)

**<font color=#1a73e8>作者：</font>** Hu Cao, Qianyi Yang, Xinyi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimation of the absolute pose of an object is an essential task for various robotic applications. Recently, incorporating gravity direction as prior information has emerged as a popular approach to simplify absolute pose estimation. However, developing a robust and efficient algorithm to solve this challenging problem remains a difficult question due to large amounts of mismatches. In addition, obtaining an accurate pose solution from selected inlier correspondences with gravity prior is still a research gap. In this paper, we propose a novel transformation strategy that exploits geometric relations derived from the gravity prior. Through transformation decoupling, the original 6 degrees of freedom (DoF) absolute pose estimation problem is simplified into a 4-DoFs problem: 1-DoF for the rotation angle and 3-DoFs for translation, significantly improving the efficiency. For the 1-DoF rotation angle, we apply a one-dimensional global voting algorithm for optimal estimation. Once the optimal rotation is obtained, the mismatched correspondences are preliminarily filtered, and translation estimation, a linear problem, can be easily solved. Furthermore, to obtain accurate pose results, we introduce a novel pose refinement algorithm to enhance the accuracy of both rotation and translation. Extensive experiments on synthetic data and three publicly available real-world datasets (TUM RGB-D, ETH3D, and RobotCar) demonstrate that the proposed method achieves stronger performance compared to existing state-of-the-art (SOTA) approaches. To further validate our method, we integrated it into ORB-SLAM2. The results on the KITTI dataset show it effectively reduces drift and improves trajectory alignment during relocalization. The source code will be released upon acceptance.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-236](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
