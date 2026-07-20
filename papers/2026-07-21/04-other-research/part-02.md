# 📦 其他研究 | 2026年07月21日

> 本类共 **152** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-152](./part-04.md)

---

### 51. [Benchmarking MRI Representations for Deep Learning-Based Focal Cortical Dysplasia Segmentation](https://arxiv.org/abs/2607.15605)

**<font color=#1a73e8>作者：</font>** Soumen Ghosh, John Phamnguyen, Amit Soni Arya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Focal cortical dysplasia (FCD) is one of the leading structural causes of drug-resistant focal epilepsy, yet its subtle and heterogeneous imaging characteristics make accurate identification and delineation challenging on conventional magnetic resonance imaging (MRI). Although T1-weighted (T1w) and fluid-attenuated inversion recovery (FLAIR) images are routinely acquired for presurgical evaluation, the contribution of different MRI representations to deep learning-based FCD segmentation remains poorly understood. In this study, we present a systematic benchmark of MRI representations for automated FCD segmentation using the nnU-Net framework. A publicly available presurgical MRI dataset comprising 85 FCD subjects and 25 healthy controls was used to evaluate eight input configurations, including conventional MRI contrasts (T1w and FLAIR), ratio-derived representations, and their multimodal combinations. To isolate the effect of MRI representation, all experiments employed identical preprocessing, network architecture, optimization strategy, and five-fold cross-validation. Among the evaluated single-modality representations, FLAIR achieved the strongest overall performance, whereas ratio-derived representations alone were insufficient for reliable identification of subtle FCD. Incorporating ratio-derived representations with conventional T1w and FLAIR images consistently improved lesion delineation, with the four-channel multimodal configuration achieving the highest overall Dice score (0.376), representing a 5.0% relative improvement over the conventional T1w+FLAIR representation. These findings demonstrate that MRI representation design is an important yet underexplored component of deep learning-based FCD segmentation and should be optimized alongside network architecture.

---


### 52. [Do Generative Models Keep Time? A Time-Aware Evaluation of Synthetic Sequential Tabular Data](https://arxiv.org/abs/2607.15606)

**<font color=#1a73e8>作者：</font>** Kiwan Kwon, Kangmin Kim, Hojin Lee 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic sequential tabular data are increasingly used for privacy-preserving data sharing, yet a generator can reproduce every marginal and every foreign-key relationship while emitting timestamps that run backwards or repeat, and while sending entities along paths that no real entity followed. Conventional tabular evaluation, which pools records into static distributions, is blind to such failures. We present a taxonomy-guided evaluation protocol for temporal fidelity, in which the applicable measurements are determined by the data rather than fixed in advance. Each dataset is first characterized along four properties: how time is represented, whether observations are regularly sampled, whether trajectories are mutually dependent, and how the schema links entities to their histories. These properties determine which evaluation dimensions are meaningful. The protocol then measures timestamp validity, cross-sectional structure at aligned time points, within-entity dynamics, and time-varying relational structure, and recasts utility and privacy evaluation over trajectories rather than isolated rows. We apply the protocol to eight generative models across thirteen datasets spanning six domains. Rankings under conventional evaluation disagree substantially with those obtained under temporal evaluation, and the resulting failures are architecture-coherent rather than random. Temporal fidelity must therefore be measured on the time axis itself, rather than inferred from pooled record distributions.

---


### 53. [ASK-NN: An Asymmetric Nearest-Neighbor Test that detects Distribution Drifts in Natural Language](https://arxiv.org/abs/2607.15607)

**<font color=#1a73e8>作者：</font>** Sergey Zakharov, Rodion Oblovatny, Alexey Zaytsev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hallucinations and artificial text in LLM-generated outputs often appear as distributional deviations between prompt and response hidden-state distributions. Since prompts or retrieved contexts typically serve as reference samples and responses as query samples, with major differences in length, these asymmetries motivate the use of change test statistics that treat the two samples differently. We consider an asymmetric two-sample test ASK-NN based on the directed k-nearest-neighbor graph. Our statistic counts reference points whose nearest neighbor in the pooled sample is also a reference point. Under the permutation null, it admits an exact finite-sample conditional mean and variance; we further establish asymptotic normality and consistency under fixed alternatives. ASK-NN is computationally effective and easy to implement. Empirically, it is competitive with kernel and graph-based baselines on synthetic benchmarks, artificial-text detection, and LLM hallucination detection from token-level hidden states.

---


### 54. [Visualization Autocomplete: Visualization Authoring via Stepwise Design Recommendations](https://arxiv.org/abs/2607.15608)

**<font color=#1a73e8>作者：</font>** Hyeon Jeon, Sungbok Shin, Niklas Elmqvist  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When domain experts create charts, the bottleneck is rarely the data, but knowing the optimal next step in chart design. The visualization design space is vast, and while domain experts can recognize a good design when they see it, it is often challenging to determine the exact path to get there. To address this, we present VISAUTOCOMPLETE, a system inspired by text autocompletion that reconceptualizes visualization design as a sequential process, recommending concrete next steps at each stage of the authoring process based on common practices. Users can intervene at any step, or delegate multiple steps to the system and select one from the design recommendations. To support responsive interaction, we distill the translation logic of a large language model (LLM) into a single function that receives the current chart state and recommended transition as input and returns the updated chart specification as output. We evaluate the system against a LLM vibecoding, Microsoft Excel, and TaskVis, an automated chart recommendation engine, on chart quality and approachability. Our results show that VisAutocomplete outperforms all baselines in the articulacy of complex chart authoring, while remaining on par with LLM in approachability.

---


### 55. [Process Reward Informed Tree Rollout for Effective Multi-Turn RL](https://arxiv.org/abs/2607.15610)

**<font color=#1a73e8>作者：</font>** Xintong Li, Sha Li, Yuwei Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a key approach for training LLM agents, yet popular methods such as GRPO/RLOO rely on multiple independently sampled complete trajectories for advantage estimation. In long-horizon agentic tasks, such a uniform rollout strategy can waste budget on uninformative dead-end attempts, while promising intermediate states do not receive sufficient exploration. The multi-turn structure of agentic trajectories, with interleaved actions and observations, naturally supports organizing a trajectory group as a tree, where each turn serves as a decision point for exploration. This perspective reframes effective exploration as the problem of deciding where to branch. We propose Process-Scorer Guided Adaptive Tree Rollout (PATR), a quality-aware rollout framework for multi-turn agent RL. PATR uses task-appropriate process feedback to score partial trajectories, selectively branches from promising states, reuses shared prefixes, and conservatively stops degenerate paths to reduce wasted sampling. The resulting rollout groups remain compatible with standard policy optimization while providing more efficient exploration under the same training budget. We evaluate PATR on FrozenLake and the challenging SWE-Bench, which is largely unexplored by prior tree-rollout agent RL methods. Experiments show that PATR improves performance by up to +5.0 points on SWE-Bench and +9.3 points on FrozenLake, highlighting process-guided tree rollouts as an effective strategy for scalable multi-turn RL.

---


### 56. [Region-Grounded Vision-Language Learning for Detection-Guided Mammographic Lesion Classification](https://arxiv.org/abs/2607.15615)

**<font color=#1a73e8>作者：</font>** Zhengbo Zhou, Jiren Li, Dooman Arefan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models trained with contrastive objectives have shown promise in medical image analysis. However, conventional global image-text alignment is ill-suited for mammography, where diagnostically relevant lesions are spatially localized and occupy only a small fraction of the image. Subtle morphological cues critical for malignancy assessment can be diluted when representations are learned at the whole-image level. In this work, we propose a novel region-grounded vision-language learning method for detection-guided mammographic lesion classification. The method mirrors radiologists' diagnostic paradigm. First, a region-text contrastive pretraining stage aligns lesion-specific features with structured clinical descriptors derived from radiology metadata. To mitigate semantic collapse and background bias in low-vocabulary settings, we introduce a multi-component objective incorporating positive alignment, fine-grained semantic hard negatives, and background suppression. Second, an auxiliary lesion detection head is jointly optimized with contrastive classification to preserve spatial sensitivity and enable localization-aware malignancy classification. Extensive experiments on two independent datasets, CBIS-DDSM and VinDr-Mammo, show superior performance of our method compared to related methods under in-domain, cross-dataset, and transfer learning settings.

---


### 57. [StructGen: Disambiguating Multi-Reference Image Generation via Structured Context Modeling](https://arxiv.org/abs/2607.15619)

