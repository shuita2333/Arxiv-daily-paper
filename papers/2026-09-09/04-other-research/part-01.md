# 📦 其他研究 | 2026年09月09日

> 本类共 **190** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-190](./part-04.md)

---

### 1. [How Much Does Corpus Choice Change Dependency-Distance Estimates?](https://arxiv.org/abs/2609.04223)

**<font color=#1a73e8>作者：</font>** Sirui Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dependency-distance estimates derived from a single corpus are routinely treated as properties of a language, yet this assumption has not been tested across independently compiled corpora. We compared mean dependency-distance estimates across 38 same-language treebank pairs from Universal Dependencies v2.18, using concordance correlation, Bland-Altman analysis, and a twelve-specification multiverse design. Cross-treebank agreement was moderate at best: substituting one treebank for another reversed nearly 40 percent of pairwise language orderings, and treebank choice accounted for roughly 29 percent of between-group variance. This disagreement substantially exceeded within-treebank sampling error and persisted across all twelve preprocessing specifications. Nevertheless, every treebank confirmed dependency-length minimization (normalized ratio below 1). The data are more consistent with MDD as a corpus-conditioned composite of grammatical, register, and annotation factors than as a stable language-level parameter: the qualitative DLM universal survives corpus substitution, but the ordinal cross-linguistic ranking does not.

---


### 2. [EXAONE Forecast for Finance](https://arxiv.org/abs/2609.04239)

**<font color=#1a73e8>作者：</font>** Seunghan Lee, Jaehoon Lee, Jun Seo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This technical report presents EXAONE Forecast for Finance (EXAONE Finance), a financial time series (TS) foundation model (TSFM) tailored to financial forecasting. Recent TSFMs achieve strong zero-shot performance through large-scale pretraining. However, they are primarily developed for general-domain TS and largely rely on self-attention backbones whose computational cost grows quadratically with sequence length and variate count. Moreover, they assume fully observed inputs and are pretrained on corpora that fail to capture the unique dynamics of financial markets. These limitations hinder their applicability to finance, where long, many-channel, intermittently observed panels are common. To address these challenges, EXAONE Finance adopts an attention-free architecture, replacing self-attention with two simple yet effective linear-time operators: 1) a causal 1D convolution for temporal mixing and 2) a group-aware pooling multi-layer perceptron (MLP) for variate mixing. Furthermore, a masked context augmentation exposes the model to contiguous missing spans during training, improving robustness to the missingness pervasive in financial markets. EXAONE Finance is pretrained on a large-scale financial corpus covering not only equities but also foreign exchange, commodities, crypto-assets, fixed income, and macroeconomic indicators. On FinVerse, a financial forecasting benchmark covering diverse asset classes, EXAONE Finance attains state-of-the-art performance, ranking first across all three evaluation tiers---point-forecast accuracy, cross-sectional asset ranking, and portfolio profitability.

---


### 3. [Spectral-Target Physical Latent Structuring for JEPA-Style World Models](https://arxiv.org/abs/2609.04264)

**<font color=#1a73e8>作者：</font>** Penghao Zhu, Salvatore Penachio, Kaustav Mukherjee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models have become increasingly popular as a method to predict and plan in latent space rather than pixel space. Recent architectures, such as LeWorldModel (LeWM), jointly train the encoder and predictor using regularization techniques like SIGReg to prevent representation collapse. Even with such regularization preventing representation collapse, we identify a new world model failure mode of \textit{physical representation laziness}, particularly noted in highly dynamic environments. For these lazy cases, the learned latent states do not collapse but nonetheless fail to represent key physical properties, causing ubiquitous downstream planning failure. To resolve this issue, we propose training-time auxiliary supervision with a lightweight "Fourier auxiliary head", which enforces physically-informed structuring of the latent space with no additional inference-time cost and can be generalized to any environment. Experimentally, we show that the auxiliary head substantially improves planning success rates in dynamic environments where the baseline LeWM exhibits physical representation laziness. It also leads to modest improvements in other environments, even when the baseline does not exhibit physical representation laziness. We further observe superior planning performance being accompanied by higher latent space correlations with key physical properties, indicating both the ability of our method to physically structure latent states and the potential planning-side benefit to the learned representation being physically structured. We also see in low-data regimes, auxiliary supervision is particularly impactful in increasing success rate. These findings support the use of our Fourier auxiliary head method to improve both overall success rate and data efficiency, while avoiding representation laziness in latent world models.

---


### 4. [ProToMEx: Rapid, Interpretable Explanations via Structured Representations](https://arxiv.org/abs/2609.04265)

**<font color=#1a73e8>作者：</font>** Athina Georgara, Adarsh Valoor, Sarvapali D. Ramchurn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing post-hoc explainers for machine learning classifiers primarily focus on feature attribution, assigning importance scores to individual features. While valuable, this approach struggles to articulate the complex, combinatorial patterns that often drive a model's decision-making process. To overcome this limitation, we introduce ProToMEx, a new paradigm for explainability that leverages Probabilistic Topic Models (PTMs). Our model-agnostic framework learns latent ''topics'' that represent distinct, high-level reasons for a classification, moving beyond simple feature importance to reveal underlying semantic structures. ProToMEx naturally provides both global explanations of a model's overall behaviour and local explanations that can disentangle multiple co-existing reasons for a specific prediction. We demonstrate empirically that ProToMEx not only produces explanations of comparable fidelity to popular methods like SHAP and LIME but also drastically reduces the amortised computational cost of generating local explanations, making it highly suitable for real-time applications. Specifically, we show that ProToMEx is ~30-40x faster than SHAP and LIME over standardised tabular datasets and synthetic datasets.

---


### 5. [A Data Fusion Framework for Grounding Aerospace Surrogate Model via Experimental Wind-Tunnel Observations](https://arxiv.org/abs/2609.04267)

**<font color=#1a73e8>作者：</font>** Nitin Nagesh Kulkarni, Dheeraj Vemula, Yin Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aerodynamic surrogate models trained on high-fidelity CFD data reproduce numerical predictions of both scalar outputs and entire fields accurately, yet their predictive fidelity is limited by systematic discrepancies between CFD and experimental observations. We present an experimentally grounded correction framework that adapts a CFD-trained deep learning surrogate using wind-tunnel PSP measurements. A Geotransolver surrogate trained on 2,300 high-fidelity CFD simulations of the NASA CRM wing-body configuration, spanning geometric variation, Mach 0.70-0.85, and angles of attack 0 to 4 degrees, reproduces the CFD integrated aerodynamic forces and pitching moment to R2 > 0.99 but does not match the experimental data. To incorporate experimental information without retraining the surrogate, a correction network is trained on spatially registered PSP measurements at two freestream Mach numbers (0.70 and 0.85) across the same angle-of-attack range, learning the discrepancy between the surrogate-predicted and experimentally measured surface-pressure distributions. At Mach 0.85 the correction substantially improves agreement with PSP, particularly at the wing suction peak, shock location, and subsequent pressure recovery, reducing both the magnitude of the prediction error and the fraction of wetted surface on which it exceeds 0.05 in Cp, and it does so from a limited experimental dataset without modifying the pretrained surrogate parameters. On held-out angles of attack the grounded surrogate agrees with measurement to within 2.3-2.7% of the measured Cp range, and outperforms direct interpolation between the measured conditions at every state tested. Experimental measurements can therefore ground a large-scale simulation-trained surrogate by learning systematic CFD-to-experiment discrepancies while preserving its generalization capability and computational efficiency.

---


### 6. [Quantum-Assisted Memory-Efficient Training for Parameter-Intensive Wi-Fi-Based Human Activity Recognition](https://arxiv.org/abs/2609.04271)

**<font color=#1a73e8>作者：</font>** To Truong An, Jie Zhang, Guolin Yin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wi-Fi-based human activity recognition (HAR) has become an important part of integrated sensing and communications, paving the way for a range of context-aware services. However, most existing Wi-Fi-based HAR systems rely on deep learning (DL) models that are computationally and memory intensive in both training and inference, which poses significant challenges for real-world deployment. Conventional training requires simultaneous updates of millions of parameters, leading to prohibitive memory consumption. In this paper, we propose a novel quantum-assisted memory-efficient training framework (Q-MET) designed to improve efficiency in both training and inference. Q-MET utilizes a hybrid quantum classical neural network to indirectly generate parameters for HAR models, significantly reducing the trainable parameter count compared to direct optimization. To further support the deployment on resource-constrained devices, we integrate structured pruning during the training phase. Experimental results demonstrate that Q-MET achieves a 90% to 95% reduction in trainable parameters compared with conventional backpropagation-based DL training while maintaining or even exceeding classical classification accuracy. Additionally, Q-MET supports lightweight inference through structured pruning, achieving 75% to 85% model sparsity with less than 2% loss in classification accuracy. To the best of our knowledge, this work represents the first quantum-assisted approach to simultaneously tackle memory inefficiencies in both the training and inference stages of HAR systems.

