# 📦 其他研究 | 2026年08月28日

> 本类共 **171** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-171](./part-04.md)

---

### 1. [User-Centered Design for Digital Patient-Navigation Tools in Oncology: Scoping Review](https://arxiv.org/abs/2608.24887)

**<font color=#1a73e8>作者：</font>** Saba Kheirinejad, Brianna M White, Parnian Kheirkhah Rahimabad 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Navigation programs for patients with cancer improve access and continuity of care, yet their digital transformation is often limited by poor usability and inadequate uptake. Applying user-centered and human-centered design (UCD/HCD) principles may close this gap, but the extent to which such design methods are used and evaluated in oncology navigation tools remains unclear. This scoping review identifies how UCD/HCD principles have been, and should be, applied in developing and implementing digital health tools for navigation for patients with cancer. A scoping review was conducted following PRISMA-ScR (Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews) and Joanna Briggs Institute guidance. A total of 7 databases (PubMed/MEDLINE, Scopus, IEEE Xplore, Web of Science, Embase, ACM Digital Library, and CINAHL) were searched for English-language articles published between January 2015 and July 2025. Eligible studies reported original, peer-reviewed research on digital or mobile health interventions linked to cancer navigation and documented at least 1 UCD/HCD activity. Two reviewers independently screened records and charted data on context, target users, functions, tool modality, design phase, methods, and outcomes. Findings were synthesized descriptively and thematically. A total of 36 studies met the inclusion criteria. Findings were organized into 4 domains: study characteristics, navigation functions and digital modalities, design processes and methods, and UCD/HCD application. Iterative prototyping and usability testing were the most common, while participatory design and implementation evaluation were underused. UCD/HCD approaches enhance usability and patient relevance of digital cancer navigation tools. However, their application remains limited across cancer types, regions, and functions.

---


### 2. [AI-Powered Mental Health Chatbots in Africa: A Systematic Review and Culturally Adaptive Framework](https://arxiv.org/abs/2608.24890)

**<font color=#1a73e8>作者：</font>** Matshepo Lebese, Pitso Tsibolane  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mental health challenges in Africa remain under-addressed due to inadequate infrastructure, stigma, and a chronic shortage of professionals. Artificial Intelligence (AI)-powered chatbots are emerging globally as low-cost, accessible tools that can offer psychological support. This paper presents a systematic review of 52 empirical studies published between 2017 and 2025, critically analysing their cultural, linguistic, and infrastructural relevance to African contexts. The findings demonstrate the potential of AI chatbots to improve accessibility, reduce symptoms of anxiety and depression, and expand psychosocial support, yet reveal limited African-specific adaptation. Most systems remain rooted in Western models and English-language designs, leaving critical gaps in local relevance, inclusivity, and sustainability. Based on the findings, the authors develop a Culturally Adaptive Digital Mental Health (CADMH) framework that integrates African cultural values, multilingual design, mobile-first optimisation, and ethical safeguards. The study highlights opportunities and barriers for integrating AI chatbots into African healthcare, offering guidance for research, practice, and policy.

---


### 3. [Measurement-Budget Allocation in Quantum Learning with Finite-Shot Generalization Guarantees](https://arxiv.org/abs/2608.24891)

**<font color=#1a73e8>作者：</font>** Ferhat Ozgur Catak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On near-term quantum hardware, estimating a Born probability requires repeated circuit executions. A quantum learning experiment with a fixed measurement budget $B$ must therefore decide how many distinct training states $n$ to use and how many shots $S$ to allocate to each state. We study this tradeoff for binary quantum classifiers with fixed or independently selected measurement operators $M$, where the ideal score is $\Tr(M\rho)$. We prove a distribution-free generalization bound that separates the finite-sample and finite-shot contributions. The sample term scales as $\sqrt{d/n}$, while the shot term scales as $\sqrt{(\log n)/S}$; under the constraint $B=nS$, these two terms move in opposite directions. Minimising a conservative closed-form surrogate of the bound gives the allocation rule $\nstar = 2\sqrt{2dB/\log(2B/\delta)}$ and $\Sstar = B/\nstar$. This surrogate has the same asymptotic scaling as the exact minimizer and yields a worst-case rate of $B^{-1/4}$. The guarantee is intentionally conservative, since it applies to the full class of binary quantum measurements. We complement the theory with PennyLane simulations using 2-qubit and 4-qubit variational quantum circuits on nine synthetic binary classification benchmarks. In all tested configurations, the one-sided empirical generalization gap remains below the theoretical bound. The result provides a conservative statistical guideline for allocating measurement budgets in finite-shot evaluation and pre-experimental planning for near-term quantum learning systems, complementing hardware-level scheduling and circuit-design considerations. Extending the guarantee to fully adaptive shot-noisy training remains an open problem.

---


### 4. [Same-Player Verification for Account Consistency in Counter-Strike 2](https://arxiv.org/abs/2608.24893)

**<font color=#1a73e8>作者：</font>** Xuchen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In competitive first-person shooter (FPS) games such as Counter-Strike 2 (CS2), account-integrity review often asks whether an account's recent behavior remains consistent with its historical operator. This consistency question arises in cases such as temporary substitution, rank boosting, and high-skill players using lower-ranked accounts, where manual review requires comparing a current match against multiple historical matches. We formulate this review task as same-player verification: we encode the behavioral trajectory of a single player in a match replay (demo) as a demo-player behavioral fingerprint, and train a model to judge whether two behavioral observations come from the same real player. Grounded in CS2 game understanding, the fingerprints cover crosshair control, movement-stop-fire coordination, economy/buy, combat/engagement, and temporal rhythm. From 1,330 CS2 demos we extract 13,300 demo-player observations, and sample 663,590 same/different pairs from an 88.4M candidate-pair space for supervised training and evaluation. The final pairwise model reaches an average ROC AUC of 0.931 and achieves 0.722 different-player recall at 95% precision. Feature analysis shows that the strongest identity signals come from low-level operations, especially crosshair control, firing rhythm, and movement-stop-fire coordination, indicating that stable low-level mechanical habits are more informative for this verification task than single-match performance outcomes. In the account-history aggregation evaluation, increasing history depth raises AUC from the K=1 single-pair baseline of 0.931 to 0.986 at K=10. These results show that CS2 demo behavior can support supervised same-player verification and account-level identity-consistency modeling through multi-demo history aggregation.

---


### 5. [Agentic World Analysis (AWA) - an alternative way to explore systems and support decision making](https://arxiv.org/abs/2608.24896)

**<font color=#1a73e8>作者：</font>** Yongchao Zeng, Alexey Voinov, Calum Brown 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> To address increasingly pressing sustainability challenges, various approaches have been developed to foresee possible futures, identify failure modes, detect vulnerabilities, and test potential mitigations. However, environmental systems are highly complex. Especially when coupled with human processes, the scale of uncertainties becomes intractable. To address this challenge, we propose a new approach - Agentic World Analysis (AWA)- combining the strengths of simulation modelling and expert elicitation. The concept of AWA is defined by three properties: 1) AWA uses an agentic AI system to mimic an expert panel that studies the world; 2) AWA projects futures iteratively through analysing scenario trees and learning from this analysis to improve decisions; 3) AWA is auditable. Based on these requirements, we implemented the World Engine by Generative Agents (WEGA) as a possible application of the AWA approach and demonstrated its functionality with a real-world case study: the Nitrogen Crisis in the Netherlands. WEGA autonomously constructed the context, identified key stakeholders and uncertainties, created expert agents, and generated future scenarios. As a result, two pathways from 2026 to 2041 were proposed, sharing a common assumption that social acceptance of nitrogen mitigation policies is low, while differing in how successful the restoration is according to the implementation of nitrogen data monitoring. The pathways are evaluated in multiple dimensions to assess their logical coherence and quality. The evaluation also actively exposes strengths and weaknesses to provide ways for testing the validity of the policies proposed. We discussed scaling up scenario analyses to enable massive pathway exploration, the trade-offs of using AWA and other approaches, and common concerns regarding AI systems.

---


### 6. [Dynamic Influence-Weighted Distillation for Single-IMU Activity Recognition](https://arxiv.org/abs/2608.24904)

**<font color=#1a73e8>作者：</font>** Bingxuan Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inertial sensors at multiple body locations can improve activity recognition, but requiring every sensor at inference increases the deployment burden. We study whether four synchronized IMUs available during training can improve a student that uses only the right-arm IMU during fitting and inference. A frozen four-IMU teacher provides logit and feature targets. Fixed-weight knowledge distillation applies each target with the same strength to every fitting sample, although the student may not benefit equally from them. We introduce dynamic influence weighting (DIW), which tests a one-step candidate update on separate fold-internal training participants. DIW then assigns separate sample-wise gates to the logit and feature losses. On WEAR, we evaluate 19 labels and 68,298 complete windows from 22 participants using subject-disjoint five-fold cross-validation. Pooled out-of-fold macro-F1 is 0.561820 for Supervised and 0.571623 for Fixed-weight KD. DIW reaches 0.638451, gains of 7.66 and 6.68 percentage points, respectively. It exceeds Supervised for 18 of 19 labels and 21 of 22 held-out participants. All three routes retain the same 80,915-parameter right-arm student at inference. Under this protocol, DIW converts training-only multi-position information into a stronger single-IMU model without changing deployed sensing or the student forward graph.