**<font color=#1a73e8>作者：</font>** Jianing Peng, Mengyu Wang, Henghui Ding 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-reference image generation aims to synthesize images by integrating attributes from multiple reference images under textual instructions. As the number of references increases, the task necessitates complex semantic comprehension, such as correctly associating attributes with the intended subjects and planing out coherent spatial arrangement between subjects and their environments. Existing approaches, which rely solely on natural language instruction, often fail to capture these complex intentions precisely, leading to semantic misalignment and inconsistent generation. We identify two key factors behind these limitations: natural language instructions are often verbose and ambiguous, and high-quality multi-reference data is scarce. To address these issues, we propose StructGen, which employs a structured, dictionary-like format to encode multiple reference images, thereby enabling explicit and unambiguous specification of generation intentions. To support this design, we construct a structured dataset based on high-quality real images and develop a corresponding training framework, along with a dedicated benchmark for challenging multi-reference scenarios. Extensive experiments on both public benchmarks and our proposed benchmark demonstrate that StructGen consistently outperforms existing methods on both semantic alignment and detailed reference-generation consistency, especially under complex instructions with multiple references. The code is available at \href{this https URL}{this https URL}.

---


### 58. [BCG-Former: Toward Pareto-Efficient Hyperspectral Image Classification via Band-Contextual Gating](https://arxiv.org/abs/2607.15639)

**<font color=#1a73e8>作者：</font>** Gaurav Sharma, Eungjoo Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral image (HSI) classification systems are increasingly deployed on platforms with strict computational budgets, such as UAVs and small spaceborne sensors. In these settings, accuracy alone is not enough; the model must also run within tight latency and memory constraints. Most recent HSI classifiers, however, focus on accuracy and pay relatively little attention to these constraints. We propose BCG-Former, a lightweight CNN-Transformer hybrid that targets this trade-off. The model introduces three innovations: (1) Band-Contextual Gating (BCG) for adaptive spectral recalibration using local inter-band context and learnable temperature sharpening, (2) a spectral summary token that bridges spectral and spatial features, and (3) single-pass Band-RoPE combined with linear attention for efficient joint representation learning. Evaluated on classical airborne (Pavia University, Salinas, Indian Pines, Houston 2013/2018) and UAV-borne benchmark datasets (WHU-Hi-LongKou, HongHu, and HanChuan), BCG-Former achieves over-all accuracy ranging from 91.51% on Houston 2018 to 99.49% on Houston 2013, while maintaining sub-millisecond inference latency (0.91-0.95ms) and using only 0.10-0.23M parameters. Across all eight benchmarks, BCG-Former consistently resides on or near the Pareto frontier of accuracy versus latency, outperforming or matching recent CNN-, Transformer-, and Mamba-based methods at a fraction of their computational cost. Ablation studies confirm that all three components are complementary, with BCG providing the largest individual contribution. These results establish BCG-Former as a strong accuracy-efficiency Pareto candidate for real-time and large-scale remote sensing applications.

---


### 59. [On the Structure of Address in Multi-Party Dialogue: From Discrete Labels to Continuous Levels](https://arxiv.org/abs/2607.15648)

**<font color=#1a73e8>作者：</font>** Taiga Mori, Koji Inoue, Divesh Lala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In multi-party dialogues between a dialogue system and multiple users, identifying to whom an utterance is addressed is a key challenge. Prior work has typically treated addressee detection as a multi-class classification task, selecting a single label representing an individual participant or the group. This formulation assumes that address is inherently discrete and has primarily been used for predicting turn-taking. In this paper, we revisit this assumption by analyzing address as a continuous phenomenon. Using a multi-party human dialogue corpus annotated by multiple annotators, we construct both binary address labels derived from majority-vote addressee labels and continuous address levels inferred from annotator judgments using a latent-variable model. We then examine how these representations relate to turn-taking as well as listener behaviors, including gaze and backchannels. Our results show that, in addition to turn-taking, both gaze and backchannels are associated with address. Furthermore, models using continuous address levels achieve better predictive fit than those using discrete labels, suggesting that address may exhibit graded structure. Finally, we discuss the future directions of addressee detection research based on the findings of this study.

---


### 60. [DiTango: Cost-Effective Parallel Diffusion Generation with Selective Attention State Reuse](https://arxiv.org/abs/2607.15650)

**<font color=#1a73e8>作者：</font>** Yuyang Chen, Runxin Zhong, Zan Zong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in AI-generated content have driven widespread adoption of Diffusion Transformers (DiTs) for high-resolution, long-duration content generation. While parallelization techniques accelerate diffusion inference, they face significant scalability challenges due to excessive communication overhead in multi-node environments.
We observe that sequence partitions in Context Parallelism (CP) exhibit distinct heterogeneity: spatially proximate partitions contribute more significantly to attention computation results. By mapping this heterogeneous pattern to hierarchical communication topology, we can access high-contribution partitions with reduced communication cost. This insight motivates our novel selective attention state mechanism that strategically balances partial attention computation and historical result reuse across denoising steps.
We present DiTango, an efficient parallel framework for DiT generation. DiTango features an anchor-guided state selection planner that optimizes computation-reuse decisions for each partition, complemented by a runtime that orchestrates efficient state-centric operations. This design achieves superior system efficiency while preserving generation quality.
Experimental evaluation on popular diffusion models demonstrates that DiTango achieves up to 1.9x end-to-end and 3.2x attention speedup with near-linear scaling in multi-node settings, while maintaining generation quality comparable to state-of-the-art approaches.

---


### 61. [CSS-BA: Gate-Guided Column Space Search for Bundle Adjustment](https://arxiv.org/abs/2607.15652)

**<font color=#1a73e8>作者：</font>** Ayano Kaneda, Takafumi Taketomi, Shugo Yamaguchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bundle adjustment (BA) remains a critical refinement module for image-based 3D reconstruction and continues to improve geometric accuracy even in learning-based pipelines. However, in low-parallax and near-rotational regimes, classical Schur-based Levenberg--Marquardt (LM) often becomes ill-conditioned and yields unreliable pose and calibration estimates. We propose Gate-Guided CSS-BA, a solver-side modification of Schur-LM that preserves the classical BA objective and trust-region framework while constraining each update to a geometrically informed low-dimensional subspace. By integrating Column Space Search (CSS) with geometry-aware gating, the method stabilizes the Schur-LM update without altering the estimation problem. In contrast to keyframe or state-selection approaches, all camera and point parameters remain in the optimization problem; only the update direction is restricted. The method serves as a drop-in replacement for existing BA pipelines. Experiments on both generic and challenging weak-geometry scenarios show more stable optimization, improved relative pose accuracy, and competitive calibration behavior while maintaining reprojection quality.

---


### 62. [PE-Field 4D: Video Generation Models as Canvas](https://arxiv.org/abs/2607.15667)

**<font color=#1a73e8>作者：</font>** Yunpeng Bai, Haoxiang Li, Qixing Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers have recently achieved strong performance in video generation, yet controlling scene geometry under viewpoint changes and camera motion remains challenging. In this work, we revisit the role of positional encoding in video diffusion transformers and show that it provides a useful spatial bias for geometry-aware control. Specifically, if reference tokens are encoded according to their projected locations in the target view, the denoising model is encouraged to retrieve content from position aligned regions of the input video. Building on this observation, we introduce a geometry-aware cross-attention mechanism that enables target video latent tokens to attend to structured context tokens derived from reference images or frames. To establish correspondence between the reference content and the target camera trajectory, we equip the context tokens with a projected positional encoding scheme that combines target-view 2D reprojection with depth-aware disambiguation. At the same time, we preserve the original spatiotemporal positional encoding of the generated video latent, allowing geometric guidance to be injected while maintaining consistency with the video model's native latent structure. The resulting framework provides a simple and effective approach for controllable video generation. It improves spatial controllability in viewpoint-dependent editing tasks, including camera re-trajectory, novel-view video synthesis, and geometry-aware video editing, while preserving the generative prior of the underlying video diffusion model. The code is available at: this https URL.

---


### 63. [Neural Non-Equilibrium Hamiltonian Monte Carlo for Corrected Boltzmann Sampling](https://arxiv.org/abs/2607.15682)