---


### 7. [Memory as transformation: LETHE, a self-referential gan-inspired architecture](https://arxiv.org/abs/2609.04289)

**<font color=#1a73e8>作者：</font>** Francesco Vitucci, Anthony Di Furia, Francesco Scagliola  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LETHE (Latent-parameter Evolution with Temporal Hierarchical quasi-Equilibrium) is a self-referential sonic-oblivion system implemented in SuperCollider. It adopts the formal vocabulary of Generative Adversarial Networks in a closed configuration without external datasets or supervision after initialization. Audio is processed by a 3 x 3 mixing matrix built around two delay lines; its nine coefficients and two delay times evolve through the interaction of a five-feature linear discriminator and a random-perturbation optimizer analogous to single-sample REINFORCE. The discriminator compares current energy behavior with an archive of the initial state and guides parameter updates. Circular, fixed, and live sources can be mixed independently. Across fixed and circular sessions with an ablation control, the active generator is necessary for parametric evolution ($\Delta c_{22}=0.000$ in all 15 ablation sessions). Situated in the tradition of self-referential electroacoustic music, LETHE delegates the sonic outcome to an adaptive closed loop whose parametric space is defined by the composer.

---


### 8. [BER-PEF: Unified Human Mobility Predictability Evaluation via Bayes Error Rate Estimation](https://arxiv.org/abs/2609.04292)

**<font color=#1a73e8>作者：</font>** En Xu, Jingtao Ding, Zhiwen Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human mobility predictability concerns the best prediction performance attainable from a given target and input information, but its ground truth is not directly observable on real mobility data. We present BER-PEF, a Bayes-error-rate-based framework that converts BER estimation into mobility predictability estimation and provides a unified protocol for comparing estimators without observable ground truth. The framework maps symbolic sequences, numeric trajectories, contextual features, and learned representations into a common feature--label space, then evaluates estimator outputs along controlled perturbation curves against a shared predictability reference interval by measuring deviations below the interval, above the interval, and across the full interval. Experiments on Foursquare NYC and TKY, GeoLife, and T-Drive show that several BER-based estimators achieve lower reference discrepancy than existing predictability methods on symbolic sequences and numeric trajectories, while their estimates track changes in empirical prediction performance under perturbation. Additional analyses show that contextual inputs and multiple structured representations can be evaluated under the same protocol, and that aggregating evidence across multiple perturbation levels provides a more reliable basis for estimator selection than relying on a single unperturbed observation. BER-PEF therefore offers a unified and verifiable path for evaluating predictability estimators on heterogeneous mobility data when ground-truth predictability is unavailable.

---


### 9. [Data-Optimized Contingency Screening: A Machine Learning Approach to Power System Security](https://arxiv.org/abs/2609.04300)

**<font color=#1a73e8>作者：</font>** Joshua Salako, Folajimi Osikomaiya, Olakorede Olamiju  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ensuring the security of the power system is essential for stability and reliability, especially in the event of disruption. Effective classification of contingency in power systems enables proactive decision-making and mitigates large-scale breakdowns and failures. This study explores the use of machine learning algorithms to classify security levels of contingencies in power systems into safe, moderate or severe classes. For this approach, Newton-Raphson load flow method extracts system data from contingency scenarios, using Overall Performance Index (OPI) as safety measure. For data pre-processing, Synthetic Minority Over-Sampling Technique (SMOTE) and Principal Component Analysis (PCA) is used to address class imbalance and reduce dimensionality, respectively. K-Nearest Neighbours (KNN), Random Forest (RF) and Support Vector Machines (SVM) is trained and evaluated on datasets generated through N-k contingency scenarios for k equal 1, 2, and 3 on IEEE-14 and IEEE-30 bus systems using four hybrid pre-processing configurations: normalized, SMOTE-balanced, PCA-transformed, and a combined SMOTE PCA-transformed. Performance is assessed by precision, recall and F1 score, with priority given to the severe contingency classes. The RF achieved the highest F1 scores of 0.97 in IEEE-30 and 0.86 in IEEE-14, SVM benefits significantly from PCA and improves the accuracy of the classification, while KNN is best suited for SMOTE and PCA conversion. The findings show that PCA contributes more than SMOTE to the overall performance of the model. However, SMOTE improves recall but can introduce false positives and is therefore a compromise of accuracy. This study highlights machine learning as a scalable and powerful alternative to traditional contingency analysis, which improves the assessment of security in real time.

---


### 10. [Iris: Climbing to the Search Frontier](https://arxiv.org/abs/2609.04304)

**<font color=#1a73e8>作者：</font>** Ziyuan Liu, Hengqi Liu, Zichuan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Iris-mini and Iris-pro, two search agents trained at the 35B-A3B and 397B-A17B scales, together with the data pipeline and training recipe behind them. Tasks are reverse-constructed from the hyperlink structure of a web corpus: we author multi-hop chains over an entity graph distilled from a seed page and its out-links, rewrite every non-answer entity into a descriptive reference so that no clue can be resolved by string matching, and admit only questions that a reference model fails closed-book yet solves once the supporting evidence is supplied. These questions are then turned into trajectories, which are filtered at both the trajectory and the turn level before SFT. The policy is then optimized by RL against live search, with the reward judge and the observation summarizer served inside the training cluster, and with over-long rollouts interrupted at the request level and resumed from their committed prefix at the next step. We alternate the two stages in a procedure we call SFT-RL climbing, returning the hardest solved and most efficient rollouts of each RL round to the next supervised pass. Because inference-time context management is worth more on these benchmarks than most reported differences between systems, we evaluate every benchmark both with and without it, holding the tool set, the context limit, and the judge fixed. All results come from a single ReAct agent, with no sub-agents and no test-time verification. With management enabled, on BrowseComp, BrowseComp-ZH, DeepSearchQA, and HLE the two models reach $82.2/84.8/86.9/52.3$ and $88.6/85.1/92.9/56.4$, the strongest overall results among open-source search agents in their respective parameter ranges. We plan to release the model weights together with the complete recipe for data construction, training, and evaluation.

---


### 11. [The microscope is the mask: privileged views and labels from a cryo-ET forward model](https://arxiv.org/abs/2609.04325)

**<font color=#1a73e8>作者：</font>** Bogdan Toader, Kiarash Jamali, Tanmay A. M. Bharat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We explore the use of simulated data for training a model for protein annotation in crowded cryo-electron tomography volumes reconstructed from images collected at limited tilt angles and severely corrupted by the measurement operator. Firstly, we leverage the corruptions imposed by the forward model to generate domain-specific augmented paired views of the exact same scene for an invariance objective integrated into the LeJEPA self-supervised training framework. Secondly, we use additional information from the simulation pipeline such as the positions and identity of proteins in the simulated volumes to inform the architecture of the model and the loss function, so that semantic information is localised at protein positions in the resulting dense feature volume. The resulting model, CARNIVAL, is evaluated without finetuning on classification and detection tasks in real tomograms, using a benchmark dataset containing multiple protein types and two tomogram processing types. We show that CARNIVAL outperforms a state-of-the-art model trained using a contrastive objective on simulated data but without forward model-based paired views or privileged information.

---


### 12. [Data-Driven Learning of Unknown Nonlinear Differential Equations Using Functional Analysis](https://arxiv.org/abs/2609.04329)

**<font color=#1a73e8>作者：</font>** Seyyed Shaho Alaviani, Yongzhi Qu, Gregory W. Vogl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, the problem of data-driven discovery of nonlinear ordinary differential equations (ODEs) is recast, and a new interpretable machine learning (ML) method is proposed. The proposed method aims to learn the unknown vector field of nonlinear dynamics without prior knowledge of the system's physics from only one single state trajectory's data. The proposed method has two fundamental differences with existing methods: 1) the formulation presented in this method is derived based on Functional Analysis and Operator Theory, and 2) the cost function is constructed in the function space as a distance between two functions as an integral, instead of the discrete-sum of errors used in existing ML approaches. An incremental learning algorithm is proposed to learn the unknown vector field to handle new training samples in an online manner. The proposed method can discover the unknown vector field from both forced and unforced autonomous and non-autonomous (or time-varying) dynamical systems. The proposed method is able to simultaneously discover unknown external forces as a function of time and unknown underlying dynamics. Finally, numerical examples are given to demonstrate the advantages of the proposed method.

---


### 13. [Modular Deep Recurrent Neural Network: Application to Quadrotors](https://arxiv.org/abs/2609.04339)

