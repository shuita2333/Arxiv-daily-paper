# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**901-908**（第 19/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | **901-908**

---

### 901. [Copy the Same, Distill the Difference: Initializing Linear Vision Transformers](https://arxiv.org/abs/2609.35745)

**<font color=#1a73e8>作者：</font>** Huaiyuan Qin, Muli Yang, Gabriel James Goenawan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Linear Vision Transformers (ViTs) are designed to replace the attention in Softmax ViTs with the linear-complexity attention operator for more efficient token routing, but they require from-scratch pre-training and typically underperform the original Softmax version. How to initialize linear ViTs both efficiently and effectively still remains unclear. In this work, we explicitly ask: given that most foundation ViTs are built on the mainstream Softmax attention, can linear ViTs benefit from their pre-trained weights? Recent works on Attention Transfer show that attention is the effective transferable component between Softmax ViTs, suggesting attention alone suffices for such reuse. However, we find the opposite for Softmax-to-linear transfer. The attention weights are operator-specific: copying them barely helps, and is sometimes even worse than random initialization. Instead, the attention's token routing behavior can be recovered through distillation with a proper loss design, letting linear ViTs reduce the gap and even match Softmax ones. In contrast, the MLP weights, which carry the learned representation, are operator-agnostic: they can be transferred by simple direct copying, which already carries most of the benefit of the pre-trained weights. Thus, copying MLPs can serve as an effective foundation for Softmax-to-linear transfer: paired with the distilled attention, linear ViTs eventually close the remaining gap and even surpass Softmax ones. These findings hold consistently across various linear ViT variants, different model sizes, and diverse datasets. We hope this study deepens the understanding of reusing pre-trained weights across attention operators: copy what stays the same and distill what differs, to recover the benefit across the Softmax-to-linear boundary.

---


### 902. [Neural Harmonic Measure Operator](https://arxiv.org/abs/2609.35752)

**<font color=#1a73e8>作者：</font>** Jinjin He, Sinan Wang, Yuchen Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Neural Harmonic Measure Operator (NHMO), a neural solver for elliptic PDE problems on variable-shape domains. The harmonic measure of a domain is the boundary probability distribution that, integrated against any boundary data, returns the Dirichlet Laplace solution. It depends only on the geometry, not on the boundary data. NHMO parameterizes the density of this measure as a transformer-based boundary kernel supervised by Walk-on-Spheres exit samples, so one trained kernel handles different boundary values on a shape with no retraining. We extend it to Poisson via a classical decomposition, with an auxiliary network amortizing the source-induced correction and avoiding the singular volume quadrature that breaks direct evaluation. At inference, new boundary values and new sources both yield PDE solutions by re-integration against the fitted kernel and lift, with no retraining. NHMO improves over four prior baselines on the MCB-B 3D variable-shape Poisson benchmark across all five categories, and is competitive with major neural-operator baselines on a controlled 2D testbed.

---


### 903. [Unifying Distributional Training for One-Step Visual Generation](https://arxiv.org/abs/2609.35763)

**<font color=#1a73e8>作者：</font>** Chi Zhang, Haoyang Shi, Yueyi Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> \emph{Distributional training} provides collective supervision for one-step visual generation by matching real and generated features in frozen representation spaces. We introduce \emph{a unified theoretical framework} that separates distribution modeling from matching discrepancy and connects global objectives to pointwise feature updates through Wasserstein gradient flow. Under this framework, FD-Loss and Gaussian-kernel Drifting are recovered through Gaussian optimal transport and kernel-density-based KL matching, respectively. The framework motivates \textbf{MGFlow}, which models feature distributions with Gaussian mixtures at an adjustable granularity between global moments and sample-based representations. MGFlow supports both optimal transport and score-based matching, and couples mass-constrained sample assignment with paired component updates to address mode collapse that mixture expressivity alone does not resolve. On ImageNet $256\times256$, MGFlow substantially surpasses the FD-Loss baseline, achieving state-of-the-art results with \textbf{1.45} $\mathrm{FDr}^6$ on pMF-H and \textbf{1.64} on JiT-H. For text-to-image generation, MGFlow post-trains FLUX.2 [klein] 4B into a one-step generator that outperforms the original four-step model on both GenEval and PickScore. Project page: this https URL

