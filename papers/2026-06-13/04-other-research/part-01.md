# 📦 其他研究 | 2026年06月13日

> 本类共 **251** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-251](./part-06.md)

---

### 1. [Stereo Vision-Based Fall Prediction and Detection using Human Pose Estimation on the AMD Kria K26 SOM](https://arxiv.org/abs/2606.12473)

**<font color=#1a73e8>作者：</font>** Shreyas Narasimhiah Ramesh, P. D. Rathika, Mahasweta Sarkar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background and Objective: Falls among elderly people can cause serious injury and reduce quality of life. Timely prediction and detection are essential to prevent harm and support well-being. We propose a portable, low-power, battery-operated, vision-based fall prediction and detection system using HPE on an AMD Kria K26 System-on-Module (SOM). The objective is a non-intrusive, privacy-preserving system for real-time fall detection.
Methods: The system uses an Intel RealSense D455 range-sensing camera connected to the K26 SOM by USB. It captures synchronized RGB and depth frames, 640 x 480 x 3 and 640 x 480 pixels, at 60 FPS. The SOM runs a three-stage pipeline with quantized YOLOX, Anchor-to-Joint (A2J), and fall-detection models. YOLOX identifies human bounding boxes from RGB frames, then discards the RGB frames to preserve privacy. A2J uses depth frames to estimate 15 joint keypoints per person. A CNN uses selected joint coordinates (x, y, z) to classify fall activity. YOLOX was trained on CrowdHuman; A2J on ITOP, MP-3DHP, UR Fall Detection, and a custom SDSU PSG dataset; and the CNN on UR Fall Detection and SDSU PSG. The design used a single-core DPU with a serial pipeline and a dual-core DPU running YOLOX and A2J with multiple threads.
Results: Quantized accuracy was evaluated using IoU >= 50% for YOLOX, mAP with a 10-cm rule for A2J, and classification accuracy, (TP + TN)/(TP + TN + FP + FN), for the CNN. Accuracies were 74%, 84.13%, and 75.85%. Throughput improved from 2.5 FPS for the single-threaded pipeline to 4.5 FPS for the multi-threaded version.
Conclusion: Results demonstrate the feasibility of privacy-preserving fall detection on an AMD Kria K26 edge device. On-device HPE and fall classification runs without cloud dependency, supporting elderly monitoring and assistive healthcare. Future work will improve model accuracy and speed.

---


### 2. [Quickest Detection of Hallucination Onset: Delay Bounds and Learned CUSUM Statistics](https://arxiv.org/abs/2606.12476)

**<font color=#1a73e8>作者：</font>** Igor Itkin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Token-level hallucination detectors are evaluated as classifiers, by AUC over all tokens, yet a streaming monitor is judged by its reaction time: the number of tokens that pass between the onset of a hallucination and the alarm. We formulate hallucination onset detection as a quickest change detection problem. A first-order Markov model of the latent faithful/hallucinated state, validated on RAGTruth, places the task inside classical change-point theory and yields Lorden's lower bound on detection delay: about 1.3 tokens at a false-alarm rate of 0.01. We then show that a causal recurrent labeler acts as a CUSUM with a learned increment; at a matched false-alarm rate it detects in 11-13 tokens, against 31 for a linear per-token baseline, and a controlled decomposition attributes most of this advantage to a better per-token score rather than to temporal accumulation. An information-rate optimality theorem of Donsker-Varadhan type explains the remaining order-of-magnitude gap: the learned score realizes only 1/4.5 of the divergence the features carry, a deficit that recalibration cannot remove, with the remainder a finite-horizon effect. Classification metrics conceal this delay structure; sequential analysis makes it measurable

---


### 3. [Boltzmann Attention: Learnable Ising Couplings for Cooperative Attention](https://arxiv.org/abs/2606.12478)

**<font color=#1a73e8>作者：</font>** Gilhan Kim, Daniel K. Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention mechanisms are central to modern sequence models, yet standard attention computes relevance primarily through individual query--key similarities. Although softmax normalization introduces competition among positions, a standard attention layer does not explicitly parameterize learnable interactions between attention decisions. This limits its ability to directly model cooperative or antagonistic co-attention structure within the attention mechanism itself. We propose Boltzmann attention, an energy-based generalization in which attention patterns are governed by an interacting Ising model. The method augments the usual data-dependent local fields with learnable pairwise couplings, allowing the model to represent inter-position correlations beyond those captured by softmax or sigmoid attention. Experiments on character-level language modeling and synthetic bracket matching show that Boltzmann attention consistently improves over standard softmax attention within a standard Transformer architecture, with the advantage becoming more pronounced as sequence length increases. A four-way ablation confirms that the improvement arises from the learnable pairwise couplings. These results suggest that explicit inter-position interactions provide a principled enhancement for attention-based sequence modeling. Moreover, the Ising formulation opens a natural path toward quantum-computing-based sampling strategies: we demonstrate that diabatic quantum annealing provides a practical training method while maintaining competitive performance with exact Boltzmann computation.

---


### 4. [Scalable anomaly detection via a univariate Christoffel function](https://arxiv.org/abs/2606.12483)

**<font color=#1a73e8>作者：</font>** Florian Grivet, Didier Henrion, Jean-Bernard Lasserre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection plays a critical role in identifying unusual patterns across domains such as fraud detection, network intrusion, and system fault diagnosis. Recently, Christoffel function-based methods, rooted in polynomial optimization, have emerged as promising alternatives to deep learning due to their strong mathematical foundations and computational frugality. However, their practical applicability is hindered by the need to invert a matrix whose size grows exponentially with the data dimension, rendering the method intractable even for moderate-dimensional datasets. This paper addresses the dimensionality limitations of Christoffel function-based anomaly detection while preserving its key theoretical properties, i.e., the on-off support dichotomy behavior and the accurate support shape capture. We introduce UCF, a univariate Christoffel function which is based on the squared distance between the query point and the support points. Extensive experiments on the ADBench benchmark demonstrate that UCF consistently outperforms 14 state-of-the-art baselines in terms of Average Precision. By resolving the scalability bottleneck of the Christoffel Function, this work expands the toolkit of anomaly detection methods with a robust, theoretically grounded, and universally applicable approach.

---


### 5. [Speculative Rollback Correction for Quality-Diverse Web Agent Imitation](https://arxiv.org/abs/2606.12485)

**<font color=#1a73e8>作者：</font>** Longkun Hao, Hongyu Lin, Hao Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training interactive web agents through imitation learning from expert trajectories has emerged as a highly effective approach. However, determining the optimal timing for expert intervention presents a critical challenge in this context. Delayed intervention often leads to the accumulation of early-stage errors, pushing the page state into an irrecoverable regime. Conversely, premature or excessive intervention causes the agent to become overly reliant on expert policies, trapping the model in local optima characterized by a single, rigid trajectory. We propose Speculative Rollback Correction (SRC), a branch-level imitation framework for resettable agent environments. Instead of requesting teacher labels at every visited state or correcting only after a completed trajectory, SRC uses fixed-horizon branch review: the student executes a short speculative segment before teacher review, and the teacher localizes the first harmful deviation only when local progress breaks. Rollback preserves useful prefixes, while successful rollouts are filtered by a hard verifier and retained in a lightweight quality-diversity archive. The resulting data supports next-action supervised fine-tuning on both localized corrections and verifier-passing trajectories. On WebArena-Infinity, SRC collects 977 verifier-passing trajectories and 9,183 next-action examples; fixed-horizon review improves the recovery-versus-query tradeoff over step-level review while retaining verifier-passing solution variants. Code is available at this https URL.

---


### 6. [An Empirical Study on Predictive Maintenance for Component X in Heavy-Duty Scania Trucks](https://arxiv.org/abs/2606.12486)

**<font color=#1a73e8>作者：</font>** Valeriu Dimidov, Sasan Jafarnejad, Raphaël Frank  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Condition-based Predictive Maintenance (PdM) for truck fleets has gained momentum in recent years. This maintenance strategy aims to minimize unplanned downtimes and reduce costs by monitoring the health status of vehicles and taking proactive action based on their condition. However, the implementation of condition-based PdM systems is challenging due to the large volume of data generated by the trucks, the inherent complexity of detecting failures through sensor data and the difficulties in finding cost-effective trade-offs in the solution's implementation. In this paper, we define and validate a condition-based PdM methodology built on the assumption that the wear-and-tear state of the monitored component can be represented as a monotonically non-decreasing time series. It involves selecting only the most recent observations from the time series and transforming them into a tabular format for classification using machine learning (ML) models designed for tabular data. Our results indicate that the proposed methodology reduces costs on the Scania Component X dataset compared to current state-of-the-art (SOTA) approaches, while also simplifying the modeling process through AutoML.

---


### 7. [A Stationary (and Therefore Compatible) Representation is All You Need](https://arxiv.org/abs/2606.12488)

