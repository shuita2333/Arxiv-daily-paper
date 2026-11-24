# 📦 其他研究 | 2026年11月25日

> 本类共 **569** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

---

### 201. [A Finite-Rate Selection Law for Annealed Gibbs Sampling](https://arxiv.org/abs/2611.29041)

**<font color=#1a73e8>作者：</font>** Izhar Ali, Muhammad Haris Khan, Saeed Ahmad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Annealed Gibbs sampling samples a multimodal model by redrawing one variable at a time from its conditional distribution as the temperature falls from a high value, where the distribution is broad, to the target temperature. Each run ends in a single mode, and unbiased Monte Carlo estimates require the runs to end in each mode in proportion to its probability under the model. At a finite cooling rate this can fail. We measure the error by $c$, the fraction of the model's log-odds between two modes that the samples retain. In the Curie--Weiss model, where a weak external field favors one of two modes, each run selects its mode near the transition at which the modes form, and rarely switches once they have separated. Near the transition, the random fluctuations of the Gibbs updates still outweigh the weak field, which therefore biases the choice of mode only slightly. Building on the selection probability of Kondepudi and coworkers, we derive a law for $c$ that agrees with an exact computation to within $2\%$ on nine linear cooling ramps. For the Hopfield model, whose modes are stored patterns and their negatives, we derive a factor by which competition among patterns raises $c$. The $c$ measured over random pattern sets lies within $3$--$6\%$ of its prediction, but single pattern sets depart from it, contrary to its derivation.

---


### 202. [Mirror Descent at the Edge of Stability](https://arxiv.org/abs/2611.29043)

**<font color=#1a73e8>作者：</font>** Vincent X. Wang, Vikas Garg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many deep learning settings, gradient descent has been shown to operate at the edge of stability -- a regime where the largest eigenvalue of the loss Hessian hovers around $2/\eta$. We study this phenomenon in mirror descent, a generalization of gradient descent. As mirror descent is non-Euclidean, existing explanations of the edge of stability phase do not extend to this setting. We generalize the existing notion of sharpness to introduce mirror sharpness, which measures the curvature of the loss with respect to the mirror potential. Empirically, we observe that the mirror sharpness hovers slightly above the $2/\eta$ threshold. Furthermore, we derive a dual central flow ODE for mirror descent that models iterates in continuous time at the onset of edge of stability. Our ODE provides insights into the difficulties of extending existing arguments for why sharpness stabilizes at $2/\eta$ from gradient descent to mirror descent in full generality.

---


### 203. [Certified Comparative Statics for Conservation-Law Equilibrium Layers, with an Application to RNA Interference](https://arxiv.org/abs/2611.29050)

**<font color=#1a73e8>作者：</font>** Shadi Khodagholi, Sara Karimi, Niloofar Yousefi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Implicit and equilibrium neural layers define their output as the fixed point of a map. Existing theory certifies that this fixed point exists; it does not certify how it responds to its inputs. For a conservation-law layer with order-preserving coupling we give a form-independent answer: every input-output comparative static is sign-certified if and only if the residual Jacobian is a nonsingular M-matrix, and the certified sign depends only on the sign of the occupancy derivative, so one guarantee covers Langmuir, Hill, and saturating-exponential occupancies. The M-matrix machinery is classical; the contribution is form-independence as the portable invariant, the first certified-sign sensitivity result for a layer of this class, and a sharp phase boundary at which certification is lost while the equilibrium remains well posed. Three consequences follow: the phase boundary, which is strictly stronger than the M-matrix condition; competitive derepression, whose derivative is identically zero for any independent per-target scorer and provably nonzero here; and non-submodularity of resource-coupled suppression. We instantiate on siRNA off-target competition and validate on real public data only, across seventeen microRNAs, two titration studies, and a paired chemical-modification experiment; a second, non-biological instantiation shows the same certified sign on measured physical data. As a trainable layer the operator learns end-to-end while remaining certified-monotone by construction, reaching magnitude parity with a parameter-matched feedforward baseline while expressing a competition effect that baseline cannot represent for any weights. The single-pool instantiation validates the mechanism but does not rank off-target magnitude or resolve position-specific design. Code: this https URL

---


### 204. [Hypothesis Generation and Semantic Attribution in Inverse Perturbation Modeling](https://arxiv.org/abs/2611.29055)

**<font color=#1a73e8>作者：</font>** Pascal Passigan, Manolis Kellis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding gene regulatory relationships at scale can help identify intervention points and anticipate unintended effects, but connecting a black-box model's learned computation to biological knowledge remains difficult. We investigate whether a sparse, typed gene network can generate inspectable hypotheses for steering malignant transcriptional programs toward expression patterns associated with favorable prognosis. Using LINCS L1000 CRISPR/Cas9 profiles paired with matched plate controls, we train a graph neural network to recover the perturbed gene from baseline and endpoint expression. Nodes combine ProTrek-derived protein representations with expression features; edges encode signed regulatory relationships and other gene interactions. We use this inverse formulation to nominate interventions for a desired multigene expression change in a specified cancer-cell context, and use integrated gradients and conductance along a path from the cell baseline toward the requested endpoint to attribute each nomination to gene states, typed messages, and residual connections. In A549, the model nominates TTK although its expression is unchanged in the request; the account assigns supporting credit through the checkpoint-associated MAD1L1 relationship and opposing credit through the E2F4 transcriptional-regulatory channel. Across 333 screened nominations in nine held-out cell lines, request-path attribution shows positive line-averaged correspondence with finite message-deletion effects at every transition. Existing TTK knockout measurements show requested-direction agreement across other markers at the 98.2nd percentile (10 wells), and ten of seventeen measured cases in the illustrative screen meet the predefined support criterion. These analyses make competing biological accounts of a nomination examinable and open to experimental test.

---


### 205. [DiRGeo: Learning Directional Geometry of Visual Representations](https://arxiv.org/abs/2611.29057)

**<font color=#1a73e8>作者：</font>** Muhammad Ahtesham, Xin Zhong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional geometric measures of visual representations are symmetric, assigning equal costs to forward and reverse motion along the same path. We propose DiRGeo, a framework for learning directional geometry over frozen visual representations. Grounded in Randers geometry, DiRGeo learns a state-dependent directional field from ordered image trajectories through self-supervised contrast, without semantic labels. Sphere-tangent correction and attractor-relative decomposition distinguish learned directional structure from normalization artifacts and common convergence. Experiments across 17 visual processes, three encoder families, and multiple representation depths demonstrate consistent directional discrimination and whole-path asymmetry beyond simple attractor-based explanations. The learned fields become increasingly process-specific in deeper representations, while natural-video experiments reveal event-dependent directional preferences. As functional validation, DiRGeo guides restoration selection. These results establish directional geometry as a useful complement to symmetric representation analysis.

---


### 206. [Recurrent Point Transformer via Test-Time Training](https://arxiv.org/abs/2611.29059)

**<font color=#1a73e8>作者：</font>** Wentao Zhou, Xuweiyi Chen, Charles Saunders 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world point clouds are not naturally bounded: 3D scans grow as sensors move through rooms, LiDAR surveys extend across forest plots, and 4D captures can span thousands of frames. Yet most point-cloud encoders are designed for fixed-size inputs, forcing inference-time cropping or tiling that loses long-range context and requires ad-hoc output stitching. We formulate arbitrary-extent point-cloud segmentation as recurrent sequence-of-chunks processing and introduce PoinTTT, a recurrent point-cloud encoder built on Point Transformer V3 (PTv3). PoinTTT augments PTv3 with residual Large Chunk Test-Time Training (LaCT) layers in both the encoder and decoder. Each LaCT layer maintains compact fast weights as recurrent state: tokens from each chunk update the fast weights, which are then applied to produce chunk features and passed to the next chunk. This design allows PoinTTT to train on fixed-size chunks while processing scenes of arbitrary spatial or temporal extent, with activation memory bounded by the chunk size. A pilot study on ScanNet and nuScenes shows that recurrent TTT improves segmentation over PTv3 baselines. On FOR-instanceV2, PoinTTT achieves state-of-the-art forest semantic segmentation of 87.9 mIoU with nearly constant memory. On HOI4D, online full-sequence recurrent inference carries state across clips rather than resetting at benchmark boundaries, reaching 42.6 mIoU; a matched full-sequence Mamba control reaches approximately 39.9. These results suggest that test-time training is a practical primitive for scalable spatial and temporal point-cloud understanding.

---


### 207. [HyperHarness: Learning to Generate Personalized Agent Harnesses from User Histories](https://arxiv.org/abs/2611.29062)

