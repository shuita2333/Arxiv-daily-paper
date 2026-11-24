# 📦 其他研究 | 2026年11月25日

> 本类共 **569** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-569](./part-12.md)

---

### 451. [Target-Part Preference Optimization for Part-Aware 3D Generation](https://arxiv.org/abs/2611.30472)

**<font color=#1a73e8>作者：</font>** Zishan Qin, Rui Li, Zeyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Part-aware 3D generation requires not only globally plausible objects but also complete, well-separated semantic parts, yet high-quality part decompositions remain too scarce to support large-scale supervised fine-tuning. We study whether preference fine-tuning based on Direct Preference Optimization (DPO) can adapt a pretrained part-aware generator from limited part-annotated data without architectural changes. We rank candidates generated with different random seeds against ground-truth (GT) geometric metrics, and select the (object, target-part) examples with the largest across-seed quality gap. Each selected example stores a seed pair whose two flow trajectories share one clean GT compositional latent and differ only in Gaussian noise. We derive a reference-relative target-block preference loss from FlowDPO that compares the two trajectories against a frozen reference model. GT flow-matching losses on the target block and complete part set provide absolute supervision, while only the diffusion transformer (DiT) is updated. Human-ranked controls test an alternative ordering source, and synthetic cropping provides controlled loser targets that are incomplete by construction. Among the three training-set scales, the medium-scale setting gives the strongest result on held-out Objaverse and outperforms both the pretrained generator and the reported direct supervised fine-tuning baseline on the multi-part aggregate. Further analysis shows sensitivity to pair ordering, target-part coverage, and the balance between pairwise and GT supervision. Cross-dataset experiments show less consistent gains under distribution shift.

---


### 452. [Do learned image captioning metrics generalize? Auditing duplicated samples in human-judgment benchmarks](https://arxiv.org/abs/2611.30488)

**<font color=#1a73e8>作者：</font>** Xiaochen Zhang, Jin Li, Chunlong Xia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learned image captioning metrics are trained and tested on human judgments, so their reported correlation is a claim about generalization. We audit this claim for the three most recent collections of such judgments, Polaris, Nebula, and Spica, matching images at the pixel level. First, test samples reappear in training sets: the Spica training set contains about two-thirds of the Polaris test set, with identical human ratings. Second, controlled retraining shows that duplicates can inflate a metric: for Pearl, the gain is confined to the duplicated samples and grows with every epoch; for DENEB, it stays below one point. The gain depends on the learner and on how often a training set repeats a sample. Third, Kendall's $\tau$ over all samples is the sum of two terms, detecting captions with the lowest human score and ranking the others; the first supplies most of the reported correlation and is nearly saturated. The recent test sets cannot order Polos, DENEB and Pearl consistently, and a ridge regression on frozen features matches or exceeds all three. Fourth, we propose a protocol that ranks a learned metric only with a model trained without test samples, reports both terms, and compares metrics by paired tests. Under it, zero-shot vision--language judges rank first on the three recent test sets, and a fine-tuned judge ranks first on the three earlier benchmarks. The same analysis applies to any evaluator learned from human judgments; filter lists and code are released at this https URL .

---


### 453. [Policy Invariance Is Not Learning Invariance: Potential-Based Reward Shaping for Navigation with a Limited View](https://arxiv.org/abs/2611.30492)

**<font color=#1a73e8>作者：</font>** Nodirjon Khabibullaev, Rajat Dandekar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Potential-based reward shaping (PBRS) does not change the optimal policy, but how much it speeds up learning depends on the potential and on effects outside this guarantee. We analyse how PBRS changes the one-step reward while it preserves the discounted return: a per-step $(\gamma-1)\Phi$ term, the terminal-state rule, a constant shift of the potential, and positive cycles in a bonus that is not potential-based. We then measure these consequences in pre-registered experiments with a PPO agent. The agent has a limited egocentric view and is tested on two MiniGrid navigation tasks (160 runs, 10 seeds per condition). On LavaCrossing, a geodesic (BFS) potential learned faster than both the sparse baseline and a Euclidean potential with a 7x7 and a 5x5 view (AUC difference +0.27 to +0.39, Holm p between 0.007 and 0.0499). The Euclidean potential did not differ from the baseline. In 20 runs with a non-potential bonus, none of the agents learned the task. The Euclidean potential caused more than twice as many deaths in lava during early training. View size did not detectably change the benefit of shaping. With a 5x5 view on SimpleCrossing, some BFS runs got stuck in loops and never learned; shifting the potential did not remove this, so the per-step term alone does not explain it.

---


### 454. [From Dependent Ciphertexts to Sharp Bounds for Polynomial Evaluation in BGV](https://arxiv.org/abs/2611.30499)

**<font color=#1a73e8>作者：</font>** Chiara Marcolla, Nadir Murru, Matilda Urani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A central challenge in Fully Homomorphic Encryption (FHE) is the selection of ciphertext moduli, which depends on accurately estimating noise growth during homomorphic evaluation. Choosing excessively large moduli reduces the efficiency and scalability of the scheme, whereas underestimating noise can result in decryption failures and potential security vulnerabilities. Average-case analyses have provided promising probabilistic estimates of noise growth in practical FHE computations. However, recent studies indicate that reliable estimates must account for dependencies among ciphertext errors, as neglecting these correlations can systematically underestimate noise.
This work presents the first average-case analysis for the BGV scheme that accounts for both correlations induced by secret/public keys and ciphertext dependencies. We propose new variance estimates for the noise coefficients in homomorphic additions and multiplications involving dependent ciphertexts, and extend our framework to the homomorphic evaluation of polynomial functions, which is widely employed in FHE applications. Our theoretical estimates closely align with experimental observations, exhibiting discrepancies smaller than 1.2 bits.
Finally, these estimates are adopted to choose the initial BGV parameters, leading to significantly smaller ciphertext moduli compared to those currently adopted in widely used FHE libraries, thus improving the efficiency of the scheme. Compared to OpenFHE, we obtain an average reduction of about 11.5% in the ciphertext modulus size, while relative to HElib, we reduce the ratio between consecutive moduli up to 23 bits per level in practical settings.

---


### 455. [Why Calibrated BM25 Filtering Barely Reduced Context on LongMemEval](https://arxiv.org/abs/2611.30500)

**<font color=#1a73e8>作者：</font>** John Knight, Erchin Serpedin, Hasan Kurban  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An assistant that summarizes old conversations may later need a detail from the original exchange. It can score archived passages against the question, but only passages that fit in the prompt reach the answering model. We tested whether a BM25 filter saves input tokens once that limit is taken into account. We calibrated the filter on passages that individually corrected an answer the model got wrong from the summaries alone. Across 75 LongMemEval questions, filtering changed one prompt and saved 0.096% of input tokens. With and without the filter, the model answered the same questions correctly under a second automated grading. On a random sample, two human graders' settled judgments agreed with the automated grades in 92.9% of definite comparisons (Cohen's kappa = 0.805). Building on earlier work that distinguishes retrieved evidence from delivered evidence, we give an exact test for packers that try whole passages in a fixed order and skip any that do not fit. Run the packer without the filter. The prompt changes exactly when an admitted passage scores below the cutoff. Code and data: this https URL

---


### 456. [A CPU-Only Framework for Mining Collectively-Behaving Bots in MMORPGs](https://arxiv.org/abs/2611.30502)

**<font color=#1a73e8>作者：</font>** Hyunsoo Kim, Jaeman Son, Sangdeok Seo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> MMORPGs continually face automated programs (bots) that disrupt gameplay balance and in-game economies. An unsupervised Transformer framework can mine collectively behaving bot groups, but its multi-GPU training is costly in live operations. We show that such GPU-trained sequence models are not strictly necessary for this task. Our CPU pipeline pairs zone embeddings learned from movement context, which place teleport-linked zones close together, with a training-free coordinate kernel, and then applies density clustering. It trains 3-5$\times$ faster than the GPU-based Transformer (56-86$\times$ on the same CPU) while matching its mining quality on two commercial MMORPGs, and has been deployed since late 2024. We also share deployment lessons on how to set the clustering threshold and when to retrain.

---


### 457. [De Novo Generation of Odorant Molecules with Targeted Olfactory Receptor Activation Patterns](https://arxiv.org/abs/2611.30509)

