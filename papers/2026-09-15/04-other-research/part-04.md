# 📦 其他研究 | 2026年09月15日

> 本类共 **201** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-201](./part-05.md)

---

### 151. [A Dual Cross-Attention Framework for Colposcopic CIN Grading and Swede Score Prediction Using a New Multi-Center Dataset](https://arxiv.org/abs/2609.12827)

**<font color=#1a73e8>作者：</font>** Dania Khan, Nuzhat Aisha Shaikh, Asfina Hassan Juicy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cervical cancer is a major global health challenge, with disease burden falling disproportionately on low- and middle-income countries (LMICs) due to a shortage of trained specialists and the subjective nature of colposcopy-based screening. To address this challenge, we propose a novel deep learning framework for the automated grading of Cervical Intraepithelial Neoplasia (CIN) and the prediction of clinical Swede scores. We also introduce the BUET Multi-Center Colposcopy Dataset, a novel, multi-center cohort designed and annotated for Swede score prediction and CIN grading. Our proposed dual-stream cross-attention architecture mimics the visual reasoning of an expert colposcopist by explicitly fusing paired multimodal cervigrams to evaluate comparative tissue responses. Furthermore, we introduce a custom composite loss function to address severe class imbalances and scoring inconsistencies across the five Swede score components. The proposed framework achieved 71.85% accuracy and an 86.23% AUC-ROC for three-class CIN grading, outperforming existing methods. For Swede score component prediction, the architecture achieved AUC-ROC values ranging from 75.7% to 88.4%, with the composite loss function yielding consistent F1-score improvements. Finally, the total predicted Swede Score, which ranges between 0 and 10, shows a Mean Absolute Error (MAE) of 1.489. The results show that the proposed method can pave the way towards developing AI-assisted colposcopy screening tools to support risk-based triage in resource-limited healthcare settings. The dataset and source code are publicly available(url: this https URL)

---


### 152. [Self-supervised Pre-training Helps Retinal Disease Progression Modelling Most When Data Is Scarce](https://arxiv.org/abs/2609.12834)

**<font color=#1a73e8>作者：</font>** Ifeoma Veronica Nwabufo, Julius Gervelmeyer, Sarah Müller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modelling how a disease progresses over time requires longitudinal imaging cohorts, which are scarce and small, whereas cross-sectional data -- one image per participant -- is abundant. Self-supervised pre-training on such data offers a way to bridge this gap, but it is unclear which strategy best supports progression modelling, or how that answer depends on the amount of labelled longitudinal data. We study this for age-related macular degeneration (AMD), pre-training encoders on the large cross-sectional NAKO cohort and predicting time to late AMD on the longitudinal AREDS dataset. We compare in-house self-supervised encoders against a general-purpose (DINOv2) and a domain-specific (RETFound) foundation model, across contrastive, masked-autoencoding, and self-distillation objectives, under frozen and fine-tuned protocols, and across labelled training sets from 100 to 32,250 examples. Which model performs best depends on how the encoder is used. When the encoder is frozen and labels are few -- the regime typical of longitudinal cohorts -- pre-trained representations reach clinically reasonable discrimination from a few hundred labelled samples, while models trained from scratch do not; this advantage fades under fine-tuning. Transfer is governed by the self-supervision objective rather than corpus scale or domain match, so that an encoder pre-trained on a modest cross-sectional cohort matches or exceeds a far larger in-domain foundation model. Together, these results offer a practical recipe for building progression models where longitudinal data is scarce: a frozen self-supervised encoder with a lightweight survival head.

---


### 153. [HemaHier: Chain-Conditioned Ordinal Hierarchies for Lineage-Aware Bone-Marrow Cytology](https://arxiv.org/abs/2609.12835)

**<font color=#1a73e8>作者：</font>** Afshin Bozorgpour, Peter Schüffler, Edgar Jost 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bone-marrow cytology is inherently structured: each cell belongs to a hematopoietic lineage, and many cell types lie on ordered maturation trajectories. Standard flat classifiers ignore this structure, treating a mild same-lineage confusion the same as a severe cross-lineage mistake and predicting only discrete labels. We propose HemaHier, an ordinal-hierarchical prediction head for a frozen or lightly adapted cytology foundation model. Its central component is a chain-conditioned maturity score that reads a single maturity value under a per-chain query, supervised only on biologically valid healthy chains, while dysplastic and off-chain cell types remain classes but are excluded from maturity supervision. Fine and lineage predictions are coupled through a shared posterior that guarantees hierarchical consistency, and a staged objective first stabilizes recognition, then adds lineage and maturity supervision. On three bone-marrow datasets under a shared ontology, HemaHier achieves competitive recognition while reducing biologically severe errors and adding a within-lineage maturity ordering that flat classifiers lack. Code is available at this https URL.

---


### 154. [Pre-Trained Low-Rank Tensor Decomposition for Multi-Dimensional Image Recovery](https://arxiv.org/abs/2609.12843)

**<font color=#1a73e8>作者：</font>** Bing-Zhang Fu, Zhi-Long Han, Ting-Zhu Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, tensor decompositions are prevalent for multi-dimensional image representation, which learn the instance-specific structure of each image from scratch. However, tensor decompositions neglect the common structure across different images, leading to limited semantic modeling capability, high computational cost, and a large number of learnable parameters. To address this challenge, we suggest the first pre-trained low-rank tensor decomposition (PLTD) framework, which organically integrates the pre-trained large vision model into the classical tensor decomposition framework. Beyond the shallow and untrained deep tensor decomposition, the suggested PLTD achieves an unprecedented balance among higher recovery fidelity, fewer learnable parameters, and smaller carbon footprint. Specifically, PLTD factorizes the target tensor into a latent tensor and a learnable transform that maps the latent tensor back to the original data domain. The latent tensor consists of two indispensable and complementary terms, i.e., a fixed pre-trained latent tensor and a learnable low-rank latent tensor. The fixed pre-trained latent tensor is distilled from a pre-trained large vision model (i.e., DINOv3) to capture the common structure of the target tensor, while the learnable low-rank latent tensor characterizes the instance-specific structure of the target tensor. To examine the potential of PLTD, we develop the corresponding multi-dimensional image recovery model and theoretically justify the advantages of this framework. Additionally, we discuss the connections between PLTD and classical tensor decomposition frameworks. Extensive experiments on multi-dimensional image recovery demonstrate that PLTD consistently achieves superior performance compared with state-of-the-art methods.

---


### 155. [MGAvatar: Mesh-Bound Gaussians for Head Avatar Geometry and Appearance Modeling](https://arxiv.org/abs/2609.12850)

**<font color=#1a73e8>作者：</font>** Lei Shi, Sen Peng, Zhiyang Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate head modeling requires a stable yet expressive geometric representation. Existing Gaussian-based head avatars commonly rely on parametric templates (e.g., FLAME) for Gaussian initialization and deformation, but these templates lack personalized priors and struggle to represent structures such as hair and clothing. To address this issue, we propose MGAvatar, a Gaussian-mesh hybrid representation that jointly models geometry and appearance through two Gaussian-mesh binding modes. Specifically, we introduce vertex-bound Gaussians and constrain their learnable parameters, enabling progressive mesh deformation to represent complex head geometry, while a pose-dependent offset module accounts for non-rigid deformations. Once geometry is stabilized, MGAvatar switches to face-bound Gaussians for appearance modeling. To improve appearance consistency across novel poses and viewpoints, we introduce a view-conditioned neural color field that alleviates artifacts caused by independently optimized Gaussian colors. In addition, we design a Gaussian offset network to predict Gaussian offset maps in the observation space, providing greater flexibility for face-bound Gaussians to capture dynamic facial textures. Extensive experiments on multi-view and monocular videos show that MGAvatar outperforms existing methods in rendering quality, producing high-fidelity head avatars with rich texture details.

---


### 156. [3D CT-to-PET Translation via Latent Brownian Bridge Diffusion](https://arxiv.org/abs/2609.12860)

**<font color=#1a73e8>作者：</font>** Sarita Mourya, Francesco Di Feola, Pierangelo Veltri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT) and positron emission tomography (PET) provide complementary anatomical and functional information for cancer diagnosis and treatment planning. However, the widespread use of PET is limited by high radiation exposure, elevated costs, and restricted availability. To address these limitations, deep learning-based CT-to-PET translation has emerged as a promising approach for synthesizing PET-like information directly from CT images, although accurately modeling the large cross-modal gap remains challenging. In this work, we propose a 3D CT-to-PET translation framework based on latent Brownian Bridge Diffusion (BBDM). The method consists of two stages. First, a Variational Autoencoder (VAE) is trained on paired CT-PET patches, integrating contrastive learning to improve latent alignment between anatomical and metabolic representations. Second, a BBDM is trained in the latent space to translate CT latent representations into their corresponding PET counterparts. The translated PET latents are then decoded and stitched to reconstruct the final 3D PET volume. We evaluate the proposed approach on two publicly available datasets. Quantitative results based on image fidelity and lesion-level PET-specific metrics demonstrate improved performance compared with competing methods. In particular, the proposed approach improves PET signal fidelity, better preserves clinically relevant uptake patterns, and shows improved performance in preserving small-lesion metabolic activation, paving the way for virtual imaging applications.