**<font color=#1a73e8>作者：</font>** Zhaoxuan Tan, Jiachen Zhao, Jingbo Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized LLM agents rely on an agent harness, the surrounding memory and control code, to connect user history with downstream decisions. Existing methods typically employ either a single shared memory workflow across all users, which is efficient to deploy but cannot adapt how evidence is retrieved and interpreted across diverse histories, or per-user harness optimization, which customizes behavior for each user but requires costly repeated candidate evaluation at deployment and suffers from sparse, noisy supervision in raw logs. To address this trade-off, we present HyperHarness, a framework that learns a shared history-to-harness generator to synthesize executable, user-specific retrieval and answer-guidance code directly from user histories. Given a user's permitted history, HyperHarness prompts a construction LLM to write personalized retrieval and guidance functions, while downstream task scores across training users supervise iterative refinements to the shared generator without reference harnesses or answering-model updates. At deployment, the frozen generator constructs a harness for each unseen user in a single pass from history alone, eliminating per-user task-scored search. Across three benchmarks (PersonaMemv3, Mem-PAL, and MemoryCD) and three answering models (Qwen3.5-9B, Qwen3.8-27B, and GPT-5.6-Luna), HyperHarness achieves the highest aggregate score in seven of nine settings and ranks second in the remaining two, improving over the strongest baselines by up to 5.95 points while cutting matched answer-time tokens by 90.32% over long-context prompting. Analyses show that optimization tailors context allocation to each executor, transfers to unseen user clusters, and amortizes adaptation costs.

---


### 208. [Single-Transformer Latent Diffusion](https://arxiv.org/abs/2611.29064)

**<font color=#1a73e8>作者：</font>** Hao-Yu Hsu, Shenlong Wang, Alexander G. Schwing  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent generative models typically rely on three separate networks: an encoder that tokenizes pixels, a generator that models the latent distribution, and a decoder that maps latents back to pixels. UNITE recently merged the first two into a single generative encoder trained in one stage, but its decoder remains a separate network. We ask whether this last network can be folded in too, so that one diffusion transformer encodes, generates, and decodes. Simply letting the shared backbone decode does not help. What makes it work is to cast all three modes as position-aligned sequence maps over one fully shared backbone, distinguished only by a mode token and the timestep. The resulting model, UNIFIED, is simple: one network trained from scratch in a single stage with only reconstruction and flow-matching losses, without adversarial losses or pretrained encoders (e.g., DINO). On ImageNet-1K 256x256 at matched parameters, UNIFIED improves gFID over UNITE at three sizes (~60M, ~115M, and ~215M) and reaches 2.08 with 215M parameters, the lowest among compared models under 250M parameters. On text-to-image generation, UNIFIED-B (218M) reaches a GenEval score of 0.87 at 512x512, exceeding single-stage pixel diffusion models with around one billion parameters. Full unification of latent diffusion is thus not merely feasible but beneficial.

---


### 209. [HiPerfCC-StateReuse: Ciphertext Reuse for Fast Confidential GPU Data Movement](https://arxiv.org/abs/2611.29067)

**<font color=#1a73e8>作者：</font>** Haoxuan Xu, Shaoyu Wang, Minghao Lin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Confidential GPUs offer near-native on-device compute performance, but transfers between CPU and GPU TEEs through untrusted host memory require bulk CPU encryption and decryption, even for unchanged data. Existing software techniques overlap or parallelize these operations but retain their per-byte CPU cost. Reusing exported ciphertext could avoid this work, but GPU TEE firmware enforces direction-specific encryption keys and fresh per-transfer initialization vectors (IVs), preventing direct reuse.
We introduce ciphertext rebinding, a purely software primitive enabling repeated and cross-GPU ciphertext reuse on existing GPU TEEs without hardware changes, while preserving confidentiality, integrity, and freshness. Specifically, ciphertext rebinding exploits the separation between ciphertext-dependent and IV-dependent components in GPU TEE's AES-GCM authentication: a GPU-precomputed summary under the destination key can enable the CPU to update authentication tags without processing the payload. With this modification, GPU's subsequent read on the retained ciphertext can still proceed through the GPU's hardware-fixed copy-engine interfaces, which cannot be modified by software. An additional GPU correction step can then compensate for differences in the keys and IVs to recover the original plaintext. By retaining GPU-exported ciphertext in untrusted host memory, ciphertext rebinding avoids bulk CPU decryption and re-encryption, improving effective bandwidth for GPU-state restoration and sharing. We implement this primitive in HiPerfCC-StateReuse through only driver and library changes, combining batched submissions with pipelined GPU processing and copy-engine transfers. We evaluate transfer efficiency and CPU overhead through microbenchmarks, and application performance through three case studies: model switching, key-value cache offloading, and cross-instance cache sharing.

---


### 210. [Projecting Beauty: Transferring Image Aesthetic Analysis onto 3D Heritage and Urban Scenes](https://arxiv.org/abs/2611.29071)

**<font color=#1a73e8>作者：</font>** Sophia Kovalenko, Alexander M. Rusnak, Vittoria Meroni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Judgments about the beauty of buildings and streets inform architectural design, urban planning, and heritage conservation, yet increasingly rely on scanned 3D models over material fabric. Automatic aesthetic assessment remains largely confined to 2D photographs. We ask what survives when image aesthetic assessment crosses this dimensional gap to produce dense, per-point aesthetic descriptions of heritage and urban point clouds. We examine three routes that sidestep costly, and sometimes ethically dubious, human labeling at scale: (1) lifting scalar scores from image aesthetic models (NIMA, SAAN) onto geometry; (2) training Aesthetic Visual Analysis (AVA) regression heads on frozen vision backbones (DINOv3, TIPS, SigLIP2, PE, RADSeg) or, in a 3D-native variant, a generalist point encoder on feed-forward AVA reconstructions; and (3) querying lifted vision-language features with a natural-language aesthetic label, taking similarity as a score. The two supervised routes transfer poorly: heads fitting AVA in-domain produce architectural class profiles that neither reproduce one another nor track other signals, while the 3D-native probe stays near chance due to reconstruction geometry quality. Text querying is markedly more coherent. Projecting out the class-text direction from point features raises mean cross-model agreement on architectural part profiles from +0.035 to +0.352, and from +0.113 to +0.293 per point; the four backbones passing a semantic sanity check correlate at 0.31-0.73, while the failing one remains an outlier. Since model agreement is not agreement with human aesthetic perception, we detail a part-aware rating protocol to clarify where human and automatic ratings disagree. We provide a reproducible transfer protocol, an account of which pseudo-labeling routes carry signal, and dense aesthetic pseudo-labels meant as hypotheses rather than ground truth.

---


### 211. [Operational Runbooks as Living Documents: A Longitudinal Study of Document Evolution under Assisted Post-Incident Revision](https://arxiv.org/abs/2611.29097)

**<font color=#1a73e8>作者：</font>** Rocker D'Antonio, Harry Xie, Xuan Guo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Operational runbooks increasingly function as living documents within operational workflows: they are maintained by people, used in incident support, and continuously revised as organizational knowledge changes. Yet little is known about how such document collections evolve over time in production settings, or which interpretable signals are useful for monitoring document change. We analyze 17 weeks of version-controlled runbook snapshots produced during post-incident revision with machine-assisted review and human oversight. We quantify document evolution using lightweight linguistic and structural signals grounded in prior work on procedural language, technical communication, and document organization. Correlation analysis shows mixed patterns of association, including both positive and negative relationships, with effect sizes ranging from negligible to moderate and varying across corpora. Temporal summaries further distinguish comparatively stable signals from revision-sensitive ones, supporting monitoring of document maintenance workflows rather than one-shot quality judgments. An illustrative analysis on public GitHub product documentation shows that signal behavior differs across corpora, reinforcing the need for context-aware interpretation. These results identify which metric classes provide stable anchors and which provide edit-sensitive indicators for managing operational documentation as an engineered document resource.

---


### 212. [TesseraFlow: Scalable Video Diffusion for Dynamic Medical Imaging Inverse Problems](https://arxiv.org/abs/2611.29099)

**<font color=#1a73e8>作者：</font>** Atakan Topcu, Mohammadhossein Momeni, Alfredo De Goyeneche 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative priors are state-of-the-art for modeling medical images in image reconstruction tasks, but reconstruction with video priors takes tens of seconds to minutes per frame. Latent priors inherit the errors of their autoencoder, the memory of pixel-space whole-frame priors grows with the frame size, and pixel-space patch priors are slow for two reasons. First, their deep networks process every frame at full resolution at every sampling step, even though early steps resolve only low frequencies. Second, their samplers spend many network evaluations per sampling step on overlapping windows, multiple re-noising rounds, or backpropagation through the prior. We introduce TesseraFlow, a complex-valued pixel-space flow prior that reduces the first cost. A global encoder reads a low-resolution view of every frame once per sampling step. A single shallow decoder operates on this view during early steps and on full-resolution space-time tiles during later steps, so no network processes a whole frame at full resolution. Our sampler, ReTile, addresses the second reason. We use randomized grid shifting at every sampling step along with re-noising, which acts as a stochastic gradient instead of computing overlapping tiles, so a single network pass per sampling step suffices. On its own, ReTile speeds up an existing global-context patch prior by 6-9x, and our prior adds a further 3-5x speedup. TesseraFlow reconstructs about one 256x256 frame per second, 20-367x faster than patch and latent video priors, and can match or exceed the best generative baseline on cardiac, brain, and abdominal MRI and lung CT, at a fraction of its GPU time.

---


### 213. [GAG-Net: Graph-Based Anatomical Guidance Network for Pharyngeal Area Segmentation in VFSS Images](https://arxiv.org/abs/2611.29118)