**<font color=#1a73e8>作者：</font>** Niccolò Biondi, Federico Pernici, Simone Ricci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning compatible representations aims to learn feature representations that can be used interchangeably over time whenever a model undergoes updates. In this paper, we demonstrate that stationary representations learned by d-Simplex fixed classifiers imply compatibility as in its formal definition. This result establishes a foundation for future works and can be directly exploited in practical learning scenarios. We address the challenge of learning compatibility using $d$-Simplex fixed classifiers when the model is sequentially fine-tuned. Learning according to a d-Simplex fixed classifier with the cross-entropy loss aligns feature distributions at the first-order statistics. Consequently, it may not fully capture higher-order dependencies in the representation between model updates. To address this issue, we demonstrate that training the model using a $d$-Simplex fixed classifier through a convex combination of the cross-entropy loss and a contrastive loss not only captures higher-order dependencies, but is also equivalent to learning with the cross-entropy under the compatibility constraints. We confirm our findings with extensive experiments also considering a new scenario where a pre-trained model is sequentially fine-tuned and occasionally replaced with an improved model. We show that stationary representations enable uninterrupted retrieval services (without reprocessing gallery images) while improving performance during model updates and replacements, achieving state-of-the-art. Code at this https URL.

---


### 8. [Robustness Verification of Recurrent Neural Networks with Abstraction Refinement](https://arxiv.org/abs/2606.12490)

**<font color=#1a73e8>作者：</font>** Li-Jen Lin, Chih-Duo Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Certified local robustness verification for recurrent neural networks (RNNs) is challenging because approximation errors introduced by nonlinear relaxations can propagate through recurrent connections and accumulate over time. As a result, scalable linear bound propagation methods often become overly conservative and fail to certify inputs that are in fact robust, especially when many pre-activation intervals cross zero. We propose an abstraction-refinement framework for RNN verification that partitions such intervals to remove the dominant relaxation error: on each refined branch, ReLU becomes exact, and smooth activations such as tanh and sigmoid admit substantially tighter linear envelopes. To control the combinatorial cost of splitting in long sequences, we introduce a SHAP-guided timestep selection strategy that ranks hidden states by their contribution to the verification objective and refines only the most critical timesteps in temporal order. Experiments on CIFAR10 and MNIST stroke benchmarks demonstrate consistent improvements in verification success and robustness-margin tightness over abstraction-only baselines, while exposing clear runtime trade-offs between ReLU and tanh models.

---


### 9. [Net-Ev$^2$: A Generative Simulator for Network Event Evolution](https://arxiv.org/abs/2606.12494)

**<font color=#1a73e8>作者：</font>** Guangyu Wang, Zhaonan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reducing real-world trial and error has long been a central goal of decision making, and generative simulators advance this goal by modeling the evolution of future states. An even more challenging yet meaningful task is simulating how disturbance events (e.g., accidents) propagate their impacts across real-world networks. The existing approaches fall short of modeling both structured attributes and unstructured semantics of events, and capturing topological structures in simulating network event evolution. Therefore, we are motivated to propose Net-Ev$^2$ ($\underline{\textbf{Net}}$work $\underline{\textbf{Ev}}$ent $\underline{\textbf{Ev}}$olution), a novel generative simulator that jointly leverages event cues while preserving network topology in simulations. Specifically, the framework consists of two stages, namely structure-guided masked pre-training and topology-aware diffusion process, which is achieved by U-Net-like graph downsampling and upsampling during denoising. At inference time, Net-Ev$^2$ can generate simulations using natural-language event input only, with greater flexibility for practical usage. Furthermore, we introduce Net-Ev$^2$-6.5M, a multimodal benchmark of aligned event and network traffic data across four large-scale road networks, as well as a new topology-aware metric, namely JL-MMD, to evaluate topological fidelity in generated network dynamics. Extensive experiments demonstrate the state-of-the-art performance and strong generalization ability of Net-Ev$^2$. Code is made available at this https URL.

---


### 10. [$μ$VLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models](https://arxiv.org/abs/2606.12497)

**<font color=#1a73e8>作者：</font>** Egor Cherepanov, Nikita Kachaev, Daniil Zelezetsky 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models predict chunks of future actions from the current observation, an assumption that fails under partial observability, where decisions depend on information no longer visible. Existing memory-augmented VLAs simultaneously introduce recurrence, retrieval, compression modules, auxiliary objectives, hierarchical memory, or task-specific architectural changes, so the contribution of recurrence itself remains entangled with surrounding machinery. We present a controlled isolation study of recurrence in a strong pretrained VLA backbone. Our formulation augments the transformer with a small set of learnable memory tokens carried across timesteps and updated through self-attention, trained end to end with truncated backpropagation through time, with no auxiliary losses and no architectural changes. We instantiate this as $\mu$VLA, a family of OpenVLA-OFT variants parameterized by memory width m, TBPTT length K, and the memory update rule (cross-step gradients or a detached EMA), so that recurrence is the only varying factor. On MIKASA-Robo, $\mu$VLA improves average success rate on five training tasks from 0.42 to 0.84 at the strongest setting and reaches 0.23 on held-out tasks with the same memory structure versus 0.07 for the memoryless baseline. On tasks requiring different memory structure, performance remains near baseline. On LIBERO, the strongest recurrent variant achieves 96.2% average success, indicating no regression under full observability. We interpret these results as a calibration of the capability envelope of minimal in-backbone recurrence, identifying the regime in which it is sufficient and the regime where additional memory structure is required. Demos and videos can be found in this https URL.

---


### 11. [From Parameters to Feature Space: Task Arithmetic for Backdoor Mitigation in Model Merging](https://arxiv.org/abs/2606.12498)

**<font color=#1a73e8>作者：</font>** Zhenqian Zhu, Yamin Hu, Yiya Diao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model merging (MM) has gained significant attention as a cost-effective approach to integrate multiple task-specific models into a unified model. However, recent work reveals that MM is highly susceptible to backdoor attacks. Existing defenses based on task arithmetic often fail to eliminate backdoors without substantially degrading clean-task performance, owing to their reliance on direct parameter-space editing. To address this gap, we propose Linear Feature Path Minimization (LFPM), a backdoor mitigation framework for model merging, which introduces an anti-backdoor task vector into the backdoored merged model. Unlike prior approaches, LFPM formulates the backdoor robustness of the merged model from a unified feature-space perspective under the Cross-Task Linearity (CTL) framework, which leverages the approximate linearity of features across tasks. This perspective guides the optimization of the anti-backdoor task to suppress backdoors while preserving clean-task performance. Furthermore, we introduce an effective optimization mechanism based on gradient accumulation and loss path-integral, ensuring robust backdoor suppression along the interpolation path. Extensive experiments demonstrate that LFPM consistently exhibits strong robustness against backdoor attacks in both full fine-tuning and Parameter-Efficient Fine-Tuning (PEFT) settings.

---


### 12. [Improving Crash Frequency Prediction from Simulated Traffic Conflicts Using Machine Learning Based Microsimulation](https://arxiv.org/abs/2606.12500)

**<font color=#1a73e8>作者：</font>** Xian Liu, Carlo G. Prato, Gustav Markkula  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic microsimulation combined with surrogate safety measures has increasingly been used as a proactive alternative to historical crash data for predicting crash frequency for current or planned road infrastructure designs. However, existing microsimulation-based safety studies have adopted simplified rule-based behaviour models, which reproduce traffic flow reasonably well but often fail to generate realistic conflict dynamics, limiting crash prediction accuracy. Recent advances in machine learning (ML)-based behaviour models offer a promising opportunity to potentially improve microsimulation realism and crash frequency predictions by learning human driving behaviour directly from large-scale trajectory datasets. To investigate this possibility, traffic microsimulation was conducted for five real-world signalised intersections in Leeds, UK, using both a standard rule-based model and a state-of-the-art ML model. Simulated vehicle trajectories were analysed using a two-dimensional Time-to-Collision metric to identify simulated conflicts, which were then modelled using Extreme Value Theory to predict crash frequency. Results show that conflicts from the ML model yielded crash predictions in line with the real-world crash data, whereas the rule-based model did not permit meaningful predictions, presumably due to a lack of model calibration to the specific simulated intersections. Directly using ML-generated simulated crashes to predict real-world crash frequency also yielded poor results, suggesting that while current ML models can realistically reproduce conflicts, they are not yet able to generate realistic crashes. Overall, the findings demonstrate that ML-based behaviour models are promising for improving crash prediction from simulated conflicts, without a need for location-specific model calibration, and suggest clear future directions for ML-based traffic microsimulation.

---


### 13. [Policy-driven Conformal Prediction for Trustworthy QoT Estimation](https://arxiv.org/abs/2606.12501)

**<font color=#1a73e8>作者：</font>** Kiarash Rezaei, Omran Ayoub, Paolo Monti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Conformal QoT, a policy-driven framework that combines statistically guaranteed QoT estimation with operational decision policies, enabling reliable lightpath-feasibility predictions under domain shift and improving accuracy from 92\% to 99.6\% on open datasets.

---


### 14. [Dolph2Vec: Self-Supervised Representations of Dolphin Vocalizations](https://arxiv.org/abs/2606.12503)