---


### 7. [Super Star: Towards Streaming Real-time Interactive Agents for Digital Humans](https://arxiv.org/abs/2608.24909)

**<font color=#1a73e8>作者：</font>** Wentao Jiang, Youchen Xie, Haidi Fan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Existing co-speech gesture generation methods are predominantly studied in offline settings, where gestures are synthesized from complete speech segments. However, interactive digital humans in real-world scenarios are required to generate speech-synchronous gestures online, using only currently available response audio under strict latency constraints. As a result, prior methods are unsuitable for real-time interaction, as they either rely on future speech information or incur substantial inference delay. In this paper, we formulate online co-speech gesture generation for interactive digital humans and propose a real-time interactive framework that couples a streaming speech response module with an online gesture generation module. Specifically, the gesture generator is designed as a causal multimodal autoregressive model that predicts body motion from streaming response speech and motion history, enabling low-latency and speech-aligned gesture synthesis without access to future speech. To support this setting, we further propose an offline data synthesis pipeline tailored to virtual companion scenarios, which leverages topic- and emotion-aware subject corpora to construct diverse human-agent dialogues and then generates co-speech gestures conditioned on the agent responses. Moreover, to bridge the gap between offline data construction and online deployment, we establish a self-evolving training loop by incorporating user feedback collected during online interaction into the data generation process, enabling continual adaptation to user preferences. Extensive experiments demonstrate that our framework achieves superior better latency-quality trade-off, stronger speech-motion synchronization, and higher user preference than competitive existing baselines. Project Page: this https URL

---


### 8. [Visualizing Patient Trajectories and Disorder Co-occurrences in Child and Adolescent Mental Health](https://arxiv.org/abs/2608.24911)

**<font color=#1a73e8>作者：</font>** Dipendra Pant, Kaban Koochakpour, Odd Sverre Westbye 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding patient trajectories and identifying patterns in episodes of care is critical for effective healthcare decision-making. We present a patient timeline visualization using clustered episodes of care derived from over 35 years of Child and Adolescent Mental Health Services (CAMHS) data. Patients were categorized into 12 groups based on three features: age group (preschoolers, middle childhood, teenagers) at the start of the first episode, gender, and presence or absence of Attention-Deficit Hyperactivity Disorder (ADHD), in order to group similar patients. The patients, timeline with demographics, and episode of care information are displayed in the trajectory to facilitate understanding of the patient and associated events, allowing observation of temporal patterns and variations. These plots reveal similarities and differences in care needs and patterns across groups. Females without ADHD have a steady increase in the number of episodes of care with age. Females with ADHD and all males experienced a peak in the number of episodes during middle childhood, followed by a decline in the teenage years. To compare and understand the intensity and co-occurring disorders with ADHD across different groups, we plotted an ADHD co-occurrence graph, and Tourette's syndrome was co-occurring predominantly in all age groups. We evaluated and refined our visualizations with the involvement of clinicians, who found them useful for understanding the context of CAMHS care. These visual tools make the population data in the Electronic Health Records (EHR) available for decision-making and enhancing the understanding of care and disorder patterns across groups.

---


### 9. [What Are We Measuring? Bonding, Trust, and the Evaluation of Human-Robot Relationships](https://arxiv.org/abs/2608.24915)

**<font color=#1a73e8>作者：</font>** Imran Khan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In human-robot interaction, relationship quality is often quantified using self-report measures, particularly related to "trust", such that a robot's trustworthiness comes to serve as an index of how close or "bonded" a human feels to it. I argue that this is a category error: trust and social bonding are distinct constructs, differing in their antecedents, their timescales, their bodily signatures, the human experience they produce, the robot responses they call for, and the ethical concerns they raise. I propose that we view them as independent dimensions, and describe the resulting two-dimensional space of possible relationship states under this view, with four configurations: avoidance, functional, dependence, and symbiosis. I then draw out some consequences for human-state-aware robotics: (1) social bonding is an explicit estimation target distinct from trust, (2) it should condition online adaptation (3) it reframes what a "failure" means, and (4) it raises the possibility of identifying dysfunctional relationships, in which a user remains attached to a robot that no longer merits reliance. This is ongoing work, offered in part to prompt the field to reconsider what it means to evaluate relationship quality in human-robot dyads.

---


### 10. [GreenLeaf Law Embed Tiny: A Compact Embedding Model for Legal Domain Retrieval](https://arxiv.org/abs/2608.24936)

**<font color=#1a73e8>作者：</font>** Surya Saka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present GreenLeaf Law Embed Tiny, a 0.6B parameter embedding model for legal domain retrieval. GreenLeaf-Tiny achieves 75.11% on the Massive Legal Embedding Benchmark (MLEB) and 64.38% on MTEB(Law, v1),demonstrating competitive performance among models under 1B parameters. Our approach combines a two-stage training pipeline that first distills knowledge from a larger teacher model into a compact student architecture, then applies domain-specific fine-tuning with hard negative mining; a carefully curated dataset of 3.4 million query-passage pairs, including 150,000 human-curated samples across diverse legal jurisdictions; and an efficient inference architecture supporting multiple quantization levels (BF16, INT8, binary) enabling deployment in resource-constrained environments. We provide detailed analysis of our training methodology, architectural choices, and comprehensive evaluation across legal retrieval tasks. Our results demonstrate that domain-specific training with high-quality data can improve performance for specialized domain applications

---


### 11. [Multi-Modal Anomaly Detection: A Survey](https://arxiv.org/abs/2608.24937)

**<font color=#1a73e8>作者：</font>** Xudong Mou, Zexin Wu, Chuan Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-Modal Anomaly Detection (MMAD) detects rare abnormal events from heterogeneous data sources and is increasingly used in safety- and reliability-critical applications such as industrial inspection and cybersecurity. Yet the literature is fragmented across domains and modality combinations, and existing surveys usually group methods by architecture rather than by how abnormality is defined and separated in multi-modal settings. We survey MMAD from an assumption-driven perspective. We formalize the problem, identify five intrinsic characteristics underlying its core challenges, and organize prior work into two complementary paradigms. The first, normality-assumption methods, models regularity via representation learning, cross-modal alignment, and knowledge enhancement. The second, anomaly-assumption methods, sharpens decision boundaries through coarse-grained, structural, and semantic anomaly injection. We also investigate how foundation models are reshaping MMAD through scalable pretraining, flexible cross-modal transfer, and emerging reasoning capabilities. Finally, we compile representative benchmarks and evaluation protocols across domains and highlight open problems and future directions for robust, adaptive, and interpretable MMAD systems.

---


### 12. [When Does Frequency Decomposition Benefit Physics-Informed Neural Networks? A Preliminary Ablation Study](https://arxiv.org/abs/2608.24940)

**<font color=#1a73e8>作者：</font>** Shubham Rai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial differential equations (PDEs) often have high-frequency and multi-scale features that neural networks struggle to approximate. Physics-Informed Neural Networks (PINNs) build the governing equations directly into training, but suffer from spectral bias: they learn low-frequency components faster than high-frequency ones. Techniques such as Fourier feature embeddings and sinusoidal activations address this, but most studies assume they help across the board without checking which spectral regimes actually benefit. We introduce a dual-branch, spectrally-gated architecture (DBSG-PINN) that splits low- and high-frequency components into separate subnetworks joined by an adaptive gate, and use it to run a partially controlled ablation of frequency decomposition and spectral routing. We test this on five one-dimensional benchmark PDEs, ranging from smooth, single-scale problems to oscillatory, multi-scale ones. Frequency decomposition helps most on the spectrally complex benchmarks, cutting relative $L_2$ error by up to $59.2\%$ on a multimodal wave problem, but gives little benefit on smoother PDEs. On one benchmark (1D Wave), it performs substantially worse than a simpler fixed-combination variant. The gate's benefit scales with how spectrally rich the target solution is: the full model's advantage over the ablations is largest on multi-scale benchmarks and smallest (or negative) on single-scale ones, consistent with the gate exploiting frequency structure rather than acting as noise,though we do not directly visualize or quantify its spatial activations in this study. All results come from a single training seed across five 1D benchmarks, so we present this as an exploratory study meant to raise questions rather than answer them, and outline the additional seeds and benchmarks needed to test whether the pattern holds.

---


### 13. [CAT-GS: Balanced Multimodal Learning via Calibrated Gating and Fusion Surgery](https://arxiv.org/abs/2608.24947)