**<font color=#1a73e8>作者：</font>** JunYeong Park, Myung Woo Park, Byung Chan Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diagnosing sarcopenic dysphagia typically requires costly supplementary imaging such as CT or MRI to assess muscle atrophy, burdening elderly patients. The pharyngeal area at rest (PA_rest), measurable directly from videofluoroscopic swallowing study (VFSS) images, is a promising biomarker that could eliminate this dependency, but repeated manual measurement has limited its adoption. PA_rest segmentation is further complicated by indistinct soft-tissue boundaries and clinical rule-based delineation criteria that data-driven models capture only imprecisely. We formulate automated PA_rest segmentation as a clinically defined measurement task, translating an implicit clinical measurement into an explicit landmark specification and annotation protocol developed with a rehabilitation medicine specialist. Applying this protocol, we constructed, to our knowledge, the first dataset for this task: 2,255 single-center VFSS frames from 137 patients, with PA_rest contours and seven landmarks verified by a senior specialist. We then introduce GAG-Net, an automated rest-frame measurement pipeline combining deformable convolutions, for irregular pharyngeal boundaries, with a graph-based anatomical guidance module that models the geometric dependencies among landmarks prescribed by the delineation rules. On a patient-level held-out test set (237 frames, 67 patients), GAG-Net achieved the lowest area measurement error (mean absolute percentage error: 8.17% against specialist-verified references; patient-level ICC 0.97) and the highest Dice score (0.8862) among all evaluated methods, with 67.2% fewer parameters and 74% less training memory than the two-stage JOINED model. Integrating clinician-defined anatomical knowledge may enable automated PA_rest measurement from VFSS images alone, supporting quantitative assessment of sarcopenic dysphagia without supplementary imaging.

---


### 214. [SilentWAM: Planning in the Masked State of a Diffusion World Model](https://arxiv.org/abs/2611.29125)

**<font color=#1a73e8>作者：</font>** Ziyu Zhao, Casey Sun, Zeyu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-action models learn from future prediction, but accessing their future representations directly at test time can require costly frame generation. Methods that generate future frames before planning incur additional forward passes, while future co-training methods omit explicit future predictions at inference. We introduce \method, a planner that reads the hidden states of masked future tokens without decoding future frames. We pretrain MMaDA-Parallel-M on driving video using frame-level masked world modeling, which predicts a masked suffix of future frames and explicitly includes inputs with all future frames masked. Learned planning queries attend to these masked positions and the observed context, and a continuous head predicts the trajectory in the same forward pass. With a single front camera, \method reaches 92.0 PDMS on NAVSIM v1 and 89.3 EPDMS on NAVSIM v2, with an end-to-end latency of 60.3\,ms.

---


### 215. [The Retry Tax: Why Static Same-Task Retries Can Cost More per Completion](https://arxiv.org/abs/2611.29133)

**<font color=#1a73e8>作者：</font>** Wei-Jung Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrying an agent after failure can complete more tasks while increasing the cost per completion. We study a static policy that stops at verified success or an attempt cap and otherwise resets the original prompt and workspace without passing feedback to the next request. Under stationary task success probabilities, independent attempts conditional on the task, and a common attempt cost, easier tasks tend to succeed earlier. When task success probabilities differ, the unresolved mix shifts toward harder tasks. Specializing classical survivor selection, we show that cost per completion is at least as high as in one-shot serving and that marginal cost per additional completion is nondecreasing wherever the completion increments are positive. These are different quantities: one averages spending over all completions, while the other prices the completions added by another attempt. We then arrange each task's existing benchmark runs in different orders, stop each sequence at verified success or the attempt cap, and average the resulting completion and spending at each supported cap. For one OpenHands configuration, replay estimates completion of 59.7 percent with one attempt and 70.0 percent with four, while cost per completion rises from about USD 0.70 to USD 1.32. The recorded trade-off describes fixed configurations on the available tasks. Choosing a cap requires comparing the additional spending with the application's value for the additional completions.

---


### 216. [Supply the Global, Supervise the Local: Combining Representation Conditioning and Alignment in Diffusion Transformers](https://arxiv.org/abs/2611.29138)

**<font color=#1a73e8>作者：</font>** Chaojie Ji, Sergio Quiroga-Sandoval, Ruxin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A pretrained image representation helps train a diffusion transformer in several roles, including as an alignment target, which the model's hidden states learn to match, as in representation alignment (REPA), and as a condition, an extra input describing the image to be generated. Combined, they would give the model an input and a target, but whether they conflict is unknown. To test this, we let the condition carry only part of REPA's target: we split the representation of each image patch into an image-level (global) part, shared by all patches of the image, and a within-image (local) part, the patch's difference from the image-level part, and use one token carrying the image-level part as the condition. Then, the two roles overlap on the image-level part, where they could conflict, while only REPA supervises the within-image part, where we can see whether the token helps REPA.
We find that the token and REPA together teach both the image-level part and the within-image part, the main source of REPA's FID improvement, far more than the sum of what each teaches alone, so they cooperate rather than conflict. These findings give one design rule for combining REPA with an image-level condition, supply the global, supervise the local, which we implement as Global-Condition REPA (GC-REPA): REPA with the token as an extra input; the token carries no information beyond REPA's target and is drawn at sampling from a separately trained token prior. GC-REPA greatly accelerates convergence: on ImageNet 256*256, SiT-XL/2 + GC-REPA reaches REPA's 4M- and SiT-XL/2's 7M-iteration FIDs within 200K and 100K iterations (20 and 70 fewer).

---


### 217. [Towards Edge Artificial Intelligence for Predicting Antimicrobial Resistance in Mycobacterium tuberculosis](https://arxiv.org/abs/2611.29143)

**<font color=#1a73e8>作者：</font>** Nishat Tasnim, Faisal Ahmed, Rokan Uddin Faruqui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Antimicrobial resistance (AMR) in Mycobacterium tuberculosis (MTB) poses a major challenge to global tuberculosis control, as multidrug-resistant strains limit available treatment options. Rapid and accurate prediction of drug resistance from genomic data could support timely treatment decisions and public health interventions. However, many existing computational approaches for genomic AMR prediction rely on computationally intensive pipelines, limiting their suitability for deployment on resource-constrained edge devices. This limitation is particularly relevant in hospital settings in low- and middle-income countries, where computing infrastructure and access to high-performance computational resources may be limited. To address this challenge, we present a lightweight, novel machine learning (ML) approach suitable for running on edge devices that combines 4-mer frequency features derived from whole-genome sequences with a Random Forest classifier to predict antibiotic resistance in MTB. The proposed ML approach achieved an average area under the receiver operating characteristic curve of 0.82 across 20 antibiotics on an independent test set.

---


### 218. [ArborNet: Volume- and skeleton-aware completion of tree quantitative structure models from incomplete point clouds using anchor-conditioned graph learning](https://arxiv.org/abs/2611.29148)

**<font color=#1a73e8>作者：</font>** Ge Jiang, Tiangang Yin, Wei Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Terrestrial laser scanning (TLS) enables 3D reconstruction of trees and quantitative structure models (QSMs) for estimating woody volume and structural traits. However, occlusion in single-station or sparsely sampled TLS causes incomplete branch observations and biased volume estimates. Existing point-cloud completion methods recover plausible geometry but do not explicitly preserve branch topology, cylinder radii, or woody volume. We propose ArborNet, a volume- and skeleton-aware framework for completing tree structures in the QSM domain. Each tree is represented as a TreeQSM cylinder graph encoding cylinder geometry, branch level, parent-child topology, and branch identity. A multi-relation graph encoder propagates information across parent, child, and intra-branch connections. An anchor-conditioned decoder generates missing cylinders through terminal-branch continuation and new-branch generation. Geometry, existence, branch, radius, axis-smoothness, and volume losses encourage structural consistency. During inference, generated cylinders are selected under predicted level-wise missing-volume budgets. We evaluate ArborNet on DART-simulated TLS trees and urban TLS trees from Hong Kong, using single-station QSMs as partial inputs and multi-station QSMs as references. Under budget-constrained inference, ArborNet achieves mean total-volume relative error of 0.081% and mean level-wise volume error of 0.676% against reference QSMs, while reducing skeleton geometry error relative to evaluated point-cloud completion baselines. These errors quantify agreement with reference QSMs, not accuracy against destructively measured woody volume. Ablation results show that joint volume supervision is particularly important for volume control. These results demonstrate the potential of QSM-domain completion to recover explicit woody structure while constraining geometry and volume.

---


### 219. [Inclusive Hand Pose Estimation via Topology-Aware Distillation and Progressive Kinematic Reasoning](https://arxiv.org/abs/2611.29163)