**<font color=#1a73e8>作者：</font>** Chiara Semenzin, Faadil Mustun, Roberto Dessi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) has opened new opportunities in bioacoustics by enabling scalable modeling of animal vocalizations without the need for expensive manual annotation. However, current SSL models in this domain prioritize broad generalization across species and are not optimized for uncovering the fine-grained structure of individual communication systems. In this work, we collect and release a novel dataset of over five years of longitudinal recordings, from five known dolphins in a semi-naturalistic marine environment, an unprecedented resource for studying dolphin communication. We adapt the Wav2Vec2.0 Baevski et al. (2020) architecture to this domain and introduce Dolph2Vec, the first large-scale, species-specific SSL model trained exclusively on this data. We benchmark our model on two biologically relevant tasks: signature whistle classification and whistle detection. Dolph2Vec significantly outperforms general-purpose baselines in both tasks. Beyond performance, we show that learned embeddings and codebook structure capture interpretable acoustic units aligned with dolphin whistle categories and possibly sub-whistle structure, enabling fine-grained analysis of communication patterns. Our findings demonstrate how SSL can serve as both a model and a scientific tool to explore hypotheses in animal communication research.

---


### 15. [Boosting Direct Preference Optimization with Penalization](https://arxiv.org/abs/2606.12505)

**<font color=#1a73e8>作者：</font>** Pengwei Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline preference optimization has become a practical substitute for reinforcement learning from human feedback, but pairwise objectives such as Direct Preference Optimization (DPO) and its variants use only the chosen and rejected responses stored in a static dataset. This leaves a useful signal unused: the response that the reference model itself would generate for the same prompt. We propose Direct Preference Optimization with Penalization (DPOP), a simple extension of DPO that augments the base preference loss with a gated penalty on reference-greedy responses. DPOP activates this penalty only when the current policy still assigns a lower likelihood to the preferred response than to the rejected response. On AlpacaEval 2.0, DPOP improves length-controlled win rate over DPO, SimPO, and AlphaDPO on both Llama-3-8b-it and Gemma-2-9b-it, achieving relative gains of 5.3\% and 4.4\% over baselines on the two models, respectively. Ablations further show that a SimNPO-style length-normalized penalty is stronger than NPO and token-level unlikelihood in this setting.

---


### 16. [Crossing the Validation Crisis: Cross-Validation Reduces Benchmarking Variance Surprisingly Well](https://arxiv.org/abs/2606.12552)

**<font color=#1a73e8>作者：</font>** Célestin Eve, Gaël Varoquaux, Thomas Moreau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning progresses through empirical work, benchmarking new methods to evaluate relative performance. However, the statistical variability inherent to evaluation - exacerbated by the stochastic nature of many algorithms - often makes performance estimation unreliable due to the limited test samples available, leading to a validation crisis in which genuine advances are difficult to discern. In this work, we show that cross-validation improves markedly confidence when evaluating and comparing learning algorithm performances. We introduce the concept of sample gain, which quantifies the virtual data augmentation achieved by using multiple cross-validation splits to reduce benchmarking variance. Experiments on both synthetic and real-world datasets (histopathologic scans and NLP fine-tuning) demonstrate that multiple splits can substantially improve the reliability and stability of performance estimates, with diminishing returns often setting in later than expected. We also introduce a procedure to dynamically early-stop cross-validation by estimating from the first few folds if subsequent folds will bring large sample gains. Our findings highlight the value of pushing cross-validation on available samples to achieve robust and reliable benchmarking.

---


### 17. [HairPort: In-context 3D-aware Hair Import and Transfer for Images](https://arxiv.org/abs/2606.12562)

**<font color=#1a73e8>作者：</font>** Alireza Heidari, Amirhossein Alimohammadi, Wallace Michel Pinto Lira 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transferring hairstyles between images is an important but challenging task in computer graphics, computer vision, and visual effects. It enables users to explore new looks without physically altering their hair, with applications in virtual try-on systems, augmented reality, and entertainment. Most prior works operate best under small pose gaps, and they fall short under large viewpoint and scale differences, where missing hair content must be synthesized rather than transferred. We propose HairPort, a 3D-aware hairstyle transfer framework that attempts to solve these issues by explicitly separating hair removal from transfer and enforcing geometric consistency before synthesis. We introduce a Bald Converter, which produces realistic bald versions of faces through LoRA-based in-context adaptation of FLUX.1 Kontext. To train our Bald Converter, we introduce a new dataset, Baldy, containing 6,000 paired bald and original images across diverse identities and conditions. We also use a 3D-Aware Transfer Pipeline that reconstructs and re-renders the reference hairstyle from the target viewpoint before compositing it onto the source image. Being 3D aware, our method supports large pose and scale discrepancies between the source and target. Finally, a conditional flow-matching generator synthesizes the transferred result from the bald source and geometry-aligned reference guidance. Together, our method enables accurate, pose-consistent, and identity-preserving hairstyle transfer, outperforming existing methods both qualitatively and quantitatively.

---


### 18. [Arbor: Tree Search as a Cognition Layer for Autonomous Agents](https://arxiv.org/abs/2606.12563)

**<font color=#1a73e8>作者：</font>** Neha Prakriya, Chaojun Hou, Zheng Gong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Arbor is a multi-agent framework that introduces structured tree search as a cognition layer for autonomous agents operating in large, stateful action spaces. Prior autonomous optimization systems operate on isolated targets with stateless evaluation. Arbor instead maintains an explicit search tree of scored hypotheses that serves as the shared working memory across agents, evolving with every measurement, treating failures as diagnostic signal that reshapes subsequent exploration, and expanding as prior successes shift the bottleneck distribution.
We validate Arbor on full-stack LLM inference optimization, a domain where achieving peak performance has historically required coordinated effort from engineering teams across the application, framework, compiler, kernel, and hardware stack. Arbor pairs an Orchestrator agent, which drives optimization by delegating to Domain Specialists across the inference stack, with a Critic agent that safeguards stability through root-cause analysis, introspection, and measurement validation -- a checks-and-balances architecture where neither agent can unilaterally drive the system. Agent capabilities are decomposed into hard skills (domain expertise) and soft skills (coordination protocols that determine how contributions compose), enabling fully autonomous multi-day campaigns. Arbor achieves up to 193% inference throughput-latency Pareto improvement over vendor-optimized baselines, while a single agent without the harness plateaus at +33% throughput improvement and crashes irrecoverably within hours. Arbor generalizes to multiple generations of hardware platform, and run-to-run variance is within 2 percentage points demonstrating that the method is hardware-agnostic and reproducible.

---


### 19. [EDEN: A Large-Scale Corpus of Clinical Notes for Italian](https://arxiv.org/abs/2606.12569)

**<font color=#1a73e8>作者：</font>** Tiziano Labruna, Guido Bertolini, Pietro Ferrazzi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present EDEN (Emergency Department Electronic Notes), a new and unique large-scale corpus of clinical notes produced in Emergency Departments of Italian hospitals. The corpus, in its current version, is composed of approximately 4 million clinical notes fully anonymized, covering diverse phases of patient care during the stay in the emergency department. In addition, a subset of about six thousand notes has been manually annotated by clinical experts through a structured Case Report Form (CRF) containing 132 items relevant for two patient situations in emergency departments, dyspnea and loss of consciousness. Items may assume numerical values (e.g., for blood saturation), categorical (e.g., for level of consciousness ), binary (e.g., for presence of traumas), and mixed value types. The annotation process involved multiple clinicians and underwent iterative revision to resolve ambiguities in item formulation, resulting in a richly structured (although high imbalanced) resource. The dataset aims to fill a relevant gap of data able to support both the development and the use of Large Language Models in concrete medical applications. We describe the data collection protocol, the on-site anonymisation pipeline, corpus statistics, and the annotation scheme. Finally, we propose CRF-filling as a novel structured information extraction benchmark, and provide zero-shot baseline resulting from Gemma-27B and MedGemma-27B. To the best of our knowledge, the EDEN dataset is the largest freely available corpus of clinical notes existing for the Italian language.

---


### 20. [High-Fidelity Two-Step Image Generation via Teacher-Aligned End-to-End Distillation](https://arxiv.org/abs/2606.12575)

**<font color=#1a73e8>作者：</font>** Dongyang Liu, Ruoyi Du, David Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step diffusion distillation has become increasingly mature for 4-8-step generation, yet pushing further to 2 steps remains challenging. In this work, we introduce Z-Image Turbo++, a high-quality 2-step image generation model distilled from the 8-step Z-Image Turbo teacher. Our method addresses the central bottlenecks of increased task difficulty and limited model capacity in 2-step generation through three simple but effective design choices tailored to this regime. First, we propose Distribution-Aligned Adversarial Learning, which uses teacher-generated images rather than external real images as real samples for GAN training, providing a more attainable and informative adversarial target. Second, we adopt Step-Decoupled Parameterization, assigning independent model parameters to the two denoising steps to better match their distinct capacity demands. Third, we perform End-to-End Training with Iterative Regularization, allowing the first step to receive gradients from final image quality while preserving a meaningful intermediate generation through an explicit step-1 loss. Together, these designs substantially narrow the quality gap between 2-step and 8-step generation in both qualitative and quantitative evaluations, highlighting the potential of carefully tailored distillation strategies for improving the quality-efficiency trade-off in few-step generation.