**<font color=#1a73e8>作者：</font>** Mahir Shahriar Tamim, Sharjil Khan, Md. Samiul Alim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> End-to-end training of multimodal neural networks often exhibits unstable neural dynamics characterized by three coupled failure modes that degrade learning: (i) modality imbalance, where one branch dominates gradient-based optimization; (ii) unstable gating, where noisy confidence cues induce erratic modality selection; and (iii) fusion interference, where modality-specific gradients conflict at the shared fusion layer. We propose CAT-GS (Calibrated, Adaptive, Thresholded Gating with Fusion Surgery), a neural dynamics-based optimization controller for intelligent computing applications. CAT-GS operates during backpropagation without modifying model architectures, fusion modules, or task losses. Through calibration of teacher-derived reliability via temperature scaling and EMA smoothing, CAT-GS stabilizes neural dynamics using a margin-thresholded policy to switch between warm-up dropout, weak-modality prioritization, and weak-biased blending, stabilizes gradient magnitudes under aggressive gating via capped gradient-budget renormalization, and applies fusion-only PCGrad to reduce destructive cross-modal interference at the primary shared bottleneck. We evaluate CAT-GS on audio--visual multimodal pattern recognition benchmarks (CREMA-D, AV-MNIST, and VGGSound), a tri-modal setting (UR-FUNNY), controlled synthetic data (CG-MNIST), and additional cross-domain benchmarks (AVE and CMU-MOSI). CAT-GS improves or matches fused multimodal accuracy against strong imbalance-aware baselines (including OGM-GE, G$^2$D, and UMT) across settings, and yields smoother gating behavior with fewer conflicting fusion gradients.

---


### 14. [Synergising Local Geo-Environmental Characteristics with Spatial Context for Enhancing Landslide Susceptibility Mapping](https://arxiv.org/abs/2608.24956)

**<font color=#1a73e8>作者：</font>** Yusen Cheng, Lei Fan, Qinfeng Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data-driven methods are widely used in landslide susceptibility mapping (LSM) because they can effectively model the complex relationships between landslides and geo-environmental conditions. Existing data-driven approaches generally follow two types of data representations. Pixel-based models focus solely on the geo-environmental characteristics of a specific landslide but neglect the influence of its surrounding environment. Patch-based models incorporate surrounding spatial context but may include pixels with weak or no spatial relevance to the target landslide location. To address this limitation, this study proposes a Local-Geo and Spatial Context Fusion (LGSCF) strategy, which synergises the geo-environmental characteristics of landslide points with their corresponding spatial context through a feature-wise modulation mechanism. We tested the LGSCF strategy by integrating it into several representative convolutional neural network (CNN) architectures, creating nine different LGSCF-based models. The study area covers approximately 2644 km2 across Jenai and Sinyi Townships in Nantou County, Taiwan, and the dataset comprises 5332 landslide samples and an equal number of non-landslide samples. The results show that LGSCF-based models consistently outperform their original versions, achieving F1-scores up to 87.09% and AUC values up to 0.9472. Furthermore, the susceptibility maps produced by LGSCF-based models show that known landslides are more accurately concentrated in "very high" susceptibility zones with fewer misclassifications. These findings demonstrate that our fusion strategy can significantly improve the accuracy of landslide susceptibility mapping.

---


### 15. [Why and When Neural Networks Improve Local Approximation in Optimization](https://arxiv.org/abs/2608.24963)

**<font color=#1a73e8>作者：</font>** Chengkuo Bian, Pengcheng Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Published experience with neural surrogates in derivative-free optimisation is contradictory: the same family of models that cuts the evaluation count of one solver leaves another unchanged, or makes it worse. We show that the contradiction dissolves once three factors are stated, and that these, rather than the fit accuracy a training curve reports, are what delimit when a learned local model pays. Role: a surrogate that proposes candidates the true objective must still approve helps, while one that replaces a gradient the solver depends on hurts. Radius: a model fitted to an optimisation path is reliable only inside a bounded neighbourhood, and its error neither vanishes as that neighbourhood shrinks nor survives its growth. Room: a surrogate can only accelerate progress the base method is still able to make. We formalise radius-aware local generalisation, relate it to the classical fully linear condition, and test each factor with the surrogate class, training pipeline and base method held fixed. Over 117 benchmark instances safeguarded assistance raises the instances solved to high accuracy from 67 to 84 while gradient replacement lowers them to 65; removing the gradient term from the training loss cuts surrogate acceptance from 0.703 to 0.148; and 1000 paired comparisons over ten noise levels show no noise threshold, only a base method that stops early. The same factors bound the gain: a model-based trust-region solver, which leaves little room, drops from 88 to 86 when the identical surrogate is attached, and released interpolation software stays ahead at 103, and on a Monte-Carlo inventory model repairing the acceptance interface is worth 10.40 cost units against 0.00 for the surrogate.

---


### 16. [Physics-Informed Error Field Learning: A Post-Training Optimization Framework for Physics-Informed Neural Networks](https://arxiv.org/abs/2608.24970)

**<font color=#1a73e8>作者：</font>** Jiuyun Sun, Yong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) have emerged as an important class of numerical methods for solving partial differential equations (PDEs). However, during the late-stage optimization process, further parameter updates often yield diminishing accuracy improvements while increasing computational costs. To address this issue, this paper proposes a Physics-Informed Error Field Learning (PIEFL) framework for PINNs. Unlike conventional approaches that continuously approximate the solution field using a single network, PIEFL introduces an auxiliary error network after the primary network achieves satisfactory accuracy and shifts the learning objective from the solution field to the error field. By deriving error control equations under physical constraints, the error network learns the discrepancy between the current approximation and the exact solution, and the learned error correction is combined with the primary prediction to improve solution accuracy. The proposed framework avoids continuous optimization of the entire solution space and focuses computational resources on correcting existing prediction errors. Moreover, PIEFL requires no modification to the primary network architecture, making it compatible with existing PINN models and applicable as a general post-training optimization strategy. Numerical experiments on representative PDEs demonstrate that PIEFL achieves higher solution accuracy under the same computational budget, validating its effectiveness in improving the performance of PINNs.

---


### 17. [Clearing the Underbrush: AI-Enhanced RF Interference Suppression](https://arxiv.org/abs/2608.24974)

**<font color=#1a73e8>作者：</font>** Rahul Jain, Pierre Trepagnier, Rick Gentile 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI-based structured interference rejection has grown more popular because deep learning approaches can outperform traditional methods by jointly considering the signal of interest (SOI) and the signal mixture (SOI plus interference). This work builds on a previous AI-enabled approach utilizing autoregressive transformer-based models by adding a Finite Scalar Quantization (FSQ) tokenizer layer which aims to improve the interference rejection performance while keeping overall latency to a minimum. Additionally, we experiment with other inference optimization techniques with the goal of speeding up inference without much accuracy loss. We explore this space with an experiment where the SOI is a digitally modulated radio frequency (RF) signal and the structured interference is a digital television signal, an extremely common type of Orthogonal Frequency-Division Multiplexing (OFDM) transmission. Our results achieve low latency and increased interference rejection over traditional techniques and prior work with other AI-enabled methods. We demonstrate the benefits of the AI-enabled approaches via audio metrics such as Perceptual Evaluation of Speech Quality (PESQ). Additionally, we explore a variety of applications and detail how our interference rejection algorithm may be used in operationally-relevant scenarios.

---


### 18. [MSR-IVA: Masked Structural Residual Independent Vector Analysis for State-Aware Fusion of Structural MRI and Dynamic Functional Network Connectivity](https://arxiv.org/abs/2608.24978)

**<font color=#1a73e8>作者：</font>** Victor Solomon, Zening Fu, Rafal Angryk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal fusion of structural MRI (sMRI) and dynamic functional network connectivity (dFNC) can reveal how brain structure relates to changing functional states. When the same structural latent representation is coupled with multiple states, applying independent vector analysis (IVA) separately to each state can produce unrelated structural decompositions, while forcing identical decompositions may suppress state-specific relationships. In addition, not every subject expresses every dynamic state. We propose masked structural residual IVA (MSR-IVA), a state-aware framework that combines a shared structural representation with state-specific residual adaptations and masks for incomplete state expression. On an Alzheimer's Disease Neuroimaging Initiative cohort, MSR-IVA improved matched source coupling by 6.5% and reduced unmatched dependence by 15.7% relative to the independent pairwise IVA baseline. Among subjects expressing both states, mean absolute cross-state structural source correlation was 0.9177 for MSR-IVA versus 0.2978 for no sharing, demonstrating controlled structural sharing that preserves source correspondence while allowing state-specific adaptation.

---


### 19. [Solving Robust POMDPs with Omega-regular Objectives via Partially Observable Stochastic Games](https://arxiv.org/abs/2608.24986)