**<font color=#1a73e8>作者：</font>** Moxian Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from an unnormalized Boltzmann density requires proposals that move probability mass globally while retaining enough path-probability information for statistical correction. We introduce Neural Non-Equilibrium Hamiltonian Monte Carlo (NHMC), a train-then-correct learned Hamiltonian sampler. Starting from a tractable base distribution, NHMC learns stochastic Hamiltonian-style paths toward the target. Once training is complete, the learned proposal parameters are fixed; the proposal then generates complete paths and endpoint configurations, which are statistically corrected using the recorded non-equilibrium work. This dimensionless generalized work is determined by the probability ratio between the forward proposal path and a reverse reference path. During training, minimizing its mean reduces a path-space KL divergence and controls an upper bound on endpoint mismatch. During evaluation, the same quantity defines weights for self-normalized importance sampling on paths (path-SNIS), estimates normalizing constants or free-energy differences, and gives the acceptance ratio for path-space independent Metropolis-Hastings (path-IMH). The same forward-reverse laws also define a shared-bridge round-trip Metropolis kernel that acts directly on configurations and preserves the Boltzmann target. On double-well and finite-volume lattice $\phi^4$ targets, the NHMC construction gives corrected estimates when path overlap is sufficient; when overlap is poor, weight degeneracy, low acceptance, and long autocorrelation expose proposal failure. We additionally report a molecular internal-coordinate feasibility study using an MD prior and learned-force path proposal.

---


### 64. [Hierarchical Specialised Ensembles for Classification of Zebrafish Phenotypes Using the Selected Image Recognition Methods](https://arxiv.org/abs/2607.15698)

**<font color=#1a73e8>作者：</font>** Piotr S. Maciąg, Monika Maciąg, Magdalena Majdan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose and evaluate three hierarchical ensemble setups for zebrafish phenotype classification from embryo images. In all setups, stage 1 uses a single four-class classifier to assign images to one of the exclusive phenotypes: Normal, Chorion, Dead, or Other. Images classified as Other are then processed in stage 2, where the ensemble design differs across setups: a single multi-label classifier, two specialized multi-label classifiers, or an ensemble of binary classifiers. We compare these setups using three backbone architectures: ResNet18, ViT, and ConvNeXt. Overall, ConvNeXt achieves the best performance across setups, while the specialized hierarchical ensemble in setup 2 provides the best balance in terms of F1-score. The results show that the proposed specialised hierarchical ensembles are effective for zebrafish phenotype recognition, and suggest that ConvNeXt is particularly useful backbone model.

---


### 65. [GoStop: Reinforcement Learning for Adaptive Temporal Aggregation in Event-Based Feature Tracking](https://arxiv.org/abs/2607.15699)

**<font color=#1a73e8>作者：</font>** Youngho Kim, Hoonhee Cho, Jae-Young Kang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feature tracking plays a fundamental role in understanding scene motion and supports various downstream tasks. Event cameras, with their high temporal resolution and asynchronous sensing, enable low-latency and motion-robust perception, making them well-suited for feature tracking under fast and non-linear motion. However, existing event-based feature tracking methods rely on fixed heuristic rules based on hand-tuning for event accumulation. Such strategies fail to adapt to diverse motion dynamics, leading to degraded performance under abrupt motion changes or low-motion scenarios. In this paper, we model event accumulation as a sequential decision-making problem and introduce reinforcement learning (RL) framework to adaptively control the accumulation process for online event-based feature tracking. Our approach trains a RL agent that decides whether to continue accumulating events or to perform tracking inference based on motion cues. The proposed adaptive temporal agent enables dynamic adaptation to varying motion patterns without relying on hand-crafted rules. Furthermore, we introduce a Dynamic Event-based Tracking (DEFT) dataset with dynamic motion distributions to evaluate the robustness of the feature tracking. Extensive experiments demonstrate that integrating our plug-and-play framework to existing feature tracking methods consistently outperforms heuristic-based approaches, improving robustness under dynamic motion while offering a better balance between tracking accuracy and efficiency. Our project codes and datasets are available at this https URL

---


### 66. [A Benchmark for Electrical Load Forecasting Across Grid Levels: Time-Series Transformers Outperform Established Methods](https://arxiv.org/abs/2607.15705)

**<font color=#1a73e8>作者：</font>** Matthias Hertel, Sebastian Pütz, Jonathan Kolar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate load forecasting at multiple grid levels is essential for future smart grids, ranging from aggregated control area forecasts for balancing supply and demand to forecasts of individual end-consumer loads for demand-side management and energy management systems. We present a comprehensive benchmark for load forecasting across grid levels, comprising three datasets that represent a transmission system operator control area, low-voltage grid feeders, and individual end consumers. We evaluate ten methods for short-term load forecasting and find that Transformer-based approaches consistently outperform established methods, reducing forecast error by 6.6-10.7 %. To analyze the impact of architectural design, we introduce YAformer, a flexible Transformer architecture that integrates modifications from prior work and is optimized via hyperparameter optimization. However, the standard Transformer achieves superior performance, suggesting that these architectural modifications are not required for accurate load forecasting. We further evaluate the Transformer-based time-series foundation model Chronos-2, which demonstrates competitive zero-shot performance on two datasets but fails to accurately capture special events in the TSO data. Detailed analyses reveal model-specific strengths and weaknesses, and ablation studies highlight the importance of long input contexts, covariates and continuous retraining - aspects that are often overlooked in the time-series forecasting literature.

---


### 67. [Efficient Difficulty-Aware Dynamic Routing for Diffusion-Based Real-World Image Super-Resolution](https://arxiv.org/abs/2607.15711)

**<font color=#1a73e8>作者：</font>** Xue Wu, Kang Zhao, Kafeng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based methods have achieved impressive performance in real-world image super-resolution (Real-ISR) by leveraging large pre-trained stable diffusion (SD) models as powerful generative priors. However, these methods still face two key limitations. First, existing SD-based one-step and multi-step Real-ISR approaches adopt a unified processing paradigm for all input samples, ignoring the varying restoration difficulty across images. Second, the aggressive resolution reduction of the VAE in SD models (e.g., 8x downsampling) leads to irreversible loss of fine-scale details, which cannot be recovered by the subsequent diffusion process.
To address these limitations, we propose a Difficulty-aware Dynamic Routing (DDR) strategy that overcomes the rigid, one-size-fits-all processing paradigm. Specifically, we first design a difficulty estimator to predict the restoration cost of each input image, enabling automatic assignment to a network of appropriate capacity. Then, we construct a set of Real-ISR networks with varying model capacities by modulating the spatial downsampling ratio of the VAE in the SD backbone, thereby preserving more high-frequency information for challenging cases while maintaining efficiency for simpler inputs.
Extensive experiments have demonstrated the superior efficiency and effectiveness of the proposed model compared to recent state-of-the-art methods.

---


### 68. [Per-Stroke Temporal Control for Text-to-Motion via Action Units and Action-Detection Guidance](https://arxiv.org/abs/2607.15717)

**<font color=#1a73e8>作者：</font>** Euijun Jung, Youngki Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-motion models are competent at the action a prompt names but unreliable at when each stroke lands: four punches alternating left and right rarely return four separable strokes. We introduce typed temporal events called Action Units (AUs) that make the individual stroke -- its body track, action class, time window, and impact timing -- an explicit conditioning signal. We ground a frozen text-to-motion backbone on the AU set through a lightweight gated adapter injecting two streams (per-stroke tokens and a per-frame phase channel), and at inference close residual timing errors with a training-free classifier gradient from a frozen frame-level detector. We measure per-stroke control on StrokeBench, whose prompts specify count, ordering, track, and core-frame placement, paired with an audited stroke corpus. AU grounding markedly raises the rate of correctly placed single strokes over the strongest prior interface, at the best motion quality among text-, interval-, and frame-level baselines. The prompted core frame emerges as a further steerable axis.

---


### 69. [CardioMeta: Calibrated Multi-Task Prediction of Diabetes, Hypertension, and Cardiovascular Disease Across Population and EHR Data](https://arxiv.org/abs/2607.15721)

**<font color=#1a73e8>作者：</font>** S M Asif Hossain, Ruksat Khan Shayoni, M. F. Mridha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cardiometabolic diseases remain among the most persistent drivers of preventable morbidity because diabetes, hypertension, and cardiovascular disease frequently co-occur and share metabolic, vascular, demographic, and behavioral determinants. Existing machine learning studies for chronic disease prediction often emphasize discrimination on a single dataset, while underreporting label leakage, calibration, temporal robustness, external transportability, and subgroup reliability. This paper presents CardioMeta, a calibrated multi-task framework for joint prediction of diabetes, hypertension, and cardiovascular disease across population survey and electronic health record (EHR) data. The study uses NHANES for population-level model development and temporal validation, and MIMIC-IV for EHR-domain evaluation under substantial distribution shift. To reduce circular label reconstruction, the primary analysis excludes disease-defining variables from the corresponding prediction heads, while a full-clinical feature setting is retained only as sensitivity analysis. CardioMeta combines a shared cardiometabolic encoder with disease-specific gated heads and post-hoc probability calibration. In the leakage-reduced temporal validation setting, the model achieved a macro-AUROC of 0.839, macro-AUPRC of 0.536, macro-F1 of 0.614, and expected calibration error of 0.024, with modest but consistent improvements over strong gradient-boosting and neural tabular baselines. External evaluation on MIMIC-IV showed clear degradation under domain shift, while limited fine-tuning partially recovered performance. The findings indicate that the principal value of multi-task cardiometabolic modeling lies not in inflated accuracy, but in reproducible leakage control, calibrated probabilities, and transparent reliability reporting across heterogeneous healthcare data sources.