**<font color=#1a73e8>作者：</font>** Kanglei Zhou, Zikai Hao, Liyuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hand pose estimation aims to recover the spatial configuration of hand joints from visual observations and serves as a fundamental perception module for downstream systems that rely on complete and topologically consistent hand representations. Most existing methods are developed under the assumption of fully articulated hand structures and tend to produce unstable or implausible predictions when parts of the kinematic structure are persistently absent, resulting in degraded performance or even system failure despite available partial observations. To study this challenge, we construct IncNYU, a physiologically constrained benchmark that simulates structural incompleteness through morphological modification of complete hand models and retains reference locations for both intact and synthetically removed regions. Based on this benchmark, we propose InsHaPE, an Inclusive Hand Pose Estimation framework designed to remain robust under structural incompleteness while preserving performance on standard, fully articulated hands. Built on hierarchical kinematic modeling, InsHaPE introduces two complementary components. First, a topology-aware distillation strategy transfers joint-level and relational priors from fully articulated hand representations, providing anatomically consistent initialization under missing structures. Second, a progressive kinematic reasoning module performs structured inference along the kinematic chain, enabling complete and anatomically consistent pose estimation under severe structural variations. Extensive experiments on NYU/IncNYU, together with external validation on MSRA, demonstrate that InsHaPE improves robustness under structural incompleteness while maintaining competitive performance on complete hands. System-level evaluations further show that InsHaPE improves robustness for downstream applications that require fixed-topology hand pose representations.

---


### 220. [Training-Free 3D Editing via Feature-Divergence Localization and Trajectory Correction](https://arxiv.org/abs/2611.29165)

**<font color=#1a73e8>作者：</font>** Tri Ton, Siwoo Lim, Joshua Tian Jin Tee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modifying 3D assets requires enacting targeted structural transformations while strictly preserving the geometric identity of unedited regions. While recent probability flow models enable training-free editing, bounding these modifications within a high-dimensional latent space presents severe mathematical challenges. Current inversion-free trajectories rely on global velocity updates, which often cause spatial bleed into preserved structures and induce trajectory under-commitment, causing edits to stall mid-path. To resolve these dual failures, we introduce FocusFlow, a segmentation-free framework that structures the integration trajectory into two disjoint phases. During early coarse structure formation, FocusFlow applies Feature-Divergence Localization (FDL) to spatially gate the velocity field using intrinsic cross-attention. Once coarse structure has formed, FocusFlow applies Reference Generation Guidance (RGG), a trajectory-correction term that drives convergence to the target shape by pulling the trajectory toward an explicit clean-latent target. Evaluated on the joint Google Scanned Objects and PartObjaverse-Tiny benchmarks, FocusFlow obtains the best preservation scores and the largest edit magnitude among compared methods, suggesting that it can reduce the traditional preservation-modification trade-off. By providing stable, localized geometric control without manual spatial annotations, this phase-scheduled approach lowers technical barriers to the modification of synthetic 3D media.

---


### 221. [What Makes Recurrence Generalize Across Lengths?](https://arxiv.org/abs/2611.29171)

**<font color=#1a73e8>作者：</font>** Yoonsung Jung, Sunghun Jung, Louise Nayeong Koh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-step reasoning requires models to preserve and update intermediate information as computation unfolds. State tracking captures this fundamental requirement, but models that succeed within a fixed range of state transitions may not generalize when substantially more updates are required. Recurrent Transformers offer a natural mechanism for addressing this challenge by repeatedly applying shared Transformer blocks, allowing computation to scale with problem length. We study when such recurrent computation generalizes beyond the training range in a controlled state-tracking task, varying operation representation, positional encoding, and recurrent capacity. We find that recurrence alone is insufficient: multi-token template representations and absolute positional encoding can severely limit extrapolation, whereas atomic operation representations enable substantially stronger length generalization. The effect of positional structure also varies with recurrent depth, with periodic positional encoding achieving the strongest mean performance at greater recurrent depth. Most importantly, scaling the recurrent operator extends the extrapolation horizon, reaching 35.1% exact-match accuracy on sequences of 20-40 operations after training only on 2-10, while substantially larger fixed-depth Transformers remain at 0%. Additional recurrent computation at test time can extend the range over which the model generalizes, but does not eliminate failure on much longer sequences. These results suggest that recurrent computation can support length-generalizable state tracking, but that its effectiveness depends critically on whether the learned computation remains reusable across sequence lengths.

---


### 222. [On Adaptive Step Sizes for Eligibility Traces in Deep Reinforcement Learning](https://arxiv.org/abs/2611.29178)

**<font color=#1a73e8>作者：</font>** Esraa Elelimy, Martha White  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many deep reinforcement learning (RL) algorithms store agent-environment interactions in a replay buffer and later learn by sampling transitions from it. However, this approach can be memory-inefficient and can delay learning because the agent can learn from a transition only when the buffer samples it. Additionally, most of these methods use one-step or short multi-step temporal-difference (TD) updates, which are slow at credit assignment. An alternative approach is to learn from the stream of observations as they arrive without relying on a buffer. Eligibility-trace algorithms allow these incremental updates and can also assign credit over many steps. These algorithms were common with linear function approximation but have only recently been used in deep RL. Basic questions, such as how to use vector step sizes with eligibility traces in the deep RL setting, remain open. In this work, we first show that adaptive vector step sizes must be part of the eligibility trace to keep the equivalence between the forward and backward views. We then show that the step sizes of common optimizers, such as Adam, do not have an online backward view. We introduce a new optimizer, Function-Space Distance (FSD), that maintains the forward-backward equivalence. We test four eligibility-trace algorithms covering semi-gradient and gradient TD updates, as well as value-based and actor-critic methods. We show that FSD performs better than SGD or naively applied Adam. The resulting algorithms outperform or match other streaming methods and are comparable to or better than PPO, which uses a buffer, in most environments. Code available at this https URL

---


### 223. [loopxDINO: Dense Visual Prediction via Iterative Latent Reasoning](https://arxiv.org/abs/2611.29180)

**<font color=#1a73e8>作者：</font>** Xiangjing An, Zhibin Jiao, Aiting Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard dense visual prediction architectures scale representation capacity by stacking deep feedforward decoders (6-16 transformer layers with 50M-200M parameters). This explicit layer stacking brings substantial activation memory overhead during backpropagation, requires high off-chip memory bandwidth for non-tied weights, and uses static computational allocation that cannot adapt to spatial image complexity.
We propose loopxDINO, which replaces physical decoder depth with iterative latent reasoning. It has two decoupled components: (1) a frozen DINOv2-Base backbone extracting spatial features in one forward pass and caching static Key-Value representations in GPU memory; (2) a compact weight-tied Looped Cross-Attention Decoder (7.96M core, 14.85M total trainable parameters) that recurrently updates queries across T iterations. Recurrence is stabilized by step-conditioned adaLN, LayerNorm-based hyper-ellipsoid manifold regularization, and learnable residual contraction damping. Intermediate mask predictions are fed back as spatial attention biases to guide queries toward ambiguous contours with no extra parameters.
On Pascal VOC 2012 semantic segmentation with a single RTX 5060 Ti 16GB GPU, loopxDINO (T=2) achieves 85.66% mIoU and 65.01% Boundary IoU. It outperforms 6-layer DINO-Trans6L (54.06M params) by +1.09% mIoU and +7.41% Boundary IoU with 72.5% fewer parameters. Compared to 4-layer DINO-FCN4L probe (2.43M params, 83.82% mIoU), loopxDINO improves boundary delineation by +6.43% bIoU and occlusion resilience by +6.76% mIoU (60% patch masking). With Adaptive Computation Time (ACT), it reaches 87.3 FPS and retains 29.64% mIoU under 60% occlusion (+5.83% over DINO-Trans6L).
Source code, pre-trained weights and evaluation suites are open-sourced under Apache 2.0 at this https URL

---


### 224. [PartPO: Part-Level Policy Optimization for Shape-to-Program Generation](https://arxiv.org/abs/2611.29213)

**<font color=#1a73e8>作者：</font>** Hannuo Zhang, Zhixiang Chi, Xuanchen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PartPO, a reinforcement learning method for generating structured shape programs from 3D point clouds. Existing shape-to-program models are trained with supervised learning on procedurally generated data and generalize poorly to more diverse shapes, while reinforcement learning from execution feedback assigns a single scalar reward to a long program that builds many parts, making credit assignment difficult. PartPO instead builds on a core property of the task: shape programs are self-describing, with each semantically named part produced by its own code block. It segments each generated program by its parts and applies part-level rewards only to the code of the corresponding part, a category reward only to the object name, and a shape-level reward to the whole program. The required part supervision is obtained without manual annotation, by grounding part names on target meshes with an open-vocabulary segmentation model prompt-tuned on the model's own outputs. Applied to MeshCoder, PartPO improves reconstruction accuracy and execution success on ShapeNetCore and ABO over the base model, rejection-sampling fine-tuning and trajectory-level RL, and generalizes to the unseen HSSD dataset. Code will be released at this https URL.

---


### 225. [NANO: Unifying Missingness and Input Uncertainty in Tabular Learning](https://arxiv.org/abs/2611.29214)