**<font color=#1a73e8>作者：</font>** Durgam Latha, Dion Reji, S. Akshay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Robust POMDPs (RPOMDPs) generalize classical POMDPs to the setting where exact transition probabilities are not known -- rather, they are only known to belong to some uncertainty set of values. In this work, we study the problem of solving RPOMDPs with general omega-regular objectives, which subsume a broad class of objectives such as reachability, safety, and linear temporal logic (LTL) objectives. We show that, for (s,a)-rectangular RPOMDPs with polytopic uncertainty sets, the problem of solving RPOMDPs under omega-regular objectives can be reduced to solving partially observable stochastic games (POSGs) under omega-regular objectives. Moreover, we show for the first time that reductions can be constructed in both directions, establishing the semantic equivalence between (s,a)-rectangular RPOMDPs with polytopic uncertainty sets and POSGs. This allows us to derive a range of new computational complexity results, including both upper and lower complexity bounds, on solving RPOMDPs with different omega-regular objectives. As a corollary, we also derive new computational complexity results for RMDPs.

---


### 20. [Rollout-Decoded Reconstruction for Long-Horizon Prediction in Latent World Models](https://arxiv.org/abs/2608.25017)

**<font color=#1a73e8>作者：</font>** Rishi Shah, Rishav Shrestha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A latent world model trains its decoder on latents anchored to observations, then deploys it on the model's own free-running rollout, hundreds of steps past the last observation. Rollout-Decoded Reconstruction (RDR) closes this gap with a single loss term that free-runs the model during training exactly as evaluation will, decodes every rollout latent, and penalizes reconstruction error against ground truth. The term adds no parameters, costs training-time compute only, and reduces to the standard objective at weight zero, so every comparison in this paper is a one-flag A/B. On the chaotic Kuramoto-Sivashinsky equation, RDR raises valid prediction time (the time to first crossing of normalized error 0.5) from $3.87 \pm 0.23$ to $6.97 \pm 0.42$ time units at an identical 193,568 parameters, a $1.80\times$ improvement confirmed on seeds never used in selection and holding in 10 of 10 preregistered configurations at ratios of 1.71-2.50$\times$. The results come from a single system; a sweep in which the advantage grows with latent width is descriptive, and control experiments on two classic tasks are preliminary.

---


### 21. [CVE-SAI: Counterfactual Visual Evidence-Guided Selective Attribute Indexing for Risk-Controlled E-commerce Search](https://arxiv.org/abs/2608.25023)

**<font color=#1a73e8>作者：</font>** Xiaolong Sun, Qichao Wang, Hangyu Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal product models can complete missing e-commerce attributes, yet current methods still optimize attribute-answer accuracy without verifying visual support, conflate transient prediction with persistent index admission, and lack explicit risk control over factually incorrect or visually unsupported values. We address these gaps with Counterfactual Visual Evidence-Guided Selective Attribute Indexing (CVE-SAI), which first infers and freezes an ontology-constrained candidate from the primary image and attribute question without catalog text, and then decides whether that candidate should enter the index. Focus-Zone Distortion (FZD) constructs an attribute-specific visual-dependence proxy through a controlled counterfactual intervention, and Evidence-Guided Attention Redistribution (EGAR) uses the proxy to refine ontology-constrained scoring. The canonical candidate is frozen before evidence necessity, evidence retention, nuisance-transformation stability, and candidate-specific catalog-text conflict audits; catalog text can only tighten admission and cannot revise the candidate. Independent family-level calibration selects one policy with a simultaneous one-sided finite-sample bound under a 5% unsafe-admission budget. Experiments on five visual attributes derived from Amazon Berkeley Objects show that CVE-SAI improves attribute inference and evidence localization, achieves the highest certified admission coverage under the shared risk protocol, and yields the strongest controlled retrieval performance with the lowest unsafe auto-induced exposure among automatic-admission systems. Separating inference from admission therefore enables visually supported attribute completion to improve retrieval while limiting persistent index contamination.

---


### 22. [Behind the [MASK]: Disentangling Representation and Faithfulness in DAPF-Based Dementia Detection](https://arxiv.org/abs/2608.25028)

**<font color=#1a73e8>作者：</font>** Pardis Ranjbar-Noiey, Natalie Parde  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spoken-language analysis via prompt-based domain-adaptive models is a promising direction for low-resource, non-invasive dementia screening, but such models remain internally opaque. We study the interpretability of the Domain-Adapted models via Prompt-based Fine-tuning (DAPF) framework, which casts dementia detection as diagnosis-related masked-token prediction. We interpret DAPF and strong baselines using a variety of probing and analysis techniques, finding that DAPF achieved the best overall performance (accuracy=0.83 and macro-F1=0.83) with diagnosis most recoverable from its [MASK] representation. However, this representational advantage did not extend to token-level explanation faithfulness. DAPF attributions primarily reflected language task vocabulary, discourse markers, and transcription artifacts, with perturbation tests showing weak or negative effects. This suggests that its masked-token interface determines diagnosis information without producing faithful token-level explanations.

---


### 23. [On the Representational Geometry of Dynamic Programs](https://arxiv.org/abs/2608.25034)

**<font color=#1a73e8>作者：</font>** Richard F. M. Lim, Ruriko Yoshida  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard neural architectures often fail to generalize to longer inputs for dynamic programming (DP) targets. We investigate what makes this hard geometrically. Every finite min-plus DP is a shortest path on a DAG, which is equivalently a tropical polynomial whose extended Newton polyhedron encodes the decision boundary of which path wins. We prove these three descriptions (graph, polynomial, polyhedron) form isomorphic semirings at two levels --- formal polynomials and their computed functions --- connected by operations that characterize all structural redundancies. We then address the length-generalization question geometrically: does the decision boundary at length $T$ decide the boundary at $T+1$? We present two structural negatives. The semiring's two native ways to reduce dimension (setting a variable to each identity) are neither injective nor always closed within the DP. Series and parallel composition fail to construct all DAG topologies from smaller sub-DAGs, and even all terminal-only operations do not capture all DP compositions.

---


### 24. [SimVerity: When Does Simulated Agent Success Survive Physical Deployment?](https://arxiv.org/abs/2608.25067)

**<font color=#1a73e8>作者：</font>** Zhonghao Zhan, Yefan Zhang, Krinos Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Simulated evaluation is widely used to benchmark AI agents, yet how much evidence a simulated pass provides about physical deployment has not been systematically quantified. We present SimVerity, a verdict-transfer assurance framework: it replays matched scenarios on target smart home deployments and cross-validates agent execution against independently qualified physical witnesses. Our evaluation highlights that deployment success is a real-world process, not a static property in simulation: completion, reported state, observable effect, and settled outcome diverged within the same execution. Although an advanced simulator cleared all 240 light trials, a camera caught 42 sub-second failures invisible to settled-state checks. False clearance was predictable: a risk profile learned from measured trials and locked before evaluation predicted failures on a path it never physically measured, beating a property-blind baseline in all eleven held-out sessions across two cohorts. Agent auditability was also measurable: switching one agent loop's model-client/serving configuration raised its scenario-matching share from 52-88% to 100%. Finally, a second qualified simulator added no independent cross-check: it never disagreed on any overlapping case, and only physical measurement exposed their shared blind spots. SimVerity turns verdict transfer into an explicit decision: clear, abstain, or escalate before deployment.

---


### 25. [DeMMO: Longitudinal and Cross-Disease Modelling of Digital Mobility Outcomes via Multi-Task Learning](https://arxiv.org/abs/2608.25073)

**<font color=#1a73e8>作者：</font>** Menghui Zhou, Zhipeng Yuan, Vitaveska Lanfranchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Digital mobility outcomes (DMOs) derived from wearable sensors characterise mobility in daily life and offer a promising means of monitoring disease progression. Yet most DMO studies examine one disease at one visit; they do not model how multivariate DMO relationships with multiple clinical outcomes evolve jointly across diseases. Technically, existing temporal multi-task frameworks can model progression within an individual disease, but they do not jointly model multiple prediction outcomes across diseases, particularly when disease cohorts do not share participants. To address these gaps, we propose DeMMO, an interpretable framework for longitudinal, multi-disease, and multi-outcome learning. DeMMO represents each disease-outcome objective by a longitudinal DMO coefficient matrix and combines temporal regularisation with stable and visit-specific feature selection. Its central technical contribution is an automatic cross-disease and cross-outcome relation-learning mechanism that learns signed relations directly from these longitudinal mappings, enabling selective information sharing without paired participants. We evaluate DeMMO on the recently released, large-scale, multicentre Mobilise-D dataset, which provides a new opportunity to study 24 harmonised real-world DMOs over five visits across multiple mobility-limiting conditions. Against nine strong linear, longitudinal, and deep-regression baselines, DeMMO achieves the best overall and outcome-specific prediction performance, with significant improvements over the strongest baselines. Stability selection further identifies reliable longitudinal DMO patterns for subsequent clinical validation and disease monitoring. The implementation code and experimental results are available at this https URL.