---


### 21. [Helping Figures Tell their Story! Paper-Grounded Video Generation Explaining Complex Scientific Figures](https://arxiv.org/abs/2606.12576)

**<font color=#1a73e8>作者：</font>** Ishani Mondal, Javad Baghirov, Jordan Boyd-Graber  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific figures compress complex pipelines into a single canvas, yet understanding them requires paper-grounded, step-by-step narration aligned with visual highlights a capability missing from current video generation systems and benchmarks. To address this, we introduce paper-grounded figure-to-video generation: generating narrated, region-grounded walkthrough videos from a figure and its paper. We propose MINARD (Multimodal Interpretation of Narrated Architecture via Region Decomposition), a pipeline that generates paper-grounded narrations and sequentially grounds them to figure regions. We also release FigTalk, a benchmark with new sequential and component-level grounding metrics derived. On FigTalk, MINARD generates humanlike, paper-faithful narrations and outperforms narration-conditioned figure spatial grounding compared to existing approaches in both automatic and human evaluation

---


### 22. [MARD: Mirror-Augmented Reasoning Distillation for Mechanism-Level Drug-Drug Interaction Prediction](https://arxiv.org/abs/2606.12578)

**<font color=#1a73e8>作者：</font>** Mohammadreza Riyazat, Vian Lelo, Rameen Jafri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mechanism-level drug-drug interaction (DDI) prediction requires identifying which enzyme or pharmacodynamic axis is implicated, in which direction, and with which evidence -- not merely whether two drugs interact. We introduce a reproducible mechanism-level DDI labelling and evaluation protocol with a structured 7-family/147-subtype taxonomy, leakage-safe cold-split protocols, and auditable reasoning metrics for evaluating pharmacological prediction beyond flat interaction classification. We propose a pipeline that produces a 7B reasoning MARD (Mirror-Augmented Reasoning Distillation), combining three training innovations: a single-token KL divergence on direction tag that ties the model's prediction, per-loss PRM-weighted DPO with programmatic hard negatives, and a leakage-safe mechanism-aware retrieval channel. Process-reward step labels are automatically verifiable against DrugBank-structured fields, requiring no human or LLM judges. On the April-2026 DrugBank release, our MARD-7B is the only system in a 32-system comparison whose accuracy survives drug-pair novelty, beating the best baseline by +13.9 pp and GPT-4o by +6.7 pp at ~1% of frontier API cost. Further analysis reveals an anti-memorisation signature where accuracy improves on rarely seen drugs, suggesting that gain comes from structured pharmacological reasoning rather than drug-frequency memorisation. We release corpus, DDI-PRM, retrieval index, and training code.

---


### 23. [Strategic Decision Support for AI Agents](https://arxiv.org/abs/2606.12587)

**<font color=#1a73e8>作者：</font>** Shayan Kiyani, Sima Noorani, George Pappas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditionally, decision support studies how humans use machine learning models to make better decisions. In modern agentic systems, this division of roles is increasingly reversed: AI agents act on behalf of users, while humans and tools becomes support mechanisms around them. This role reversal brings reliability concerns to the forefront, since agentic errors can be consequential and agent behavior must remain aligned with human goals and constraints. Departing from the classical view of decision support, we revisit its two basic principles, the cost--value tradeoff of seeking support and the role of uncertainty quantification, in a setting where AI agents are the central actors. We propose a framework for strategic decision support for AI agents through an optimization problem that minimizes support usage subject to controlling a counterfactual missed-support error: the probability that the agent acts alone on instances where support would have materially improved its output. At the population level, we show that the optimal policy is a threshold rule on the value of support. Building on this structure, we develop an online algorithm that adaptively thresholds such a score and uses randomized exploration to control missed-support error without distributional assumptions. We further introduce a calibration-on-the-fly method that reduces unnecessary support calls online. We instantiate this framework across diverse scenarios, including information gathering, human--AI collaboration, and tool use, showing how each can be modeled through the same strategic decision-support lens. Experiments across these settings show that our method reliably controls the target error while substantially reducing support usage in practice.

---


### 24. [Pythagoras-Prover: Advancing Efficient Formal Proving via Augmented Lean Formalisation](https://arxiv.org/abs/2606.12594)

**<font color=#1a73e8>作者：</font>** Joshua Ong Jun Leang, Zheng Zhao, Mihaela Cătălina Stoian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern Lean theorem provers achieve strong performance only with substantial training and inference compute, driven in part by scarce verified proof data and the long reasoning traces of formal proof search, making both supervised fine-tuning (SFT) and sampling expensive. We introduce Pythagoras-Prover, a compute-efficient open-source family of Lean theorem provers built for practical compute budgets. The family spans two generation paradigms: autoregressive models at 4B and 32B parameters, and a first proof-of-concept diffusion-based prover (4B) that iteratively refines Lean proofs at inference time. For training efficiency, we build a Lean-verified corpus stratified into easy, medium, and hard problems for curriculum SFT, so models acquire proof skills progressively from shorter, simpler proofs to longer, harder ones. During SFT, a dynamic proof-reasoning filtering scheme preserves informative proof traces while keeping each instance within an 8k-token context budget. We also introduce Augmented Lean Formalisation (ALF), which expands scarce verified corpora into variants of formal statements, populated via self-distillation for extra training signal without formally verifying every mutated instance. By perturbing known problems while preserving their formal character, ALF reduces reliance on any statement's surface form. Empirically, Pythagoras-Prover-4B surpasses DeepSeek-Prover-V2-671B at pass@32 on MiniF2F-Test (86.1% vs 82.4%) with ~167x fewer parameters, while Pythagoras-Prover-32B sets the open-source state of the art at 93.0% on MiniF2F-Test and solves 93 of 672 PutnamBench problems. We release MiniF2F-ALF, an ALF-mutated contamination-sensitive benchmark on which every evaluated model loses accuracy; here our 32B remains strongest and our 4B matches the prior state of the art, Goedel-Prover-V2-32B.

---


### 25. [Dual-State Slot Attention: Decoupling Appearance and Identity for Video Object-Centric Learning](https://arxiv.org/abs/2606.12601)

**<font color=#1a73e8>作者：</font>** Sieu Tran, Duc Nguyen, Hao Vo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised video object-centric learning aims to decompose dynamic scenes into persistent, object-level representations without supervision. However, existing slot-based methods struggle to maintain stable object identity in challenging settings such as rapid motion and partial occlusion. First, they typically encode both the per-frame appearance of an object and its identity across frames in a single slot vector, creating an objective conflict that leads to slot swapping: reconstruction requires sensitivity to transient visual changes, whereas temporal consistency requires invariance to them. Second, the token renormalization used in Slot Attention can amplify weakly attending slots, allowing them to absorb tokens from other objects and destabilize slot-to-object correspondence.
We propose Dual-State Slot Attention (DSSA), a fully self-supervised framework that addresses these limitations by separating appearance from identity and by reducing spurious updates from weakly matching slots. DSSA decomposes each slot into a local state for per-frame appearance and an identity state for temporally stable object information, thereby aligning reconstruction and temporal consistency with separate representations. The identity state is updated through a learned recurrent transition that acts as a temporal filter on the local state, while competition-modulated aggregation (CMA) down-weights updates from weakly matching slots and prevents them from absorbing tokens from other objects. Experiments on MOVi-C, MOVi-D, and YouTube-VIS demonstrate that DSSA consistently improves segmentation quality and temporal consistency over prior methods, while also yielding stronger downstream object recognition and video dynamics prediction. Code and models will be made publicly available upon acceptance.

---


### 26. [Evaluation of AutoML Frameworks for IDS under Imbalanced Data Conditions of the NSL-KDD Dataset](https://arxiv.org/abs/2606.12611)

**<font color=#1a73e8>作者：</font>** Wiliane Carolina Silva, Evandro César Vilas Boas, Felipe A. P. de Figueiredo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work investigates the impact of severe class imbalance on the performance of automated machine learning (AutoML) frameworks for multiclass network intrusion detection using the NSL-KDD dataset. Unlike previous studies that simplify the problem through binary classification or minority-class removal, we preserve the original five-class distribution, including highly underrepresented attacks such as R2L and U2R, enabling a realistic evaluation of imbalance-sensitive learning behavior. Nine open-source AutoML frameworks were analyzed under a unified and reproducible experimental protocol, considering differences in architectural design, ensemble strategies, validation procedures, hyperparameter optimization, and imbalance-handling mechanisms. The results demonstrate that frameworks incorporating ensemble learning and imbalance-aware optimization achieve better minority-class discrimination. PyCaret obtained the best overall performance, reaching 66\% macro-F1, followed by AutoGluon with 55\%, whereas frameworks lacking native balancing support exhibited significant degradation in minority-class detection capability. The analysis further shows that accuracy-oriented optimization alone is insufficient for highly imbalanced IDS scenarios, since high-weighted metrics may coexist with poor generalization on rare attack categories. As a contribution, this work establishes a standardized benchmark for AutoML-based intrusion detection under severe multiclass imbalance, highlighting current architectural limitations and the need for native integration of imbalance-aware optimization, resampling, and stratified evaluation strategies into automated learning pipelines. The source code is publicly available.

