# 📦 其他研究 | 2026年07月01日

> 本类共 **489** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

---

### 201. [The Role of Online Forums in Developer Understanding of Privacy Law -- A Reddit Case Study](https://arxiv.org/abs/2606.29393)

**<font color=#1a73e8>作者：</font>** Sara. Haghighi, Clark LaChance, Ali Pourghasemi Fatideh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software practitioners use online forums to navigate complex and often ambiguous legal privacy requirements, yet little is known about their professional backgrounds, what challenges they face, and how they use and assess the credibility of the advice received, or how they resolve ambiguities in posts. We report the findings of a survey of 223 Reddit users from regulatory-focused subreddits, complemented by a qualitative analysis of 2,248 posts and responses. Our results show that, despite holding privacy-related certifications, most participants frequently use forums to seek legal advice. Key challenges reported or identified include implementing a data protection impact assessment, reporting a data breach, and obtaining cookie consent. Reddit users often assess credibility by reviewing respondents' post history, verifying sources cited, trusting advice from recognized experts, and following up for clarity before responding. We highlight research and educational directions to bridge gaps in support needed for regulatory compliance guidance.

---


### 202. [Learning to Adaptively Allocate Gaussians for Arbitrary-Scale Image Super-Resolution](https://arxiv.org/abs/2606.29400)

**<font color=#1a73e8>作者：</font>** Giulio Federico, Giuseppe Amato, Claudio Gennaro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In computer graphics, visual content is continuously warped, zoomed and resampled. This occurs when engines upscale frames, users zoom into 3D scenes, or foveated VR applies varying scaling. Handling these transformations requires Arbitrary-Scale Super-Resolution (ASR). Traditional models, designed for fixed scales, typically predict at a lower integer scale (e.g., x4) and rely on sub-optimal interpolation for continuous resolutions, compromising quality. Furthermore, most methods process pixels uniformly. Since fine details are sparse, this creates overhead; efficiency dictates concentrating resources only where structural complexity demands it. While implicit models and Gaussian Splatting (GS) enable continuous representation, GS is advantageous due to adaptive densification. However, transitioning GS into a feed-forward model for ASR is non-trivial. Standard GS optimization needs high-resolution gradients to drive primitive growth, which are unavailable during inference. Thus, the network must autonomously predict GS densification from low-resolution inputs. To solve this, we propose QuADA-GS. After encoding inputs into a latent space, a Neural Routing Architecture evaluates local complexity to distribute a global budget, assigning specific upsampling factors to features to avoid redundant processing. Features are dynamically densified based on these factors, forming an irregular topology decoded into 2D Gaussian primitives. To coordinate features before decoding, we introduce Hierarchical Pointer Convolution. This non-grid operator achieves O(1) neighbor lookup complexity, facilitating efficient spatial communication and bypassing dense bottlenecks. Experiments show QuADA-GS achieves state-of-the-art ASR performance, maintaining low latency and a lean memory footprint.

---


### 203. [FiRe: Frequency Reparameterization as a Preconditioner for Periodic Implicit Neural Representations](https://arxiv.org/abs/2606.29414)

**<font color=#1a73e8>作者：</font>** Harinandan Shukla, Rajarshi Verma, Jitin Singla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Periodic Implicit Neural Representations (INRs) such as SIREN and FINER assign every neuron, the same global frequency, spending the representational budget inefficiently when local signal content varies. We introduce FiRe (Frequency Reparameterization), that accelerates optimization by reparameterizing per-neuron frequency of periodic INRs without changing their underlying activation function. FiRe gives each neuron a bounded, input-dependent frequency via a separate low-rank gating path and is applicable to any periodic activation function. The gate acts as an implicit preconditioner that improves optimization conditioning at initialization via the Neural Tangent Kernel (NTK). This better-conditioned initialization makes optimization converge faster, and the high-frequency content of the reconstruction tracks the target more closely at a fixed computational budget. On 2D image fitting, FiRe increases PSNR over a parameter-matched baseline (up to +1 dB at short training budgets), with gains that vary with resolution and diminish at full convergence. We characterize how performance depends on resolution, rank, and training budget, and give an NTK account that predicts these trends.

---


### 204. [Can Machines Really See Objects in Images? A Study Based on Syntactic Distance and Visual Self-Referential Instances](https://arxiv.org/abs/2606.29416)

**<font color=#1a73e8>作者：</font>** Xingyu Peng, Junran Wu, Yue Hou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can a vision model truly see an object, or does it only fit surface-level visual cues? Following Wittgenstein's view that the limits of language are the limits of the world, we view a model's recognition ability as bounded by the descriptive system it has learned. In current vision models, this system is often realized through learned feature representations that exploit local statistical cues. We therefore ask whether a model can still classify correctly when such local cues provide no stable basis for distinction. We formalize this question with syntactic distance, which measures class separability through the symmetry of the operations mapping one class to the other: positive distance exposes exploitable local features, whereas zero distance requires global semantics rather than local rules. We construct a visual self-referential task in maximum-variance binary noise: positive samples contain a closed square, while negative samples contain an otherwise identical square with one flipped boundary pixel. The two classes differ in global semantics but have zero syntactic distance, making local statistical shortcuts unreliable. Experiments on ResNets and Vision Transformers reveal a consistent phase-transition phenomenon, with accuracy collapsing to random guessing once the image scale crosses a critical point and does not recover within the tested range. Larger training sets and models only delay this collapse, while globally attentive ViTs reach it earlier. These results reveal a structural capability boundary of current architectures on global-concept tasks, suggesting that general intelligence may require creating new language, not reusing an existing one.

---


### 205. [Temporal Posed and Spontaneous Gesture Recognition from Electromyography in the Rock-Paper-Scissors Game](https://arxiv.org/abs/2606.29423)

**<font color=#1a73e8>作者：</font>** Xin Wei, Huakun Liu, Felix Dollack 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The importance of gesture recognition has been acknowledged in many domains requiring real-time recognition systems. Two requirements for these are fast recognition in multiuser contexts. Therefore, we explored the temporal characteristics of electromyography (EMG) and its accuracy in recognizing gestures in a Rock-Paper-Scissors (RPS) game. Twenty-four participants played RPS in dyads, while a two-channel EMG was recorded from the forearm. We found out that EMG onsets could be detected at least 800 ms before the gesture's visible onset, and that the EMG peaks around 342 ms before the visible onset of the gesture. Furthermore, we evaluated self-gesture recognition in both posed and spontaneous gesture conditions. The mean accuracy for posed gestures reached 63.4%. The model trained on posed gestures achieved 53.6% for spontaneous gestures, with considerable variation across individuals. We also checked whether detecting a player's gesture from the opponent's EMG was possible. The peak mean accuracy was 65%, peaking at 2082 ms after the visual onset of the gesture. This suggests that the opponent's reaction to an observed gesture contains information about the observed gesture due to the dynamics of the interactions while playing. The temporal predictive advantage of EMG signals, where muscle activation precedes observable movement, offers potential benefits for applications requiring rapid intent recognition, such as human-computer interaction and assistive technologies. Future work should focus on refining onset detection and reducing the impact of spontaneous movement variability across conditions to improve recognition performance in dynamic and real-world environments.

---


### 206. [EntroRouter: Learning Efficient Model Routing via Entropy Regulation](https://arxiv.org/abs/2606.29424)

**<font color=#1a73e8>作者：</font>** Kaiyi Zhang, Xueliang Zhao, Zhuocheng Gong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model routing balances solution accuracy and computational cost by selecting among models of varying capabilities. While recent multi-round frameworks interleave reasoning and planning, we identify a structural failure mode termed Trust Region Collapse. We demonstrate that the deep coupling of reasoning and routing, exacerbated by the dominance of strong pre-training priors under sparse supervision, leads to degenerate local optima where capable experts are systematically suppressed. To decouple these processes, we propose $\textbf{EntroRouter}$, a single-round routing framework that treats entropy regulation as a core objective. We first initialize the policy via Soft Supervision, fitting a distribution of suitable models to establish a high-entropy prior for exploration. Subsequently, we stabilize Reinforcement Learning using a Soft Anchor, which utilizes offline capability estimates to orchestrate controlled entropy contraction within a safe trust region. Extensive experiments demonstrate that EntroRouter retains 98.3% of the strongest expert's accuracy while reducing computational costs by 48.25%.

---


### 207. [Mixture of Debaters: Learn to Debate at Architectural Level in Multi-Agent Reasoning](https://arxiv.org/abs/2606.29425)

