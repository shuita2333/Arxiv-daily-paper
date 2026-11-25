# 📦 其他研究 | 2026年11月26日

> 本类共 **342** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-342](./part-07.md)

---

### 151. [The Old Scene Lives in the Cache: Diagnosing and Shedding Stale History in Streaming Video Generation](https://arxiv.org/abs/2611.32116)

**<font color=#1a73e8>作者：</font>** Hao Zhou, Ziyang Xu, Chenhan Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Switching scenes while preserving the original subject in streaming video generation exposes a conflict: cached history helps maintain the subject but also sustains old-scene objects that should disappear. Through controlled interventions on text conditioning, denoising steps, the local window, and the attention sink, we identify how cached visual history keeps this obsolete content. When the original frames remain in the cache, KV flush and sink recomputation still leave old-scene objects in the generated videos. Replacing this history with target-scene history largely removes those objects, but also changes the subject, reducing face similarity to the pre-switch subject. We then propose Molt Forcing, a training-free method that rebuilds scene history from a cold-start target scene while selectively retaining subject tokens from the original cache. Across 16 scene families, Molt Forcing removes old-scene objects at least as reliably as an Echo-Forcing hard cut while keeping the subject much closer to its pre-switch appearance.

---


### 152. [Monte Carlo Tree Search for Classifier Chains](https://arxiv.org/abs/2611.32118)

**<font color=#1a73e8>作者：</font>** Romain Poggi, Jesse Read  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-label classification continues to be relevant to a variety of modern tasks. Among other challenges, modern data sets are increasingly large with respect to the number of labels, and these labels may be noisy or missing in the training sets. Label-wise scores and ranking-based metrics have been popular, but optimising exact multi-label evaluation (where a predicted set of labels should match the true set exactly) is particularly relevant for many domains, e.g., in medicine; alongside some measure of confidence. This requires an estimation of joint probability across labels (a model of label dependence; conditioned on each input instance). A family of methods known as probabilistic classifier chains provides such inference. However, these existing varieties either do not scale to a large number of labels or do so by approximating joint via marginal distributions in a way that compromises the estimation of uncertainty for exact match accuracy. We overcome this issue by proposing TSCC; leveraging a Monte Carlo Tree Search methodology to enhance chain inference via an efficient balance between the exploration of label space and the exploration of promising label-set predictions. Results are promising both in terms of predictive and computational performance.

---


### 153. [CoverMem: Coverage-Constrained Visual Memory for Budgeted Embodied Question Answering](https://arxiv.org/abs/2611.32119)

**<font color=#1a73e8>作者：</font>** Ruijie Ma, Haoyue Liu, Mingda Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Episodic-memory embodied question answering enables agents to answer questions based on previously recorded visual observations of the surrounding scenes. However, growing observation histories, varying observation quality across viewpoints, and limited computational resources make it challenging to construct and maintain compact visual memories while retrieving sufficient evidence for question answering. To address these challenges, we introduce CoverMem, which incorporates three key components: (1) a coverage-constrained memory construction method that selects a compact set of informative full frames satisfying object-quality and representative-scene coverage requirements; (2) a coverage-preserving incremental maintenance strategy that locally reselects only the affected frames to satisfy updated coverage requirements as observations arrive; and (3) a budgeted complementary frame selection method that balances question relevance, additional support for question requirements, and redundancy with selected frames within a fixed budget. Experimental results on three benchmarks covering diverse environments and question types demonstrate that CoverMem improves question-answering performance under limited visual budgets.

---


### 154. [EditText: Structure-Aware Generation and Selective Visual Transport for Fine-Grained Text Editing](https://arxiv.org/abs/2611.32134)

**<font color=#1a73e8>作者：</font>** Zhaobin Chu, Guandong Li, Xin Lv 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained text editing aims to accurately replace text in a specified region while preserving the source text's font, color, and texture, as well as visual consistency in unedited regions. We present EditText, a unified framework for fine-grained text editing that combines target character generation with visual transport from the source image. The model uses dual-condition Fill inputs: a masked image and a source text style reference, both sharing a spatial reference with the target image. The masked image hides the original text and retains unedited content as a source canvas; the style reference supplies appearance cues that guide new character generation together with the target text. We introduce an Attention Transport framework in which Source Weight describes the attention allocated to a condition and the Spatial Aggregation Kernel describes its internal spatial attention distribution. Accurate transfer of source details depends on attention strength, the retention of details in condition features, and spatially accurate aggregation. For selected non-edit queries, we therefore preserve the total attention weight assigned to the masked image while redistributing its attention toward spatially corresponding neighborhoods, enabling selective visual transport. Multi-stage training, combined with a Glyph-aware Structural Loss on local target character structure, teaches the model to generate accurate text, preserve source text appearance, and retain unedited details. We also introduce TBench, a fine-grained text editing benchmark covering Alphabetic, Logographic, and Arabic numerals, to evaluate character updates, appearance preservation, and the preservation of unedited details. On TBench, EditText achieves state-of-the-art non-edit-region SSIM (0.9769) and full-image LPIPS (0.0460).

---


### 155. [Interpretable Orthogonal Latent Diffusion with Scale-Selective Uncertainty for Medical Image Super-Resolution](https://arxiv.org/abs/2611.32135)

**<font color=#1a73e8>作者：</font>** Onkar Jadhav, Tim French  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models are increasingly used for medical image reconstruction and super-resolution, but their samples may contain plausible fine-scale hallucinations that are difficult to identify from the reconstructed image alone. We propose Med-PODiff, a patch-wise proper orthogonal decomposition (POD) diffusion framework for brain MRI super-resolution that performs generative reconstruction in compact and interpretable local coefficient spaces. Unlike pixel-space or learned-latent diffusion models, Med-PODiff uses the POD structure to separate low-rank anatomical variation from fine-detail residual variation, enabling predictive uncertainty to be decomposed into total, coarse, and fine components. Building on this decomposition, we define a pixel-wise hallucination-risk score, $H_p$, that emphasizes regions where fine-detail uncertainty dominates coarse structural uncertainty. On brain MRI, Med-PODiff outperforms representative diffusion baselines in reconstruction quality while producing well-calibrated predictive intervals, with total uncertainty detecting high-error regions at AUROC 0.954. More importantly, the decomposed uncertainty is scale-selective: coarse and fine uncertainty preferentially predict errors at the corresponding scales, with $H_p$ localizing fine error at AUROC $0.906$. Controlled injections and retrospective Cartesian $k$-space undersampling further support fine-detail localization and degradation robustness. The discarded POD tail is only $3.8\%$ of the retained fine-error magnitude, and Med-PODiff improves downstream segmentation consistency while requiring substantially less inference time than pixel-space diffusion.

---


### 156. [VIDE : Training-Free Video Anomaly Detection via Visual Intrinsic Distribution Estimation](https://arxiv.org/abs/2611.32138)

**<font color=#1a73e8>作者：</font>** Kevin D. Nguetche, Atif Belal, Lilian Hollard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In embedding-based video anomaly detection (VAD), normal clips can have high similarity to anomalous descriptions, an anomaly bias that leads to false positives. Methods such as PRISM mitigate this bias by measuring deviations from a normality reference along anomaly directions. Both the normality reference and the anomaly directions are derived from text and shared across videos, although normal activity and the appearance of anomalies vary across scenes. The resulting scores are also sensitive to prompt selection. To address these limitations, we propose Visual Intrinsic Distribution Estimation (VIDE), a training-free framework that adapts text-derived scoring to each test video using frozen clip embeddings. VIDE estimates normal scene content from clips with low initial anomaly scores and uses this estimate to partially correct the textual reference. It then rescales category responses, penalizes clips with strong responses across categories, and refines the anomaly directions using high-scoring clips. VIDE averages scores across prompt views to reduce sensitivity to prompt selection and fuses scores from two frozen encoders. With both encoders, VIDE improves AUC over the best PRISM result by $1.5$, $1.9$, and $3.5$ points on UCF-Crime, XD-Violence, and MSAD, respectively, and AP by $6.5$ points on XD-Violence and $9.3$ points on MSAD. VIDE yields the highest AUC among the compared training-free methods on all three benchmarks and the highest reported AUC among all compared methods on XD-Violence and MSAD. Our code is included in the supplementary material and will be made publicly available.

---


### 157. [LiteSTAR: Low-Rank Channel Modulation for Temporally Consistent CVD Video Compensation](https://arxiv.org/abs/2611.32140)