**<font color=#1a73e8>作者：</font>** Kexin Zhang, Manhao Guan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Odor perception arises from a combinatorial code in which each molecule activates a specific subset of olfactory receptors (ORs), and the resulting activation pattern determines the perceived smell. We present a framework for de novo generation of molecules predicted to match target multi-receptor activation profiles. We first construct a panoramic binding matrix over 20 ORs, then cluster it to discover representative activation patterns, and finally formulate a structured selectivity loss, combining pairwise ranking, distribution matching, and complexity constraints, to steer a molecular generator via reinforcement learning. Across nine target profiles of varying complexity, our method achieves high predicted selectivity within 18000 oracle calls and provides the largest gains on profiles that are rare under the prior, especially broad-spectrum and sparse-activator targets.

---


### 458. [When Do Spatial Plans Help Text-to-Image Generation? Causal Control, System Utility, and Text Responsiveness](https://arxiv.org/abs/2611.30514)

**<font color=#1a73e8>作者：</font>** Lu Han, Jingyao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A generator can follow a spatial plan, but the benefit of supplying that plan depends on what the model can already do from text. In a controlled study with 18 paired training seeds, correcting predicted positions and sizes improves spatial intersection-over-union by 0.030, yet direct text is non-inferior at matched training compute. In a pretrained generator, a fixed rule layout improves two-object task success over the same text-only adapter by 12.50 percentage points, mostly by separating objects that already appear in the correct order. We then ask whether a more precise instruction can achieve the same separation across conditioning paths. On 288 new task families, adding a minimum-gap instruction improves success by 37.15 points with the text-only adapter, by at most 0.69 points with widely spaced regions, and by 6.94 points with tightly spaced regions. Under tight regions, 230 of 288 baseline images have the correct objects and direction yet miss the required gap, ruling out a high baseline success rate as the sole explanation for the weak text response.

---


### 459. [Field-Level Crop Classification via Similarity-Induced Supervision from Imperfect Labels](https://arxiv.org/abs/2611.30515)

**<font color=#1a73e8>作者：</font>** Raul Lomonte Figueiredo, João Rebouças Dorea, Dário Augusto Borges Oliveira  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Regional-scale crop mapping is critical for food production monitoring, yet remains challenging in tropical regions, where persistent cloud cover limits optical imagery. Synthetic aperture radar (SAR) enables continuous observation throughout the agricultural cycle, but a second obstacle is label quality: national-scale land cover products exhibit systematic biases that underestimate less prevalent crops, and training directly on them inherits and amplifies their errors. This work proposes a methodology to build large-scale crop classification models from imperfect public land cover products, requiring no new field campaign, ground survey, or manual label correction. The approach combines two mechanisms. The first reduces the semantic inconsistency of the labels by shifting supervision from the sample level to the group level: a similarity-based clustering model organizes SAR time series into coherent groups, and noisy labels are used only to assign each group its most representative class. The resulting clusters are highly pure with respect to the reference classes (89.0% and 91.2% in the two study regions). The second reduces the spatial inconsistency of the predictions: a segmentation model delineates crop field boundaries from optical imagery, and patch-level predictions are consolidated by majority voting within each field, yielding spatially coherent maps. Evaluated in two Brazilian municipalities, Campo Verde (Mato Grosso) and Luís Eduardo Magalhães (Bahia), the approach consistently outperforms the noisy baseline in mean class accuracy, with gains of up to 10.14 percentage points, especially for minority crops. A state-scale analysis across Mato Grosso and Bahia shows stable behavior without further model adjustment, and the derived municipal crop areas are consistent with official IBGE/PAM statistics, an independent estimate the model never observes.

---


### 460. [VeriOrigin: A Proactive Image Protection Framework for Provenance, Tamper Localization, and Lossless Recovery](https://arxiv.org/abs/2611.30523)

**<font color=#1a73e8>作者：</font>** Jiale Chen, Wei William Wang, Junnan Yin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Versatile watermarking, which seamlessly integrates provenance and tamper detection, has recently attracted widespread attention. In this paper, we propose \textbf{VeriOrigin}, a comprehensive and unified image protection framework that not only robustly achieves provenance and highly precise tamper localization under various complex distortions, but also guarantees perfect recovery of the original cover in lossless channels. To realize this framework, we depart from conventional flow based architectures. Instead, we design \textbf{XOnet}, a CNN based invertible encoder. XOnet comprises two standard CNN based watermarking sub networks, Xnet and Onet, which achieve reversibility through cross residual prediction. Based on XOnet, we train the proactive protection scheme via a two stage strategy: first optimizing the watermarking branch, followed by the tamper localization branch. During inference, the cover image undergoes sequential watermarking and tamper residual embedding. Extensive experimental results on four datasets demonstrate that VeriOrigin achieves precise tamper localization and strong robustness, while guaranteeing lossless cover recovery for integrity authentication. Project page is available at this https URL

---


### 461. [Assembly-JEPA: Using World Models for Fine-Grained Industrial Image Verification](https://arxiv.org/abs/2611.30530)

**<font color=#1a73e8>作者：</font>** Michael Hollmer, Andreas Fischer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated verification of industrial assembly processes remains a challenging problem due to substantial visual variability, limited availability of labeled defect data, and the fine-grained nature of many assembly errors. Existing approaches often rely on object detection, CAD models, or supervised classification pipelines, which can struggle to generalize across changing products and assembly configurations. In this work, we propose a novel self-supervised assembly verification framework based on Joint Embedding Predictive Architectures (JEPAs). Starting from the JEPA-based world model LeWorldModel, we investigate how the architecture must be adapted to verify the correctness of fine-grained assembly operations. To this end, we formulate assembly verification as a predictive world modeling task operating on before-and-after observations of assembly processes. Experimental results on industrial assembly tasks demonstrate that the proposed approach reliably detects both fine-grained incorrect assembly states and action-state mismatches, achieving an AUROC of 86.9% on a newly introduced assembly verification dataset. These results indicate that JEPA-based predictive representations constitute a promising foundation for robust and data-efficient industrial assembly verification.

---


### 462. [ReDiffDet: Rotation-equivariant Diffusion Model for Oriented Object Detection](https://arxiv.org/abs/2611.30531)

**<font color=#1a73e8>作者：</font>** Zeyu Ding, Yong Zhou, Jiaqi Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The diffusion model has been successfully applied to various detection tasks. However, it still faces several challenges when used for oriented object detection: objects that are arbitrarily rotated require the diffusion model to encode their orientation information; uncontrollable random boxes inaccurately locate objects with dense arrangements and extreme aspect ratios; oriented boxes result in the misalignment between them and image features. To overcome these limitations, we propose ReDiffDet, a framework that formulates oriented object detection as a rotation-equivariant denoising diffusion process. First, we represent an oriented box as a 2D Gaussian distribution, forming the basis of the denoising paradigm. The reverse process can be proven to be rotation-equivariant within this representation and model framework. Second, we design a conditional encoder with conditional boxes to prevent boxes from being randomly placed across the entire image. Third, we propose an aligned decoder for alignment between oriented boxes and image features. The extensive experiments demonstrate ReDiffDet achieves promising performance and significantly outperforms the diffusion model baseline.

---


### 463. [BEND: Spectral Bregman Losses for Multi-Image Unlearning in Diffusion Models](https://arxiv.org/abs/2611.30532)

**<font color=#1a73e8>作者：</font>** Mohamed-Hicham Leghettas, Markus Püschel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models memorize training images and reproduce them almost verbatim when prompted, creating copyright and privacy liabilities. Data unlearning erases the influence of specific training samples from a trained model without retraining, and is two-sided: it must forget the targets while preserving generation quality on everything else. Prior methods use the squared-L2 diffusion loss, at most with a hand-set frequency mask; however, it is known that every Bregman divergence is a mathematically valid choice and the squared-L2 is only the simplest example. BEND is the first to search this family: it fits a spectral Bregman divergence to the unlearning task through a bilevel loop, so the loss itself is shaped to forget thoroughly while protecting quality. It also redirects a memorized image to the mean of its retain images, where ReTrack, the state of the art, redirects it to a single near-copy. On Stable Diffusion, a single BEND model erases all 48 verifiably memorized benchmark images at once. It forgets at least as much as per-target, sequential, and jointly trained ReTrack (SSCD 0.084 versus 0.094-0.120), at the quality of the model before unlearning (CLIP-IQA 0.81 versus 0.64-0.69). BEND also outperforms the state of the art on CelebA-HQ in all three measures of the benchmark, and matches or exceeds it on MNIST and CIFAR-10.