**<font color=#1a73e8>作者：</font>** Dayong Liang, Kaisong Gong, Yi Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing multi-agent debate frameworks suffer from two critical limitations: they rely on static architectures where agent roles and coordination patterns are fixed at design time, and they require instantiating multiple model copies, incurring substantial computational overhead. We propose Mixture of Debaters (MoD), a unified framework that enables dynamic self-debate within a single model by leveraging the Mixture-of-Experts paradigm. We address three key challenges in adapting MoE for dialectical reasoning: (1) dual-routing that decouples role allocation from process flow, dynamically determining when to debate versus when to synthesize; (2) momentum switching that smooths token-level routing with local context, reducing expert-switch jitter; and (3) unified self-debate that encapsulates diverse debating personas into lightweight expert modules, eliminating inter-agent communication while preserving behavioral diversity. Extensive experiments on multimodal benchmarks demonstrate that MoD outperforms both single-model baselines and conventional multi-agent systems, achieving superior accuracy with 3.7x lower latency and 87% reduction in token this http URL source code can be accessed at this https URL.

---


### 208. [Robust Zero-shot Anomaly Detection under Limited Auxiliary Anomaly Priors](https://arxiv.org/abs/2606.29428)

**<font color=#1a73e8>作者：</font>** Guanyu Lu, Fang Zhou, Cheqing Jin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot anomaly detection aims to identify defects in arbitrary novel domains; however, existing models assume that the auxiliary data contains a rich diversity of anomalies, neglecting the far more complex and unpredictable variations in real-world target domains. This study introduces DIVE, the first approach to investigate the scenario of limited auxiliary anomaly priors and resolve the resulting substantial performance degradation. Through a shallow-and-deep text embedding injection strategy during visual encoding, DIVE learns to abstract generic anomaly concepts shared across the auxiliary training domain and diverse target domains. Moreover, we propose a disentanglement mechanism to tackle the suboptimal alignment between visual embeddings entangled with object semantics and object-agnostic textual prompts. Experiments demonstrate that, under the setting of limited anomaly patterns in auxiliary data, DIVE outperforms SOTA baselines by up to 16.2% and 28.5% on two classification metrics, and 23.4%, 24.1%, and 47.0% on three segmentation metrics, in terms of average performance across twelve datasets. Furthermore, it maintains highly competitive performance when auxiliary data exhibits sufficient anomaly diversity.

---


### 209. [EvLIR: Learning Illumination Residuals from Ordered Events for Low-Light Image Enhancement](https://arxiv.org/abs/2606.29430)

**<font color=#1a73e8>作者：</font>** Haoxian Zhou, Chuanzhi Xu, Langyi Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light image enhancement is severely ill-posed when the input frame contains missing structure, saturated noise, and weak local contrast. Event cameras provide asynchronous brightness-change observations with high temporal resolution, but prior works often treat voxel channels as an unordered or static feature stack before fusion, rather than explicitly modeling their within-window temporal evolution, weakening the temporal evidence that makes events useful. We propose EvLIR, a temporal-residual enhancement framework that learns illumination residuals from ordered events for low-light image enhancement. Given a low-light frame and its aligned event voxel, EvLIR preserves the ordered temporal bins of the event stream and introduces a Temporal Event Residual Module (TERM) to encode short-window event dynamics with a lightweight ConvGRU. The resulting temporal state is converted into a bounded illumination correction, which provides spatially adaptive photometric guidance for Retinex-style illumination estimation and subsequent reliability-aware image-event restoration. On SDE and SDSD indoor/outdoor benchmarks, EvLIR achieves the best result on eleven of twelve dataset-metric pairs, with average scores of 25.63~dB PSNR, 28.30~dB PSNR*, and 0.827 SSIM across the four benchmarks.

---


### 210. [Randomized neural operator for parametric PDEs with fast training and conformal uncertainty quantification](https://arxiv.org/abs/2606.29440)

**<font color=#1a73e8>作者：</font>** Zirui Deng, Jingbo Sun, Deyu Meng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Repeatedly solving parametric PDEs is essential for uncertainty quantification, design optimization and inverse problems, but conventional neural operators require expensive non-convex training. We introduce PCA--RaNN, a randomized latent neural operator that combines PCA-based dimensionality reduction with fixed random features and a closed-form least-squares readout. It recasts latent operator learning as fixed-feature linear regression, reducing training time by one to three orders of magnitude across benchmarks while maintaining competitive accuracy. We introduce an energy-matched scaling rule and a lightweight two-parameter BFGS refinement to correct suboptimal feature scales. Ensemble averaging reduces predictive variance. On Burgers, Darcy, Navier--Stokes and backward heat equation benchmarks, PCA--RaNN provides a favorable speed--accuracy trade-off against operator-learning baselines. The ensemble supports split-conformal prediction intervals, and the linear readout enables rapid online adaptation via recursive least squares without retraining hidden features. This provides an efficient, uncertainty-aware surrogate for many-query scientific workflows.

---


### 211. [Miti360: A Comprehensive Dataset for Improved Reforestation Monitoring](https://arxiv.org/abs/2606.29447)

**<font color=#1a73e8>作者：</font>** Cedric Kiplimo, Samuel Mbatia, Ciira wa Maina 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Over the past decade, interest in applying machine learning (ML) to automate forest monitoring has grown significantly. However, existing training datasets are predominantly drawn from North America, Europe, Asia, and Australia, leaving a critical gap in African forestry data. To address this limited geographic diversity, we present Miti360, a comprehensive dataset for reforestation monitoring that comprises high-resolution imagery, ground truth data, and longitudinal weather data. Data collection occurred within a 770-ha reforested section of the Kieni Forest in Kenya between March 2023 and February 2025. Miti360 comprises aerial photos (orthophotos and tiles) with tree bounding box annotations, terrestrial images (single and stereo), and detailed data records including tree biophysical parameters, species, and GPS coordinates, alongside historical weather data. Aerial surveys utilized a DJI Mavic 2 Pro, with imagery stitched via Agisoft Metashape and tiled using ArcGIS Pro, while terrestrial captures used smartphones and custom stereo cameras. Miti360 enables the training of ML systems for tasks such as accelerating tree censuses, matching species to geographical areas, modelling growth based on weather conditions, and developing digital twin frameworks. Models can be trained on Miti360 to address challenges specific to Sub-Saharan Africa, ultimately advancing reforestation monitoring and fostering sustainable forestry practices in underrepresented regions. We demonstrate the utility of this dataset by successfully tracking tree crowns across three years and improving the DeepForest model's box precision and box recall by 12% and 69% respectively through fine-tuning on Miti360.

---


### 212. [Resonant Brane Splatting for Arbitrary-Scale Super-Resolution](https://arxiv.org/abs/2606.29453)

**<font color=#1a73e8>作者：</font>** Giulio Federico, Giuseppe Amato, Claudio Gennaro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Arbitrary-Scale Super-Resolution (ASR) reconstructs images at continuous magnification factors. Recent methods accelerate inference by replacing computationally heavy implicit neural decoders with explicit 2D Gaussian Splatting (GS). However, since standard Gaussians are smooth low-pass primitives, modeling edges and fine textures requires multiple overlapping, well-aligned splats, which creates severe bottlenecks during rasterization. To address this, we introduce Resonant Brane Splatting (RBS), a feed-forward ASR framework. RBS replaces flat Gaussians with Branes: expressive primitives that emit spatially varying colors to natively model local contrast and complex textures within a single footprint. We achieve this by augmenting the standard Gaussian envelope with internal Gaussian-Hermite modes, assigning a distinct color coefficient to each. The zero-order mode recovers standard GS, while higher-order modes capture high frequencies. We predict Brane parameters directly from low-resolution features. Because Branes provide a mathematically richer formulation than simple Gaussians, far fewer primitives need to overlap to reconstruct a given target pixel. To exploit this, we introduce an efficient fully differentiable rasterizer with a precise culling strategy based on the classical quantum turning point. This allows us to safely skip negligible regions, drastically reducing the rendering overhead. Experiments on standard ASR benchmarks show that RBS improves reconstruction quality over implicit and GS baselines, while achieving superior speed-quality trade-off than prior GS methods.

---


### 213. [How Much Due Diligence Before You Bid? Learning in Intractable Takeover Auctions](https://arxiv.org/abs/2606.29457)