---


### 27. [Towards Provably Fair Machine Learning: Bayesian Approaches For Consistent and Transparent Predictions](https://arxiv.org/abs/2606.12615)

**<font color=#1a73e8>作者：</font>** Owen O'Neill, Fintan Costello  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ML classifiers deployed in high-stakes domains produce predictions whose quality varies systematically across subgroups. For granular subgroups defined by intersections of multiple features, predictions are often inconsistent with the observed data: the model's outputs contradict the evidence available for that subgroup. This problem is exacerbated by regularisation, which improves aggregate performance by collapsing small subgroups into larger groups, disproportionately affecting demographic minorities. We define two requirements for consistent prediction: determinism (identical individuals receive identical predictions) and statistical consistency (we cannot reject, at significance level alpha, the hypothesis that the predictions for a subgroup were drawn from the Bayesian optimal target distribution inferred for that subgroup). From these requirements we derive the Fair Bayesian classifier, which enforces both across every group and subgroup simultaneously and abstains whenever no consistent deterministic prediction is possible. On three benchmark datasets (Adult, COMPAS, and Bank Marketing), standard classifiers produce statistically inconsistent predictions for a substantial proportion of subgroups. Our classifier achieves zero consistency error by construction while exceeding baseline accuracy and multicalibration on every dataset tested. Statistical consistency provides a principled foundation for prediction quality with direct implications for algorithmic fairness. Minority demographics are disproportionately concentrated in small subgroups, precisely where frequentist inference is least reliable; addressing this inference problem is therefore a necessary step toward fair ML. By enforcing Bayesian consistency at the finest resolution the data supports, the our classifier demonstrates that exhaustive subgroup fairness with principled abstention is achievable in practice.

---


### 28. [PersonaDrive: Human-Style Retrieval-Augmented VLA Agents for Closed-Loop Driving Simulation](https://arxiv.org/abs/2606.12616)

**<font color=#1a73e8>作者：</font>** Mahmoud Srewa, Praneetsai Iddamsetty, Mohammad Abdullah Al Faruque 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Closed-loop driving simulators typically populate their environments with non-ego traffic agents that behave largely the same way, produced either by rule-based traffic managers or by learned models trained toward a single behavioral mode. Recent work introduces style variation through post-hoc labels on observational data or LLM-inferred reward weights, but these signals act as proxies for what a style should reward rather than demonstrations of humans explicitly asked to drive in that style. We introduce PersonaDrive, a pipeline that conditions a vision-language-action (VLA) driving agent on retrieved demonstrations from a style-instructed human driving dataset, in which participants drive CARLA leaderboard routes under aggressive, neutral, and conservative instructions on a driver-in-the-loop rig. The pipeline has three stages: (i) offline triplet mining over per-style human driving data using a combined image-text similarity score; (ii) training a lightweight retrieval head that fuses frozen visual features with a small control encoder over per-style databases; and (iii) fine-tuning a single VLA backbone to treat retrieved context points as in-context behavioral demonstrations during waypoint prediction. At inference, the same backbone is conditioned on any style by swapping which per-style database the retrieval head queries, so selecting a style requires no per-style retraining while enabling human-style, style-diverse non-ego agents for closed-loop simulation. On Bench2Drive, PersonaDrive (no style) improves the driving score by 4.6% over SimLingo and 2.5% over HiP-AD, and under style conditioning attains the highest driving score in every style within a roughly 2% band (its weakest style surpassing the strongest baseline, DMW, by 5.4%), while average speed and acceleration rise by 18% and 25% from the conservative to the aggressive instruction.

---


### 29. ["Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms](https://arxiv.org/abs/2606.12618)

**<font color=#1a73e8>作者：</font>** Alan Cooney, David Africa, Geoffrey Irving  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Robust lie detectors for language models could enable powerful techniques for auditing, monitoring, and post-hoc investigation of model behaviour, but evaluating them requires testbeds where models verifiably believe the opposite of what they say. We show that existing trained model organisms often fail this requirement, leaving prior positive and negative detection results difficult to interpret. We address this with 13 reasoning model organisms whose hidden beliefs are verified in chain-of-thought and shown to generalise to held-out tasks, alongside Varied Deception, a prompted-lying testbed covering a broad range of lie-inducing motivations. On these testbeds we evaluate four detectors: a chain-of-thought judge, a logprob classifier, and two activation probes, including Did-You-Lie (DYL), a new method for training follow-up probes. On prompted lying, across 31 open-weight models spanning 2B to 1T parameters, all four detectors show positive scaling with model capability. However, every activation- and logprob-based detector drops sharply on our trained model organisms, with DYL retaining the most signal; only the chain-of-thought judge remains strong, with 0.82 balanced accuracy, partly as an artefact of our verification process favouring CoT-readable beliefs. Current lie detectors therefore cannot support high-confidence claims about model beliefs, and we suggest research directions that may address some of their current limitations. We release our datasets, model organisms, and trained detectors.

---


### 30. [Context-Aware Feature-Fusion for Co-occurring Object Detection in Autonomous Driving](https://arxiv.org/abs/2606.12628)

**<font color=#1a73e8>作者：</font>** Binay Kumar Singh, Niels Da Vitoria Lobo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection in autonomous driving requires precise localization and an inherent understanding of the relational context between co-occurring objects. In extremely complex heterogeneous environments rare classes, small-scale objects, and frequently appearing objects are difficult for standard object detection frameworks to handle. In this paper, we propose a novel framework called Context-Centric Feature Fusion (CCFF), which utilizes two attention-based modules, Local Context Fusion Module (LCFM) uses the RoI-to-RoI self-attention mechanism to resolve spatial interactions, mainly considering small and partially obscured objects, while Global Context Attention Module (GCAM) converts the co-occurrence of objects priors by pooling top-K RoI features into a global context attention token, avoiding the computational overhead of pixel-level global pooling. This fusion of local and object-centric global features yields contextualized embeddings that enhance classification results and co-occurring objects detection. Our method is evaluated on two datasets, Cityscapes and BDD100K which demonstrate significant improvement on relational consistency, achieving a Category-level Consistency Strategy (CCS) of 0.973 and 0.969, respectively. Furthermore, our approach produces substantial gains in small object detection (AP_S: 14.1%) and successfully recovers rare classes such as "Train" that are typically lost in large distributions. Our efficiency report shows that the framework processes images in real time with a 0.2 FPS overhead. The code is available at this https URL.

---


### 31. [Bag of Dims: Training-Free Mechanistic Interpretability via Dimension-Level Sign Patterns](https://arxiv.org/abs/2606.12629)

**<font color=#1a73e8>作者：</font>** Varun Reddy Nalagatla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that the standard basis of transformer hidden states already provides a training-free, architecture-general feature basis. Individual dimensions encode semantic content via their signs and confidence via their magnitudes, functioning as independent binary registers. We validate this Bag of Dims framework across three model families (Qwen 3.5-4B, Gemma 3-4B, Mistral 7B) through four progressive experiments. Sign patterns alone carry predictive content: replacing all magnitudes with unity achieves 72-93% top-5 next-token accuracy through the LM head, and pure Hamming scoring without any decoder reaches 80-90% top-4096. These sign patterns organize into semantic features: using a single-token type cache (one forward pass per vocabulary token, no context), we discover 175 categories via per-dimension sign consistency (mean AUC 0.80) from 50 anchors with zero training. A trained probe adds only +0.018 AUC and converges to axis-aligned weights, confirming negligible cross-dimension structure. This structure extends to attention: all 175 categories remain discoverable in K and V projections. On the write side, static FFN weight inspection links 20% of features to individual writer neurons (>0.70 agreement; random controls: 0%), with top-200 neuron coalitions achieving >0.70 agreement on 99.9% of prototypes via majority vote. Fully unsupervised discovery (random seeds, no labels) scales to 1500 features at 100% yield and 99% sparsity across all three models, with pairwise MI of 0.0014 bits confirming low inter-dimension coupling. These results establish that the standard basis already suffices for feature reading throughout the transformer compute pathway, requiring no training, no optimization, and no GPU-days beyond a single forward pass per vocabulary token.

---


### 32. [Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2606.12634)

**<font color=#1a73e8>作者：</font>** Tianyu Ding, Jianhong Xin, Juan Pablo De la Cruz Weinstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon tool-use reinforcement learning can learn from outcome verification, but its
trajectory-level advantage is broadcast across many reasoning, API, and answer tokens.
Self-distillation promises a denser signal by reusing a policy's own rollouts or a privileged
teacher. We show, however, that direct token-level self-distillation can silently destroy tool use:
it rehearses teacher behavior without knowing which actions the verifier rewards, so useful skills
and harmful shortcuts are amplified together. We introduce Sibling-Guided Credit Distillation
(SGCD), which uses distillation for credit assignment rather than as a competing actor loss.
Dynamic sampling produces mixed successful and failed sibling rollouts; an external LLM summarizes
their contrast into a training-only stepwise credit reference; dense teacher/student divergence
drives credit reassignment; and bounded detached credit weights reshape GRPO token advantages. The
deployed student sees no external LLM, sibling evidence, or oracle. Across AppWorld and
$\tau^3$-airline, SGCD improves over matched GRPO comparators: AppWorld TGC $42.9 \to 45.6$ on
test_normal and $24.7 \to 27.0$ on test_challenge, and $\tau^3$-airline pass@1 $0.583 \to 0.602$.