---


### 464. [Where Compositionality Hides: Shared-Content Interference in Vision-Language Retrieval](https://arxiv.org/abs/2611.30538)

**<font color=#1a73e8>作者：</font>** Chimata Anudeep, Harsh Vardhan Poddar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Paired compositional benchmarks such as Winoground ask each image to prefer its matching caption and each caption to prefer its matching image. A failed Group decision can come from a wrong caption preference or from the cross-image comparison alone, and Group Score merges the two. Choosing between retraining the encoder and changing the scoring rule therefore requires separating them. We study mean-erasure, which projects each frozen image embedding away from the mean of the two normalized candidate captions. We prove that the projection preserves every within-image caption ranking and makes Group Score equal baseline Text Score. On Winoground, mean-erasure raises CLIP ViT-B/32 Group Score from 9% to 31%, and five CLIP and SigLIP checkpoints gain 21 to 27 percentage points. ColorSwap shows a similar gain for color-object binding. A score decomposition shows that about 60% of Image failures already score the correct joint assignment above the swapped one and fail only on an offset between the two images. Fixed corrections and a learned bilinear scorer gain under one point. A direction estimated from retrieved captions gains about five points with two captions and falls below baseline with sixteen. Before retraining an encoder for paired retrieval, measure the Group loss that mean-erasure recovers: gains beyond baseline Text Score require changing the caption decisions themselves.

---


### 465. [SVUBench: A Comprehensive Benchmark for Proactive Streaming Video Understanding](https://arxiv.org/abs/2611.30541)

**<font color=#1a73e8>作者：</font>** Yuxuan Liang, Bohan Zhang, Haiyang Yu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Proactive streaming video understanding requires models to interpret unfolding events, respond timely, and retrieve relevant historical evidence. To systematically evaluate these capabilities, we introduce SVUBench, a comprehensive proactive streaming video benchmark comprising 12,131 questions and 62,881 answer points across ten proactive tasks spanning Perception, Understanding, and Reasoning. Constructed through model-assisted annotation and human verification, SVUBench introduces two complementary interaction modes. Basic evaluates sustained proactive responses from video onset, while Trajectory requires historical recovery and continuous response updates following task activation during streaming. A Duration-Scaled Challenge further evaluates these capabilities across four video duration tiers. We develop the Proactive Response Score (PRS) with task-adaptive answer windows to jointly assess answer correctness, response timeliness, historical consistency, and content quality. Extensive experiments and analysis reveal the strengths and limitations of existing models, highlighting directions for advancing proactive streaming video understanding.

---


### 466. [Reproducible by Seed? Not on GPUs: Batch-Dependent Non-Determinism in Text-to-Image Models](https://arxiv.org/abs/2611.30545)

**<font color=#1a73e8>作者：</font>** Javier Conde, Xiuyuan Qi, Shanshan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In text to image AI models, fixing the prompt and the random seed is widely assumed to fix the image. We show that it does not on GPUs. We evaluate six text-to-image models (diffusion and autoregressive) under four numerical precisions and quantizations on three GPU types (RTX A6000, RTX 6000 Ada, and H100 NVL), across up to 100 prompts per set for all six models. For each configuration we compare, with the prompt and seed fixed, the image generated alone with the image generated inside a batch, and we also compare across GPUs. Every replay control reported here is bit-exact, so the variation is not random noise: the execution setting, mainly the batch composition and the GPU, decides the output. The effect is large and model dependent. Structural similarity between the single-image and the batched output falls to 0.580 for an autoregressive model in bf16 and to 0.551 with int8. For a second autoregressive model in bf16 it falls to 0.261 with sampled decoding and to 0.229 with greedy decoding, and for an fp8 diffusion model to 0.68. A diffusion model in bf16 stays close to the batch-1 output (0.96-0.98) but changes every image. In most cases the batched image is a different but equally valid image; in some, such as prompts with digits and counters, it is visibly worse. Cross-GPU differences are of the same order as the batch effect: for one autoregressive model in bf16 compared across two GPU architectures (RTX 6000 Ada versus RTX A6000), no image is bit-identical and the cross-GPU LPIPS (0.355 to 0.383) matches the batch effect within one GPU (0.347 to 0.381). The consequences are direct: seeds do not make results reproducible, benchmarks and image-quality comparisons that mix batch sizes or hardware can be biased, and safety audits and A/B tests on generated images need the serving setup reported.

---


### 467. [Irreducible shallow tanh neural networks are a manifold](https://arxiv.org/abs/2611.30553)

**<font color=#1a73e8>作者：</font>** Ivan Bioli, Isabella Carla Gonnella, Carlo Marcati 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks (NNs) have been increasingly used as function approximators, motivating the study of the geometry of their function spaces. We study the set of functions represented by shallow neural networks with hyperbolic tangent activation, fixed input and output dimensions, and $n$ hidden neurons. In particular, we prove that the subset represented by irreducible networks in the sense of Sussmann (Neural Networks, 1992), i.e., networks with no redundant neurons, is a smooth embedded submanifold of the Sobolev spaces $\mathrm{W}^{\ell,p}$ on bounded sets for any $\ell\in\mathbb{N}$ and $p\in[1,+\infty]$. The key step is to show that if a sequence of networks converges in $\mathrm{W}^{\ell,p}$ to an irreducible network with the same number of hidden neurons, then the parameters of the approximating networks remain bounded. Finally, we show that this manifold has exactly $n+1$ connected components when both the input and output are scalar, and is connected otherwise.

---


### 468. [Splitting Belief Bases Conditionally based on Constraints for c-Representations and their Solutions](https://arxiv.org/abs/2611.30556)

**<font color=#1a73e8>作者：</font>** Lars-Phillip Spiegel, Christoph Beierle, Gabriele Kern-Isberner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Splitting notions for conditional belief bases aim at localizing reasoning and computation tasks to subbases containing only the relevant parts of the belief base. Among the different reasoning mechanisms, c-representations, a special kind of Spohn's ranking models, have been shown to provide high-quality inferences. c-Representations can be conveniently specified via a constraint satisfaction problem. In this article, we introduce the notion of conditional constraint splittings, extending constraint splittings by also allowing the subbases to share conditionals. Taking inspiration from conditional syntax splittings, we identify the subclasses of safe and fully localized conditional constraint splittings, allowing us to locally and independently solve the constraint system on the subbases. We also generalize solution splittings for c-representations to safe conditional c-solution splittings and provide an in-depth analysis of their relationship to conditional constraint splittings. Additionally, we elaborate on the relationship of these new splitting notions to safe and generalized safe conditional syntax splittings and also to safe covers, which have been proposed for localized computation of c-representations.

---


### 469. [JONES-19: A Cultural Image Dataset Based on The Grammar of Ornament](https://arxiv.org/abs/2611.30558)

**<font color=#1a73e8>作者：</font>** Linh Pham, Stuart Shieber, David Alvarez-Melis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce JONES-19, a high-quality image dataset documenting 1,901 ornament designs belonging to nineteen human cultures. The images and their annotations are based on an open access archive of The Grammar of Ornament (London, 1856), by Owen Jones. The dataset poses numerous challenges as a benchmark for computer vision classification tasks and for research at the intersection of machine learning and art and design: a small sample size, image samples of human-designed artifacts rather than common objects in-context or natural scenes, imbalanced class distribution, and image distinctions based on fine details involving line patterns, reliefs, and colors. As a design-inspired dataset, JONES-19 can serve as a benchmark for various research fields, such as visual recognition, data-efficient learning, art-historical research, architectural style analysis, and cultural heritage. This paper describes the curation of the JONES-19 dataset and reports a baseline classification benchmark that evaluates the suitability of the dataset for training classifiers and exposes insights into inter-class relationships--particularly cultural similarities--by examining patterns in misclassification errors. The dataset and its accompanying documentation are available at: this https URL.

---


### 470. [Reliable Recursive Memory for Causal Multi-scale Video Polyp Segmentation](https://arxiv.org/abs/2611.30568)