---


### 157. [VideoTok4D: A 4D-Aware Video Tokenizer for Compact World Representation](https://arxiv.org/abs/2609.12874)

**<font color=#1a73e8>作者：</font>** Xinyi Chen, Hanxin Zhu, Xijun Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video tokenizers have emerged as a cornerstone of modern video modeling, underpinning progress in compression, reconstruction and generation by mapping high-dimensional visual signals into compact latent spaces. However, despite this progress, current tokenization paradigms largely remain within the 2D visual domain, treating videos as image sequences rather than observations of an underlying dynamic 3D world. Consequently, the learned tokens inherit this observation-centric bias, limiting their capacity to compactly represent real-world 4D scenes. To mitigate this issue, we propose VideoTok4D, a novel 4D-aware video tokenizer for compact world representation. Specifically, our approach comprises three key designs: 1) a spatiotemporal disentanglement strategy that factorizes videos into static and dynamic tokens for holistic world modeling; 2) a track-aware dynamic attention mechanism that aggregates trajectory-aligned cues to promote cross-view motion consistency; and 3) Co4DGen, a diffusion prior learned over the resulting VideoTok4D token space for efficient 4D scene generation. Extensive experiments have demonstrated that our proposed method achieves state-of-the-art performance while requiring up to 4 orders of magnitude less storage than dense 4D representations. Moreover, the compact token space substantially shortens diffusion sequences, enabling efficient generation.

---


### 158. [What an odour descriptor corpus can and cannot measure: valence, attenuation, and the ceiling of the public record](https://arxiv.org/abs/2609.12875)

**<font color=#1a73e8>作者：</font>** Stylianos Kampakis, Fabio Rovai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine olfaction trains on pooled public descriptor corpora, but whether a shared descriptor word measures the same thing across corpora has not been tested, nor has the ceiling of what any of them can measure.
We audit four corpora from Pyrfume. Conditioning on the molecule makes McNemar's test the exact conditional test of the corpus effect. Corpora disagree heterogeneously across descriptors ($I^2 = 80\%$) and non-uniformly with labelling breadth ($z = 17.2$), so no single offset repairs pooling. Median tetrachoric agreement is 0.795 against median $\kappa$ of 0.413: sources largely concur on which molecules deserve a word and differ on how readily they apply it. Of 109 descriptors with an estimable effect, 36 show large differential functioning on the ETS scale.
Against a human panel's reliability, Morgan fingerprints with the full RDKit descriptor block reach 32.9\% of achievable; adding every label from two merged corpora reaches 33.9\%. The gap does not close with model capacity, encoding choice, more molecules, or more words.
The missing variance is valence. One pleasantness rating per molecule reaches 54.6\% of achievable (57.1\% on an independent older instrument). Valence recovered from descriptors ($\rho = 0.457$) yields only 16.6\%, so it must be measured. Five raters exceed structure plus the full descriptor record; fifteen to twenty saturate. We release a descriptor crosswalk and twenty machine-checked theorems.

---


### 159. [MedSNIP: Building and Benchmarking Snippet-Level Granularity for Medical Fact Verification](https://arxiv.org/abs/2609.12884)

**<font color=#1a73e8>作者：</font>** Hasan Iqbal, Sarfraz Ahmad, Hyunjae Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A medical claim's correctness often depends not on the claim alone, but on the clinical structure around it. A claim may require a lab reference range, a causal or conditional link, or patient-specific details to be judged correctly, and atom-level decomposition can fragment these dependencies, leaving the verifier with clinically incomplete claims. We reformulate medical fact-checking around snippet-level verification, where clause-grouped units preserve local clinical structure. We introduce MedSNIP-Bench, a human-annotated benchmark for snippet-level medical fact verification, and MedSNIP, an automatic snippet-generation pipeline. MedSNIP-Bench covers 276 consumer-health and clinical-vignette responses, segmented into 2,524 snippets with dual in-general and in-patient-context labels and six structural pattern codes. MedSNIP is evaluated against human snippet boundaries on MedSNIP-Bench and then used to generate snippet-level units for external corpora. Across MedSNIP-Bench, HealthFC, and MedHallu, snippet-level verification preserves or improves false-class F1, with gains concentrated where answers are long enough to fragment and where the verifier is strong enough to exploit the recovered structure. The largest merge-pattern gain is on causal-conditional clinical chains. It also reduces verifier calls by 24-73%, though the saving survives end-to-end only when decomposition is cheap, which an open-weight decomposer makes possible at no loss of chunking fidelity.

---


### 160. [Learning Sign Language Recognition under Label Noise: A Study of Noise-Robust Losses for Isolated and Continuous Settings](https://arxiv.org/abs/2609.12885)

**<font color=#1a73e8>作者：</font>** Akihisa Shitara, Yoichi Ochiai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In sign language recognition, the isolated (ISLR) classification loss treats a single label as ground truth, as does the frame-level auxiliary classifier over pseudo-labels we add to continuous (CSLR) methods, which lack one. Stylistic variation blurs ISLR annotation and the lack of temporal boundaries in CSLR forces pseudo-labels; both are noisy. We therefore apply symmetric and generalized cross entropy (SCE, GCE), robust alternatives to cross entropy (CE) from image classification, not to connectionist temporal classification but to the preceding single-label classifier. On ASL Citizen with injected symmetric noise on three backbones (three seeds for ST-GCN), robust losses cost at most 2.5 pt when labels are clean and beat CE by 2.9-10.0 pt in all six conditions at noise rate 0.2, one of which only after q was re-selected on dev. GCE gains more, but its optimal q does not transfer across backbones, whereas one SCE setting works in all nine conditions; both vary 2-11 times more than CE across runs, so a favorable point estimate does not establish stability. For CSLR (PHOENIX-2014) we report no gain; our frame-level targets carry a systematic assignment bias, making that study a diagnosis of a single configuration. At lambda_aux = 25 the pseudo-label CE auxiliary raises word error rate above the no-auxiliary baseline on VAC, CorrNet and SlowFastSign, and GCE/SCE improve on CE by 1.7-3.2 pt (three of six conditions return below that baseline). However, the three losses differ by more than an order of magnitude in effective gradient at a common lambda_aux: matching the initial gradient shrinks the gap to 0.4-0.9 pt, and lowering the CE weight alone already beats that baseline, so neither the degradation nor the improvement can be separated from the effect of the weight. We use only symmetric noise; multi-seed evaluation covers only ST-GCN and VAC isolated.

---


### 161. [Large Distant Gradients Need Not Be Reliable: reliability-weighted credit assignment for long-horizon autoregressive forecasting](https://arxiv.org/abs/2609.12890)

**<font color=#1a73e8>作者：</font>** Junhao Zhao, David Michael Simberg, Jacob Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In autoregressive forecasting, long prediction rollouts provide distant supervision, but backpropagation through time (BPTT) carries gradients from those losses through many autoregressive steps. Repeated Jacobian products can make distant gradients dominate the update while amplifying predictable signal and unpredictable noise together; a large distant gradient therefore need not carry reliable learning signal. Motivated by this observation, we introduce Internal Dual-Wiener routing (Internal-DW), a principled backward-only intervention that preserves the full forward rollout and all horizon losses while reliability-weighting internal gradient routes. At each residual block, we derive bounded Wiener gains for the identity and nonlinear routes that balance preserving predictable learning signal against suppressing unpredictable variation, and estimate them from route-level gradient statistics and an explicit noise model. In a controlled system with known gradient signal-to-noise ratio (SNR), we show that distant gradients can grow even as their SNR falls, and that Internal-DW reduces held-out error in recovering predictable gradient signals and improves forecasting. On four history-dominated, weak-drive testbeds, Internal-DW reduces forecast error by 5.2%-13.8% relative to full BPTT, outperforms gradient clipping and Jacobian regularization on all four, and outperforms validation-selected truncated BPTT (TBPTT) on three. It also extends or preserves the fitted optimal training-horizon range across these four testbeds. Across the full benchmark suite, the current Internal-DW estimator has a clear applicability boundary: its benefit diminishes or reverses when usable history is limited or when the selected sampler fails to represent dominant drive-dependent variation. The results show that retaining long-horizon supervision does not require trusting every backward contribution equally.

---


### 162. [Quantifying the Value of Privileged Information Using a PAC-Bayesian Approach](https://arxiv.org/abs/2609.12891)