**<font color=#1a73e8>作者：</font>** Kuangdai Leng, Maria Tsekhmistrenko, Matteo Bagagli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Missing values are common in tabular data, yet current approaches to handling them often overlook two dimensions. First, an observed value may be uncertain, while a Not-Observed (N.O.) value may still have a reasonable estimate. Inputs should therefore span a continuous spectrum from no evidence to a fully trusted observation. Second, Not-Applicable (N.A.) means that no meaningful value exists for a record, yet this semantic state often lacks explicit representation. To address both dimensions, we introduce NANO, a unified plug-in for input encoding that fits most token-based architectures. Guided by Bayesian evidence weighting, NANO adjusts the influence of a supplied value according to confidence, with all zero-confidence estimates mapped to the same N.O. representation. NANO accepts, but does not require, per-example confidence information during training or inference. For N.A., a separate representation enables models to encode inapplicability and its schema-defined reasons into context. Experiments across eleven datasets and nine backbones show that mixed-confidence training enables a single NANO model to generalize across inference confidence levels, remaining competitive without estimates and improving steadily as estimate reliability and confidence increase. The effectiveness of NANO's handling of N.A. is further demonstrated on three augmented datasets.

---


### 226. [Ego-HMB: Human Motion Bridging from Egocentric Images via A Motion Bridge Diffusion Model](https://arxiv.org/abs/2611.29218)

**<font color=#1a73e8>作者：</font>** Gaoge Han, Yongkang Cheng, Shaoli Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Egocentric Human Motion Bridging, a task that generates a coherent 3D human motion sequence from two endpoint egocentric images. Unlike conventional motion in-betweening, which requires structured 3D endpoint poses, this setting uses raw first-person observations available from wearable devices in VR/AR and robotics. It presents challenges due to viewpoint variations, partial body visibility, and temporal ambiguity under cross-modal endpoint constraints. To address these challenges, we propose Ego-HMB, a unified diffusion-based framework that learns endpoint pose estimation and temporally consistent motion infilling within a single model through two training stages. First, Egocentric-to-Canonical Pretraining uses a hierarchical curriculum with progressively increasing temporal spans to strengthen endpoint pose priors. Second, Motion Bridge Diffusion Training incorporates endpoint and physics awareness, diffusing from neighboring poses to promote temporal continuity while preserving global endpoint constraints. Extensive experiments compare our approach with one-stage methods that directly generate motion from two egocentric images and two-stage pipelines that combine endpoint pose estimation with motion interpolation. Ego-HMB consistently outperforms these baselines in endpoint accuracy and motion generation quality. Code is available at this https URL.

---


### 227. [Curvature Mismatch and Local Errors in Galaxy Property Estimation](https://arxiv.org/abs/2611.29224)

**<font color=#1a73e8>作者：</font>** Austin Lutterbach, Angus Hoy, Jasper Chong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear probes are widely used to evaluate learned representations and infer physical quantities from unlabelled data. The probe's predictions are from an affine function in ambient space restricted to the underlying representation, and consequently, even a representation that has complete information needed to predict a target can produce systematic probe errors when that information is encoded in a form inaccessible to the linear probe. Here we share that some of this probing error is due to the innate geometry of the manifold. Linear probes, when evaluated on a curved manifold, generally have a nonzero intrinsic Hessian (what we colloquially call "probe-facing curvature") given by $\langle w_N,\mathrm{II}\rangle$, the manifold's second fundamental form dotted with the probe's normal component. We fit linear probes to galaxy embeddings from five pretrained encoders and intervene on this curvature term to evaluate its contribution to the probe performance. We find that keeping this inherited curvature improves the local fit where it matches the label's curvature. Removing the curvature component of the probe where it does not match the label curvature also provides improvements, and correcting it in every neighbourhood raises held-out local $R^2$ by 0.006 to 0.010 on galaxies, gaining more where the two curvatures disagree. We isolated these gains to be from the underlying geometry and not an automatic guarantee from least squares training.

---


### 228. [Why Adaptive Optimizers Struggle with Large Convolution Kernels](https://arxiv.org/abs/2611.29232)

**<font color=#1a73e8>作者：</font>** Tianyu Ding, Jiachen Jiang, Jinxin Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large convolution kernels enlarge the receptive fields of ConvNets at a modest computational cost, but they are notoriously difficult to train. Existing large-kernel networks therefore rely on costly training techniques, such as parallel small-kernel branches with batch normalization. In this paper, we trace this difficulty to adaptive optimizers such as Adam, which normalize the update of every weight separately. Since input features rarely average to zero, all weights of a kernel share a common gradient, and these optimizers move the mean of a $k\times k$ kernel $k$ times as far as a single parameter. We find this mean amplification in widely used ConvNets and vision transformers, and show that it can force the maximal learning rate to fall as $1/k^2$. We further prove that the basis of the discrete cosine transform (DCT) isolates the mean and is the only orthonormal basis that diagonalizes every stationary gradient statistic with mirrored boundaries. We therefore train large kernels through their DCT coefficients and convert them back after training. The resulting method, DCT-Rep, requires only a few lines of code and adds no parameters, no inference cost and negligible training overhead. Extensive experiments on image classification, object detection, semantic segmentation and image restoration show that DCT-Rep consistently improves large-kernel ConvNets and vision transformers, by $+0.79\%$ top-1 accuracy for a large-kernel ConvNeXt-T and $+0.43\%$ for ViT-S/16 on ImageNet-1K, $+1.4$ box AP on COCO, $+1.2$ mIoU on ADE20K and up to $+0.4$ dB on image deblurring, where the gain grows with the kernel size.

---


### 229. [Complementary Geometry in Gaussian Splatting](https://arxiv.org/abs/2611.29236)

**<font color=#1a73e8>作者：</font>** Mingle Jiang, Jikui Zhou, Chenghan Lyu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian Splatting has achieved high visual quality in novel view synthesis, but the accuracy of its rendered geometry remains a challenge. In particular, the rendered depth is computed as an opacity-weighted average along each ray, which may not correspond to the actual scene surface. In this paper, we observe that depth predictions from different views of the same frozen Gaussian representation exhibit complementary errors, allowing us to improve novel-view geometry using information from other views without modifying the original representation. Based on this observation, we propose REVEAL, a general framework that selectively refines novel-view depth using complementary geometric information. Specifically, we first reproject depth predictions from source views to the target view and combine them using robust multi-view consensus. We then introduce a learned selection mechanism to determine whether the candidate depth is more accurate than the original prediction, based on the expected reduction in depth error. In addition, we introduce RIG, a real-world benchmark captured with synchronized RGB-D cameras, which provides ground-truth depth for evaluating both static and dynamic reconstruction models. Experiments on 6 Gaussian Splatting backbones across 3 benchmarks show that REVEAL consistently improves depth accuracy while maintaining comparable rendering quality.

---


### 230. [Fuzzy e-Means: Fuzzy c-Means on Large Data with Moving-Average Mini-Batch Updates](https://arxiv.org/abs/2611.29241)

**<font color=#1a73e8>作者：</font>** Paritosh Tiwari, Punit Rathore  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fuzzy c-means (FCM) gives every point a degree of membership in every cluster. Its standard solver, alternating optimization (AO), needs a full pass over the data per iteration and often many iterations, while methods built for large data stop at a worse objective or still need tens of passes. We run FCM with the optimizer of e-means, a recent mini-batch k-means that keeps moving averages of the number and the sum of the points in each cluster and sets its batch size and step size by scaling laws. The optimizer carries over because an FCM centroid is also a weighted sum divided by a total weight, but this direct transfer fails in two ways: the e-means rule that relocates nearly empty clusters also removes the centroids of small, distant groups, and FCM started from random points can settle in poor local minima. Fuzzy e-means (e-FCM) therefore starts with one pass of e-means with hard assignments and then runs fuzzy moving-average passes without relocation. On 28 configurations with up to 109.5 million points and 16,384 clusters, e-FCM reaches the objective of 25 AO iterations in two to four passes when clusters hold several hundred points or more, 11 to 20 times faster than AO on one-million-point embedding sets with 1,024 clusters. It ends within 0.16% of converged AO on these sets and below converged AO where AO from random points lands in poor minima, but it is slower than AO on small low-dimensional problems, where an AO pass takes milliseconds. Finally, the common fuzzifier m=2 makes the centroids collapse or merge on most high-dimensional sets, and e-FCM can choose the fuzzifier by matching a known overlap at about two passes per candidate value.

---


### 231. [Tissot indicatrix for location encoders: Characterizing local distortion in learned geographic embeddings](https://arxiv.org/abs/2611.29249)

**<font color=#1a73e8>作者：</font>** Guofeng Cao, Gengchen Mai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the increasing adoption of geographic artificial intelligence, location encoders are widely used to map geographic coordinates to learned embeddings for tasks in Earth observation and geospatial modeling. Similar to map projections, location encoders can distort geographic space, that is, equal-distance displacements in different directions can result in unequal embedding changes. However, such distortion remains largely unexamined, and it can propagate into downstream applications. We adapt Tissot's indicatrix, a cartographic tool for map projection distortion, to characterize this distortion. At each location, we compare encoder outputs at equal distances in 32 directions and fit a tensor, represented by an ellipse, whose elongation (anisotropy) and orientation describe the local distortion. The fit requires only encoder outputs without access to model internals and is validated against references with known geometry. By applying the method to thirteen released checkpoints of five encoder families, we find that distortions vary across space and inherit the input geometry to varying degrees, closely in GeoCLIP with its Equal Earth input (anisotropy correlation of 0.88) and weakly or moderately in the other encoders. The distortion also affects the locations an encoder treats as neighbors. Within 1km of 20 query sites, the 40 nearest neighbors in geographic and embedding space overlap by a median of only 57.5--87.5% across the checkpoints, while the fitted ellipses select exactly the same embedding neighbors in 265 of 299 comparisons. These findings provide a geographic basis for assessing location encoders, and the accompanying eTissot package implements the methods for user-specified encoders.