**<font color=#1a73e8>作者：</font>** Tong Wang, Wenbo Peng, Yaolei Qi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video polyp segmentation (VPS) is essential for computer-aided colonoscopy, as it localizes and tracks polyps frame by frame. However, VPS remains challenging because polyps resemble the mucosa and change quickly in scale, which calls for history beyond a short clip, and because blur, specular highlights, and occlusion often degrade only part of a frame. Existing methods keep history as whole frames, so their cost grows with the history length, and a partly degraded frame carries its degraded content to later predictions. To address these issues, we propose STREAM, a streaming framework for VPS that extends the causal multi-scale aggregation (CMA) of our conference work from a fixed clip to an online stream. STREAM introduces a Recursive Slot Memory (RSM) that summarizes multi-scale features and soft foreground and background cues into a constant number of slots, which the current features read and pass to CMA, supplying long-range history at a constant cost. Furthermore, we design Reliability-Aware Slot Writing (RASW), which estimates a pixel-level quality map from the current frame, supervised by its local error, and uses it to control which locations are written into RSM and how much each slot is updated. Experiments on SUN-SEG and CVC-ClinicDB demonstrate that STREAM achieves state-of-the-art performance, improving the Dice of the conference model from 81.3% to 85.7% on the hardest subset while running at 48 FPS with a constant state of 0.32 MB. Code will be released at this https URL.

---


### 471. [Write, Evolve, Read: Streaming Cameras into a Persistent World State for 4D Occupancy Forecasting](https://arxiv.org/abs/2611.30573)

**<font color=#1a73e8>作者：</font>** ZiAn Wang, Tianyi Wang, Zhihao Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D occupancy forecasting predicts the 3D semantic occupancy of a driving scene seconds ahead. Over a few seconds, the scene changes little while the vehicle moves, so most of the space ahead has already been seen. Sorting the future into unchanged, changed, and unseen space, we find that current camera-based world models fall short on the unchanged part: they fail to hold on to what they have already seen, rather than to forecast what will change. We therefore make what the model has seen its state. PersistWorld streams camera frames into a persistent 3D world state anchored in the scene, writing each frame once instead of rebuilding the state from past frames. The state is learned end to end with the forecast, and an evolver predicts it at any queried time along the ego trajectory. On Occ3D-nuScenes, PersistWorld raises the IoU of the best camera-based world model by 19 points at 1-3 s and by 18 to 24 points up to 8 s, while running more than twice as fast. Code and models: this https URL. Project page: this https URL

---


### 472. [Physics-Constrained Neural ODEs for Learning Traffic Dynamics and Trajectories from Road Entry/Exit Times](https://arxiv.org/abs/2611.30577)

**<font color=#1a73e8>作者：</font>** Dennis Bogatov Wilkman, Karl Henrik Johansson, Matthieu Barreau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of learning microscopic traffic dynamics and reconstructing vehicle trajectories from section entry/exit timestamps (EET) recorded by cameras and from the positions of a probe vehicle leading the platoon. The dynamics are difficult to recover as each vehicle's position is measured only at two points, and its trajectory between them is unknown. By combining Neural ODEs with a local density approximation, we learn a follow-the-leader model whose speed--density relation is a neural network. With such sparse data, an unconstrained network may learn physically unrealistic relations, such as negative speeds or non-zero speeds on a fully congested road. We therefore introduce a normalization that, applied to a monotone neural network with a learned regime change, enforces the endpoint conditions, guaranteeing an admissible speed--density relation while provably retaining the ability to approximate any admissible one. We validate the method on first- and second-order simulations, recovering the speed--density relation of the first-order model and reconstructing the trajectories of both models, with mean maximum position errors of 2.50~m and 2.51~m, respectively, on a 125~m road segment. On real-world ring-road data, the proposed model still yields an admissible relation, whereas both baselines violate the constraints; the large spread in the data, however, highlights the limitations of a first-order model with homogeneous driver behaviors.

---


### 473. [A Search Worth a Billion Pixels: Explaining Gigapixel Classifiers](https://arxiv.org/abs/2611.30578)

**<font color=#1a73e8>作者：</font>** Danilo Danese, Angela Lombardi, Tommaso Di Noia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perturbation-based attribution methods explain model predictions without accessing their internal representations, but scaling them to high-resolution images requires balancing perturbation granularity and computational cost. Fine-grained perturbations require many model evaluations, whereas coarse masks may overlook small but relevant evidence. We introduce Wavelet Find-and-Refine (WaFR), a model-agnostic attribution method combining adaptive hierarchical search with sparse multiscale regression. By selectively refining regions that influence the prediction, WaFR maintains fine-grained localisation with a computational cost that depends on the spatial distribution of the evidence. As image resolution increases to 8,192 pixels per side, WaFR maintains a Pointing Game score of at least .995 in controlled localisation experiments, including at matched forward-pass budgets. On gigapixel whole-slide images, it requires a median of 176 forward passes and achieves the highest mean patch-level AUROC among the evaluated perturbation-based methods (.949).

---


### 474. [Interrogation Protocols for AI Control](https://arxiv.org/abs/2611.30583)

**<font color=#1a73e8>作者：</font>** Aniruddh Pramod, Matthew Khoriaty, James Lucassen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As the intelligence of an AI agent increases relative to a trusted monitor, so does the risk that the monitor will fail to understand the agent's actions or to evaluate them confidently. We introduce interrogation protocols to a high-stakes AI control setting, and allow the monitor to ask the untrusted agent questions about confusing actions. For interrogation to improve safety, a weaker model must be able to distinguish misleading explanations produced by an attack policy from genuine ones produced by an honest policy. We find that on a held-out subset of BashArena, an interrogation protocol improves safety at a 1% audit budget from 72.6% for an actions-only baseline, which does not use interrogations, to 79.5% (+7.0 pp [+0.9, +20.1], 95% paired bootstrap interval), but most of this uplift can be captured by having a trusted model state a specific concern. More broadly, our work suggests that interrogating agents can improve safety, allowing monitors to catch more attacks at a larger capability gap.

---


### 475. [DARE: Dual-Level Adversarial Learning with Domain-Aware Regularization for Whole Slide Image Classification](https://arxiv.org/abs/2611.30589)

**<font color=#1a73e8>作者：</font>** Yuxuan Jiang, Haichuan Dong, Manning Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathological whole slide images (WSIs) exhibit substantial domain shifts across hospitals due to variations in scanning devices, staining protocols, and tissue preparation procedures, leading to significant performance degradation when models are applied to data from different sources. Although unsupervised domain adaptation (UDA) has shown strong performance in transferring models from a labeled source domain to an unlabeled target domain in natural images, it remains relatively underexplored in computational pathology. The ultra-high resolution of WSIs and their pronounced inter-slide and intra-slide heterogeneity pose unique challenges for domain adaptation, often rendering existing UDA methods unstable and susceptible to negative transfer. To address these challenges, we propose Dual-level Adversarial learning with domain-aware REgularization (DARE), a plug-and-play UDA framework for WSI classification. DARE incorporates adaptive pseudo-labeling within a teacher-student architecture to provide stable supervision for the target domain, alongside adversarial alignment of both patch-level and slide-level embeddings. Together, these components enable the joint optimization of semantic representations at both levels for cross-domain alignment. We further introduce domain-aware attention masking to regularize attention and improve cross-domain generalization. Extensive experiments on four public WSI datasets demonstrate that DARE consistently outperforms state-of-the-art approaches across various domain shifts.

---


### 476. [HOSE: Hierarchical Orthogonal Subspace Erasure for Concept Unlearning in Diffusion Models](https://arxiv.org/abs/2611.30592)

**<font color=#1a73e8>作者：</font>** Xiaoqi Wei, Li Li, Kejiang Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models can generate harmful or sensitive content, such as pornographic or violent imagery, raising serious security concerns. Model editing has recently emerged as an efficient approach to mitigate this issue. It modifies pretrained models with minimal parameter updates to alter specific concepts while preserving overall model capabilities. However, due to the entangled representations of different concepts in diffusion models, direct modifications inevitably disrupt non-target concepts. Meanwhile, U-Net's hierarchical heterogeneity hinders unified strategies from balancing erasure and quality. To address these issues, we propose Hierarchical Orthogonal Subspace Erasure (HOSE). This method projects parameter updates into the subspace orthogonal to general knowledge, thereby eliminating interference with non-target concepts. Considering the hierarchical heterogeneity of the U-Net architecture, we further propose a hierarchical adaptive mechanism, constructing differentiated subspace projections for different layers to precisely adapt to the model's hierarchical structure, thereby resolving the inherent trade-off between erasure and image quality in unified constraints. Experimental results demonstrate the proposed method reduces harmful content generation by 80% compared with the unedited model. While it inevitably incurs some image quality degradation, it still outperforms other editing-based baselines in terms of quality preservation, and achieves a significantly better trade-off between harmful content suppression and quality loss than these baselines. Notably, our approach demonstrates higher adversarial robustness than existing SOTA method, indicating that the target concepts have been more thoroughly erased. The source code is publicly available at this https URL.