**<font color=#1a73e8>作者：</font>** Peiyang Lin, Sichen Lin, Yipeng Liao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color Vision Deficiency (CVD) affects a large population worldwide, yet practical recoloring must run continuously on-device. Frame-wise video recoloring produces color flickering, while existing methods rely on costly cross-frame alignment in pixel or feature space. We observe that color flickering correlates with variations in channel-wise responses, with color-sensitive variations concentrated in a low-rank subspace. Based on this observation, we propose Lightweight Spatio-Temporal Adaptive Recoloring (LiteSTAR), built around LiCaD, a plug-and-play Lightweight Channel-Adaptive Decoder. LiCaD performs temporal filtering in a low-rank state space with learned process and observation uncertainties. It then modulates feature channels to achieve temporal consistency without explicit spatial alignment. LiteSTAR further employs adaptive patch routing to improve color discrimination for CVD users while avoiding unnecessary over-enhancement. We also introduce EgoCVDSet, the first egocentric video benchmark for CVD recoloring. Extensive quantitative and qualitative experiments demonstrate that LiteSTAR achieves superior performance with only 0.05M parameters. LiCaD further demonstrates strong generalization across different tasks and network architectures. The code, models, and dataset will be released after review.

---


### 158. [CSC-Mamba: Bridging multimodal convolutional sparse coding and state space models for multi-contrast MRI super-resolution](https://arxiv.org/abs/2611.32144)

**<font color=#1a73e8>作者：</font>** Iman Marivani, David Van Hamme, Jan Aelterman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-contrast MRI super-resolution accelerates clinical protocols by reconstructing high-resolution (HR) target modalities from low-resolution (LR) inputs, guided by easily acquired reference contrasts. While purely data-driven deep neural networks achieve strong performance via rich representation capacity, they rely on heuristic fusion mechanisms (e.g., naive concatenation or black-box cross-attention) that lack theoretical grounding. Alternatively, model-based deep unfolding networks enforce principled cross-contrast fusion through explicit priors, yet their unrolled steps remain constrained to shallow convolutions, lacking modern deep blocks to capture global context. To bridge this gap, we propose CSC-MAMBA, unifying deep-unfolded multimodal convolutional sparse coding with the Vision Mamba state-space backbone. By fusing common structural priors from the guidance modality via unfolded sparse coding and globally refining contrast-specific representations with a Mamba back- bone, our approach benefits from interpretable, model-guided fusion and long-range spatial context. Experiments on the IXI dataset demonstrate that CSC-MAMBA outperforms state-of-the-art methods in reconstruction quality, achieving up to a 0.62 dB gain in PSNR while remaining computationally efficient.

---


### 159. [RetraQ: Manifold-Constrained Critic Guidance for Flow Policies in RL](https://arxiv.org/abs/2611.32148)

**<font color=#1a73e8>作者：</font>** Xuanzhuo Liu, Wu Chen, Ruixiang Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A learned critic can improve a pretrained flow-matching policy by steering sampled actions toward higher predicted value. However, even a critic that fits the behavior data well can provide misleading action gradients. Gradient components pointing away from the data-supported region are weakly constrained by behavior data and can lead guidance to exploit critic extrapolation errors. We introduce RetraQ (Retraction-based Q-guidance), which uses geometry encoded by the pretrained flow to constrain both the direction and the destination of critic guidance. A single velocity evaluation of the frozen flow defines a denoising map. RetraQ filters the critic gradient with the map's Jacobian and applies the map itself to correct the updated action. Our analysis characterizes when these operations approximate tangent filtering and retraction onto the behavior manifold. The same update guides actions at test time and provides targets for policy distillation and online reinforcement learning. In controlled studies, RetraQ improves true return while keeping refined actions close to the data-supported region, and its distillation targets remain more stable than those of raw critic ascent. In offline-to-online training on LIBERO and OGBench, RetraQ achieves higher mean final success than the evaluated critic-guidance baselines. On a real-world plug-insertion task, test-time RetraQ improves the success rate of a behavior-cloned $\pi_{0.5}$ policy from 55.0% to 76.7%. Online training further increases success to 98.3% in only 30 minutes and 100% within one hour. Project page: this https URL

---


### 160. [Let The Pixels Through: Rethinking Long Skip Connections for Scalable Pixel Diffusion](https://arxiv.org/abs/2611.32151)

**<font color=#1a73e8>作者：</font>** Jiachen Lei, Jiahong Wu, XiangXiang Chu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training pixel diffusion models remains less straightforward, owing to the ad hoc training recipes and architecture designs, along with the sensitivity to hyper-parameter choices. We show that strong denoisers can be built by refining existing pixel-native designs from the literature. Specifically, we revisit the long skip connection in U-Net and find that the optimization benefit commonly attributed to it is not necessary for its denoising benefit. We further find that the conventional linear combination of features from the skip and main backbone is inadequate for regimes of various noise levels. Motivated by these observations, we introduce two core modifications. First, we adopt asymmetric long skips, which propagate fine-grained information from input embeddings to decoder layers. Second, we introduce adaGLU, a SwiGLU-like MLP block, in decoder layers to adaptively filter information from the embeddings before being added to main-branch features. The above designs give a simple pixel diffusion transformer architecture. When trained from scratch, it scales smoothly from small-scale baselines up to 1.6B parameters, achieving 1.62 and 1.70 FID on ImageNet-256 and -512, respectively. Besides, it natively supports multimodal inputs, such as text and images, yielding competitive performance in text-to-image generation. We release our codes at this https URL

---


### 161. [Encrypted Fixed-Point Multiplication in Quasilinear Complexity](https://arxiv.org/abs/2611.32157)

**<font color=#1a73e8>作者：</font>** Jung Hee Cheon, Junho Lee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Homomorphic encryption enables computation on encrypted data, but its high computational overhead remains a central obstacle. We overcome this obstacle asymptotically for high-precision fixed-point arithmetic. In this paper, we introduce focused encoding, which represents a fixed-point number of $n$-bit precision using a polynomial of degree $O(n/\log n)$ over a polynomially bounded modulus by concentrating precision at one embedding. We then introduce an error-shaping technique for homomorphic operations to preserve the encoding. This yields an encrypted fixed-point multiplication algorithm for the CKKS scheme that runs in online time $O(n \log n)$ at $n$-bit precision for any fixed multiplicative depth, with security parameter $\lambda = O(n/\log^2 n)$.
Further, we develop bootstrapping for focused encoding to overcome the quadratic cost of conventional bootstrapping. We bootstrap ciphertext coefficients at an enlarged scale and shape the resulting error to preserve focused encoding, at the cost of additional modulus consumption. Then, to reduce the remaining logarithmic overhead, we decompose the ciphertext into components over a smaller subring and bootstrap each separately. This reduces the online cost per multiplication, including bootstrapping, to $O(n \log n + n (\log \lambda)^3 \log \log \lambda)$ for security parameter $\lambda = O(n/\log^3 n)$.

---


### 162. [Breaking the Binary-Lifting Barrier for DNA Minimizer Density: Exact Optimization of a Native 4-ary Order at (w, k) = (12, 5)](https://arxiv.org/abs/2611.32159)

**<font color=#1a73e8>作者：</font>** Stefan G. Creadore, Peyton Berntsen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Minimizer schemes sample at least one $k$-mer from every window of $w$ consecutive $k$-mers via a total order $\pi$ on $\Sigma^k$. For DNA ($\sigma = 4$), state-of-the-art lookup schemes such as GreedyMini and OptMini optimize a binary order ($2^k$ ranks) and lift it to $\Sigma^k$ by ranking one bit-plane primarily and breaking $2^k$-way ties lexicographically on the other bit-plane. At $(w, k) = (12, 5)$, this projection locks sets of $32$ DNA $5$-mers into contiguous blocks and restricts the active universal hitting set (UHS) prefix to $448$ of $1024$ $5$-mers, giving exact expected DNA density $2246214544 / 2^{34} \approx 0.1307468945$ for OptMini (this http URL) and $2248978620 / 2^{34} \approx 0.1309077849$ for GreedyMini (this http URL). We bypass binary lifting and optimize directly over native $4$-ary permutations ($|\Sigma^k| = 1024$) from scratch via: (i) an exact de Bruijn endpoint transfer-matrix dynamic program over $B(4, 4)$ ($256$ states), (ii) a weighted set-cover ratio initializer (SetCover4) producing a compact $U = 314$ UHS prefix, (iii) bitmask-sparse simulated annealing preserving the zero-cost $w$-walk-free tail invariant, and (iv) two-pass $O(N)$ exact best-insertion sweeps with large-neighborhood ruin-and-recreate search. The resulting explicit $4$-ary order achieves exact expected DNA density $2234289615 / 2^{34} \approx 0.130052772292$ (density factor $1.690686$), cutting charged windows by $11924929$ contexts ($-0.530890\%$ relative) below OrensteinLab/Minimizers and $14689005$ ($-0.653141\%$) below this http URL at $8200$-byte lookup storage ($1280$ bytes bit-packed). Warm-start relaxation stalls at $U = 379$ ($0.1301728789$), whereas native $4$-ary initialization breaks $32/32$ high-bit blocks across all $2+2$ nucleotide partitions.