---


### 232. [OAT3D: A Generative Model for 3D Shape- and Resolution-Free Structural Topology Optimization](https://arxiv.org/abs/2611.29253)

**<font color=#1a73e8>作者：</font>** Hongrui Chen, Kittipong Thiamchaiboonthawee, Zhen Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Topology optimization determines how material should be distributed within a design domain to optimize structural performance under prescribed loads, supports, and constraints. The problems are highly nonconvex, and conventional solvers require repeated finite element analyses, making high-resolution 3D topology optimization computationally expensive. Data-driven approaches face an additional bottleneck: generating training datasets requires solving large numbers of these costly problems, so existing work in data-driven topology optimization primarily focuses on 2D problems. Large-scale 3D datasets remain scarce, and existing models remain limited in problem scale and boundary-condition diversity. Here, we introduce Optimize Any Topology-3D (OAT3D), a generative model for high-resolution 3D structural topology optimization. OAT3D introduces a novel sparse problem encoding to represent load and fixity conditions and combines a sparse volumetric variational autoencoder with a conditional diffusion transformer. We construct a dataset of 501,865 optimized topologies, generated using 51,800 GPU-hours and encompassing structures with up to one million elements and substantially more complex loading and support configurations than any existing structural topology optimization dataset. To our knowledge, this is the largest dataset for 3D topology optimization structures. Trained on this dataset, OAT3D generates structures at 512$^3$ resolution and achieves a $44.9\times$ speedup for raw candidate structure generation or $3.65\times$ speedup to reach similar compliance over conventional topology optimization. These contributions expand the scale and diversity of data-driven topology optimization for three-dimensional structural design.

---


### 233. [Denoised but Not Improved: What EEG Denoising Does to a Downstream Task](https://arxiv.org/abs/2611.29256)

**<font color=#1a73e8>作者：</font>** Xianglong Bao, Zhe Wang, Kewen Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scalp electroencephalography (EEG) is routinely denoised before it reaches a downstream model, and the denoising literature scores a method by how closely its output matches a clean reference waveform. That reference does not exist for real scalp recordings: it is synthesized by adding artifact templates to signals merely presumed clean, and even an exact separation would return cortical activity blurred by volume conduction rather than the activity itself. Fidelity to it is therefore an unvalidatable objective, and whether it predicts any downstream benefit has gone largely unexamined. We report an audit that examines it. Holding a seizure-detection pipeline fixed and varying only the preprocessing stage, we find that five standard denoising methods, spanning analytic, cross-channel and supervised deep families, all fail to improve on the unprocessed signal, and most degrade it. To say what such a stage must instead do, we formalize a label-only, classifier-free probe that reads it by the separability geometry it induces on task-relevant features, decomposing any change into a between-class distance and a within-class scatter term. On a transform that does improve the task, the probe attributes the entire gain to a roughly one-quarter reduction of within-class scatter, with class separation statistically unchanged. What a downstream model benefits from is therefore variance suppression on task-relevant structure, which waveform-fidelity metrics neither measure nor reward.

---


### 234. [CFANet: Learning Conflict-Free Weather Adapters for All-Weather Image Restoration](https://arxiv.org/abs/2611.29257)

**<font color=#1a73e8>作者：</font>** Minglong Xue, Wenchao Yan, Guoan Guan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> All-weather image restoration aims to recover clean images from diverse weather degradations such as rain, haze, and snow. Most existing all-in-one methods handle different weather types with a unified network or rely on single-label weather modeling. However, real-world adverse weather is often compositional, where multiple known weather primitives may coexist in a single image. To this end, we propose Conflict-Free Adapter Network (CFANet) for open-compositional all-weather image restoration. CFANet first employs a Weather Mixture Router (WMR) to predict non-exclusive composition weights for rain, haze, and snow from shallow features. Guided by these weights, a Shared-Private Weather Adapter (SPWA) dynamically composes a common adapter with weather-private adapters inside each Conflict-Free Adapter Block, preserving shared restoration capability while providing weather-specific residual adaptation. Moreover, a lightweight Natural Color Adapter (NCA) performs constrained color calibration to improve color fidelity and visual naturalness. Extensive experiments demonstrate that the proposed method achieves competitive adverse weather image restoration performance and benefits downstream visual tasks. Our code is available at this https URL

---


### 235. [Look Back: Reinforcement Learning with Counterfactual World Models](https://arxiv.org/abs/2611.29259)

**<font color=#1a73e8>作者：</font>** Jinwoo Kim, Toghrul Abbasov, Lucius E.J. Bynum 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agents in complex, stochastic environments must contend with dynamics that can exceed their world models' predictive capacity and randomness that obscure the consequences of their actions. We hypothesize that, compared to imagining entirely new trajectories in such complex environments, it can be easier to transform observed trajectories with alternative actions. Counterfactual world models condition on observations to predict alternative outcomes under the same underlying environmental randomness, using experience as a reference for predicting action-dependent changes. We present a policy gradient estimator, REINFORCE Look Back (RLB), that uses counterfactual returns as baselines to distinguish action effects from environmental luck, and prove conditions for unbiasedness and variance reduction. In settings where environmental evolution is harder to predict than action-induced changes, we show that counterfactual world models are easier to learn and support better policy learning than ordinary world models. Our findings suggest that counterfactual thinking can help agents learn effective behavior without independently reproducing the full complexity of their worlds.

---


### 236. [Revealing Semantic Gaps in Zero-Knowledge Virtual Machines via Obligation-Targeted Semantic Fuzzing](https://arxiv.org/abs/2611.29260)

**<font color=#1a73e8>作者：</font>** Hongbo Wen, Jingyu Ke, Hanzhi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zero-knowledge virtual machines (zkVMs) prove correct execution of programs and underpin systems securing billions of dollars in digital assets. Their security depends on alignment between the instruction set architecture (ISA) that programs target, such as RISC-V, and the constraint system, polynomial equations that check the prover's record of every intermediate value (the witness). Mismatches, or semantic gaps, come in two kinds: underconstraint bugs let a malicious prover forge a proof of an execution the ISA forbids (a soundness violation), and divergence bugs make the zkVM itself deviate from the ISA or crash, so an honest prover cannot prove a legitimate execution (a completeness violation). Both cluster at corner cases such as division by zero that conventional fuzzing almost never reaches, and underconstraint bugs leave program output unchanged. Our key insight is that these corner cases correspond to constraint obligations derived from the ISA specification and the proof system's algebraic structure. We build Beak, a reinforcement-learning fuzzer in which obligations replace three random decisions: they supply inputs that trigger each obligation, reward executions that trigger new combinations of obligations, and direct witness tampering to the step where an obligation is triggered. Beak flags divergence bugs by comparing registers against a reference RISC-V emulator, and underconstraint bugs by checking whether the constraints accept a tampered witness. On six leading production RISC-V zkVMs, Beak detects 25 of 37 known bugs (67.6%) versus 5 (13.5%) for the prior state of the art, and discovers 14 previously unknown bugs, all responsibly disclosed and patched.

---


### 237. [Dually Constrained Parameter Projection for Continual Learning](https://arxiv.org/abs/2611.29269)

**<font color=#1a73e8>作者：</font>** Bowyn Tan, Zhilong Zheng, Yang Guan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning requires a model to learn multiple new tasks sequentially while retaining performance on previous tasks. Projecting model parameters onto the Jacobian null space of previous tasks after unconstrained training on a new task has emerged as an effective paradigm. However, unidirectional projection merely minimizes the parameter distance to the new-task optimum, overlooking the new-task loss landscape. To address this limitation, we propose DUET, a bidirectional projection algorithm that imposes Jacobian null-space constraints from both previous and new tasks during post-training projection. Specifically, DUET formulates the post-training adjustment as a dually constrained optimization problem. It minimizes the distance between parameters before and after training on a new task, subject to loss preserving constraints on both tasks. To solve the optimization problem, we develop an alternating bidirectional projection algorithm, whose convergence is guaranteed by the contraction mapping theorem. For reliable multi-step projection, we rectify existing step size selection criteria via an effective-rank aware formulation, overcoming their failure under rank-deficient Jacobians. Extensive experiments demonstrate that DUET consistently outperforms existing unidirectional projection methods and achieves state-of-the-art performance on multiple datasets.

---


### 238. [DriveOddsBench: Are Driving Video World Models Aligned with Real-World Odds?](https://arxiv.org/abs/2611.29275)