**<font color=#1a73e8>作者：</font>** Vasily Bokov, Sebastian Schmitt, Vedran Dunjko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In practice, various learning scenarios provide access to auxiliary features exclusively during training. Incorporating such data to enhance model performance gave rise to a paradigm known as Learning Using Privileged Information (LUPI). While this extra information is intended to improve the resulting model, establishing a generalized, cohesive understanding of how privileged information (PI) transfers useful knowledge remains a challenge. Vapnik's original theory and subsequent works offer performance guarantees in certain cases, but these results are inherently per-algorithm and rely on setting-specific proof approaches. Consequently, a more general framework explaining how and when PI transfers useful knowledge is still missing. To bridge this gap, we introduce an algorithm-agnostic, information-theoretic approach based on the PAC-Bayes framework. Rather than asking whether a particular algorithm exploits PI, we ask how much value it could offer: comparing the tightest achievable risk bound with and without PI yields its potential - an upper limit on the extractable gain. We introduce a metric that quantifies this potential directly from empirical training risk, bypassing the need for test-time data access, and validate our findings in both supervised and unsupervised settings. The results demonstrate a robust correspondence between our training-time metric and true test-time performance gains. Ultimately, this work takes a necessary step toward an information-theoretic understanding of LUPI, and quantifying the potential of privileged features before committing to a model.

---


### 163. [Beyond Accuracy: Uncertainty-Guided Boundary Refinement for Reliable Biomedical Image Segmentation](https://arxiv.org/abs/2609.12892)

**<font color=#1a73e8>作者：</font>** Anima Kujur  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate biomedical image segmentation requires not only high global overlap but also reliable delineation of clinically meaningful boundaries. In blood-smear microscopy, cytoplasm and nucleus contours provide the structural basis for downstream morphology analysis; however, deep segmentation models may remain uncertain or overconfident near ambiguous boundary regions even when achieving strong Dice scores. This work proposes a Reliability-Aware Boundary Refinement Network (RABR-Net), a two-stage framework for trustworthy image segmentation. A strong UNet++ EfficientNet-B4 base segmenter first produces initial class probabilities and logits. Predictive entropy, test-time augmentation variance, margin uncertainty, probability gradients, and soft boundary cues are then combined into a boundary-aware reliability representation. This representation guides a gated residual refiner that selectively corrects uncertain boundary pixels while preserving confident regions of the base prediction. The framework is evaluated using overlap accuracy, class-wise Dice, Boundary Dice, HD95/ASSD, calibration, risk--coverage analysis, robustness under image perturbations, qualitative correction maps, and paired statistical testing. On the held-out test set, the proposed method improves Dice from 0.9602 to 0.9614, Boundary Dice from 0.3448 to 0.3611, and HD95 from 3.0354 to 2.8274 compared with the cached base prediction. Statistical analysis confirms significant improvements in Dice, Boundary Dice, and HD95. Qualitative results show that the learned gate concentrates around uncertain cytoplasm and nucleus boundaries, and correction maps confirm localized boundary refinement. Although calibration does not automatically improve after refinement, the proposed framework provides an interpretable and reliability-focused strategy for boundary-sensitive biomedical image segmentation.

---


### 164. [Tracing and Coordinating Cross-Layer Influence for Multimodal Model Merging](https://arxiv.org/abs/2609.12897)

**<font color=#1a73e8>作者：</font>** Pengyang Zhou, Xiaobin Tu, Zhengxi Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal model merging aims to consolidate task experts into a single model that retains their complementary capabilities. Most unimodal model merging methods combine expert updates within individual layers, and multimodal approaches largely follow this design. However, an expert update changes the representations passed to subsequent layers, allowing its influence to propagate across depth and affect how visual and textual information interact. When visual and language updates are combined, later updates act on inputs already modified by earlier ones, coupling their effects. This poses two challenges: (1) how to characterize the multimodal influence of individual expert updates across depth, and (2) how to jointly combine expert updates based on their multimodal influence. To address these challenges, we propose TAC-Merge for tracing and coordinating cross-layer influence in multimodal model merging. It contains two modules, i.e., multimodal influence mapping (MIM) and coupled merge control (CMC). MIM constructs graphs of update effects and uses Ricci curvature together with expert predictions to define a shared fusion objective. CMC models interactions among coefficient adjustments and jointly optimizes regional weights to synthesize one shared model. Experiments across diverse multimodal tasks demonstrate the effectiveness of TAC-Merge in consolidating complementary expert capabilities and supporting generalization to unseen tasks.

---


### 165. [UniPart: Towards Zero-shot Language-Grounded 3D Part Segmentation for Embodied Interaction](https://arxiv.org/abs/2609.12898)

**<font color=#1a73e8>作者：</font>** Xinqiang Yu, Zekun qi, Jiawei He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained robotic manipulation depends on understanding parts, not only whole objects. Existing 3D foundation models tend to be either generalized but object-aware, or part-aware but limited to closed-set taxonomies, which weakens zero-shot transfer. We study text-conditioned 3D part segmentation, where a free-form phrase selects a functional part on point cloud. We introduce UniPart, a feed-forward cross-modal 3D Transformer that conditions CLIP text embedding. To scale supervision, we build LangPart-1M with 160K+ Objaverse assets and 8M text to part pairs using multi-view consistent part generation. We further manually label a high-quality subset, LangPart-4K, for fine-tuning and evaluation. UniPart achieves strong zero-shot results on open-vocabulary part benchmarks and transfers to language-conditioned part grasping in real world.

---


### 166. [Physical-State-Guided Diffusion Sampling for Full-Waveform Inversion](https://arxiv.org/abs/2609.12899)

**<font color=#1a73e8>作者：</font>** Chen Min, Haowen Jiang, Zheng Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full waveform inversion (FWI) estimates subsurface velocity from seismic recordings, but its ill-posedness and nonlinearity make accurate reconstruction strongly dependent on initialization and prior information. Diffusion posterior sampling provides a learned geological prior, yet directly coupling its denoiser to the nonlinear wave solver can yield unreliable physical guidance. We propose Physical-State-Guided Diffusion Sampling (PSG), which couples a persistent physical velocity to the diffusion prior through a Gaussian bridge. The physical state is refined by waveform fitting regularized by the denoised velocity, and in turn guides the reverse diffusion process. This formulation separates the wave-equation and denoiser gradients while preserving conventional FWI initialization and accumulated optimization history. On four OpenFWI families, PSG's terminal denoised estimates outperform classical and diffusion-based baselines under clean and missing-trace acquisitions and maintain strong structural recovery under measurement noise. Repeated stochastic runs preserve the dominant geological structures, with ensemble variability concentrated near geological interfaces and positively associated with local inversion error. A frozen OpenFWI-trained prior further supports inversion of the larger Marmousi, Overthrust, and BP2004 Salt models, recovering complex geological structures without retraining.

---


### 167. [Parallel Training Using a CNN-DNN Architecture for Accelerated Development of Diagnostic Models](https://arxiv.org/abs/2609.12902)

**<font color=#1a73e8>作者：</font>** Janine Weber-Hamacher, Astha Jaiswal, Philipp Fervers 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence has shown promise in assisting radiologists in imaging-based diagnosis across a wide range of diseases. Efficient training of large deep learning models is essential to cope with extremely large data sets or dynamically growing disease data, like in a pandemic like situation. In this retrospective study, we collected 300 CT scans from COVID-19 and non-COVID-19 pneumonia patients from three different centers in Germany. We investigated a hybrid CNN-DNN network model based on image decomposition and localization that naturally supports parallel and efficient training of deep learning models. In total, 156 models with three different architectures were trained to capture features at different levels resulting in 12 patient-level COVID-19 diagnosis models. Diagnostic performance as well as time saving were measured.
The highest accuracy was obtained from DenseNet121 and 3D CNN models with a parallel CNN-DNN approach, resulting in $88.78\%$ training, $76.67\%$ validation and $76.03\%$ test accuracy for the DenseNet121 with $4\times4\times1$ subdomains and $87.72\%$ training, $76.82\%$ validation and $74.86\%$ test accuracy, respectively, for the 3D CNN with $4\times4\times1$ subdomains. The strongest reduction in parallel training time by a factor of $31$ was observed for the 3D CNN model and $4\times4\times2$ subdomains.
Our parallel training approach improves efficiency as well as performance enabling rapid model development, among others crucial for pandemic preparedness.

---


### 168. [Hidden in Rounds: Predicting the Time Cost of 802.11 Contention in Federated Learning](https://arxiv.org/abs/2609.12903)

**<font color=#1a73e8>作者：</font>** Satwat Bashir, Tasos Dagiuklas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning over IEEE~802.11 shares the wireless channel among clients that send model updates. We use ns-3 to measure the frame-delivery ratio and saturation throughput for different client densities and offered loads. A separate FedAvg trainer uses the frame-delivery ratio as a first-order proxy for the update-admission probability and uses an equation to estimate communication time. The method does not simulate the delivery of a complete model update or measure end-to-end training time. Across 720 evaluated runs with two datasets, two data partitions, six client densities, six offered loads, and five seeds, all runs reached their predefined target accuracy within the round budget. Rounds-to-target changed little with offered load, while communication time-to-target increased by about two orders of magnitude across the client-density range. A Bianchi-anchored estimator produced a mean absolute percentage error from $2.3\%$ to $10.2\%$ on held-out configurations. This error is measured against communication time constructed from the same round-duration equation, not against independently measured completion time. We also compare uniform participation with persistent heterogeneous participation. The study does not detect a statistically distinguishable excluded-class accuracy gap over five seeds, but the confidence intervals are wide. The results apply only to the evaluated configurations and do not provide a general convergence or fairness guarantee.