**<font color=#1a73e8>作者：</font>** Zain Naboulsi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When two companies bid to buy the same target, no one knows exactly what the target is worth. Each bidder pays for due diligence: costly, imperfect homework that sharpens its own private estimate before it bids. How much of that homework is worth buying? We build a simple computer model of the bidding contest and let it teach itself to bid well by playing against itself, the way a game engine learns chess. The economic question, how much diligence pays for itself, and the computational question, when the contest becomes too complex to solve exactly, are both controlled by a single thing: how many pieces of private information a bidder carries. Our main finding is that the right amount of diligence is modest and finite. It falls as diligence gets more expensive, and it falls further when both sides are doing their homework, because competition erodes the value of knowing more. We also test a recent claim from AI research: that simple, general self-play methods can rival the specialized, expensive algorithms usually built for games like these. Running on an ordinary laptop with no costly frontier AI, we find the simple methods are the best of the self-learning approaches, though purpose-built exact methods still win whenever the game is small enough to solve outright. The simple methods earn their keep only once the game grows too large to solve exactly, which is the regime real deals live in, and there we show they still find strong bidding strategies. The contribution is threefold: a cheap, reproducible way to study deal-making under uncertainty; a concrete, model-based answer to how much due diligence is worth buying; and evidence about when lightweight, general-purpose AI is good enough to replace specialized methods. We release all the games, code, and experiments.

---


### 214. [From Phase to Phenomenon: Self-Supervised Learning of Subsurface Scattering with Minimal Phase-shift Inputs](https://arxiv.org/abs/2606.29461)

**<font color=#1a73e8>作者：</font>** Arjun Majumdar, Raphael Braun, Andreas Engelhardt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a self-supervised pretraining framework for learning sub-surface scattering (SSS) light transport representations from minimal input. Our method leverages a stereo projector-camera setup that captures only eight high-frequency phase-shift profilometry (PSP) images per view to pretrain an encoder in a multi-view, multi-object setting. We introduce a tailored augmentation strategy for PSP-based SSS data, and show that it significantly outperforms standard ImageNet-style augmentations for SSL pretraining. The pretrained encoder learns generalizable SSS representations that transfer effectively to downstream tasks, including spatially varying relighting and representation evaluation using a kNN classifier. Combined with a decoder, the model reconstructs dense scattering footprint responses, trained using a dedicated cost function that improves accuracy, particularly for anisotropic footprints. Despite using only eight input images per view, our approach generalizes to unseen objects with complex geometry and material properties, achieving high-fidelity reconstructions while requiring orders of magnitude fewer images than prior methods.

---


### 215. [CellDETR: A Detection-Guided Framework for Scalable Cell Representation Learning from Histopathology Images](https://arxiv.org/abs/2606.29463)

**<font color=#1a73e8>作者：</font>** Shikang Zhang, Guojun Li, Yicong Mao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in pathology foundation models have substantially improved patch and slide level representation learning from whole-slide images (WSIs).However, cell-level representations learning remain underexplored, limiting cell resolved interpretability, biological discovery, and clinical translation. We propose CellDETR, a detection-guided framework built on Deformable DETR for scalable cell representation learning from WSIs. By introducing location feature decoupling and box-constrained attention mechanism, CellDETR enables automated extraction of cell-level embeddings, and outperform existing state-of-the-art methods in supervised cell classification on PanNuke data. In addition, by incorporating contrastive learning design, we build a CellDETR-based pretraining model for scalable cell representation learning from unlabeled WSIs, which improves downstream cell classification performance. Furthermore, we show that after pretraining with Xenium spatial transcriptomics-derived cell annotations, CellDETR achieves accurate cross-dataset cell classification, demonstrating the transferability and biological relevance of the learned cell embeddings. Together, CellDETR provides a scalable route toward general cell-level representation learning framework for interpretable computational patholog

---


### 216. [Self-Supervised Calibration of Scientific Instruments Using Physical Consistency Constraints](https://arxiv.org/abs/2606.29466)

**<font color=#1a73e8>作者：</font>** M. Rejmund, A. Lemasson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Calibration remains one of the principal obstacles to the deployment of machine learning in scientific instrumentation because it typically relies on expert intervention, dedicated procedures, and manually labelled data. We introduce a physics-informed self-supervised framework that jointly learns latent detector calibration parameters and task-specific predictions directly from raw measurements without requiring pre-calibrated signals or external labels. The method exploits known physical constraints to generate pseudo-labels iteratively, transforming calibration into a self-supervised optimization problem. The approach is demonstrated for ionic charge-state determination in the VAMOS++ magnetic spectrometer, where the calibration of a segmented ionization chamber and the inference of ionic charge states are learned simultaneously. Starting from a weak prior on the mean ionic charge state, the model progressively refines its predictions through iterative fractional pseudo-labelling driven by the discrete nature of atomic masses. Beyond accurate ionic charge-state reconstruction, the inferred calibration coefficients provide a compact representation of the detector state that enables automated monitoring of gain drifts, pressure variations, and detector aging. The resulting labels can subsequently be transferred to specialized models that quantify detector imperfections and track their spatial and temporal evolution. These results establish a general paradigm for self-calibrating and self-monitoring scientific instruments and represent a step toward intelligent experimental systems capable of autonomous calibration, analysis, and performance optimization.

---


### 217. [Structured Proper Loss Geometries for Multiclass Classification: Theory and Controlled Empirical Evaluation](https://arxiv.org/abs/2606.29471)

**<font color=#1a73e8>作者：</font>** Soumyadip Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Strictly proper scoring rules identify the true conditional class distribution at population level, but their curvature can alter optimization and finite-sample behavior. We study three multiclass objectives: a class-aware quadratic Bregman score (CAPM), a strongly convex generator with constrained log-cosh ridges (HPG), and an HPG objective with an annealed probability-margin penalty (APMS). CAPM is treated as a structured instance of established quadratic scoring-rule theory. We derive conditional-regret, curvature, range, and logit-gradient bounds for CAPM and HPG, and prove exact penalty-range and conditional-target displacement bounds for APMS. Controlled five-seed experiments use Digits, Wisconsin breast cancer, and synthetic confusion and long-tail problems under clean labels, symmetric and pair-flip corruption, class imbalance, calibration evaluation, input corruption, and first-order adversarial perturbations. The candidates are close to cross-entropy on clean data and show descriptive gains in some noisy-label cells, but the five-seed comparisons are interpreted descriptively rather than as significance evidence. The selected noisy-label baselines perform better on Digits with 40% symmetric label noise, and explicit prior-adjustment methods perform better in the 30:1 synthetic long-tail experiment. Ablations do not show a consistent benefit from the candidate-specific graph, ridge, or margin components. The mathematical analysis establishes the stated properties, and the experiments delimit the empirical evidence; together they do not support a claim of general superiority.

---


### 218. [Agent-Computer Observation Interfaces Enable Dynamic Computer Use](https://arxiv.org/abs/2606.29472)

**<font color=#1a73e8>作者：</font>** Bojie Li, Noah Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> SWE-agent established the action interface as an underexplored design axis for software-engineering agents; we make the analogous case for the observation interface in computer-use (CU) agents. Current CU agents, closed and open-source alike, tie observation to action--one screenshot every 3-5 s, no audio--leaving them blind and deaf between screenshots to video, animations, transient UI events, meetings, and spoken instructions. We introduce the Agent-Computer Observation Interface (AOI), a model-agnostic perception layer that decouples continuous, adaptive observation from discrete actions through three gated components: inter-step keyframe capture, volume-gated audio transcription, and CU-model-generated visual narration that persists as text. Each produces almost nothing on static, silent content, reducing to the standard loop without degrading it.
On DynaCU-Bench (100 dynamic browser tasks plus a 50-task static control), CU models from 7B to frontier scale gain +17 to +48 pp over their screenshot baselines with zero retraining, turning tasks that are near-impossible from periodic screenshots into largely solved ones. The gap is starkest on audio: on a spoken-content subset AOI agents solve every task, whereas streaming voice models hear accurately but cannot act on what they hear without the scaffold. The decomposition is as informative as the headline gain: keyframe selection turns out not to matter--the value comes from narrating captured frames into persistent text--and the interface is not a fixed bundle, since on a newer model (Gemini 3 Flash) the keyframe stream actively regresses through image-token dilution, so its components must be selected per model rather than shipped as one configuration.

---


### 219. [MAVIN: Multi-Shot Audio-Visual Generation with Narrative Control](https://arxiv.org/abs/2606.29473)