---


### 163. [MyMuse: A Personal Museum for Post-Visit Inquiry and Reflection](https://arxiv.org/abs/2611.32169)

**<font color=#1a73e8>作者：</font>** Jiyeon Bae, Chunggi Lee, Jinwook Seo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artwork photographs may preserve what visitors saw without preserving why it mattered. Revisiting them can involve recalling earlier responses and developing new questions and interpretations as knowledge and personal experiences change. Yet recurring interests may remain difficult to recognize across individual exchanges. Informed by a formative study with ten visitors, we present MyMuse, a post-visit system that connects inquiry about individual artworks with reflection across visitors' accumulated records. In its Personal Museum, visitors revisit artworks, ask questions, and record interpretations that inform subsequent system responses. Its interactive Narrative Report reorganizes the same records across artworks through four interpretive lenses. In two within-subject studies with 16 participants, direct comparisons favored MyMuse for vivid revisitation. The report received higher ratings for recurring-interest awareness, cross-artwork connections, and unexpected discovery than a per-artwork presentation of the same records. These findings suggest that examining accumulated records can support reflection on recurring interests and relationships among visitors' responses across artworks.

---


### 164. [Multi-view Random-set Learning](https://arxiv.org/abs/2611.32170)

**<font color=#1a73e8>作者：</font>** Mengchi Zuo, Tianyang Wang, Cai Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trusted multi-view learning aims to integrate heterogeneous views for accurate and reliable predictions. However, multi-view data often exhibit the view degradation phenomenon: individual views contain only partial discriminative information and cannot independently determine the instance-level label. Requiring such views to produce unambiguous class evidence can distort evidence learning and mislead subsequent fusion. Existing methods addressing this problem have at least one of the following drawbacks: (1) assigning evidence to individual classes without explicitly representing unresolved class groups; (2) projecting composite beliefs onto individual classes before fusion, preventing direct refinement of candidate groups through cross-view set intersections.
To address these limitations, we propose a new Multi-view Random-Set Learning (MRSL) paradigm, which preserves view-specific support for candidate class sets and refines candidate classes through cross-view fusion. Specifically, we quantify class overlap to select a compact collection of sets for each view, avoiding the exponential cost of modeling all class subsets. We then perform set-level fusion by assigning joint support to set intersections, allowing complementary views to narrow the candidate classes before probability conversion. Experiments on synthetic and eight real-world datasets validate the proposed overlap measure and demonstrate that MRSL achieves the highest accuracy on all eight datasets. Compared with the strongest baselines, MRSL improves average accuracy by 4.71% and reduces average expected calibration error by 6.33%. All datasets and code will be made publicly available upon acceptance.

---


### 165. [Mind the Band: The Hidden Frequency Variable in Geometric RoPE](https://arxiv.org/abs/2611.32171)

**<font color=#1a73e8>作者：</font>** Seonghyun Jin, Youngmin Kim, Jong Chul Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometric rotary position encodings (RoPE) incorporate 3D camera geometry into multi-view attention by rotating token features according to viewing rays, depths, and reprojected image coordinates. Each coordinate is rotated across a progression of frequencies--its frequency band--yet existing implementations leave this band to inherited defaults, either retaining standard 2D RoPE's top frequency or letting the frequency span grow exponentially with the attention head dimension. We show that this unstandardized setting can reverse benchmark rankings. In novel view synthesis on RealEstate10K, RayRoPE matches the strongest baseline in the 47M model (144-channel heads), yet trails by 1.2 dB in the 25M model (48-channel heads), and exhibits the same reversal when varying head size alone at fixed model width. Populating a 243x range with four frequencies instead of the 3x default at 48 channels recovers 0.9 dB of that gap. Across view synthesis and two-view depth estimation, overly narrow bands consistently blur correspondence, whereas all three projection-based encodings perform reliably when their top frequency lies within 0.3--3 rotations per 8-pixel patch (10--90 rotations across 256x256 RealEstate10K). At the opposite extreme, overly wide bands degrade RayRoPE through a forward-backward asymmetry: averaging rotations over a predicted depth interval damps high frequencies in the forward pass, yet leaves their gradients with respect to predicted depth undamped. Blocking only those high-frequency depth gradients recovers 90--93% of the lost PSNR, showing that forward smoothing does not guarantee backward stability. Guided by this analysis, we distill practical guidelines--setting bands in image coordinates, populating spans in small heads, and avoiding unconditional same-view damping--and advocate reporting and matching frequency bands in future multi-view benchmarks.

---


### 166. [MediaStormBench-CameraLog: Can Multimodal Models Identify a Camera's Log Curve?](https://arxiv.org/abs/2611.32172)

**<font color=#1a73e8>作者：</font>** Ming Ma, Wenhao Hu, Qichao Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> MediaStormBench is a multimodal benchmark for real-world film and television production, with each subset drawn from MediaStorm's day-to-day work. We release its first subset, MediaStormBench-CameraLog (CameraLogBench), on a common foundational task in footage ingest and initial color grading: identifying the Log curve of a clip without metadata. Cameras record Log footage by compressing a wide range of scene light into code values with a vendor-defined logarithmic curve, and color can be restored correctly only once that curve is known. The curve, however, is recorded only in file metadata, easily lost in transcoding and team hand-offs. A colorist then has to try candidate curves one by one against a waveform scope, and a wrong choice shifts the tones and colors of the whole clip. Recovering the curve from the image alone is challenging, because vendor curves cluster tightly in code value and are coupled with unknown exposure. CameraLogBench is built on professionally shot footage and tests whether multimodal models can identify the curve, with a probe that removes the correct option to expose guessing from priors. Because every candidate curve is strictly defined by a published vendor formula, we derive four controls from one implementation of these formulas: graded negatives, synthetic frames of identical scenes, in-context specification digests, and a training-free formula baseline, which together decouple semantic priors from photometric measurement. Across 11 models, real-footage accuracy barely exceeds always guessing the most frequent curve; when the correct option is removed, models almost never abstain, revealing heavy reliance on scene and brand priors. Supplying the vendor specification sharply improves recognition on calibrated charts but hardly helps on natural images without a photometric reference, exposing a gap between reading a specification and measuring pixels.

---


### 167. [A Unified Control Framework for Gradient Inversion Defense in Federated Learning](https://arxiv.org/abs/2611.32174)

**<font color=#1a73e8>作者：</font>** Lianhai Ren, Chi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient perturbations are widely recognized as an effective defense against gradient inversion attacks in federated learning, but they are equally known to impair optimization, creating a persistent tension between privacy and utility. In this paper, we show that existing gradient perturbation defenses, despite their different formulations, can be unified under a controlled dynamics framework, providing a cohesive understanding of their optimization behavior and enabling the derivation of universal convergence and safety conditions without relying on case-specific analyses. Leveraging this observation, we propose ``Near Orthogonal Gradient Projection (NODE)'', which injects perturbations only along directions orthogonal to the original gradient so that the defended gradient maintains a fixed cosine similarity with the true gradient. By preserving the first-order descent direction, NODE substantially reduces the optimization cost of strong perturbations while maintaining effective protection against gradient inversion attacks. We theoretically establish convergence guarantees under standard optimization assumptions and further show that, under mild conditions on the gradient distribution, NODE remains effective in preventing inversion attacks. Comprehensive experiments on multiple benchmark datasets, including CIFAR-10, ImageNet, and Chest X-ray, together with a variety of gradient inversion attacks, demonstrate that the proposed framework achieves an improved privacy--utility trade-off over existing defenses across a broad range of training settings.

---


### 168. [LoopFit: Retrofitting Pretrained Diffusion Transformers with Recurrent Refinement](https://arxiv.org/abs/2611.32175)

**<font color=#1a73e8>作者：</font>** Xiaocheng Lu, Haoxi Li, Dazhao Du 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling inference computation offers a way to improve diffusion transformers (DiTs), but taking more sampling steps leaves the depth of each denoising prediction unchanged. Recurrently reusing Transformer blocks increases computation within each step, allowing further refinement of hidden representations. Retrofitting pretrained models enables this capability without repeating pretraining, but requires blocks learned for fixed-depth computation to refine states produced by their own repeated application. The challenge is to use each additional pass to correct local errors without disrupting the structure established by earlier passes. We introduce LoopFit, which uses feedback from earlier passes to guide refinement at each image patch. Residual Attention Modulation (RAM) uses each patch's feature change in one pass to scale and shift its input to attention in the next. During training, Residual Relay Loss (RRL) gives greater weight to patches whose prediction errors persist across passes. A noise-dependent depth schedule speeds up sampling by using four passes at high noise and one at lower noise levels. At comparable cost, backbones trained with four passes solve more problems using recurrent depth than extra sampling steps. Across 12 visual puzzle settings, LoopFit solves 89.8% of boards, compared with 87.8% for the strongest baseline evaluated on all 12. Most of the gain comes from tracing long paths on mazes and frozen lakes.