---


### 169. [Offline Reinforcement Learning for Wind Farm Control: A Wind Tunnel Study under Dynamic Wind Directions](https://arxiv.org/abs/2609.12905)

**<font color=#1a73e8>作者：</font>** Yuhan Su, Hongyang Dong, Simone Tamaro 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper addresses the wind farm power maximization problem in the presence of wind direction changes. Specifically, a model-free Modified Twin Delayed Deep Deterministic Policy Gradient with Behavior Cloning (MTD3-BC) algorithm is proposed to tackle this task through yaw control under varying wind direction conditions. MTD3-BC is an offline reinforcement learning (RL) algorithm that aims to infer good behavior from only a precollected offline dataset. Additionally, to ensure smooth and moderate yaw adjustments, a new action consistency term is introduced into the policy optimization objective. Unlike online RL methods, MTD3-BC does not require extensive interactions with a wind farm simulator during training, significantly reducing computational costs and training time. A wind tunnel experiment is conducted to validate the effectiveness of the algorithm under varying wind directions. The results demonstrate that MTD3-BC successfully mitigates wake effects, delivering farm-level power gains of approximately 10\% over the baseline greedy strategy and performance on par with a data-calibrated model-based wake-steering benchmark, while requiring no wake model and only a small fraction of the training cost of online RL. To our knowledge, this is the first time an offline RL wind farm control policy has been validated and demonstrated experimentally.

---


### 170. [Forging Tree-Ring: Reproducing and Instrumenting Black-Box Semantic Watermark Forgery](https://arxiv.org/abs/2609.12909)

**<font color=#1a73e8>作者：</font>** Saifur Rahman Tamim, Md Taslimul Hasan Toufique, A.M. Tayeful Islam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Semantic watermarking schemes such as Tree-Ring hide a detectable pattern in the initial noise latent of a diffusion model. Recent work shows these watermarks are not only removable but forgeable: an attacker who never sees the watermarking key can still produce images the genuine detector accepts. We reproduce the Reprompt forgery attack of Müller et al. against Tree-Ring on Stable Diffusion XL, using the authors' released code, on free-tier dual T4 GPUs with 14.6 GB of usable memory per device, substantially less per-GPU memory than the A40 hardware used in the original study. The attack reproduces. Over six trials of three arms we detect genuine images 6/6, clean images 0/6, and forged images 5/6, at 325-332 s per attack. Three further results came out of running it under constraint. The released detector computes a non-central $\chi^2$ statistic and hands back only its CDF, so we recovered the discarded statistic; our recovery matches the released detector exactly, and two natural scores built from it separate the forged arm from the clean null at AUC 0.861 and 0.972 on the same eighteen observations. Running SDXL in half precision requires patching the pipeline's direct autoencoder calls, and a controlled probe confirms the patched path leaves the detector statistic unchanged. Finally, we report a prediction we made from reading the detector source that our measurements then contradicted. The notebook, the pinned fork and every measurement artifact are released with the paper.

---


### 171. [NeuroClick: Preserving Surgeon Autonomy through Hands-Free Earable Tooth-Click Control in Neurosurgery](https://arxiv.org/abs/2609.12910)

**<font color=#1a73e8>作者：</font>** Jonas Hummel, Maximilian Burzer, Clara Sayffaerth 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Neurosurgeons frequently interact with operating room (OR) technologies while sterility and occupied hands constrain control. We introduce earables as a direct, hands-free control platform for neurosurgery using tooth-click input. Formative OR observations and interviews with 10 domain experts grounded the design. Using OpenEarable 2.0 data from 12 participants, we developed a real-time recognition pipeline whose classifier achieved a median macro F1-score of 98.6% under leave-one-subject-out cross-validation. We evaluated the technique with 20 neurosurgeons during a simulated resection task in a neurosurgical OR. Participants reported few focus shifts and rated Earable favorably for workflow integration and perceived safety. Autonomous microscope control was rated significantly higher with Earable than Delegation, whereas Delegation enabled faster task completion under continuous assistant availability. Workload, usability, and task errors showed no significant differences. Preferences depended on training, reliability, context, and assistant availability. Earables thus add a direct, hands-free option for controlling selected functions alongside established workflows.

---


### 172. [Shuffling is Not Enough: Breaking Permutation-Based Model Confidentiality in Hybrid FHE Inference](https://arxiv.org/abs/2609.12911)

**<font color=#1a73e8>作者：</font>** Jiseung Kim, Hyung Tae Lee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hybrid fully homomorphic encryption~(FHE) inference improves the practicality of private inference by letting the server evaluate linear layers homomorphically while the client decrypts and applies nonlinearities. Recent schemes attempt to protect model confidentiality by returning noisy, output-permuted responses and appealing to shuffle-model differential privacy~(DP). We show that this protection fails in the correctness regime required by hybrid FHE systems. For a $d$-input linear layer, $d+1$ admissible queries suffice for exact recovery of a permutation-invariant layer summary, hence for perfect model distinguishability. We further show that input DP is orthogonal to model confidentiality and that the local-DP premise required for shuffle amplification cannot hold under correctness-bounded noise. We recover all linear layers of a \safhire{}-style ResNet-20 end-to-end from TFHE transcripts with zero error, using $d+1$ queries per layer for a total of $5{,}712$ direct queries. Under the same query model, we also confirm exact per-layer recovery on pretrained ImageNet-scale CNNs and ViT-B/16. The leaked spectra enable fingerprinting, lineage attribution, and improved logit-based extraction, while suppressing them destroys inference utility.

---


### 173. [Input Resolution Matters: Real-Time Object Detection Latency](https://arxiv.org/abs/2609.12920)

**<font color=#1a73e8>作者：</font>** Qingyang Zhang, Fumio Machida, Laura Carnevali  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We model total latency as the convolution of preprocessing, inference, and postprocessing distributions under a simplifying independence approximation, with selected stage parameters expressed as functions of source-image resolution. Under this assumption, the probability density of the total latency is the convolution of the stage-wise densities, and its cumulative distribution function (CDF) provides the distribution of end-to-end detection time. Each stage is modeled by a parametric distribution (e.g., Exponential, Erlang, Normal, Gamma), with parameters expressed as functions of the source-image resolution. Experiments with YOLOv11n on NVIDIA Jetson Orin NX using COCO2017 images across multiple resolutions assess the proposed models against fixed-parameter baselines using Kolmogorov Smirnov, Anderson Darling, and Cramér von Mises statistics. The results indicate that resolution-aware parameterization can improve distributional approximation in the measured setting, particularly for the more flexible Normal and Gamma models, while the quality of fit remains distribution dependent. Our contribution is a theoretically grounded and lightweight formulation for studying resolution-dependent latency distributions in a measured object detection pipeline.

---


### 174. [A Large-Scale AIS Dataset from Finnish Water](https://arxiv.org/abs/2609.12938)

**<font color=#1a73e8>作者：</font>** Debayan Bhattacharya, Ikram Ul Haq, Carlos Pichardo Vicencio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This research paper contributes to the maritime research community by introducing a comprehensive AIS dataset from Finnish waters, specifically the Baltic Sea region. AIS data, initially designed for collision prevention, have evolved into a versatile tool with applications across diverse maritime domains. Our paper not only curates and categorises existing AIS datasets but also introduces a collected AIS dataset from the Baltic Sea area, renowned for its intercontinental cargo routes, military activities, and frozen water expanses. This dataset includes 229 millions data points and provides researchers with a resource for studying maritime activities and vessel behaviour in this dynamic region, notably distinguished by the inclusion of data from Finnish lakes. Our analysis includes a detailed listing of ship types and relevant features, empowering researchers to explore various maritime domains. To enhance comprehension and analysis, we provide visualisations of maritime traffic patterns. By publishing this AIS dataset, we aim to catalyse innovation and collaboration in maritime research, offering a gateway to deeper insights into maritime activities in the Baltic Sea and Finnish lakes.

---


### 175. [Fast and Faithful: Principled Conditional Flow Matching for Inverse Problems](https://arxiv.org/abs/2609.12953)