**<font color=#1a73e8>作者：</font>** Kaiqi Liu, Yunyao Mao, Ziqi Cai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent generative models produce high-fidelity videos, they struggle with the complex narrative control required for coherent multi-shot audio-visual generation. Existing methods suffer from temporal misalignment, limited controllability, and incomplete scripting. In this paper, we propose MAVIN, the first framework for multi-shot audio-visual generation with customized narrative control. To resolve temporal misalignment, we propose boundary-aware attention, which leverages hierarchical captions and boundary-aware token routing to render audio-visual elements within their respective temporal boundaries. To improve the controllability for multi-subject scenarios, we propose ID-aware propagation, utilizing identity embeddings and an identity-aware mask to bind specific identities to consistent visual appearances and vocal timbres. To provide comprehensive audio-visual narratives, we present a multi-agent scripting pipeline to transform free-form user inputs into hierarchical captions. Furthermore, we construct MAVINSet, a multi-shot audio-visual dataset for robust training and evaluation. Extensive experiments demonstrate that MAVIN achieves state-of-the-art performance, opening up a new avenue for integrating generative models into professional filmmaking workflows.

---


### 220. [To Reason or to Fabricate: Reasoning Without Shortcuts via Hint-Anchored Pairwise Aggregation](https://arxiv.org/abs/2606.29481)

**<font color=#1a73e8>作者：</font>** Jiuheng Lin, Chen Zhang, Yansong Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While reinforcement learning (RL) significantly enhances LLM reasoning, its efficacy is severely undermined by Pre-RL data overlap, where RL datasets overlap with pretraining or SFT corpora, causing models to exploit shortcuts by memorizing correct answers and fabricating post-hoc reasoning. To address this, we introduce HIPPO, a novel RL framework that integrates hint-injected aggregation with a tailored pairwise reward model. By utilizing hint injection to deliberately trigger overlap-induced behaviors, the resulting traces naturally serve as explicit anchors for pairwise comparison. This provides highly discriminable preference signals, enabling a lightweight judge model to reliably distinguish genuine reasoning deduction from shortcut-driven rationalization, while the pairwise formulation ensures stable and robust optimization compared to standard PRMs. Extensive experiments demonstrate that HIPPO yields substantial improvements over standard baselines and generalizes effectively to out-of-distribution general tasks, showing it extracts authentic, transferable reasoning skills rather than superficial shortcut patterns.

---


### 221. [The Calibrated Deepfake Trust Score (CDTS): Competence-Coupled Trust Degradation Across Deepfake Detectors](https://arxiv.org/abs/2606.29484)

**<font color=#1a73e8>作者：</font>** Md Anas Biswas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern deepfake detectors are rarely consumed as bare classifiers. In moderation, provenance, and verification pipelines their output probability is read as a degree of trust, so its calibration matters as much as raw accuracy. We reframe deepfake detection as a calibrated, self-auditing trust instrument, the Calibrated Deepfake Trust Score (CDTS), and identify what governs its trustworthiness. Our central finding is a competence-calibration coupling: the calibration of the trust score degrades as the detector's discriminative competence falls. We establish it across 32 configurations (pooled Pearson r = -0.81), demonstrate it within a single dataset, reinforce it by inducing low competence directly, and replicate it on a fourth held-out dataset the detectors never trained on. It holds across three architecturally distinct detectors, two convolutional networks and a CLIP vision transformer (r = -0.88, -0.83, -0.86). The result is also deployable: a single calibrator frozen on in-domain data fails on exactly the low-competence generators the coupling flags (its error tracks competence at r = -0.98), and competence is estimable without labels, so a label-free monitor flags calibration risk on unseen generators and routing source-batches on a reference-free competence estimate lowers overall AURC and improves the low-to-mid coverage operating region relative to confidence-based routing. The same competence factor also drives calibration inequity across demographic subgroups (distinct from accuracy inequity) and explanation faithfulness. We therefore argue that detector trustworthiness is organized by competence as a shared driver, that competence is the right quantity to estimate and condition on, and that trust scoring must be competence-aware. We offer the CDTS wrapper as the mechanism, and report openly where the unification is tight and where it is architecture-specific.

---


### 222. [Which Tokens Need Context? A Reference-Based Analysis of Translation Responsibility Using Fertility and Entropy](https://arxiv.org/abs/2606.29489)

**<font color=#1a73e8>作者：</font>** Ramakrishna Appicharla, Baban Gain, Santanu Pal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When humans translate, not every word depends equally on the surrounding context. Some tokens, particularly function words like pronouns and auxiliaries, rely heavily on preceding or following sentences, while others, such as proper nouns, do not. Understanding this inherent context sensitivity is essential for evaluating whether machine translation systems use context in human-like ways. However, existing approaches to analysing context usage rely on discourse-specific test sets or model internals, making them narrow or model-dependent. We propose a post-hoc, model-agnostic framework to quantify context sensitivity at lexical and syntactic levels using two measures derived from word alignments: fertility (number of target tokens generated per source token) and entropy (stability of fertility patterns across contexts). Using reference translations for three language pairs (German $\leftrightarrow$ English, English $\rightarrow$ Hindi) under four context conditions, we show that context selectively redistributes generative responsibility from source to context tokens without altering overall fertility. Function words show the largest fertility reductions, while content words remain stable, suggesting that context resolves ambiguity rather than adding new information. Our framework provides a ground-truth characterisation of selective context usage in human translation, establishing a diagnostic baseline for evaluating machine translation models.

---


### 223. [Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving](https://arxiv.org/abs/2606.29493)

**<font color=#1a73e8>作者：</font>** Pawan Sasanka Ammanamanchi, Siddharth Bhat, Stella Biderman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmarks for LLM-assisted theorem proving in Lean are often treated as intrinsically reliable because every solved instance comes with a machine-checked proof. However, the kernel only checks that a proof establishes a \emph{formal} statement; it does not verify that the statement faithfully encodes the intended informal problem, nor that evaluation harnesses are robust to trivial or adversarial solutions. We audit five widely used Lean theorem-proving benchmarks and their forks, using corpus-scale static checkers to surface 4,833 findings, including 398 mechanically certified issues such as counterexamples, vacuous theorems, and unsound axioms. We also document semantic defects such as missing hypotheses, problem simplification, incomplete or incorrect translations, and Lean-specific specification hazards. Beyond dataset construction, we survey evaluation-time failure modes and show, on corrected subsets, that defects can both inflate and deflate reported prover scores. We propose a fault taxonomy, a suite of automated checkers and recall-oriented semantic audit prompts, and release standards to guide the creation of formal math datasets and to make evaluation more reproducible and trustworthy. Our checkers, audit prompts, and corrected dataset snapshots are available at this https URL.

---


### 224. [VCS-SLAM: Geometry-Validated Semantic Evidence Fusion for 3D Gaussian SLAM](https://arxiv.org/abs/2606.29494)

**<font color=#1a73e8>作者：</font>** Raman Jha, Shuaihang Yuan, Yi Fang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual SLAM performance often deteriorates in complex real-world applications. Semantic 3D Gaussian SLAM commonly fuses 2D semantic priors into a persistent 3D map using uniform optimization weights. However, such priors are not equally reliable in online mapping: occlusions, unsupported semantic boundaries, and ambiguous ray geometry can introduce persistent semantic artifacts into the global Gaussian map. We propose VCS-SLAM, a geometry-validated semantic evidence fusion framework for RGB-D 3D Gaussian SLAM. Instead of treating all semantic observations as uniformly valid supervision, VCS-SLAM evaluates their geometric reliability through visibility consistency, surface-supported boundary evidence, and ray-level conflict uncertainty. The resulting reliability-aware objective suppresses occluded semantic updates, reduces unsupported semantic bleeding, and delays premature label assignment in ambiguous regions. Experiments on Replica demonstrate improved semantic consistency, boundary preservation, and reconstruction quality. Results on ScanNet further show that VCS-SLAM maintains competitive tracking performance under real RGB-D inputs

---


### 225. [Rectifying Mask via Entropy for Distractor-Free 3DGS in Ambiguous Scenarios](https://arxiv.org/abs/2606.29496)

**<font color=#1a73e8>作者：</font>** Wongi Park, Jiyeon Lim, Minjae Lee 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present RefineSplat, a systematic framework that effectively constructs transient masks to identify diverse ambiguous distractors. To do this, we qualitatively and quantitatively analyze issues and propose a novel entropy-aware adaptive masking method. Unlike existing approaches that struggle to distinguish transient elements from static scenes due to color or semantic ambiguity, RefineSplat captures ambiguous distractors leveraging entropy and instance masks. Furthermore, we propose a simple yet effective entropy-aware density control to align Gaussians in ambiguous scenarios considering Entropy-aware positional gradients. Additionally, to rigorously validate our method, we first create and release the Ambiguous wild dataset, including 18 scenes where distractors and static scenes are hard to distinguish due to color or semantic resemblances. Experimental results on various datasets demonstrate that RefineSplat shows state-of-the-art performance, showing distractor-free novel view synthesis.

