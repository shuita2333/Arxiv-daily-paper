# 📦 其他研究 | 2026年08月18日

> 本类共 **165** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-165**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-165**

---

### 151. [Style or Signature? Artist-Disjoint Evaluation of Style Classification in Frozen Vision Embeddings](https://arxiv.org/abs/2608.14435)

**<font color=#1a73e8>作者：</font>** Rory Ashton  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen image embeddings from models such as CLIP are increasingly used to classify paintings by art-historical style, with high reported accuracy. We ask whether this accuracy reflects an understanding of style or the recognition of individual artists. Standard evaluation uses random splits in which works by the same artist appear on both sides, so a classifier can succeed by recognising the painter rather than the movement. We re-evaluate style classification under an artist-disjoint protocol, holding out every artist in turn so that no work is ever classified using other works by its own painter. On a balanced dataset of 320 paintings across four twentieth-century movements, 5-NN style accuracy falls from 0.87 to 0.77 under this protocol, and the drop is sharply uneven. Impressionism and Cubism barely move, while Surrealism falls twenty points. The pattern holds across four image encoders, including a vision-only self-supervised model, which places the effect in visual structure rather than language. Where an encoder captures genuine shared form, individual artists are barely recognisable yet style is robust, while Surrealism shows the opposite. We argue that artist-disjoint evaluation is necessary to measure stylistic understanding in frozen embeddings.

---


### 152. [Designing Compact Neural Architectures via Neuron Gating and Mixed Activation](https://arxiv.org/abs/2608.14443)

**<font color=#1a73e8>作者：</font>** Abhishek Shukla, Ankur Sinha, Faiz Hamid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Architecture Search (NAS) is naturally formulated as a bilevel optimization problem, where the upper-level optimizes the architecture using validation performance and the lower-level trains network parameters using training loss. However, NAS is computationally expensive due to discrete architectural decisions, exponentially growing search spaces, and the high cost of training candidate architectures. This work develops a general bilevel optimization framework for NAS across diverse architectures, including MLPs, CNNs, RNNs, and Transformers, to identify compact architectures with strong predictive performance. We propose three scalable formulations that replace discrete neuron- and activation-level decisions with continuous relaxations, enabling differentiable optimization over otherwise combinatorial architecture spaces. These formulations give rise to three NAS methods: NAS based on Neuron Gating (NAS-NG), NAS based on Mixed Activation (NAS-MA), and NAS based on Neuron Gating and Mixed Activation (NAS-NGMA). Experiments on MLPs and CNNs using MNIST and CIFAR-10 show that the proposed methods consistently identify compact architectures with competitive or improved predictive performance. On MNIST, NAS-NGMA achieves 98.68% test accuracy with 7.69M MLP parameters, while NAS-NG achieves 99.63% accuracy with only 0.26M CNN parameters. On CIFAR-10, the proposed methods consistently outperform vanilla DARTS. Further experiments demonstrate that NAS-NG can optimize substantially over-parameterized and literature-optimal architectures, improving accuracy while reducing parameters. These results establish relaxed bilevel optimization as a scalable alternative to discrete NAS and provide a general framework for efficient neuron- and activation-level architecture optimization.

---


### 153. [Wyvern: An Agentic Framework for Generating Grounded Multimodal Reports](https://arxiv.org/abs/2608.14446)

**<font color=#1a73e8>作者：</font>** Beatrice Alessandra Motetti, Emilien Guandalino, Daniele Jahier Pagliari 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the current artificial intelligence-driven innovation era, the pace of knowledge growth is accelerating, and is hard to keep up with. While generative models are increasingly used to synthesize content, they often lack in information grounding. To address these peculiarities of our time, we propose Wyvern, a multi-agent framework for the automated generation of grounded, multimodal technical reports. Wyvern allows for the generation of multimodal outputs, integrating images, tables, and text with supporting references in a unified report. Additionally, a particular focus is placed on the grounding of the content, with the implementation of a claims auto-revision stage. We conduct a human evaluation study to assess the quality of our proposed framework. The results show that the figures' informativeness is perceived as superior to that of a recent baseline in 87% of cases. Furthermore, Wyvern's reports are rated as more useful than those produced by three alternative methods in 63% to 100% of instances. We also carry out automatic evaluations showing that Wyvern gains up to 2.3$\times$ in citation recall and 1.6$\times$ in citation precision with respect to the baselines.