**<font color=#1a73e8>作者：</font>** Shirin Shoushtari, Edward P. Chandler, Xiao Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching approaches to imaging inverse problems commonly incorporate measurements in two ways. Conditioning-based approaches supply measurement-derived information as a network input, often through concatenation, while inference-guided approaches combine an unconditional velocity field with a separate data-consistency update. In these common formulations, the forward model is not explicitly enforced within the learned conditional velocity field. We propose a principled parametrization of the measurement-conditional velocity field to solve inverse problems. Under linear interpolation, we express the conditional velocity $v(x_t,t,y)$ in terms of the posterior mean $E[x_1 | x_t,y]$, and characterize that mean as the unique minimizer of a variational objective whose data-consistency term is explicit. We further prove that the velocity field defines a probability flow from the source distribution to the measurement-conditioned posterior. Splitting the variational objective yields a conditional velocity parameterization with operator-dependent data-consistency updates, which we train end-to-end under the flow-matching objective, with no additional guidance at inference. Our method achieves state-of-the-art PSNR with $50\times$ fewer function evaluations than the strongest flow baseline. Varying the sampling steps provides test-time control over the distortion-perception trade-off without retraining.

---


### 176. [Middleware for Feed Recommendation in Practice: How Feed Creators Build, Maintain, and Sustain Custom Feeds on Bluesky](https://arxiv.org/abs/2609.12958)

**<font color=#1a73e8>作者：</font>** Tony Zhou, Leijie Wang, Amy X. Zhang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Scholars have long proposed third-party middleware as an alternative to centralized algorithmic feeds: feeds built and distributed by independent feed creators. This vision saw no large-scale instantiation until Bluesky, a decentralized microblogging platform, introduced custom feeds in 2023. Although central to the middleware ecosystem, we know little about how feed creators understand their role, build feeds, and sustain them. Through interviews with n = 26 feed creators and third-party developers of feed-building tools, and analysis of n = 88,302 custom feeds, we identify two creator orientations---utility-providing and community-building. Additionally, creators struggle to maintain feeds that fully realize middleware ideals: they lack granular interaction data, receive little feedback, and lack technical expertise to act on either. Finally, creators sustain their feeds as unpaid hobbyists with little platform support and are divided on whether to monetize beyond covering costs. We conclude with design and policy implications for strengthening the middleware feed ecosystem.

---


### 177. [Fewer Words, Not Fewer Tokens: Measuring the Sanskrit Tokenization Penalty per Proposition](https://arxiv.org/abs/2609.12960)

**<font color=#1a73e8>作者：</font>** Devansh Sharma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sanskrit fuses case, number, person and tense into word endings and chains clauses into compounds, so it is information-dense per word. Whether that density survives subword tokenization is a separate question, to be asked per unit of meaning rather than per word. On identical FLORES-200 devtest content, Sanskrit costs 1.774-2.187 times the English tokens under deployed tokenizers with vocabularies of 200,019 ids or more, but only 1.325-1.353 times the Hindi tokens. Against a deployed English tokenizer, Sanskrit-trained BPE arms then look cheaper per proposition than English on contemporary prose (0.887). Against a matched English control, the same algorithm and vocabulary trained on the English side of the same corpus, that flip disappears: at 32,000 and 64,000 pieces all 8 matched pairs, each size-matched arm against both a pair-matched and a byte-matched control, sit above 1.0 on prose with 95% intervals excluding it. The gap closes as the vocabulary grows: at 128,000 pieces the BPE pair reads 0.983 in domain while staying above parity out of domain (1.025) and on FLORES (1.116). The ratio factorises into a character-length ratio and a tokens-per-character ratio, the second near 1 throughout: what survives matched tokenization is character-level length, which Sanskrit prose lacks over English in SLP1 (1.028) and Sanskrit verse has (0.596). The robust statement is about deployed practice: on contemporary prose and on FLORES, with the Sanskrit side in SLP1 against the deployed o200k English pivot, Sanskrit costs 1.831-2.899 English tokens per proposition under the tokenizers people actually ship. Code, the results snapshot and every table here are public.

---


### 178. [Generative Retrieval for Unsupervised Text-Based Person Search](https://arxiv.org/abs/2609.12965)

**<font color=#1a73e8>作者：</font>** Mang Ye, Yucheng Ji, Yang Bai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-based person search (TBPS) aims to retrieve images of a target person from a large image gallery based on a given natural language description. Most existing methods rely on supervised learning with manually annotated image-text pairs. In this paper, we explore unsupervised TBPS, with only unlabeled images. We propose GTR+, a two-stage generation-then-retrieval framework. In the generation stage, we introduce a tiered description generation framework designed to produce fine-grained and stylistically diverse textual descriptions through a three-tier sequential process. The base tier leverages an automated question-and-answer mechanism to generate basic visual attribute descriptions; the intermediate tier enhances fine-grained detail using an inter-sample contrastive mechanism; the advanced tier further enriches textual diversity via a stylized expansion mechanism. In the retrieval stage, to mitigate the impact of noisy pseudo texts, we develop an adaptive confidence-weighted retrieval learning framework. We model image-text pairs as clean or noisy using a Gaussian Mixture Model, calibrated by real-time image-text similarity and static text generation probability from the prior stage, yielding adaptive sample weights during training. Beyond that, we also contribute LargeFine-Person, a large-scale TBPS dataset with high-quality, fine-grained, and diverse textual annotations, enabling a practical and generalizable TBPS pre-training benchmark under unsupervised setting. Experiments on multiple TBPS benchmarks demonstrate the effectiveness and generalization of both GTR+ and LargeFine-Person. Code is available at: this https URL.

---


### 179. [Information-Induced Training Geometry: Exact Reduction, Canonical Completion, and Structured Expressivity](https://arxiv.org/abs/2609.12991)

**<font color=#1a73e8>作者：</font>** Zavier Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training data constrains optimizer geometry through the covectors visible to a declared information channel. We study how such partial information determines a full positive cometric relative to a reference and which degrees of freedom remain unidentified. Our central result resolves full-column-rank positive-definite compression under affine-invariant Riemannian geometry. The compression map is a split-Hadamard metric submetry and admits an explicit unique completion that is the affine-invariant nearest full geometry realizing a visible target and yields exact full-to-visible variational reduction. When the channel moves, the completions form a gauge-invariant rank stratification of the positive-definite cone. Its closed-form pullback pair metric separates visible-metric motion from subspace rotation through a reference-mismatch weight, yields an explicit positive-semidefinite multi-direction Gram matrix, and exposes the precise singularity of reference-valued modes. The mechanism is explained by a metric theorem equating ball submetry, attained fiber distance, and lossless reduction of every monotone radial visible decision problem. A smooth split-Hadamard theorem supplies coherent information sheets, proximal commutation, and solution-wise gradient-flow lifting. The positive-definite realization also gives closed-form prior-data shrinkage. Diagonal and block optimizer families reduce to relative-interior conic image tests with valid facial certificates, while deterministic and finite-sample bounds quantify recovery of the visible geometry and its subspace. Together these results characterize exact reduction, reference-dependent completion, and structured expressivity for the stated finite-dimensional affine-invariant model.

---


### 180. [Investigating Temporal Motion Features for Pose-to-Text Indian Sign Language Translation](https://arxiv.org/abs/2609.12993)

**<font color=#1a73e8>作者：</font>** Manav Dhamecha, Praveen Kumar Chandaliya, Pruthwik Mishra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We investigate the effect of pretrained T5 model scale and explicit motion features on pose-to-text Indian Sign Language Translation (SLT) for the WSLP 2026 Shared Task. Pose sequences are projected into the embedding space of T5 through a lightweight pose encoder, with the complete model fine-tuned to generate English text. The shared task data used for this work consists of a test set with 5,334 examples and a validation set with 5,257 examples. We compare T5-small, T5-base, and T5-large, and additionally introduce a motion-augmented variant, T5-small + Motion, that adds explicit frame-to-frame pose differences to the input representation. T5-small achieves the best BLEU and ROUGE scores among the spatial-only models, while T5-large obtains the highest chrF score. Augmenting T5-small with motion features yields the largest single improvement observed in our study, substantially improving BLEU over the spatial-only baseline and making it the strongest model overall on this metric. Our submitted system ranked 5th on the official WSLP 2026 SLT testing leaderboard. The source code and trained models are publicly available on GitHub and HuggingFace.

---


### 181. [A Full Adam Theorem for Spectral Heavy-Tail Onset](https://arxiv.org/abs/2609.12996)

**<font color=#1a73e8>作者：</font>** Zongmin Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove a full Adam theorem for spectral heavy-tail onset in a closed Gaussian Stein-Hermite teacher-student state-evolution model. The theorem begins with the actual full-batch Adam recurrences, derives the population gradient by Stein-Hermite calculus, proves finite-width covariance concentration, converts multi-step Adam momentum into an exact non-centered Gaussian sign kernel, controls the diagonal Adam denominator by a basis-homogenization theorem, derives a regularly varying projected update response from a Hermite edge-transfer theorem, pushes the response through the exact Gram update, and proves approximate-target KL contraction with matching upper and lower hitting bounds. The final law is (\tau_\varepsilon=\Theta(\Delta_1^{-\gamma}d^\rho\log(\Psi_0/\varepsilon))), where (\Delta_1) is the first spike-bulk spectral gap. The result is full in the following precise sense: every step from Adam's momentum and denominator to the spectral hitting law is formalized inside the closed state-evolution model. We also prove that a stronger arbitrary-gradient Adam theorem is impossible, and that exact two-step linear-network loss dynamics do not identify factor spectra or heavy-tail hitting times.