---


### 169. [SolarFilNet-V4: Multi-Scale Transformer Vision with Physics-Informed Adaptive Post-Processing for Solar Filament Segmentation](https://arxiv.org/abs/2611.32193)

**<font color=#1a73e8>作者：</font>** Indra Agustian, Ruvita Faurina  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Solar filaments are cool, dense chromospheric plasma structures held by magnetic field lines above polarity inversion lines. Their destabilization triggers coronal mass ejections and severe space weather hazards. Segmenting individual filaments from ground-based GONG H-alpha observations (2048 x 2048 pixels) is challenging due to low contrast, turbulent fibrils, delicate barb structures, and annotator boundary variance. In this technical report, we describe SolarFilNet-V4, a targeted segmentation framework developed for the MAGFiLO 1.0 benchmark (Solar Filament Segmentation Challenge 2026). Our method couples a lightweight Pyramid Vision Transformer (PVT-v2-B1) backbone with anisotropic curvilinear strip convolutions (k=15) and dual-frequency feed-forward blocks (DFFN) to follow extended flux ropes while capturing thin central spines. A shallow full-resolution convolutional branch operating at 1024 x 1024 preserves high-frequency edge details and mitigates transformer downsampling. We train the network using multi-task supervision over masks, centerline spines, barb boundaries, and pixel-contrastive representations. At test time, we apply 8-fold dihedral test-time augmentation (D4), bilinearly upscale predictions to the native 2048 x 2048 grid, and apply an activity-adaptive post-processing routine that calibrates morphological joining parameters for quiet versus active solar disks. On the official benchmark, SolarFilNet-V4 achieves an out-of-fold validation Panoptic Quality of 0.4340 and a Public Leaderboard score of 0.380. The model contains 15.46M parameters and requires 224.34 GFLOPs per forward pass, reducing parameter count by 36.8% compared to standard ResNet-34 U-Net baselines.

---


### 170. [What to Change, What to Keep: Experience-Evolving Agents for Video Recasting](https://arxiv.org/abs/2611.32196)

**<font color=#1a73e8>作者：</font>** Shiying Zhang, Yuxia Zhu, Huaze Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video recasting aims to transform the entities and environments of existing videos into new visual worlds while preserving their essential actions and interactions. However, achieving coherent transformations remains challenging, as coordinated edits can disrupt the original event structure. In this paper, we introduce RecastAgent, an experience-guided agentic framework for source-conditioned video recasting that operates under frozen model weights. Our framework employs an Experience-Guided Planner to choose edit prompts and input video states under qualitative visual critique, allowing the agent to build upon partial progress or backtrack to preserve source structure. Across tasks, an Experience Accumulation module distills completed trajectories into conditional, evidence-linked principles that record both an editing strategy and its scope of validity. We additionally construct a benchmark of 67 source videos with 134 paired-specification tasks across six creative categories for evaluation. Experiments demonstrate that RecastAgent outperforms single-pass and agentic rewriting baselines across Bernini and Ditto. Furthermore, accumulated experience improves performance on held-out test videos and transfers zero-shot to external benchmarks like FiVE-Bench and VE-Bench.

---


### 171. [MoGe-4D: Efficient, Flexible, and Unified Dense 4D Reconstruction and Tracking](https://arxiv.org/abs/2611.32198)

**<font color=#1a73e8>作者：</font>** Ruicheng Wang, Linlin Xin, Sicheng Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic scenes from RGB video requires reasoning about both 3D geometry and motion across viewpoints, yet existing methods either split reconstruction and tracking into fragmented pipelines or face prohibitive dense spatiotemporal decoding costs. We introduce MoGe-4D, a feed-forward framework that unifies geometry and motion prediction via ordered queries of paired allocentric and egocentric dynamic point maps. Each query maps source pixels to a target time simultaneously in both camera frames, resolving relative camera pose in closed form while flexibly serving depth, dynamic registration, and dense 3D tracking. For efficient dense querying, MoGe-4D decouples scene modeling from query decoding: a high-capacity context encoder caches coarse global spatiotemporal features once, while a lightweight query encoder rapidly decodes dense point maps at flexible resolutions. Furthermore, as supervising dense 4D queries demands continuous 3D correspondences whose raw trajectory storage is prohibitive, we introduce RigIDTrack, a synthetic data pipeline and dataset that compresses surface dynamics into rigidity-regularized affine bodies, recovering exact arbitrary-frame 3D trajectories with $\sim15\%$ storage overhead over RGB-D video. Across diverse benchmarks, MoGe-4D achieves state-of-the-art dense 3D tracking, matches dedicated 3D foundation models in reconstruction, and runs substantially faster than prior 4D baselines.

---


### 172. [Who gets the information? An $α$-fair label-coverage framework for multi-label feature selection](https://arxiv.org/abs/2611.32200)

**<font color=#1a73e8>作者：</font>** Zhenzhi Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent information-theoretic filters for multi-label feature selection disagree on how to distribute relevance over labels: some amplify features that inform a few labels, others balance what every label receives. We show these choices are implicit social welfare functions. Treating labels as agents whose utility is the information they receive, we propose FLIC, which greedily maximises the $\alpha$-fair welfare of per-label information coverage. A single parameter $\alpha$ moves from utilitarian ($\alpha=0$) through proportionally fair ($\alpha=1$) to max-min selection ($\alpha\to\infty$), and a dozen published relevance terms lie on this axis, most as special cases, first-order approximations or limits. The objective is monotone submodular for every $\alpha\ge0$ whenever each label's information is, so greedy selection is a $(1-1/e)$-approximation; this fails for $\alpha<0$, and the max-min limit is inapproximable. Fano's and the Hellman-Raviv inequalities tie raw coverage to the Bayes Hamming loss and normalised coverage to per-label relative error. FLIC uses bias-corrected, label-wise conditional information and has no relevance-redundancy trade-off parameter. On 22 data sets, FLIC is the best of 14 information-theoretic filters on seven of nine metrics, winning 86 of 117 pairwise comparisons significantly and losing none significantly. Among 17 methods it ranks first on ranking loss, coverage and macro-AUC with two classifiers and has the best mean rank (narrowly with ML-kNN), while three embedded methods lead on Hamming loss, one-error and micro-F1.

---


### 173. [SplatTok: Data-Driven Compression of 3D Gaussian Splats with Scene-Level Tokens](https://arxiv.org/abs/2611.32202)

**<font color=#1a73e8>作者：</font>** Sai Karthikey Pentapati, Shashank Nelamangala Sridhara, Birendra Kathariya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian splats enable real-time rendering but require substantial storage. Existing compression methods either encode the primitives of a given splat or optimize a compact representation independently for each scene. Yet a Gaussian splat is only one realization of a scene: different arrangements of primitives can produce nearly identical rendered views. We exploit this freedom on the decoding side with SplatTok, a learned scene-resynthesis codec. Trained across thousands of real-world scenes, a transformer encodes an existing splat into compact, spatially anchored latent tokens, and a shared decoder synthesizes a new set of standard Gaussian primitives without preserving correspondence to the input. The representation is learned through rendering supervision rather than primitive reconstruction. At compression time, a quantization-aware latent search refines only the scene code, keeping the networks frozen, and closes most of the encoder's remaining error. On standard benchmarks, using only renders of the input splat for the latent search, without the original training images, SplatTok matches the PSNR of the feed-forward codec FCGS with 4 to 6.5 times smaller files, compressing input splats about 75 to 110 times. With the training images, it exceeds the PSNR of the per-scene method HAC++ with 13 to 41% smaller files. A single model trained on DL3DV generalizes to unseen scenes with millions of Gaussians and supports multiple target rates without retraining.

---


### 174. [FlashSegmentator: High-Throughput TotalSegmentator Inference without Loss of Accuracy](https://arxiv.org/abs/2611.32208)