**<font color=#1a73e8>作者：</font>** Jiaxi Liu, Keshu Wu, Bin Ran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models predict how a scene will evolve, and their sampled futures are increasingly used in place of the real one, from planning to simulation. These uses assume that the samples are aligned with real-world odds, with each future appearing among them as often as it would follow the same history in reality, yet current evaluations only score how real each sample looks. Testing this assumption on real driving data is hard for three reasons. Each recorded history has only one real future, so the true probabilities are unknown. Physical quantities must be read from video, where reading errors can look like model errors. Finally, the many possible analyses invite selective reporting. We introduce DriveOddsBench, a pre-registered benchmark that addresses all three. First, if the samples follow the real distribution, the rank of the real outcome among them is uniform in every history, so pooled ranks test them without probability labels. Second, one validated instrument reads the same quantities, such as the lead-vehicle gap and the ego motion, from the generated futures and from the real future, which first passes through the world model's autoencoder so that both are read alike. Third, all confirmatory analyses were frozen before any test clip was measured. We test eleven general and driving world models on 200 held-out Argoverse 2 histories in five scenario families, with 35,200 generated futures. None is aligned, and every model underestimates its uncertainty. The real outcome falls outside the range of all 16 samples in 28-61% of cases instead of the 11.8% expected under the real distribution. Five models are significantly skewed, in opposite directions, and the largest errors are in the ego motion. Nine models beat climatology without being aligned, and among these models neither type nor scale predicts which comes closest.

---


### 239. [ContinuLoc: Continuous Pose Inference over Neural Fields for UAV Geo-Localization](https://arxiv.org/abs/2611.29276)

**<font color=#1a73e8>作者：</font>** Weikun Zhou, Jinliang Lin, Yu Zang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view UAV geo-localization involves three design choices: how to represent the UAV observation, how to represent the geo-referenced map, and how to infer pose from their interaction. The dominant paradigm organizes the map as a discretized 2DoF candidate library, coupling map representation to pose inference and thus bounding spatial localization precision by candidate sampling resolution. We decouple map representation from pose inference by encoding the geo-referenced map as a continuously queryable semantic neural field, enabling localization to be formulated as explicit optimization over a continuous 4DoF pose space parameterized by 2D ground position, in-plane heading, and viewing scale. Pose hypotheses are evaluated on demand using global descriptors in a shared semantic feature space, bypassing the sampling bottleneck of retrieval. We learn 4DoF pose-sensitive visual representations under full 4DoF supervision provided by ContinuScenes, a multi-city benchmark with dense near-nadir UAV imagery and complete pose annotations. Inference proceeds hierarchically, progressing from broad pose-space coverage to adaptive concentration on high-compatibility regions. Experiments demonstrate substantial gains over representative localization paradigms under progressively stricter 4DoF accuracy criteria.
Code is available at this https URL

---


### 240. [One-shot is Enough: Boosting SAM for Medical Image Segmentation through Structured Information Modeling](https://arxiv.org/abs/2611.29278)

**<font color=#1a73e8>作者：</font>** Guilin Guan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, Foundation models such as the Segment Anything Model (SAM) have demonstrated strong generalization capabilities, but because they are primarily pre-trained on natural images, they perform poorly when faced with medical images. With sufficient labeled medical data, this challenge is somewhat alleviated. However, the difficulty and high cost of acquiring large amounts of labeled data make one-shot learning a highly attractive research paradigm. But within this paradigm, SAM struggles to fully extract its potential multi-granular information, leading to a sharp decline in performance. To address this, we propose OB-SAM, a one-shot enhancement framework for medical image segmentation. It aims to maximize the utilization of information from a single sample from the perspective of structured modeling. Specifically, we first designed a Multi-Frequency Decoupling (MFD) module, which divides features into different frequency domain components, allowing each branch to focus on information expression at different semantic levels, thereby alleviating overfitting and enhancing feature representation capabilities. Secondly, we introduce a Progressive Feature Integrator (PFI) module to promote complementary fusion among multi-level features, thereby avoiding the dominant effect of a certain level of feature in the fusion process. Furthermore, we propose an Selective Context Filtering (SCF) Module that adaptively selects key contextual information by modeling the contrast relationship between the foreground and background, thereby achieving precise localization of the lesion area. Extensive experiments across seven diverse datasets validate that OB-SAM achieves state-of-the-art performance.

---


### 241. [RadioWorld: Transferring World Models to Radio-Frequency Radiance Fields](https://arxiv.org/abs/2611.29282)

**<font color=#1a73e8>作者：</font>** Hu Zhou, Jiazhou Zhou, Shuowen Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Electromagnetic (EM) wave propagation in the physical world constitutes a Radio-Frequency (RF) radiance field, providing rich information for 6G communication and sensing. However, existing neural RF field methods suffer from three fundamental limitations: (1) they predominantly rely on per-scene optimization and cannot generalize to unseen scenes; (2) they require costly reference RF measurements in each target scene; and (3) they degrade severely when extrapolating beyond the vicinity of reference measurements. To overcome these limitations, we present RadioWorld, a general framework that adapts a world model to synthesize RF radiance fields directly from physical scene geometry and transceiver locations, without requiring any reference RF measurements at inference. Specifically, RadioWorld couples two specialized modules within a dual-stream Mixture-of-Transformers (MoT) architecture: a Scene-Understanding Transformer that encodes 3D scene geometry and transceiver locations to extract environment-aware global EM propagation features, and a Field-Generation Transformer that attends to these features to synthesize the RF radiance field with the local query conditions. We also establish UrbanRF-Bench, a large-scale ray-traced benchmark spanning 657 urban scenes and 32,850 RF radiance fields across seven global cities. Extensive experiments demonstrate that RadioWorld significantly outperforms specialized baselines and accurately synthesizes RF fields at arbitrary locations in unseen cities. Code, datasets, and checkpoints will be released upon acceptance.

---


### 242. [Dual-Side Uncertainty Estimation: Calibrating Data and Model Uncertainty into a Shared Probability Space](https://arxiv.org/abs/2611.29284)

**<font color=#1a73e8>作者：</font>** Jiaxuan Gao, Yang Hu, Feihong Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal user intention analysis infers latent goals from heterogeneous behavioral observations but faces cross-modal input mismatch and output semantic errors. Existing uncertainty estimators focus on input reliability or output confidence and often reduce token uncertainty to simple statistics, overlooking structured dependencies. We propose DUE (Dual-Side Uncertainty Estimation), which jointly estimates input-side aleatoric and sentence-level epistemic uncertainty. From a single generation, Dirichlet perturbations of cross-layer representations produce an ordered token uncertainty sequence. A sequence-aware Normal-Inverse-Gamma estimator uses this sequence to quantify epistemic uncertainty and confidence in its estimate. Evidential multimodal alignment captures aleatoric uncertainty from noisy, incomplete, or inconsistent inputs. DUE calibrates both heterogeneous scores into a shared error-probability space and sequentially fuses them to estimate overall generation risk. Experiments demonstrate strong performance in input-mismatch detection, output semantic-error detection, and overall reliability estimation without repeated generation.

---


### 243. [Robust Concept Erasure in Text-to-Image Models via Simulating Brain Functional Localization](https://arxiv.org/abs/2611.29288)

**<font color=#1a73e8>作者：</font>** Manyi Li, Yufan Liu, Bing Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept erasure in text-to-image models aims to prevent a target concept from appearing in generated images while preserving general image generation capability. However, erased concepts can still be reactivated by attacks. Prior attacks mainly search text or image input spaces, leaving the initial latent space underexplored. To address this gap, we introduce IVO (Initial latent Variable Optimization), a new concept reactivation attack that changes the starting point of image generation by optimizing the initial latent. Comprehensive experiments across 8 erasure methods show that IVO reactivates erased concepts more effectively than the attack baselines, revealing a blind spot in erasure robustness evaluation. This motivates us to localize model components associated with the target concept and then treat them as intervention sites for more robust concept erasure. We propose CeFlune (Concept Erasure via Functional Localization of Unit Neurons), which adapts brain functional localization to text-to-image models. CeFlune defines linear modules as Unit Neurons and localizes concept-responsive ones by comparing their response trajectories in the model's task and resting states. It then updates the localized Unit Neurons to constrain their responses and the erased model's predictions. Across U-Net diffusion and flow-matching transformer architectures, CeFlune achieves a favorable balance between concept erasure and general image generation capability in comparisons with up to 15 baseline methods. Under IVO and 4 other evaluated attacks, CeFlune also shows lower concept reactivation.

---


### 244. [Which Failure Does an Intervention Repair? When Agent Interventions Help, and Where Self-Evolving Skills Stall](https://arxiv.org/abs/2611.29290)

**<font color=#1a73e8>作者：</font>** Zihan Jin, Gaoyuan Du, Jiate Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An intervention that improves one agent can break another, and adding a stronger harness on top need not repair the damage. Agent interventions such as skills, harnesses, and extra inference budget are nonetheless usually credited with one average gain, measured under one setup. We ask instead when each intervention helps and which failure it repairs. A matched factorial study over nine benchmarks, four models, four skill conditions, four harness levels, and three budgets, with nearly 0.9 million trajectories, changes one axis at a time. No configuration is best everywhere, interventions interact rather than add, and a harness can absorb a skill's gain, rescue a failure the skill causes, or leave the gain intact. The failure left by the current system points to the fix: missing knowledge to a stronger model, execution errors to a richer harness. Yet feedback is not recovery: a matched recovery repairs mainly failures that leave a visible error signal. Skills that evolve from the agent's own experience hit a bottleneck: they rarely beat a short human-written skill, can learn dataset shortcuts, break when moved to another model, and cannot supply missing facts, which outside information does. A benchmark-level switch to the model favored by a 20-task labeled pilot achieves both higher performance and lower cost than always using the stronger model. Agent interventions should be judged by which failure they repair and under which configuration.