**<font color=#1a73e8>作者：</font>** Nima Mohajerin, Steven L. Waslander  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A modular deep Recurrent Neural Network (RNN) is introduced to facilitate the process of deploying various architectures of RNNs, and to automatically compute derivatives for gradient-based learning methods. The modularity leads to a set of new architectures, one of which includes feedforward inter-layer connections. By adding feedforward inter-layer connections in a multi-layer RNN, it is observed that the capability of the RNN to learn and model high-order dynamics and nonlinearities is significantly improved. The problem of vanishing/exploding gradient in space for a multilayer RNN is also alleviated using feedforward connections. These results are demonstrated using a quadrotor case study, for which a model of the altitude dynamics is learned with our particular network structure, while existing methods are unable to generalize as quickly or at all.

---


### 14. [Object Concepts Emerge from Motion](https://arxiv.org/abs/2609.04348)

**<font color=#1a73e8>作者：</font>** Boshi Li, Xiaohui Wang, Xiaoyang Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-centric visual representations are important for physical-world perception, but existing visual pretraining methods often capture semantic categories without preserving the identity and coherence of individual instances. We present a biologically inspired framework that learns object-centric representations for single images from raw videos. Our approach uses motion boundaries as a source of object-level grouping: off-the-shelf optical flow and clustering produce pseudo-instance masks, which supervise a single-image encoder with pixel-level pairwise metric learning. The framework requires neither human annotations nor camera calibration. We first obtain 195 million pseudo-labeled frames from 7,163 hours of driving and web videos, then expand the supervision to 421 million frames with Motion-Verified Self-Training, which combines model proposals with motion evidence. We train encoders up to Swin-H and distill the learned representations into a family of Swin backbones. Across monocular depth estimation, 3D object detection, 3D occupancy prediction, and end-to-end planning, the resulting models achieve competitive or superior performance relative to supervised and self-supervised pretraining baselines, with particularly strong transfer on geometry- and instance-sensitive tasks. These results show that motion-derived supervision can teach static image encoders to represent visual instances, providing a complementary direction for scalable visual pretraining.

---


### 15. [Adapting from Downturns: Prediction of Long-Term Conversational-Skill Development in Mental-Health Crisis Counselors](https://arxiv.org/abs/2609.04350)

**<font color=#1a73e8>作者：</font>** Vivian Nguyen, Lillian Lee, Elizabeth A. Olson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How do people learn to become better conversationalists? This question is especially important in the context of mental-health counseling, where conversational skills are essential, yet volunteer counselors often have limited access to supervision and structured feedback. Understanding how counselors develop their ability to steer conversations toward positive outcomes -- and identifying early which counselors are (not) on track to improve -- can help prioritize support for the counselors who need it most.
In this work, we introduce the task of predicting, early in a conversationalist's career, whether they will eventually improve at steering conversations toward positive outcomes, and demonstrate the feasibility of this task in the case of volunteer mental-health crisis counselors. Our central insight is that people may struggle with particular kinds of moments in a conversation, and that what is especially revealing of their likelihood of future improvement is how they learn to handle those moments over time. We operationalize this insight by designing a method that identifies the types of moments a counselor initially struggles with, captures how they adapt their response when they re-encounter similar moments in subsequent conversations, and learns which early adaptations predict improvement months or even years later. While this future-prediction task is challenging, our counselor-adaptation approach yields better results than baselines that learn directly from the conversation transcript.

---


### 16. [A Quantum Variational Approach to Prototypical Recurrent Unit](https://arxiv.org/abs/2609.04354)

**<font color=#1a73e8>作者：</font>** Mahyar Sadeghi Garjan, Tommaso Cesari, Michel Barbeau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a lightweight Quantum Prototypical Recurrent Unit (QPRU) that requires significantly fewer parameters than both classical recurrent architectures, such as Long Short- Term Memory (LSTM) and Gated Recurrent Unit (GRU), and quantum variants, including Quantum LSTM (QLSTM) and Quantum GRU (QGRU). Despite its compact design, the QPRU achieves competitive forecasting performance, matching state-of-the-art baselines while offering important structural and practical advantages, including enhanced scalability and a reduced number of trainable parameters.

---


### 17. [Blockchain-Enabled Secure Logging for Fiscal Electronic Mechanisms: Evaluation of the Greek eSEND and myDATA Tax Systems](https://arxiv.org/abs/2609.04356)

**<font color=#1a73e8>作者：</font>** Panagiotis Mavridis, Anargyros Baklezos, Christos Nikolopoulos  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper analyzes the implementation of blockchain-based integrity mechanisms in Greek Fiscal Electronic Mechanisms (FEMs) and the central tax information system eSEND. The study examines the cryptographic architecture of fiscal devices, including Electronic Cash Registers, Fiscal Printers, Fiscal Signing Machines, and FEMAS devices, which implement double or triple hash-chain structures to ensure transaction immutability. The transmission protocol between fiscal devices and the central database is also evaluated with respect to encryption, sequential validation, and blockchain verification. In contrast, the architecture of Electronic Invoicing Provider Services and the myDATA central platform is analyzed, highlighting the absence of blockchain-based integrity guarantees. The comparison demonstrates that hardware-based fiscal mechanisms provide stronger guarantees for transaction completeness and tamper resistance than purely software-based invoicing infrastructures. The findings highlight architectural weaknesses in the current e-invoicing framework and propose improvements for ensuring transaction integrity in digital tax ecosystems.

---


### 18. [On the Abundance of Critical Points of the t-SNE Energy](https://arxiv.org/abs/2609.04379)

**<font color=#1a73e8>作者：</font>** Nakul Haridas, Ryan Murray  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper considers the energy landscape of the t-SNE algorithm. While this algorithm has enjoyed broad adoption, the non-convexity of the associated energy has made it difficult to rigorously understand what the algorithm captures in many settings. In particular, a number of well-known numerical examples, several of which are reproduced in this article, suggest a complicated energy landscape with many local minimizers that do not respect the topology or clustering structure of the underlying data. This work seeks to provide first steps towards a rigorous explanation of these phenomena. Specifically, for a general family of energies, which include both the original t-SNE algorithm and recently identified large data limits, and for densities in feature space which obey a continuous symmetry, we construct infinite families of distinct critical points. These critical points are based upon identifying pairs of discrete symmetries, one in the original feature space and the other in the target embedding space, which are preserved under gradient dynamics. These critical configurations exhibit many characteristics, such as topology breaking and spurious clustering, which are often observed empirically. Finally, numerical and analytical examples are given throughout as a means of illustrating the approach.

---


### 19. [What Moves? Localized Motion Representations for Compositional Scene Control](https://arxiv.org/abs/2609.04383)

**<font color=#1a73e8>作者：</font>** Frank Fundel, Malek Ben Alaya, Thomas Ressler-Antal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world dynamics are inherently compositional: multiple entities move simultaneously within a shared scene, each exhibiting distinct motion patterns. Yet most existing video representations encode motion globally, without explicitly capturing localized motion for individual entities. Crucially, motion is defined relative to a global reference frame, including camera motion and scene layout. However, localized embeddings are often computed from cropped images or obtained by masking features after encoding, discarding the context needed to interpret motion. To address this, we introduce a promptable localized motion representation that produces persistent embeddings for user-specified regions defined by spatial masks. Rather than cropping the input or masking features, our model processes the full video and conditions motion encoding directly on the queried region. This yields temporally consistent, region-addressable embeddings that isolate local dynamics while retaining the global context required for disambiguation. We demonstrate object-level motion transfer, enabling controlled composition of dynamic scenes. Beyond generative control, our embeddings support localized action classification in multi-actor videos. Across both tasks, our approach improves controllability and outperforms global representations localized through cropping or post-hoc masking. Project Page: this https URL

---


### 20. [Candidate Comparability Before Promotion: Conditional Validation in Adaptive Network Intrusion Detection](https://arxiv.org/abs/2609.04388)

**<font color=#1a73e8>作者：</font>** Roberto Fernández-Barrios, Iker Pastor-López, Amaia Pikatza-Huerga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adaptive network intrusion detection systems retrain classifiers after drift alarms, but an alarm detects change; it does not establish that a challenger should replace the deployed incumbent. Promotion is security-relevant because it changes the model responsible for subsequent attack detection, and evaluating it has a methodological problem: promotion conclusions may depend on how the challenger was constructed and on how much evidence supports it. We test that dependence on CICIDS2017, UNSW-NB15 and ToN-IoT with self-contained challenger pipelines, nested candidate-size controls, a common-harness comparison of nine update policies, and a final sensitivity confining every exact feature vector to one evaluation, training or probe role. Incumbent-owned frozen preprocessing amplified apparent promotion harm; with self-contained challenger pipelines the mean full-drift harm did not persist. Raising nominal candidate evidence from 512 to 2,000 samples per class improved promotion under pool-constructed progressive drift by +0.53, +1.67 and +0.38 balanced-accuracy points: positive and statistically resolved in all three benchmarks, but materially benchmark-dependent rather than homogeneous, and driven mainly by fewer false positives. Policy conclusions were partially robust: policy ordering changed with candidate comparability, no policy globally dominated, and earlier compatibility statements for a label-free estimator and a calibrated ensemble narrowed. Validation helped evidence-disadvantaged challengers but added no average benefit at parity. Thirteen replays on real, time-ordered traffic showed no net harm from always deploying. Challenger construction and evidence should be controlled, reported and interpreted explicitly when promotion is evaluated.