---


### 26. [NVExplain: Explaining Time Series Forecasting with Latent Trajectory Analysis and Structure-Preserving Surrogates](https://arxiv.org/abs/2608.25080)

**<font color=#1a73e8>作者：</font>** Muyan Anna Li, Manikandan Ravikiran, Aditi Gautam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting models are widely used in high-stakes settings, yet their predictions remain difficult to interpret because existing post-hoc methods often ignore temporal dependence and fail to provide horizon-specific explanations. We propose a model-agnostic explainability framework that explains forecasting predictions by attributing each forecast horizon to temporally relevant historical lags. The framework models forecasting as a latent trajectory and introduces semantic flow to quantify how information evolves across time in the model's internal representations. By aggregating semantic flow, it constructs a lag-horizon attribution matrix that captures horizon-resolved temporal influence. To improve explainability, we further generate structure-preserving perturbations and fit sparse local surrogate models, producing human-readable and temporally coherent explanations. We evaluate the method using faithfulness and stability diagnostics across multiple benchmark datasets. Results show that the semantic-flow variant achieves competitive or superior faithfulness compared to standard post-hoc baselines, while being substantially more computationally efficient. Stability analysis further demonstrates that the explanations are robust and identifies regimes where interpretation should be applied with caution.

---


### 27. [The Frame Kernel Method for Multiscale Operator Learning](https://arxiv.org/abs/2608.25084)

**<font color=#1a73e8>作者：</font>** Branden Frieden, Ryan Whitehead, M. Keith Ballard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a natively multiscale operator learning method for the surrogate modeling of (numerical solvers for) multiscale partial differential equations (PDEs). The primary novelty of our method lies in a novel multiscale kernel frame function approximation technique. Leveraging this new kernel frame technique, we cast the operator learning problem as one of learning frame coefficients of output functions as a function of frame coefficients of input functions. The generalization step then automatically allows for a multiscale decomposition of the output functions. Our method is applicable to both tensor-product grids and point clouds. We present interpolation proofs, error estimates, and numerical convergence rates for our frame approximation. We the demonstrate the applicability of our method for the surrogate modeling of inherently multiscale PDEs. The new multiscale frame kernel method is significantly more accurate than popular neural operators on challenging problems from the literature, while simultaneously admitting an a posteriori multiscale decomposition upon generalization.

---


### 28. [Teaching Geometric Proof with Tech: Pitfalls and Possibilities](https://arxiv.org/abs/2608.25117)

**<font color=#1a73e8>作者：</font>** Hwei-Shin Harriman, Wode Ni, Yuchen Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Geometric proof is a foundational yet challenging topic in mathematics, requiring students to integrate visual, logical, and notational skills. While technology has enhanced learning in other mathematical domains, its impact on geometric proof remains limited. To investigate this gap, we interviewed 18 geometry teachers to establish the technical requirements of educational proof tools. These requirements inform our review of 33 commercial and research tools. Our findings reveal a critical mismatch: while teachers value certain digital tools for initial planning and exploration activities, they revert to pen-and-paper for formal proof because it supports diagram annotation and provides space for multiple approaches to proof-solving. Annotating the diagram is a key component of the proof-solving workflow that existing tools do not support. We propose four technical and human-centered design guidelines for educational proof tools to meet teacher needs at scale: integrating diagram and proof, generating problems and feedback automatically, supporting multiple proof formats, and reducing accidental complexity in the user experience.

---


### 29. [Toward Machine Learning with the Unit as a Primitive: Learning from Unit-Linked Events](https://arxiv.org/abs/2608.25118)

**<font color=#1a73e8>作者：</font>** Heyang Gong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning is usually formalized through samples, while the persistent individual to which multiple observed or possible events refer often remains implicit. We propose the \emph{unit} as an explicit primitive at the level of task semantics. A learning task first declares a population of persistent referents and a sameness criterion; the realized value $u$ denotes the selected referent. Supervised learning is the main formal specialization. Its semantic object is a family of unit-conditioned response laws. Homogeneity is the special case in which those laws coincide; a sample-only conditional is silent as to whether the world is homogeneous or the observed law is only the marginal of a heterogeneous family. What is learned from data is a pair $(T_\phi,R_\theta)$: a tokenizer that produces a contextual unit token and one shared response-law form that reads it. The structured class takes that form to be a simple relation in the token; a linear predictor is the running instance. The token is the learner-side representation through which the task-side unit affects prediction, while a learner specification that omits unit information is unit-insensitive; homogeneity remains a property of the world-side response family. When identity is unresolved, the world-side law mixes unit-conditioned targets, while the learner composes its shared form with a token. A trusted resolver may fix the unit and supply a lookup token; otherwise \emph{unit abduction} forms a token of the same type from factual evidence. Unlinked single-row observations can fail to distinguish a heterogeneous unit world from a homogeneous pooled world; trusted same-unit pairs separate a restricted witness. The formal results concern this supervised specialization.

---


### 30. [Static Detection of Post-Quantum Cryptographic Algorithms in Stripped Binaries for Digital Forensic Examination and Migration Assurance](https://arxiv.org/abs/2608.25122)

**<font color=#1a73e8>作者：</font>** Muhammad Shaheer Bin Junaid  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Currently, there is no method to verify from compiled binary code whether a quantum-vulnerable algorithm has been replaced by an approved post-quantum algorithm. Cryptographic discovery tools identify algorithms by symbols, library dependencies, and runtime behaviour; however, all these signals are destroyed by stripping, statically linking, and optimising a binary. This paper presents Kestrel, a static analysis method for identifying the standardised lattice-based schemes ML-KEM and ML-DSA in stripped binary code. Kestrel identifies ML-KEM and ML-DSA by detecting the number-theoretic transform constant tables that form the read-only data upon which the arithmetic depends. The fingerprints Kestrel derives from public scheme parameters are localised by means of a normalisation-and-multiset-matching procedure; the false-positive probability is established analytically. In experiments on four independent implementation lineages and all build transformations, including compiler-level obfuscation, Kestrel achieved recall of 128 of 128 with zero false positives. Applying Kestrel to 6,224 binaries on a production Linux system disclosed twelve uncatalogued programs containing ML-KEM; these included the OpenSSH key-exchange program and the container-management stack. In several of these programs, post-quantum code entered production through the language runtime without the awareness of the projects distributing them. Kestrel distinguishes genuine post-quantum implementations from advertised claims not backed by the underlying code, attributes each detection to its originating codebase, and, in a forensic disk-image trial, recovered a detection from unallocated space after the deleted binary could no longer be reconstructed. Thus, Kestrel provides a practical basis for cryptographic migration assurance, software supply-chain inspection, and post-quantum forensic examination.

---


### 31. [Multimodal Injury Risk Prediction in Tennis](https://arxiv.org/abs/2608.25126)

**<font color=#1a73e8>作者：</font>** Francisco Erramuspe Alvarez, Shobharani Polasa, Weihao Qu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning has had a significant positive impact on the prediction of athlete performance and injury risk. Most works in this field rely on subjective observations and expert assessments, which restrict their effectiveness. In sports like soccer, basketball, and wrestling, some studies attempt to address this challenge by integrating data from alternative sources, such as readings from wearable devices, alongside traditional subjective observations and expert assessments to enhance accuracy. However, similar research in tennis remains largely unexplored. In this paper, we propose a multimodal Predictive Athlete Readiness framework for Tennis (PART) to assess both performance and injury risk in tennis players. By leveraging machine learning and deep learning techniques, PART processes multiple sources of data collected from nine collegiate tennis players, including physiological metrics, training and match data, sleep data from wearable devices, self-reported information via daily questionnaires, jump assessments, and motion analysis from match play videos. PART captures four characteristics of tennis players: overall wellness, injury risk, physical capability, and playing style. By integrating these four characteristics by supervised learning, it is capable of providing a holistic assessment of the tennis athlete's condition, along with advanced forecasts of specific body areas at risk such as the upper body (e.g., elbows) or lower body (e.g., knees). Our evaluation, conducted with data from nine collegiate tennis players, shows that PART achieves strong performance in predicting both overall wellness and injury risk. Additionally, our framework also shows promise for recreational tennis players, who often suffer from injuries due to incorrect playing techniques.

---


### 32. [Rethinking the Transferable Adversarial Attacks and Robust Defense in Federated Learning](https://arxiv.org/abs/2608.25133)