---


### 226. [Learning Where and When: Patch-Based Spatiotemporal Localization in Weakly Supervised Video Anomaly Detection](https://arxiv.org/abs/2606.29498)

**<font color=#1a73e8>作者：</font>** Hamza Karim, Nghia Nguyen, Lokman Bekit 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly supervised video anomaly detection (WSVAD) has predominantly focused on temporal localization, identifying when anomalies occur while largely neglecting their spatial extent within frames. Yet, spatial localization is essential for interpretability and practical deployment in real-world settings. We introduce a patch-based spatiotemporal framework for weakly supervised anomaly localization that jointly models where and when anomalies occur. Our approach operates on grid-level patch features and learns region-level anomaly scores under a multiple instance learning paradigm. We further propose a Proximity-Aware Top-k spatiotemporal selection strategy that enables the model to generate fine-grained spatial anomaly maps without requiring bounding-box supervision during training. Our method surpasses existing state-of-the-art approaches across multiple benchmarks, yielding substantial gains in spatiotemporal localization accuracy. In addition, we release frame-level bounding-box annotations for the test sets of two widely used datasets, along with our code and pretrained models, providing new resources to facilitate future research in spatially grounded WSVAD.

---


### 227. [The Verbose Context Problem in Medical Records](https://arxiv.org/abs/2606.29503)

**<font color=#1a73e8>作者：</font>** Shiva Kaul, Min-Gyu Kim, Anjum Khurshid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The verbose context problem occurs when structured concepts have token-inefficient textual representations. This bottleneck is acute in population health: cohort-level analysis of longitudinal patient records requires reasoning over thousands of medically-coded events, often exceeding 400K tokens in total. We present PopMedQA, a benchmark isolating this problem through computational tasks on groups of longitudinal patient records. We construct the benchmark using neopatient, a new library for language-controlled generation of artificial patient records. Through extensive ablations -- including prompting strategies, prompt compression, and agentic decomposition -- we find that domain-independent methods fail to alleviate the verbose context problem. There remains significant opportunity to exploit domain-specific structure in language model inputs for population-scale reasoning.

---


### 228. [Empirical Evaluation of Multi-Modal Touch Detection in Over-the-Shoulder Video Surveillance](https://arxiv.org/abs/2606.29504)

**<font color=#1a73e8>作者：</font>** Mohammadreza Rashidi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Intelligence Surveillance (VIDINT) on over-the-shoulder footage is a proposed vector for monitoring human-computer interaction patterns without direct screen recording access. In this paper, we evaluate a Behavioral Intelligence (BEHINT) touch-detection framework designed to reconstruct keystroke events on mobile keypad interfaces from physical finger interactions. Our system integrates four parallel detection modalities: (1) anatomical hand landmarks via MediaPipe, (2) HSV skin color filtering, (3) temporal frame differencing for motion detection, and (4) shape-guided Canny edge analysis. We map relative touch coordinates to a reference screen layout to reconstruct typing sequences. Evaluation on a 120-frame first-person staged video of passcode entry reveals that while MediaPipe and Skin Detection fail to run autonomously due to partial hand occlusion and ambient noise, Motion-Only and Edge-Only configurations achieve F1-scores of 18.5% and 18.2%, respectively. The combined multi-modal configuration achieves an F1-score of 16.7% and a sequence similarity of 3.0% when mapped to the iOS passcode layout. We conduct ablation, resolution decay, noise sensitivity, and proximity threshold tuning to characterize the system's operational envelope. We then audit generalization on 5 real, publicly licensed third-person phone videos and find that the detector emits a median of 57 touch points per frame (peaking at 205), one to three orders of magnitude more than the rate of real taps, because the skin filter responds to the whole hand rather than to fingertip contact. The staged keystroke result does not survive contact with uncontrolled footage; the system does not achieve reliable keystroke reconstruction outside the calibrated staged setting.

---


### 229. [Benchmark AUC Is Not Deployable Reliability: A Cross-Dataset Audit of Off-the-Shelf Features for Surveillance Video Anomaly Detection](https://arxiv.org/abs/2606.29506)

**<font color=#1a73e8>作者：</font>** Mohammadreza Rashidi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated "suspicious behavior" flagging is a headline promise of AI surveillance, and the field reports high frame-level ROC-AUC on standard video anomaly detection benchmarks. Those numbers are measured by training and testing on the same camera and scene. We audit what happens when that assumption is dropped. We build an unsupervised normality model from the all-normal training frames of one dataset, using frozen off-the-shelf embeddings (CLIP, DINOv2, ResNet-50, EfficientNet-B0) and a nearest-neighbour distance, and score the test frames of the same and of other datasets. Across 4 real datasets (UCSD Ped1, UCSD Ped2, CUHK Avenue, ShanghaiTech) and 4 backbones, same-dataset AUC averages 0.704 but cross-dataset AUC averages 0.499, which is chance: a detector calibrated on one scene is no better than a coin flip on another, and in several pairs it is below chance. The strongest backbone makes this worse, not better: DINOv2 has the best same-dataset AUC (up to 0.901 on Ped2) and the largest cross-dataset drop. The collapse is not an artefact of the scoring rule: replacing the nearest-neighbour detector with a PaDiM-style Mahalanobis detector reproduces it almost exactly (cross-dataset gap 0.202 versus 0.208). Even at a favourable operating point the false-alarm rate is on the order of 31,931 per hour. We conclude that the benchmark numbers quoted for surveillance anomaly detection describe a calibrated laboratory setting and overstate deployable reliability by a wide margin, and we release the code that reproduces every number.

---


### 230. [Reinforcement Learning in Super Mario Bros: Curriculum, Pedagogy, and Optimal Level Design in World 1-1](https://arxiv.org/abs/2606.29511)

**<font color=#1a73e8>作者：</font>** Jesse Ponnock, Lucas Ho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World 1-1 of Super Mario Bros is widely celebrated as a masterclass in game design: its progressive structure is credited with teaching players core mechanics through the level itself. We ask whether that structure is empirically measurable using reinforcement learning. We implement World 1-1 from scratch as a fully discrete environment and compare four algorithms -- Q-Learning, SARSA, Monte Carlo, and Deep Q-Network (DQN) -- across three progressively complex versions of the same level. Monte Carlo emerges as the strongest agent (94.9% $\pm$ 1.5% win rate), outperforming DQN (76.4% $\pm$ 3.4%) by learning to maximize intermediate rewards along winning paths rather than taking the most direct route. We then use Monte Carlo in a curriculum experiment permuting World 1-1's six canonical segments across twelve conditions. Canonical ordering converges fastest, achieves the highest learning efficiency, and is the only condition with zero catastrophic failures; no random permutation matches all three criteria simultaneously. These results provide, to the best of our knowledge, the first empirical validation that World 1-1's canonical design encodes genuine pedagogical structure: one that measurably accelerates learning and cannot be replicated by chance.

---


### 231. [Scenes as Objects, Not Primitives: Instance-Structured 3D Tokenization from Unposed Views](https://arxiv.org/abs/2606.29513)

**<font color=#1a73e8>作者：</font>** Mijin Yoo, In Cho, Subin Jeon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A 3D scene is understood through its objects, not the primitives that compose them. Yet feed-forward reconstruction methods output dense, unstructured sets of points or Gaussians, leaving object-level structure to be recovered after the fact. We propose a feed-forward framework that decomposes a scene into instance-structured 3D token groups directly from unposed multi-view images -- compact object-centric units from which reconstruction, segmentation, and manipulation all follow. Each token group pairs an instance token capturing entity-level identity with anchor tokens that encode local geometry and appearance, which are decoded into a set of 3D Gaussians. This two-level factorization decouples object identity from local appearance, making object instances a native interface of the representation rather than a derived product. The token groups are learned through differentiable rendering with joint reconstruction and segmentation supervision, requiring no 3D annotations. Our feed-forward model surpasses per-scene optimization baselines in class-agnostic instance segmentation while remaining competitive in novel view synthesis. Beyond these metrics, the same token groups directly unlock instance-level scene editing -- removing, translating, or inserting objects by operating on their groups -- as well as efficient open-vocabulary 3D instance retrieval, where retrieval complexity scales with the number of instances rather than primitives.

---


### 232. [A Mathematical Optimization Approach for Expert-Informed Bayesian Best Subset Selection](https://arxiv.org/abs/2606.29516)