---


### 477. [Advancements in Diabetic Retinopathy Classification Using Novel Multi-Stacked U-Net Architectures](https://arxiv.org/abs/2611.30593)

**<font color=#1a73e8>作者：</font>** Ameya Uppina, S Navaneetha Krishnan, Talluri Krishna Sai Teja 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diabetes leads to several health complications throughout the body, with the complication in the eyes being Diabetic Retinopathy. It leads to damaging or abnormal changes in the blood vessels' structure, causing vision loss. The need for massive screening of a large population of diabetic patients has created a necessity for computer-aided, fully automatic diagnosis of DR. CNNs have shown great promise in the classification of DR based on the Fundus images. Building a reliable model faces considerable challenges due to the limited availability of high-quality annotated datasets and issues with varying image quality and class imbalances. This paper aims to demonstrate the UNET, and its Stacked Architecture variant and their performance across several datasets. This paper has compared and studied the UNET architecture's performance across multiple stacks and has come to a soft conclusion that the architecture performs its best at three stacks, and any more leads to deterioration of its performance. The model aims at classifying the images into five categories, 0 to 4, where 0 is no DR, and 4 is proliferative DR.

---


### 478. [ViDiHand2: Unifying Video Diffusion Priors and Hand Geometry for 3D Hand Motion Reconstruction in the Wild](https://arxiv.org/abs/2611.30597)

**<font color=#1a73e8>作者：</font>** Yuxi Wang, Yufei Liu, Chengkai Jin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning robot manipulation from egocentric human videos requires accurate metric 3D hand motion. Recent methods leverage pretrained video diffusion model (VDM) priors to recover occluded hands directly from full-frame videos, but their appearance-based depth regression generalizes poorly to unseen cameras. In this work, we propose ViDiHand2, a geometry-driven framework that reformulates VDM-based hand depth estimation from direct regression into fine-grained geometric constraint solving. Specifically, we introduce Fine-Grained Geometric Lifting and Clip-Level Ray Fitting, which recover metric depth by enforcing geometric consistency between pixel-aligned 2D joints and the metric structure of MANO hands, while leveraging temporal observations across the clip. Since the lifting relies on these 2D joints, to improve robustness under occlusion and image truncation, we further develop Confidence-Gated Fusion to adaptively combine geometrically lifted joints with MANO predictions according to localization confidence. Finally, we enhance the VDM backbone to better capture spatial-temporal representations and produce the per-frame 2D joint and MANO predictions that both steps rely on. Extensive experiments on seven public datasets demonstrate that ViDiHand2 consistently outperforms 18 baselines, reducing in-the-wild absolute joint error by 42% and detection failures by 8.82x compared with the best baseline on each metric, while running at 57 FPS. The code is available at this https URL.

---


### 479. [JaxNaviSim: A GPU-Accelerated, Data-Driven Simulator and Learning Benchmark for Maritime Navigation](https://arxiv.org/abs/2611.30600)

**<font color=#1a73e8>作者：</font>** Quang Anh Pham, Janaka Chathuranga Brahmanage, Hue Tse Leong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coordinating vessels through the shared waterways of busy ports grows more challenging as vessel traffic increases. Port authorities need realistic simulations to assess how arrival schedules, anchorage assignments, and routes affect vessel throughput and navigation safety. Existing AIS-based trajectory models predict a vessel's track from its past trajectory in an open-loop fashion. They do not simulate step-by-step responses to other ships or test whether a vessel collides or reaches its goal. To address this problem, we introduce JaxNaviSim, a data-driven simulator and learning benchmark coupling Automatic Identification System (AIS) data with fast, controllable traffic simulation, in which learned models steer vessels through recorded traffic. First, we release a dataset of ~141 million AIS records from over 30K vessels across eight high-density regions of the Singapore Strait, among the world's busiest waterways, with ~6.7 million vessel-hours. Unlike several existing AIS datasets which mostly cover open seas, ours captures close-quarters vessel traffic in the narrow strait. Second, we define a navigation task for each recorded vessel trajectory. A model steers that vessel every 10 s from its recorded state to its anchoring point or region exit, while surrounding ships follow their recorded tracks or are steered by the model. We implement a JAX simulator that runs these tasks in large batches on a GPU. We also incorporate multiple vessel dynamics models and sea surface currents. Finally, we benchmark imitation learning (IL), offline and online RL, and include Predictive Action Refinement (PAR) as a safety baseline that cuts collision rates to 1-3%. The comparison shows that low tracking error does not ensure arrival, and learned policies can reach most destinations yet collide in 20-45% of episodes.

---


### 480. [Learning Multimodal Representations from Partially Paired, Small-Scale Data](https://arxiv.org/abs/2611.30601)

**<font color=#1a73e8>作者：</font>** Merel Kuijs, Till Richter, Rushin H. Gindra 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modeling multimodal data from partially paired samples is critical for advancing domains like biomedicine, where vast unimodal datasets and foundation models exist but paired data remains scarce. Existing fusion methods rely on large-scale paired datasets, limiting their use in scenarios with incomplete pairing. We introduce CAMEO, an adversarial learning-based modality fusion framework that integrates modalities from small, partially paired datasets. Combining any pre-trained unimodal encoder with a cross-modal latent alignment mechanism, CAMEO learns shared representations requiring only minimal paired samples. Evaluated on computational pathology tasks such as niche classification and cell type composition prediction, CAMEO achieves superior data efficiency, outperforming contrastive approaches like CLIP in low paired-data regimes, and highlighting the benefits of adversarial alignment when paired annotations are scarce. To facilitate further research, we additionally release a fully annotated HuggingFace dataset comprising three organs and paired image and gene expression modalities. By extending fusion methods to address limited pairing and small-scale datasets, we provide a framework that advances multimodal learning and broadens its applicability to real-world biomedical problems.

---


### 481. [GSDet: Gaussian Splatting for Oriented Object Detection](https://arxiv.org/abs/2611.30602)

**<font color=#1a73e8>作者：</font>** Zeyu Ding, Jiaqi Zhao, Yong Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Oriented object detection has advanced with the development of convolutional neural networks (CNNs) and transformers. However, modern detectors still rely on predefined object candidates, such as anchors in CNN-based methods or queries in transformer-based methods, which struggle to capture spatial information effectively. To address the limitations, we propose GSDet, a novel framework that formulates oriented object detection as Gaussian splatting. Specifically, our approach performs detection within a 3D feature space constructed from image features, where 3D Gaussians are employed to represent oriented objects. These 3D Gaussians are projected onto the image plane to form 2D Gaussians, which are then transformed into oriented boxes. Furthermore, we optimize the mean, anisotropic covariance, and confidence scores of these randomly initialized 3D Gaussians, using a decoder that incorporates 3D Gaussian sampling. Moreover, our method exhibits flexibility, enabling adaptive control and a dynamic number of Gaussians during inference. Experiments on 3 datasets indicate that GSDet achieves AP$_{50}$ gains of 0.7\% on DIOR-R, 0.3\% on DOTA-v1.0, and 0.55\% on DOTA-v1.5 when evaluated with adaptive control and outperforms mainstream detectors.

---


### 482. [Vasicek Diffusion Bridge for Graph Generation](https://arxiv.org/abs/2611.30605)

**<font color=#1a73e8>作者：</font>** Junyi Tang, Chang Liu, Kun Zhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-based graph generation models progressively transform Gaussian noise into structured graphs through stochastic dynamics. We observe that the effectiveness of this transformation is fundamentally determined by the evolution of the diffusion trajectory. Existing graph diffusion models often suffer from excessive uncertainty during diffusion and delayed growth of the signal-to-noise ratio, causing useful structural information to emerge only in the later stages of generation. To address this issue, we propose the Vasicek Graph Diffusion (VGD), a graph diffusion process derived from the Vasicek dynamics. The key insight of VGD is data-anchored mean dynamics with a closed-form solution, which analytically establishes a continuous transition from Gaussian noise to the target graph distribution. Unlike conventional graph diffusion processes that rely predominantly on stochastic evolution, VGD introduces a data-anchored drift that continuously steers the latent state toward the target distribution throughout diffusion. As a consequence, VGD maintains a smoothly evolving uncertainty while rapidly increasing the signal-to-noise ratio throughout diffusion, allowing informative graph structures to emerge much earlier during generation. Extensive experiments on multiple graph generation benchmarks demonstrate that VGD outperforms existing diffusion-based graph generative models in terms of generation quality and structural fidelity.