**<font color=#1a73e8>作者：</font>** Zuobin Xiong, Deval Mukherjee, Homook Cho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The development of federated learning (FL) techniques has helped improve the privacy preservation of users' data and extended the applications of machine learning models. However, the involvement of a large number of users in FL also creates open opportunities for different adversaries, such as poisoning attacks, Byzantine attacks, and adversarial example attacks. Yet, recent research has disclosed that existing poisoning attacks and Byzantine attacks can not achieve satisfactory penetration in realistic FL scenarios caused by strong assumptions, \textit{e.g.,} client selection rate, and the ratio of malicious attackers. In this paper, the transferability of adversarial examples among different client models is analyzed to understand the relation between adversarial examples and clients' data distribution. Moreover, to mitigate the attacks of transferable adversarial examples, we design a defense mechanism stemming from the transferability of model robustness by adversarial training. As a result, through theoretical analysis of transferability, we gain insights into adversarial examples and the vulnerability of federated learning systems. Our proposed adversarial attack and defense methods are evaluated via real-life datasets in various settings to show their performance over the existing state-of-the-art methods.

---


### 33. [Drift Variation Autoencoder: Unifying Generation and Representation Learning through Conditional Posterior Flow Matching](https://arxiv.org/abs/2608.25138)

**<font color=#1a73e8>作者：</font>** Jiarui Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic masking, cropping, or modality removal makes deterministic reconstruction an incomplete target: one observation can admit many clean completions. This work takes the corresponding posterior $P(X\mid C)$ as the common statistical object for conditional generation and generatively sufficient representation learning. Drift Variation autoencoder trains a masked encoder $Z=E(C)$ and a conditional flow decoder with one clean-prediction Flow Matching loss. The analysis first decomposes the ideal conditional KL into generator approximation and the representation deficiency $I(X;C\mid Z)$. It then derives orthogonal risk decompositions for conditional Flow Matching. For an affine Gaussian path, the clean-prediction representation gap is zero if and only if $P(X\mid Z)=P(X\mid C)$. Thus the encoder-dependent excess clean-prediction risk induced by Flow Matching and the profiled ideal conditional KL have the same posterior-sufficient zero set, without being numerically equal objectives. An exact conditional field with a zero-noise endpoint then generates $P(X\mid Z)$ and hence $P(X\mid C)$ at a joint ideal optimum. The result extends to continuous multimodal product spaces when the complete modality tuple remains the Flow target for every observation mask. On CrossGeom-4, an 18-run controlled benchmark, observable factors have linear-probe $R^2$ of $0.9990$-$0.9992$, shuffling the joint model's encoder condition increases conditional error by $13.5\times$-$15.7\times$, and joint target attention reduces disagreement on an unobserved factor shared by two outputs by $90.1$-$92.8\%$ relative to independent target decoders. Visible modalities are also generated and reconstructed, directly validating the full-tuple objective. Unconditional mode balance remains imperfect, delimiting the empirical claim to a controlled multimodal proof of concept.

---


### 34. [CA-less Mutual Co-Signing of Documents over a Unidirectional Visual Channel with Transported Hardware Attestation](https://arxiv.org/abs/2608.25144)

**<font color=#1a73e8>作者：</font>** Dmytro Diikun  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We describe and analyze a protocol for mutual co-signing of a document by two mobile devices that (i) communicate only over a one-way, lossy, low-bandwidth optical channel (an animated on-screen code read by the counterparty's camera), (ii) use no intermediary server on the trust path, and (iii) use no certificate authority. Trust in each party's public key is instead grounded in a hardware attestation token produced by the platform secure element, transported in full over the visual channel by a rateless (fountain) code and cryptographically bound into the co-signature. The core technical contribution is a two-stage hash anchor that removes the circular signing dependency inherent to interactive co-signing: the first party commits to the document before the identity of the second party is known, and the second party's identity is later bound to that commitment without invalidating the first signature. We give a threat model, define four security properties (anchor binding, co-signature inseparability, attestation-bound key provenance, and post-signing tamper evidence) and reduce them to standard assumptions (collision resistance of H and EUF-CMA security of the underlying signature scheme), with the secure element modeled as an ideal signing oracle. We report a working instantiation on iOS/Android using ECDSA P-256 in the Secure Enclave/StrongBox, SHA-256, Apple App Attest / Play Integrity, and an LT-style fountain code, together with an independent third-party verifier that recomputes all anchors and checks both signatures fully offline.

---


### 35. [SNAP-KG: Streaming Node Assignment via Projection for Knowledge Graph Entity Integration](https://arxiv.org/abs/2608.25149)

**<font color=#1a73e8>作者：</font>** Jui-Chien Lin, Mohammad Mohammadi Amiri, Oshani Seneviratne  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graph (KG) construction pipelines must continuously integrate newly arriving entities into a growing graph. Unlike inserting triples between existing nodes, a newly arriving entity has no graph connectivity: it emerges from the acquisition phase as a raw feature vector and must be assigned to a semantic community before entity resolution and link prediction can operate over a tractable candidate set. Existing multi-view graph clustering methods exploit multiple relation types as structural views, but are transductive: they assume a fixed graph and cannot assign unseen entities without retraining. We propose SNAP-KG (Streaming Node Assignment via Projection for Knowledge Graph Entity Integration), a framework supporting graph-structural multi-view relational clustering and inductive inference for streaming entities. SNAP-KG trains a projector to map a new entity directly to the learned embedding space using only raw features, enabling immediate cluster assignment without graph access or model retraining. Experiments on five benchmark multi-view graph datasets and a production-scale KG of 2.4 million nodes demonstrate multiple orders-of-magnitude inference speedups over retraining-based approaches and competitive clustering quality. As a candidate scoping mechanism for downstream tasks, SNAP-KG achieves 62-75% candidate search reduction on the five benchmark datasets and 97% on OGB-WikiKG2 for entity resolution and link prediction.

---


### 36. [What Do Audio-Visual Synchronization Metrics Actually Measure?](https://arxiv.org/abs/2608.25157)

**<font color=#1a73e8>作者：</font>** Jai Kumar Sharma, Peeyush Tapadiya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic AV-sync metrics are widely used to rank and train audio-visual generators, but they are rarely audited as measurement instruments. We jointly audit AV-Align, ImageBind AV-relevance, JavisScore, and Synchformer/DeSync under a common reliability protocol: controlled-distortion monotonicity, preprocessing sensitivity, rank uncertainty, cross-metric agreement, PEAVS-proxy agreement, and learned fusion. The result is an axis split, not a single winner: Synchformer/DeSync is the strongest temporal-offset tracker ($\tau=0.84$), ImageBind/JavisScore better match the PEAVS human-aligned proxy ($\tau=0.20$) and content-disruption families, and AV-Align is the weakest standalone metric. The metrics mutually disagree (Krippendorff $\alpha=0.066$), and neither linear nor simple $k$-NN fusion improves PEAVS agreement over the best individual metric. We recommend reporting AV-sync as a Reliability Card (metric-family breakdowns with confidence intervals) rather than a single bare synchronization score.

---


### 37. [Bayesian Flow Networks for Offline Trajectory Planning](https://arxiv.org/abs/2608.25163)

**<font color=#1a73e8>作者：</font>** Ludvig Killingberg, Helge Langseth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (RL) leverages static datasets to learn decision policies without real-time environment interaction. While recent sequence-modeling approaches rely on continuous diffusion models for trajectory synthesis, applying these methods to discrete planning tasks requires a categorical formulation rather than the standard Gaussian construction. We present BFN-RL, a unified generative modeling framework for offline RL based on Bayesian Flow Networks (BFNs). By iteratively evolving distribution parameters rather than noisy data instances, BFN-RL natively models both discrete and continuous trajectory spaces within a single probabilistic formulation. The categorical planner generates future state sequences, and a learned inverse-dynamics model converts consecutive generated states into actions. Evaluations in discrete planning and continuous control show that BFN-RL can generate effective trajectories across both categorical and continuous state spaces. Our results establish BFNs as a versatile generative foundation for offline trajectory planning across data modalities.

---


### 38. [BGPay: An Incentive-Compatible Mechanism for BGP Hijack Filtering](https://arxiv.org/abs/2608.25165)

**<font color=#1a73e8>作者：</font>** Tomasz Sadowy, Constantine Doumanidis, Maria Apostolaki  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> BGP hijacking remains a persistent threat as existing defenses, including RPKI/ROV suffer from a fundamental incentive misalignment: the networks best positioned to filter malicious announcements bear operational costs but receive no direct benefit, while the victim prefix owner captures all the value. We advocate a market-based alternative in which prefix owners post standing bounties for filtering invalid announcements of their prefixes, turning filtering from altruism into a private transaction. Our insight is that neither a propagating hijack nor its absence can hide from public route collectors, whose committed routing tables could become an independent root of trust for releasing funds of the bounty. We build on this insight to design BGPay, an escrow protocol in which filterers and monitors commit before either reveals, and a smart contract pays out on evidence rather than on the prefix owner's judgment. Analyzing 1K real hijack incidents, we find that today's collectors already provide enough visibility where it matters: ASes that are more important for containing the hijack are also highly visible from the public monitors. Hence, setting rewards proportionately to containment impact discourages misbehavior.

---


### 39. [See More, Detect Less? Taming Information Leakage in Multi-View Anomaly Detection](https://arxiv.org/abs/2608.25168)