**<font color=#1a73e8>作者：</font>** Nolan Alexander, Henning Mortveit  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central challenge in statistical modeling is identifying the subset of features that belong in the true regression model. The classical best subset selection problem, recently made tractable via mixed-integer optimization (MIO), finds the globally optimal sparse solution. It does not, however, make use of any information beyond the observed data. In many applied settings, domain experts can meaningfully rank or score the relevance of candidate predictors, yet no existing framework integrates such probabilistic expert assessments directly into the best-subsets objective. This paper presents Expert-Implied Bayesian Best Subsets (EBBS), a method that incorporates domain-expert probability estimates of feature relevance into the MIO best-subsets problem through a maximum a posteriori (MAP) framework. Expert views from multiple respondents are aggregated into a single prior probability per feature using the Poisson binomial distribution for marginal probability estimates, the pairwise win rate for pairwise comparisons, or the normalized mean rank for ordinal rankings. This probability enters the objective function as a log-odds penalty term that smoothly encourages or discourages the selection of each feature consistent with the expert consensus. This paper provides analytic derivations of the MAP formulation and characterizes its theoretical properties. The proposed model reduces to Best Subsets when experts all have no views. Empirical results on synthetic and real datasets are forthcoming.

---


### 233. [Anti-Collapse Dynamics and the Emergence of Multi-Time-Scale Learning in Recurrent Neural Networks](https://arxiv.org/abs/2606.29519)

**<font color=#1a73e8>作者：</font>** Lorenzo Livi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-range learning is hard for recurrent networks trained with stochastic gradient descent, because the influence of a past input fades with the lag $\ell$, and if it fades too fast the dependence cannot be learned from finite data. This fade is captured by an envelope $f(\ell)$. An exponential fade makes the data needed to learn a lag-$\ell$ dependence grow exponentially, putting long horizons out of reach; a power-law fade keeps the cost polynomial. We show that the asymptotic decay class of $f(\ell)$ is not fixed by the architecture. Instead, it emerges from the coupling between the state dynamics and parameter dynamics, settling into either a collapsed regime (fast, exponential forgetting) or an extended, anti-collapsed regime (slow, power-law forgetting). The intuition is a competition within these coupled dynamics. Training drives the network's effective time scales toward short ones, while rare, heavy-tailed fluctuations of the learning dynamics push a few of them to very long values. The extended regime survives only when these heavy-tailed pushes are strong enough to balance the pull. We make this mathematically precise with a coarse-grained stochastic process and prove exactly when the extended regime exists. A single exponent, the spectral exponent~$\beta$, then governs both the spread of time scales and how slowly the network forgets. Realizing the regime in practice needs one more ingredient: the joint action of the architecture and the optimizer must be able to hold such a broad spread. A network whose capacity to generate broad time-scale spectra is severely constrained still collapses, even when supplied with strong heavy-tailed forcing. Heavy-tailed fluctuations thus act not as noise to be suppressed, but as the mechanism that sustains long-range learning.

---


### 234. [Not All Objectives Are Born Equal: Priority-Constrained Descent for Hierarchical Multi-Objective Optimization](https://arxiv.org/abs/2606.29521)

**<font color=#1a73e8>作者：</font>** Dara Varam, Mohamed I. Alhajri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning problems rarely involve objectives that are equal in importance. A primary objective defines the goal, whilst secondary objectives, such as sparsity, compression, or robustness constrain the solution. While existing multi-objective methods have proven effective in practice, they have a clear symmetry problem and neglect the inherent objective hierarchy built into these objective spaces. We introduce Priority-Constrained Descent (PCD), a gradient-based optimization framework designed to explicitly exploit hierarchical objective structures. PCD preserves the direction of primary descent whilst allowing for the minimal distortion necessary to guarantee progress on secondary objectives, controlled by a single $\tau \in [0, 1]$ that dictates the strength of the distortion. The resulting formulation is invariant to objective scaling and admits exact closed-form solutions for problems with two and three objectives. We evaluate PCD within structured network compression settings, unstructured sparsity and low-rankness, and across a variety of synthetic experiments, showing Pareto dominance and better per-objective performance with secondary progress guarantees over existing methods, further exhibiting the interpretable trade-off that $\tau$ provides.

---


### 235. [Do Models Read What They Write? Causal Registers in Scratchpad Reasoning](https://arxiv.org/abs/2606.29522)

**<font color=#1a73e8>作者：</font>** Benjamin Shih, John Winnicki, Eric Darve  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central hope behind process supervision is that models can expose intermediate variables that matter for their later behavior. For this to help with alignment, a scratchpad must be tied to the computation: when the model writes a state, later steps should compute from that state. To test this requirement, we use a controlled state-tracking task with a known update rule, comparing models trained to report only the final state with models trained to write intermediate states before giving the final answer. At evaluation, we edit the internal representation of one written state while leaving the visible scratchpad text fixed. Because the transition rule is known, the edit has a single correct downstream consequence. In Qwen2.5-Coder-7B, the state-writing model predicts the next phase bit implied by the edited state on 80% and 91% of held-out examples across the two task variants, while pretrained and final-answer-only controls remain near baseline. Additional controls rule out generic next-token steering and copying another continuation: the prediction depends on both the edited state and the current move. The same causal-use pattern replicates across model families. Together, these results suggest a sharper goal for scratchpad oversight: not just to make intermediate reasoning legible, but to train written states that the model uses as part of its computation.

---


### 236. [GarmentZoom: Generating Zoomable Images from Garment Listings](https://arxiv.org/abs/2606.29535)

**<font color=#1a73e8>作者：</font>** Renjie Zhao, Jingwei Ma, Huy Huynh Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online product listings for garments often include an overview photo and a close-up to show garment details. However, each photo focuses on either field of view or garment detail, forcing users to alternate between views and breaking browsing continuity. We present GarmentZoom, a system that enhances the full-view photo to match the fidelity of its accompanying close-up, enabling seamless zoom-and-pan exploration. Unlike standard reference-based super-resolution, our setting involves close-up references that are spatially unaligned with the full view, and scale factors that vary substantially across garments 3-20$\times$. Prior work typically relies on alignment to transfer details or requires per-instance fine-tuning to memorize them. Instead, we train a single model that supports a continuous range of scales across diverse garments. Our approach synthesizes details without requiring spatial alignment and matches the quality of per-instance methods with a fraction of the training cost.

---


### 237. [OSWorld2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks](https://arxiv.org/abs/2606.29537)

**<font color=#1a73e8>作者：</font>** Mengqi Yuan, Zilong Zhou, Xinzhuang Xiong 等 36 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing computer-use benchmarks fail to capture the realism, complexity, and long-horizon demands of real-world computer use, limiting their ability to reveal the limitations of frontier agents. We introduce OSWorld 2.0, a benchmark of 108 long-horizon computer-use workflows across everyday and professional tasks, designed to capture complex and challenging real-world phenomena. Each task represents a realistic end-to-end workflow that takes human users a median of about 1.6 hours to complete and requires an average of 318 tool calls with Claude Opus 4.7 using maximum thinking, compared with about 30 in OSWorld 1.0. OSWorld 2.0 targets challenge phenomena that are common in real workflows yet underrepresented in prior benchmarks, spanning interaction-design challenges such as streaming interaction and dynamic environments, as well as agent-pattern challenges such as cross-source reasoning, implicit-state inference, and visual-spatial precision. Tasks are grounded in authentic input artifacts and cross-referenced against realistic stateful user profile data, and include separate safety reports auditing safety-sensitive execution. Under our primary binary-completion metric at 500 steps, Claude Opus 4.8 with maximum thinking and batched tool calls scores best but still completes only 20.6% of tasks at a 54.8% partial score; GPT-5.5 is far more token-efficient yet plateaus near 13%. These results show that current agents are still far from professional-level computer use: rather than stumbling on basic GUI control or coding, they lose track of constraints, miss information that arrives mid-task, guess rather than ask the user, and skip verification, struggling most when a task hinges on hidden state they must recover.

---


### 238. [Learned Coordination Conventions in Cooperative MARL: Measuring the Translation Gap Between Theory-Informed Roles and Learned Routing](https://arxiv.org/abs/2606.29541)