---


### 70. [Natural Backdoor Attacks on Speech Recognition Models](https://arxiv.org/abs/2607.15724)

**<font color=#1a73e8>作者：</font>** Jinwen Xin, Xixiang Lyu, Jing Ma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rapid development of deep learning, its vulnerability has gradually emerged in recent years. This work focuses on backdoor attacks on speech recognition systems. We adopt sounds that are ordinary in nature or in our daily life as triggers for natural backdoor attacks. We conduct experiments on two datasets and three models to validate the performance of natural backdoor attacks and explore the effects of poisoning rate, trigger duration and blend ratio on the performance of natural backdoor attacks. Our results show that natural backdoor attacks have a high attack success rate without compromising model performance on benign samples, even with short or low-amplitude triggers. It requires only 5% of poisoned samples to achieve a near 100% attack success rate. In addition, the backdoor will be automatically activated by the corresponding sound in nature, which is not easy to be detected and will bring severer harm.

---


### 71. [Event3R: Asynchronous-to-Global 3D Reconstruction from Event Camera via Spatial-Temporal Feature Aggregation](https://arxiv.org/abs/2607.15727)

**<font color=#1a73e8>作者：</font>** Jian Huang, Haotian Shen, Xinhao Lou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust 3D reconstruction is essential for robotics and embodied perception. Recent feed-forward approaches such as DUSt3R have demonstrated impressive progress in dense 3D reconstruction from RGB images, achieving global geometric consistency and strong generalization. However, extending such dense 3D reconstruction to event cameras remains challenging due to their asynchronous, sparse, and highly dynamic nature, as well as the lack of large-scale, well-labeled datasets. In this work, we introduce Event3R, a feed-forward framework that directly maps asynchronous event streams to globally consistent 3D point clouds. Event3R represents incoming events as spatial-temporal voxels, enabling time-aware feature integration through a temporal attention module that enhances the module's temporal feature learning. To further strengthen temporal representation learning and reduce reliance on labeled data, we propose a Masked Bin Modeling (MBM) strategy for self-supervised pre-training, enabling robust temporal representation learning with minimal labeled data, and retain it as an auxiliary fine-tuning objective. In addition, contrastive alignment and consistency regularization losses are incorporated during fine-tuning to reinforce structural correspondence and temporal coherence across views. Extensive experiments on both synthetic and real-world benchmarks demonstrate that Event3R achieves robust, temporally consistent, and globally aligned 3D reconstructions, significantly outperforming existing event-based methods.

---


### 72. [The Third Competition on Document Forgery Detection on ID-Cards and Passports](https://arxiv.org/abs/2607.15734)

**<font color=#1a73e8>作者：</font>** Juan E. Tapia, Mario Nieto, Juan M. Espin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a comprehensive analysis of the results from the Third International Competition on Document Forgery Detection on ID-Cards and Passports, which was held across two distinct tracks. Track 1 evaluates a synthetic-data-based ID-PAD system under controlled but diverse conditions, where the winning team, \textit{Incode}, achieves an $AV_{Rank}$ of 27.82%, confirming consistent performance across metrics and highlighting the importance of a balanced, generalizable design. In Track 2, the challenge intensifies with heterogeneous attack scenarios across different domains, where \textit{Incode} again achieved the top position with an $AV_{Rank}$ of 68.71% across thresholds, outperforming some baselines and established methods. These results demonstrate that PAD effectiveness requires not only high accuracy but also consistency across diverse attack types and imaging conditions. The success of this initiative across both tracks underscores the value of collaboration between companies and academic teams. This year, more than \textit{63 teams} were registered, and more than \textit{100 submission models} were evaluated. This competition has evolved into a leading benchmark state-of-the-art in PAD on ID documents, setting the standard for performance, reproducibility, and real-world applicability in secure identity verification.

---


### 73. [Learning Faster without Deeper Networks: A*-Inspired Batch Selection for Efficient CNN Training](https://arxiv.org/abs/2607.15745)

**<font color=#1a73e8>作者：</font>** Anxhelo Shehu, Enes Stastoli, Arben Cela  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Common practice when training Convolutional Neural Networks (CNNs) is to use randomly shuffled mini-batches. This creates two limitations: slower convergence, and a diminishing learning signal, since many samples are quickly classified as easy during training. We address these inefficiencies with A*-Inspired Batch Selection (A*-BS), a lightweight, model-agnostic strategy that formulates mini-batch scheduling as a heuristic search problem. Each batch is treated as a node in a search space and ranked using an A*-like score combining a loss-based difficulty measure with a reuse penalty. This encourages informative gradient updates and batch diversity throughout training, without modifying network architectures or optimization algorithms, so it integrates seamlessly into existing pipelines. We evaluate A*-BS on the twelve 2D classification tasks of the MedMNIST-v2 benchmark, using a deliberately simple architecture of approximately 2.25x10^5 parameters, compared against the ResNet-18 and ResNet-50 baselines reported by the benchmark. On half of these tasks, the lightweight model with A*-BS reaches higher accuracy and AUC than both ResNet baselines, with relative gains of up to 15%. An ablation under identical architecture and hyperparameters shows A*-BS outperforms random batch shuffling on all twelve tasks. Wall-clock measurements further show the lightweight CNN with A*-BS trains substantially faster than ResNet-18 and ResNet-50 on identical hardware. These results indicate that intelligent batch ordering can partially compensate for reduced architectural complexity, offering a computationally efficient alternative to deeper models, with reliability reinforced by strong performance even against deeper, more sophisticated architectures.

---


### 74. [Ciphertext- and Polynomial-Level Optimization for Fully Homomorphic Encryption](https://arxiv.org/abs/2607.15750)

**<font color=#1a73e8>作者：</font>** Seongho Kim, Heelim Choi, Jaemin Kim 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) schemes such as RNS-CKKS enable privacy-preserving services by allowing direct computation on encrypted data. While recent FHE compilers optimize FHE programs, they operate at the coarse-grained ciphertext level, where each ciphertext operation comprises a sequence of polynomial operations. At this granularity, the compilers miss optimization opportunities across ciphertext operations. This work presents Recifhe, a new multi-level compiler that supports not only ciphertext-level but also polynomial-level optimization. At the ciphertext level, Recifhe transforms a non-FHE input program into an FHE program by inserting ciphertext management operations and applies global optimizations. At the polynomial level, Recifhe eliminates redundant polynomial computations across ciphertext operations. Recifhe achieves a 1.25x speedup over ciphertext-level-only optimization.

---


### 75. [Trainable Spline Representations for Physics-Informed Learning](https://arxiv.org/abs/2607.15751)

**<font color=#1a73e8>作者：</font>** Giovanni Canali, Nicola Demo, Gianluigi Rozza  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work introduces Physics-Informed Splines (PI-Splines), a structured spline-based architecture for physics-informed learning. Instead of representing the solution of a differential equation with a neural network, PI-Splines directly parametrize the unknown field through a tensor-product B-spline expansion with trainable control coefficients. This formulation preserves the residual-based training paradigm of Physics-Informed Neural Networks while providing compact support, explicit smoothness control, analytical derivatives, and a direct geometric interpretation of the trainable parameters. When compatible with the spline representation, boundary conditions can be imposed strongly by fixing suitable boundary control coefficients. The proposed method is evaluated on several benchmark problems of increasing difficulty and compared with standard physics-informed frameworks under matched governing equations, collocation sets, loss terms, and optimization procedures, so as to isolate the effect of the approximation architecture. Numerical experiments show that PI-Splines provide a competitive and stable alternative to neural physics-informed architectures, particularly in settings where structured representations, locality, and parameter efficiency are desirable.

---


### 76. [CoG-Guided Weight Correction for Fault-Tolerant Deep Neural Networks](https://arxiv.org/abs/2607.15753)