---


### 154. [Shift Aware Transfer Learning with Adaptive Dual-Encoder Fusion for PM Forecasting in Data-Limited Environments](https://arxiv.org/abs/2608.14456)

**<font color=#1a73e8>作者：</font>** Shahab Band, Hamed Mohammadi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Short-horizon forecasting of fine particulate matter (PM2.5) remains difficult when observations from the target domain are limited and the statistical properties of the source and target domains differ. In these settings, models trained only on local data may not capture complex temporal dynamics, while direct transfer learning can result in negative transfer. This study develops a shift-aware dual-encoder transfer framework that combines source-domain knowledge with target-specific representation learning. The source encoder was pretrained using hourly observations from 10 U.S. monitoring locations. The framework was then adapted and evaluated using two years of hourly observations from 77 stations in Taiwan under a chronological train-validation-test protocol. Among the four principal baselines, the frozen-source dual-encoder model achieved the best performance, with MSE = 21.8960, MAE = 3.1597, and R^2 = 0.8725. This corresponds to an MSE reduction of approximately 7.1% relative to TL-v1 and 4.1% relative to TL-v2. The ablation analysis showed that removing the Taiwan-specific branch caused the largest decline in performance. Allowing the source encoder to adapt produced the best overall result, with MSE = 21.6575, MAE = 3.1383, and R^2 = 0.8739. SHAP analysis indicated that predictions were driven mainly by recent PM2.5 observations and meteorological variables related to pollutant transport and dispersion. These results suggest that source-domain knowledge is most effective when target-specific information is preserved and the transferred representation is allowed to adapt under target supervision.

---


### 155. [LP-NAS: Linear Programming-based Neural Architecture Search](https://arxiv.org/abs/2608.14472)

**<font color=#1a73e8>作者：</font>** Abhishek Shukla, Ankur Sinha, Faiz Hamid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Architecture Search (NAS) aims to automate neural network architecture design, reducing reliance on human expertise. Among the various NAS methods, differentiable NAS has gained prominence due to its efficiency and accuracy compared to conventional NAS approaches. Since differentiable NAS relaxes the architecture search space into a continuous domain, it is possible to apply principles from continuous optimization to NAS. In this paper, we propose Linear Programming-based NAS (LP-NAS), a mathematical programming-based framework for differentiable NAS that is applicable to a wide range of continuous search spaces. LP-NAS formulates a linear program (LP) using the validation-loss gradient and the training-loss Hessian to compute an architecture update direction that improves generalization while preserving the optimality of the model parameters. By following this LP-derived descent direction, LP-NAS efficiently navigates the architecture search space, leading to faster and more effective architecture optimization. We introduce two computationally efficient variants of LP-NAS, namely S-LP-NAS and R-LP-NAS. Applying LP-NAS to the Differentiable Architecture Search (DARTS) search space results in two algorithmic variants, S-LP-DARTS and R-LP-DARTS. Both variants achieve faster convergence and significantly higher validation performance during the early search iterations than the standard DARTS algorithm. Extensive experiments on CIFAR-10 and CIFAR-100 show that LP-DARTS outperforms standard DARTS in both the architecture search and evaluation phases. Additionally, we compare our approach with several DARTS variants (P-DARTS, PC-DARTS, and STO-DARTS) on the CIFAR-10 dataset and demonstrate its effectiveness. Furthermore, we validate the transferability of the discovered architectures through experiments on the ImageNet dataset.

---


### 156. [Approximate Muon with low-rank adapters](https://arxiv.org/abs/2608.14492)

**<font color=#1a73e8>作者：</font>** Ben Anson, Conor Houghton, Edward Milsom  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Muon optimizer shows clear benefits versus alternatives when pretraining neural networks. However, it is used less frequently for parameter-efficient fine-tuning (PEFT). One potential reason is that the most common PEFT method, LoRA, does not naturally combine with Muon since it is not mathematically possible to orthogonalize the weight update given by a low-rank parameterization. In this paper, we address this issue by approximating the solution to a relaxed Muon objective in the low-rank setting via linearization and then least-squares. We provide an efficient implementation that uses matmul operations only, as opposed to more complex linear algebra decomposition routines. Our method, sMuon (small Muon), performs favourably across SFT and a ReLoRA pretraining experiment. While results are model- and eval-dependent, we find overall that using Muon for low-rank fine-tuning provides moderate performance improvements.