**<font color=#1a73e8>作者：</font>** Yosuke Yamagishi, Tomohiro Kikuchi, Shouhei Hanaoka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: To develop, evaluate, and publicly release FlashSegmentator, an open-source inference pipeline that increases the throughput of TotalSegmentator without retraining or loss of segmentation accuracy. Materials and Methods: This retrospective study used public datasets: 73 CT examinations from the TotalSegmentator test split (median age, 65 years; 37 male, 35 female, one unknown), 30 abdominal CT examinations from the Beyond the Cranial Vault (BTCV) dataset, 512 training-split CT examinations for concurrent-process analysis, and 55 MRI examinations. FlashSegmentator adds static-shape compilation, pipelining, batched sliding-window inference, and GPU postprocessing. Throughput was compared with the reference implementation (including its lower-resolution modes) and FastSegmentator on GH200, A100, and T4 GPUs. Dice agreement was tested with two one-sided tests (margin, +/-0.01). Results: FlashSegmentator processed 3782, 1810, and 270 examinations per hour on the GH200, A100, and T4 (57.7, 33.9, and 6.4 times the reference implementation and 3.20, 2.50, and 1.22 times compiled FastSegmentator). Dice scores were equivalent for all 117 structures on every GPU (mean difference <= 1.2 x 10^-5; P < .001) and at the examination level on BTCV. In contrast, the lower-resolution modes of the reference implementation processed 181 and 213 examinations per hour on the A100 but reduced mean Dice by 0.116 and 0.241. On MRI, throughput increased 94-fold with all 50 structures equivalent. Estimated A100 cloud cost per 10,000 examinations decreased from 997 to 29 US dollars. Conclusion: FlashSegmentator increased the throughput of TotalSegmentator on data center and entry-level GPUs without loss of segmentation accuracy compared with the reference implementation.

---


### 175. [ArEssays: Towards Robust Arabic Handwritten Text Understanding in Educational Settings](https://arxiv.org/abs/2611.32211)

**<font color=#1a73e8>作者：</font>** Hamdy Mubarak, Anas Madkoor, Ehsaneddin Asgari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated understanding of handwritten Arabic student essays remains challenging due to script complexity and high variability
in children's writing. We introduce ArEssays, a large-scale dataset of authentic essays from primary to secondary students
across Egypt, with both verbatim transcriptions and linguistically corrected versions. We benchmark 34 vision-language and OCR
models, including fine-tuned systems, and find large performance gaps on real student handwriting. We release the dataset,
training pipelines, and results to support research in Arabic OCR, document understanding, and educational NLP.

---


### 176. [EvoSearch: Self-Evolving Active Perception for Wide-Area Geospatial Search](https://arxiv.org/abs/2611.32214)

**<font color=#1a73e8>作者：</font>** Zhenghao Xie, Jing Xiao, Zihao Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial search is fundamental to resource surveys and environmental monitoring, requiring the discovery of relevant evidence across large geographic areas and multiple spatial scales. Existing active perception methods adaptively select observation locations and scales to improve search efficiency, yet their search trajectories become increasingly long and costly as the search area expands. A key limitation is that final-answer correctness alone provides little guidance on which observations to retain and when to stop, hindering efficient wide-area search. To address this challenge, we propose EvoSearch, a self-evolving active perception framework that co-evolves the perception policy and exploration program to compress search trajectories while preserving answer quality. Specifically, quality-cost comparisons between completed branches from shared evidence train the policy to acquire useful observations, avoid redundant ones, and stop when sufficient evidence is available. Execution feedback from the updated policy then guides exploration-program revision, adapting experience generation to the policy's changing observation needs. We further introduce GeoSearchBench, a benchmark for evaluating search quality and visual processing efficiency through relational search and region search. Experiments demonstrate that EvoSearch shortens search trajectories and substantially reduces visual processing while maintaining overall search quality, supporting scalable active perception for wide-area geospatial search.

---


### 177. [PoseVLN: Learning Geometric State Evolution for Vision-Language Navigation](https://arxiv.org/abs/2611.32218)

**<font color=#1a73e8>作者：</font>** Pengyu Hou, Mingfei Han, Haihong Hao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Navigation (VLN) requires an embodied agent to relate past experience, current spatial state, and future motion while following natural-language instructions. Recent approaches improve these capabilities through long-horizon memory, state-aware reasoning, and future prediction, yet these components are often modeled separately, leaving navigation state evolution insufficiently connected across time. We argue that camera pose provides a natural geometric representation for bridging past, present, and future states. Based on this insight, we propose PoseVLN, a pose-aware VLN framework that jointly learns navigation decisions and geometric state evolution. PoseVLN organizes visual memory and the current observation in an episode-relative coordinate frame, and jointly predicts the next K navigation actions together with a local $\Delta$Pose over the same horizon. The predicted $\Delta$Pose is composed with the current trajectory-level pose to obtain the future pose state, which is recursively propagated throughout navigation, forming a continuous geometric state evolution from past memory to future motion. Experiments on the R2R-CE and RxR-CE Val-Unseen splits demonstrate the effectiveness of explicitly modeling geometric state evolution, with PoseVLN outperforming the strongest compared baselines by 2.6 and 2.9 percentage points in success rate, respectively, using only single RGB observations.

---


### 178. [FaceNet versus VGG Features in Wasserstein Distortion for Face Image Compression](https://arxiv.org/abs/2611.32220)

**<font color=#1a73e8>作者：</font>** Xinyu Wang, Jona Ballé  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wasserstein distortion (WD) compares local statistics of deep features and has been used to optimize learned image codecs for perceptual quality, but existing WD objectives rely on features from networks trained for generic image classification, such as VGG. We ask whether features from a face recognition network better reflect the perceived quality of compressed faces. In the Cool-Chic codec, we replace the VGG features in a WD-based objective with intermediate feature maps of FaceNet, and compare the two objectives on 20 LFW face images at a matched average bitrate of about 0.15 bits per pixel. In a preliminary pairwise human study, FaceNet-based reconstructions were preferred in 72.5% of judgments and by a majority of participants on 16 of the 20 images. These results suggest that the choice of feature network inside WD affects the perceived quality of face images, and that face recognition features are a promising direction for face-aware perceptual compression.

---


### 179. [Joint Classification and Generation on Tabular Data: an Empirical Study](https://arxiv.org/abs/2611.32225)

**<font color=#1a73e8>作者：</font>** Tim d'Hondt, Oleksii Furman, Damian Kwolek 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many applications of machine learning on tabular data need both a classifier and a generator of realistic records. The default is to train two separate models, whereas a single joint model promises both from one set of weights. Several families of tabular deep learning models can be turned into such a joint model, which raises the question of which joint model is preferable at which computational budget. In this empirical study, we introduce and compare joint models based on four state-of-the-art tabular data modeling families (energy-based models, probabilistic circuits, tabular foundation models and tabular diffusion models) against measured FLOPs and wall-clock time, on 29 classification datasets. Methods are evaluated based on two defined aggregate scores that take into account different aspects of prediction and generation. We then also compare these joint models with every pair of a separate classifier and generator at different computational budgets, to see when a joint model may be a defendible choice against the regular practice of keeping a separate classifier and generator. We find that the best joint model is a probabilistic circuit at the smallest budgets and, beyond that, a tabular foundation model that generates column by column using a regressor (TabICL). Compared with pairs of separate models, this study finds a joint model is rarely preferable but often very close to the best pair, without the hassle of training and maintaining two separate models.

---


### 180. [Relation Before Action: Explicit Relation Modeling for Latent Action Pretraining](https://arxiv.org/abs/2611.32226)

**<font color=#1a73e8>作者：</font>** Boning Zhang, Junyu Gao, Changsheng Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning latent actions from unlabeled video sequences offers a promising way to acquire reusable action representations without relying on embodiment-specific control annotations. However, existing latent-action pretraining approaches commonly couple the modeling of visual transitions with action inference, directly mapping paired observations or derived transition cues into latent action codes. This formulation leaves two distinct tasks entangled: characterizing the relational structure of an observed transition and abstracting it into a compact action representation. We propose RELACT, a relation-first framework that explicitly separates transition relation modeling from predictive action abstraction. RELACT first constructs a structured relation representation $R$ that captures how visual elements and their interactions evolve across observations. It then infers a compact, state-conditioned stochastic latent action $U$, whose predictive effects are learned through action-conditioned latent dynamics. The resulting action representation can be grounded in native control spaces for model-based planning or used to supervise downstream embodied policies. Extensive experiments across in-domain and out-of-domain image-goal navigation, goal-conditioned manipulation, and downstream policy adaptation demonstrate improved predictive action representations and consistent gains in planning and control, supporting the effectiveness and generality of relation-first latent action pretraining.

---


### 181. [ST-SfM: Spatio-Temporal Structure-from-Motion for Initialising 4D Gaussian Splatting](https://arxiv.org/abs/2611.32231)