---


### 182. [SV-Cine: Diagnosis-Conditioned Segmentation of Single Ventricle Physiology via Generative Data Augmentation](https://arxiv.org/abs/2609.12997)

**<font color=#1a73e8>作者：</font>** Lila Cunge, Yuehong Liu, Hang Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single Ventricle Physiology (SVP) is a rare subtype of congenital heart disease characterized by the presence of a single functional cardiac ventricle with atypical anatomic configurations that challenge conventional image segmentation approaches. The scarcity of clinical data and the morphological diversity across SVP subtypes make the development of robust segmentation methods particularly difficult. To address these limitations, we propose a cardiac MRI segmentation framework focused on ventricular chambers and myocardium segmentation tailored for SVP. First, we introduce a data augmentation pipeline that generates synthetic 3D cardiac meshes using SDF4CHD and corresponding synthetic cardiac MRI through generative modeling. Second, we introduce SV-Cine, a diagnosis-conditioned adaptation of the foundation model CineMA that incorporates patient-level diagnostic information through Feature-wise Linear Modulation layers, enabling diagnosis-aware feature adaptation during segmentation. We evaluated the framework on an internal cohort with varying SVP subtypes. SV-Cine achieved median Dice scores of 0.89 (IQR: 0.80--0.91) for the left ventricle and 0.72 (IQR: 0.54--0.84) for the right ventricle, outperforming the strongest baseline, nnU-Net, by 0.39 Dice points on right ventricle segmentation. It also yields a median ejection fraction error of 5.55 percentage points (IQR: 3.41--7.69) for the dominant ventricle. Compared with the internal cohort, LV and myocardium segmentation performance was lower for the external cohort; whereas RV Dice scores were comparable for both cohorts. Our findings suggest that a pretrained foundation model can be adapted for highly specialized downstream tasks through usage of diagnosis priors while leveraging anatomic knowledge learned from large-scale MRI datasets during pretraining.

---


### 183. [Dual-guided Hierarchical Edge Localization for Large-scale Optimal Transport Across Dimensions](https://arxiv.org/abs/2609.13010)

**<font color=#1a73e8>作者：</font>** Wenzhou Xia, Qiaoqiao Ding, Jingwei Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimal transport (OT) compares distributions and aligns datasets in machine learning, yet unregularized discrete OT requires a linear program with quadratically many transport variables. We propose HELLO, a hierarchical solver that casts large-scale discrete OT as edge localization and uses dual potentials to guide both coarse-to-fine initialization and within-level refinement. Initialization propagates coarse dual potentials across a recursive subsampling hierarchy to assign candidate edges. Refinement then iteratively inserts the largest dual violators in each row and column until the relative KKT residual meets a prescribed tolerance, while budgeted pruning ensures linear memory complexity. For exact-arithmetic refinement, we prove finite termination at a global optimum under a symbolic lexicographic rule. At the million-point scale, HELLO attains lower transport objectives with order-of-magnitude runtime improvements over strong baselines across feature dimensions from single digits to thousands. It further scales to 1.28 million samples per marginal in 8192 dimensions on a single H100, using 41.6 GiB peak GPU memory while satisfying a full relative KKT residual below $10^{-6}$. Beyond standard discrete OT, the framework supports general pairwise costs and serves as a scalable balanced-OT oracle for semi-discrete OT, Gromov--Wasserstein, unbalanced OT, and OT-based Flow Matching.

---


### 184. [TileNet: Tile-Based CNN-SVM Architecture for Autonomous Unmanned Aerial Systems Inspection of Flat Roofs](https://arxiv.org/abs/2609.13013)

**<font color=#1a73e8>作者：</font>** Samuel Dunthorne, Hashim A. Hashim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flat roofs are among the most influential components of the building envelope, governing both structural performance and thermal efficiency, and thereby contributing directly to household energy consumption, carbon emissions, and long-term environmental sustainability. Timely detection of roof defects is essential for reducing heating and cooling losses, preventing moisture-driven degradation such as mold growth, and supporting national climate-change mitigation goals. This paper presents a real-time, Unmanned Aerial System (UAS)-based deep learning framework that autonomously detects defects using live imagery captured during dual-altitude aerial passes. The multi-resolution flight strategy is designed to aid the identification of both small, fine-scale defects and larger structural issues, enabling more comprehensive assessments. To meet the strict computational and power constraints of embedded UAS hardware, the proposed framework integrates a tile-based architecture with a lightweight Convolution Neural Network-Support Vector Machine (CNN-SVM) classifier designed for low-latency onboard inference. The final model-comprising five convolutional layers and four dense layers, the last a linear SVM head, achieved a mean test accuracy of $94.4\%$ ($95\%$ confidence interval $\pm0.4\%$ over three seeds) on a photo-level split ($43,383$ training, $3,869$ validation, and $2,540$ test tiled and augmented images), outperforming GoogLeNet ($89.2\%$) and AlexNet ($79.8\%$). Experimental evaluations using real UAS imagery collected by onsite visits with DJI Matrice 350 RTK drone demonstrate that the system supports rapid, repeatable, and safe roof inspections while reducing human risk, lowering operational costs, and enabling more sustainable building maintenance.

---


### 185. [Label-Guided Knowledge Distillation for 3D-CNNs in Action Recognition](https://arxiv.org/abs/2609.13024)

**<font color=#1a73e8>作者：</font>** Yanjiang Shi, Peng Zhao, Nan Qi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As a key model compression technique, knowledge distillation aims to transfer knowledge from a high-capacity teacher model to a lightweight student model for enhancing the latter's performance. In this work, we reviewed the feature knowledge distillation for 3D-CNNs and observed that most feature distillation methods in video analysis are simple adaptations of those used in image analysis, often neglecting the differences of video features in the temporal dimension. To address this issue, we proposed Label-Guided Knowledge Distillation (LGKD) to guide the distillation of student model features using ground truth labels. Our method entails two components: sample-wise distillation and class-wise distillation, enabling the student model to learn feature representation of the teacher model at two levels. Sample-wise distillation utilizes label information and the teacher's probability distribution to guide the learning of features that significantly impact temporal accuracy while mitigating noise. Meanwhile, class-wise feature distillation employs a prototype network to further capture the relational knowledge among samples within the same category, enhancing the student's ability to learn higher-dimensional semantic information and improving model generalization. To demonstrate the effectiveness and superiority of our method, we conducted comprehensive experiments on two benchmark action recognition datasets, UCF101 and HMDB51, achieving competitive results.

---


### 186. [Groupoid-Based Internal State Representations for Reinforcement Learning with Local Symmetries](https://arxiv.org/abs/2609.13035)

**<font color=#1a73e8>作者：</font>** Ben Opperman, Eduardo Alonso, Esther Mondragón  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symmetries play a central role in reducing the complexity of reinforcement learning problems, yet most existing approaches rely on fixed group actions or predefined state abstractions. Classical reinforcement learning algorithms typically assume a globally structured Markov decision process with uniformly applicable actions and transitions, an assumption that limits their ability to exploit modularity and local, context-dependent regularities present in many realistic environments. We propose a reinforcement learning framework using groupoids to capture local, state-dependent symmetries and support the dy- namic discovery of equivalence structures during interaction. The agent maintains orbit representatives together with transporters that map raw states to canonical forms, enabling learning and decision-making to be performed in a symmetry-reduced space while preserving local distinctions. Empirical results demonstrate that the proposed groupoid-based approach improves sample efficiency and convergence in dense and large-scale environments exhibiting strong partial symmetries, yielding substantial performance gains over standard Q-learning. These findings show that dynamically exploiting local symmetry provides a practical and mathematically principled route to scalable and generalisable reinforcement learning.

---


### 187. [Transfer Learning for Evolving Domains](https://arxiv.org/abs/2609.13039)

**<font color=#1a73e8>作者：</font>** Ricardo Ribeiro Pereira, Jacopo Bono, Hugo Ferreira 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transfer learning explores how to leverage knowledge from various tasks or domains (sources) to enhance predictive performance in related tasks or domains (targets). Typically, transfer learning research is segmented into several isolated sub-areas (such as domain generalisation, domain adaptation, or multi-domain learning), each making distinct assumptions about target data availability, namely how much data and how many labels are available at training time. However, in many real-world applications, data availability is not fixed but evolves over time, as instances and labels are progressively collected from a new domain. Each of the classical settings then describes only a snapshot of a trajectory that a deployed system must traverse in full. We formalise this trajectory as a transfer learning problem in its own right, Transfer Learning for Evolving Domains (TrED), specified by a data availability process fixed by the environment, a learning protocol that the method is free to choose, and an evaluation criterion that scores the whole trajectory of models rather than a single one. Within this formalism, the classical settings are recovered as regimes that a learner may pass through, rather than as separate problems that TrED concatenates. We then examine the transfer learning literature to identify mechanisms that are promising building blocks for a solution, and find that most methods are tailored to a single regime and that even the strongest existing candidates do not yet optimise the whole trajectory. We argue that TrED is a well-posed and unsolved problem, and an important direction for future research.