---


### 21. [Evaluation of Phonetic Encoding Algorithms on Transcription Datasets](https://arxiv.org/abs/2609.04391)

**<font color=#1a73e8>作者：</font>** Can Özbey, Emre Kaplan, Berkin Deniz Kahya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this work, a novel evaluation scheme built on a generalized variant of the Rand Index measure, namely, the Hüllermeier-Rifqi Index, is proposed in order to assess how well phonetic encoding algorithms conform to word-based transcriptions in IPA (International Phonetic Alphabet) notation. For this objective, the discordance score is obtained by calculating the absolute difference between the pairwise similarity values of ground-truth transcriptions and those of corresponding phonetic encodings, which are computed using normalized edit distance as a permutation dependent string metric. The resulting score is subsequently adjusted with respect to that of a random string generator incorporating the same alphabet as the encoder under consideration. A wide range of phonetic encoders were evaluated as such on multi-lingual transcription datasets along with their recall capabilities based on the collision rate. The validity of the proposed scheme is further supported by its applicability in measuring the orthographic transparency of a language when the writing system is viewed as an inherent phonetic representation.

---


### 22. [The Anatomy of an ASR Hallucination](https://arxiv.org/abs/2609.04404)

**<font color=#1a73e8>作者：</font>** Hamees Sayed, Apoorv Singh, Kumar Aman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ASR systems sometimes produce fluent text that is unrelated to the speech they receive. We view these hallucinations as one possible consequence of a broader grounding failure, in which the transcript is no longer adequately guided by the audio. To understand where this failure becomes possible, we study two independently trained Conformer-Large recognizers - one CTC and one RNN-T - under environmental degradation and speaker-background shift. In both models, the final encoder stage emerges as a critical boundary: bypassing the final block causes divergence on nearly every utterance, whereas bypassing middle blocks has little effect. At this same stage, the representations become more compact, text becomes readable by the trained decoder, and grapheme information becomes explicit. Importantly, the intervention produces garbled or repetitive output rather than fluent fabrication. Our result therefore identifies a mechanistic precondition for hallucination - the failure to produce adequately grounded output - not the complete origin of naturally occurring hallucinations. Together, the results reveal a consistent terminal-stage dependency for grounded recognition across two decoder families and multiple distribution shifts.

---


### 23. [Disentangling Attention in Deep Operator Learning: A Controlled Study of Data-Driven and Physics-Informed Architectures](https://arxiv.org/abs/2609.04407)

**<font color=#1a73e8>作者：</font>** Amar Alem Koric, Qibang Liu, Seid Koric  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural operators learn mappings between input functions and complete PDE solution fields, enabling forward evaluations of new problem instances orders of magnitude faster than conventional numerical solvers. Attention mechanisms have recently been introduced into neural operators, but most studies change several architectural components at once, making it difficult to identify what actually improves accuracy. This work presents a controlled and systematic study of five deep operator network (DeepONet) variants with distinct attention mechanisms, trained under both data-driven and physics-informed regimes, to isolate the effects of cross-attention, self-attention, tokenization, and attention depth. We evaluate them on a source-driven transient one-dimensional nonlinear diffusion-reaction equation, a transient one-dimensional viscous Burgers equation with variable initial conditions, and a two-dimensional Poisson heat-conduction problem with heterogeneous source fields. Per-sensor tokenization with cross-attention reduces the mean relative L_2 error of the classical DeepONet in all benchmark-training combinations by factors of 2.4-28.0, while the best attention configurations reach 3.5-32.3. Branch self-attention paired only with dot-product fusion is inconsistent, degrading the one-dimensional problems while helping the more complex two-dimensional source field; added on top of cross-attention it improves all six cases, though by less than cross-attention fusion alone. Global pre-mixing provides no consistent benefit. Increasing cross-attention depth further improves accuracy, but with diminishing returns and a substantially higher cost under physics-informed training. Overall, query-dependent cross-attention is the most reliable mechanism, whereas branch self-attention is most useful for large, spatially complex functional inputs.

---


### 24. [Beyond a Universal Forecasting Selector: Demand-Conditioned Model Selection across Demand Patterns and Horizons](https://arxiv.org/abs/2609.04425)

**<font color=#1a73e8>作者：</font>** Adolfo González  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting-model selection remains difficult in heterogeneous demand because the most suitable decision rule may vary with demand structure, data availability, and forecasting horizon. This study examines whether the selector itself should be treated as a context-dependent component of the forecasting process. Five selection mechanisms - RMSSE, ERA, OWA, CCG-AHSC, and CCG-AHSCD - are compared across 24 optimized forecasting models, nine datasets, three training-testing partitions, and horizons from 1 to 12 cycles. Selector performance is evaluated ex post using Global Relative Accuracy (GRA), statistical tests, and a best-attainable-model reference. No selector dominates across all conditions. CCG-AHSC and CCG-AHSCD are more competitive for Smooth demand and several Erratic configurations, whereas OWA and ERA perform better in Intermittent and Lumpy settings. Selector suitability also changes with historical data availability and horizon, supporting a context-dependent rather than universal approach to forecasting-model selection.

---


### 25. [Segmentation of the aorta in 4D flow MRI using 4D convolutional kernels and learning from sparse annotations](https://arxiv.org/abs/2609.04439)

**<font color=#1a73e8>作者：</font>** Hinrich Rahlfs, Julio Garcia, Chiara Manini 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated aortic segmentation in 4D flow MRI is essential for reproducible hemodynamic assessment but is limited by scarce dense annotations and high computational demands. We developed a fully automated 4D (3D+time) U-Net for segmenting the ascending aorta, arch, and proximal descending aorta, using a parameter-efficient hybrid 4D kernel to capture temporal context and sparse 4D labels derived from existing 2D expert contours and centerlines, thereby avoiding the need for dense 4D annotations. Training comprised 268 scans from 8 centers and 2 vendors, with evaluation on an internal test set (32 scans) and an external post-contrast set (30 scans; different site, protocol, and annotator), compared against frame-wise 3D networks and two semi-automatic references. Against time-resolved annotations, the 4D U-Net achieved Dice scores of 0.927 (internal) and 0.911 (external), versus 0.919/0.847 for the 3D U-Net, 0.893 for static PC-MRA, and 0.808 for registration-based propagation; differences were small in systole but pronounced in diastole. Agreement with expert contours for peak velocity, net flow, axial and circumferential wall shear stress, and diameters was excellent (ICC >=0.954 internal, >=0.980 external), while semi-automatic references performed worse. The method thus provides reproducible, time-resolved aortic segmentation for automated hemodynamic analysis and generalizes across multicenter, multivendor, and independent post-contrast data. The model is publicly available.

---


### 26. [TRILOGUE: A Trilingual Spoken Dialogue Fact-Checking Benchmark with Evidence and Paired Audio](https://arxiv.org/abs/2609.04452)

**<font color=#1a73e8>作者：</font>** Chaewan Chun, Meruyert Aristombayeva, Jiyoung Choi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern misinformation is often heard before it is read, yet fact-checking systems are still evaluated mainly on clean written claims. Spoken dialogue remains different even when systems operate on transcripts: claims may be distributed across speakers and turns, depend on prior context, and become harder to verify when Automatic Speech Recognition (ASR) errors distort the available text. Prior spoken dialogue fact-checking resources are small, English-centric, or focused on annotation rather than end-to-end benchmarking, leaving no large multilingual benchmark with paired speech and turn-level labels. We introduce TRILOGUE (TRIlingual spoken diaLOGUE fact-checking), a large-scale trilingual benchmark of source-grounded spoken dialogues in English, Russian, and Kazakh. It contains nearly 12K dialogues, 187K turns, and 390 hours of paired audio with ASR transcripts and word-level timestamp alignments across all three languages, including nearly 5K human-recorded Russian and Kazakh dialogue files. TRILOGUE supports claim check-worthiness detection, source-article evidence retrieval, and claim verification with claim-only, gold-evidence, and retrieved-evidence inputs. Baselines show that ASR degradation and cross-lingual transfer remain challenging, especially for Kazakh, while retrieved source evidence substantially narrows the gap to gold-evidence verification.