---


### 904. [Reliability-Gated Fusion of Consumer Head and Foot IMUs for Lower-Body 3D Pose](https://arxiv.org/abs/2609.35764)

**<font color=#1a73e8>作者：</font>** Zhilin Guo, Boqiao Zhang, Oszkár Urbán 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse inertial pose estimation promises camera-free motion capture from consumer devices, but consumer sensors are unreliable: firmware-fused orientations are biased, mounting varies between sessions, and streams drift or drop out. On a new 35-take single-subject benchmark pairing an earbud head inertial measurement unit (IMU) with two smart-insole foot IMUs (SAM-3D-Body pseudo-ground-truth labels), we show the reliability problem is channel-level: a channel ablation isolates foot acceleration as the most informative input (66.6 mm vs. 79.0 mm head-only) and the firmware-fused foot orientation as the liability that destroys the gain. We therefore let the model learn how much to trust each channel of each stream: one temporal gate per stream per channel block, trained with an auxiliary reliability objective on synthetically corrupted pretraining data. The channel-gated model is the most accurate of our learned fusion arms on clean data (69.4 mm vs. 83.7 static, 86.6 ungated) and under every simulated fault (bias in training; drift, dropout eval-only); its gates suppress the natively biased foot-orientation channels on clean real data without test-time supervision and flag dropout bursts at 0.92-0.999 AUROC. Two contrasts: dropping a channel known a priori to fail is flat across foot faults but collapses when an unanticipated stream fails (head dropout: 92.9 vs. 79.3 mm); and a fine-tuned HMD-Poser is more accurate on clean data (64.4 mm) and nominally under drift, with no significant paired difference under bias or dropout, but a larger worst-case degradation from clean (+16.1 vs. +3.5 mm, single seed). Learning to gate reliability instead of sensor count is the lever for deployable sparse inertial capture. Code is available at this https URL.

---


### 905. [Retrieving Biblical Intertextual References in Karen Blixen's Seven Gothic Tales](https://arxiv.org/abs/2609.35765)

**<font color=#1a73e8>作者：</font>** András Kovács, Alexander Conroy, Daniel Hershcovich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Identifying intertextual references is central to literary scholarship, but computationally difficult when source material is transformed through paraphrase, allusion, historical language, and translation. We investigate this problem through biblical intertextuality in Karen Blixen's Seven Gothic Tales. Drawing on the commentary to a critical edition, we construct a benchmark of 189 annotated references and evaluate retrieval against all 31,170 verses of historically plausible Danish Old and New Testament translations. We compare TF-IDF and BM25 with multilingual and Danish sentence encoders, examine the effect of linguistic normalization, and fine-tune a Danish encoder using hard negatives and five-fold cross-validation. We analyze performance across automatically derived lexical-overlap strata representing quotations, paraphrases, and allusions. Linguistically normalized BM25 provides a strong zero-shot baseline, attaining an overall R@10 of 0.365 and retrieving every quotation within its ten highest-ranked verses. The best zero-shot dense model achieves a comparable overall score of 0.360 while performing better on allusions. Fine-tuning DFM-large raises its overall R@10 from 0.265 to 0.508 and more than doubles its performance on allusions, from 0.138 to 0.339. However, evaluation against editorial annotations alone understates the model's scholarly usefulness: a literary scholar judged seven of 30 selected rank-one predictions counted as false positives to be meaningful additional references. These findings show both the potential and the epistemic limits of computational intertextual retrieval. Rather than treating scholarly annotations as exhaustive or model outputs as discoveries, we propose retrieval models as heuristic co-readers that recover documented references and generate candidates for expert-led close reading.

---


### 906. [Learning Native Reflection in Unified Models with Interleaved Reinforcement Learning](https://arxiv.org/abs/2609.35767)