---


### 245. [GALILEO: Geometric RoPE with Galilean Key Transport for Dynamic Scenes](https://arxiv.org/abs/2611.29293)

**<font color=#1a73e8>作者：</font>** Youngmin Kim, Seonghyun Jin, Jong Chul Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometry-aware rotary positional encodings, such as RayRoPE, help attention reason about the 3D spatial relationships between tokens and the query camera. However, they implicitly assume a static scene, encoding each key at its observed position regardless of when it was captured. For dynamic scenes with temporally separated input views, this mismatch places the same moving object at a different position in each input frame, so it can be rendered at an inaccurate position. While temporal encodings inform attention when a token was observed, they do not resolve where its content should be at the query time. We introduce a simple and general approach that aligns positional encodings with dynamic scene geometry through Galilean transport. Before positional encoding, each key's 3D position is transported to the query time using its estimated velocity and the temporal offset. By modifying only key positions, our method integrates directly with existing encodings, including RayRoPE and URoPE, without altering their formulations. Velocities can be obtained from arbitrary sources. By default, we estimate them from token correspondences within the network. Integrated into LVSM, our method improves dynamic view synthesis on Syn4D, dynamic Objaverse, and real-world Stereo4D videos over baselines. Ablations show that encoding velocities as token features yields smaller gains, while attention visualizations reveal that our method attends to query-time locations of moving content, unlike RayRoPE. Beyond view synthesis, our method also reduces tracking errors on dynamic objects in a pretrained 3D point tracker and improves moving-vehicle generation in a video generator.

---


### 246. [DoppelVet: Comparative Safety Verification for Self-Evolving Agents](https://arxiv.org/abs/2611.29306)

**<font color=#1a73e8>作者：</font>** Yifan Duan, Du Yin, Siyuan Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents improve by retaining feedback as reusable memories or skills, but every mistaken approval can shape many future behaviors. Two updates can provide exactly the same evidence to a verifier yet produce opposite safety outcomes, so the verifier cannot distinguish them from that evidence alone. We introduce DoppelVet, a verification framework that checks proposed updates before they enter an agent's persistent state. Without access to safety labels, DoppelVet constructs an alternative that matches every signal used by the existing verifier. It replays both updates from the same state and directly compares their behaviors in both presentation orders before deciding whether to retain the candidate. We evaluate DoppelVet on DoppelVet-Grid and DoppelVet-Tool, covering executable programs and natural-language memories. Across nine open-weight and proprietary verifiers, DoppelVet raises mean harmful-update detection AUC from 0.762 to 0.940 on DoppelVet-Grid and from 0.681 to 0.826 on DoppelVet-Tool, outperforming VaG and AgentDoG 1.5. On DoppelVet-Grid, it reduces trajectories experiencing degradation from 30.39% to 0.43% over a ten-generation self-update loop and leaves no final degradation.

---


### 247. [Where Does Personalization Reside in Photo Editing? Evidence from One Photographer's Lightroom History](https://arxiv.org/abs/2611.29307)

**<font color=#1a73e8>作者：</font>** Dongwu Qian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized photo-editing systems must infer both a photographer's recurring preferences and the intent of a particular shoot, yet these signals are rarely evaluated separately. We study interpretable Lightroom adjustments in a longitudinal, private dataset of 3,193 edited photographs from 41 catalogs by one professional photographer, with holdouts formed at the batch level. We compare absolute and prior-relative targets, image-conditioned predictors, and estimators that receive a small set of edits from the target batch. Residual prediction improves validation error, but its advantage on held-out batches is small and not significant under a batch-clustered bootstrap (0.592 vs 0.582 EV exposure MAE). In a batch-shared protocol, closed-form shrinkage using 4, 8, or 16 same-batch anchors reaches 0.466, 0.457, or 0.453 EV with the best estimator at each k, compared with 0.586-0.592 EV for the prior-only baseline; the paired reductions are significant under a batch-clustered bootstrap. Learned anchor-conditioned heads do not improve on this closed-form estimator, and a negative-trained prior already yields a low cold-image false-edit rate, leaving little benefit for an additional gate. The recommended estimator is closed-form and auditable, and it requires only a handful of same-batch edits. A render-space check against 383 native Lightroom exports reproduces the ranking: at k=8, online EB lowers Delta E00 against the prior by 0.41 (p=0.042), and the photographer's true parameters lower it by 0.78 (p=0.034). An appendix extends the action space from six to thirteen global controls: a same-batch median look lowers rendered chroma toward the export, while a per-photograph residual head again fails to transfer. The study is limited to one photographer and does not claim that slider accuracy measures aesthetic preference.

---


### 248. [PrimiTok: Learning to Diversify and Allocate Primitives for Visual Tokenization](https://arxiv.org/abs/2611.29311)

**<font color=#1a73e8>作者：</font>** Yizhu Chen, Chen Ju, Donghao Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unifying visual understanding and generation requires representations that preserve both semantic information and fine-grained image details. Continuous tokenizers trained primarily for semantic alignment may omit fine-grained reconstruction details, whereas discrete tokenizers face information loss from codebook quantization. Conventional multi-codebook designs assign every token the same number of codewords regardless of local content. We instead view codewords as reusable visual primitives whose allocation and composition adapt to each token. We introduce PrimiTok, a compositional visual tokenizer that represents each visual token through adaptive allocation and weighted composition of learned codebook primitives. PrimiTok integrates two complementary components: Diverse Quantitative Primitives (DQP), which encourages diversity among sub-codebook centroids to reduce redundancy, and a Dynamic Primitive Allocator (DPA), which selects primitives according to token complexity. Embedding quantization error supervises how many primitives are selected from each sub-codebook, and DPA aggregates them with input-dependent weights. Joint reconstruction and image--text contrastive learning encourage the resulting representations to retain visual fidelity and semantic alignment. Experiments demonstrate improved reconstruction and semantic alignment over SOTA baselines, with further evaluations on multimodal understanding and visual generation.

---


### 249. [Prompt-Consistent Cross-View Object Geo-Localization](https://arxiv.org/abs/2611.29312)

**<font color=#1a73e8>作者：</font>** Lingyun Xing, Wenning Hao, Kai Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view object geo-localization (CVOGL) aims to locate an object indicated by a click point in a ground or drone query image within a satellite reference image. Through a quantitative prompt-sensitivity evaluation, we find that existing CVOGL methods suffer from a prompt-disobeying overfitting problem: when the click point is moved or removed, their predictions barely respond, indicating that the models rely on spurious feature correlations rather than genuinely following the prompt semantics. We trace this behavior to the limited scale of the benchmark dataset, which contains only 4,343 prompt-object pairs per task, so that the models simply memorize the object associated with each scene instead of learning the true prompt-to-object correspondence. To address this, we propose two plug-and-play components. First, we construct the CVOGL-MO dataset by expanding the existing training and test sets with diverse multi-object annotations, mitigating the memorization that induces shortcut learning. Second, we propose the Cross-View Co-Scene Multi-Object Contrastive Loss (CVMCL), which enforces distinct feature representations for different click points within the same scene, compelling the model to follow prompt instructions. We further design a prompt-sensitivity evaluation protocol with prediction-shift metrics, providing the first quantitative measurement of prompt-following capability for CVOGL. Both components are architecture-agnostic and can be integrated into existing methods without any architectural modification. Experiments on three representative backbones show that our components substantially improve prompt-following accuracy on the new multi-object test sets and markedly increase prompt sensitivity. Our dataset and code will be publicly released at this https URL.

---


### 250. [Reward Tilting via Semantic Noising](https://arxiv.org/abs/2611.29318)

**<font color=#1a73e8>作者：</font>** Rafał Karczewski, Peter Blohm, Markus Heinonen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Steering a generative model toward a desired property typically requires separate fine-tuning for each reward or additional computation during sampling. We propose semantic noising, which conditions generation on a noisy semantic representation of the data. The resulting posteriors correspond to exponential tilts by linear-quadratic rewards in semantic space, allowing a single model to support objectives and strengths chosen after training. A conditional generator can be trained to approximate these posteriors directly, while models that generate semantic representations by diffusion provide analytic tilted denoisers for the same family of rewards. We illustrate semantic noising in three settings. An autoregressive molecular generator trained with semantic noising controls properties individually and jointly, with a better reward--KL trade-off than property-conditioned models. On ImageNet, a joint diffusion model of images and their CLIP embeddings achieves FID comparable to REG, and tilting it toward a higher aesthetic score matches the best of 16 samples at the cost of a single sample. Finally, pretrained factorized models such as Kandinsky 2.2 support the same tilts without retraining.

---


> [!TIP]
> 当前位于：**201-250**（第 5/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