---


### 27. [Topology-Aware Training and Spatial Diagnostics for Fiber Bundle Segmentation in Tracer Histology](https://arxiv.org/abs/2609.04454)

**<font color=#1a73e8>作者：</font>** Joselyn Romero Avila, Kyriaki-Margarita Bintsi, Ermias Habte 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anatomic tracer studies reveal how axon bundles project from an injection site, branch into smaller groups of axons, and course through the brain to reach their destinations. Histological data from such studies provide anatomical reference information for validating diffusion MRI tractography. However, manual annotation of the histological data is very labor-intensive, and although automated segmentation methods have been proposed, they rely mainly on pixel-overlap losses such as BCE and Dice; topology-aware loss functions have not been studied for this task. We compare BCE-Dice, clDice, Betti matching, and Topograph for fiber bundle segmentation in macaque tracer histology using a frozen DINOv3 backbone. To our knowledge, this is the first exploration of foundation-model features for this task. BCE-Dice achieved the highest Dice, while clDice achieved the highest bundle recall but poor mask overlap. Topograph had similar Dice to BCE-Dice, the lowest $\beta_0$ error, and fewer false positives than BCE-Dice and Betti matching. Fiber bundle segmentation methods are typically evaluated with a permissive rule that counts a bundle as detected given any overlap with the prediction. We show this rule does not capture oversegmentation, and that per-section TPR can be inflated by empty sections assigned perfect recall. To quantify this, we introduce Excess32, a spatial diagnostic measuring predicted pixels outside a 32-pixel tolerance band around annotated bundles. In validation, a Betti-Topograph union raises sparse-bundle TPR from 0.818 to 0.933, but worsens FDR from 0.296 to 0.509, Excess32 from 0.108 to 0.466, and area ratio from 0.94 to 3.34. These results show detection metrics alone are insufficient to characterize segmentation quality.

---


### 28. [On-board ML for Trace Gas detection in Imaging Spectroscopy data](https://arxiv.org/abs/2609.04458)

**<font color=#1a73e8>作者：</font>** Vít Růžička, Adam Chlus, Andrew Thorpe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data collected during aerial and spaceborne imaging spectroscopy campaigns enables the detection of transient events such as trace gas emissions. However, current processing pipelines depend on slow, on-the-ground processing, which delays the time to information of each detected event and prohibits immediate follow-up actions. During the Tokyo Field Campaign of March 2026, we explored on-board processing of Imaging Spectroscopy data from the equipped AVIRIS-5 sensor. Due to communication bottlenecks, full datacubes cannot be downlinked immediately during the flight. Instead we downlink the potential events predicted by our efficient and small machine learning model. We show the first on-board detection of methane point source emission with Imaging Spectroscopy data using Edge ML.

---


### 29. [Nested Inductive Bias Framework for SPD Manifold Learning](https://arxiv.org/abs/2609.04466)

**<font color=#1a73e8>作者：</font>** Tushar Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In Geometric Deep Learning, inductive biases serve two primary functions: enforcing manifold constraints and embedding relational priors. Currently, representation learning on SPD manifolds frequently relies on pullback Euclidean metrics, such as the Log-Euclidean Metric, to satisfy the former. While computationally efficient in avoiding domain boundary violations, these metrics induce a flat geometry that may fail to capture the intrinsic relational priors of datasets. While metrics such as the Poincaré metric are widely utilized to induce domain-aligned relational priors, generalizing them from standard vector representations to the SPD manifold has remained a challenge. To bridge this gap, we introduce a Nested Inductive Bias framework that utilizes a two-stage diffeomorphic composition to formally pull back non-Euclidean target geometries onto the SPD manifold. This framework enables the construction of curvature-aligned Riemannian classifiers that simultaneously respect matrix constraints and the latent relational geometry of the data. Empirical evaluations on kinematic and signal processing benchmarks, together with synthetic experiments, demonstrate that deep manifold networks experience degradation in class separability unless the metric curvature aligns with the intrinsic data distribution. Furthermore, for standard vectorized architectures, we propose the Rational Conformal Metric (RCM), designed to establish state-of-the-art geometric robustness against outliers by bounding the representation space.

---


### 30. [Nebulon Enterprise Simulated Threats for Phishing Research (NEST-Phish): A Synthetic Enterprise Phishing Email Dataset for Behavioral and Machine-Learning Research](https://arxiv.org/abs/2609.04474)

**<font color=#1a73e8>作者：</font>** Emily J. Winokur, Lauren S. Treiman, Allen G. Moore 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing remains one of the most persistent cyber threats, yet publicly shareable datasets for studying phishing in realistic enterprise email settings remain limited. To address this gap, we introduce a synthetic enterprise phishing email dataset built around a fictitious organization, Nebulon. The dataset spans a broad set of workplace communication themes and includes matched synthetic legitimate and phishing emails with interpretable phishing-cue annotations. Here, ``legitimate'' denotes the non-phishing class, not legitimately occurring organizational emails. Human-subject categorizations and classifier evaluations show that the dataset supports meaningful variation in phishing judgments while also providing learnable signal for supervised detection. This publicly released resource is intended to support future work on phishing detection, human susceptibility, explainability, and benchmark development in enterprise-like contexts.

---


### 31. [Client-Side Probing of Deleted Ridge Statistics in Federated Unlearning](https://arxiv.org/abs/2609.04475)

**<font color=#1a73e8>作者：</font>** Yijun Quan, Giovanni Montana  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated unlearning aims to remove a client's data from a shared model without retraining from scratch. Some efficient systems make deletion exact by storing compact, additive summaries of the training features and broadcasting an updated linear classifier after every accepted change. We show that these broadcasts can also reveal the hidden summaries. A malicious client can submit known changes, use the returned classifiers to identify the server state, and compare states immediately before and after an isolated deletion. This exposes the deleted sample, class, or client summary and can enable its reinsertion. We characterize exactly when the observations contain enough independent information, give a matching optimal construction for unrestricted probes, and derive a more realistic estimator based on additions formed from the attacker's own data. On MNIST and CIFAR-10, high-precision broadcasts permit exact label recovery for every tested sample deletion with both probe types. Lower-precision broadcasts sharply reduce fine-grained recovery, and insufficiently diverse responses prevent identification altogether. Unrestricted probes are readily detected by their size; most individual attacker-data additions resemble honest batches, although we do not claim that the complete sequence is inconspicuous. The results identify a concrete privacy and integrity risk, its algebraic cause, and practical limits involving broadcast precision, update verification, response rate, and concurrent activity.

---


### 32. [When Quantization Breaks Memory: Recurrent-State Write-Back in Low-Precision Temporal Inference](https://arxiv.org/abs/2609.04490)

**<font color=#1a73e8>作者：</font>** Ismail Erbas, Xavier Intes, Vikas Pandey  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantization is widely used to reduce the computational and memory demands of neural-network inference. In recurrent networks, however, the quantized state is stored and returned at the next time step, so the rule used to store that state can alter subsequent computations. Here, we introduce recurrent-state write-back to denote this rule and isolate its effect in a compact GRU encoder--decoder for fluorescence lifetime imaging, a molecular imaging modality used in quantitative biological imaging. A central task is estimating two lifetime parameters, the short-lived component {\tau}1 and the long-lived component {\tau}2, from high-noise time-resolved fluorescence signals. Holding the trained model fixed, replacing continuous state propagation with deterministic 4-bit state storage increases estimation errors for {\tau}1 and {\tau}2 by approximately 70x and 300x, respectively. Failure occurs when repeated small updates remain below the write threshold, leaving the stored state nearly fixed while the network continues to propose change. Error feedback, residual memory, and direction memory carry information from these suppressed updates across time and recover accuracy without retraining. Precision sweeps show that increasing state precision can worsen a fixed recurrent solution, while matched training shows that compatibility with the state interface can be learned. To test whether this behavior extends beyond the GRU, we repeat the post-training intervention in an independently trained LSTM, where coarse write-back reproduces the failure, error feedback restores accuracy, and state-specific interventions reveal greater sensitivity of the cell state than the hidden state. Our results establish recurrent-state write-back as a key determinant of low-precision recurrent dynamics and identify the state-storage interface as a central design consideration for quantized recurrent inference.

---


### 33. [ResLearn-XR: Residual Learning for Network Traffic and Quality-of-Experience-Aware Modeling in Extended Reality](https://arxiv.org/abs/2609.04493)