**<font color=#1a73e8>作者：</font>** Yijia Fan, Ziqi Huang, Zhongang Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models can both look at and render images, so in principle they can repair their own generations: diagnose what an image gets wrong, revise it, observe the result, and diagnose again. Whether a revision helps is known only after it is rendered, so the reflection text and the image generation must be learned jointly, over the whole loop. Supervised fine-tuning (SFT) on reflection trajectories gives a cold start but does not find the high-success repair paths, and naive RL that optimizes only the renderer or only one head leaves most of the gain untapped. We introduce UMM-Reflection, which applies reinforcement learning (RL) to complete reflection trajectories inside one unified model: sibling trajectories share one initial image, so the group-relative advantage compares reflection strategies, and one trajectory-level advantage updates both the reflection tokens and the flow-based revisions, avoiding the combinatorial blow-up of per-round credit assignment. Unlike single-round editing or pipelines with an external critic, credit flows across rounds and to both roles of the same model, and no verifier is needed at inference. On BAGEL, UMM-Reflection improves GenEval by 12.05 points over SFT, and the gains transfer to WISE (+10.97), OneIG-Bench (+3.48), and T2I-CompBench++ (+4.63), none of which is used in training.

---


### 907. [PDMD: Projected Distribution Matching Distillation for Video Diffusion Models](https://arxiv.org/abs/2609.35768)

**<font color=#1a73e8>作者：</font>** Zimo Wang, Junkun Yuan, Angtian Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video diffusion models require tens of denoising evaluations over long spatiotemporal token sequences. Distribution Matching Distillation (DMD) reduces the number of function evaluations (NFE) to just a few. However, DMD samples can degrade during training, exhibiting progressive oversaturation and artifacts. We trace this instability to critic errors, which enter successive student updates and accumulate over time. We introduce Projected Distribution Matching Distillation (PDMD) to filter critic errors. PDMD projects out the component of the DMD update parallel to the student-critic endpoint residual. At a fixed noisy query, we prove that this residual is an unbiased estimate of the critic's endpoint error. Under high-dimensional assumptions, this projection removes a constant fraction of critic error while discarding only a vanishing fraction of ideal DMD signal. Empirically, the projection stabilizes training and improves sample quality where DMD degrades and develops unnatural textures. PDMD requires only a one-line code change to DMD, with no extra loss, network, data, model pass, or multi-stage training. With Wan2.1, PDMD achieves a VBench total score of 83.73 at 4 NFE, surpassing matched DMD by 1.03 points. On MiniMax-H3 joint video-audio generation, PDMD achieves a VideoGen-Eval visual total score of 83.17, 0.41 points above the strongest distilled baseline. PDMD also achieves the best performance on all six audio metrics among the compared 4-NFE models. Qualitative comparisons and user studies favor PDMD over the distilled baselines in visual quality, motion, and audio quality. Code and models are available at this https URL.

---


### 908. [FurE: Efficient Instance-Specific 3D Fur Reconstruction without Animal-Fur Datasets](https://arxiv.org/abs/2609.35770)

**<font color=#1a73e8>作者：</font>** Srinjay Sarkar, Prakhar Kaushik, Soumava Paul 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Realistic and editable animal fur reconstruction from multi-view images is challenging due to fine-scale detail, self-occlusion and obfuscation, and, unlike human hair, the lack of animal-fur datasets. Fur usually covers most of an animal's body, with large inter-species and intra-species variability. We present FurE, an efficient strand-based animal fur reconstruction method that recovers a per-strand, editable groom by optimizing a root-conditioned latent field, decoded into strand geometry via a PCA-based decoder. We reconstruct a defurred animal body using local fur-thickness cues from a surface-constrained Gaussian Frosting representation together with part-based priors. We further show that a PCA-based decoder learned from human-hair strand data can alleviate animal-data scarcity while enabling substantially faster optimization. FurE achieves a 10x speedup in strand training over current SOTA dense per-strand optimization while retaining strand fidelity and generalizing across synthetic and real-world sequences, with quantitative and qualitative validation despite the reduction in training time.

---


> [!TIP]
> 当前位于：**901-908**（第 19/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | **901-908**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