---


### 33. [CD-RCM: Generalizable Continuous-Depth Novel View Synthesis for Reflectance Confocal Microscopy](https://arxiv.org/abs/2606.12635)

**<font color=#1a73e8>作者：</font>** Tooba Imtiaz, Milind Rajadhyaksha, Kivanc Kose 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reflectance confocal microscopy (RCM) provides noninvasive, cellular-resolution "optical biopsies" of human skin \emph{in vivo} by acquiring en-face images at successive depths, forming a sparse z-stack. Due to optical limitations, these stacks are anisotropic 3D volumes with lateral resolution (0.5 $\mu$m) $\sim$6 times higher compared to axial resolution, which is defined by the optical sectioning (3 $\mu$m), limiting the interpretation of tissue. Our goal is to provide continuous-depth visualization by interpolating intermediate sections and making the 3D volume isotropic. Such a representation permits arbitrary-direction sectioning, including histopathology-like cross-sectional examination, without requiring per-patient optimization. To that end, we introduce the first RCM-specific novel-view synthesis (NVS) approach, CD-RCM, a feedforward model that predicts realistic, unseen depths from sparsely sampled RCM stacks. Classical neural rendering methods focus on reconstruction from surface-level multi-view observations. In contrast to surface-level camera views, RCM can acquire optically sectioned en-face images of tissue beyond the surface up to 200 $\mu$m. However, during visualization of the RCM stacks, observations of the shallower sections (towards the surface) obscure the deeper ones. This unique axial imaging geometry and layer-dependent anatomical organization motivated our development of a tailored architectural and training framework that explicitly accounts for RCM's depth-resolved, occlusive imaging physics. Experiments demonstrate that CD-RCM achieves high-fidelity novel-view synthesis with sub-second inference time.

---


### 34. [The Metric Picks the Winner: Evaluation Choice Flips Model Rankings for Drug-Response Prediction in Unseen Chemistry](https://arxiv.org/abs/2606.12639)

**<font color=#1a73e8>作者：</font>** Dhruv Agarwal, Riya Bisht  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting how a cell's transcriptome responds to a drug it has never seen is a core, hard problem in computational cell biology: recent benchmarks show complex models often fail to beat trivial baselines once test compounds are held out by chemistry. We study one cell line and assay, THP-1 cells profiled by DRUG-seq, scored by the active-compound weighted MSE(wMSE) of the VCPI prediction contest. We propose a staged approach: dumb baselines (untreated control and mean training-compound response) that the field keeps failing to beat; non-parametric retrieval (a Tanimoto-weighted average of a held-out compound's nearest training compounds); and a fusion stage combining a frozen chemistry embedding with retrieval-support features to predict the residual over the mean, with an uncertainty head and gene programs. On the released VCPI THP-1 drug-seq data (14,026 training compounds), under a Bemis-Murcko scaffold split, the model ranking inverts depending on the metric. Under an inverse-variance per-gene proxy, a regularized linear regression on Morgan fingerprints appears to win over the deep models, retrieval, and ChemBERTa -- the textbook "simple baselines win" result. But under the contest's true active-set metric (per-(gene, compound) Mejia weights, validated against the official scorer; mean baseline 0.535 vs the organizers' 0.507 reference), that reverses: the deep models win, our fusion decoder significantly beats the linear fingerprint baseline (-0.012 wMSE, paired bootstrap p < 10^-4), and the proxy's winner becomes the worst chemistry-aware predictor. Picking the metric picks the winner -- to our knowledge the first demonstration on real held-out drug chemistry of the metric-calibration effect established largely on genetic perturbation. We release a reproducible pipeline
wired to the official scorer that emits a valid submission over the real 1064 x 12,995 grid.

---


### 35. [Individual Control Barrier Functions-Guided Diffusion Model for Safe Offline Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2606.12640)

**<font color=#1a73e8>作者：</font>** Qingyun Guo, Junyi Shi, Jianuo Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning allows control policies to be learned directly from data without online interaction, making it suitable for safety-critical tasks. Recent studies have applied diffusion models to offline reinforcement learning to leverage their strong capacity for modeling complex data distributions. However, existing approaches primarily focus on single-agent settings, leaving the safety challenges in multi-agent environments largely unexplored. In this work, we propose a safe offline multi-agent reinforcement learning algorithm that embeds neural individual control barrier functions into the diffusion model to enhance safety during trajectory generation, with control policies recovered through inverse dynamics. We evaluate our algorithm across diverse benchmarks, demonstrating substantial safety improvements while maintaining competitive rewards.

---


### 36. [TEDD: Robust Detection of Unstable Temporal Features](https://arxiv.org/abs/2606.12643)

**<font color=#1a73e8>作者：</font>** Ricardo Ribeiro Pereira, Bruno Casal Laraña, Nádia Soares 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When working with real-world temporal data, it is common to encounter features whose distribution is changing over time. The naive employment of Machine Learning models on this unstable data might lead to rapidly degrading performance, especially if the new distribution is much different from what was previously seen during training. In order to cope with this problem, it is critical to automatically identify features that are changing over time. With these features detected, data scientists and other practitioners will be able to mitigate the issue (for instance, by applying data transformations), deploying more robust models that retain high performance for longer periods of time. In this paper, we describe which temporal changes a feature should not suffer from, and propose TEDD, a technique to a) identify when a dataset might lead to an unstable Machine Learning model and b) automatically detect which features cause such lack of robustness. In order to achieve it, we leverage a regression model to highlight which features contribute to a good prediction of an instance's timestamp. We compare our approach to other methods in real and synthetic data, testing their detection capability on all simple change patterns. We show that our method: detects all types of basic changes, both for numerical and categorical features; can detect multivariate drifts; returns a comparable value measuring the amount of change of each feature; requires no parameter tuning; and is scalable both on number of features and instances of the dataset.

---


### 37. [OpenRoundup: Multi-Table Data Wrangling Through Interactive Visualization](https://arxiv.org/abs/2606.12648)

**<font color=#1a73e8>作者：</font>** Stephen Kasica, Charles Berret, Tamara Munzner  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Data journalists routinely integrate records across multiple independently published sources to support accountability reporting, yet no existing interactive wrangling tool treats the collection of tables -- rather than the single table -- as its primary unit of work. We present OpenRoundup, an open-source, browser-based system that enables data journalists to consolidate multiple tables into a single analysis-ready output without writing code. The interface comprises five coordinated panels that implement a schema-first, values-on-demand paradigm with live schema previews, ambient data quality alerts, and a recursive treemap visualization of the evolving operation tree. A client-only architecture powered by DuckDB-WASM runs in the browser, providing strong data privacy guarantees suited to sensitive journalism data. The system introduces two conceptual contributions: eager table consolidation, in which a composite table is assembled early in the wrangling phase via interactive, incremental assembly of multiple source tables; and a declarative vocabulary for table consolidation consisting of two operations, Stack and Pack. We evaluate the system through a replication study in which the authors reproduce 17 published journalist programming workflows using only the interface, and a deployment study with four professional data journalists. The replication study demonstrates expressive coverage of real-world consolidation tasks. The deployment study confirms utility for practitioners who understand joins conceptually but lack the programming skills to execute them, and surfaces an unanticipated secondary value for data journalism education.

---


### 38. [Physics-Aware Auxiliary Losses Improve Out-of-Distribution Generalization of a GNN Synthesizability Filter](https://arxiv.org/abs/2606.12651)

**<font color=#1a73e8>作者：</font>** Riya Bisht, Dhruv Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning drug-discovery pipelines increasingly rely on generative models that propose molecules far from the data used to train downstream synthesizability filters. Existing
filters (SAScore, SCScore, RAscore, DeepSA) are purely statistical and degrade in exactly this out-of-distribution (OOD) regime. We ask whether cheap, closed-form physical priors, used
as auxiliary supervision on a graph neural network (GNN), improve OOD generalization. We add two auxiliary losses to a GINE backbone: a topological complexity regression supervised by
the Bertz index, and a strain-energy soft penalty supervised by MMFF94 force-field energy. On a 65,177-molecule corpus (HIV, Tox21, COCONUT) labeled by SAScore thresholds we reproduce
a strong in-distribution baseline, then evaluate a 4-way ablation (baseline / +complexity / +strain / +both) on a single-source OOD split (train on drug-like HIV+Tox21, test on
COCONUT natural products), repeated over 5 seeds with paired bootstrap confidence intervals. All three physics-aware variants give a small but statistically significant OOD improvement
over the baseline (mean OOD AUC 0.9774): +complexity Delta = +0.0060 (95% CI [+0.0023, +0.0102]), +strain Delta = +0.0032 ([+0.0008, +0.0052]), +both Delta = +0.0066 ([+0.0038,
+0.0093]); every interval excludes zero, and the combination is best. The variants are indistinguishable in-distribution, so the effect is visible only under OOD evaluation. We are
explicit that the effects are modest, and we report a cautionary methodological finding: a single-seed version of this experiment produced a qualitatively different (non-monotone)
story that did not survive multi-seed evaluation.