**<font color=#1a73e8>作者：</font>** Harshit, Sami Brandt  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic Gaussian splatting is usually initialised either with random points or with a structure-from-motion (SfM) cloud of the first frame. Neither says anything about what moves, where and when. We introduce ST-SfM, a sparse spatio-temporal SfM for synchronised, calibrated multi-camera video that splits the scene into two branches. Static structure is detected once per camera on a temporal-median image, gated for temporal stability and matched along epi-polar lines. Motion is detected as space-time interest points (STIPs) in the video volume, described with HOG3D and matched only between candidates that agree both epipolarly and in time. Union-find tracks that refuse inconsistent merges are triangulated with RANSAC over all view pairs, giving static 3D points and dynamic 4D points (x, y, z, t) with sub-frame times. We use ST-SfM derived sparse 4D cloud to initialise 4D Gaussian splatting. In comparison with random initialisation on N3DV scenes we get improvements in PSNR, SSIM and LPIPS.

---


### 182. [MYSTIQUE: Few-Shot Facial Identity Transfer with Performance Preservation](https://arxiv.org/abs/2611.32232)

**<font color=#1a73e8>作者：</font>** Shihan Cheng, David Hyde, Junting Deng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In visual effects, identity transfer replaces the identity in a driving image with that of a target person, while preserving the expression, lighting, pose and scene of that image. Paired ground truth is rarely available, so many methods are trained by self-reconstruction, where the model can learn a shortcut by copying identity cues from the driving image. This shortcut causes identity leakage at inference, where the driving image shows a different person. Our key observation is that leakage can enter through any input that reads the driving image. We therefore present MYSTIQUE, a diffusion-based identity transfer method that takes identity from a set of the target's photos and reads expression, lighting and scene through separate streams. It learns to disentangle identity from the other streams through multi-stage training, with disentanglement strategies at their inputs: a random block mask whose boundaries do not follow the face outline, self-augmentation, which randomly changes the face shape in the expression input and keeps its expression, and face randomization, which replaces the person in the expression and lighting inputs while the ground truth stays the driving image. At inference, we also warp the lighting input onto the face shape of a first pass, which reduces face-shape leakage through the lighting stream. Since face-recognition scores and human judgments each have limits, we evaluate identity with both, together with face-shape metrics on rendered faces of known shape. In a user study, raters judge MYSTIQUE's results more like the target than those of each compared method. Among these methods, MYSTIQUE also recovers the target's face shape most accurately, and its recognition score gains the most as more photos of the target are given.

---


### 183. [Can You Find the Edit When Nothing Looks Wrong? A Paired Benchmark for Text-Driven Image Manipulation Localization Beyond Semantic Abnormality](https://arxiv.org/abs/2611.32242)

**<font color=#1a73e8>作者：</font>** Peiyu Zhuang, Jianquan Yang, Zhuoying Cai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-driven image editing can alter a photograph while keeping the result coherent with the scene. Existing benchmarks lack matched plausible and anomalous edits of the same target, making it difficult to measure how localization performance changes with semantic plausibility. We construct a paired benchmark by generating semantically plausible and anomalous replacements of the same target in each source photograph. Both edits use the same editor, language, and generation settings. We estimate a separate mask for each output and retain pairs with sufficient mask overlap, enabling direct comparison of localization performance under the two semantic conditions. The release contains 47,747 bilingual triplets from 6,500 photographs, spanning four editors, three source domains, and six intended violation types. Across nine public localizers, editor-averaged IoU is lower on plausible edits in 26 of 27 model-dataset comparisons. This gap persists under pixel-change controls and region-size analyses. These findings reveal a semantic-plausibility shortcut: localization often weakens when an edited result looks ordinary. The benchmark provides a controlled setting for measuring this gap and developing localizers that remain effective on plausible edits.

---


### 184. [Seldon TFM family: Seldon-Mini, Seldon and Seldon+](https://arxiv.org/abs/2611.32257)

**<font color=#1a73e8>作者：</font>** Stanislas Angebault, Nicolas Atienza, Nicola Cancedda 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Seldon, a family of tabular foundation models. Our classifier Seldon+ ranks first among 15 models on TabBench, our benchmark of 124 classification datasets, and on its variant with missing values. In our own runs of public benchmarks, it also ranks first on BeyondArena IID classification and TabBench-Bio, and second on TabArena classification. The open-weight models Seldon-Mini (27M parameters) and Seldon (213M parameters) both lie on the TabArena Pareto front of Elo against inference time: no entry is both more accurate and faster. On TabArena, Seldon ranks fourth and Seldon-Mini seventh among 109 leaderboard entries, and on the IID track of BeyondArena, Seldon ranks second among 42 entries. Seldon-Mini and Seldon handle both classification and regression, use an architecture similar to those of Kumo-Tabular, TabFM and TabPFN-3.5, and are trained on synthetic tables only.

---


### 185. [CoMNO: Commutator Memory Neural Operators for Long-Horizon PDE Prediction](https://arxiv.org/abs/2611.32274)

**<font color=#1a73e8>作者：</font>** Han Xiao, Xin Zhang, Yuhan Zou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving nonlinear partial differential equations (PDEs) over long time horizons is computationally expensive using traditional numerical methods. While neural operators provide an efficient alternative, they suffer from the accumulation of approximation errors along the predicted trajectory, typically caused by the failure to capture fine-scale details. In this work, we design a Commutator Memory Neural Operator that identifies fine-scale dynamical details by commuting two operations and leverages these details to enhance the neural operator's capability in capturing fine-scale features over long time horizons. Specifically, we identify a performance gap between two operations: downsampling the high-resolution field before rollout prediction versus performing rollout prediction before downsampling. We observe that fine-scale dynamical details are often encoded in this gap. By commuting these two operations, the fine-scale details removed during downsampling can be captured. Furthermore, we employ a memory module to store these fine-scale features along the trajectory and retrieve them during rollout, generating spatially adaptive corrections that enhance long-horizon fidelity. Empirical results across five systems demonstrate that CoMNO improves prediction accuracy and long-horizon rollout stability.

---


### 186. [$ε$-Seg++: Ensembling Across Hierarchy and Training Time for Label-Efficient EM Segmentation](https://arxiv.org/abs/2611.32290)

**<font color=#1a73e8>作者：</font>** Edoardo Giacomello, Sheida Rahnamai Kordasiabi, Mehdi Seifi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation of electron microscopy (EM) volumes is a central step in quantitative cell biology, but dense voxel-wise annotation is prohibitively expensive. $\epsilon$-Seg showed that a hierarchical variational autoencoder trained on sparsely annotated voxels can yield competitive segmentations, but it classifies from its topmost latent level only and operates exclusively on 2D patches. We introduce $\epsilon$-Seg++, which places a semantic expert at every level of the hierarchy and consolidates their predictions with a parameter-free product of experts. We further enable 3D inputs through a leakage-free sub-volume splitting protocol, which allows 2D and 3D models to be compared under identical sparse supervision. Because validation labels are just as scarce as training labels, we treat checkpoint selection as part of the method and average the top-ranked checkpoints, a second ensemble, this time across training time. On the BetaSeg FIB-SEM dataset, the multi-level experts improve 2D mean Dice by about 0.1 at 2,500 training labels. With up to 600 training labels, the 2D model matches or exceeds 3D $\epsilon$-Seg at about one eleventh of its prediction cost. Above roughly a thousand labels, 3D inputs dominate, and at matched annotation cost 3D $\epsilon$-Seg++ reaches a mean Dice of 0.905 versus 0.880 for D3PM, while predicting between 5.4 and 27 times faster (with our checkpoint ensemble or a single model, respectively). Checkpoint ensembling matches single-best selection on average and markedly improves the worst case when the validation set is small.

---


### 187. [ArabFake: A multitask deep learning framework for Arabic fake news Detection, Categorization, and risk prediction](https://arxiv.org/abs/2611.32303)

**<font color=#1a73e8>作者：</font>** Ahmed Maher Khafaga Shehata, Mohammed Nasser Al-Suqri, Nour Eldin Mohamed Elshaiekh Osman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The spread of fake news among Arabic media including social media represents a great challenge to the integrity of information and the trust of the public in it. In this paper, we introduce a comprehensive deep-learning framework, named ArabFake, that goes beyond the binary classification on Arabic fake news detection. ArabFake, built over MARBERTv2 (a state-of-the-art model for multi-dialectal Arabic tweets), proficiently address the complexity of the Arabic language while performing three unified tasks which are fake news detection, content categorization and its risk assessment. The framework promotes efficiency and performance both by enabling multi-task learning through shared knowledge representation across tasks. In order to facilitate development and evaluation, we present the ArabFake Dataset consisting of 2,495 manually labelled news items with labels that are verified by experts regarding fake news categories and risk levels. ArabFake demonstrates robust performance, achieving an F1 score of 94.12% for fake news detection, 84.92% for categorization, and 88.91% for risk zone assessment, highlighting its reliability and effectiveness across multiple tasks. We improve interpretability and extract insight into manipulative techniques by integrating valence scoring as part of the framework that emphasizes misleading linguistic cues used to disseminate fake news within the produced image. The results show that ArabFake is a holistic Arabic fake news detection framework that has practical implications on news organizations and fact checking projects.

