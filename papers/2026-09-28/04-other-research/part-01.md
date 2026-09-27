# 📦 其他研究 | 2026年09月28日

> 本类共 **266** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 1. [Stable and Faithful Explanations for Knowledge Tracing](https://arxiv.org/abs/2609.28502)

**<font color=#1a73e8>作者：</font>** Praveena Padi, Arun Morampudi, Ujval Sai Gopal Irrinki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge tracing (KT) models predict student performance opaquely, limiting pedagogical action. This study contributes a validation protocol testing predictive competitiveness (RQ1), explanation stability (RQ2) and retraining-based faithfulness (RQ3) together. Thirteen behavioral features across five pedagogical themes were engineered from ASSISTments 2009 and 2012, with history features computed from temporally preceding interactions and current response latency retained only for retrospective analysis. ASSISTments 2009 was rebuilt: the uncorrected skill-builder release duplicates each multi-skill interaction across one row per skill, and because those rows share one correctness label, they leak it into preceding-interaction features. Rebuilding lowered model AUC and reordered the explanation results. An Extreme Gradient Boosting (XGBoost) model explained with Tree SHapley Additive exPlanations (TreeSHAP) was compared against four deep baselines (DKT, SAKT, AKT and SimpleKT) under an information-matched protocol giving the deep models the same behavioral signals and restricting XGBoost to what is derivable from the identifier-and-correctness stream they consume. XGBoost reached an area under the curve (AUC) of 0.777 on 2012 and 0.786 on rebuilt 2009, with prediction-time AUCs of 0.771 and 0.775, respectively, after excluding current response latency; restricted to the baselines' information it performed as they did (0.697 against 0.700, and 0.717 against 0.720), locating the difference in information supplied, not model family. Rankings were consistent across folds, seeds and conditioning schemes (Spearman rho = 0.989-1.000), and removing top-ranked TreeSHAP features harmed AUC more than random removal, though split-gain and permutation rankings performed comparably. Student-level examples are illustrative interpretations, not validated recommendations.

---


### 2. [Stress-Testing Structure-Aware Calibration of Malware Graph Neural Networks under Type Shift](https://arxiv.org/abs/2609.28517)

**<font color=#1a73e8>作者：</font>** Junru Zhu, Yixin Yang, Xiaoqing Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-hoc malware calibrators can condition confidence on graph structure, but their structural inputs may leave the support represented by validation data under malware-type shift. We study this risk on MalNet-Tiny by holding out each of four malware types across three seeds, freezing a graph isomorphism network, and fitting post-hoc mappings only on known-type data. Adding eight community covariates to a generic-topology calibrator increases mean negative log likelihood (NLL) by 0.1369; a type-cluster bootstrap gives a 95% interval of [-0.0125, 0.2864]. A capacity-matched control adds eight label-independent nuisance variables over 20 deterministic repeats and increases NLL by only 0.0415, indicating that input count explains part but not all of the degradation. We then use calibration data to define a community-support guard: predictions outside the 95th percentile of calibration-standardized community displacement revert to the generic calibrator. The guard reduces combined NLL by 0.1133 and high-confidence errors from 43.25 to 33.25 per 400-sample cell, while its NLL remains close to the generic baseline. These results show how structural covariates can create support-sensitive confidence errors and how a label-free fallback can recover most of the resulting loss.

---


### 3. [$\unicode{x1F493}$Heartian: Physiology-Aware Relightable Gaussian Head Avatar](https://arxiv.org/abs/2609.28539)

**<font color=#1a73e8>作者：</font>** Xiaoyue Fan, Jose Echevarria, Akshay Paruchuri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian head avatars typically model intrinsic facial appearance as temporally static, omitting subtle cardiac-induced skin-color variation. We propose $\unicode{x1F493}$Heartian, a physiology-aware modulation framework that learns cardiac-cycle-dependent per-frame albedo modulation of facial skin-region Gaussians within a relightable head avatar to encode remote photoplethysmography (rPPG) signals. Using synchronized contact PPG supervision, $\unicode{x1F493}$Heartian models the prescribed cardiac waveform as the sum of two Gaussian functions and learns per-frame spatial residuals via a lightweight MLP. Across 152 stationary recordings from UBFC-rPPG, PURE, and MMPD, attribute-space recovery of the supplied signal achieves a pooled recording-level heart-rate MAE of 0.29 bpm and MAPE of 0.38%. The signals remain detectable after rendering by benchmark rPPG methods, with the best tested configuration - a motion-augmented TS-CAN decoder pretrained on UBFC-rPPG - recovering heart rate from the rendered MMPD avatars at 0.97 bpm MAE and 1.21% MAPE. Meanwhile, $\unicode{x1F493}$Heartian maintains reconstruction quality comparable to the baseline, with negligible average PSNR degradation of 0.005 dB. Overall, our work embeds recoverable rPPG signals as controllable material attributes to subject-specific Gaussian head avatars while retaining the reconstruction quality.

---


### 4. [PAWS: Policy-driven Agentic World Simulation](https://arxiv.org/abs/2609.28547)

**<font color=#1a73e8>作者：</font>** Tiviatis Sim, Jia Hui Woon, Xinming Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Policy interventions propagate through public communication, institutional decisions, and stakeholder responses, yet datasets for financial multi-agent simulation rarely connect these processes to temporally aligned historical evidence. We introduce PAWS, a Policy-driven Agentic World Simulation dataset covering 36 verified U.S. financial and economic policy episodes, 12,727 policy-linked news records, and 65,291 source-grounded stakeholder actions. Each action is linked to its supporting news and represented by a multi-layer event frame capturing its interaction mode, financial-action family and subtype, semantic attributes, and conditional mappings to external taxonomies. Entities are resolved to normalized organizations, and actions are aligned with daily market-return context to support policy-agent simulation replay. On 2,522 stratified action samples, independent AI and human reviewers achieved 89.4% initial agreement on interaction mode, with disagreements subsequently adjudicated. Case studies of the 2008 short-selling ban and 2001 decimalization recover documented policy timelines and associated market patterns across both dense and sparse news settings. A replay study further shows that high accuracy can mask failure to detect rare stakeholder actions, identifying action timing and calibration as central challenges. PAWS provides an auditable substrate for evaluating agent influence, policy-response cascades, and action-outcome alignment in historically grounded financial simulations.

---


### 5. [SMILESGNN: Interpretable Clinical Toxicity Prediction via SMILES-Graph Cross-Attention Fusion](https://arxiv.org/abs/2609.28553)

**<font color=#1a73e8>作者：</font>** Quang Minh Nguyen, Thuy Quynh Nguyen, Duc Minh Le 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug toxicity prediction is critical for reducing late-stage attrition in drug discovery, yet remains challenging due to severe class imbalance, scaffold-based generalization, and the clinical need for interpretable predictions. Single-modality approaches-SMILES Transformers or graph neural networks capture complementary aspects of molecular structure, while sequence-only models cannot directly provide graph-attributed explanations. We present SMILESGNN, a multimodal architecture that fuses a SMILES Transformer encoder and a GATv2 graph encoder via cross-attention, and SMILESGNN-PT, a variant using a ChemBERTa-2 pretrained backbone. The design retains an explicit graph branch within the predictive pipeline, supporting GNNExplainer-based analysis of substructures associated with toxic predictions. On ClinTox, SMILESGNN achieves AUC-ROC 0.987 and F1 0.906 with only 0.4M parameters, performing competitively with a strong SMILESTransformer and a larger ChemBERTa-2/GATv2 concat-fusion baseline. On Tox21 (12 tasks), SMILESGNN-PT obtains mean AUC-ROC 0.750, comparable to ChemBERTa-2 alone and the same-backbone concat-fusion baseline. Overall, the results suggest that cross-attention is a practical fusion alternative that preserves competitive predictive performance while enabling graph-based interpretability support.

---


### 6. [CFD Correction of Open Tip Clearance Flow in a Compressor Cascade Using VAE Latent Space Adaptation](https://arxiv.org/abs/2609.28558)

**<font color=#1a73e8>作者：</font>** Xiang Zuo, Hefang Deng, Caiyan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> CFD predictions of open tip clearance flow in compressor cascades are subject to discrepancies relative to experiments, while experimental observations are sparse and high-resolution experimental ground truth is unavailable. This study proposes a non-intrusive correction method based on a variational autoencoder (VAE) and latent-space adaptation. A VAE is first trained using a dataset of 166 parametrically sampled CFD total pressure loss fields to learn a low-dimensional statistical representation of these fields. The VAE is then frozen, and a low-rank latent-space adapter is trained using only 12 paired CFD--experiment operating conditions. An observation operator maps the corrected high-resolution fields to the experimental observation space, allowing supervision to be applied only at the available measurement locations and within the measured pitchwise windows. In the current 12-fold cross-validation, the mean absolute error decreases from 0.1335 to 0.0473, the root mean square error from 0.1717 to 0.0621, and the relative $L_2$ error from 0.5108 to 0.1871. These results indicate that the method improves agreement between CFD predictions and sparse experimental observations of open tip clearance flow without modifying the RANS solver or constructing artificial high-resolution experimental labels.

---


### 7. [CARE: Condition-Aware Representation Regularization for Diffusion Models](https://arxiv.org/abs/2609.28561)

**<font color=#1a73e8>作者：</font>** Fengjia Guo, Zhuoyi Yang, Jie Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in diffusion models highlight the importance of representation regularization for improving sample quality and training efficiency. However, commonly used regularization methods often overlook the built-in conditions (such as labels or texts) which directly determine the generation target. In this work, we demonstrate how conditioning signals affect the feature distribution and introduce the CARE (Condition-Aware REpresentation regularization). CARE is a lightweight plug-and-play regularization framework that dynamically modulates feature distribution based on condition similarity. CARE leverages built-in conditioning signals to judiciously guide the representation space, promoting tighter feature clusters for similar conditions without relying on explicit alignment losses or external supervision. Empirically, CARE consistently improves both visual fidelity and convergence stability across both class-to-image and text-to-image tasks. On ImageNet, CARE achieves a 19.08\% reduction in FID in 400k training steps, leading to a 3.5$\times$ speed-up. When applied to text-to-image generation, CARE lowers FID by 16.61\% in 200k iterations and improves semantic alignment between generated samples and text prompts. Moreover, CARE can be seamlessly integrated with existing regularization methods, yielding additional performance gains.

---


### 8. [SpaFactor: Lightweight Spatial Context-Aware Gene Program Modeling for Histology-to-Transcriptomics Inference](https://arxiv.org/abs/2609.28563)

**<font color=#1a73e8>作者：</font>** Shiting Ruan, Xitong Ling, Qiming He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) profiles gene expression within tissue architecture, but its cost and experimental complexity limit routine use. Predicting spatial expression from routinely available hematoxylin and eosin (HE) images therefore offers a scalable alternative. However, conventional methods often fit high-dimensional gene outputs as independent targets, overlooking the biological coordination among genes while remaining vulnerable to high-dimensional noise and overfitting. Existing attempts to address this limitation often rely on computationally heavy graph networks or complex auxiliary supervision. We therefore introduce SpaFactor, a lightweight and efficient low-rank morphology-program-gene factorization framework. At the input, SpaFactor efficiently fuses the visual representation of the central spot with multiscale local and regional neighborhood context, yielding a histologic representation that captures cellular morphology and microenvironmental heterogeneity. For modeling, a residual MLP stably learns a nonlinear mapping from the tissue microenvironment to low-dimensional latent gene programs. These activities are decoded through shared gene loadings into coordinated multi-gene expression predictions. Across five public cohorts, SpaFactor achieves the best aggregate performance, with particularly clear improvements for spatially variable genes, and more faithfully recovers biologically organized spatial patterns. These results demonstrate that lightweight joint modeling of tissue context and gene programs can improve both predictive accuracy and biological fidelity.

---


### 9. [When Explanations Cannot Be Read: Measuring and Correcting SHAP and LIME Rendering for Right-to-Left Languages](https://arxiv.org/abs/2609.28565)

**<font color=#1a73e8>作者：</font>** Rameesha Zia, Muhammad Shahid Iqbal Malik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post hoc explanation methods such as SHAP and LIME are widely used to interpret text classifiers, but their visualizations are mainly designed for left-to-right languages. When applied to right-to-left (RTL) languages such as Urdu, Arabic, Persian, and Hebrew, the attribution values remain mathematically valid, while their visual presentation fails. Tokens appear out of sequence, connected letterforms break apart, and plot layouts do not follow the natural reading direction. This study addresses this gap as a visualization problem rather than a limitation of the explanation methods themselves. We present SHAP-RTL, a rendering layer that corrects reading direction and script shaping in SHAP and LIME visualizations, with per-language font selection, while preserving the original attribution values, feature ordering, and model outputs. The approach is evaluated on Urdu, Arabic, Hebrew, and Persian hate and offensive-language datasets using TF-IDF and logistic regression classifiers. Rendering correctness is measured by an OCR round trip over 200 feature words per language. Default rendering yields character error rates of 0.820 to 0.979, meaning the label no longer carries its token; the common reshape-and-reorder workaround fails for Urdu at 0.998, worse than no correction; and the Matplotlib 3.11.0 text rewrite inverts that workaround, while SHAP-RTL remains correct under both versions. The framework also verbalizes the same attributions as short contextual explanations in the reader's language, constrained to the identified features. Evaluation in this paper concerns rendering correctness; assessment of the generated explanations is left to future work. The study highlights the importance of language-aware visualization in making post hoc explainability more accessible across different writing systems.

---


### 10. [Leakage-Safe Machine Learning for Hydrogen Embrittlement Detection in 316L Stainless Steel: A Region-Held-Out Evaluation of Texture and Deep Features in SEM Micrographs](https://arxiv.org/abs/2609.28567)

**<font color=#1a73e8>作者：</font>** Muhammad Awais, Muhammad Yaseen, Abdul Shakoor 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scanning electron microscopy (SEM) is routinely used to characterize the microstructural changes caused by hydrogen embrittlement (HE) in structural steels. Machine learning can automate this characterization, but models are often evaluated using image-level splits. When several images come from the same specimen region, such splits leak information between the training and test sets. Here, we propose a region-held-out protocol for classifying as-received (AR) and hydrogen-charged (H2) SEM micrographs of 316L stainless steel, based on Leave-One-Region-Out (LORO) cross-validation over 14 spatial regions (8 AR, 6 H2; 31 images). We compared six feature-classifier combinations built on local binary patterns (LBP), grey-level co-occurrence matrices (GLCM), self-supervised convolutional embeddings pretrained on 143 unlabeled SEM images, and a convolutional neural network (CNN). The simplest texture approach, LBP with a support vector machine (LBP+SVM), performed best, achieving a balanced accuracy of 0.79, H2 recall of 0.69, and H2 precision of 0.82, outperforming every deep-learning and combined-feature model. A group-level permutation test (500 permutations sampled from the 3,003 possible region-to-label assignments) yielded p = 0.008, indicating that the result cannot be explained by a chance alignment of the region structure. Grad-CAM maps from a CNN trained on the full dataset tended to concentrate on localized surface and grain-boundary features, where hydrogen-induced morphological changes are known to occur. Under a leakage-safe, statistically validated protocol, texture descriptors recover a hydrogen-charging signature from SEM micrographs even with few samples, and the same protocol can be extended to larger HE detection studies in other alloy systems.

---


### 11. [Uncovering Residential PV-EV Co-Adoption from Smart-Meter Data: Load Archetypes and Detection for Demand-Side Planning](https://arxiv.org/abs/2609.28578)

**<font color=#1a73e8>作者：</font>** Jack Zheng, Hao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The increasing adoption of electric vehicles (EVs) and rooftop photovoltaic (PV) systems is reshaping residential electricity demand and creating new challenges for demand-side management (DSM), tariff design, and low-voltage network planning. Much of the existing literature examines EV charging or PV generation in isolation, leaving the behavioral dynamics of household co-adoption less understood. We develop an integrated, two-part workflow to analyze advanced metering infrastructure (AMI) data. A discovery component applies dynamic time warping (DTW) k-means with DTW barycenter averaging to cluster daily import or export profiles into interpretable behavioral archetypes, while a predictive component trains a bidirectional long short-term memory (BiLSTM) model on 21-day windows and benchmarks it against tabular baselines for PV/EV activity detection. The EV activity labels are inferred from charging-like load signatures because charger measurements are unavailable. Using half-hourly AusNet residential data from Victoria, Australia, the clustering uncovers distinct patterns across PV-only, EV-only, co-adoption, and neither cohorts; for co-adopters, a midday-centered weekday export archetype accounts for approximately 50% of days. At validation-tuned thresholds, both BiLSTM and XGBoost achieve strong discrimination. BiLSTM obtains 0.991 for the area under the receiver operating characteristic curve (AUROC), 0.906 for macro-F1, and the highest recall on the most difficult class (0.836 for EV-only recall). Tree-based baselines remain competitive. Performance remains stable across plausible labeling rules (macro-F1: 0.894--0.914) and strictly forward temporal splits (macro-F1: 0.894--0.906).

---


### 12. [Token Clustering and Semantic Sequence Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2609.28580)

**<font color=#1a73e8>作者：</font>** Yimin Zhu, Mahmood Elahi, Lincoln Linlin Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although hyperspectral images (HSIs) provide rich spectral-spatial information, accurate pixel-level classification remains challenging because of spectral-spatial heterogeneity and complex spatial structures. Existing vision state space models (Mamba) typically construct sequences according to predefined spatial neighborhoods, without explicitly accounting for semantic similarity or spatial non-stationarity. To address this limitation, we propose Token Clustering and Semantic Sequence Mamba (STMamba), which organizes sparse tokens into semantically coherent sequences for hyperspectral image classification with the following features. First, at the macro level, a hierarchical encoder decoder progressively selects semantic tokens with the Token Clustering Module (TCM) and restores dense features using a parameter-free Cross-scale Neighborhood Attention (CNA) Upsampler. Second, at the micro level, TCM first identifies representative cluster centers through density-aware clustering and estimates soft memberships based on feature similarity. A quadtree-based dynamic selection strategy then retains sparse and spatially distributed tokens from each semantic cluster, forming coherent semantic-token sequences while reducing redundant pixel-wise representations. Third, parallel Spatial and Spectral Semantic-wise Sequencing Mamba (SWSM) modules capture complementary long-range spatial and spectral dependencies within homogeneous semantic token sequences while suppressing irrelevant interactions across heterogeneous regions. Experimental results on three large-scale benchmark datasets demonstrate that STMamba outperforms the SOTA methods with respect to quantitative and qualitative results.

---


### 13. [Auditability Is Not One Property: Rule Overlap, Behavioural Agreement, and Composition in Reinforcement Learning](https://arxiv.org/abs/2609.28581)

**<font color=#1a73e8>作者：</font>** Liu Hung Ming  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement-learning (RL) policies are often distributed as opaque neural checkpoints, while training logs show that a run occurred without explaining what the policy learned. We study whether independently trained policies can be represented and composed through auditable discrete behavioral rules. We define auditability as six separately testable predicates: trace integrity, lossless coding, rule coverage, behavioral agreement, composition quality, and value-model reliability. Our protocol uses a shared frozen symbolizer, passive rule extraction, an append-only hash-bound ledger, exact environment replay, and offline confidence-ranked arbitration with an explicit blind-spot fallback.
The results place strict limits on this description layer. Rule-set overlap does not imply behavioral agreement: policies may share symbolic rules while choosing near-chance-matching actions on fresh states. The fused policy therefore selects among existing rules rather than generating a new skill. On a conflict-dominated task, an apparent fusion failure is traced to an induction/deployment mismatch: rules induced from sampled actions were evaluated under argmax actions, and deployment-consistent re-induction reverses the arbitration ordering. A fitted-Q generalized-policy-improvement diagnostic also fails in both environments, limiting claims that rule fusion is superior to value-based composition. One exploratory comparison favors rule fusion, but its comparator is post hoc, the task is partly saturated, and the fused policy remains below the strongest held-out actor.
We contribute an evidence-bounded audit and composition protocol, not a claim of universal interpretability or autonomous skill generation. Future work must add temporally extended skills, cross-skill interfaces, composition search, and independent novelty audits.

---


### 14. [TAM-Chain: Multi-Scale Thyroid Cytology Classification via Absorbing Markov Chains and Shannon Entropy Uncertainty Quantification for False-Negative Suppression and Domain-Shift Adaptation](https://arxiv.org/abs/2609.28590)

**<font color=#1a73e8>作者：</font>** Hai Pham Ngoc  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background & Problem: Thyroid Fine-Needle Aspiration Biopsy (FNAB) cytology based on the Bethesda System plays a pivotal role in early thyroid cancer detection; however, deep learning approaches face substantial challenges regarding high false-negative rates and overconfidence under clinical domain shift.
Methods: In this study, we propose TAM-Chain, a multi-scale (10x, 20x, 40x) thyroid cytology classification framework leveraging Absorbing Markov Chain theory combined with Shannon Entropy-based Uncertainty Quantification. The framework dynamically models multi-magnification feature extraction as an absorbing stochastic process, enabling optimal stopping criteria and a human-in-the-loop referral mechanism to strictly suppress critical diagnostic errors.
Results: Extensive evaluation on an internal test set (N = 235) demonstrates a Macro F1 score of 0.9741 with an absolute False-Negative Rate (FNR) of 0.00%. On an independent external validation set (N = 1015) presenting severe domain shift, TAM-Chain maintains superior stability and classification performance (Macro F1 = 0.7026) by adaptively adjusting the expected stopping step and triggering specialist referrals, significantly outperforming single-magnification baselines.
Conclusion: The TAM-Chain framework proves to be a highly effective, safe, and adaptable solution for digital pathology workflows, successfully harmonizing automated diagnostic efficiency with stringent biological safety.

---


### 15. [BRFID: Toward Byzantine-Robust Federated Intrusion Detection](https://arxiv.org/abs/2609.28599)

**<font color=#1a73e8>作者：</font>** Asmah Muallem, Firdous Kausar, Sajid Hussain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Flipping 60\% of training labels from a single Byzantine client using label-flipping model poisoning self-degrades an attacker's own federated detection accuracy, $99.96\%$ (at no poisoning rate) to $84.33\%$ in a three-client federated IDS. Where the Federated global ensemble maintains stable accuracy across all tested poison rates, without a defense mechanism in place and without coordination between attackers. In this paper, we present empirical results quantifying the impact of label-flipping poisoning attacks on a three-client federated IDS trained on CICIDS2017 with non-IID attack subtype distributions across clients. We demonstrate that the signal of the adversarial self-compromise represents a detectable anomaly for exploitation for Byzantine client identification in the absence of target data exfiltration. We note that the aggregation step uses a Federated Forest (tree concatenation) rather than a parametric FedAvg; the results therefore measure the impact of poisoning on per-client performance under ensemble aggregation, and extension to genuine FedAvg with a parametric classifier is planned for future work.

---


### 16. [Physics-Informed Self-Supervised Learning for Joint Wire Calibration and Interaction Position Reconstruction in Multi-Wire Parallel Plate Avalanche Counters](https://arxiv.org/abs/2609.28604)

**<font color=#1a73e8>作者：</font>** Antoine Lemasson, Maurycy Rejmund  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific instruments require accurate calibration to convert detector signals into reliable physical observables. Conventional calibration procedures typically rely on dedicated calibration measurements, analytical response models or labelled reference data, limiting their ability to adapt to changing operating conditions and detector aging.
We present a physics-informed self-supervised learning framework that jointly performs wire calibration and interaction position reconstruction in Multi-Wire Parallel Plate Avalanche Counters (MWPPACs) without requiring labelled position measurements or dedicated calibration runs. The method formulates detector calibration as a latent optimization problem in which global wire gains and event-wise interaction positions are estimated simultaneously using supervision derived exclusively from detector geometry and charge-energy consistency constraints. A detector-independent neural network reconstructs sub-wire interaction positions from local charge distributions, eliminating the need to assume analytical induction profiles by learning the detector response directly from experimental data. The end-to-end differentiable framework enables continuous detector self-calibration while improving the uniformity and accuracy of position reconstruction. Experimental evaluation on the entrance MWPPAC tracking detectors of the VAMOS++ magnetic spectrometer demonstrates stable convergence, improved spatial homogeneity and enhanced position resolution.
Beyond the detector studied, the method establishes a general framework for physics-informed self-supervised calibration of scientific instruments and is a step toward autonomous intelligent instrumentation capable of continuous adaptation during operation. In this paradigm, detector calibration is no longer a prerequisite for an experiment but an integral part of the measurement process itself.

---


### 17. [fable.intermittent: benchmarking probabilistic forecasting methods for intermittent time series](https://arxiv.org/abs/2609.28607)

**<font color=#1a73e8>作者：</font>** Stefano Damato, Lorenzo Zambon, Giorgio Corani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intermittent time series are common in spare-parts demand and retail sales. Since the cost of forecast errors is typically asymmetric, decisions such as inventory control require the full predictive distribution rather than a point forecast. Many probabilistic forecasting methods have been proposed; their implementations, however, are scattered across different software frameworks, making it difficult to compare them systematically. We introduce this http URL, an R package that implements several probabilistic forecasting methods for intermittent series within the fable framework. The package allows several models to be fitted and evaluated on a collection of time series through a single, simple forecasting pipeline. We also introduce TWEES, a new exponential smoothing model with a Tweedie predictive distribution. Fitting TWEES requires repeated evaluation of the computationally demanding Tweedie density. We also release the R package tweedieDistr, whose implementation of the Tweedie distribution is substantially faster than the existing one while preserving the same numerical accuracy. We evaluate the methods implemented in this http URL on four datasets, also released in the package.

---


### 18. [CONCURDEP: Event-Guided Analysis of Dependency Invalidation in CPython Concurrency](https://arxiv.org/abs/2609.28608)

**<font color=#1a73e8>作者：</font>** Baihong Chen, Hadley Westover, Wen Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Removing CPython's Global Interpreter Lock (GIL) exposes native code to concurrency absent from ordinary C types. Mutation or re-entry can revoke a borrowed object, storage pointer, traversal state, or lease between acquisition and use while its owner remains alive, causing native memory errors and runtime-state corruption. Race analyses track conflicting accesses. Python/C lifecycle analyses track individual object states. These reporting units leave implicit owner-subject-storage relations disconnected from later uses under parallel and re-entrant events. We present CONCURDEP, a source-level static analysis of dependency invalidation. Its key insight is to represent the runtime property a native use requires and ask which target-matched event can revoke it within the dependency's live region. CONCURDEP recovers runtime-semantic dependencies, connects them to events through an event-aware native concurrency dependency graph, and applies property-specific state and protection transfers through a shared engine and six mechanism plugins. CONCURDEP correctly classifies all 180 matched semantic-conformance cases and analyzes each of three production CPython releases with five-run medians of 22.13-27.66 seconds and 670-784 MiB peak resident memory. Source auditing confirms 1,094 of 4,273 unique production fingerprints (25.60% confirmation yield). Removing derived relation recovery loses 25-44 represented roots per release; removing cross-entry events loses 73-94. The study identifies 144 distinct bugs across free-threaded and conventional-GIL builds, including 95 previously unreported in public sources. These results show that explicit dependency, event, and property semantics expose consequential runtime failures across API boundaries and execution modes at release scale.

---


### 19. [PePESeg3D: Perception Prior Enhances Multi-Scale Segmentation for 3D Gaussian Splatting](https://arxiv.org/abs/2609.28645)

**<font color=#1a73e8>作者：</font>** Sungjae Choi, Seunghee Koh, Junmo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in 3D Gaussian Splatting (3DGS) have extended its capabilities to multi-scale segmentation. Existing methods reconstruct a scene with Gaussian primitives and learn multi-scale segmentation features separately, which leaves the geometry unaware of semantic structure and the feature learning dependent on incomplete mask supervision. To address these limitations, we present PePESeg3D, a novel framework that injects perception priors into a multi-scale 3D Gaussian segmentation pipeline. To fully exploit perception priors, we integrate them not only into contrastive feature learning but also into the upstream geometry reconstruction. Specifically, PePE Reconstruction incorporates monocular depth and mask constraints to ensure semantically coherent object structures. Building on this aligned geometry, PePE Contrastive Learning leverages dense depth-color cues and view-consistent centroid supervision to compensate for the incompleteness of multi-scale masks obtained from a 2D foundation model. Extensive experiments on the SPIn-NeRF, LERF-Mask, and NVOS benchmarks demonstrate that PePESeg3D achieves state-of-the-art performance in both multi-scale segmentation and scene reconstruction, highlighting the importance of integrating perception priors into both geometry optimization and feature learning for accurate multi-scale 3D segmentation. Our code is available at this https URL.

---


### 20. [Training Object Permanence in World Models](https://arxiv.org/abs/2609.28654)

**<font color=#1a73e8>作者：</font>** Haotian Zhang, Fengyuan Yu, Dezhi Luo 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Object permanence and solidity are hallmarks of human cognitive priors. Recent studies show that video generation models, a paradigmatic class of current world models, have begun to show emerged reasoning abilities, making them ideal candidates for building human-like physical intelligence. Do video models have emerged object permanence in them? If not, could we train them with a core-cognition inspired dataset? We introduce WROP (World Reasoning with Object Permanence), a data infrastructure of 150 hand-designed cognitive science inspired tasks, divided into six cognitive categories. We build Blender generators that randomize speed, lighting, camera angle, and other nuisance parameters while preserving each task's cognitive structure, yielding 10,000+ samples per task. We release a 1.5M-sample training corpus and a 300-question exam. On this exam we evaluate 14 video models: 3 reference-to-video, 7 edit, and 4 continuation, among which PWM-WROP, our 16B world model. In a blind pairwise Elo study, PWM-WROP ranks first among continuation models and third overall, behind only a statistical tie between two reference-to-video models. We release the data, exam, model answers, scores, weights, and PWM, our native-PyTorch training stack on AWS Trainium2.

---


### 21. ["What I See is What I Hear": Deepfake Detection Across Diverse Hearing Abilities](https://arxiv.org/abs/2609.28659)

**<font color=#1a73e8>作者：</font>** Magdalena Pasternak, Malvika Jadhav, Palavi V. Bhole 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The proliferation of audiovisual deepfakes has lowered the cost of fraud, impersonation, and misinformation, but their success ultimately depends on human perception. Detection requires integrating auditory and visual cues, yet security and privacy research has largely overlooked d/Deaf and hard-of-hearing (DHH) populations. We address this gap with an in-person, mixed-methods study of 80 participants: 31 hearing persons (HPs), 15 hard-of-hearing (HoH) participants, 17 d/Deaf participants, and 17 cochlear implant (CI) users. Each participant judged the authenticity of 30 clips, where manipulations spanned text-to-speech, voice conversion, lip-sync, or face-swap. DHH participants were less accurate than HPs overall (76.4% vs. 88.0%, p<.001), primarily because they more often classified authentic clips as manipulated (FPR: 29.7% vs. 11.2%). Differences depended strongly on the manipulated channel. For audio-only manipulations, HoH participants matched HPs (90.0% vs. 90.3%), followed by CI users (79.4%) and d/Deaf participants (41.2%). When clips contained an audiovisual manipulation, accuracy clustered between 84% and 87%, although performance still varied by manipulation method. Our work systematically characterizes how deepfakes affect DHH populations, highlighting the asymmetric risks audiovisual manipulations may pose to groups with different hearing abilities and the need for accessible, tailored defenses that support all users.

---


### 22. [OPDiv: Optimal Selection of Top-K High-Scoring, Diverse Compounds](https://arxiv.org/abs/2609.28665)

**<font color=#1a73e8>作者：</font>** Miroslav Lžičař  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A virtual screening campaign may produce thousands of promising candidates, but only a small number can be purchased, synthesized, or tested. The practical question is how to select a set of compounds that both rank well and are diverse enough: this poses a genuine tradeoff, where selecting the highest-scoring molecules yields limited diversity, while diversity selection sacrifices some well-scoring molecules. We introduce OPDiv, a diversity selection and evaluation algorithm solving this tradeoff by finding an optimal subset of molecules using integer optimization. We demonstrate the selection algorithm in practice with fingerprint distance, shape and electrostatic diversity and compare the resulting diversity spectra. We argue that virtual screening is not merely a ranking problem, but also an implicit constrained optimization task: when redundant chemotypes are undesirable, pipelines should be compared based on the top-k compound selections satisfying the desired diversity constraints. OPDiv makes it possible to find the optimal compound set under a given diversity threshold efficiently and serves as a fair benchmark of the best diverse selection achievable by a given structure-based or ligand-based virtual screening pipeline, molecular search or generative model.

---


### 23. [Beyond Static Graph World Models: Learning Stochastic Latent Dynamics over Evolving Topologies](https://arxiv.org/abs/2609.28670)

**<font color=#1a73e8>作者：</font>** Alex Schutz, Nick Hawes, Victor-Alexandru Darvariu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-based world models have recently emerged as a means of learning transitions over relational state representations. However, existing approaches are largely limited to fixed-topology graphs or deterministic, fully observable environments. We propose the Graph Dynamics Model (GDM), a world model for graph-structured observations that is designed to handle the more general setting of evolving topologies in stochastic and partially observable environments. The GDM uses a sparse recurrent adjacency matrix to model topology updates and perform message passing, together with a recurrent state-space architecture for modelling stochastic transitions. Furthermore, we identify a gap in the evaluation of graph-based world models, as existing methods do not provide a means of comparing predicted and true distributions over the joint graph state comprising the interdependent topology, node features, and graph features. We therefore introduce the Graph Distribution Distance (GDD) metric, which uses maximum mean discrepancy with a graph kernel to comprehensively compare joint next-state distributions. We evaluate the GDM across several environments, including stochastic and partially observable settings. We demonstrate that GDM outperforms baseline models and displays zero-shot generalisation on large graphs.

---


### 24. [Available but Not Usable: Dark Patterns and Interaction Cost in Social Media Privacy and Safety Settings for Teens](https://arxiv.org/abs/2609.28672)

**<font color=#1a73e8>作者：</font>** Jingxin Dong, Lingyun Chen, Chen Ling 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social media platforms are central to teenagers' lives, and their designs can expose users to privacy, safety, and wellbeing harms. Platforms increasingly offer protective settings, though the presence of a control reveals little about whether teenagers can find, use, and benefit from it over time. We paired an expert evaluation of six privacy and safety tasks across TikTok, Instagram, Snapchat, and YouTube with moderated think aloud sessions in which 11 teenagers aged 14 to 17 attempted the tasks. Interaction cost and dark patterns analysis allowed us to compare the complexity designed into each task with the effort participants incurred as they located, configured, and interpreted controls. Recurring dark patterns appeared across tasks, and most participant attempts exceeded the expert baseline. Protective settings therefore risk being insufficiently usable or durable in practice, and we propose a wayfinding audit that integrates expert evaluation, usability testing, interaction cost, and dark pattern analysis.

---


### 25. [M-plicits: Neural Implicit Surfaces via Nested Multiscale Residuals](https://arxiv.org/abs/2609.28684)

**<font color=#1a73e8>作者：</font>** Vinícius da Silva, Isabelle Melo, Matheus Bessa 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Encoding input coordinates with sinusoidal functions into multi-layer perceptrons (MLPs) has proven effective for implicit neural representations (INRs) of surfaces defined as zero-level sets. However, existing methods often struggle to balance training efficiency, rendering speed, and noise robustness: single-MLP approaches are expensive at inference, grid-based representations are fast but can limit surface smoothness and overfit input noise, and previous multiscale approaches frequently capture noise and produce artifacts due to hard spectral truncation. To address these limitations, we propose M-plicits, a multiscale framework that models surfaces as a residual sum of MLPs trained via a sequence of nested neighborhoods. Unlike existing residual approaches that rely on standard domain-wide sampling and require costly mesh extraction for visualization, our method strictly localizes supervision to narrow bands around the previous zero-level sets. This nested design naturally provides robustness against noisy input data: the coarse network acts as a low-pass filter that establishes a clean geometric prior, while subsequent residuals progressively refine the geometry without fitting to high-frequency artifacts. We further introduce a multiscale sphere-tracing algorithm and a GEMM-based analytical normal computation that bypasses auto-differentiation entirely, yielding high-fidelity real-time rendering. On Stanford and Thingi32, M-plicits achieves the best mean Chamfer distance in the coarse configuration and the best median Chamfer distance and IoU in the fine configuration, with substantially better noise robustness than iNGP, BACON, and IDF, while using an order of magnitude fewer parameters than grid-based baselines. Code, models, and data will be released at this https URL.

---


### 26. ["A Necessary Evil": Teenagers' Sensemaking of Privacy and Safety Settings on Social Media](https://arxiv.org/abs/2609.28685)

**<font color=#1a73e8>作者：</font>** Jingxin Dong, Lingyun Chen, Chen Ling 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social media platforms are embedded in teenagers' daily lives, supporting friendship and identity while exposing teenagers to unwanted contact and privacy harms. Previous scholarship has documented how attention capture strategies and dark patterns shape social media use, and we extend this work to better understand platform settings that ostensibly provide privacy and safety protection. We report on think-aloud sessions with 11 teenagers aged 14 to 17 who completed six privacy and safety tasks on Instagram, TikTok, Snapchat, and YouTube. We show how participants worked out what a setting meant through their routines, boundaries, and prior experiences, how they accommodated protections softer and less predictable than expected, and how they treated the platform as the authority on what protection should look like. We argue that feature-by-feature evaluation cannot establish whether teenagers are protected, and that platforms should carry the obligation to show that a protective action took effect and is durable.

---


### 27. [Federated Learning of AnDE Classifiers](https://arxiv.org/abs/2609.28695)

**<font color=#1a73e8>作者：</font>** Pablo Torrijos, Juan C. Alfaro, José A. Gámez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work presents a federated framework for training Averaged $n$-Dependence Estimators (AnDE) in distributed environments. The proposed method focuses on the discriminative setting, where model weights are learned locally and aggregated globally, supporting any dependency order $n$. This design allows federated training without transmitting semantically meaningful parameters, improving privacy. Additionally, generative AnDE models are federated to provide a comparative baseline, with optional differential privacy applied to the aggregation of probability tables. Experiments on 12 discrete datasets show that discriminative models with $n \geq 1$ consistently outperform federated Naive Bayes (NB, $n=0$), and that privacy-preserving aggregation is effective with limited accuracy loss. These results establish federated AnDE as a viable and privacy-preserving framework, showing that probabilistic models remain applicable in modern federated learning settings.

---


### 28. [zkSAS: Practical Zero-Knowledge Proofs for Verifiable Spectrum Access Management](https://arxiv.org/abs/2609.28699)

**<font color=#1a73e8>作者：</font>** Nishat F. Purbasha, Ifteher Alom, Eric W. Burger 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Dynamic Spectrum Access (DSA) through the Spectrum Access Systems (SAS) elevates spectral efficiency, yet existing centralized models face allocation logic opaqueness and a lack of independent verifiability. While blockchain-based SAS architectures offer transparency and verifiability by default, they introduce critical privacy risks and prohibitive on-chain computational overhead. We introduce zkSAS, a practical zero-knowledge proof (ZKP) system designed to address the verifiability and privacy gaps in SAS deployments, with direct applicability to both the existing CBRS SAS model and blockchain-based SAS models. The system features a suite of ZKP circuits, encompassing proofs of allocation constraint validity and proofs of move list validity to verify that channel assignments and move list-based incumbent protection measures, respectively, adhere to regulatory constraints without exposing sensitive user data. Comprehensive evaluation of our prototype in both centralized and blockchain-based settings indicates that while proof generation scales with spectrum user population, verification remains lightweight and constant-time. We envision that zkSAS offers a scalable and practical path to secure, verifiable dynamic spectrum sharing.

---


### 29. [An Explainable DistilBERT-BiLSTM-Attention Framework for Binary and Multi-Class Hate Speech Detection](https://arxiv.org/abs/2609.28703)

**<font color=#1a73e8>作者：</font>** Rameesha Zia, Muhammad Shahid Iqbal Malik  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hate speech on social media poses serious risks to social harmony, mental well-being, and public safety, making its timely and accurate detection essential for content moderation systems. Most existing studies focus on binary classification, evaluated their frameworks on a single dataset, and provide limited insight into how decisions are made, which limits their real-world applicability. In addition, limited work is done on the explainability of their predictive inference. To address these challenges, this study proposes a multilevel and explainable hate speech detection framework. The proposed model integrates DistilBERT (Distilled Bidirectional Encoder Representations from Transformers) embeddings with a Bi-LSTM (Bidirectional Long Short-Term Memory) model, and an attention mechanism to capture both contextual meaning and sequential dependencies in text. To enhance trust and transparency, LIME (Local Interpretable Model-agnostic Explanations) is employed to explain model predictions by highlighting influential textual features. The framework is evaluated on two benchmark datasets using both binary and multi-class classification to examine robustness and generalization. In addition, an ablation study is presented to highlight the significance of various components of proposed framework. For binary classification, the proposed model achieves F1-scores of 96.78% on the Davidson dataset and 99.53% on the SMHS dataset. In the multi-class setting, it attains F1-scores of 97.00% and 94.99% on the Davidson and SMHS datasets, respectively, outperforming existing baseline approaches. The results demonstrate that multilevel evaluation improves the reliability that the proposed framework effectively balances performance and efficiency. This makes the framework suitable for practical hate speech moderation systems that require accurate, generalizable, and explainable decisions.

---


### 30. [Understanding Creative Design Practices among Data Artists](https://arxiv.org/abs/2609.28715)

**<font color=#1a73e8>作者：</font>** Tianwei Ma, Anna Offenwanger, Naimul Hoque  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Creative and artistic data visualizations communicate stories and invite engagement, yet how designers develop their expressive forms remains poorly understood. We investigate the design process of data artists through three complementary studies: an analysis of 40 public project accounts, artifact-anchored interviews with seven experienced data artists, and a design task-based study with eight data artists. We find that stories and visual forms develop together through data exploration, reference adaptation, sketching, and prototyping. Inspiration comes from data, existing work, everyday imagery, and personal experience. Sketches help develop mappings, while prototypes with real data can reshape representations and intended stories. Designers consider multiple possibilities but typically develop one direction at a time, partly because producing alternatives is costly. Their choices balance meaning, visual appeal, readability, and feasibility. These findings inform tools connecting stories, references, and real data, including AI assistance that supports testing and revising alternatives while preserving designers' creative judgment.

---


### 31. [Assembling, Breaking, and Refusing the Mask: Agency in AI-Mediated Self-Presentation in Livestreaming](https://arxiv.org/abs/2609.28721)

**<font color=#1a73e8>作者：</font>** Yang Hong, Nusrat Jahan Mim, Sharifa Sultana  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Our mixed-method study examines how Chinese women livestreamers use masking to construct idealized mediated personas while navigating gendered, commercial, organizational, and platform pressures alongside personal agendas. We built on the concept of masking, analyzed 627 recruitment posts, and conducted livestream observations and interviews with 26 Chinese women streamers. We found that streamers assembled masks across bodies, AI-mediated technologies, spaces, performances, and social relations to become recognizable while protecting personal boundaries. These masks were continually negotiated, and participants sometimes broke, resisted, or refused them when demands became misaligned or unsustainable. We conceptualize masking as a sociotechnical assemblage in which agency lies in preserving, disrupting, and reconfiguring relations rather than controlling a single interface. We further theorize breaking as a consequential part of masking that exposes hidden labor and unequal costs of visibility. We offer theoretical and design directions for more negotiable, contestable, and agency-supporting AI-mediated self- presentation.

---


### 32. [Upholding Robustness in Federated Learning: Trends, Emerging Strategies, and Research Opportunities](https://arxiv.org/abs/2609.28722)

**<font color=#1a73e8>作者：</font>** Pravija Raj P V, Ashish Gupta, Andrea Augello 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Federated Learning (FL) has been widely adopted for protecting user privacy in machine learning, it remains vulnerable to various robustness challenges, including performance-impairment risks, information-stealing threats, and aggregation vulnerabilities. This work offers a holistic synthesis of FL robustness along three tightly coupled angles: (i) a threat-centric view of robustness that categorizes the multifaceted attack surfaces, (ii) a structured taxonomy of robust aggregation strategies distinguishing outcome-centric approaches from security-centric strategies, and (iii) a layered taxonomy of defensive strategies. We rigorously examine current evaluation practices for FL robustness and identify major applications and open research challenges to guide future research.

---


### 33. [Unmasking Shortcut Learning in IoT Intrusion Detection: A Forensic, Multi-Paradigm Evaluation of Feature Dependence and Data Leakage](https://arxiv.org/abs/2609.28725)

**<font color=#1a73e8>作者：</font>** Uday Shankar Roy, Mahbuba Jahan Minu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning-based Network Intrusion Detection Systems often report near-perfect performance on IoT benchmarks. However, whether these models learn generalizable attack behavior or exploit spurious dataset shortcuts- such as static testbed IP/MAC addresses and chronological recording artifacts-remains an important question. We evaluate the CyberFlowIoT-GICAP benchmark, containing 3,617,388 flow records across 126 PCAP sessions with 849,395 benign flows. Four learning paradigms are evaluated across four feature configurations using PCAP-disjoint splits; LightGBM is additionally evaluated using conventional random-flow splitting. When only statistical flow behavior is used (Fbehav), LightGBM (92.58% +/- 8.18%), Random Forest (92.59% +/- 8.18%), and Deep MLP (92.55% +/- 8.18%) achieve nearly identical Macro-F1, indicating that performance is constrained by feature representation rather than model complexity. With raw timestamps (Ftstamp), tree-based models reach 99.28% Macro-F1, while the linear model remains at 90.62%, showing that nonlinear models can exploit dataset-specific temporal structure. Attack detectability is highly asymmetric: high-rate and active attacks maintain >99.8% recall from flow behavior alone in nonlinear models, whereas the DNS Beaconing drops from 27.78% to 0.00% recall when contextual features are removed. Conventional random-flow splitting increases attack recall by up to 14.00%, highlighting the effect of placing flows from the same sessions in both training and test sets. We conclude with a 4-point protocol checklist for realistic IoT NIDS evaluation.

---


### 34. [Policy Complexity, Reaction Time, and Bounded Rationality in Reinforcement Learning](https://arxiv.org/abs/2609.28737)

**<font color=#1a73e8>作者：</font>** James Wu, Chris R. Sims  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biological agents do not learn under conditions of unlimited computation. For humans, learning and choice are shaped by constraints on perception, attention, and working memory, which limit how much state information guides behavior and therefore bound policy complexity. Standard reinforcement learning models typically optimize reward without explicitly representing these internal costs, making them less suitable as models of biological intelligence. We derive MI-SARSA, an on-policy temporal-difference algorithm that incorporates mutual-information regularization through a learned marginal action prior and a penalty on state-specific deviations from that prior. This yields a sequential learning model in which state information is used selectively when its expected return benefit justifies the added informational cost. Critically, the same state-specific information cost that governs policy compression also generates trial-level predictions for reaction time, distinguishing MI-SARSA from most reinforcement learning models, which predict choices or returns but not latency. Empirically, MI-SARSA produces a reward-complexity tradeoff, and stronger information penalties produce simpler policies with lower control costs and faster reaction times. Under environment shift, increasing regularization reduces post-switch performance degradation but also lowers asymptotic return, revealing a robustness-capacity tradeoff. Together, these results position MI-SARSA as a model of bounded sequential learning under cognitive constraints.

---


### 35. [Temporal Taxation Compounds Under Post-Training Compression of Whisper Models](https://arxiv.org/abs/2609.28739)

**<font color=#1a73e8>作者：</font>** Srishti Ginjala, Eric Fosler-Lussier, Christopher W. Myers 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition models are audited for demographic fairness at full precision, yet the models that ship to production have been quantized, pruned, and distilled. We ask whether post-training weight compression, which alters model weights rather than the audio signal or its feature representation, redistributes error burden across demographic groups. Across the Whisper family on Fair-Speech, Common Voice 25, and AfriSpeech-200, 50% Wanda pruning of Whisper-large-v3 sharply widens the Black/AA-vs-Asian temporal-taxation differential on Fair-Speech: the absolute word-error-rate gap between the worst- and best-served groups more than doubles; at an assumed cost of five seconds of correction effort per transcription error this is a rise from 30 to 64 seconds of correction time per minute of speech. This +111% relative increase is invariant to the assumed per-error cost, survives an audio-quality control, and is only partly mitigated by beam-search decoding, which still leaves an +86% increase. At edge model size, INT4 HQQ quantization compounds catastrophic transcript loops on West African accents by factors of five to seven. Distillation, by contrast, narrows demographic gaps in 21 of 27 evaluated settings (teacher-student pair, precision, and dataset), with the exceptions concentrated on a single model pair. We cast the temporal-taxation construct of Choi and Choi (2025) as a quantitative metric, and show that single-snapshot fairness audits on full-precision models do not capture the deployment-time burden that compression places on already-marginalized speakers.

---


### 36. [Evaluating Cross-region Generalization for Wavelet-Diffusion Precipitation Downscaling](https://arxiv.org/abs/2609.28749)

**<font color=#1a73e8>作者：</font>** Weikang Qian, Yixin Wen, Chugang Yi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have shown strong potential for kilometer-scale precipitation downscaling, but their performance in geographically unseen regions and event regimes remains insufficiently understood. Building on the wavelet diffusion model (WDM) framework, this study evaluates cross-region and cross-event generalization. Six 3 x 3 deg U.S. regions represent convective, winter, tropical, and atmospheric-river precipitation regimes. Low-resolution inputs are generated by block averaging NOAA Multi-Radar/Multi-Sensor (MRMS) composite reflectivity fields. A WDM trained only on Oklahoma (OK) samples and a WDM trained on all six regions are compared with nearest-neighbor and Bicubic interpolation. Model performance is evaluated using three metric families that measure image-domain reconstruction, spectral and distributional fidelity, and bin-wise precipitation detection. The OK-trained WDM remains competitive outside OK. Although the all-region WDM delivers the best and most consistent overall image-domain and detection performance, its gains are uneven across precipitation intensities. Bin-wise critical success index (CSI) over 5-dBZ reflectivity bins shows that WDM improvements concentrate in localized higher-reflectivity structures, which image-domain metrics partly obscure. In addition, the performance differences among samples are strongly associated with the spatial organization of the precipitation field, quantified by Moran's I as the spatial autocorrelation of each reflectivity bin. The sample-level Moran's I-CSI correlation stratified by sample intensity reaches 0.901 in all six regions, including regions unseen during training. Overall, these findings support future efforts to transfer downscaling models to regions with limited local training data and to generate globally consistent, high-resolution precipitation products.

---


### 37. [Learned Cross-Task Relationships in Multi-Task Models](https://arxiv.org/abs/2609.28776)

**<font color=#1a73e8>作者：</font>** Victor Zhang, Yiping Yuan, Florian Raudies 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a framework that learns cross-task relationships in multi-task models by approximating the joint distribution of task labels through targeted pairwise relationships. This approach improves performance via transfer learning and enhances information extraction without the intractable complexity of modeling the full joint space. Although our framework applies to any multi-task system, we demonstrate its efficacy within YouTube's production recommendation systems. Experiments across the Notifications, Homepage, and Watch Next surfaces show improvements in both accuracy and user satisfaction metrics. Finally, we propose a workflow template to facilitate broader future implementation.

---


### 38. [Data Patching](https://arxiv.org/abs/2609.28777)

**<font color=#1a73e8>作者：</font>** ATM Mizanur Rahman, Syed Ishtiaque Ahmed, Sharifa Sultana  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> To provide data-driven quality services to their citizens, every institution determines the acceptability of the citizen data and datafied mechanisms through institutional protocols, including preset standards and policies. However, data meeting standards at one institution might fail to meet a different institution's standards in subsequent phases of the intended citizen services due to mismatched protocols, leading to data devaluation in the citizen service ecosystem. Terming this phenomenon cross-institutional data devaluation, we investigate its causes and workarounds through interviews with 41 Bangladeshi participants. We found that traditional data auditing mechanisms cannot solely address data devaluation; hence, we draw on our findings and theory of cross-institutional AI audits to propose the Citizen-centered Cross-institutional Data Audit (CCDA). We also discuss design and policy implications of CCDA in HCI and datafied citizen services.

---


### 39. [The Mechanics of Delta Learning: Target Design for Generalizable Scientific Machine Learning](https://arxiv.org/abs/2609.28782)

**<font color=#1a73e8>作者：</font>** Kareem M. Gameel, Ihor Neporozhnii, Sjoerd Hoogland 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In scientific machine learning, $\Delta$-learning trains models on residual errors relative to physical baselines, assuming that more accurate baselines with smaller residual scales inherently improve downstream performance. Here, we demonstrate that residual scale alone is an insufficient heuristic for learnability. Evaluating molecular graph neural networks on total energy targets, we show that complex local descriptor baselines can yield small residual targets that are disproportionately rough within architecture-informed proxy spaces and harder to learn relative to their scale. Conversely, semi-empirical baseline reduces both scale and normalized roughness, improving in-domain and out-of-domain prediction. We introduce scale-normalized graph Dirichlet roughness ($D_{\text{IQR}}$) as a pre-training diagnostic for residual learnability and establish baseline complementarity as a core target-design principle, elevating target space formulation alongside model architecture as a key axis for scientific machine learning.

---


### 40. [Vector Bellman Theory for Multichain Robust Average-Reward Markov Decision Processes](https://arxiv.org/abs/2609.28792)

**<font color=#1a73e8>作者：</font>** Yue Wang, George Atia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robust average-reward Markov decision processes provide a fundamental framework for long-term performance optimization under uncertainty, and can have optimal long-run rewards that depend on the initial state. This state dependence requires a vector Bellman theory that accounts for both recurrent-class rewards and transition uncertainty. We develop such a theory for finite models with compact, post-action $(s,a)$-rectangular ambiguity. A gain-first, bias-second optimization principle yields a coupled vector gain-bias system, and every finite solution identifies the optimal robust gain and supplies stationary saddle strategies against history-dependent opponents, simultaneously from all initial states. We further characterize solvability through stationary gain conditions and a uniform bound on canonical transient corrections, and give sufficient conditions that permit distinct recurrent-class gains. The certificates also yield asymptotically affine trajectories of the robust Bellman operator, based on which we design a robust approximately shifted Halpern planning algorithm. Under finite Bellman solvability, the gain estimates and Bellman displacements converge to the optimal gain vector, and every extracted greedy controller is average-optimal after a finite, instance-dependent budget. These results thus connect finite Bellman certificates to undiscounted planning for state-dependent robust average rewards, providing theoretical understandings.

---


### 41. [Monitoring Urban Traffic Dynamics at Fine Spatiotemporal Resolution Using Distributed Acoustic Sensing and Deep Learning](https://arxiv.org/abs/2609.28793)

**<font color=#1a73e8>作者：</font>** Hao Tian, Heng Cai, Xiaowei Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mapping the distribution of traffic dynamics at high spatiotemporal resolution is a fundamental question in transportation research. Distributed acoustic sensing (DAS), an innovative seismic observation tool, emerges as a promising solution for real-time urban traffic monitoring at high spatial and temporal scales. Distributed acoustic sensing repurposes existing underground fiber-optic cables as dense, continuous sensor arrays, enabling passive and privacy-preserving monitoring of roadway traffic activity at meter-level spatial and second-level temporal resolution. This study examines whether integrating DAS and deep learning models can serve as a continuous and efficient urban traffic observatory for revealing urban traffic dynamics (i.e. traffic volume and congestion, event-driven changes) at high spatiotemporal resolution. Using a DAS deployment along a roadway network in the City of College Station, Texas, USA, this study develops a deep learning-empowered analytical framework that converts raw ground vibration waveforms into spatiotemporal representations, detects vehicle trajectory, and infers traffic states from aggregated traffic volume and speed. A hybrid training strategy combining synthetic and manually annotated DAS images is used to improve vehicle detection under noisy and congested conditions, with model outputs further aggregated to characterize system-level traffic dynamics.

---


### 42. [The Interface Is Downstream: Designing the Terms of Human-Agent Collaboration](https://arxiv.org/abs/2609.28801)

**<font color=#1a73e8>作者：</font>** Hector Ouilhet Olmos  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Before an agent responds or acts, much of the experience has already been designed. Memory and retrieval shape what it notices. Evidence rules shape what it may claim. Permissions shape what it can do. Learning rules shape what it carries into the next encounter.
The argument comes from Alicia, a personal agent I've built and used since January 2026. A fine-tuning pilot produced no defensible model-performance result. It exposed a provenance failure: Alicia repeated an interpretation from a retrieved synthesis, cited a source note credited by that synthesis, and left the synthesis out of the visible chain.
In a model-blind review of thirty-three citations, one reviewer judged that the retrieved intermediary supplied the claim in sixteen relayed citations and part of it in four. Five of twelve citations to directly retrieved targets lacked support in the target excerpt supplied for review. These judgments remain unadjudicated, and the packet is not public.
I call the shared setting a humorphic environment: a persistent computational setting that translates a human practice into software. The first Humorphism paper translated partnership. This paper translates the studio, the room where practice happens. The failure prompted an audit of attention, evidence, action, and learning, with a review artifact and available recourse for each. The test is whether the person can inspect and contest what shaped the teammate's behavior. The output is downstream. Correction, consent, and learning carry the collaborative interface back upstream.

---


### 43. [DeltaWAM: Delta World Action Models for Bimanual Manipulation](https://arxiv.org/abs/2609.28811)

**<font color=#1a73e8>作者：</font>** Han Yan, Zishang Xiang, Haokai Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-action models (WAMs) transfer visual and motion priors from pretrained video generators to robot control by jointly modeling visual dynamics and actions. Existing WAMs, however, predict dense future frames during training, repeatedly modeling largely unchanged content and coupling action-conditioned dynamics to nuisance appearance variations. At inference, processing each complete observation with the heavy video expert bottlenecks few-step action generation. Accordingly, we propose DeltaWAM, which jointly predicts visual deltas and actions using dense-anchor, sparse-delta, and action streams, with three architectures that differ in representation and computation sharing. We further develop Streaming Delta Memory (SDM), which updates cached anchor context with compact observed deltas, reducing heavy video-expert processing. On RoboTwin, DeltaWAM with SDM improves average success over Fast-WAM from 81.3% to 85.4% in the clean setting and from 75.8% to 83.9% under visual randomization. The three architectures reduce training FLOPs by 17.78-23.77%, while SDM reduces one-step inference latency and FLOPs by 36.57% and 31.55%, respectively; real-world evaluations further show the highest overall success rate and normalized progress among the evaluated policies. Code: this https URL. Website: this https URL.

---


### 44. [When Does Unsupervised Learning Succeed or Fail? A PoS Perspective on Reconstruction-Based Anomaly Detection](https://arxiv.org/abs/2609.28832)

**<font color=#1a73e8>作者：</font>** Mehmet Yamaç, Yagmur Mustu, Muhammad Numan Yousaf 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstruction-based unsupervised learning can fail in two opposing ways: a model may reconstruct anomalies too accurately or discard valid nominal variation. Using the Pursuit of Subspaces hypothesis, we characterize these failures through the meet, union, and join geometries induced by the nominal components. Excess learned range produces join blindness, while insufficient capacity produces meet preference and loss of nominal fidelity. We show that the compact nominal union is optimal among nominal faithful ranges and generally requires a nonlinear reconstruction map. Based on this geometry, we introduce Dynamic Push and Pull, which learns from controlled perturbations without anomaly labels, and nested manifold carving, which applies the same principle recursively in latent space. Experiments confirm the predicted changes in latent geometry across every tested Push and Pull configuration. The proposed methods improve reconstruction-based anomaly detection across standard benchmarks and unseen image degradations, while also improving pretrained ECG representations for downstream classification. These results connect reconstruction failures to identifiable geometric conditions and provide practical mechanisms for learning compact representations.

---


### 45. ["You Can't Just Automate It": Negotiating and Sustaining a "Good" Family Life Through Energy Practices](https://arxiv.org/abs/2609.28858)

**<font color=#1a73e8>作者：</font>** Yang Hong, Ying-Yu Chen, Wei-Chien Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study examines how Taiwanese parent-child families negotiate a "good" family life through everyday energy use and imagine future smart homes that support it. We conducted in-home interviews and co-design sessions with 21 families, including 46 parents and children. We found that families pursued a good life through energy practices shaped by thrift, comfort, care, safety, and enjoyment. These arrangements were continually adapted and responded to changing bodies, schedules, people, and infrastructures. This adaptive work was unevenly distributed, which in turn shaped different smart-home imaginaries. Drawing on the lens of Nearby and adversarial design, we conceptualize adaptation as situated sociotechnical work through which families continually rework energy arrangements. We further distinguish collective goods from plural and contestable goods to show why family IoT must support shared values while preserving opportunities to question and revise household arrangements. We offer theoretical and design directions for more adaptive, participatory, and contestable family IoT.

---


### 46. [Multimodal Routing and Region Refinement for Language-Guided Medical Image Segmentation](https://arxiv.org/abs/2609.28860)

**<font color=#1a73e8>作者：</font>** Md Maklachur Rahman, Md Hasan Al Banna, Saraf Anjum 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Textual descriptions can reduce ambiguity in medical image segmentation by specifying the finding and location to be delineated. Existing text-guided methods mainly improve where image and language features interact but generally retain a single learned update pathway across all image-text pairs. We propose MRSeg, a parameter-efficient framework that uses each image-text pair to route the adaptation of visual and textual features before dense prediction. Frozen ConvNeXt-Tiny and PubMedBERT encoders provide multiscale visual features and clinical text tokens. A joint router uses the deepest visual feature and pooled text to predict a sparse mixture over low-rank adapter bases. The resulting route is shared across separate adapter banks for two visual scales and text, coordinating their adaptation while keeping the feature-specific parameters separate. Region Bridge uses text-derived queries to aggregate dense visual tokens into latent regions, refines these regions through self-attention and text cross-attention, and redistributes the refined information back to the feature maps. Finally, a multiscale decoder combines refined semantic features with shallow image evidence. On QaTa-COV19 and MosMedData+, MRSeg achieves 90.90/83.32 and 81.53/68.82 Dice/mIoU, respectively, with 7.11M trainable parameters and 7.60 GFLOPs. Code: this https URL.

---


### 47. [Image Fidelity is Not Field Fidelity: Joint Thermodynamic Reconstruction and Error Localization in Neural Tomography](https://arxiv.org/abs/2609.28868)

**<font color=#1a73e8>作者：</font>** Alan Hsu, Jenna Samra, Alin Razvan Paraschiv 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural fields for scientific tomography are optimized from 2D images, but the actual quantity of interest is often a latent 3D physical field. Because the forward map is many-to-one, low 2D image error need not certify a correct 3D field. Moreover, the latent field is not directly supervised during training, and its error cannot be evaluated against truth at deployment. We develop CoroNeRF to jointly optimize 3D electron density and temperature fields directly from multiview, multiline intensities through a differentiable atomic-emission renderer. Using solar coronal tomography as a controlled testbed, we evaluate physical-field recovery and test whether cross-seed instability provides a ground-truth-free-at-inference indicator of local physical-field error. We underscore the following two observations. (i) Image fidelity is not field fidelity: spectral ablations show that limited-channel reconstructions can fit their available observations well while recovering substantially worse fields, whereas evaluation on a common richer probe exposes the discrepancy. (ii) Cross-seed instability ranks local physical-field error across tested matched-model conditions, supported by sparsification and physical signal-strength controls. Seed-deviation projections provide complementary directional validation, but shared forward-model mismatch can still produce incorrect cross-seed consensus. These results characterize joint thermodynamic recovery and the usefulness and limits of seed-based error localization in a controlled, single-scene solar tomography testbed.

---


### 48. [When Do Differentially Private Inputs Protect Graph Shift Operators?](https://arxiv.org/abs/2609.28899)

**<font color=#1a73e8>作者：</font>** Andrew Campbell, Chenyue Zhang, Hang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study the differential privacy (DP) of a graph shift operator (GSO) when an analyst observes the output of a graph filter. In particular, we study the setting in which the input signals to the graph filter are drawn from a differentially private distribution. Unlike approaches that perturb the GSO or the filter output, we use the randomness already present in the inputs to protect the GSO. This yields an equivalent level of privacy protection to that of the perturbation methods without adding noise, and thus a better privacy-utility trade-off. We provide an explicit characterization of the privacy loss and its certificate in terms of the zeros of the graph filter. In doing so, we show that the log-likelihood ratio between the releases of two adjacent topologies is governed by the distances from each zero to the graph frequencies of the two GSOs. Then, by uniformly bounding the log-likelihood ratio over the adjacent topologies, we obtain an explicit $(\varepsilon,\delta)$-DP guarantee for Gaussian inputs. We further show, via a Cramér--Rao bound, that the zero placement that limits the privacy loss also raises the floor on the adversary's reconstruction error. Finally, empirical validation is performed on a synthetic network of financial exposures, where the largest position a pair can conceal and the accuracy with which it can be sized are collinear across pairs. Both are set by the graph-frequency content of the pair, and the full network becomes recoverable only as the certified budget grows.

---


### 49. [HelpCoach: Scaffolding Targeted AI Help-Seeking During Problem-Solving](https://arxiv.org/abs/2609.28918)

**<font color=#1a73e8>作者：</font>** Hyoungwook Jin, Weirui Peng, Jieun Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Students increasingly turn to AI for help with problem-solving, yet too much AI support can undermine learning itself. To benefit from AI, students need to specify the necessary knowledge and scaffold type in their questions. However, they struggle to formulate such targeted questions because they lack metacognitive skills to recognize and select effective help options. We developed HelpCoach, an add-on for chat interfaces that helps students formulate knowledge- and scaffold-specific questions and receive targeted help during problem solving. HelpCoach continuously assesses students' help-seeking performance and prompts students to improve through an adaptive revision template. Whereas prior work has largely taught help-seeking skills apart from learning tasks, HelpCoach's in situ scaffold enables concrete practice on metacognitive skills and immediate revisions to help-seeking behavior. In a study with 40 college students learning web programming, HelpCoach led to more specific questions during chatbot interactions and greater knowledge retention than pre-task help-seeking training alone.

---


### 50. [ViRDM: Taming Representation Distribution Matching for Few-Step Causal Video Generation](https://arxiv.org/abs/2609.28923)

**<font color=#1a73e8>作者：</font>** Zichong Meng, Chongjian Ge, Chun-Hao P. Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step autoregressive (AR) video diffusion enables low-latency streaming generation, but existing post-training methods predominantly rely on Distribution Matching Distillation (DMD), requiring both a large pretrained teacher and an online critic to estimate distributional discrepancies through diffusion scores. In this work, we ask whether this resource-intensive teacher--critic stack can be eliminated by post-training only the generator against a precomputed target distribution. Drawing inspiration from representation distribution matching (RDM) for one-step image generation, we systematically study its transfer to few-step causal video generation and identify three key barriers: a memory-intractable gradient path, a distinct video optimization regime, and representation distributions that underconstrain temporal dynamics. We introduce ViRDM, a teacher- and critic-free video post-training recipe that addresses these barriers sequentially. By coupling RDM with stochastically truncated clean-exit supervision, a lightweight VAE decoder, and staged vector--Jacobian products, ViRDM makes representation distribution matching memory-feasible for multi-step causal video rollouts. We further establish effective generated-population and initialization regimes for video RDM, and introduce lightweight dynamics regularization to compensate for the underconstrained temporal dynamics. ViRDM turns three-network distillation into generator-only post-training, reducing GPU memory use and training time while improving video quality. With only 20 generator updates, the recipe reaches 84.87 on the official VBench evaluation, outperforming the previous best few-step causal baseline by 0.36, while requiring 16 A100 GPU-hours. We additionally report exploratory results demonstrating the potential of the same recipe for lower causal sampling budget and for one-, two-, and four-step bidirectional generation.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