---


### 483. [Tri-DNO: Trilateral Diffusion Noise Optimization for 3D Human Object Interaction](https://arxiv.org/abs/2611.30607)

**<font color=#1a73e8>作者：</font>** Paul Hinzer, Niklas Gard, Anna Hilsmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating realistic 3D human object interactions (HOI) is essential for applications, such as augmented or virtual reality (AR/VR) or character animation of interactive entertainment. A particular challenge lies in the faithful generation of hand grasps in human object interaction scenes, where even minor geometric inconsistencies, such as insufficient contact or interpenetration, can significantly compromise realism. While diffusion-based generative models have shown promising results in HOI synthesis, ensuring physically plausible hand-object interactions remains challenging.
We present Tri-DNO, a diffusion noise optimization strategy to sample from a pretrained multimodal HOI diffusion model, improving hand-object contact. Rather than modifying or retraining the generative model, our approach iteratively optimizes the initial noise of the diffusion generator, thereby generating firm hand object contact, while mitigating penetration and keeping the hand position realistic. Experiments on the GRAB dataset demonstrate improvements over the baseline in grasp quality without additional model training or increased computational cost compared to existing methods. We further demonstrate the applicability of our approach to practical media production scenarios.

---


### 484. [What Environment Invariance Identifies: Minimal Invariant Sets in Reproducing Kernel Hilbert Spaces](https://arxiv.org/abs/2611.30609)

**<font color=#1a73e8>作者：</font>** Ridham Patel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Invariant causal prediction identifies the direct causes of a target $Y$ by searching for covariate sets whose conditional law of $Y$ is stable across environments. We state that criterion at the level of operators, calling a set $S$ invariant when the conditional mean embeddings of $Y$ given $X_S$ agree across environments, and characterise the resulting family exactly: under two conditions on the environments, which we state separately because they fail independently, the invariant sets are precisely those containing $PA(Y)$ and no descendant of $Y$. Two consequences follow. Invariance does not identify $PA(Y)$ uniquely, since every descendant-free superset is invariant as well; and $PA(Y)$ is the unique minimal invariant set. In finite samples, recovery requires the non-invariant sets to be separated from invariance by a margin, and the sample size splits into a screening term logarithmic in the ambient dimension and a term inherited from conditional mean embedding estimation, which is the binding one. The characterisation yields two selection rules with different failure modes, of which the conservative one controls false positives. Controlled experiments verify each population prediction directly, including the failure of uniqueness. They also show that invariance testing is a practical bottleneck: two natural designs are severely miscalibrated, while the selected test reduces but does not eliminate Type I error inflation.

---


### 485. [Bug Bounty Programs in the AI Era: How Does Platform Anti-Spam Friction Affect Vendor Profitability?](https://arxiv.org/abs/2611.30615)

**<font color=#1a73e8>作者：</font>** Haruki Oyama, Masato Kamba, Koshi Ota  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Since 2023, bug bounty platforms have introduced participation rules, such as proof-of-concept mandates, against a flood of AI-generated low-quality submissions. The platforms set these rules, but vendors running programs on them bear the cost when a vulnerability goes unreported and gets exploited. We ask whether the rules benefit the vendors they are meant to protect. Adding to Gal-Or, Hydari, and Telang's 2024 model a vendor triage cost per report reviewed and a participation cost paid in effort by the researchers reporting vulnerabilities, we locate a threshold in an effective triage-burden parameter, which captures the vendor's processing burden per unit of aggregate search effort, with the rules lowering profit below it and raising it above. Because attackers never use the platform, the participation cost falls on researchers alone and fewer take part. Bug-finding coverage falls and breach damage rises, which costs the vendor, while its triage bill falls, which helps.

---


### 486. [Omniprediction with the Minimum Number of Linear Scores](https://arxiv.org/abs/2611.30625)

**<font color=#1a73e8>作者：</font>** MohammadHossein Bateni, Zahra Hadizadeh, MohammadTaghi Hajiaghayi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An $\varepsilon$-omnipredictor uses one forecast for an entire family of downstream losses. After postprocessing for each loss, its expected loss must be at most $\varepsilon$ above that of the best comparator for that loss. A binary single-index model (SIM) learns a norm-bounded weight vector $w$ and a nondecreasing link $\rho$. It reduces the features $x$ to one linear score $w^\top x$, then maps that score to a probability $p(x)=\rho(w^\top x)$. Hu, Tian, and Yang (STOC 2025) achieved $\varepsilon$-omniprediction for binary matching losses using $O(1/\varepsilon^2)$ SIMs and asked whether one SIM suffices. In the population model, we prove that one SIM suffices for exact omniprediction in their bounded-action setting. The result holds for any compact family of continuous nondecreasing target links.
With unrestricted actions and matching losses generated by $1/\beta$-strongly convex entropies, the SIM's link can also be $\beta$-Lipschitz. For $K$ classes and $d$-dimensional features with finite first moment, $\min\{d,K-1\}$ linear scores are necessary and sufficient in the worst case. A joint link maps these scores to class probabilities, and its Lipschitz bound $\beta$ is also sharp under the comparator's coefficient norm bound.
For bounded features and smooth entropies, we achieve $\varepsilon$-omniprediction for two or three classes using $\widetilde O(1/\varepsilon^2)$ samples at fixed confidence and regularity. This bound is independent of $d$ and tight up to logarithmic factors. For any fixed number of classes $K \ge 2$, the tight worst-case sample complexity for $\varepsilon$-omniprediction under the Dirichlet condition on the features is $\Theta_K(1/\varepsilon^2)$.

---


### 487. [Rewirable Circuits in Transformers with Loom Attention](https://arxiv.org/abs/2611.30634)

**<font color=#1a73e8>作者：</font>** Da Xiao, Qingye Meng, Shengping Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose loom attention, which allows a Transformer to dynamically rewire its circuits at every token by interweaving a head's vertical attention over the outputs of earlier heads (to obtain its query, key and value) with its horizontal attention over tokens. We instantiate vertical attention efficiently with normalized and gated linear attention over a per-token matrix memory, which stores the compressed head outputs and serves as a second residual stream. This yields LoomFormer, a dual-stream architecture that splits control and content between the vector and matrix streams. Across model sizes and training token budgets in language modeling and downstream tasks, LoomFormer matches Transformers trained with over 3x compute and recent residual-stream baselines (HC/mHC, MUDDFormer, AttnRes) trained with ~1.7-2.8x. For example, trained on the same 300B tokens with only 2% extra FLOPs, LoomPythia-2.8B achieves ~1.6x the average downstream gain of mHC-Pythia-2.8B over Pythia-2.8B, and matches (0-shot) or surpasses (5-shot) Pythia-12B. Code is available at this https URL

---


### 488. [Motion on Demand: Adaptive Optical Excitation for Event Cameras](https://arxiv.org/abs/2611.30641)

**<font color=#1a73e8>作者：</font>** Yingtao Li, Chaoran Feng, Haoran Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras respond only to brightness changes, so whether an edge is visible depends on image motion perpendicular to it---a motion that constantly shifts with camera and scene dynamics. Rotating a wedge prism in front of the lens introduces controlled image motion to reveal static or slow edges. However, a fixed rotation speed cannot adapt to changing motion conditions: when natural motion is already sufficient, additional optical excitation generates redundant events and introduces unnecessary alignment errors. Inspired by the division of labor between fast haltere feedforward and slower visual feedback in fly gaze control, we present EvGaze, an event camera system that adaptively regulates prism rotation speed. EvGaze employs a learned multimodal controller that integrates luminance, event, and inertial observations, with a fast inertial pathway that refines speed decisions between visual updates. To preserve geometric consistency during speed changes, we compensate for prism-induced image motion at individual event timestamps using measured encoder angles. On EvMotion, EvGaze recovers more edges than full-speed prism rotation with 39% fewer events. On DSEC with simulated optical modulation, it reaches 0.73 feature-tracking success (compared with 0.55 on native events and 0.67 at 180 RPM) while generating 26% fewer events than 360 RPM. Real-device experiments further demonstrate online closed-loop adaptation, reducing average event rates by 17% relative to full-speed rotation.