**<font color=#1a73e8>作者：</font>** Yoga Suhas Kuruba Manjunath, Jie Gao, Lian Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present ResLearn-XR, a residual learning framework for predicting eXtended Reality (XR) network traffic and estimating Quality-of-Experience (QoE) risk. ResLearn-XR adopts a two-stage temporal learning structure comprising a base sequence prediction model augmented with task-specific residual learning components to improve adaptability to bursty, non-stationary XR traffic dynamics. The residual learning stages operate in the value space for continuous XR traffic forecasting and in the logit space for probabilistic QoE risk estimation. \rev{For the QoE-risk branch, we introduce a Data Descriptor Algorithm (DDA), a causal feature-construction module that converts packet-level application-layer observables into frame-timing-aware descriptors suitable for encrypted traffic analysis. We also construct an XR Traffic-QoE dataset that pairs continuous XR traffic traces with session-level user-reported QoE labels. ResLearn-XR reduces SMAPE by up to 17.84% across frame-count, frame-size, and inter-arrival-time prediction, while reducing QoE-risk estimation SMAPE by up to 87.8% over single-stage baselines.

---


### 34. [EyeMakeYou: Identity-, Task-, and Subjective-State-Conditioned Diffusion for High-Frequency Gaze Synthesis](https://arxiv.org/abs/2609.04501)

**<font color=#1a73e8>作者：</font>** Kamrul Hasan, Mehedi Hasan Raju, Oleg V. Komogortsev  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Eye movement biometrics (EMB) is an emerging behavioral modality for user authentication, particularly in virtual- and augmented-reality systems, where gaze dynamics contain distinctive subject-specific features. However, robust EMB systems require diverse, high-quality gaze recordings that are expensive to collect and often unavailable at the scale needed for model development. Generative models can mitigate data scarcity, but existing methods either synthesize generic gaze behavior or personalize signals primarily by identity, without jointly representing the user's task and subjective state. Consequently, generated signals may appear visually realistic while failing to retain the behavioral properties required for biometric applications. To address this limitation, we propose EyeMakeYou, a multi-conditional denoising diffusion framework for subject-specific, high-frequency gaze synthesis. EyeMakeYou generates 5-s, 1000-Hz bivariate gaze-velocity sequences from an identity-removed reference trajectory and conditions the denoising process on an identity embedding, a task embedding, and self-reported ratings of overall difficulty, mental tiredness, and eye tiredness. Its objective combines diffusion noise prediction and identity preservation with multi-resolution spectral, drift-consistency, and event-weighted local-smoothness losses. Experiments on GazeBase show that EyeMakeYou achieves higher median spatial accuracy and greater real--synthetic similarity in the embedding feature space than the existing generative approaches, while retaining selected task-dependent associations between subjective reports and oculomotor features. These findings support conditional diffusion as a practical approach for augmenting gaze datasets for biometric and interactive applications.

---


### 35. [BioSync: Transformer-Based Cross-Modal Fusion for a Multimodal Physiological Digital Biomarker](https://arxiv.org/abs/2609.04504)

**<font color=#1a73e8>作者：</font>** Seyed Mahmoud Sajjadi Mohammadabadi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cardiac, neural, behavioral, and speech measurements from wearable and mobile devices provide partial, noise-sensitive views of physiological state. BioSync combines these measurements into the \textbf{BioSync Index (BSI)}, a continuous composite digital biomarker defined under the BEST framework. The model applies multi-head self-attention to modality tokens and adds a linear branch whose hypothesis class includes standard feature concatenation. This architecture is motivated by latent-variable measurement theory and by the possibility that joint observations contain information unavailable from individual modalities. We evaluated BioSync on two literature-informed synthetic cohorts: a four-modality cognitive-decline cohort using HRV, EEG, actigraphy, and speech, and a metabolic-autonomic cohort structured around the public AI-READI wearable schema. In the cognitive cohort, BioSync and concatenation obtained AUCs of 0.928 and 0.926, respectively. In the metabolic cohort, BioSync obtained accuracy/F1 of 0.764/0.766, compared with 0.756/0.758 for concatenation. The BSI correlated with latent severity in both cohorts ($r=0.91$ and $r=0.68$). A pure-attention ablation obtained cognitive-cohort AUC 0.911, locating the increase to 0.928 in the combined wide-and-deep architecture. With matched modality-dropout training, BioSync led concatenation at five of six cognitive-cohort corruption rates and at the highest metabolic-cohort rate. Its cognitive-cohort AUC was also higher than five published digital-biomarker reference values, although differences in datasets and tasks preclude a controlled benchmark claim. Comparison with single-modality, early-fusion, and late-fusion designs across six prespecified criteria identifies the model's computational properties; validation on real cohorts remains necessary.

---


### 36. [Hoss: Fast Oblivious Semantic Search with Heterogeneous GPU-CPU-TEE Architecture](https://arxiv.org/abs/2609.04522)

**<font color=#1a73e8>作者：</font>** Jianzhang Du, Weijie Huang, Chenghong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Semantic search is widely deployed in modern AI systems, but protecting both data contents and access patterns remains challenging. The current state-of-the-art system, Compass, achieves oblivious semantic search by building an optimized ORAM over HNSW graphs. However, even with aggressive optimizations, it still incurs large overheads. Closing this performance gap is fundamentally difficult: Compass has already removed most cryptographic overheads, leaving ORAM accesses as the dominant cost, which are constrained by well-known Omega(log N) bandwidth lower bounds. Our key insight is that traditional ORAM overhead stems from the assumption of limited private memory, whereas modern GPU TEEs provide large private memory (Pmem) that blinds internal access patterns (Hunt et al., NSDI '23). This shift opens a new design space. We therefore propose Hoss, a first-of-its-kind oblivious semantic search system with a heterogeneous CPU-GPU TEE architecture that supports fast, scalable search with low cost of ownership. In Hoss, the GPU TEE's large Pmem hosts the hot-path HNSW traversal, while the lower layers of the graph, if they exceed GPU capacity, are offloaded to CPU TEEs. The system invokes oblivious primitives only when accessing these lower layers. The availability of large Pmem also enables new optimization opportunities. For example, Hoss features a host-access ORAM mechanism that goes beyond traditional performance constraints and incorporates several data-dependent optimizations that are not possible in prior designs. We implement a prototype of Hoss and benchmark it against Compass. Our results show that Hoss achieves up to 67x speedup while maintaining high recall, with larger gains at scale.

---


### 37. [Towards a universal language of concepts: A survey](https://arxiv.org/abs/2609.04528)

**<font color=#1a73e8>作者：</font>** Aishni Parab  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humans can learn and generalize novel concepts from sparse data because they express knowledge in rich structural formats. In this paper, we propose that programs are a strong candidate for universal representation of concepts. We review computational models of concept learning that use programs as their concept representation and evaluate their contribution toward a universal representational language.

---


### 38. [An Energy-Based Conservative-Dissipative Latent Neural Evolution Operator for Magnetization Dynamics](https://arxiv.org/abs/2609.04530)

**<font color=#1a73e8>作者：</font>** Sebastian Schaffer, Lukas Exl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop an energy-based reduced-order model for micromagnetic magnetization dynamics that couples a convolutional autoencoder to a structured latent neural ordinary differential equation. Motivated by the precessional-dissipative structure of the Landau-Lifshitz-Gilbert equation, the latent vector field is generated from the gradient of a learned scalar potential through an antisymmetric operator and a symmetric positive-semidefinite dissipative operator. This potential is learned in nonunique latent coordinates and is not identified with the Gibbs free energy, but decreases monotonically along autonomous continuous-time solutions, while the antisymmetric component permits motion along its level sets. The encoder, decoder, latent energy, and operators are trained jointly on short trajectory windows using latent and decoded-rollout losses alone, without time-derivative supervision, physical-energy labels, or dissipation penalties. At inference, an initial state is encoded once, evolved in latent space, and decoded only at the requested output times, enabling substantially cheaper trajectory prediction than the micromagnetic solver used to generate the training data. We compare quadratic, deep, and additive deep-quadratic latent energies on two datasets parameterized by field amplitude and generated for the two applied-field directions of the NIST $\mu$MAG Standard Problem 4. Dissipative-only and antisymmetric-dissipative models achieve comparable accuracy on short training-style windows but differ substantially on uninterrupted rollouts, for which the antisymmetric-dissipative models provide markedly more accurate trajectory predictions. The deep-quadratic energy gives the best overall accuracy for both field directions and exhibits slower error growth when rollouts are extended to twice the training horizon.

---


### 39. [Mitra-v2 Technical Report](https://arxiv.org/abs/2609.04540)