---


### 157. [Generating Benchmark Health Data Using a Tabular Diffusion Transformer](https://arxiv.org/abs/2608.14496)

**<font color=#1a73e8>作者：</font>** Hao Yan, Lisa Pilgram, Dan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-Tabular Data Generation (CTDG) seeks to learn a generative model from multiple heterogeneous tables and produce new synthetic tabular datasets. However, existing synthetic tabular data generation methods are largely restricted to single-input-table scenarios and struggle to effectively handle multiple heterogeneous tables with diverse feature sets. To address this limitation, we propose a two-stage framework for cross-tabular data generation. In the first stage, each heterogeneous raw table is transformed into a standardized statistical table with the same set of columns across all tables. Each statistical table captures the marginal distributions of the original columns and the pairwise correlations among them. In the second stage, a diffusion transformer model is trained to capture structural patterns across these homogeneous statistical tables and to generate synthetic statistical tables. Synthetic raw tables are subsequently reconstructed from the generated statistical tables via multivariate Gaussian sampling followed by an inverse probability integral transform. This two-stage CTDG framework enables the learning of a unified generative model from multiple heterogeneous tables and supports the generation of an unlimited number of realistic synthetic heterogeneous tables. Experimental results demonstrate high fidelity in the learned statistical representations and a favorable fidelity-diversity trade-off in the generated synthetic data, validating the effectiveness of the proposed approach.

---


### 158. [Lower Bounds on Black-Box Constructions of Pseudorandom Functions](https://arxiv.org/abs/2608.14501)

**<font color=#1a73e8>作者：</font>** Bar Alon, Itai Dinur, Muthuramakrishnan Venkitasubramaniam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In their seminal work, Goldreich, Goldwasser, and Micali [CRYPTO 1984] constructed a pseudorandom function (PRF) using a black-box access to a pseudorandom generator (PRG). When combined with Levin's domain extension technique, the GGM construction invokes the PRG $\omega(\log n)$ times, where $n$ denotes the input length to the PRG. To this day, no black-box construction achieving fewer calls is known.
Recently, Beimel, Malkin, and Mazor [CRYPTO 2024] showed that for a certain family of constructions, which they termed \emph{tree constructions}, the GGM construction is optimal. However, the basic challenge of whether a PRF can be built with just \emph{one invocation} of the PRG still remains open.
In this work, we consider fully black-box constructions of PRFs from PRGs, where both the construction and the reduction are required to be black-box, and the number of interactions the reduction makes with the adversary is independent of the number of oracle calls the adversary makes to its underlying function within each interaction. Our main result shows that no such construction can have $o(n/\log n)$ and $o(\mathsf{in}/\log\mathsf{in})$ \emph{non-adaptive} calls to the PRG, where $\mathsf{in}$ is the input length of the PRF. This impossibility holds even for weak PRFs with one-bit output, where the adversary is restricted to making i.i.d. uniformly random queries. In addition, we prove a lower bound for weak PRFs with sufficiently long outputs that holds even when the construction is allowed to make adaptive queries to the PRG.

---


### 159. [RecipeNet: A Hierarchical Transformer for Recipe Data](https://arxiv.org/abs/2608.14505)

**<font color=#1a73e8>作者：</font>** Pin-Yen Huang, Sachin Chhabra, Prasanth Sai Gouripeddi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recipe data arises in domains such as materials synthesis, pharmaceutical formulation, and industrial manufacturing, where procedures are represented as ordered sequences of steps containing heterogeneous structured fields. Existing tabular learning methods typically flatten this structure into fixed-schema representations, limiting their ability to capture hierarchical field interactions and procedural dependencies. We propose RecipeNet, a hierarchical Transformer architecture that encodes field-level interactions within each step and sequential dependencies across steps through stacked Transformer encoders. Experiments on multiple recipe datasets and tasks demonstrate that RecipeNet consistently outperforms existing tabular models, highlighting the value of hierarchical and sequential modeling for recipe representation learning.

---


### 160. [Visualizing Uncertainty in Non-linear Projections with Ensembles](https://arxiv.org/abs/2608.14513)