**<font color=#1a73e8>作者：</font>** Shang-Fu Chen, Kuan-Chuan Peng, Jhih-Ciang Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In multi-view anomaly detection, more cross-view information can actually hurt. When multiple inspection views are naively fused in a reconstruction-based pipeline, normal cues from intact views propagate to the decoder, which faithfully reconstructs anomalous regions, collapsing the reconstruction gap the detector depends on. We call this failure mode \emph{cross-view information leakage} and show that effective multi-view fusion must explicitly restrict the information reaching the decoder. Building on this insight, we present GLAD(Global-Local Attention Driven framework), the first framework combining vision foundation model features with local and global cross-view fusion for multi-view anomaly detection. The Multi-view Merging Attention (MMA) module performs local cross-view fusion at linear complexity with learnable view importance weighting and token-wise gating, letting each view selectively incorporate fine-grained evidence from other views at $\mathcal{O}(N)$ cost. The Object-Guided Attention (OGA) module captures global context by aggregating class tokens from all views into a single object-level representation and broadcasting it back to patch tokens via temperature-scaled sigmoid gating, replacing the original patch representations rather than adding a residual to preserve the reconstruction gap. Experiments on Real-IAD and MANTA-Tiny show that GLAD outperforms state-of-the-art methods across sample-, image-, and pixel-level metrics, confirming that principled information restriction is key to multi-view anomaly reasoning.

---


### 40. [Lowering the Barrier to AI-Driven Inspection: A No-Code Workflow for Automated Structural Defect Detection](https://arxiv.org/abs/2608.25176)

**<font color=#1a73e8>作者：</font>** Michael Holm, Tanner McElroy, Xinghang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structural health monitoring (SHM) is essential in modern engineering, providing data for condition-based maintenance, lifecycle assessment, and predictive decision-making. Traditionally, SHM relied on visual inspection to detect defects such as cracks and deformations. Early computer vision (CV) methods, including thresholding, edge detection, and handcrafted features, aimed to automate this process but were highly sensitive to noise, imaging variations, and multiscale defects, limiting their reliability.
Recent advances in machine learning, particularly convolutional neural networks (CNNs) and You Only Look Once (YOLO), have improved defect detection accuracy and enabled real-time analysis. However, adoption in SHM remains limited due to technical barriers such as data labeling, model training, and deployment, which typically require programming expertise.
To address this gap, we introduce YOLOEZ, an open-source, GUI-based tool for end-to-end YOLO model application. YOLOEZ integrates data labeling, training, and inference into a single interface, enabling high-performance model development without code while supporting reproducible workflows.
Evaluation against existing software and classical image processing demonstrates that YOLOEZ not only outperforms traditional methods across most detection metrics, but also lowers adoption barriers present in other modern CV tools. By combining accuracy with accessibility, YOLOEZ facilitates wider use of AI-driven monitoring for predictive maintenance, digital twins, and intelligent structural systems.

---


### 41. [Lightweight Machine Learning-Driven Monocular Sidewalk Path Extraction for Embedded Micromobility Navigation](https://arxiv.org/abs/2608.25178)

**<font color=#1a73e8>作者：</font>** Lkhanaajav Mijiddorj, Yang Yan, Tyler Beringer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sidewalk-scale path extraction demands perception and planning that run reliably on compact, low-power hardware in cluttered, map-sparse environments. We present a monocular vision pipeline for sidewalk path extraction in micromobility systems that progresses through three design iterations, from a skeleton-graph baseline through distance-transform corridor planning to a lightweight image-space architecture, and provides a systematic comparison of five path-planning methods across both bird's-eye-view (BEV) and image-space domains. A compact SegFormer-B0 student model, trained with a semi-supervised teacher-student framework using OneFormer Swin-L pseudo-labels, achieves a hand-annotated IoU of 0.946 at 11.7 ms per frame, improving over the baseline checkpoint (IoU 0.758, 18.9 ms). In a controlled planner comparison on 32 hand-labeled frames, image-space midpoint planning achieves the lowest lateral center error (14.3 px) at 2.2 ms, a 421x speedup over BEV distance-transform planning (926.8 ms, 65.0 px center error), while maintaining comparable mask-path alignment (98.5% versus 98.6%). A full-video replay across six campus sequences (22,679 frames) confirms that the improved segmentation reduces temporal instability from 1.46% to 0.33% and increases template-path availability from 73.7% to 79.3%. We further show that BEV-only path extraction is fragile in monocular settings: in one profiled run, 99.3% of frames produced no valid BEV path. The final recommended architecture, image-space midpoint primary, image-space distance-transform fallback, and BEV reserved for visualization, runs the full perception-to-path stack in under 50 ms per frame on CPU, making it suitable for embedded pedestrian-speed micromobility systems.

---


### 42. [Simultaneous inference of environmental and interaction forces in collective dynamics](https://arxiv.org/abs/2608.25181)

**<font color=#1a73e8>作者：</font>** Nipuni de Silva, Ming Zhong, James M. Greene  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collective dynamics arise in a wide range of physical, biological, and engineering applications. Examples include cell migration, swarm robotics, social dynamics, and animal behavior. A defining characteristic of these systems is the emergence of large-scale coordination from local interactions among agents; a fundamental question is thus to understand the local interactions that give rise to the observed emergent dynamics. We are interested in methods for learning interactions generally, which can describe a wide class of physical systems exhibiting collective dynamics defined by an interaction kernel, without a priori assumptions on the analytical form of this kernel (i.e. it is nonparametric). The advantage of this kernel-based approach is that it incorporates the underlying physics of the model (i.e. collective dynamics), which more general equation-learning approaches may ignore, potentially limiting their effectiveness for model accuracy and predictions. In this work, we extend existing variational learning approaches to collective systems with both interaction kernels and environmental/intra-agent forces. The proposed framework simultaneously infers the interaction kernel non-parametrically while learning the environmental force using either semi-parametric or fully nonparametric representations. The methodology is validated on several benchmark models exhibiting synchronization, alignment, attraction-repulsion, and external environmental forces. We also introduce a model-selection procedure based on our nonparametric learning framework to identify models that optimally explain a given set of trajectory observations. By exploiting the feature-identification capability of the learned models, the proposed procedure can distinguish among different collective dynamics frameworks and recover mechanistic interaction mechanisms directly from trajectory data.

---


### 43. [BanglaMamba: Exploring State Space Models for Bangla Fake News Detection](https://arxiv.org/abs/2608.25190)

**<font color=#1a73e8>作者：</font>** M. K. Khalidi Siam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fake news detection has become an important Natural Language Processing (NLP) task due to the rapid spread of misinformation through online news platforms and social media. While transformer-based models such as BanglaBERT achieve strong performance for Bangla text classification, their quadratic computational complexity makes them less suitable for long-document processing in resource-constrained environments. This paper investigates Mamba-based State Space Models (SSMs) as an efficient alternative for Bangla fake news detection. We propose BanglaMamba and compare it with pre-trained BanglaBERT and a similarly configured BERT model trained from scratch. Experimental results show that BanglaBERT achieves the highest Macro-F1 score (0.9260), while BanglaMamba (0.9029) achieves performance comparable to the from-scratch CustomBERT (0.9057) despite using a different architecture. Meanwhile, BanglaMamba achieves approximately $2.2\times$ higher inference throughput and 49% lower inference peak GPU memory usage than the BERT-based models. Cross-dataset evaluation shows that BanglaBERT generalizes better to an external dataset, highlighting the importance of large-scale pretraining. These findings demonstrate that Mamba-based SSMs can provide a competitive and computationally efficient alternative to Transformer-based architectures for Bangla fake news detection, particularly in resource-constrained settings.

---


### 44. [Hyperbolic Latent Geometry for Tree-Structured Prototype Networks: A Local-vs-Global Trade-off](https://arxiv.org/abs/2608.25199)

**<font color=#1a73e8>作者：</font>** Peter Flo, Luca Grossmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a tree-structured regularizer over class-prototype layouts in a hierarchical-classification model and ask whether the choice of latent manifold for the prototypes (Euclidean R^d vs. the Poincare ball B^d_c) affects how well that regularizer can be satisfied without distorting the data likelihood. The two manifolds differ only in their volume growth: hyperbolic space grows exponentially with radius and embeds trees with provably lower distortion than R^d of matched dimension, so the structured regularizer should be cheaper to satisfy on B^d_c. Across 150 seed-replicated regularized maximum-likelihood fits spanning embedding dimension, curvature, and regularizer strength on WikiArt (27 styles, 81,446 paintings, frozen CLIP ViT-B/16 features), we find a single robust effect: Poincare prototypes preserve the topology of the nearest-neighbor graph in latent space substantially better than matched Euclidean prototypes (sibling recall@5 +8.7 pp, cousin recall +15.2 pp; paired-t p < 10^-4, sign agreement 0.94), and the gap holds across three reference-tree definitions (hand-built lineage, CLIP-derived, and DINOv2-derived). On classification, Euclidean prototypes are tied with logistic regression on raw encoder features, indicating no detectable contribution from the latent geometry; only the hyperbolic fit improves on a k-NN encoder baseline for local retrieval. Global tree-fidelity comparisons are unstable across reference trees and we do not claim a winner. The results give an empirical separation, on a real hierarchical-classification problem, between two natural latent geometries for a class-structured regularizer.