**<font color=#1a73e8>作者：</font>** Yefan Tao, Xiyuan Zhang, Xinyi Liu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Mitra-v2, a tabular foundation model that delivers state-of-the-art performance on real-world classification and regression problems, from credit-risk scoring and clinical prediction to equipment-failure detection and house-price estimation. Mitra-v2 is trained only on synthetic data, with a pretraining distribution that is much larger and more diverse than Mitra-v1's. Built on a small 2D Transformer backbone, Mitra-v2 supports longer contexts and larger feature spaces. Improved optimization lets it learn from this larger task distribution. We evaluate Mitra-v2 on the TabArena and TALENT benchmarks, comprising more than 300 real-world datasets under two evaluation protocols. On the full TabArena benchmark, Mitra-v2 delivers state-of-the-art performance at the level of the industry-scale TabFM and EXAONE Tabular models, while surpassing TabPFN-3 by a wide margin in both classification and regression. Mitra-v2 matches the 1.6B-parameter TabFM with only 5% of its size (77M parameters), delivering frontier performance at a fraction of the cost. On TALENT, Mitra-v2 remains among the leading models, clearly outperforming TabPFN-3 and TabICLv2. It also ranks first on classification tasks with more than ten classes, even though it was pretrained only on tasks with at most ten classes. These results make Mitra-v2 one of the strongest and most broadly applicable open tabular foundation models released to date. We release the model weights, the inference and fine-tuning code, and our evaluation results under the Apache-2.0 license.

---


### 40. [Data-Driven Discovery of Composition-Dependent Constitutive Models for Hyperelasticity and Viscoelasticity of Digital Materials](https://arxiv.org/abs/2609.04541)

**<font color=#1a73e8>作者：</font>** Josué García-Ávila, Beijun Shen, Manuel K. Rausch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital materials fabricated by multi-material 3D printing are designed as controlled mixtures of stiff and compliant constituents, yielding effective responses that span more than an order of magnitude in apparent stiffness and exhibit strongly nonlinear, composition-dependent, and rate-dependent dissipative behavior. Classical finite-strain viscoelastic models represent such behavior with closed-form strain energy functions for equilibrium and non-equilibrium stresses as well as evolution of internal variables, which may limit flexibility when a single constitutive model is expected to generalize across materials and loading rates. Here, we present a data-driven multi-material constitutive modeling framework that generalizes a formulation by Bergström and Boyce. The proposed framework retains the structure of the classical model, namely multiplicative kinematics, invariant-based strain-energy functions, and a scalar dissipative evolution law directed along the normalized nonequilibrium deviatoric stress. For the equilibrium branch, the data-driven discovery framework either directly predicts closed-form model parameters as functions of composition or automatically constructs a polyconvex strain-energy function using neural ordinary differential equations (NODEs). The nonequilibrium branch kinetics are learned similarly, either by directly identifying closed-form parameters across compositions or by using appropriately constrained artificial neural networks. Using multi-rate uniaxial compression data across multiple material compositions, we show that the proposed formulation captures rate-dependent stiffness and hysteresis across compositions while preserving thermodynamic consistency.

---


### 41. [Fast Surrogate Modeling of Excitable and Oscillatory FitzHugh-Nagumo Dynamics with Parametric Neural Operators](https://arxiv.org/abs/2609.04549)

**<font color=#1a73e8>作者：</font>** Andrew Franck, Justin Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The FitzHugh-Nagumo (FHN) system serves as a simplified model of neuronal voltage dynamics, capturing the activator-inhibitor structure behind both isolated action potentials and the rhythmic spiking seen across the brain. Exploring its 5D physiological parameter space is important for neuromodulation and mapping voltage recordings back to biophysics, yet classical finite-difference solvers make rapid parameter sweeps expensive. We train parameter-conditioned Fourier Neural Operators (FNOs) as fast, differentiable surrogates for the FHN voltage and recovery fields on a one-dimensional spatial domain, conditioning each Fourier layer on the parameter vector $\lambda = (D_u, D_v, a, b, \tau)$ via feature-wise linear modulation (FiLM). We apply a single bifurcation analysis that delimits the two distinct regimes the model spans, oscillatory (tonic firing) and excitable (action-potential propagation), and we train one operator in each. In the oscillatory regime the surrogate attains sub-$0.1\%$ relative $L^2$ error on both fields, runs nearly three orders of magnitude faster than the finite-difference baseline, generalizes uniformly across the parameter space, and extrapolates to low single-digit percentage errors outside of the training bounds. In the excitable regime the same operator accurately reproduces the firing threshold and the $c \propto \sqrt{D_u}$ conduction-velocity law and replicates full traveling pulses, fully capturing the excitable bifurcation structure rather than just smoothly interpolating fields.

---


### 42. [Rhythms of Work: Multi-Scale Interpretation of Human Behavioral Traces for Workplace Agents](https://arxiv.org/abs/2609.04556)

**<font color=#1a73e8>作者：</font>** Lin Ai, Scott Counts  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Runtime traces are becoming a central substrate for understanding agentic systems, yet interpretation has focused largely on what the agent did. Workplace agents face the complementary problem: interpreting the human activity that surrounds them. Hours of low-level events carry rich evidence about a user's state but are too granular to reason over directly, and flattening them into one stream or compressing them into a single embedding both treat "summarize the user's behavior" as if it had one correct answer. We argue instead that behavioral interpretation is resolution-dependent: the same trace should admit multiple addressable interpretations at different temporal resolutions. We construct a multi-resolution vocabulary of semantically normalized operators, recurring motifs, coherent episodes, and day-level rhythms, each preserving the structure salient at its own horizon. Applied to 667 million human-attributed events from a large commercial productivity suite (50,000 users, 100 organizations), it yields 120 operator types, thousands of motifs, 25 episode types, and five day-rhythm archetypes. We validate it on real telemetry: re-running the entire pipeline on a disjoint 2,000-user sample recovers the same taxonomy (structural stability), and on held-out users the full representation forecasts a user's next episode more accurately than a flat-operator baseline, a 17% relative macro-F1 gain (predictive validity), so the abstractions preserve future-relevant information rather than merely describe it. A controlled resolution ablation then shows that no single level is optimal across questions: different agent-facing questions about the same trace are best answered at different resolutions. Behavioral trace interpretation for agents should therefore be multi-resolution and query-conditioned: an agent should access the temporal grain a question needs, not one universal summary.

---


### 43. [Reducing Hallucinated Transcripts in Whisper via Hallucination Space Projection](https://arxiv.org/abs/2609.04561)

**<font color=#1a73e8>作者：</font>** Maryam Abbasihafshejani, Murtuza Jadliwala  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Whisper is a widely used foundation model for automatic speech recognition (ASR), but its generative decoder can produce fluent hallucinated transcripts for inputs containing little or no speech. We propose a training-free, inference-time method to reduce these hallucinations using low-rank projection of decoder activations. A compact hallucination-associated subspace is estimated from non-speech calibration data, and decoder hidden states are projected away from this subspace during inference.
We evaluate two variants: always-on, which applies projection to all inputs, and gated, which applies it only when Whisper predicts that an input is likely non-speech. Across non-speech benchmarks, always-on projection reduces average hallucination rate (HR) from 31.31% to 2.44%, a 92.21% relative reduction, while gated projection reduces HR to 3.74%, an 88.05% relative reduction, with lower false rejection of genuine speech. On LibriSpeech, gated projection increases absolute word error rate (WER) by 0.33-4.39 percentage points and yields false-rejection rates (FRR) of 0.41--9.97% across model and split settings.
These results show that low-rank activation projection can substantially suppress Whisper hallucinations without retraining, while providing a controllable trade-off between hallucination suppression and speech recognition performance.

---


### 44. [Optimizing Credential Blast Radius Through Trust Boundaries and Delegation Under Post-Quantum Authentication Costs](https://arxiv.org/abs/2609.04566)

**<font color=#1a73e8>作者：</font>** Pauli Taipale, Harri Lainio  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Partitioning interacting services into independently rooted trust domains limits issuer-compromise reach while increasing calls across trust boundaries. Post-quantum replacements for public-key authentication and key-establishment mechanisms can increase crossing latency on constrained or lossy paths. We formulate the joint selection of trust domains and credential-derivation structures under policy and latency constraints, linking separate service-interaction and credential-derivation graphs through domain assignment. Credential blast radius measures weighted service impact after compromise. A linear upper bound supports optimization, while a joint event model gives exact expected impact. For shared issuers, the bound is exact under nonoverlapping credential reach and otherwise requires explicit propagation. While the general problem is NP-hard, scalarized two-domain direct issuance reduces to a weighted minimum cut. Joint optimization yields lower blast radius than choosing boundaries first in 195 of 230 exhaustive synthetic comparisons, especially under chained delegation. A trace-derived replay used measured post-quantum costs, synthetic risk inputs, a fixed derivation family, and one to six trust domains. The best design found reduced expected impact by up to 36% relative to one domain within the latency budget. The framework turns risk assumptions and measured crossing costs into candidate trust-domain and credential-derivation designs.