**<font color=#1a73e8>作者：</font>** Bahram Parchekani, Samira Nazari, Ali Azarpeyvand 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Neural Networks (DNNs) used in safety-critical applications are vulnerable to hardware and memory faults that corrupt network weights and degrade reliability. In this paper, we propose a Center of Gravity (CoG) guided weight correction method that restores faulty weights based on their spatial characteristics within each layer. The proposed approach detects and corrects weight faults using distance-aware correction rules, eliminating the need for retraining or architectural modification. The effectiveness of the proposed method in terms of the capability of tolerating hardware faults has been evaluated through performing fault injection at different Bit Error Rates (BERs).
Experiments on safety-critical LSTM-based Networks, including StageNet for disease progression tracking and MTFNet for cardiac anomaly detection, demonstrate fault tolerance improvements of up to 230x and 6.41x, respectively, at a BER of 10^{-3}, with negligible accuracy loss. When extended to Convolutional Neural Networks (CNNs), the method achieves up to 49.55x and 20.79x improvements under comparable fault conditions on ResNet-18 and VGG-16, respectively. To the best of our knowledge, this is the first work to apply the CoG concept to neural network weight tensors for enhancing model reliability.

---


### 77. [DICOMHawk: A Cyber Deception Framework for Medical Imaging Infrastructure](https://arxiv.org/abs/2607.15754)

**<font color=#1a73e8>作者：</font>** Karina Elzer, Alberto Mongardini, Ricardo Yaben 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber-attacks against exposed healthcare infrastructure threaten sensitive patient data and clinical operations, yet existing defensive tools for DICOM-based medical imaging systems provide limited interaction and are easily fingerprinted. We introduce DICOMHawk, a cyber-deception framework that emulates DICOM and PACS services using realistic interactions, dynamically populated medical records, and embedded honeytokens. In an 86-day comparison and a 347-day deployment across multiple networks, DICOMHawk attracted more valid sessions than Dicompot, avoided honeypot detection, and captured 49 medical-related attacks. The results show that realistic, long-term, multi-location deception improves visibility into threats targeting medical imaging systems.

---


### 78. [GeoChrono: Benchmarking and Rethinking Long-Term Temporal Understanding in Remote Sensing](https://arxiv.org/abs/2607.15768)

**<font color=#1a73e8>作者：</font>** Yujie Li, Jiancheng Pan, Zhiwei Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing offers an unparalleled vantage point for observing the Earth's long-term surface evolution, yet it demands that a model not only perceive land cover at isolated moments, but also track changes, memorize evolution histories, and reason across time and space. However, existing studies lack a systematic evaluation that dissects these distinct competencies. To fill this gap, we introduce ChronoBench, a multidimensional benchmark that decomposes this task into four progressive cognitive levels (i.e., Land Cover Perception, Temporal Recognition, Long-Term Memory, and Spatio-Temporal Reasoning). The ChronoBench comprises 12 sub-tasks and 17,689 rigorously validated QA (Question-Answer) pairs. Extensive evaluations reveal that mainstream MLLMs fall drastically behind human experts, with Long-Term Memory emerging as the most critical bottleneck. Motivated by this finding, we further propose GeoChrono, an MLLM with enhanced capabilities for tracing, memorizing, and reasoning about long-term geographic evolution. Leveraging the physical prior that geographic parcels remain spatially fixed while their semantics evolve, we design a Temporal Trajectory Encoder~(TempEnc) that constructs per-location temporal trajectories for dedicated land cover evolution modeling, and we introduce a Coarse-to-Fine Token Compressor~(C2FComp) that adaptively preserves dynamic regions while compressing the static background. To support training, we also construct ChronoInstruct, a 104K-sample instruction-tuning dataset spanning all competency levels for training. GeoChrono achieves state-of-the-art performance on ChronoBench, surpassing the leading commercial MLLMs by over 20%, while C2FComp reduces visual tokens by over 56% while retaining GeoChrono's 94.6% performance. The code and data will be available at this https URL

---


### 79. [SlotMem: Character-Addressable Internal Memory for Narrative Long Video Generation](https://arxiv.org/abs/2607.15772)

**<font color=#1a73e8>作者：</font>** Yilai Liu, Xin Zhang, Shiyuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Maintaining recurring character identities across scene transitions and long temporal gaps is a central challenge in narrative long video generation. Methods targeting global consistency often retrieve memory using cues that are not aligned with character identity preservation, while recent character-centric variants still rely on coarse frame-level kv memory that entangles identity with incidental visual factors and lacks a continuous update mechanism under limited memory capacity. To address these limitations, we propose \textbf{SlotMem}, a character-addressable internal memory framework for multi-character narrative long video generation. Specifically, SlotMem uses a Character-Semantic Probe to localize character-relevant visual tokens from cross-attention responses, and a Memory Encoder to compress DiT tokens into compact role-wise slot memory. As generation proceeds, a Memory Writer conservatively updates each character's memory with new observations, while Character-Wise Cross-Attention retrieves the role memory and injects it only into localized tokens of the same character. Experiments on multiple narrative long video generation benchmarks show that SlotMem improves long-range character consistency over existing baselines, while maintaining comparable video quality. Our code is available at this https URL.

---


### 80. [From Diffusion to Reaction-Diffusion: A Dynamical-Systems View of Oversmoothing in Hypergraph Neural Networks](https://arxiv.org/abs/2607.15773)

**<font color=#1a73e8>作者：</font>** Zhiheng Zhou, Mengyao Zhou, Yancheng Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Higher-order couplings enhance the expressive power of hypergraph neural networks (HGNNs), but they also intensify representation collapse in deep propagation due to strong multi-way feature mixing. This work investigates hypergraph oversmoothing from a dynamical-systems perspective and develops a reaction--diffusion framework for depth-resistant hypergraph learning. By defining hypergraph gradient and divergence operators, we interpret message passing as an incidence-level diffusion process. The analysis of pure diffusion shows that its continuous semiflow exponentially contracts the null-mode-free component of node representations and drives the Dirichlet energy to zero, revealing hypergraph oversmoothing as an intrinsic transverse-energy dissipation phenomenon. Motivated by this analysis, we propose Hypergraph Neural Reaction--Diffusion (HNRD), which introduces a reaction mechanism acting on the transverse component to compensate diffusion-induced dissipation and stabilize discriminative variations. We establish global well-posedness of the proposed dynamics and prove that the null-mode-free Dirichlet energy remains bounded away from zero. A forward-Euler discretization provides a practical HNRD layer with a stability condition for deep propagation. Experiments on benchmark and synthetic heterophilic hypergraphs demonstrate that HNRD consistently improves over representative hypergraph baselines. Depth, robustness, and efficiency analyses further show that HNRD preserves stable performance and nonzero Dirichlet energy under deep propagation and perturbations. These results provide a principled dynamical framework for designing deep hypergraph architectures that maintain higher-order expressiveness without representation collapse.

---


### 81. [Scaling Time Series Classification via XAI-Driven Data Reduction](https://arxiv.org/abs/2607.15774)

**<font color=#1a73e8>作者：</font>** Davide Italo Serramazza, Thach Le Nguyen, Georgiana Ifrim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explainable AI (XAI) for time series has seen significant algorithmic growth, but its utility in providing measurable performance gains for downstream tasks remains under-explored. This paper bridges this gap by introducing drXAI, a novel methodology that repurposes XAI attribution methods for effective data reduction in Time Series Classification (TSC). The core challenge in modern TSC is scalability; state-of-the-art models, such as Transformers, exhibit quadratic complexity relative to sequence length and linear complexity relative to the number of channels. This renders them computationally prohibitive for massive datasets. drXAI addresses this by using a fast, GPU-accelerated classifier (Hydra) to generate local attributions. We aggregate these into global feature importance scores and employ an automated elbow-cut heuristic to select the most salient features without requiring manual thresholds.
We evaluate our approach on both synthetic and real-world univariate and multivariate datasets. On synthetic benchmarks, drXAI successfully recovers ground-truth features where traditional baselines fail. On real-world data, drXAI achieves between 80% and 90% data reduction while maintaining classification accuracy comparable to models trained on the full dataset. Most importantly, we show that drXAI allows resource-intensive models like ConvTran to scale to datasets that were previously inaccessible due to memory constraints. Our results show the benefits of using XAI not just for interpretability, but as a robust tool for feature selection and scalability in time series analysis. All our code and data are openly available.

---


### 82. [AquaAugmentor: A Novel Feature Augmentation Algorithm for Water Potability Prediction](https://arxiv.org/abs/2607.15775)