---


### 188. [Quantile-based Loss Filtering for Outlier-Robust Stochastic Gradient Descent](https://arxiv.org/abs/2609.13040)

**<font color=#1a73e8>作者：</font>** Jamie Haddock, Anna Ma, Elizaveta Rebrova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study loss-based filtering for finite-sum optimization with a subset of corrupted component functions whose gradients may be highly unreliable. Motivated by minimum-loss-based SGD (min-$k$-loss) and quantile-based methods for corrupted linear systems, we propose and analyze a general loss-filtering framework -- Quantile-\(k\)-Loss SGD (Q\(k\)L-SGD) -- that samples \(k\) component losses at each iteration and updates using an index chosen uniformly from the lower empirical \(q\)-quantile. We prove linear convergence of this family of methods under standard convexity assumptions, requiring the sample size to scale with the number of corruptions and a subset strong-convexity threshold. For the cases when large enough sampling is impossible or undesirable, we give a complementary small-sample probabilistic analysis that covers any sample size $k$ and the convergence behavior depends on the probability of selecting an outlier and on the curvature of the selected good step. Experiments on polynomial regression, regularized logistic regression, and regularized hinge loss show that intermediate quantiles often outperform both standard SGD and min-\(k\)-loss SGD. In particular, min-\(k\) often stalls by repeatedly selecting nearly solved components, while intermediate quantiles retain robustness and produce more informative updates.

---


### 189. [DynSHAP: Towards Explainable Dynamic Survival Analysis](https://arxiv.org/abs/2609.13042)

**<font color=#1a73e8>作者：</font>** Nastasya Anokhina, Jonas Jürß, Pietro Liò  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models for dynamic survival analysis (DSA) achieve strong predictive performance by incorporating longitudinal patient data, but their black box nature limits clinical trust and adoption. Existing explainability methods cannot handle longitudinal, irregular inputs and functional survival outputs simultaneously, which limits their usability in DSA. We propose DynSHAP, a SHAP framework suited specifically for dynamic survival analysis. It extends common marginal SHAP estimators to this setting by treating time--feature pairs as players in the Shapley game. We further introduce Temporal DynSHAP, which learns linear dependencies in features over time and uses conditional sampling to address them in explanations. When applied to synthetic data with known ground-truth attributions, Temporal DynSHAP recovers temporally dependent features more accurately than marginal estimators for a given state-of-the-art model. Applied to two real-world clinical datasets and two DSA architectures, DynSHAP produces attributions faithful to model learning, allowing medical experts to see which patient information drove the prediction and when.

---


### 190. [Unified CT and MRI Pancreas Segmentation for Label-Efficient Cross-Modality Subregion Transfer](https://arxiv.org/abs/2609.13043)

**<font color=#1a73e8>作者：</font>** Ziliang Hong, Hongyi Pan, Halil Ertugrul Aktas 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust medical image segmentation across imaging modalities is challenging because of large differences in appearance and intensity distributions. Models trained on a single modality often show substantial performance drops when applied to unseen domains. In this work, we develop a unified 3D pancreas segmentation framework that applies domain-adversarial learning to 4,604 heterogeneous CT and MRI scans to learn anatomical representations. A shared nnU-Net encoder-decoder is trained for whole-pancreas segmentation, with a latent domain discriminator encouraging CT-MRI feature alignment. The learned encoder is subsequently transferred to pancreatic head-body-tail segmentation using limited MRI-only subregion annotations. An average Dice score of 87.31% on the in-distribution test set and Dice scores ranging from 84.20% to 88.09% across external OOD datasets were achieved in whole pancreas segmentation. Dice scores of 80.53% on MRI and 83.05% on CT were achieved for downstream subregion segmentation, without using CT subregion annotations. These results demonstrate that a unified anatomical representation can support both cross-modality pancreas segmentation and label-efficient downstream transfer.

---


### 191. [Robust Policy Optimization via Adversarial Importance Sampling](https://arxiv.org/abs/2609.13044)

**<font color=#1a73e8>作者：</font>** Amine Andam, Jamal Bentahar, Mustapha Hedabou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Significant progress has been made in safeguarding deep reinforcement learning (DRL) policies against input perturbations. Developing robust DRL involves three main stages: algorithm design, implementation, and evaluation. In this work, we identify and address a key limitation at each stage. First, we introduce Adversarial Importance Sampling (Advis), a method that uses importance sampling over trajectories from standard training to estimate and optimize verifiable worst-case returns. Advis satisfies three desirable criteria not jointly achieved by prior work: it requires no additional environment interactions, no auxiliary networks, and captures long-term robustness. Second, we introduce advrl, a modular PyTorch library that provides clean, single-file implementations of existing robustness methods and adversarial attacks, facilitating rapid prototyping and enabling reproducible and traceable evaluations. Third, we revisit evaluation under learned adversaries and show that optimal adversarial hyperparameters do not transfer across agents, which can lead to an overestimation of robustness when using a limited set of attacker configurations. Accordingly, we evaluate policies against a large and diverse set of attackers, using 6-14x more configurations than prior work. Finally, we evaluate our approach on continuous control environments, demonstrating its effectiveness relative to existing baselines. The code is available at: this https URL

---


### 192. [Diffusion Models and Concept Formation](https://arxiv.org/abs/2609.13047)

**<font color=#1a73e8>作者：</font>** Zekun Wang, Karthik Singaravadivelan, Christopher J. MacLellan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humans organize knowledge into a taxonomy of concepts with nested levels of abstraction and a \emph{basic level} at which people recognize and name objects with the least cognitive effort. Cobweb is a classic cognitive account of this ability, an incremental learner that builds a probabilistic concept hierarchy by maximizing category utility. We argue that diffusion models, although designed for image synthesis, implicitly perform the same computation. The noisy marginals of a diffusion model are Gaussian smoothings of the data distribution, and the modes of these marginals form a hierarchy that corresponds to a Cobweb tree of probabilistic prototypes in four respects. Both are hierarchical density models, both are hierarchical-Bayesian models with Gaussian prototypes, both treat categorization as score-following that reduces uncertainty, and in both a basic level emerges. We locate this basic level for a diffusion model at an intermediate noise level, where recent analyses show that the reverse process commits to the class identity of a sample. The two models differ mainly in how they represent and learn the taxonomy. Cobweb learns a discrete tree incrementally, whereas a diffusion model encodes a continuous, interpolable hierarchy in a single learned score field fit to the data distribution. We test the correspondence on MNIST and Fashion-MNIST by recovering the diffusion hierarchy through mode-finding and comparing the basic levels of the two models. This reframes diffusion as a cognitive model of concept formation and offers Cobweb a continuous, scalable instantiation.

---


### 193. [MCRL2: Multi-resource Cross-attention-based Representation Learning-augmented Reinforcement Learning for Cloud Microservice Scheduling](https://arxiv.org/abs/2609.13048)

**<font color=#1a73e8>作者：</font>** Tiangang Li, Shi Ying, Xiangbo Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient microservice scheduling is crucial for maintaining load balance across nodes in data centers and ensuring high quality of service. However, achieving this in practice remains challenging due to dynamic resource imbalance under fluctuating workloads, nonlinear coupling across multiple resource dimensions, and the heterogeneity of microservice resource demands. While reinforcement learning-based approaches have shown promise, they struggle to capture the complex interdependencies among heterogeneous resources and neglect the importance of learning informative system representations. To address these limitations, we propose MCRL2, a novel reinforcement learning approach augmented with multi-resource cross-attention-based representation learning for microservice scheduling. Specifically, we first propose MCRL, a novel representation learning approach that captures structured and informative interactions among nodes, resources, and microservices via a multi-resource cross-attention mechanism. Then, MCRL2 augments reinforcement learning through MCRL-enhanced actor-critic architecture combined with a maximum entropy objective, improving system state expressiveness and leading to more stable and effective scheduling decisions. Extensive experiments on real production cluster traces demonstrate that MCRL2 significantly outperforms existing baselines in load balancing, scheduling success rate and average completion time across diverse workload patterns.

---


### 194. [A Unified and Constrained View of Regularization-Based Robust Reinforcement Learning](https://arxiv.org/abs/2609.13050)

**<font color=#1a73e8>作者：</font>** Amine Andam, Jamal Bentahar, Mustapha Hedabou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Regularization-based methods have become a standard approach for training Deep Reinforcement Learning policies against adversarial input perturbations. In this paper, we unify these methods by deriving new upper bounds on the performance gap between the nominal and worst-case policies. Each upper bound is expressed as an existing regularization objective plus a KL-divergence penalty between the nominal and worst-case policies, which further explains why adding a KL penalty improves robustness in practice. Building on these bounds, we formulate robust training as a constrained optimization problem, showing that existing methods correspond to the special case of a fixed Lagrange multiplier. We instead update the multiplier jointly with the policy to automatically tune the regularization weight. Finally, we conduct extensive adversarial evaluations across several continuous control tasks to validate our theoretical analysis.