---


### 45. [Optimizer Memory Schedules for Outscaling the Overtraining Axis](https://arxiv.org/abs/2609.04577)

**<font color=#1a73e8>作者：</font>** Katie Everett, Shikai Qiu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate how optimizers scale across the overtraining axis and show that relative optimizer performance and optimal hyperparameters change substantially with training horizon. In particular, we study how matrix-preconditioned methods (Muon and SOAP) and a momentum-scheduled method (ADANA) scale relative to AdamW. We compare these four optimizers across models from 51M to 253M parameters and overtraining (OT) factors from 1x to 256x, sweeping the base learning rate at every setting. The preferred learning rate schedule can reverse across the overtraining axis, the best weight decay coefficient scales approximately as sqrt(OT), and longer horizons generally favor longer fixed memory. ADANA's scaling advantage over AdamW persists after tuning AdamW's fixed memory separately at each horizon. Log-time weight decay and momentum cooldown provide substantial gains for ADANA that compound as training increases. With this treatment, ADANA outscales AdamW with an exponent advantage close to that predicted by DANA theory on power-law random features. Muon and SOAP instead provide roughly constant token-efficiency advantages over AdamW across most of the measured range, although SOAP may gain further at the highest overtraining factors. ADANA begins behind both matrix-preconditioned optimizers but closes the gaps as training increases, surpassing Muon and becoming competitive with SOAP at our highest OT factors. These results establish training horizon as an essential axis for optimizer evaluation and design.

---


### 46. [Representation Redundancy and Structural Complexity in Finite-Field Inversion](https://arxiv.org/abs/2609.04583)

**<font color=#1a73e8>作者：</font>** Zheng Zhang, Na Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The representation chosen for a mathematical operation can affect both its algebraic form and its empirical learning difficulty. We study this phenomenon for inversion over \(\mathbb F_{2^n}\), with field elements expressed in varying ordered \(\mathbb F_2\)-bases. We prove that two ordered bases induce the same coordinate inversion map if and only if they belong to the same Galois orbit. Since every orbit has size \(n\), the correspondence between ordered bases and distinct inversion maps is exactly \(n\)-to-one. We then analyze three Boolean formulations of inversion. The reference formulation has algebraic degree \(n-1\) and joint ANF leap \(1\), the mixed representation formulation has degree \(2(n-1)\) and joint ANF leap \(2\), and the complete raw formulation has degree at most \(3(n-1)\) and joint ANF leap at least \(n\). Exhaustive computations agree with the theoretical results and bounds in the cases considered. Controlled experiments with multilayer perceptrons show the same ordering in learning difficulty, while Galois orbit redundancy provides only a limited generalization benefit under the tested conditions. These results show that exact redundancy among representations can coexist with changes in Boolean structure and learning behavior when the representation is exposed as part of the input.

---


### 47. [Dual-Part Multi-Lateral Branched Network for Multi-Class Segmentation in Cardiovascular Catheterization Angiograms](https://arxiv.org/abs/2609.04590)

**<font color=#1a73e8>作者：</font>** Olatunji Omisore, Ahmed Elazab, Ali Shahidinejad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Catheterisation image processing requires segmentation models that are fast, accurate and explainable. While most of the existing studies usually focus on binary segmentation, there is a recent demand for simultaneous segmentation of multiple structures found in catheterization scenes. In this study, a dual-part MLBNet architecture is designed with multi-lateral encoder blocks and multi-head decoder branches for class-aware segmentation in cardiovascular catheterization scenes. Lateral branches in the encoder enables repeated feature extraction to learn diverse shared representations, while multiple decoder heads are used to introduce class-skewed branches that specialize in different structural properties in catheterization scenes. To analyze the performances of the dual-part MLBNet architecture, several multi-class segmentation angiogram data obtained during cardiovascular catheterization in phantom models, synthetic human-simulated aorta, and animal model are used for model training and evaluation. Results obtained showed the dual-part models could effectively separate guidewire, catheter, vessels and background pixels to their classes of memberships with high probability. The results demonstrate that all models were able to distinguish the dominant background class from foreground structures with high overall accuracy.

---


### 48. [Hidden In Plain Gaze: Gaze Representations as Privacy Controls for Utility and Re-identification Risk in XR](https://arxiv.org/abs/2609.04592)

**<font color=#1a73e8>作者：</font>** Cory Ilo, Brendan-David John, Doug A. Bowman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intelligent extended reality (XR) systems increasingly use eye and head tracking to infer user intent, task, and attention, but the same signals can also reveal biometric identity. We study whether gaze data representation choice can serve as a lightweight privacy control at feature extraction, before adding perturbation or formal privacy mechanisms. Using the egocentric HoloAssist dataset, we compare three gaze representations under matched model capacity: raw gaze, spatial attention heatmaps, and engineered eye-movement features. We evaluate each representation on action recognition as task utility and closed-set user re-identification as privacy leakage. Representation choice substantially changes the privacy-utility tradeoff. Engineered features retain roughly 85% of raw gaze's action-recognition accuracy while reducing re-identification by about an order of magnitude, to roughly four times the chance rate across 206 identities. This reduction attenuates rather than eliminates identity leakage, and the differences across representations show that abstraction alone does not guarantee privacy. Engineered features expose interpretable and auditable structure, giving designers a transparent privacy lever that complements mechanisms such as differential privacy.

---


### 49. [GNN-Guided Graph Coarsening and Adaptive QUBO Penalties for the Capacitated Vehicle Routing Problem with Time Windows on a Quantum Annealer](https://arxiv.org/abs/2609.04593)

**<font color=#1a73e8>作者：</font>** Youssef Kamel Rezk, Paweł Gora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph coarsening reduces the large Quadratic Unconstrained Binary Optimization (QUBO) formulations arising when vehicle-routing problems are solved by quantum annealing. Nearby customers with compatible time windows are merged into super-nodes, the reduced problem is solved, and the solution is expanded to the original graph. For the Capacitated Vehicle Routing Problem with Time Windows (CVRPTW), existing coarsening heuristics require family-specific tuning and remain unreliable on random instances. We address these limitations on the Solomon benchmark using simulated annealing and a D-Wave Advantage2 processor.
We first introduce adaptive penalty calibration. Uniform penalty scaling has little effect, whereas controlling the internal coefficient range substantially improves raw samples. Removing non-binding constraints, normalising binding ones, and scaling the remaining penalties reduces mean raw constraint violations from 33.0 to 0.06 at the same solver budget (p=3.7e-11, n=56). A variable-count-preserving control attributes this gain to conditioning rather than problem size.
Second, we replace the hand-tuned merge score with a graph neural network (GNN) using one configuration across all families. At N=10, it achieves 100% feasibility across all Solomon families, including R-type (100% vs. 80% for the tuned heuristic). Across N=10,...,100, feasibility is 83% vs. 69%, with the GNN better or tied on 85/90 instance-size pairs. At N=80,100, the difference is significant (p=0.002; 25/25 pairs), while the QUBO remains approximately 5-6 times smaller.
Finally, hardware experiments reproduce the conditioning effect at fixed logical variable count: feasible samples increase from 0.02% to 39% across 13 instances. Classical repair with local search remains a reference bound for end-to-end solution cost.

---


### 50. [An Evaluation Framework for Generating Multi-View Images of a Person in a Scene](https://arxiv.org/abs/2609.04603)

**<font color=#1a73e8>作者：</font>** Mahir Majid, Young Kyung Kim, Guillermo Sapiro  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent generative image-editing Diffusion Transformers (DiTs) demonstrate impressive semantic editing capabilities but still struggle with spatially consistent camera angle changes. A primary bottleneck in training foundation models to execute free-form, promptable camera angle changes is the lack of specialized training data. While multi-view datasets exist for generic 3D environments and objects, there remains an absence of paired, multi-view datasets featuring human subjects at fixed locations in natural scenes, including frontal and side-profile views. Capturing such multi-camera data in unconstrained environments is logistically challenging and unscalable. In this paper, we first experiment with multiple state-of-the-art image editing models to create this data synthetically, but find that the outputs are frequently prone to hallucinations involving how much the subject's head turns relative to the background, often producing inconsistent environments. To address this issue, we propose the Head Scene Rotation Difference (HSRD) metric to quantitatively evaluate camera movements around a person. The proposed metric operates by decoupling camera movement from localized head pose manipulation. As demonstrated by the extensive experimentation, HSRD provides the pipeline necessary to evaluate 3D spatial parallax for a person in a scene, paving the way to reliably construct high-quality multi-view synthetic datasets.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-190](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