---


### 489. [Beyond Naming Accuracy: Template Composition and Species-Name Decisions](https://arxiv.org/abs/2611.30642)

**<font color=#1a73e8>作者：</font>** Junle li, Bochang zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language classifiers identify species by matching images to text prompts containing species names. BioCLIP2 changes its predicted species less often than BioCLIP 2.5 Huge across four photographic templates, but the ranking reverses across a bank of 80 templates. This comparison leaves open whether the reversal depends on the number of templates or their wording. We hold the count at four and compare the classifiers on every four-template subset of the 80-template bank and of a second pool of 24 reviewed photographic templates, keeping images and candidate names fixed. Huge is more consistent across the reviewed pool as a whole, yet 19.09% of its four-template subsets favor Bio-CLIP2 on iWildCam and 5.10% do so on Rare Species. We then test whether both rankings hold on 5,487 frames from previously unused iWildCam sequences. Among 4,356 subsets containing two photo and two photograph templates, simultaneous 95% intervals support lower disagreement for Huge in 1,526 subsets and for BioCLIP2 in 43. Even with the same prompt count and noun mixture, the choice of sentences can determine which classifier appears more consistent.

---


### 490. [Part-wise Certified State Estimation of Articulated Objects from Passive Stereo](https://arxiv.org/abs/2611.30646)

**<font color=#1a73e8>作者：</font>** Orion Desbonnet, Kei Higuchi, Alex Sykes 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robots in manufacturing often handle thin, hinged objects known from CAD models that change shape during the task, like folding cartons. Monitoring such tasks requires estimating the object's articulation state, its pose and the shape of any semi-deformable part. Learning-based estimators generalise across objects but lose precision while handling thin parts. Model-based fitting is precise but often needs accurate depth, a close initial estimate and a clean object mask. We present part-wise certification of an articulated object's state, estimated from passive stereo. Our estimator rivals the precision of the best model-based fitting method without using depth, a close initial estimate or a mask. We detect the corners that the CAD model defines in both stereo images and fit the articulated model to them. Geometric certificates, which we extend from rigid to articulated objects, then tell whether to trust each part, because the fit returns a state even for hidden parts. Certified estimates on unlabelled video become labels that improve sim-to-real transfer. On five of seven simulated objects, we locate the parts we certify three to five times more precisely than the strongest learned baseline on the same readings, given depth and true masks. On a real folding carton, our median corner error on the end panels is 2.1% of the carton's size, at least 40% lower than every learned baseline and also lower than a depth-based fit initialised near the true state.

---


### 491. [MTL-MHOL: Predicting Online Conversions under Delayed Feedback and Data Sparsity](https://arxiv.org/abs/2611.30648)

**<font color=#1a73e8>作者：</font>** Mario Tejera Vicente, Eva Hagen, Emma van Breukelen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes the model-agnostic Multi-Task Learning Multi-Head Online Learning (MTL-MHOL) framework for conversion rate (CVR) prediction. Existing approaches typically address key challenges in CVR prediction, such as delayed feedback and data sparsity, in isolation or lack flexibility and practical applicability. MTL-MHOL adopts a time bucketing approach to account for delayed feedback and combines it with multi-task learning of an auxiliary task to mitigate data sparsity. We evaluate the framework on proprietary datasets from a private company and on a public dataset from Criteo. MTL-MHOL matches or outperforms all benchmark models in terms of Negative Log-Likelihood (NLL) and Relative Cross Entropy (RCE), and it correctly captures temporal trends in the data using an MLP backbone, while maintaining strong performance with a DeepFM backbone. In particular, MTL-MHOL matches the performance of the advanced delayed-feedback method FSIW, outperforms the entire-space approach ESMM by 21.5% in RCE, and achieves up to 81% lift in RCE compared to the best-performing classical benchmark.

---


### 492. [Zhengrong: World Models with Pole-Based Action-Response Factorization for Direct Visual Planning](https://arxiv.org/abs/2611.30666)

**<font color=#1a73e8>作者：</font>** Yu Zhang, Jingrui Li, Congyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Direct visual world models predict the effects of candidate action sequences without recursive latent rollout, yet they leave the temporal structure of action effects unspecified. We introduce Zhengrong (Zhengrong-PoleWM), a world model that decomposes a latent trajectory into an initial-condition anchor, a free response, and delayed responses to action innovations. Nonlinear networks map visual history and causal action prefixes to response coefficients. A shared bank of stable conjugate poles determines how each response evolves with elapsed time. This factorization preserves nonlinear interactions across actions, anchors predictions exactly at the initial state, prevents future actions from affecting earlier predictions, and yields bounded responses to finite control plans. We derive an exact re-anchoring identity that identifies the additional basis direction $\Psi_\kappa(s)$ needed to represent shifted trajectory tails. Across four offline image-goal control benchmarks (Cube, TwoRoom, PushT, and Reacher), Zhengrong-PoleWM achieves $90.83\% \pm 0.47\%$ macro-average success over two training seeds at epoch 20, exceeding the strongest baseline (QQWorld) by 6.08 percentage points. Selecting checkpoints by validation loss yields $91.21\% \pm 1.00\%$. In a controlled first-epoch Cube study without restart regularization, neural and pole response heads outperform a generic direct predictor by 20.67 and 23.34 percentage points, respectively. On an NVIDIA A100 GPU, median latency for a full 30-iteration cross-entropy method search ranges from 74 to 87 ms across the four tasks. The mean of these medians is 77.5 ms, a 15.8% latency reduction relative to Fast-LeWM and a $7.1\times$ speedup over autoregressive LeWM.

---


### 493. [Beyond the Black Box: A Diagnosis-Driven Agent for Interpretable MIP Solver Tuning](https://arxiv.org/abs/2611.30670)

**<font color=#1a73e8>作者：</font>** Yidong Luo, Weihuang Wen, Xuanhao Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tuning a mixed-integer programming (MIP) solver is an instance-specific problem, where a poor configuration can increase solving time by orders of magnitude.
Existing Bayesian optimization tuners treat solver tuning as a black-box optimization problem: each evaluation returns a single score, allowing the tuner to learn which configuration is faster, but not why.
Inspired by the use of profilers in GPU-kernel optimization, we introduce APEC (Agent for Per-instance Explainable Configuration), a log-grounded tuning agent for MIP solvers.
APEC has three layers: a deterministic layer that profiles each log, an interpretation layer that guides hypothesis-driven diagnosis, and a system layer that controls evaluation, enabling more reliable and interpretable solver tuning.
On the full MIPLIB 2017 benchmark set, APEC achieves a 1.58X improvement over the default configuration with over 38% fewer parameter changes than the baselines, making the results easier to read.

---


### 494. [How Many Parameters Does Forecasting Need? A Survey and Code-Level Audit of Lightweight Long-Term Time Series Forecasting](https://arxiv.org/abs/2611.30685)

**<font color=#1a73e8>作者：</font>** Issam Ait Yahia, Abdelkader El Mahdaouy, Ismail Berrada  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term time series forecasting supports decisions in energy, transportation, weather and finance, where forecasts are produced continuously and often on constrained hardware. Recent work has moved in two directions. One scales Transformers and pre-trained foundation models to millions or hundreds of millions of parameters. The other shows that models with only hundreds to tens of thousands of parameters remain competitive on the standard benchmarks. Existing surveys organize forecasting models by backbone and treat efficiency as a side topic, so the reasons these small models work, and the way their sizes are reported, remain unexamined. This survey focuses on lightweight long-term forecasting. It provides a taxonomy of about thirty-five models in six families, with a common notation and an architecture diagram for each core model. It offers a structured-linear view in which the smallest models are linear maps restricted by frequency truncation or period folding, and it tests each restriction in closed form on eight benchmarks. It complements the literature review with an audit of sixteen official code repositories, which reproduces published parameter counts and reveals reporting gaps of up to 289 times. Finally, it gives practical guidance on model selection and reporting, and summarizes open problems.

---


### 495. [Synthetic Twins: Closing the Gap Between TTS Test Sets and Real Recordings in Turkish ASR Evaluation](https://arxiv.org/abs/2611.30694)