---


### 188. [CREDIT: Compositional Reliability Learning for Noisy Composed Image Retrieval](https://arxiv.org/abs/2611.32310)

**<font color=#1a73e8>作者：</font>** Tiancai Zhou, Yongxiang Li, Suimei Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) aims to retrieve a target image that satisfies user intent based on a multimodal query consisting of a reference image and a modification text. However, real-world training data are often corrupted by Noisy Triplet Correspondence (NTC), where the semantic correspondence among the reference image, modification text, and target image becomes unreliable. Existing methods implicitly assume that the correctness of triplet correspondence can be determined by fixed decision rules. However, under NTC, the authenticity of semantic correspondence is difficult to determine accurately, and different triplets exhibit varying degrees of semantic reliability rather than binary correctness. Consequently, deterministic confidence is insufficient to faithfully characterize correspondence reliability, often leading to overconfident supervision for unreliable triplets and progressively reinforcing noisy semantics during compositional representation learning. To address this challenge, we propose a Compositional Reliability learning framework with Evidential uncertainty and DiffusIon-guided refinemenT (CREDIT), which explicitly quantifies the uncertainty of triplet correspondence to estimate its reliability and suppress the propagation of noisy supervision. CREDIT consists of two complementary components: The Evidential Compositional Uncertainty Learning (ECUL) module explicitly models correspondence uncertainty via evidential learning, enabling uncertaintyaware reliability estimation to suppress noisy supervision. Building upon the reliable supervision provided by ECUL, the Diffusion-enhanced Reference Refinement (DRR) module further refines reference representations through textconditioned diffusion, producing more robust compositional query features. Extensive experiments demonstrate that CREDIT consistently outperforms existing methods under various settings.

---


### 189. [SynAVID: A Synthetic Audio-Visual Immersive Dataset of Dynamic Scenes](https://arxiv.org/abs/2611.32311)

**<font color=#1a73e8>作者：</font>** Jun Xu, Sujing Li, Chunhao Bi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Immersive scene modeling requires synchronized visual and auditory observations under changing viewpoints and scene conditions. Obtaining such observations and references for controlled scene changes remains challenging. We introduce SynAVID, a synthetic audio-visual immersive dataset comprising eight indoor and outdoor scenes. Each minute-scale episode combines fixed camera arrays and moving trajectories with synchronized, viewpoint-dependent binaural audio. Shared scene dynamics, sound-source events, and observer poses drive visual rendering and geometry-aware acoustic synthesis. We evaluate existing methods for visual reconstruction, binaural audio reconstruction, and audiovisual editing. Mixed-observation configurations generally improve visual reconstruction on fixed and moving test views, while transiently occupied and sparsely observed regions remain challenging. Methods rank differently on spectral, interaural, and perceptual audio metrics. Geometric and instance annotations expose uneven observation support and local Gaussian representations beyond aggregate scores. Paired references assess target edits and surrounding content, while controlled geometry changes produce listener-dependent acoustic responses. The project page is available at this https URL.

---


### 190. [SPRUNN: Structural Proximity for Pruning in Deep Neural Networks](https://arxiv.org/abs/2611.32317)

**<font color=#1a73e8>作者：</font>** Babak Rokha, Ali Azarpeyvanda, Alireza Khanteymoori 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Neural Networks (DNNs) have demonstrated significant accuracy across various machine learning tasks. However, these networks suffer from a huge number of parameters and computations, which leads to time-consuming processes. Consequently, parameter pruning approaches have been proposed to compress DNNs and efficiently implement them. The main challenge in pruning is selecting the appropriate parameters for pruning without significantly damaging the accuracy. In this paper, we propose SPRUNN, an algorithmic pruning approach based on the structural proximity criterion for filter pruning in convolutional layers of deep neural networks. Structural Proximity (SP) calculates filter similarity by considering all filters and comparing each one with the others, effectively identifying less important filters for pruning in the convolutional layers. Furthermore, we integrate this approach with fine-grained pruning in Fully Connected(FC)layerstocompresstheDNNsthatinclude both convolutional and FC this http URL,weproposealearning rate refinement strategy during the retraining phase. Experimental results demonstrate that SPRUNN achieves significant compression with high accuracy across diverse architectures and datasets.

---


### 191. [Alpha-Beta Pruning via Monadic Continuations](https://arxiv.org/abs/2611.32320)

**<font color=#1a73e8>作者：</font>** Martín Escardó, Paulo Oliva  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Alpha-beta pruning is a fundamental technique in game-playing AI, enabling efficient minimax search by avoiding the exploration of branches that cannot affect the optimal decision. We present a monadic formulation of alpha-beta pruning based on the combination of the continuation monad and the reader monad. Unlike previous approaches that encode alpha-beta bounds into the types of available moves, our construction records these bounds within monadic outcomes, leaving the move types unchanged. We further show that the ordinary continuation monad suffices to compute not only optimal outcomes but also optimal plays, by extending the outcome type to include the corresponding sequences of moves. This provides an alternative to generalisations of the continuation monad proposed to address the inefficiencies associated with the selection monad in alpha-beta search. We illustrate our approach with an implementation of Tic-Tac-Toe, observing a 39-fold reduction in the number of plays evaluated, compared with exhaustive search, in computing an optimal play. Finally, we formally establish the correctness of our construction by proving that the monadic alpha-beta search computes the same optimal outcomes and plays as exhaustive minimax search. Our results demonstrate how a foundational algorithm in AI can be expressed and verified using standard monadic abstractions, providing a basis for further development of compositional approaches to adversarial search.

---


### 192. [FigmaEval: A Benchmark for Evaluating AI Agents in Professional UI Design](https://arxiv.org/abs/2611.32321)

**<font color=#1a73e8>作者：</font>** Xinyue Huang, Yongyong Gao, Zhengyuan Pan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in AI agents have enabled autonomous UI design using professional tools such as Figma, yet evaluating their design capabilities remains challenging due to the open-ended nature of design tasks and the absence of unique ground truths. We introduce FigmaEval, a benchmark for evaluating AI agents on professional UI design tasks, comprising 84 tasks and 783 screens derived from real-world Figma design files. FigmaEval adopts a constrained-specification, open-solution paradigm, standardizing task requirements and design resources while allowing agents to independently determine layouts, visual hierarchies, component composition, and visual presentation. To assess design quality beyond reference similarity, we develop 22 expert-grounded evaluation rubrics across six dimensions and introduce a human evaluation arena where professional designers compare agent-generated designs through blinded pairwise judgments. Evaluating eleven models under a unified Figma agent setup, we find substantial agreement between rubric-based assessments and human preferences, alongside distinct differences in design practices and quality--efficiency trade-offs. FigmaEval provides a framework for systematically assessing professional UI design capabilities and understanding the strengths and limitations of current AI agents.

---


### 193. [A recursive self-improvement framework for electron microscopy analysis](https://arxiv.org/abs/2611.32325)

**<font color=#1a73e8>作者：</font>** Yaotian Yang, Sijia Tao, Yuping Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Resolving local atomic structures such as defects and interfaces from electron microscopy contrast relies heavily on researcher judgement, leading to low efficiency and subjective standards. Here we present PhyEvo-Mic-RSI, a physics-guided and expert-informed recursive self-improvement framework that turns one-off human corrections into reusable, verifiable capabilities by updating executable operators, parameters and routing rules with versioned inheritance. Given researcher-defined tasks, the system selects analysis paths from image features without expert labels, while testing and inheriting code updates under fixed budgets. Combining physical priors with expert feedback improves atomic point-defect detection over larger models and raises cross-material interface coverage from 5.13% to 72.11% within a 10% area budget. Adapting the framework to micrographs from unseen studies further separates touching nanoparticles by aligning optimization with particle-level measurements. This work moves computational microscopy beyond standalone models and static scripts towards self-evolving platforms that accumulate human scientific expertise

---


### 194. [Longitudinal Characterization of Personalized Hydration Dynamics Using a Facial-Video Digital Hydration Biomarker](https://arxiv.org/abs/2611.32326)