---


### 39. [Amnesia: A Stealthy Replay Attack on Continual Learning Dreams](https://arxiv.org/abs/2606.12655)

**<font color=#1a73e8>作者：</font>** Ahmed Sharshar, Naveen Kumar Kummari, Mohsen Guizani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) models often use experience replay to reduce catastrophic forgetting, but their robustness to replay sampling interference remains underexplored. Existing CL attacks alter inputs or training pipelines (poisoning/backdoors) and rarely include explicit auditable constraints, limiting realism. Here, auditability means a monitor can verify compliance from sampler-visible telemetry - e.g., logged replay index/label statistics - by checking that the realized replay class histogram stays close to a nominal baseline and that replay rate is unchanged per batch and/or over a rolling window. We study a limited-privilege insider who controls only replay index selection, not pixels, labels, or model parameters, while staying within auditable limits such as queue priorities. We introduce Amnesia, a replay composition attack that maximizes degradation under two budgets: a visibility budget delta bounding the TV/KL divergence from a nominal class histogram p0, and a mass budget f fixing the replay rate. Amnesia has two steps: (i) compute lightweight class utilities, such as EMA loss or confidence, to tilt p0 toward harmful classes; and (ii) project the tilt back into the delta-ball using efficient KL (exponential tilt) or TV (balanced mass redistribution) optimizers. A windowed scheduler enforces rolling audits. Across challenging CL benchmarks and strong replay baselines, Amnesia consistently lowers final accuracy (ACC) and worsens backward transfer (-BWT). The KL variant delivers high impact while remaining largely undetected under multiple audit schemes, including per-batch and rolling-window checks. The TV variant is more damaging but easier to detect, especially under tight per-class constraints. These results expose index-only replay control as a practical, auditable threat surface in CL systems and establish a principled impact-visibility trade-off.

---


### 40. [Physics-Informed Neural Networks for Chemotherapy Pharmacokinetics: Benchmarking the Clinical Estimator and Exposing Parameter Identifiability](https://arxiv.org/abs/2606.12658)

**<font color=#1a73e8>作者：</font>** Riya Bisht, Dhruv Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) are an attractive tool for partial-observation problems in biology, where the governing dynamics are known but some compartments cannot be measured. Chemotherapy pharmacokinetics (PK) is a clean instance: drug concentration in plasma is routinely measured, but concentration in tissue -- which determines tumour kill and off-target toxicity -- is not. We benchmark a PINN against the standard clinical baseline (nonlinear least-squares on the analytical biexponential plasma solution, hereafter NLS) and a physics-agnostic neural baseline (a data-only MLP) on two PK problems. On the linear two-compartment problem, NLS is near-optimal; the PINN matches it to within a small constant factor while also producing the tissue curve in a single training pass, whereas the data-only MLP fails on tissue by roughly 10x. On a Michaelis-Menten extension (saturable elimination), the biexponential closed form no longer exists, so NLS is mis-specified and silently returns meaningless rate constants. The PINN instead exposes a deeper fact: the Michaelis-Menten two-compartment model is non-identifiable from plasma alone, and the PINN reports this honestly by converging to a basin with k12 -> 0. Adding two sparse tissue observations largely resolves identifiability: across five seeds the PINN recovers k21 to within 1% of truth and Vmax, Km to within one standard-deviation bar, while k12 moves in the correct direction (0.02 -> 0.82) but remains ~2 sigma below truth -- a recovery the closed-form NLS estimator cannot attempt at all, because its biexponential ansatz describes only plasma. Our claim is not that PINNs beat NLS. It is that PINNs offer a uniform recipe that ties the textbook estimator on the textbook problem, exposes structural identifiability that
the textbook estimator hides, and absorbs heterogeneous measurements within a single loss.

---


### 41. [CAPED: Context-Aware Privacy Exposure Defense for Mobile GUI Agents](https://arxiv.org/abs/2606.12666)

**<font color=#1a73e8>作者：</font>** Siyu Shen, Fenghao Xu, Wenrui Diao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Screenshot-based mobile GUI agents can operate ordinary smartphone apps through the same visual interface as a human user, but this capability also turns every screen observation into a privacy boundary. During normal task execution, screenshots may expose contacts, messages, photos, files, recommendations, health cues, and other sensitive context that is unrelated to the user's request. We call this problem incidental visual privacy exposure. It is difficult to address with existing defenses: text anonymization misses many visual and inferential cues, while generic privacy masking can remove the evidence and controls that a GUI agent needs to complete the task.
This paper presents CAPED, a context-aware pre-upload exposure control layer for mobile GUI agents. CAPED is designed as a phone-side protection layer: before screenshots are released to a remote multimodal agent, it extracts task requirements, uses screen context as a privacy prior, parses visible UI elements, and selectively exposes only content needed for the current task while masking incidental private content. We evaluate CAPED on AndroidWorld for broad task utility and with a controlled 28-task seeded privacy evaluation used as a measurement instrument for trajectory-level incidental leakage. In this seeded evaluation, Full CAPED reduces success-conditioned weighted seeded leakage from 0.766 under raw screenshots to 0.268 while preserving high task utility. A broader AndroidWorld run shows a remaining prototype-level utility cost, but the results support the central claim that screenshot upload should be treated as an explicit device--cloud boundary decision, governed by task-driven selective exposure rather than all-or-nothing screen sharing.

---


### 42. [SalArt-VQA: Diagnosing Whether VLMs Understand Salient Artifacts in Generated Images](https://arxiv.org/abs/2606.12671)

**<font color=#1a73e8>作者：</font>** Xiaoxiao Sun, Ruotian Zhang, Junzhe Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used to detect whether AI-generated images contain visible artifacts, yet their ability to analyze such artifacts remains poorly understood. A correct image-level decision can still hide important failures: a model may correctly flag an artifact while relying on the wrong visual cue, selecting the wrong region, or describing a defect that the image does not support. To evaluate these behaviors directly, we introduce SalArt-VQA, a diagnostic benchmark for fine-grained SALient ARTifact understanding in AI-generated images. SalArt-VQA contains 950 images and 3,681 human-authored multiple-choice questions spanning artifact images, matched real reference images, and paired generated reference images. Four aligned question types evaluate presence detection, semantic localization, spatial grounding, and evidence-grounded defect identification, while the reference splits test calibration and abstention when the annotated defect is absent. Across 20 VLMs, SalArt-VQA reveals failures that image-level detection accuracy hides: the strongest model reaches 99.37% detection recall on artifact images but answers all four artifact-side questions correctly on only 53.26% of images. Comparing artifact images with artifact-free references reveals a sensitivity-calibration tradeoff: sensitive models often make unsupported artifact claims, while conservative models avoid false alarms largely by missing real artifacts. These results show that high artifact detection accuracy alone does not imply grounded artifact understanding. SalArt-VQA exposes these hidden failure modes and provides a fine-grained evaluation of whether VLM artifact claims are supported by local visual evidence.

---


### 43. [A Zero-shot Generalized Graph Anomaly Detection Framework via Node Reconstruction](https://arxiv.org/abs/2606.12673)

**<font color=#1a73e8>作者：</font>** Phan Nguyen, Dat Cao, Hien Chu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-domain graph anomaly detection (GAD) aims to identify abnormal nodes in unseen target graphs, showing strong potential in real-world applications with heterogeneous graph data. However, existing methods often depend on dataset-specific feature semantics and structural patterns, which limits their ability to generalize across different domains. To address this challenge, we propose AlignGAD, a zero-shot generalized graph anomaly detection framework. Our framework is built upon three key components: a Global Unification Module that aligns heterogeneous node features and normalizes graph signals in the spectral domain; a Clustering Module that constructs cluster-aware graph views to capture group-level abnormal patterns; and a Node Discrepancy Scoring Module that measures reconstruction discrepancy and aggregates anomaly evidence from different graph views. Experiments on multiple real-world datasets demonstrate the effectiveness of AlignGAD under the zero-shot GAD setting.

---


### 44. [Fed-FBD: Federated Functional Block Diversification for Isolation, Privacy, and Surgical Unlearning](https://arxiv.org/abs/2606.12679)