**<font color=#1a73e8>作者：</font>** Kai Nylund, Michael Correll, Lace Padilla  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Widely used non-linear dimensionality reduction (NLDR) methods such as UMAP and t-SNE are stochastic--repeated runs on the same data can produce different low-dimensional projections. In this paper, we explore two problems related to projection variability: on some datasets clusters, structure, and outliers may change run-to-run, and on others projections can be extremely stable when overfitting noise. To address the first problem, we propose visualizing the median of multiple NLDR outputs rather than relying on individual projections. To address the second, we perturb input data before creating consensus embeddings. We find that taking the median of multiple projections performs comparably to individual runs on multiple quality metrics, while increasing perturbation emphasizes global over local structure. We show through a set of exploratory visualizations that even relatively simple ensemble presentations can be used to better communicate the reliability of projection patterns.

---


### 161. [Marionette: Predicting World States, Rendering Geometry, Painting Appearance](https://arxiv.org/abs/2608.14530)

**<font color=#1a73e8>作者：</font>** Zian Meng, Zhen Li, Chuanhao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive game world models typically autoregress visual observations directly in pixel or latent space, forcing structured properties such as pose, geometry, and occlusion to be implicitly maintained by the same generative sequence. Over long horizons, errors in these latent world properties accumulate, making consistency and controllability fragile. We explicitly model the evolving world state, delegate exact geometric computation to a fixed, zero-parameter renderer, and leave the neural model to synthesize appearance. We instantiate this idea as Marionette, a world model for interactive games with articulated characters. First, a two-stage autoregressive dynamics model predicts an explicit and interpretable 276-dimensional 3D world state comprising multi-entity articulated skeletons, metric root trajectories, and rotations. Second, a zero-parameter graphics bridge converts the predicted state into pose-control videos, computing world-space geometry and occlusion in closed form. Third, a control-conditioned video-diffusion observation model synthesizes photorealistic RGB observations from the resulting structured controls. Our experiments establish two properties of Marionette. First, the predicted world state is directly controllable. Forcing a mismatched action stream changes root-aligned joint error by 31% across 48 held-out segments. Second, long-horizon behaviour is determined in the state, and can be repaired there. Left free, the two generated characters drift to 21.2 m apart (recorded sessions stay near 5 m) and a third of frames show ground penetration. Two rules imposed on the explicit state, a terrain collider and a separation cap, cut penetration by 66% and keep the pair engaged, with no change to the observation model. Routing appearance through the predicted state costs no fidelity we can detect, at an FVD of 831 against 799 for recorded pose.

---


### 162. [Trust Without Boundaries: An Architectural Analysis of Satellite Flight Software](https://arxiv.org/abs/2608.14532)

**<font color=#1a73e8>作者：</font>** Jack Vanlyssel, Gruia-Catalin Roman, Kendra Cook 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As spacecraft become more software-driven and interconnected, onboard flight software is an increasingly important security boundary. Popular flight software architectures often treat onboard components as trusted peers, simplifying integration while limiting internal isolation and access control. We analyze NASA's Core Flight Software (cFS) to examine how authority, identity, communication, observability, and persistence are distributed across onboard components. Using NASA's flight-representative NOS3 simulator, we validate these weaknesses through five experiments implemented with a malicious onboard component that abuses legitimate architectural privileges. We then compare cFS with other modular flight software frameworks to identify recurring trust assumptions and architectural weaknesses. Our results show that a single compromised component can exploit broadly shared authority in ways that are difficult to distinguish from legitimate behavior. We conclude with architectural implications and discuss mechanisms for strengthening internal trust boundaries in future flight software systems.

---


### 163. [Decoding the Past: An Uncertainty-Aware Deep Learning Framework for Sex Attribution in Prehistoric Hand Stencils](https://arxiv.org/abs/2608.14539)