---


### 45. [LibriBrain100: One Hundred Hours of Broad and Deep MEG Data for Neural Speech Decoding at Scale](https://arxiv.org/abs/2608.25204)

**<font color=#1a73e8>作者：</font>** Francesco Mantegna, Dulhan Jayalath, Gereon Elvers 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce LibriBrain100, a large-scale MEG dataset for speech decoding designed from the ground up for reproducible, standardised evaluation. LibriBrain100 more than doubles the size of the original LibriBrain release, resulting in over 100 hours of high-quality MEG acquired while subjects listened to naturalistic continuous speech. With $\sim$80 hours from a single subject, LibriBrain100 sets a new record for deep, within-subject neural data (8$\times$ more than the next comparable dataset and roughly 80$\times$ more than other datasets). To demonstrate the payoff of this depth-first design, we evaluate on a word-classification benchmark---an increasingly well-established stepping stone towards the open challenge of noninvasive brain-to-text decoding. Using an existing decoding model, we achieve state-of-the-art performance---validating both the quality of the recordings and the value of within-subject data at scale. Because collecting 80 hours of data per user is impractical for real-world applications, we also collected $\sim$40 minutes of additional data from each of 32 subjects. Using the same word-classification benchmark, we demonstrate the value of broad multi-subject data: supervised finetuning of a pre-trained model can substantially compensate for limited per-subject data. We provide standard train, validation, and test splits, all reproducible through an open-sourced Python library that supports easy downloading, optional preprocessing, and data loading for common deep learning frameworks. In addition, the dataset and evaluation infrastructure are being released alongside an open machine-learning competition with a public leaderboard for standardised benchmarking. Ultimately, our hope is that LibriBrain100 will accelerate progress towards practical non-invasive brain-computer interfaces, capable of restoring communication to people living with severe paralysis.

---


### 46. [Authenticated Data Structures for Dynamic Workloads](https://arxiv.org/abs/2608.25206)

**<font color=#1a73e8>作者：</font>** Ziheng Shangguan, Aviv Yaish, Dahlia Malkhi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce the Huffman-Merkle Tree (HMT), an authenticated data structure (ADS) for dynamic workloads where items may differ in access frequencies, and access frequencies can change over time. An ADS allows proving item membership against a short commitment to a large mutable state, with applications including verifiable storage, Internet transparency services, and blockchains. Optimizing ADS performance under continuously changing access frequencies has not been fully addressed before, neither in theory nor in practice. HMT addresses dynamically changing access skew through two complementary mechanisms. The first is a Huffman-coding-based Merkle-tree layout, with a novel extension to support evolving access frequencies. The second is an elastic tiering regime that partitions items across separate trees, such as hot and cold tiers, with adaptive migration between them. The key insight in this approach is to place frequently accessed items closer to the root, while assigning less frequently accessed items to progressively larger and deeper trees. This reduces the overall frequency-weighted access cost. Our scheme is designed to scale to gigabytes of data spanning millions of items. To handle dynamism efficiently, layout updates are applied in batches, access frequencies are tracked using a count-min sketch, and the system employs a tier-promotion cache while exploring multiple tier-migration policies. We implement HMT and compare it on real-world data with Ethereum's Merkle Patricia Trie (MPT) ADS and its proposed replacement, the Unified Binary Tree (UBT). Our evaluation considers two metrics: the amount of hashing per update and access-weighted membership-proof size. The latter captures both item access cost and frequency. We find that the best HMT policy uses about 2.4x and 0.34x less average hash operations than MPT and UBT respectively, and has 0.18x and 0.55x shorter proofs.

---


### 47. [Automotive HSMs - Architectural Challenges and Security Implications](https://arxiv.org/abs/2608.25216)

**<font color=#1a73e8>作者：</font>** Krishna Teja Medam, Austin Bruce  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automotive electronic control units (ECUs) increasingly depend on hardware-rooted security to protect software integrity, authenticity, and lifecycle management in the presence of remote and physical threats. Hardware Security Modules (HSMs) have become a key building block in automotive system-on-chips (SoCs), providing isolated cryptographic services, secure key storage, and controlled execution under stringent real-time and cost constraints. This paper presents an architectural analysis of automotive HSMs and examines their role in establishing secure boot and hardware roots of trust. We first survey common HSM integration models used in production ECUs and discuss their flexibility and current automotive use cases. We then introduce realistic threat models to motivate hardware-backed security controls and analyze how HSM design choices influence secure boot chains of trust, secure storage, secure execution, and software signing mechanisms. Key tradeoffs between isolation, performance, updateability, and attack surface are discussed, with optional consideration of side-channel implications. The paper concludes by highlighting open challenges and future directions for scalable and resilient automotive hardware security. Finally, we discuss emerging challenges such as cryptographic agility and post-quantum readiness that are likely to shape the next generation of automotive HSM architectures.

---


### 48. [The Systems Paper is Dead. Long Live the Systems Paper](https://arxiv.org/abs/2608.25219)

**<font color=#1a73e8>作者：</font>** Bjoern Hartmann  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The way we structure, conduct, and write up interactive systems research in UIST papers rests on assumptions about constraints that may no longer hold today. What should an impactful UIST paper look like when building working systems is no longer hard? I argue that it should look different, and that we should ask more of our papers once implementation stops being a bottleneck.

---


### 49. [Representing MAX functions using two-hidden-layer ReLU networks](https://arxiv.org/abs/2608.25221)

**<font color=#1a73e8>作者：</font>** Zhimao Wang, Amitabh Basu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study exact representations of $\mathrm{MAX}_N(x)=\max{x_1,\ldots,x_N}$ using two-hidden-layer ReLU neural networks. This problem has been studied in recent years in an attempt to characterize the exact number of hidden layers required to represent continuous piecewise linear functions. The best lower bound is 2, while the current upper bound is logarithmic in $N$. It remains completely open if the right answer is a constant number of hidden layers (possibly even 2!) or not. In fact, a recent breakthrough was the representation of $\mathrm{MAX}_5$ as a two-hidden-layer ReLU function obtained in [Bakaev et al., 2026], and the case of $\mathrm{MAX}_N$ was stated as open for $N\geq 6$ in that paper.
Using a careful computer assisted search, we obtain two-hidden-layer ReLU representations of $\mathrm{MAX}_5, \mathrm{MAX}_6, \mathrm{MAX}_7$, and $\mathrm{MAX}_8$. We obtain these by considering rational linear combinations of terms of the form $\max\{\sum_{r=1}^{s}\max(x_{a_r},x_{b_r}),\sum_{r=1}^{s}\max(x_{c_r},x_{d_r})\}$, where $a_r,b_r,c_r,d_r\in\{1,\ldots,N\}$. Each inner maximum of two coordinates can be computed in a first hidden layer, and the outer maximum of the two side-sums can be computed in a second hidden layer. Consequently, every finite linear combination of these terms has a two-hidden-layer ReLU realization. An identity for $\mathrm{MAX}_N$ in this form therefore gives an exact two-hidden-layer ReLU representation of $\mathrm{MAX}_N$.
Very recently, two-hidden-layer representations of $\mathrm{MAX}_N$ of the above form were obtained for all $N\leq 10$ in [Ruess et al., 2026]. Our representations are different and were developed independently. While our techniques share most of the high-level ideas presented in [Ruess et al., 2026], there are also some minor differences which may be of interest for future research on this problem.

---


### 50. ["Am I Just That Dumb?": Applicability, Action and Verification in Consumer IoT Security Advice](https://arxiv.org/abs/2608.25225)

**<font color=#1a73e8>作者：</font>** Veerle van Harten, Carlos Hernández Gañán, Michel van Eeten 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Public campaigns urge people to change default passwords on Internet of Things (IoT) devices and keep them updated, assuming users can independently determine whether the advice applies. We gave 28 participants in the Netherlands two pieces of government-issued advice reflecting guidance in several countries and asked them to try to apply each to three of six consumer devices selected from bestseller lists, not confirmed feature availability (168 sessions). The protocol asked for each action to be demonstrated rather than completed. Of 84 password sessions, 33 reached no password setting, 50 an account-level setting, and one a device-level setting. Of 84 update sessions, 27 reached no update, 19 a companion-app update, and 38 a verified firmware update. No product had a manufacturer-set credential shared across units as described by the advice; the single device-level credential was unique to its unit. We contribute an account of what generic advice and the devices it addresses let users determine, act on, and verify.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-171](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