**<font color=#1a73e8>作者：</font>** Weijie Chen, Alan B. McMillan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative model training without sharing raw patient data, but standard approaches such as FedAvg treat each client as a black box and provide no mechanism for isolating an adversarial contributor, auditing per-client influence, or honoring a departed participant's right to be forgotten. We present Fed-FBD (Federated Functional Block Diversification), a modular federated architecture that decomposes a ResNet backbone into six functional blocks (the stem, four residual groups, and the classification head) and maintains a warehouse of N color variants, each assembled from independently tracked and contributor-stamped blocks. Fed-FBD provides three capabilities absent in FedAvg: (i) architecturally guaranteed block-level isolation, so that an adversarial or mislabelled client cannot contaminate the clean colous; (ii) privacy-by-design, where membership inference advantage is already indistinguishable from chance before any privacy mechanism is applied; and (iii) surgical machine unlearning of a departed participant's contribution at sub-second cost and without retraining. Experiments on six MedMNIST-2D datasets, PathMNIST at 224x224, and CIFAR-10 show that Fed-FBD trades a modest 0.3%-3.1% IID accuracy gap on the adequately sized datasets for these guarantees, remains within 0.8%-4.0% of FedAvg at Dirichlet alpha=1.0 on three of four datasets, and confines all six adversarial attacks we study to the poisoned client's own blocks with at most +/-0.01 AUC drift on the clean colors.

---


### 45. [How Useful is Causal Invariance for Domain Adaptation in Finite-Sample Settings?](https://arxiv.org/abs/2606.12680)

**<font color=#1a73e8>作者：</font>** Julia Kostin, Kasra Jalaldoust, Elias Bareinboim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models often degrade when they are deployed on a target distribution that differs from the source distributions they were trained on. Recent work in causality-based domain generalization has shown how shared causal structure between domains can induce invariant predictors, e.g., models on a subset of features which have stable risk across structured domain shifts. However, the extent to which such population-level causal invariances can lead to gains in finite-sample settings remains underexplored. In particular, in practice we often have access to a few labeled target samples, a setting called supervised domain adaptation (sDA). In this paper, we explore when (full or partial) causal knowledge can provably improve supervised domain adaptation.
As a first step, we study linear regression, where full or partial causal knowledge specifies a collection of invariant or possibly invariant feature subsets, each yielding a source-trained candidate predictor. We derive matching upper and lower bounds showing that finite-sample gains are governed by the target-risk margins separating the candidates, together with the finite-source estimation error. When these margins are sufficiently large relative to $n_Q$, an adaptive aggregation procedure can match the best candidate predictor while avoiding negative transfer relative to target-only learning. On the other hand, when the margins are too small, no algorithm can reliably exploit the candidate collection to obtain faster finite-sample rates. We further connect these margins to structural shift magnitude in linear SCMs and validate the theory on real-world causal benchmarks.

---


### 46. [From AGI to ASI](https://arxiv.org/abs/2606.12683)

**<font color=#1a73e8>作者：</font>** Tim Genewein, Matija Franklin, Alexander Lerchner 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Over the last decade, building human-level artificial general intelligence has moved from far-fetched speculation to being a concrete next-decade target for many of the largest AI organisations. Achieving this goal would have profound and far-reaching impacts on human society, which raises many complex questions for the decade ahead. This report investigates how AI itself might continue to develop in a post-AGI world along the continuum of machine intelligence. The endpoint of this continuum, Universal AI, is theoretically well understood, which provides some formal grounding for the main focus of this report: the transition from human-level AGI to artificial general superintelligence, which, intuitively, can be understood as a system that is more intelligent and cognitively capable than large organisations of humans. After characterizing ASI, the report discusses four potential pathways from AGI to ASI: scaling AGI, AI paradigm shifts, recursive improvement, and ASI emerging from large-scale multi-agent collectives. The report then discusses possible frictions and bottlenecks along these pathways. Determining whether the impact of these frictions will be negligible or substantial raises a number of concrete open research questions. Due to large uncertainties for predicting ASI progress, it cannot be ruled out that AI progress might continue to accelerate over the next years. This could imply that the image of a single transformative step change, caused by the introduction of human-level AGI into our society, could be inaccurate. More apt might be the prospect of a series of transformative societal changes caused by AI-enabled progress and breakthroughs across many areas of science and technology. Preparing for this prospect requires a massively interdisciplinary endeavour of global scope and interest.

---


### 47. [Forecasting Is Not Attribution: Localizing Decoder Bypass in Graph-Based Neural Marketing Mix Models](https://arxiv.org/abs/2606.12687)

**<font color=#1a73e8>作者：</font>** Yunbo Wang, Bolbi Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Marketing mix models are used to forecast business outcomes and to attribute those outcomes to marketing channels, but these goals are not equivalent. We study a failure mode in graph-based neural MMM called attribution bypass: a high-capacity decoder can obtain low forecasting error through target autoregression, dense communication, co-movement, context, or latent memory while failing to route counterfactual sensitivity through the graph used as the attribution object. We introduce DICE-MMM as a bounded diagnostic and training framework. We do not claim that observational neural MMM identifies causal effects. Instead, DICE separates three questions often conflated in graph-based MMM: graph recovery, forecasting accuracy, and whether the trained decoder's perturbation-induced influence is graph aligned. Stage 1 trains a graph encoder with a restricted graph-mediated decoder. Stage 2 freezes the selected encoder and trains a graph-safe latent decoder whose cross-node communication must pass through the supplied graph. Decoder use is evaluated with CIG, AR-CIG, and graph-swap tests. Across controlled R/d/T swaps and an external multi-graph rawlog stress test, DICE improves stable graph recovery over CausalMMM. The experiments show that forecasting accuracy is not an attribution certificate: in a sparse-target benchmark, no-graph and full-graph decoders achieve MSE@7 around 0.004 while AR-CIG nAUPRC remains near or below zero, whereas an oracle graph reaches 0.807 +/- 0.129 at comparable MSE. Frozen graph-swap localizes the bottleneck: the same DICE-hard-trained decoder moves from nAUPRC -0.044 +/- 0.006 under learned graph inputs to 0.894 +/- 0.027 with the oracle graph. The contribution is a stress test and failure-localization framework showing that low MSE can hide attribution bypass and that the unresolved bottleneck is graph-support selection, not forecasting or decoder capacity.

---


### 48. [Two-Layer Linear Auto-Regressive Models Estimate Latent States](https://arxiv.org/abs/2606.12691)

**<font color=#1a73e8>作者：</font>** Yahya Sattar, Sunmook Choi, Leo Maynard-Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auto-regressive models have emerged as powerful tools for sequential data, from language to video. Understanding how and why these models learn latent representations remains an open theoretical question. In this work, we demonstrate that when trained by empirical risk minimization on data from partially observed linear dynamical systems, two-layer linear auto-regressive models naturally learn to approximate Kalman filtering. In particular, we show that the learned hidden representation coincides, up to a similarity transformation, with the state estimates produced by the optimal (Kalman) filter, even though the model has no explicit knowledge of the underlying dynamics or state. The result follows from three main insights. First, we establish that the Kalman filter is well approximated by an auto-regressive model with bounded truncation error. Second, we show that despite non-convexity, the two-layer optimization landscape is benign, i.e., all stationary points are either strict saddles or global minima. Finally, as our main contributions, we provide finite-sample guarantees on prediction error, parameter estimation error, and latent state recovery. Numerical simulations support the theoretical results and demonstrate that the latent representations of auto-regressive models recover state estimates.

---


### 49. [VLADriveBench: Evaluating CoT-Action Relationship in VLA for Autonomous Driving](https://arxiv.org/abs/2606.12706)

**<font color=#1a73e8>作者：</font>** Thach Nguyen, Danhua Guo, Tom Lampo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models generate chain-of-thought (CoT) reasoning alongside driving trajectories, but existing benchmarks evaluate only trajectory quality and do not assess whether the CoT is relevant, consistent, or causally connected to the driving action. We introduce VLADriveBench, a framework that combines observational metrics (mentioning, hallucination, contradiction, action alignment) with a CoT intervention protocol to provide complementary views of the CoT-action relationship. Applying VLADriveBench to three models across two architectures, we find that the two analyses can diverge sharply: ORION scores highest on observational alignment yet its CoT is epiphenomenal, while Alpamayo v1.5 scores lower yet its CoT is strongly causal, with visual salience gating the extent of CoT influence.

---


### 50. [AfriSUD: A Dependency Treebank Collection for Evaluating Models on African Languages](https://arxiv.org/abs/2606.12708)

**<font color=#1a73e8>作者：</font>** Happy Buzaaba, Cheikh Mouhamadou Bamba Dione, David Ifeoluwa Adelani 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite their linguistic diversity and global significance, African languages remain underrepresented in research and resources to support NLP. We aim to bridge this gap by introducing AfriSUD, the first large-scale collection of syntactically annotated treebanks for nine diverse African languages spanning major language families and regions across Sub-Saharan Africa. Using the Surface-Syntactic Universal Dependencies (SUD) framework, our community-led effort provides high-quality, native-speaker verified data that capture typological key features such as agglutination and tone. We evaluate a range of models on AfriSUD for part-of-speech tagging and dependency parsing including non-transformer baselines, multilingual pretrained encoders, and LLMs. Our results reveal a significant syntax gap, where models still show clear limitations across the nine languages, suggesting that existing architectures may not fully capture the structural diversity of African-language syntax.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-251](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