**<font color=#1a73e8>作者：</font>** Yoosung Hong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Role-semantic assignments provide priors over how heterogeneous agents may coordinate, but cooperative MARL systems instead settle on conventions through decentralized, non-stationary learning, with no guarantee that the resulting structure matches those priors. We study this translation gap between theory-informed role expectations and learned coordination structure through a diagnostic combining a role-routing matrix, formation sensitivity ($\Delta_{\max}$), and gradient/occlusion attribution across three-role MiniGrid and SMACv2 (Terran) environments.
We show that label-conditioned attention produces substantially more concentrated and role-specific routing than flat MLP baselines, remains stable under 3v3--9v9 scaling, transfers zero-shot across team sizes, and is invariant to ally-slot padding. A 5-seed re-evaluation shows partial alignment between learned conventions and designer-specified priors while revealing where small-n noise can manufacture apparent strategic divergence. We present these results as an empirical framework for measuring coordination structure in cooperative MARL rather than as a new equilibrium concept or causal explanation.

---


### 239. [VISTA-DZ: Visual Semantic Trajectory Adaptation for Personalized Dilemma Zone Prediction](https://arxiv.org/abs/2606.29548)

**<font color=#1a73e8>作者：</font>** Chuheng Wei, Ziye Qin, Ziran Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Driver decision making in the dilemma zone at signalized intersections is safety critical, as vehicles approaching a yellow signal must decide whether to stop or proceed within limited time and distance margins. Accurate prediction of both stop-go decisions and decision timing is important for adaptive signal control, advanced driver assistance systems, and human-centered intelligent transportation applications. However, dilemma zone behavior is strongly driver dependent. Similar approach trajectories may lead to different decisions across drivers because of differences in risk preference, braking habit, and decision threshold. Existing personalized models often rely on handcrafted scalar descriptors, which provide useful but limited summaries of individual behavior. This paper proposes VISTA-DZ, a semantic-profile-conditioned framework for personalized stop-go and decision-time prediction. Historical trajectories are converted into visual representations, interpreted by a vision-language model to generate behavioral profiles, and encoded as semantic embeddings to condition a dual-output prediction network. The final model combines a bidirectional GRU encoder, driver-conditioned multi-head cross-attention, and Feature-wise Linear Modulation for temporal evidence selection and feature adaptation. Experiments on the SDZ dataset and a newly collected FDZ dataset show that VISTA-DZ outperforms trajectory-only and handcrafted personalization baselines, achieving 93.26% in-domain simulation accuracy and 90.22% mean accuracy across 20 held-out simulation drivers. Cross-domain results further show feasible zero-shot simulation-to-real transfer and better real-world generalization when simulation data are combined with limited field data.

---


### 240. [Persona-Trained Monte Carlo: Estimating Market-Outcome Distributions via Swarms of Persona-Conditioned Neural Policy Bots in a Limit Order Book](https://arxiv.org/abs/2606.29556)

**<font color=#1a73e8>作者：</font>** Salavat Ishbulatov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Persona-Trained Monte Carlo (PTMC), a method for estimating distributions of market-outcome statistics by repeatedly simulating limit-order-book interaction among swarms of persona-conditioned neural-policy trading bots. Each run instantiates many bots sharing one trained policy network but conditioned on heterogeneous, individually sampled persona parameters drawn from a learned trader-heterogeneity distribution; the bots interact in a continuous double auction, and the resulting price path is one Monte Carlo sample. Repeating this over independent persona-population draws yields an ensemble from which a target market statistic is estimated. Randomness enters through persona draws, within-run action sampling, and optional exogenous shocks, not solely through price as in classical Monte Carlo. We distinguish PTMC from adjacent paradigms, including classical Monte Carlo, hand-coded agent-based models, single-agent reinforcement learning, and large-language-model-based generative agents. To justify the design, we survey cross-disciplinary foundations -- agent-based computational economics, market microstructure, behavioral finance, deep reinforcement learning, generative/LLM-based agents, news-driven trading, systemic risk, econophysics, and game theory -- connecting each literature to a specific design choice in the policy network, training data, or validation protocol. We formalize the PTMC estimator and its convergence properties, specify a candidate bot architecture and training objective, and propose a four-level validation methodology: stylized-fact matching, microstructure- and agent-level checks, and historical stress-test comparison against a zero-intelligence baseline. The framework is proposed but not implemented: we contribute a formal estimator, a cross-disciplinary design justification, and a validation roadmap, and conclude with open research questions.

---


### 241. [Speculative Pre-Positioning: Decoding Stateful Sessions to the Next Decision Point Off the Critical Path](https://arxiv.org/abs/2606.29565)

**<font color=#1a73e8>作者：</font>** Victor Norgren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A stateless inference server (vLLM, SGLang, TensorRT-LLM) idles between requests while the accelerator waits; a stateful session reclaims that idle time. Speculative pre-positioning decodes the session forward to its next decision point with the target model's own forward pass and no draft model, moving the cross-request prefill and entry-decode off the critical path: the next request resumes from a pre-paid entry on its delta, or, when a confidence gate fires, is answered from a cached distribution in one near-constant vocabulary scan with no decode, at a cost only of energy and a rare, bounded false accept. The payoff is conditional on capability: a capable model fires the gate at near-full coverage and about 87% precision (a smaller one never clears it), returning the first token in about 1.0 ms versus the 39 ms decode a prefix cache still pays.

---


### 242. [Anisotropy Decides Cosine vs. Rank Metrics for Text Embeddings](https://arxiv.org/abs/2606.29571)

**<font color=#1a73e8>作者：</font>** V.S. Raghu Parupudi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The standard way to compare two text embeddings is cosine similarity. Scattered studies report that a different metric does better, but never pin down the geometric condition that decides when, or why. We settle both with a comprehensive empirical study: nineteen parameter-free similarity metrics on nineteen encoders, from compact sentence transformers up to seven-billion-parameter large language models, across seven datasets. The answer is geometric. When an encoder spreads its variance evenly across directions, cosine is the best parameter-free choice and no other metric helps by a usable margin. When the variance concentrates into a few dominant directions, a property known as anisotropy, rank-based and L1-type metrics beat cosine by a clear margin. The absolute gain is modest, but because cosine starts low on these encoders it is a sizable relative improvement, around twenty percent on average and largest where cosine is weakest. What decides this is the geometry of the embedding space, not how the model was trained: where the two disagree, the metric follows the geometry. One number, the fraction of variance held by the single most dominant dimension, predicts how much the alternatives help across all nineteen encoders, with a rank correlation of 0.86 and a linear correlation of 0.95. To test this as the cause rather than a correlate, we project out the dominant directions: cosine recovers and the advantage of the other metrics nearly vanishes, but only on the encoders that were anisotropic to begin with. The effect is directional, not magnitude based, since it survives normalizing every vector to unit length. Among parameter-free metrics, then, cosine is the right tool wherever an encoder is well spread, which includes the fine-tuned embedders commonly deployed for retrieval, and we give a one-number diagnostic for when it is not.

---


### 243. [Bilevel Optimization for Neural Architecture Search](https://arxiv.org/abs/2606.29582)

**<font color=#1a73e8>作者：</font>** Abhishek Shukla, Ankur Sinha, Faiz Hamid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bilevel optimization has become an influential and widely adopted framework for addressing hierarchical optimization problems in machine learning, providing an effective approach to modeling the interaction between two levels of optimization, with applications such as hyperparameter tuning, meta-learning, adversarial training, and data poisoning. Neural Architecture Search (NAS), a subfield of hyperparameter optimization, is a prime example of a bilevel optimization problem, with architecture parameters optimized at the outer-level and network weights optimized at the inner level. This paper presents a structured overview of NAS through the lens of bilevel optimization. We categorize existing NAS approaches into two main classes: sampling-based methods, which search optimal architectures using different architecture samplers, and bilevel theory-based methods, which solve the architecture search problem using bilevel optimization principles. We further highlight our current research direction, wherein the bilevel NAS formulation is addressed through an auxiliary mathematical programming framework. This framework enables the systematic integration of second-order information from the model's training loss function and ensures the optimality of the model parameters while modifying architecture parameters. By simultaneously updating the architecture and model parameters along their respective optimal descent directions derived from the auxiliary mathematical program, these methods achieve more principled and theoretically consistent results. The same auxiliary program can also be used for simultaneous hyperparameter and model fine-tuning. A comparative analysis shows that bilevel theory-based approaches generally outperform sampling-based methods, both in accuracy and efficiency.

---


### 244. [SonoCLIP: Mask-Guided Region-Aware Vision-Language Pretraining for Fetal Ultrasound Analysis](https://arxiv.org/abs/2606.29586)