**<font color=#1a73e8>作者：</font>** Muntasir Tabasum, Al Zadid Sultan Bin Habib, Tanpia Tasnim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Access to potable water is crucial for health, economic development, and sustainability. However, accurately classifying water quality remains a significant challenge due to the complexity and variability of water source data. This paper addresses the challenge of predicting water potability through machine learning and deep learning algorithms. It introduces a novel feature augmentation algorithm, AquaAugmentor, to enhance the predictive performance of these models for low-dimensional datasets. Utilizing a dataset that includes chemical attributes of water, such as pH, hardness, solids, chloramines, sulfate, and others. This study evaluates the performance of the models with and without AquaAugmentor. Each model applied to classify water as potable or non-potable and its performance is then evaluated and compared based on test accuracy and AUC score. The results highlight the strengths and limitations of our proposed algorithm, providing insights into the most effective techniques for improving the predictive performance of water quality classification. This study contributes to the broader efforts of ensuring safe water access and serves as a framework for employing machine learning in environmental quality assessments. The findings aim to assist researchers, policymakers, and public health officials in making informed decisions based on reliable machine learning predictions.

---


### 83. [AgentFAIR: A Multi-Agent Collaborative Framework for FAIRness Evaluation of Geospatial Datasets](https://arxiv.org/abs/2607.15781)

**<font color=#1a73e8>作者：</font>** Ming Chen, Pranav Pai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geospatial datasets support applications from urban planning to climate modeling, yet consistent assessment of FAIR compliance is difficult. Existing evaluators use different rubrics and evidence sources and may fail on JavaScript-rendered pages or repository-specific identifiers. For 50 datasets from 10 repositories, the standard deviation of normalized scores across available tools averages 15.0 percentage points and reaches 30.3 for one dataset. Because these outputs are not equivalent measurements, we use them to characterize disagreement and failure modes, not comparative accuracy. We present AgentFAIR, a multi-agent framework combining structured metadata extraction with 13 sub-principle-specific LLM evaluators. Each produces a 0-3 maturity score, cited evidence, and recommendations; a critic checks evidence and consistency and can request targeted re-evaluation. Mean Findability, Accessibility, Interoperability, and Reusability scores are 79.7%, 70.4%, 45.3%, and 72.0%. Rank correlations with four baseline tools range from 0.31 to 0.61; the FAIR-enough comparison is not statistically significant. On a 10-dataset repeated-run subset, sub-principle agreement averages 89% (standard deviation: 3 percentage points), versus 71% without the critic. A preliminary 15-dataset expert study yields Fleiss' kappa of 0.71 and 82% alignment with expert consensus. API cost is approximately USD 0.054 per dataset. These results support auditability and feasibility, while the limited benchmark, incomplete ablations, and single-model-family validation constrain claims about accuracy and generalization.

---


### 84. [Vogls: a Fast Interactive Full-timing Simulator for Pre-silicon Power Side-Channel Analysis](https://arxiv.org/abs/2607.15782)

**<font color=#1a73e8>作者：</font>** Gijs Burghoorn, Ileana Buhan, Lejla Batina  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Designing hardware circuits resistant to side-channel attacks increasingly relies on simulation to predict device leakage before fabrication. Current functional verification simulators are designed for extended correctness-checking runs and are ill-suited for producing large numbers of short trace collections with slight input variants needed for side-channel analysis. We present Vogls: an open-source Verilog simulator built for side-channel analysis, that is the first simulator to combine compiled-code performance, full-timing simulation, and fine-grained control over the simulation state. Vogls simulates a timing annotated gate-level AES design 5.9 times faster than Icarus Verilog and is only 30% slower than Verilator on a PicoRV32 RTL design while also offering a more accurate timing model. Vogls provides a Python interface that allows simulations to be paused, forked, inspected, and mutated around points-of-interest without modifying the hardware design and thereby preserving timing and leakage characteristics. Furthermore, a trace-collection workflow runs setup code once and forks at the point-of-interest, eliminating the need to re-simulate from reset for every trace. A case study demonstrates Vogls on a differential power analysis attack that successfully recovers the key at RTL, GTL and full-timing GTL abstraction levels.

---


### 85. [On the Geometry of Learned Representations in Event-Based Multi-Modal Egomotion Estimation](https://arxiv.org/abs/2607.15794)

**<font color=#1a73e8>作者：</font>** Stefano Silvestrini, Michele Ceresoli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classical approaches to event-based egomotion estimation, including those adopted by the top-performing teams of the ELOPE challenge, rely on geometric optimization frameworks such as contrast maximization, homography estimation, or dense optical flow combined with analytic motion inversion. This work investigates the geometric structure that emerges inside a multi-modal network for egomotion estimation. Event tensors, inertial measurements, and range signals are fused through a cross-modal attention architecture and trained in a batch setting. We analyze the latent space geometry and attention dynamics, showing that (i) embeddings lie on low-dimensional manifolds aligned with motion variables, (ii) attention weights adapt with angular excitation and visual reliability, and (iii) the fused representation recovers classical observability cues. These results bridge analytical estimation theory and modern data-driven fusion.

---


### 86. [Knowledge-Assisted Multi-Graph Dependency Learning for Multivariate Time Series Anomaly Detection in Multi-Stage Industrial Processes](https://arxiv.org/abs/2607.15799)

**<font color=#1a73e8>作者：</font>** Jaeyeong Lee, Taeseong Yoon, Wonmo Koo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial processes often generate complex, interdependent time-series data from multiple sensors across multiple stages, forming complex dependencies among variables and process stages. Effective monitoring and timely anomaly detection of these time series through multivariate time series anomaly detection (MTAD) is crucial for preventing failures and ensuring the reliability of automated systems. Graph neural networks (GNNs) have advanced MTAD by leveraging data-driven graphs to model complex dependencies among variables, effectively capturing relational structures within multivariate time series to enhance anomaly detection performance. However, existing GNN-based approaches often overlook critical process knowledge, and even when this knowledge is considered, seamlessly incorporating it into existing models remains inherently challenging, leading to suboptimal performance. To address this limitation, we propose a knowledge-assisted multi-graph framework for modeling sensor dependencies in multi-stage industrial processes for MTAD, which explicitly incorporates process knowledge into graph learning to enhance dependency modeling and improve anomaly detection performance. Our method constructs three complementary graphs: one purely data-driven and two refined by integrating structural constraints derived from process knowledge. To effectively leverage these graphs for anomaly detection, we employ a multi-graph attention network, enabling a more accurate and robust representation of complex dependencies. Comprehensive experiments on two real-world, multi-stage industrial datasets demonstrate that incorporating process knowledge substantially enhances anomaly detection performance.

---


### 87. [HybridSim: A Physics-Learning Hybrid Digital Twin for mmWave Human Sensing](https://arxiv.org/abs/2607.15806)

**<font color=#1a73e8>作者：</font>** Weitao Xiong, Tianyu Liu, Peng Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity simulation of mmWave radar signals for dynamic human motion is valuable for developing radar-based human sensing models; yet collecting accurately labeled measurements for a specific deployment site remains expensive. We present HybridSim, a physics-learning hybrid simulator that synthesizes mmWave radar signals from dynamic human meshes under a fixed indoor room configuration, explicitly decoupling propagation into two components. To parameterize the human subject, we use a tri-plane representation to extract human features and a Graph Convolutional Network to stabilize optimization and mitigate gradient instability. The direct signal path is modeled via an inverse-rendering formulation with a microfacet BRDF to capture primary surface reflections. In parallel, the indirect path is approximated by combining 3D Gaussian Splatting with a virtual-receiver geometry to fit and reproduce site-specific multipath interference patterns, achieving substantially lower computational cost than explicit full ray tracing. Experiments in a fixed-room setting show improved agreement with a physically based reference and consistent gains on downstream radar-based human sensing tasks when using HybridSim for site-specific data augmentation.

---


### 88. [Examining the Associations between Visual and Non-Visual Elements and Cyclists' Route Choices for Various Trip Purposes](https://arxiv.org/abs/2607.15808)

**<font color=#1a73e8>作者：</font>** Heyang Hua, Koichi Ito, Filip Biljecki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding cyclist preferences for the characteristics of the built environment is important in promoting sustainable urban transportation and active mobility. Despite previous studies on cyclists' route choices, the influence of visual and non-visual factors on these choices for different trip purposes remains unclear; thus, this paper fills this gap through a data-driven case study in Montreal, Canada. Non-visual factors include socioeconomic factors and two-dimensional environments, while visual factors involve visual perception during cycling and are computed using street view images. The study consists of two parts: one part analyzes spatiotemporal information to explore the non-visual factors between the start and end points of cycling trips, and the other part investigates the discrepancies in distributions of these factors between the shortest path and the actual one. The findings reveal the spatiotemporal characteristics that influence active riding choices, such as increased greenery and lower levels of motorization. These insights can inform the planning of street networks and the development of infrastructure to improve the use of active transportation.