**<font color=#1a73e8>作者：</font>** Nur Yağmur Tuncer, Mustafa Sertaç Türkel, Fatma Nur Korkmaz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech synthesized by text-to-speech engines is a low-cost substitute for recorded test sets in automatic speech recognition, yet an off-the-shelf synthetic test set is worth only a few dozen real recordings for estimating the real error rate of a recognizer. This paper examines which properties of real recordings are missing from synthetic speech and how much of the gap can be closed. For 507 Turkish Common Voice recordings, synthetic twins are built: a ladder of synthetic copies that adds, one factor at a time, the pitch of the speaker, a clone of the same speaker, the real recording channel and the speaking rate. At each step, the agreement between ASR behaviour on the copy and on the real recording is measured. Across three zero-shot cloning engines and panels of six and 19 recognizers, the speaker clone is the step that improves agreement on which sentences are hard, raising the Spearman correlation from .41 to .55 for Chatterbox. Matching the channel or adding generic noise corrects the error level when the synthetic speech is easier than real speech. The twin with the highest worth is equivalent to 70 to 122 real recordings, depending on the recognizer panel, compared with about 9 for a stock voice. The findings replicate on VoxForge, a second corpus in which speaker identity is known rather than inferred: the clone raises sentence agreement from .31 to .50 and the worth from 8 to about 50 recordings. Agreement on which sentences are hard is distinct from agreement on how hard they are. The paper concludes with a practical recipe and a reporting checklist for synthetic ASR test sets.

---


### 496. [Speculate in the Right Order: Efficient Self-Speculative Decoding for Autoregressive Image Generation](https://arxiv.org/abs/2611.30704)

**<font color=#1a73e8>作者：</font>** Yihan Chen, Jintao Zhang, Jun Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-speculative decoding accelerates autoregressive image generation by leveraging the same model for parallel drafting and sequential verification, without requiring an additional draft model. While existing methods primarily focus on improving drafting and verification strategies, recent advances in random-order autoregressive modeling introduce an additional degree of freedom: the generation order. In this work, we theoretically analyze how generation order affects self-speculative decoding efficiency, identifying two key factors: draft-target mismatch, which determines token rejection probabilities, and early-rejection cost, which reflects the higher cost of rejecting tokens earlier in a speculative round. Motivated by these insights, we propose Speculation-Aware Ordering (SAO), a training-free framework for offline optimization of generation orders. Instead of evaluating candidate orders through costly speculative decoding, SAO uses simple pairwise conditional-TV statistics to formulate a rejection-cost-aware objective and efficiently construct speculation-friendly generation orders offline. Extensive experiments across different backbones and speculative widths demonstrate that SAO improves decoding efficiency, with the additional benefit of improved generation quality. Furthermore, SAO provides complementary efficiency gains when combined with existing self-speculative decoding methods. To the best of our knowledge, this is the first work to identify generation order as a new optimization dimension for efficient self-speculative decoding in autoregressive image generation.

---


### 497. [Intra-Class Diversity Loss for Person Re-Identification](https://arxiv.org/abs/2611.30707)

**<font color=#1a73e8>作者：</font>** Wei Zhou, BaXian Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Person re-identification (ReID) aims to retrieve images of the same pedestrian across different cameras. However, the non-overlapping identities between training and testing sets, together with large intra-class variation, make it challenging to learn generalizable pedestrian representations. Most existing ReID loss functions mainly focus on intra-class compactness and inter-class separation, which may overlook useful intra-class differences. To address these issues, we propose a novel Intra-Class Diversity (ICD) loss that aims to maximize intra-class differences in classification-irrelevant directions. To the best of our knowledge, we are the first to introduce this class-weight-orthogonal diversity learning objective for person ReID. Specifically, based on the geometric relationship between the learned representation and its corresponding class-weight vector, we decompose each representation into the component along the class-weight direction and its orthogonal component. This decomposition provides a clear and interpretable geometric basis for modeling intra-class diversity. ICD then encour- ages larger differences among the orthogonal components of samples belonging to the same identity, while the classification loss maintains identity discrimination. The proposed ICD loss can be incorporated into existing ReID frameworks as an additional regularization term without modifying the feature extraction network. Extensive experiments on three widely used ReID datasets demonstrate the effectiveness of ICD and its complementarity with existing metric learning losses.

---


### 498. [Co-speech Gesture Attribute Annotation with 3D Human Mesh Recovery](https://arxiv.org/abs/2611.30725)

**<font color=#1a73e8>作者：</font>** Frances Yung, Muhammad Naufilr  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Co-speech gestures convey meaning alongside speech, but annotating their physical attributes in video is labour-intensive. We propose two approaches to automate annotation of ten gesture attributes using human mesh recovery (HMR), which estimates a full 3D body skeleton from a single video frame: AI-assisted geometrical rules and a graph convolutional network (SL-GCN). Both use pose estimates from SAM 3D Body, evaluated on 2,020 gestures from the GESRes dataset. For physically defined attributes such as height, arm swivel and movement speed, both methods achieve agreement with expert annotation comparable to that between human annotators. For attributes whose annotation requires higher-level multimodal contextual inference, performance remains lower. The rule-based approach requires substantially less annotated data, is fully transparent, and can be adapted to different annotation schemes, offering a practical and interpretable complement to data-driven methods

---


### 499. [Same Seed, Different Picture? Deciding Early at Low Resolution for Seed-Faithful Few-Step Flow Sampling](https://arxiv.org/abs/2611.30728)

**<font color=#1a73e8>作者：</font>** Huiran Duan, Weilun Feng, Yuqi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step samplers make large text-to-image flow models fast, but from the same noise they no longer generate the image of the standard 50-step sampler. Subjects, attributes and layout change, not just fine detail. We trace this loss of seed fidelity to the start of sampling. The coarse part of the initial noise decides coarse structure first, while the noise level is still above 0.9. Few-step samplers cross this range in their first steps, which account for 25-52% of their distance to the 50-step reference. Because this decision is coarse, a half-resolution run from the same coarse noise can make nearly the same decision at a third of the cost. We therefore propose Decide-then-Render (DtR), a training-free sampler that decides the composition in a few low-resolution steps, rebuilds the full-resolution state with the seed's own noise and renders the details. On 4 large models, DtR runs 11-25$\times$ faster than the reference sampler. At each speed-up, it is closer to the reference and rated higher by ImageReward than every compared sampler, including few-step schedules calibrated per budget and published multi-resolution samplers. On FLUX.1-dev, it remains the most faithful sampler down to about $8\times$, ahead of caching accelerators. A user study on this model found DtR's samples closer to the reference in 86% of pairwise trials. DtR transfers to a held-out model and to video, and distilled models can serve as its renderers. Project link: this https URL

---


### 500. [Complying with Cybersecurity Legislation: NIS2 Challenges and Industry Case Study](https://arxiv.org/abs/2611.30732)

**<font color=#1a73e8>作者：</font>** Ricardo Galvão, Miguel Coelho, João R. Campos  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Given the ever-increasing dependency on interconnected digital systems, cybersecurity has become a major concern. To protect markets and societies, governmental entities are developing legislation to enhance cyber resilience across sectors, introducing new technical and legal requirements. The NIS2 Directive, a revised version of the European-wide cybersecurity legislation, entered into force on 16 January 2023. Member States were required to adopt and publish transposing measures by 17 October 2024 and apply them from 18 October 2024. Specific obligations for essential and important entities are set out in national legislation. At the same time, other organizations, while not legally bound, seek to improve their cybersecurity maturity in alignment with EU-wide advances, for which NIS2 serves as a key reference. This paper presents the work conducted within a large European enterprise to align itself with the NIS2 Directive, focusing on how organizations can analyze and interpret its provisions to drive concrete technical and organizational improvements. A systematic methodology is applied to frame the company within the NIS2 context, identify relevant requirements, and derive actionable measures. Beyond outlining the technical steps taken, the work highlights the challenges of translating legislative requirements into practical implementations, emphasizing the use of existing IT resources while accounting for key legal aspects. The paper concludes with a discussion and reusable artifacts addressing critical areas such as Supply Chains and Third Parties and Zero-Trust Principles, illustrating how legislative instruments such as NIS2 can be translated into practical mechanisms to strengthen cybersecurity strategies.

---


> [!TIP]
> 当前位于：**451-500**（第 10/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-569](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