**<font color=#1a73e8>作者：</font>** Hang Su, Chao Sun, Zhaofan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language foundation models have shown strong potential in medical image analysis. Although foundation models for ultrasound imaging have recently emerged, the domain remains particularly challenging due to severe speckle noise, acquisition variability, and subtle anatomical boundaries, leading to high inter-observer variability. Existing CLIP-based models rely primarily on global image-text alignment, limiting their sensitivity to clinically decisive local structures. We propose SonoCLIP, the first million-scale region-controllable fetal ultrasound vision-language foundation model that integrates segmentation masks as mask-channel visual prompts within the vision encoder, enabling joint global-local contrastive representation learning. To support scalable region-text alignment, we introduce a sigmoid-based pairwise contrastive loss that improves stability under large-scale supervision. We further curate a 1.44M-image multimodal fetal ultrasound dataset spanning 24 standard planes for large-scale pretraining. Extensive cross-center evaluations demonstrate that SonoCLIP achieves superior zero-shot transfer performance under both global and mask-guided inference, establishing a controllable and clinically oriented foundation model for fetal ultrasound analysis. Our code and data are available at this https URL.

---


### 245. [STEMGym: Benchmarking Sequential Decision-Making under Dose Budgets in Autonomous Electron Microscopy](https://arxiv.org/abs/2606.29592)

**<font color=#1a73e8>作者：</font>** Can Polat, Erchin Serpedin, Mustafa Kurban 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central premise of autonomous scientific imaging is that smarter navigation, whether Bayesian, RL-based, or otherwise adaptive, is the principal lever for sample-efficient acquisition. We present evidence to the contrary in scanning transmission electron microscopy (STEM), an atomic-resolution imaging modality whose every measurement deposits damaging electron dose. We introduce STEMGym, an open-source Gymnasium benchmark of 15 physics-simulated STEM worlds spanning five materials, three difficulty levels, and four characterisation tasks, scored by the Dose-Efficiency Curve area (DEC-AUC), a single scalar capturing the information-vs-dose Pareto frontier. Across 33 agent configurations under realistic dose budgets, the dominant determinant of dose efficiency is the analyst (perception) pipeline, not the navigator: pairing a trained CNN analyst with naïve raster scanning raises DEC-AUC by 5.5x over a CNN-free raster baseline (0.287 vs.\ 0.052), while substituting Bayesian or adaptive finite-state-machine navigation for raster yields no statistically significant further gain. Production-tier vision-language models further underperform task-specific CNNs by {\sim}13x on crystallographic defect analysis. By decoupling perception, navigation, and planning under a unified dose budget, STEMGym reframes where ML effort should be invested in autonomous electron microscopy and provides the measurement infrastructure to test it.

---


### 246. [How AI settled the complexity of the oldest SGD algorithm](https://arxiv.org/abs/2606.29593)

**<font color=#1a73e8>作者：</font>** Michał Dereziński, Xiaoyu Dong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In 1937, Stefan Kaczmarz proposed a simple algorithm for solving systems of linear equations. This algorithm turned out to be the earliest known example of stochastic gradient descent, a ubiquitous computing paradigm that drives the training of modern AI models such as ChatGPT and Gemini. Now, those AI models have joined forces to discover the worst-case complexity of the Kaczmarz algorithm. This paper tells the story of how it happened.

---


### 247. [Does Role Specialization Matter for Explanation Faithfulness in Mixture-of-Experts?](https://arxiv.org/abs/2606.29613)

**<font color=#1a73e8>作者：</font>** Yeji Kim, Housam Babiker, Mi-Young Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures have recently been extended with role-based mechanisms for interpretability. This is typically done by assigning semantic roles to individual expert components, for example roles like synergy, redundancy, and uniqueness in multimodal settings. However, whether such structural role decomposition preserves explanation faithfulness of the overall architecture remains largely underexplored. We hypothesize that inter-expert representation overlap weakens effective role separation and degrades attribution-based faithfulness, even when semantic roles are explicitly defined. To address this limitation, we introduce representation-level decorrelation regularization to explicitly reduce inter-expert similarity in latent space. Using representation decorrelation objectives, we encourage clearer specialization among experts by minimizing representation overlap. Our experiments show that across multiple multimodal benchmarks, this separation consistently improves explanation faithfulness, as measured by comprehensiveness, sufficiency, and their Area Over the Perturbation Curve (AOPC) summaries, while preserving task performance. We further show that these improvements are not limited to role-based architectures such as Interpretable Multimodal Interaction-aware MoE (I2MoE). Similar trends are observed in a standard sparse MoE baseline, suggesting that representation-level separation may provide a more general mechanism for enhancing explanation faithfulness in MoE systems. Overall, our findings suggest that structural role decomposition alone may be insufficient to guarantee faithful explanations and that representation-level separation helps improve explanation faithfulness. To support reproducibility, the source code and supplementary material are publicly available at this https URL.

---


### 248. [SCARCE: Scalable Cascade Analysis for Rare-event Characterisation via Embeddings](https://arxiv.org/abs/2606.29623)

**<font color=#1a73e8>作者：</font>** Yingjie Wang, Yi Dong, Edmund Lau 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rare events govern the safety profile of modern AI systems, yet their probabilities are extremely difficult to estimate: direct Monte Carlo requires prohibitive sample budgets. Subset Simulation (SS) addresses this by decomposing a rare-event probability into moderate conditional probabilities over nested intermediate events. However, classical SS requires a handcrafted scalar performance function whose sublevel sets define those events, demanding detailed knowledge of the failure geometry and limiting transfer to new domains. We propose SCARCE (Scalable Cascade Analysis for Rare-event Characterisation via Embeddings), which replaces the performance function with learned latent representations and geometric rulers that score proximity to failure regions. Adaptive thresholding constructs nested intermediate events directly from data. We formalise SCARCE through a non-negative supermartingale, yielding a high-probability upper envelope that remains valid under early stopping. On MNIST misclassification, where dense Monte Carlo provides ground truth, SCARCE achieves approximately 400--500 times lower mean absolute error than grid-searched traditional SS while eliminating systematic over-counting. We then study PAIR-style LLM jailbreaks under a fleet-level threat model with adversarial fraction $\eta$. On Llama-Guard-3-8B hidden states, a PCA-based ruler attains 2.6% mean relative error for $\eta \geq 10^{-3}$ against finite-sample references whose average bootstrap relative half-width is 27.9%, and transfers to a GCG-style corpus with 2.93% relative error after recalibration. A directional criterion $\mathrm{KL}(p_{\mathrm{good}}\,\|\,p_{\mathrm{bad}})$ ranks rulers consistently with estimation error (Spearman $\rho=0.83$).

---


### 249. [SFBench: The SciFy Scientific Feasibility Benchmark](https://arxiv.org/abs/2606.29630)

**<font color=#1a73e8>作者：</font>** Cash Costello, James Mayfield, Elsbeth Turcan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present SFBench, a benchmark dataset for evaluating systems that assess the feasibility of scientific claims. SFBench includes 197 claims in materials science, each annotated with a ground-truth feasibility score on a five-point scale along with an explanation of that assessment. The collection differs from previous collections in several important ways: 1) it defines a complex task that requires reasoning over claims of varying scientific feasibility; 2) its claims are not extracted from existing scientific publications but are created de novo, greatly reducing the chances that LLMs have trained on them; 3) claims and ground truth are established by subject matter experts, not by artificial intelligence; and 4) unlike many benchmarks that ask about question/answer pairs, provide multiple choice answers, or ask questions requiring short, fixed answers, SFBench explanations are completely open-ended. We describe the benchmark design, data creation process, and evaluation metrics, and we report baseline results using recent GPT models.

---


### 250. [Two-Stage Prompt Optimization for Few-Shot Relation Extraction: From Reasoning-Guided Search to Gradient-Guided Refinement](https://arxiv.org/abs/2606.29639)

**<font color=#1a73e8>作者：</font>** Aunabil Chakma, Mihai Surdeanu, Eduardo Blanco  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic prompt optimization is still underexplored for episodic few-shot relation extraction with smaller language models. We propose a two-stage framework that combines reasoning-based prompt optimization with gradient-based prompt optimization. The first stage can use any reasoning-based optimizer to make broadprompt improvements in natural language. The second stage applies our GradPO, which uses loss and gradient signals to identify high-impact prompt spans and refine them with local edits. Experiments on FS-TACRED and FS-FewRel show that local refinement usually improves prompts found by the first stage, and GradPO is the most consistent refiner. Our framework achieves state-of-the-art performance on FS-TACRED with Qwen3-4B and remains competitive on FS-FewRel.

---


> [!TIP]
> 当前位于：**201-250**（第 5/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