**<font color=#1a73e8>作者：</font>** Janindu Athukorala, D.M.J. Prathapa, Thanveer Ahamed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background. Hydration is often assessed at a single time point despite continuous changes in body water. A facial-video biomarker has tracked hydration-state transitions, but its longitudinal behavior is unclear.
Objective. To assess within-person hydration score changes, individual differences in fluid response, and implications for personal calibration.
Methods. Five adults completed water and electrolyte days with an identical 2.0 L fluid schedule, using facial videos every 30 minutes over 12 hours (250 videos). On a separate morning, each completed a 500 mL electrolyte challenge with baseline and four follow-up videos over 2 hours (25 videos). Analyses assessed trajectories, post-drink changes, variability, time at or above score 50, and exploratory effects of starting score and beverage day.
Results. The first scan was the day's lowest on 7 of 10 days. Across 50 intakes, the mean post-drink change was +4.0 points, exceeding a shuffled-time comparison (p less than 0.001). For 21 intakes starting below 50, no subsequent score fell; the mean rise was +11.3 points versus +5.7 expected under permutation (p less than 0.001). Intakes starting at 50 or above showed no rise beyond chance. After 500 mL electrolytes, mean change over 2 hours was positive for all five participants, with peak increases of 7.2 to 22.6 points at 30 to 90 minutes. Despite identical fluid schedules, time at or above 50 ranged from 16% to 100%. The electrolyte day showed a greater mean increase from morning baseline than the water day (+7.7 points), although day order was fixed.
Conclusion. Facial-video hydration scores showed longitudinal changes associated with drinking and marked individual differences. These exploratory findings support further research on personal calibration and hydration protocols in larger controlled studies.

---


### 195. [FlowVecFont: Scalable Vector Font Generation via Latent Flow Matching](https://arxiv.org/abs/2611.32327)

**<font color=#1a73e8>作者：</font>** Takumu Fujioka, Gouhei Tanaka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fonts are natively represented as vector outlines. Many existing studies on vector font generation have relied on specialized generation or refinement mechanisms, bitmap representations, or externally pretrained models to address the challenges of learning vector representations. These approaches often increase system complexity, incur additional computational and implementation costs, and introduce dependencies on external resources. We show that scaling a simple model enables high-quality pure vector font generation without external pretraining. We propose FlowVecFont, a scalable model for vector font generation based on latent flow matching and trained solely on vector outlines. A Transformer-based variational autoencoder maps glyph sequences into fixed-length continuous latent tokens, enabling standard conditional flow matching for vector glyph generation. The model supports conditioning on class labels or reference glyphs, with the latter enabling generalization to unseen characters and fonts. Experiments on 5M glyphs collected across Google Fonts, including non-Latin characters, show that generation quality improves with model scale across conditioning strategies. In a comparison on Latin glyphs, the 800M-parameter FlowVecFont outperforms DeepVecFont-v2 and DesigNet and achieves quality competitive with the pretrained 27B-parameter VecGlypher. We also provide TorchFont, a machine learning library for vector fonts.

---


### 196. [Cross-Version Compatibility of TESSERA Embeddings Through Lightweight Translation](https://arxiv.org/abs/2611.32329)

**<font color=#1a73e8>作者：</font>** Yutong Yang, Zhengpeng Feng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Downstream models often outlive the embedding release on which they were trained. We test whether lightweight converters let a classifier trained on one Tessera release use embeddings from another. We fit converters between v1, v1.1, and v2 on 6,280 co-located triplets from 25 sites in 2024, with disjoint training, validation, and test sites. On a four-class land-cover test, a classifier trained on true v2 reaches 0.937 accuracy and 0.844 macro-F1. The same classifier scores 0.061 and 0.050 on raw v1.1, but 0.917 and 0.795 on converted v1.1. Direct v1-to-v2 translation has lower error than composition through v1.1. Geographic transfer is less reliable. On a separate cohort of 20 sites, a converter trained on the original sites reaches 0.597 accuracy despite 0.902 cosine similarity to v2, whereas a converter trained within the new cohort reaches 0.784. Tests with 2021 WorldCover labels and at 24 sampled sites without valid native v2 values extend the evaluation. Conversion recovers much of the frozen classifier's performance on the tested sites, but the new-site result shows that embedding similarity cannot stand in for downstream evaluation.

---


### 197. [GUI-WEdit and GUI-SkillEvo: Gradient-Free Adaptation of Small GUI Agents](https://arxiv.org/abs/2611.32332)

**<font color=#1a73e8>作者：</font>** Haixia Bi, Yingtian Chen, Sihan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small graphical user interface (GUI) agents can execute desktop workflows, but repeated local errors and fragile procedural decisions limit their reliability. We present GUI-WEdit-4B and GUI-SkillEvo-2B, two gradient-free adaptations of GUI-Owl-1.5 backbones. For the 4B model, we use trajectory feedback to construct guarded, closed-form updates to a late multilayer perceptron (MLP), retaining successful states as protection constraints. The final checkpoint changes 23,739,095 parameter values, or 0.535\% of the 4,437,815,808-parameter backbone, within one weight tensor. For the 2B model, an assistant iteratively proposes and refines procedural skills while the model weights remain fixed. On the 361-task OSWorld subset excluding Google Drive tasks, the frozen systems obtain final aggregate scores of 48.02\% and 45.47\%, respectively.

---


### 198. [GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM](https://arxiv.org/abs/2611.32335)

**<font color=#1a73e8>作者：</font>** Weicong Zhang, Yuan Huang, Yu Zheng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoramic cameras capture nearly the entire spherical field of view in a single frame. However, the mismatch between this panoramic coverage and the field of view of LiDAR poses a substantial challenge for panoramic Gaussian splatting SLAM that relies on LiDAR depth priors. We introduce GOLD-SLAM, a Gaussian-splatting Omnidirectional LiDAR-Depth SLAM system that combines high-quality rendering with accurate geometric reconstruction. It performs tracking and mapping in the spherical domain and uses tracked visual features in regions without LiDAR coverage to improve pose estimation. To address insufficient coverage of newly observed surfaces and floating artifacts during incremental mapping, we introduce Depth-Aware Map Extension and Pruning (DAEP). To enable broader evaluation, we collect a new dataset, WHOLE, using a UAV platform across Weak-geometry, High-dynamic, Omnidirectional, Low-light, and Easy scenarios. Extensive experiments on public benchmarks and WHOLE demonstrate competitive rendering quality and improved geometric accuracy relative to perspective systems. Compared with existing panoramic baselines, GOLD-SLAM improves mean PSNR by 5.56-9.10 dB and reduces mean Depth-L1 by 71.9-83.9%. To assess deployment feasibility on resource-constrained platforms such as UAVs, we evaluate an embedded configuration of GOLD-SLAM on a Jetson Orin NX (16 GB), demonstrating online operation at the cost of reconstruction quality.

---


### 199. [Get the Next Moment Right: Short-Term Event Planning for Physically Plausible Video Generation](https://arxiv.org/abs/2611.32337)

**<font color=#1a73e8>作者：</font>** Hao Liu, Xiang Tang, Ruotong Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models synthesize realistic imagery yet still struggle to produce physically plausible evolution. Existing methods guide generation with a motion trajectory predicted for the entire clip in advance, so prediction errors accumulate and degrade later frames. We propose STEP(Short-Term Event Planning), a training-free closed-loop framework that guides generation one short clip at a time. Each round consists of four steps: grounding measures the scene state from the latest frames, event planning predicts the next physical event and renders it into a control clip, latent-guided generation produces the next short clip under this control, and verification checks whether the event occurs and resamples the clip if it does not. Because each round is grounded in the frames actually generated, control relies only on reliable short-range predictions. STEP improves the physical plausibility of three frozen generators on Physics-IQ Verified and PhyGenBench, and can be applied to new generators without training.

---


### 200. [Part-Set Prototypes for Explainable Mountain Gazelles Sex Classification](https://arxiv.org/abs/2611.32343)

**<font color=#1a73e8>作者：</font>** Tali Boneh Shitrit, Amir Kedem, Ilan Shimshoni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-explainable visual models for fine-grained recognition are often hindered by rigid geometric constraints that cannot capture diverse semantic shapes in unconstrained "in-the-wild" imagery. Real-world camera-trap data introduces challenges, including non-optimal poses, lighting variations, occlusions, animal camouflage, and environmental shortcuts. To address this, we introduce set prototypes, a general architecture where both part cardinality and unconstrained spatial layouts are mined directly from data. Our joint-matching formulation places parts simultaneously on a frozen DINOv3 token grid via truncated Sinkhorn competition, allowing unsupported parts to abstain without spatial collapse. We evaluate our approach on Mountain Gazelle sex classification, a camera-trap benchmark, where our model achieves 0.878 macro-F1--outperforming prior architectures and at par with an unconstrained linear probe. The strongest prototypes localize to distinctive biological areas such as horns, neck and body, allowing ecologists to visually verify decisions before trusting the metric. This formulation generalizes naturally to diverse ecological monitoring challenges beyond a single species.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-342](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