**<font color=#1a73e8>作者：</font>** Karel Becerra, Boris Mederos, Dean Snow 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Determining the biological sex of the individuals who created Upper Paleolithic hand stencils remains a challenging problem due to the absence of ground truth, population differences between contemporary and prehistoric groups, and the uncertainty introduced by image degradation. Traditional morphometric methods suffer from high structural overlap across sexes, poor cross-population generalizability, and subjective feature engineering. This study presents an uncertainty-aware deep learning framework for sex attribution in prehistoric hand stencils that explicitly models, propagates, and aggregates uncertainty throughout the analytical pipeline. The methodology combines dual image processing, dual contour extraction, structured silhouette augmentation, model architectural diversity, and ensemble-based decision aggregation. The pipeline generates twelve plausible silhouette realizations per stencil to capture boundary uncertainties, which are processed by two ensembles of ten deep neural networks each (EfficientNet-B3 and MobileViT-S) trained on 14,036 contemporary hand samples. Furthermore, a triangulated validation scheme integrates ensemble predictions with unsupervised 2D latent-space manifold mapping (UMAP + k-NN) and explainable AI spatial attributions (LayerCAM) to ensure anatomical consistency. On contemporary data, ensemble models achieve strong classification performance, with accuracies exceeding 88% in older age groups. When applied to prehistoric stencils, the framework produces both sex predictions and confidence measures of internal agreement, enabling the distinction between morphologically stable and ambiguous cases. Convergence across ensemble predictions, latent-space structure, and interpretability analyses shows that uncertainty can become a measurable component of archaeological inference, enabling robust and reproducible decoding of ancient rock art.

---


### 164. [MagnifiQ: Patch-aware Text Guided Progressive Upscaling for High-Resolution Image Restoration](https://arxiv.org/abs/2608.14543)

**<font color=#1a73e8>作者：</font>** Mahesh Reddy, Yashesh Savani, Antoine Mercier 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution image restoration from degraded inputs is challenging because it must preserve global structural consistency while recovering fine-grained local details, especially at 4K resolution where direct diffusion-based restoration is computationally expensive and prone to repeated or inconsistent textures. In this work, we introduce MagnifiQ, an image restoration framework that progressively upscales and restores images across resolutions, e.g., from 1024x1024 to 4096x4096. Our approach leverages a pre-trained text-to-image diffusion model such as SDXL and adapts it for more scalable high-resolution inference by replacing its original self-attention layers with convolutional operations whose computational cost grows linearly with image resolution. We further propose a progressive upscaling strategy that iteratively restores images over multiple resolution stages, refining each intermediate output rather than directly hallucinating the final 4K image, thereby improving global coherence and reducing high-resolution artifacts. To enhance local details while controlling content drift, MagnifiQ uses patch-specific text prompts that provide spatially localized semantic guidance during restoration. Extensive experiments on synthetic and real-world degraded images show that MagnifiQ outperforms prior diffusion-based restoration methods in perceptual quality and human preference, producing sharper textures and more coherent 4K results while offering practical speed--quality trade-offs through its scalable backbone and progressive design.

---


### 165. [CPI-Bench: A Comprehensive,Practical and Intelligent Benchmark for Real-World Image Editing](https://arxiv.org/abs/2608.14546)

**<font color=#1a73e8>作者：</font>** Qinye Zhou, Jun Zheng, Yongchao Du 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of image editing models and their widespread application across various domains, there is an increasingly urgent need to deploy these model capabilities directly into real-world scenarios. However, existing benchmarks remain confined to simple single-image tasks, suffering from limited coverage dimensions and an inability to effectively differentiate performance among diverse models. Consequently, they fail to reliably evaluate model performance in complex multi-image editing, highly demanding reasoning instructions, and practical deployment settings. To address these limitations, we propose CPI-Bench, a Comprehensive, Practical andIntelligent benchmark for real-world image editing. CPI-Bench comprises three core subsets: CPI-General-Bench, which comprehensively covers diverse editing tasks and pioneers the inclusion of multi-image editing evaluation; CPI-Practical-Bench, which focuses on high-frequency real-user application scenarios; and CPI-Intelligent-Bench, which is dedicated to evaluating capabilities in highly demanding reasoning-based editing. Evaluation results of mainstream image editing models based on CPI-Bench demonstrate that CPI-Bench enhances performance differentiation among models. It provides a comprehensive and reliable quantification of gaps in general editing capabilities, practical deployment efficacy, and advanced reasoning-based editing, offering invaluable guidance for the future optimization of image editing models. Crucially, our ranking analysis reveals that CPI-Bench achieves the highest alignment with the Arena Image Edit Leaderboard, indicating it faithfully captures the preferences and perceptual judgments of human evaluators, serving as a robust proxy for real-world user experience.

---


> [!TIP]
> 当前位于：**151-165**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-165**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