---


### 195. [Benign Loss Landscapes Can Coexist with Worst-Case Hardness](https://arxiv.org/abs/2609.13057)

**<font color=#1a73e8>作者：</font>** Zach Furman, Stephan Wäldchen, Yangda Bei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks are expressive enough to contain worst-case targets that can be evaluated in polynomial time but cannot be learned in polynomial time by gradient descent. For practical tasks they nonetheless learn well, raising the question of what non-generic structure of real-world targets enables this. Existing surrogate models cannot pose this question because they either lack hard-to-learn targets entirely (deep linear networks) or cannot evaluate such targets efficiently (kernel methods, infinite-width limits). We study tree tensor networks (TTNs), a model class that generalizes deep linear networks and Tucker decompositions. We show they embed arbitrary read-once Boolean formulas, and thus contain polynomial-size targets that cannot be learned by gradient descent in polynomial time under the same mechanism as neural networks. Despite this, we prove that their loss landscapes are conditionally benign for every realizable target: every local minimum that is minimum-norm is global. Thus, surprisingly, bad local minima are not what distinguishes between typical and worst-case problems in TTNs. Instead, learning difficulty in TTNs can arise from high-order degenerate saddle points, which we show are caused by rank-deficiency. This is explored through a case study of the parity function, illustrating the potential for TTNs to relate landscape geometry to computational hardness.

---


### 196. [Continue, Adapt, or Yield: In-Turn Adaptation to Overlapping Speech in Full-Duplex Agents](https://arxiv.org/abs/2609.13117)

**<font color=#1a73e8>作者：</font>** Yunqi Lu, Tyler Baumgartner, Nikhil Johri 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex evaluation often emphasizes whether an agent keeps speaking or stops. That binary cannot express a third response humans use routinely: continuing to speak while incorporating what the listener just contributed. The contribution may be a missing word, a correction or a clarification. We introduce Duplex Cue, an evaluation of this \emph{in-turn adaptation} in full-duplex voice agents. Duplex Cue separates listener intent (backchannel, collaboration, or interruption) from speaker behavior: continuing unchanged, adapting within the turn, or yielding. Adaptation includes acknowledgment as well as content revision. In a single-model case study using 300 human-confirmed cues from unscripted English conversations, we compare recorded human responses with PersonaPlex continuations generated while replaying the listener's audio. We retain 208 pairs with the ongoing speaker active at cue onset and a scorable response in each condition. On the 66 collaborative pairs, recorded speakers adapt in 68.2\% of cases, compared with 34.8\% for PersonaPlex. The model otherwise continues unchanged (42.4\%) or yields (22.7\%). These findings show why evaluating natural voice interaction requires measuring how an agent responds to a listener's contribution as well as whether it keeps speaking.

---


### 197. [CMA-OT: Hierarchical Expert Supervision for Dance-to-Music Generation](https://arxiv.org/abs/2609.13118)

**<font color=#1a73e8>作者：</font>** Jinting Wang, Chenxing Li, Dong Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dance-to-music (D2M) generation aims to synthesize music that is rhythmically and stylistically aligned with dance videos. A key challenge arises from the semantic mismatch between sparse dance cues, such as rhythm and style, and the dense information required for music composition, including structure, instrumentation, and expressive dynamics. Existing methods typically rely on these sparse cues and supervise only the final audio output, resulting in poorly learned music representations and generated music with limited musicality and structural coherence. To address these issues, we propose Curriculum-guided Multi-scale representation Alignment with scale-aware Optimal Transport (CMA-OT), a novel paradigm that leverages an external music expert to provide hierarchical supervision for the generator's latent features, bridging the semantic gap and enhancing representation learning. To effectively incorporate hierarchical supervision, we introduce a curriculum-guided multi-scale learning strategy that progressively transfers musical knowledge from the expert to the music generator, enabling stable and effective representation learning. Moreover, to accommodate the semantic and structural variations across different expert scales and achieve fine-grained alignment under temporal mismatch, we propose a scale-aware optimal transport alignment mechanism, which models soft correspondences between hierarchical expert representations and the generator's latent features. Extensive experiments on two datasets demonstrate that CMA-OT achieves state-of-the-art performance in rhythmic synchronization, perceptual quality, and overall music generation.

---


### 198. [A Hybrid LSTM-XGBoost Framework for Multi-Horizon Stock Return Prediction Across Diversified Equity Portfolios](https://arxiv.org/abs/2609.13125)

**<font color=#1a73e8>作者：</font>** Seif ElDein Mostafa, Yahia Ahmed, Farah Datwish 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of equity returns remains a major challenge in computational finance due to the non-stationary, nonlinear, and low signal-to-noise ratio nature of financial time series. This paper proposes a hybrid two-stage architecture that combines a long short-term memory (LSTM) network with an XGBoost gradient-boosted regressor for multi-horizon stock return prediction across a diversified panel of 14 U.S. equities spanning six industry sectors. The LSTM component, comprising two stacked layers with 64 hidden units, processes 60-day sliding windows of five sequential market features to produce 64-dimensional temporal embeddings that encode learned sequential market dynamics. These embeddings are concatenated with 14 hand-crafted technical indicators to form a 78-dimensional hybrid feature vector, which is subsequently passed to an XGBoost regressor tuned via 3-fold cross-validation grid search. The framework is trained on a multi-stock pooled corpus using strict chronological splits and per-stock MinMaxScaling to prevent look-ahead bias, and evaluated across four prediction horizons of 30, 90, 252, and 365 trading days. Experimental results demonstrate that the hybrid model achieves a test RMSE of 0.0949 on the 30-day horizon, roughly one-third that of the standalone LSTM baseline, while marginally matching or surpassing the XGBoost-Only baseline across the majority of stocks. Directional accuracy rises with horizon length, reaching 97.6% at 365 days; we show, however, that this largely tracks the high base rate of positive long-horizon returns in the sample, and we therefore benchmark directional accuracy against a naive always-positive predictor and treat the above-base-rate gap at short horizons as the more informative signal. A composite investment scoring framework derived from multi-horizon predictions is further proposed to support portfolio ranking and decision support.

---


### 199. [From Review to Reuse: How Post-Task Workflow Can Support Human-AI Agent Interaction](https://arxiv.org/abs/2609.13136)

**<font color=#1a73e8>作者：</font>** Zekun Wu, Xinru Wang, Rock Yuren Pang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI agents can automate tasks by turning a single natural-language request into a multi-step process spanning tools, files, and applications. Users are often left to judge that process from fragmented execution information and the final output. To make the completed process easier to understand, validate, and reuse, we investigate post-task workflows: editable, graph-based representations of an agent's completed execution. We first analyzed 10,803 public workflow templates from n8n to characterize real-world automation practice, then developed Trace2Flow, a research probe that translates agent execution traces into interactive post-task workflows. In a study, participants (N = 20) reviewed agent executions with prompt or agent errors. We found that post-task workflows improved their understanding and error detection over a prompt-only condition, and that validation succeeded mainly when users cross-checked across multiple evidence sources. For follow-up tasks, adapting the workflow matched adapting the prior prompt in success, time, and difficulty, and was often preferred.

---


### 200. [SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking](https://arxiv.org/abs/2609.13141)

**<font color=#1a73e8>作者：</font>** Zhiwei Li, Lei Zhu, Hao Gu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training attention sparsification reduces the quadratic cumulative attention cost of pretrained Transformers by selecting a small set of context units (tokens or blocks) for each query. Existing trainable methods usually use a lightweight selector to score context units, followed by hard Top-K selection that blocks gradients from the language modeling loss. Consequently, these methods commonly distill layer-wise dense attention distributions. Although this encourages the selector to rank context units by dense attention weights in the original model, the ranking is not directly aligned with their impact on predictions under a fixed attention budget (i.e., the number of attended context units per query), potentially wasting the limited budget on less useful units. To address this misalignment, we propose Simple Attention Sparsification (SAS), a gated sparse attention mechanism that optimizes context ranking end-to-end with the language modeling loss. The key idea is to inject the selector's continuous scores into attention logits during training, allowing the loss to update the selector through standard backpropagation. We identify several choices crucial for this simple design to work well in practice: placing the gate inside the attention softmax in log form, using normalized softmax gates to calibrate historical context against the always-retained current block, and preserving continuous selector scores so the model learns relative priorities rather than only hard selections. To support long-sequence training, we implement a memory-efficient Triton kernel that integrates SAS into FlashAttention-style computation. Across reasoning, long-context understanding, and agentic tasks, SAS consistently outperforms trainable sparse attention baselines across attention budgets, with especially large gains under tight budgets, demonstrating more effective context ranking for downstream tasks.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-201](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