---


### 89. [Graph Coloring Approach to Solving Sudoku with Oscillatory Neural Networks](https://arxiv.org/abs/2607.15814)

**<font color=#1a73e8>作者：</font>** Filip Sabo, Aida Todri-Sanial  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Oscillatory Neural Networks (ONNs) present an attractive physics-based computing paradigm rooted in the dynamics of a network of typically fully coupled oscillators aiming to minimize an underlying energy function. In this paper, we propose an ONN-based solver for one well-known constrained combinatorial optimization problem, namely a Sudoku, by formulating the problem as a Graph Coloring problem. By modifying the already existing Graph Coloring solver to a computationally cheaper version and introducing an additional term ensuring the fulfillment of the Sudoku constraints, our solver is shown to significantly outperform the existing HNN- and ONN solvers in terms of accuracy. In particular, we are able to achieve nearly flawless accuracies on $4 \times 4$ as well as rather high accuracies on $9 \times 9$ Sudoku puzzles for different numbers of unknown digits.

---


### 90. [Can't Stop: How Context and Individual Traits Influence Effectiveness of Different Gradual Interventions for Infinite Scrolling on Short-Form Video Platforms](https://arxiv.org/abs/2607.15818)

**<font color=#1a73e8>作者：</font>** Luca-Maxim Meinhardt, Manuela Dragic, Mark Colley 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Infinite scrolling on short-form video platforms like TikTok encourages prolonged engagement and post-usage regret. Interventions aim to mitigate such behavior, but their effectiveness may depend on the interplay between intervention type, contextual factors, and individual traits. In a 7-day within-subject randomized field study (N=104), we compared a baseline pop-up and two gradually intensifying design frictions (visual and haptic). We evaluated behavioral changes and user experience using objective and subjective measures. Results showed that the pop-up was initially effective but quickly lost impact, whereas the visual gradual intervention sustained subjective ratings the longest. Bayesian modeling revealed that self-regulation traits moderate how participants responded to the three intervention types. For participants with low impulsivity, the type of intervention had little influence on its subjective effectiveness. For participants with high impulsivity, however, differences between intervention types were substantial, with the explicit baseline pop-up being most effective compared to the novel gradual interventions. Contextual factors, in contrast, showed little influence. These findings suggest that intervention modality and individual differences in self-regulation shape intervention effectiveness.

---


### 91. [Cost-efficient generative AI summarization for scalable automated essay scoring in educational assessment](https://arxiv.org/abs/2607.15829)

**<font color=#1a73e8>作者：</font>** Haowei Hua  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated essay scoring (AES) enables scalable assessment and timely feedback but remains challenged by transformer input-length limitations, which can cause information loss when processing long essays. This study proposes a generative AI-assisted summarization framework to improve long-form essay representation while maintaining scoring reliability. Using the ASAP 2.0 dataset, we generate controlled-length summaries with three GPT-5 variants (GPT-5, GPT-5 mini, and GPT-5 nano) and use them as inputs for downstream AES models. To preserve original writing signals, handcrafted linguistic features extracted from full essays are integrated with summary representations to form a hybrid framework. The approach is evaluated in terms of scoring performance, summarization quality, and computational cost. Scoring reliability is measured using quadratic weighted kappa (QWK), while summary quality is assessed through lexical overlap, semantic similarity, information retention, and redundancy metrics. Results show that GPT-5 mini achieves the highest agreement with human ratings, whereas GPT-5 produces the strongest summarization quality. Summary quality decreases for higher-scoring essays, indicating that more complex writing is more difficult to compress without information loss. These findings reveal trade-offs among model capacity, summary fidelity, cost efficiency, and preservation of educational constructs. This study provides an initial controlled evaluation of GPT-based summarization for AES and identifies important baselines and ablation studies required for future generalization. Overall, generative AI summarization offers a promising approach for scalable writing assessment while requiring careful validation of information preservation and fairness.

---


### 92. [Data-Native Global Optimization for Big Data K-means Clustering](https://arxiv.org/abs/2607.15835)

**<font color=#1a73e8>作者：</font>** Ravil Mussabayev, Rustam Mussabayev, Zukhra Yerdaliyeva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Big data clustering remains challenging: the Minimum Sum-of-Squares Clustering (MSSC) problem underlying K-means is NP-hard, and existing methods either reach poor local minima or require prohibitive metaheuristic hybrids. We target arbitrarily tall data: a fixed feature space may contain arbitrarily many, possibly infinitely many, observations, while the algorithm accesses only finite random samples. We propose Big-means++, an algorithm achieving scalability and global-search quality by curating inputs to MSSC optimization on big data. It orchestrates local K-means refinements into a data-native global search for big data clustering. Rather than optimizing the full-data MSSC objective, Big-means++ traverses sample-induced surrogate landscapes. Each sample defines a distinct empirical MSSC approximation with a perturbed local-optimum structure, turning sample-to-sample variation into a global-search mechanism. Unlike Big-means, a flowing-incumbent strategy propagates centroid state across empirical landscapes through K-means refinements on fresh samples without rollback to a best-so-far solution. This increases mobility and favors stable, high-quality configurations across approximations of the full-data structure. A new shaking mechanism varies sample size geometrically, broadening the surrogate landscapes explored across resolution scales, accounting for cluster imbalance, and improving solution quality. A competitive multi-agent system asynchronously explores independent sampled landscapes, transforming diverse stochastic trajectories into collective search intelligence. Automatic convergence detection stops each agent after attaining a high-quality solution but before further search risks degrading it, while providing a universal speed-quality control. Experiments on 22 datasets against 11 competing algorithms demonstrate the effectiveness, efficiency, and robustness of Big-means++.

---


### 93. [Is That Really My X-Ray? Measuring Internet-Exposed DICOM Services in the Presence of Deception](https://arxiv.org/abs/2607.15839)

**<font color=#1a73e8>作者：</font>** Ricardo Yaben, Karina Elzer, Alberto Maria Mongardini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> DICOM is the dominant protocol for exchanging medical images, yet many Internet-facing deployments lack basic security controls, exposing sensitive patient data to unauthorized access. Accurately measuring this exposure is complicated by honeypots, network telescopes, and other measurement artifacts that inflate published estimates. This paper presents a noise-aware study of Internet-facing DICOM services, combining active IPv4-wide scanning with passive honeypot deployments. We scan common DICOM ports using an ethics-constrained probe limited to association negotiation and C-ECHO. Then, we introduce a reproducible false-positive filtering method that identifies honeypots, telescopes, malformed responders, and other deception artifacts, reducing apparent exposure by 39%. After filtering, we identify 3,979 vulnerable DICOM deployments, all of which lack encryption and accept unauthenticated connections; 1,782 run outdated or deprecated software, and 1,551 carry known remotely exploitable vulnerabilities. Follow-up scans reveal that approximately 50% of exposed services show no evidence of maintenance over 5 months of observation, and that responsible disclosure led to only modest, short-term remediation. On the passive measurement, we deploy Dicompot and find that its raw session logs overstate activity by up to 83% due to generic TCP noise being incorrectly logged as DICOM sessions. After filtering, we observe a reconnaissance gap: Most actors issuing C-ECHO probes never escalate to data exfiltration, consistent with sophisticated actors fingerprinting the honeypot and disengaging before proceeding. Our results show that DICOM exposure measurements can be significantly distorted by deception and logging artifacts, but once corrected, reveal widespread risks to patient privacy and healthcare security that existing deception systems are insufficient to capture.

---


### 94. [CAMMAR: Culture-Aware Matryoshka for Metaphorical Arabic Representations](https://arxiv.org/abs/2607.15847)

**<font color=#1a73e8>作者：</font>** Suzan Awinat, Alfonso Ortega del Puente  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Metaphor in Arabic is a culturally grounded mechanism for constructing meaning, encoding cultural knowledge that shapes interpretation. Yet current Arabic language models typically collapse lexical, cultural, and metaphorical information into a single representational space, a phenomenon we term "semantic smearing". We introduce CAMMAR (Culture-Aware Matryoshka for Metaphorical Arabic Representations), a representation learning framework that organizes meaning into nested lexical, cultural, and metaphorical embedding subspaces through a staged semantic curriculum. The design implements compositional principles of Al-Jurjani's theory of nazum, modeling figurative meaning as compositionally grounded in prior semantic relations, and yields a training-free geometric measure of metaphoricity based on the distance between lexical and metaphorical representations.
Evaluated on a new span-annotated Arabic metaphor set as word-matched figurative/literal pairs, the geometric readout detects metaphor well above chance when the inter-layer geometry is shaped by paired supervision (AUC up to 0.84; figurative outscores its literal counterpart for the same word in 82.6\% of pairs), but sits at chance under an unsupervised domain contrast alone, a clean separation between a legible-under-supervision regime and a non-emergent one. A controlled ablation shows that grounding the lexical layer in morphological roots gives a small but consistent gain, an effect absent from direct probing that reflects the layer's quality as a measurement anchor. We will release the datasets, cultural concept inventory, and code upon acceptance.

---


### 95. [Test-Time Noise Guided Adaptation for Realistic Autoregressive Video Generation](https://arxiv.org/abs/2607.15849)

**<font color=#1a73e8>作者：</font>** Dimitrios Karageorgiou, Symeon Papadopoulos, Ioannis Kompatsiaris 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models have enabled the generation of arbitrarily long videos by removing conditioning on future frames, thus greatly improving computational efficiency. Yet, they suffer from error accumulation over time, as the denoised sequence gradually drifts away from the conditioning distribution seen during training. Recent advances attempt to reduce this error by anchoring each generated frame to the learned manifold of real ones. However, even when all generated individual frames lie close to the real manifold, there are trajectories which the model lacks sufficient knowledge to continue without exiting it, thus reaching a terminal point. To prevent the model from being trapped in terminal points, we start from the hypothesis that for well-modeled future trajectories the distribution of the predicted noise should match the one of the forward noising process. To enforce such a prior at test time, we introduce Terminal points Avoidance through Noise Guided Optimization (TANGO), which uses the diffusion model as a critic of its own outputs, by predicting one step forward and requiring an isotropic Gaussian noise prediction. We use the deviation from this expected noise distribution to search for an alternative trajectory that does not lead to a terminal point. Our approach achieves a $3.1\%$ absolute improvement on VBench over state-of-the-art, while reducing Fréchet Video Distance by $28.3\%$ on average across $15$s videos. Our code is available on this https URL.

---


### 96. [Von Mises-Fisher Mixture Model with Dynamic Shrinkage for Realistic Test-Time Transduction](https://arxiv.org/abs/2607.15851)

**<font color=#1a73e8>作者：</font>** Jiazhen Huang, Zhiming Liu, Changhu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A range of methods aim to enhance the performance of vision-language models (VLMs) at test time. Among them, transduction has emerged as a promising paradigm due to its strong compatibility and efficiency. However, realistic evaluations often involve highly imbalanced class distributions, which cause performance degradation or even collapse. In this work, we systematically revisit transduction from the perspective of penalized likelihood estimation (PLE), showing that PLE with a KL-divergence anchor term naturally yields an adaptive shrinkage behavior between prior anchors and empirical estimates. From this viewpoint, the brittleness of transductive methods can be attributed to the absence of anchoring mechanism and static modeling of the shrinkage strength. Therefore, we propose Mixture of Von Mises-Fisher Models with Dynamic Shrinkage (MOON). MOON is built upon a mixture of von Mises-Fisher distributions to model feature representations on the unit hypersphere. To handle imbalance, MOON dynamically adjusts the shrinkage strength using zero-shot priors at both instance and class levels. Thus, it suppresses unreliable assignments and prevents harmful updates from outlier classes, thereby mitigating negative transfer. MOON is model-agnostic, training-free, and requires no task-specific hyperparameter tuning. Extensive experiments further validate the advantage of MOON in both performance and efficiency. Our code is available at this https URL

---


### 97. [Contextual Semantic Relevance Tracks fMRI BOLD Responses During Naturalistic Speech Comprehension](https://arxiv.org/abs/2607.15856)

**<font color=#1a73e8>作者：</font>** Kun Sun, Rong Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Naturalistic language comprehension requires listeners to process both local probabilistic expectations and contextual semantic relations. Surprisal has been widely used to quantify local word unexpectedness, but evidence that it robustly predicts fMRI BOLD responses during continuous comprehension has been mixed. This study investigates whether contextual semantic relevance, defined as how strongly an incoming word relates to its recent semantic context, predicts BOLD responses during naturalistic speech comprehension. We analyzed two public fMRI datasets, the Alice dataset and the Moth dataset, treating them as complementary rather than identical replications. Transformed BOLD responses were modeled with generalized additive mixed models (GAMMs) and original continuous BOLD time series were tested with FIR/deconvolution analyses. In Alice, semantic relevance was significant across all 12 ROIs (region of interest), whereas surprisal was not significant after FDR correction. In Moth, semantic relevance showed consistent negative effects across all 30 ROIs, while surprisal showed no comparable pattern. These findings suggest that semantic relevance is a promising BOLD-sensitive metric of contextual semantic fit. More broadly, our findings support the view that slow hemodynamic responses during naturalistic speech comprehension may be especially sensitive to contextual semantic integration, whereas local probabilistic prediction error may be more difficult to detect reliably with fMRI. In this sense, semantic relevance extends computational models of language comprehension from prediction alone toward context-sensitive semantic integration.

---


### 98. [Conditional Reliability of Toxicity Signals for Multilingual and Code-Mixed Abuse Detection](https://arxiv.org/abs/2607.15861)

**<font color=#1a73e8>作者：</font>** Indraveni Chebolu, Rohan Singh, Arnab Mallick 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Moderation systems increasingly rely on external toxicity tools, but those tools are unreliable under code-mixing, transliteration, slang, and language mismatch. We study the \emph{conditional reliability} of toxicity priors in Indian multilingual and code-mixed short text: English toxicity, Indic abuse, and rule-based severity cues can be useful evidence, but only in some linguistic and abuse-severity contexts. We propose ToxGate, a trust-fusion head that conditions each auxiliary signal on the encoder representation before adding it to the prediction state. Across three short-text abuse datasets, four transformer encoders, and five seeds per setting, ToxGate improves over matched plain encoders in 10 of 12 in-domain settings and 7 of 8 transfer settings. The largest and most interpretable gains occur in high-risk moderation slices, including explicit slurs, violent threats, and cross-dataset transfer. The broader lesson is that moderation systems should treat external toxicity tools and priors as conditional evidence rather than fixed features or ground truth, in focused ablations, source-specific gating gives the strongest results in transfer, severe-abuse slices, and high-risk triage.

---


### 99. [Breakdowns for Human-Machine Creative Reflexivity](https://arxiv.org/abs/2607.15866)

**<font color=#1a73e8>作者：</font>** Marianne Bossema, Somaya Ben Allouch, Rob Saunders  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) works via goal-directed computation, which differs fundamentally from human creative processes. This poses challenges for the intelligent support of creative experiences. We propose ``breakdowns'' as opportunities for the exchange of perspectives between human and machine. Breakdowns disrupt a flow and force us to consciously evaluate our ``being-in-the-world''. Between human and machine, breakdowns can function as openings for collaborative creative reflection. We are currently studying human-human creative interactions, to identify the markers of these inter-subjective openings, and to understand how they are used in a co-creative process. We present preliminary findings on breakdowns as a design principle for creativity support, prioritising human creative agency and meaningful reflection over automated content generation.

---


### 100. [EgoExoMoCap: Distributed Ego-Exo Human Motion Capture](https://arxiv.org/abs/2607.15868)

**<font color=#1a73e8>作者：</font>** Jiaxi Jiang, Bharat Lal Bhatnagar, Nan Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human motion capture from head-mounted devices (HMDs) offers a scalable way to acquire real-world human motion and interaction data, which is crucial for applications in embodied AI and VR/AR. Existing approaches focus on either egocentric body tracking, estimating the motion of the subject wearing the device, or exocentric tracking, capturing the movements of people in the wearer's surroundings. So far, these two paradigms have largely been explored in isolation. In this paper, we propose a novel distributed framework that jointly leverages ego- and exocentric multi-modal signals for human motion estimation from HMDs. Unlike traditional motion capture systems requiring bulky multi-camera setups or obtrusive mocap suits, our approach, EgoExoMoCap, is as simple as two (or more) people, each wearing a pair of smart glasses. The method leverages head (plus potentially wrist) tracking signals for accurate estimation of global motion in the 3D world and combines context-aware image features based on DINOv3 to achieve robustness in the presence of noise and occlusions. Extensive experiments on two in-the-wild datasets show that our approach can robustly reconstruct motion even in challenging scenarios.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-152](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
