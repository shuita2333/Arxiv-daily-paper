# 📦 其他研究 | 2026年06月03日

> 本类共 **651** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

---

### 351. [DiffuSent: Towards a Unified Diffusion Framework for Aspect-Based Sentiment Analysis](https://arxiv.org/abs/2606.01323)

**<font color=#1a73e8>作者：</font>** Shu Long, Yanglei Gan, Xuchuan Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aspect-Based Sentiment Analysis (ABSA) encompasses seven distinct subtasks, each focusing on different extracted elements. Despite the proven success of generative models in unified aspect sentiment analysis, existing approaches often rely on auto-regressive token-by-token generation without grasping the whole information of the aspect and opinion terms, resulting in boundary insensitivity, particularly in context of multi-word aspect and opinion terms. To address these issues, we present DiffuSent, a non-auto-regressive diffusion framework that systematically formulates all ABSA subtasks as boundary denoising diffusion processes, progressively refining boundaries over noisy states. Furthermore, we introduce a contrastive denoising training strategy which effectively address duplicate predictions with subtle variations introduced by diffusion process. Extensive experiments across 28 settings (7 subtasks x 4 datasets) demonstrate that DiffuSent achieves delivers consistent improvements over the strongest generative and span-based systems. DiffuSent exhibits notable gains on multi-word triplets, achieving an average improvement of +2.48 F1, and maintains robust extraction accuracy in sentences containing multiple sentiment triplets. Moreover, the non-auto-regressive decoding enables substantial efficiency benefits, reaching up to 181 times faster inference than auto-regressive generative baselines

---


### 352. [Conditioned free-energy density of proteins using unbalanced solutions to constraint satisfaction problems](https://arxiv.org/abs/2606.01329)

**<font color=#1a73e8>作者：</font>** Pratik Worah, Subhash Khot, Srinivasa Varadhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that computing the log-partition function (free-energy) of conditioned inhomogeneous Curie--Weiss spin Hamiltonians reduces to an unbalanced $2 \to 1$ norm computation, and design a polynomial-time SDP algorithm for this problem with a lower bound proof for the amount of unbalance achieved. Applied to the protein Ubiquitin, the framework starts from a known crystal structure, explores alternative backbone conformations across the free-energy landscape, and identifies flexible regions of the protein while preserving its native secondary structure.

---


### 353. [HOLA: Holistic Multi-Modal Alignment for Open-Set 3D Recognition](https://arxiv.org/abs/2606.01334)

**<font color=#1a73e8>作者：</font>** Koby Aharonov, Oren Shrout, Ayellet Tal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-set 3D recognition requires models that generalize to rare or unseen categories. Recent approaches address this by distilling language-vision knowledge into 3D encoders, typically relying on heavy 2D ViTs and aligning each point cloud with a single image or caption, thus anchoring representations to partial views. We propose aligning each point cloud with multiple images and textual descriptions to capture a more holistic understanding of 3D objects. To realize this idea, it is essential to design a loss function capable of jointly aligning a 3D instance with multiple matched signals, multi-view images and multiple texts, while separating positive aggregation from negative competition. We introduce such a function, termed the decoupled multi-positive contrastive loss. Our formulation enhances the loss's hardness-aware focus on challenging negatives, avoiding the "spotlight crowding" that occurs when many positives share the same softmax with all the negatives. Complementing this, we present a lightweight text adapter applied only to web captions, reducing the domain gap to curated annotations and enabling effective use of large-scale unsupervised text. Our model demonstrates state-of-the-art open-vocabulary performance on long-tail benchmarks, yielding substantial zero-shot improvements while sustaining high frame rates.

---


### 354. [LongAttnComp: Cross-Family Context Compression for Long-Context Reasoning](https://arxiv.org/abs/2606.01336)

**<font color=#1a73e8>作者：</font>** Mengmeng Ji, Ravi Shanker Raju, Jonathan Lingjie Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As real-world applications increasingly require processing inputs of 100k+ tokens, the gap between context length and inference efficiency has become a critical bottleneck. Context compression offers a way to reduce prefill costs while preserving task accuracy. However, existing training-free attention-based methods leave substantial gaps in demanding long-context tasks such as code reasoning. We present LongAttnComp, a long-context adaptation of AttnComp that fine-tunes a lightweight cross-attention scoring layer and introduces tokenlevel chunking, a token-budget top-p algorithm, positional reordering, and a formatagnostic query parser. We further design a two-stage fine-tuning recipe for the compressor: Stage 1 builds a general retrieval foundation from NIAH-style data, and Stage 2 extends it with multi-hop and reasoning data for broader long-context task coverage. On InfiniteBench Code-Debug, LongAttnComp matches or exceeds full-context accuracy, substantially outperforms training-free baselines, and transfers across four target models from three families. On LongBench v2, the two-stage recipe largely closes the Stage 1 gap on multi-document reasoning while preserving Code-Debug performance.

---


### 355. [FreqLite: A Lightweight Frequency-Decomposed Linear Model with Adaptive Reversible Normalization for Robust Long-Term Time-Series Forecasting](https://arxiv.org/abs/2606.01339)

**<font color=#1a73e8>作者：</font>** Mirza Samad Ahmed Baig, Syeda Anshrah Gillani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term time-series forecasting needs models that are accurate yet efficient enough for commodity hardware. Lightweight linear forecasters are remarkably strong in this regime, yet they leave two openings: reversible instance normalization (RevIN) de-normalizes the entire horizon with a single lookback statistic, which is inaccurate under non-stationarity, and time-domain trend/seasonal decomposition relies on a fixed, non-adaptive filter. We present FreqLite, an ultra-lightweight, channel-independent frequency-decomposed linear forecaster: a learnable, lossless, partition-of-unity spectral filter splits the input into bands that are forecast by per-band linear heads and, unlike low-pass-truncation approaches, the high-frequency band is retained and modeled. FreqLite is the best lightweight model on the standard long-term forecasting benchmarks and, at long lookback (L=336), attains a lower average error than a PatchTST Transformer (0.3244 vs. 0.3587 MSE) while using 4x fewer parameters, 2.2x less memory, and 2.2x less time per epoch on a single 4 GB laptop GPU; although modest in magnitude, its improvements are statistically significant under paired Wilcoxon tests across all matched cells (p < 1e-5). We further introduce Adaptive Reversible Instance Normalization (A-RevIN), a regime-adaptive reversible normalization that strictly generalizes RevIN (recovered exactly when its gate is closed), engages under non-stationarity, and reduces to RevIN without harm on stationary data. We validate this on both a real strongly non-stationary dataset (ILI, up to ~5% MSE reduction) and a controlled synthetic drift sweep in which A-RevIN's benefit and its learned gate both rise monotonically with injected non-stationarity. Every component is independently ablatable (Linear and RLinear are special cases of FreqLite), and all results are reproducible on commodity hardware.

---


### 356. [ChartArena: Benchmarking Chart Parsing across Languages, Scenarios, and Formats](https://arxiv.org/abs/2606.01348)

**<font color=#1a73e8>作者：</font>** Shangpin Peng, Gengluo Li, Xingyu Wan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Charts are a primary medium for conveying quantitative and relational information, yet systematically evaluating chart parsing models remains difficult. Existing benchmarks focus on narrow chart types and leave diagrammatic structures such as flowcharts and mind maps largely unaddressed, while models produce outputs in incompatible formats, and datasets rarely include the printed or hand-drawn images encountered in practice. To address these issues, we introduce ChartArena, a comprehensive bilingual benchmark covering eight chart families spanning both numeric charts and diagrammatic structures, each evaluated across three visual scenarios: digital renderings, printed photos, and hand-drawn photos. The dataset is built via a human-agent collaborative annotation pipeline with multi-stage human verification to ensure annotation reliability. To enable fair cross-model comparison, we further design a format-agnostic evaluation protocol that maps heterogeneous outputs into two canonical semantic spaces, a normalized triple view and a directed graph view, and scores them with structure-aware metrics. Through extensive evaluation of 26 leading MLLMs, we observe three consistent findings: (i) frontier proprietary models such as Gemini 3.1 Pro lead overall, yet the strongest open-source systems are rapidly closing the gap; (ii) document parsing models handle numeric charts reasonably but fall sharply behind on diagrammatic structures; and (iii) expert chart parsers remain limited to narrow chart families. Across all models, radar charts and hand-drawn scenarios stay especially challenging. These findings show that ChartArena exposes clear capability gaps and provides a unified foundation for future progress. ChartArena is publicly available at this https URL.

---


### 357. [FlowTime: Towards Continuous Generative Watch Time Prediction via Flow-based Personalized Priors](https://arxiv.org/abs/2606.01352)

**<font color=#1a73e8>作者：</font>** Hongxu Ma, Han Zhou, Chenghou Jin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Watch time has emerged as a pivotal metric for optimizing deep user engagement in short-video recommender systems. However, current methods of watch time prediction (WTP) suffer from inherent paradigm-specific limitations. Direct Regression faces mean-collapse due to unimodal Gaussian assumptions, while Ordinal Regression is hampered by quantization errors from rigid discretization. Similarly, Discrete Generative Regression struggles with high inference latency and heuristic vocabulary design. Beyond these specific flaws, a shared deficiency is the inability to capture the intrinsic multimodality and heterogeneity of User-Item Interaction Patterns. To address these challenges, we first revisit the WTP problem from a causal perspective and identify these user-specific patterns as structural confounders that modulate watch time outcomes, where identical interests manifest as distinct watch time outcomes conditioned on diverse user habits. Then, we formally propose a new (or the fourth) paradigm -- Continuous Generative Regression, and introduce FlowTime, a novel method utilizing a One-step Generative Variational Autoencoder. FlowTime effectively circumvents the latency of iterative denoising while maintaining the expressivity of continuous latent spaces. Furthermore, we design a Flow-based Personalized Prior that leverages NFs to warp a standard Gaussian prior into a complex, history-conditioned manifold, thereby enabling the adaptive modeling of multimodal interaction patterns. Finally, we build TimeRec, the first open-source WTP Library, alongside a novel personalization metric to establish a rigorous benchmarking standard. Extensive offline experiments and online A/B tests demonstrate FlowTime's significant superiority over SOTA methods.

---


### 358. [Diamonds in the Sky: Pareidolic Animals in Clouds](https://arxiv.org/abs/2606.01361)

**<font color=#1a73e8>作者：</font>** Miriam Horovicz, Yacov Hel-Or, Yael Moses  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> People often see animal shapes in clouds, a phenomenon known as pareidolia. We propose an AI-based method that aims to predict which animals people are likely to perceive in clouds, even though state-of-the-art recognition methods typically fail to detect such animals. Additionally, we introduce a method to assist individuals in perceiving specific pareidolic animals, even if they did not recognize them initially. Our approach uses a diffusion model to transform cloud segments into an animal shape that visually resemble the original cloud. This diffusion technique is inspired by the observation that the diffusion process succeeds only when the target animal resembles the shape of the cloud, and that subtle visual hints often suffice to help individuals recognize specific pareidolic animals. A generated image, successfully derived from the diffusion model, is then used to predict the pareidolic animal. Additionally, a short morphing video transitioning from the generated image back to the original cloud segment is employed to further enhance the human's perception of the pareidolic animals.

---


### 359. [All Models are Wrong, Knowing Where is Useful: On Model Uncertainty in Reinforcement Learning](https://arxiv.org/abs/2606.01363)

**<font color=#1a73e8>作者：</font>** Bernd Frauenknecht, Devdutt Subhasish, Artur Eisele 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement learning (MBRL) infers information about the environment from a learned dynamics model and bears the potential to address open problems such as data efficient and safe learning in robotics. However, inaccuracies of the learned dynamics model are typically exploited by the agent, substantially hampering the capabilities of MBRL methods. We present a framework for dealing with inaccuracies of probabilistic models through targeted handling of uncertainty that effectively mitigates model exploitation. We present recent successes in learning directly on hardware and safe exploration, and discuss future directions for uncertainty-aware MBRL.

---


### 360. [BRo-JEPA: Learning Modular Arithmetic in Latent Space](https://arxiv.org/abs/2606.01372)

**<font color=#1a73e8>作者：</font>** Divyansh Jha, Yuanfang Xie, Varan Mehra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can neural networks learn abstract algebraic rules, or do they merely memorize training patterns? We investigate this using MNIST digits as states and modular arithmetic operations as actions in a JEPA-style latent world model. Standard supervised baselines and JEPA models with additive operation embeddings fit seen operations but fail to extrapolate reliably to unseen ones. To bridge this gap, we introduce a block-rotation predictor that imposes the circular structure of modulo-10 arithmetic in latent space. This enables strong zero-shot generalization, with the best ResNet-based JEPA block-rotation model achieving 99.46\% zero-shot and 99.46\% rollout accuracy. Our results suggest that latent world models can learn symbolic transformation rules when architecture matches the structure of the problem. Our code can be \href{this https URL}{accessed here}.

---


### 361. [From Performance to Viability: A Bootstrap Framework for Latent-Space Representation Learning in Adaptive Biological Systems](https://arxiv.org/abs/2606.01374)

**<font color=#1a73e8>作者：</font>** Jacques Raynal, Pierre Slangen, Elsa Raynal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Observable performance is commonly used to characterize biological systems. In adaptive systems, however, similar performances may arise from distinct organizations, and configurations that appear comparable at a given time may follow different longitudinal trajectories. This limitation motivates a methodological framework for moving beyond performance-based interpretation without assuming a complete mechanistic model in advance. This article proposes a bootstrap framework for latent-space representation learning in adaptive biological systems. Here, bootstrap is used in a methodological and epistemological sense: new analytical levels are introduced when the preceding representation becomes insufficient to account for observed adaptive dynamics. The framework is organized around five levels: observable performance, dynamic organization, latent organization, longitudinal viability, and internal predictive approximation. The framework is illustrated by three previously reported gait--occlusion studies, used here only as a methodological case sequence and not as new experimental evidence. The article formalizes how performance analysis led to latent organization, how static latent organization led to longitudinal viability, and how observed viability led to internal predictive approximation. The contribution is not a new learning algorithm, clinical protocol, or dataset, but a bootstrap framework for latent-space representation learning describing how increasingly informative representations can emerge from observational insufficiencies in adaptive biological data.

---


### 362. [Turning Back Without Forgetting: Selective Backward Refinement for Parameter-Efficient Continual Learning](https://arxiv.org/abs/2606.01379)

**<font color=#1a73e8>作者：</font>** Anushka Tiwari, Kaiyi Ji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While prompt-based parameter-efficient continual learning mitigates catastrophic forgetting by isolating task-specific prompts, this isolation also limits later tasks from improving earlier ones, leaving backward knowledge transfer underexplored. We address this limitation by proposing Selective bAckward refinement for positive Backward knowledge transfER (SABER), a replay-free framework that enables controlled backward transfer in prompt-based continual learning. SABER determines when backward refinement is beneficial using complementary task-correlation criteria based on prompt-gradient geometry and loss-distribution similarity, and how to perform refinement safely by restricting updates to non-interfering directions in the prompt parameter space. Extensive experiments across multiple continual learning benchmarks and diverse pretrained backbones, including T5-Large, LLaMA, and Qwen, demonstrate that SABER consistently achieves positive backward transfer while maintaining strong overall average performance. Code is available at this https URL.

---


### 363. [Training-free image inversion for one-step diffusion models](https://arxiv.org/abs/2606.01380)

**<font color=#1a73e8>作者：</font>** Tao Wu, Senmao Li, Yaxing Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce a novel training-free inversion (TFinv) framework for one-step diffusion models,addressing key challenges in real image inversion and editing. We first identify two critical factors hamperingreal-image inversion and editing: (1) Initial Latent Editability, which is related to the distance between theinitial noise and the ideal Gaussian distribution, and (2) Caption Gap, which means the alignment betweentext captions and image representations. Both factors influence inversion efficiency and the editability ofone-step diffusion models. Then, we propose two novel techniques: iterative noise alignment (iterNA), whichminimizes the distribution gap to align with the normal Gaussian distribution, and suffix learning (suffL),which enhances text-to-image caption alignment by introducing learned suffix prompt tokens. These techniquesenable precise inversion of input images into their initial noise representations and facilitate image this http URL, we propose a mask-based editing technique for localized edits while preserving backgroundintegrity. Comprehensive experiments on the PIE-Bench dataset validate that our method TFinv not onlyachieves state-of-the-art performance in one-step diffusion editing, but also significantly outperforms existingmultistep approaches in efficiency. The code is available at this https URL.

---


### 364. [Formal Verification of Secure Encrypted Virtualization](https://arxiv.org/abs/2606.01381)

**<font color=#1a73e8>作者：</font>** Hansika Weerasena, Amitabh Das, Prabhat Mishra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted execution environments (TEEs) provide a secure environment for data and code in use, ensuring that they are protected with respect to confidentiality and integrity. Virtual machine (VM)-based TEEs utilize virtualization technology to create isolated execution spaces that can support a complete operating system or specific applications. AMD secure encrypted virtualization (SEV) is a key technology used in confidential computing in the cloud enabling hardware-based memory encryption to protect sensitive data within VMs. However, AMD SEV often operate without formal assurances of their security guarantees. Our research introduces a formal framework for representing and verifying AMD SEV confidential VMs. Specifically, we conduct design-level and property-level abstraction on AMD SEV specification and conduct property checking on the model to ensure confidentiality, integrity and availability. This approach provides a rigorous foundation for defining and verifying key security attributes for safeguarding execution environments.

---


### 365. [GuidaPA: Privacy-Preserving Chatbot for Public Administration via Federated Learning](https://arxiv.org/abs/2606.01386)

**<font color=#1a73e8>作者：</font>** Daniel M. Jimenez-Gutierrez, Albenzio Cirillo, Raffaele Nicolussi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present GuidaPA, a privacy-preserving chatbot for the Italian Public Administration (PA) trained via Federated Learning (FL) on documentation from two national PA platforms, SIGESON and SIDFORS. Our corpus includes approximately 8 pages of SIGESON manuals and 31 pages of SIDFORS manuals/FAQs; while this study uses public documentation as a safe proxy, the intended deployment extends to restricted internal sources (e.g., tickets, officer manuals, database extracts) that can not be centrally pooled due to regulatory and organizational constraints. GuidaPA integrates role-based access control, secure client-side preprocessing, explicit monitoring of non-IID effects, and parameter-efficient federated fine-tuning of large language models. Using QLoRA (4-bit) over 15 federated rounds with an 80/20 train-test split per client, we evaluate answer quality with ROUGE, BLEU-4, and METEOR. The best federated model achieves ROUGE-1/2/L of 61.10/55.77/59.44, BLEU-4 of 45.02, and METEOR of 63.94-close to private centralized fine-tuning while keeping data on-site. Compared to the general-purpose baseline, domain fine-tuning improves ROUGE-1 from 41.45 to 62.18 and BLEU-4 from 26.97 to 50.90. Overall, the results indicate that FL can deliver high-quality conversational AI for public services without centralized data sharing

---


### 366. [Dr. DocBench: A Comprehensive Benchmark for Expert-Level and Difficult Document Parsing](https://arxiv.org/abs/2606.01393)

**<font color=#1a73e8>作者：</font>** Minglai Yang, Xinyan Velocity Yu, Pengyuan Li 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document parsing and recognition are fundamental capabilities for vision-language models (VLMs) and document processing systems. However, existing Optical Character Recognition (OCR) and document parsing benchmarks are increasingly limited in coverage and difficulty: many focus on common document genres or uniformly sampled pages where modern parsers already perform strongly, while offering limited annotation for expert-domain structures such as chemical formula, music notation, complex tables, and cross-page layouts. We introduce Dr. DocBench, a difficulty-aware benchmark for expert-level document parsing. Built from a large-scale multilingual book corpus, Dr. DocBench spans 52 BISAC subject domains and selects challenging documents through parser-failure-based sampling, targeting cases where multiple state-of-the-art systems struggle. It contains 4,514 annotated pages from long documents averaging around 100 pages, with 65k high-quality page- and block-level annotations for layout, reading order, hierarchical relations, and domain-specific visual contents. Evaluations of pipeline-based parsers and general-purpose VLMs show that strong performance on existing benchmarks does not transfer to our expert-level document parsing. Our analysis reveals substantial failures across subjects, content types, and structural attributes, highlighting Dr. DocBench as a comprehensive testbed for diagnosing and advancing document intelligence.

---


### 367. [PAI-Studio: Cinematic Video Background Replacement with Camera-Aware Motion](https://arxiv.org/abs/2606.01399)

**<font color=#1a73e8>作者：</font>** Heyuan Gao, Bangxun Tang, Yiren Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PAI-Studio, a new reference-conditioned video synthesis task that addresses a long-standing challenge in cinematic background replacement: generating dynamic backgrounds aligned with foreground motion while preserving foreground identity, matching reference scene appearance, and achieving globally consistent illumination with realistic foreground relighting. Existing open-source systems and commercial APIs cannot simultaneously ensure motion-consistent background generation, high-fidelity foreground relighting and foreground identity preservation, often resulting in static backgrounds, inconsistent boundaries, and noticeable compositing artifacts. To bridge this gap, we build upon a Diffusion Transformer video backbone and reformulate the problem as an in-context conditional generation task. Through bidirectional attention, our model jointly captures foreground dynamics and background reference information within a unified architecture. We further construct a 30K-scale dataset sourced from high-quality films and online videos to support this task. Extensive evaluations demonstrate that our method significantly outperforms existing open-source and commercial API solutions.

---


### 368. [Neural Network Compression by Approximate Differential Equivalence](https://arxiv.org/abs/2606.01402)

**<font color=#1a73e8>作者：</font>** Ravi Dhiman, Andrea Passarella, Mirco Tribastone 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network compression is commonly achieved by pruning parameters based on local importance scores, e.g., magnitude-based pruning. We propose a complementary approach that compresses models by aggregating neurons with similar functional behavior rather than removing weights independently. Our method encodes a trained network as a polynomial ODE system and applies a lumping method called Approximate Forward Differential Equivalence to identify neurons with approximately matching induced dynamics. A single tolerance parameter, $\varepsilon$, controls the compression level and induces a smooth trade-off between model size and predictive accuracy. We evaluate the method on synthetic datasets derived from nonlinear dynamical systems with known ground-truth behavior and on public regression benchmarks. Across both settings, the proposed approach achieves substantial parameter reduction while preserving accuracy, and consistently compares favorably with magnitude-based pruning and Wanda at similar compression levels. These results suggest that differential equivalence-based aggregation is a principled and effective alternative to conventional weight-centric pruning.

---


### 369. [Differentially Private Datastore Generation for Retrieval-Augmented Inference](https://arxiv.org/abs/2606.01413)

**<font color=#1a73e8>作者：</font>** Abdelrahman Abouelenein, Marwan Torki  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> It is crucial for modern on-device AI systems that rely on retrieval-augmented inference to release and share datastores without compromising individual privacy. This can be achieved using Differential Privacy (DP), which provides a formal guarantee that ensures individual contributions remain indistinguishable, even under adversarial analysis. In this paper, we introduce a hashing-based probability generation framework designed to enable the creation and release of differentially private datastores. Our approach employs locality-sensitive hashing (LSH) to efficiently partition high-dimensional data into buckets. We then add calibrated DP noise to the accumulated vote for each bucket, generating a probability distribution across classes. Our method is broadly applicable to any pipeline requiring secure key,value datastore creation and release. We conducted experiments on seven datasets with varying sample sizes and class counts, ranging from 2 to 14. At epsilon=5, our released DP datastore achieves strong privacy protection with only an average 2.6% drop in accuracy. Finally, we benchmark DP datastore resilience to membership inference attacks, reducing attack accuracy to 53.60%.

---


### 370. [Agent Skills Should Go Beyond Text: The Case for Visual Skills](https://arxiv.org/abs/2606.01414)

**<font color=#1a73e8>作者：</font>** Binxiao Xu, Ruichuan An, Bocheng Zou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reusable skills are a key mechanism for extending agent capabilities, allowing agents to accumulate experience and solve increasingly complex tasks. Yet most existing skill-learning methods store reusable experience as text-only assets, such as instructions, reasoning traces, or summarized trajectories. We argue that this text-only paradigm creates a fundamental bottleneck for visual-centric tasks, where reusable knowledge often depends on spatial layout, visual grounding, fine-grained appearance, and localized state changes. To address this limitation, we propose \textbf{\NAME}, a multimodal skill paradigm that combines declarative textual logic with explicit visual support. We distinguish three reusable forms: static priors for stable spatial conventions, dynamic priors for in-situ visual working memory, and interleaved visual skills that bind ordered text steps to the source frames, screenshots, or page regions that justify them. Rather than only describing what to do, visual skills also encode where to look, how to inspect, and how to verify visual outcomes. To scale visual-skill construction, we introduce \textbf{\SYSTEM}, an automatic system that converts agent experience into reusable multimodal skills by preserving textual reasoning, spatial references, visual boundaries, and interaction patterns from task trajectories. Experiments on GUI and other visual-centric tasks show that visual skills consistently outperform text-only skills, particularly when success requires spatial correspondence, visual evidence, and state-aware interaction. These results support our central position: reusable agent skills should go beyond text and become multimodal assets for future multimodal agents.

---


### 371. [GovAI-Pipe: A Layered AI Governance Pipeline for Citizen-Facing AI in Turkey's e-Government Gateway](https://arxiv.org/abs/2606.01417)

**<font color=#1a73e8>作者：</font>** Ahmet Kaplan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Turkey's e-Government Gateway (e-Devlet) serves over 68 million registered users with more than 9,200 government services, and is increasingly integrating artificial intelligence into citizen-facing applications such as chatbot assistants and eligibility assessments. However, no structured technical governance infrastructure currently connects high-level AI policy frameworks, such as the EU AI Act, OECD AI Principles, and Turkey's own National AI Strategy, to the operational reality of deploying AI within a centralized e-government platform. We propose GovAI-Pipe, a four-layer governance pipeline designed using Design Science Research methodology that maps the AI model lifecycle to governance checkpoints: (1) pre-deployment validation for bias testing, explainability, and privacy impact assessment; (2) deployment governance for risk-tier classification and approval workflows; (3) runtime monitoring for drift detection, fairness tracking, and human-in-the-loop escalation; and (4) post-incident governance for audit trails, rollback, and citizen redress. Each layer is anchored to specific provisions of the EU AI Act, the GDPR data protection framework, and the National AI Strategy. We demonstrate the framework through two high-risk e-Devlet use cases, showing how GovAI-Pipe operationalizes governance principles as auditable, technical pipeline components.

---


### 372. [DENSER: Depth-Guided Ensemble with Staged EFA-GS Reconstruction for Soccer Novel View Synthesis](https://arxiv.org/abs/2606.01419)

**<font color=#1a73e8>作者：</font>** Parthsarthi Rawat  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose DENSER, a Depth-guided ENSemble with Staged EFA-GS Reconstruction for soccer novel view synthesis. DENSER extends EFA-GS with three key contributions: (1) camera-height-based loss weighting that prioritises ground-level broadcast views, (2) monocular depth supervision from Depth-Anything-V2 to regularise geometry in textureless regions, and (3) a three-model pixel-average ensemble whose members diverge from a shared base checkpoint by varying training length and Gaussian scale clamping. On five held-out challenge scenes we achieve a mean PSNR of 29.89 dB, SSIM of 0.791, and LPIPS of 0.366.

---


### 373. [Target localization, identification and sensing using latent symmetries](https://arxiv.org/abs/2606.01421)

**<font color=#1a73e8>作者：</font>** David Dukov, Malte Röntgen, Bryn Davies  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that an array of scatterers which has been designed to have latent ("hidden") symmetries can be used as a sensor. We use the capacitance matrix as a canonical model for three-dimensional hybridisation and study how the introduction of an "intruder'' scatterer breaks the latent symmetries. By analysing the degree to which each symmetry is broken, we identify the radius of the intruder and localize its position. This can be achieved using a dictionary-based approach, however Bayesian inference or an artificial neural network (multi-layer perceptron) perform better in the presence of measurement noise. To our knowledge, this is the first time latent symmetries have been exploited successfully for sensing problems. It is also the first time latent symmetries have been observed in a three-dimensional open system that cannot be approximated by a sparse graph.

---


### 374. [Learning-based Directed Graph Abstraction of Combinatorial Spaces for Order-Preserving Search in Mixed-Combinatorial Nonlinear Optimization](https://arxiv.org/abs/2606.01425)

**<font color=#1a73e8>作者：</font>** Gishnu Madhu, Feng Liu, Souma Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-combinatorial nonlinear programming (MCNLP) problems arise in many engineering design and planning applications, e.g., due to categorical, component, and geometric design choices, as well as joint task and motion planning. Traditional representations of combinatorial spaces, such as integer or binary encoding, often introduce spurious relations, increase dimensionality, and require additional compatibility constraints. Instead, this paper draws on recent developments in robot planning and vehicle/network routing domains that aim to learn search heuristics over combinatorial spaces using graph neural networks (GNNs). More specifically, this paper presents a first-of-its-kind structured abstraction of the combinatorial space by learning a mapping from an undirected fully connected graph of combinations to a directed graph indicating improvement directions using an Edge Field Graph Network (EFGN). To demonstrate the utility of this new way of abstracting the combinatorial space in solving MCNLPs, we adopt a recent optimization framework that purely searches over the non-combinatorial (e.g., continuous) variables and retrieves the best-suited combination for each candidate design by using the abstraction model, akin to a recommender system. The presented direction-aware abstraction model provides a potentially more scalable and interpretable retrieval of combinations compared to the original recommendation system in that framework. For evaluation, the proposed method is integrated with a well-known particle swarm optimization and genetic algorithm solvers on three benchmark nonlinear problems with varying numbers of combinations and variables. Compared to baseline solvers using indexified combinations, the GNN-based recommender consistently achieves better mean optimum values and robustness across multiple runs.

---


### 375. [Leaf Spectral Reflectance Prediction Using Multi-Head Attention Neural Networks](https://arxiv.org/abs/2606.01432)

**<font color=#1a73e8>作者：</font>** Parastoo Farajpoor, Alireza Pourreza, Mohammadreza Narimani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate modeling of leaf spectral reflectance from physiological and biochemical traits is essential for advancing remote sensing applications in plant science and precision agriculture. Widely used radiative transfer models, such as PROSPECT-PRO, rely on generalized trait-reflectance relationships developed from a wide range of species, which may not fully capture the spectral behavior of specific crops like grapevines. In this study, we developed a trait-to-spectra prediction model using a multi-head attention neural network trained on a grapevine-specific dataset that includes 16 leaf traits measured across multiple varieties, growth stages, and years. The model was evaluated using stratified 5-fold cross-validation and achieved an average coefficient of determination (R^2) of 0.84 and normalized root mean squared error (NRMSE) of 1.52 percent, demonstrating high accuracy and generalizability. When compared to PROSPECT-PRO in forward mode, the neural network exhibited lower mean absolute error (MAE), especially in the near-infrared (NIR) and shortwave-infrared (SWIR) regions. These results emphasize the importance of species-specific modeling approaches and show that integrating biochemical and structural traits into data-driven architectures can significantly improve spectral prediction. The proposed model provides a robust framework for generating accurate leaf-level reflectance data, with potential applications in canopy trait retrieval, vineyard monitoring, and remote sensing-driven crop management.

---


### 376. [DrugClaw and DrugAudit: A Primary-Source-Grounded Agent and Authority-Aware Benchmark for Drug-Information Question Answering](https://arxiv.org/abs/2606.01434)

**<font color=#1a73e8>作者：</font>** Qing Wang, Bo Li, Jialu Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Drug-information question answering is a high-stakes setting where hallucinated facts can mislead clinical decision-making and the provenance of each cited fact matters as much as the fact itself. We present DrugClaw, a multi-agent retrieval-augmented system that queries a registry of drug and pharmacovigilance skills via a reflection-driven state-machine workflow and returns answers grounded in primary regulatory or peer-reviewed records. We also contribute DrugAudit, a 3,772-item authority-aware benchmark with an evaluation panel that scores upstream-of-gold source match, token-level semantic snippet overlap, and citation faithfulness under a dual-judge LLM-as-judge protocol with inter-judge kappa = 0.88 (almost-perfect). Across DrugAudit plus drug-related subsets of MedQA (751) and PubMedQA (512), DrugClaw is top-1 on every column of the headline table: composite Evidence Index under both judges, judge-mediated answer correctness, primary-source rate (0.918, +10.1 pp over next-best), faithfulness (0.887, +5.9 pp), MedQA (0.920), and PubMedQA (0.693).

---


### 377. [CEAR: Certified Ensemble Adversarial Robustness in DNNs](https://arxiv.org/abs/2606.01437)

**<font color=#1a73e8>作者：</font>** Daniel Sadig, Mohammadreza Maleki, Hamed Karimi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Neural Networks (DNNs) are highly susceptible to adversarial perturbations, leading to extensive research on robustness for safety-critical applications. State-of-the-art empirical defense mechanisms improve the robustness of DNNs through the training phase, but still struggle against adaptive white-box attacks. On the other hand, certified defenses offer provable guarantees of robustness within a specified perturbation bound. These guarantees hold regardless of the level of perturbations, even if the attacker is given full knowledge of the model. In this paper, we propose CEAR, an ensemble-based robust method that utilizes a hybrid of empirical and certified defense mechanisms. CEAR trains each network within the ensemble using varying Gaussian noise and temperatures to obfuscate gradients and logits, making the model more resistant to stronger gradient-based attacks. We then use noisy logits and propose two different voting mechanisms to further improve robustness. Furthermore, we extend randomized smoothing to verify the robustness of ensemble-based classifiers. Our experimental evaluations on MNIST, CIFAR10, and TinyImageNet datasets demonstrate superior certified accuracy on average, increased robustness radius, and decreased transferability compared to baseline methods.

---


### 378. [On the Evaluation of Spiking Neural Network Configurations for Network Intrusion Detection](https://arxiv.org/abs/2606.01442)

**<font color=#1a73e8>作者：</font>** Raj Patel, David Amebley, Taye Akinrele 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network intrusion detection is a core component of modern cybersecurity infrastructure, yet the deep learning models that dominate the field are computationally demanding, motivating interest in lightweight alternatives suited to edge and neuromorphic deployment. Spiking Neural Networks (SNNs) are therefore a natural candidate, but their design space, spanning the choice of neuron model and spike encoding scheme, remains poorly characterized for intrusion detection. We bridge this gap by using a controlled ablation study using 9 neurons coupled with 3 spike encoding schemes, making 27 variants, all implemented on snntorch evaluated over raw inputs with limited preprocessing on four benchmark datasets (NSL KDD, KDDCup99, CIC-IDS2017, and CTU-13) with 5 seeds. We find that spike encoding scheme is a better determinant for detection quality than the neuron model, where rate and delta spike encodings perform worse than latency encoding over the sweep. The LeakyParallel neuron with latency encoding performed the best overall, averaging at 92.11% accuracy and 0.80 macro- F1 at a rate of 2.01% false positives averaged over all 4 datasets, with accuracy close to perfect for CIC-IDS2017 and CTU-13, and also performed the fastest on inference. These results highlight the potential of SNNs as a viable alternative to traditional methods of intrusion detection when considering low-latency or resource-constrained deployments.

---


### 379. [UR-JEPA: Uniform Rectifiability as a Regularizer for Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2606.01443)

**<font color=#1a73e8>作者：</font>** Triet M. Le  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central difficulty in training Joint-Embedding Predictive Architectures (JEPAs) is preventing representation collapse. LeJEPA addresses this by enforcing an isotropic Gaussian target on the embeddings via Sketched Isotropic Gaussian Regularization (SIGReg). This target is in tension with the manifold hypothesis, which expects embeddings to concentrate on a low-dimensional subset of the ambient space. We propose \emph{UR-JEPA}, which targets a uniformly $n$-rectifiable measure of local tangent dimension $n$ at small scales, realized through a Gaussian-kernel smoothed Carleson-type square function $\mathcal{L}^{\text{CGLT}}$, with a complementary Jones $\beta$-number formulation. On Inet10, UR-JEPA($\mathcal{L}^{\text{CGLT}}$) attains $0.9141 \pm 0.0014$ for a $+0.83$\,pp gain over LeJEPA($\mathcal{L}^{\text{SIGReg}}$) with $\sim 30\%$ lower seed standard deviation; on matched-recipe Galaxy10~SDSS, a single-seed ImageNet-$100$ run, and a $3$-seed EuroSAT remote-sensing run, the two methods lie in the same peak-accuracy band at convergence, with UR-JEPA retaining its lower-seed-variance signature. On EuroSAT the in-domain pair is competitive at $96.0$ to $96.1\%$ with large remote-sensing foundation-model transfer at a $25\times$ smaller backbone. The distinction is geometric: direct visualization of the projector output distribution shows that on all four datasets UR--JEPA($\mathcal{L}^{\text{CGLT}}$) produces a global PCA spectrum with a $4$ to $5$ order-of-magnitude drop at index $\sim 20$ to $25$ out of $D = 32$, while LeJEPA's spectrum is near-flat (top-to-bottom ratio at most $3.6$). Per-dimension marginals are simultaneously near-Gaussian for both methods (mean Shapiro-Wilk $W \in [0.992, 0.996]$) as a Diaconis-Freedman consequence. At matched accuracy the two regularizers therefore yield structurally distinct projected representations.

---


### 380. [NetVAD: Foundation-Model Representation Learning for Identifier-Free Unsupervised Intrusion Detection](https://arxiv.org/abs/2606.01452)

**<font color=#1a73e8>作者：</font>** Darren Fürst, Patrick Levi, Sebastian Steindl  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Detecting zero-day exploits in production networks requires robust Intrusion Detection Systems (IDS). However, current unsupervised models struggle to match the performance of supervised classifiers, which are trained for specific attacks only. To bridge this gap, we leverage the emerging capabilities of Network Foundation Models. We propose \textit{NetVAD}, a strictly identifier-free Variational Autoencoder that projects representations from a frozen Foundation Model into a task-specific latent space, trained solely on benign traffic. Evaluated on ToN-IoT and IoT-23, NetVAD achieves highly competitive unsupervised performance. On ToN-IoT, it achieves a 98% Micro F1-score and a 96% Macro F1-score at an operational false positive rate. Unlike prior work, we show the model's performance transparently for all attack-classes of the datasets. While the architecture excels at discerning complex botnet behaviour (99.6% F1 on Okiru), our evaluation reveals limitations of flow-based Foundation Models in detecting single-packet reconnaissance events. Finally, a comprehensive ablation study confirms that while large-scale pre-training is essential to prevent performance degrading, specialised decoder architectures are necessary to precisely model the complex benign manifold, ensuring attacks are caught more reliably, due to a higher reconstruction loss.

---


### 381. [Transferring Information Across Interventions in Causal Bayesian Optimization](https://arxiv.org/abs/2606.01457)

**<font color=#1a73e8>作者：</font>** Mohammad Ali Javidian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization is a popular way to optimize expensive systems, where every experiment, simulation, or intervention costs time or money. In its standard form, it treats the variables we control as plain inputs to a black box and cannot tell apart mere correlation from a real cause and effect. Causal Bayesian optimization closes part of this gap by using a known causal graph together with observational data to decide which variables are worth intervening on. Existing methods, however, learn the effect of each possible intervention almost in isolation, even though in a causal system these effects usually share the same underlying mechanisms. We propose graph-coupled causal Bayesian optimization, which ties the different intervention effects together through the uncertainty we have about a small set of shared causal parameters. The result is a causal kernel that lets evidence collected from one intervention improve our estimate of related interventions. For identifiable linear Gaussian causal models, we show that this kernel has low rank, bounded by the number of shared parameters rather than by the size of the intervention menu. This in turn yields an information-gain bound that grows only logarithmically in the optimization horizon, and a regret bound that cleanly separates three sources of error: optimization, causal estimation, and the choice of which intervention sets to consider. We also describe nonlinear and adaptive extensions. Across theory-aligned Gaussian systems, shared-mechanism stress tests, and standard causal optimization benchmarks, the method keeps the benefits of causal Bayesian optimization while transferring information across related interventions, with the clearest gains when direct interventions on the target's parents are unavailable and sparse interventional data must be reused across a large family of candidate interventions.

---


### 382. [Genotype-Conditioned Molecular Generation via Evidence-Grounded Multi-Objective Latent Perturbation in Diffusion Models](https://arxiv.org/abs/2606.01461)

**<font color=#1a73e8>作者：</font>** Brenda Nogueira, Gisela A. Gonzalez-Montiel, Nitesh V. Chawla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Developing effective anticancer therapeutics remains challenging due to tumor heterogeneity and the absence of well-defined molecular targets across cancer subtypes. Generative models conditioned on cancer genotypes offer a promising avenue for personalized drug discovery, yet existing approaches lack explicit optimization for simultaneous sensitivity, synthesizability, and mechanistic binding plausibility. We present a latent-space optimization approach for a pretrained genotype-to-drug diffusion model, introducing a learnable perturbation over the molecular latent space optimized via gradient ascent to maximize a composite reward combining predicted drug sensitivity (AUC), drug-likeness (QED), and synthetic accessibility (SAS). Critically, biological realism is enforced by grounding both reward design and evaluation in experimentally-derived cancer cell line data and validated pharmacologic signals, anchoring candidate generation in real-world clinical evidence. Mechanistic consistency plausibility is further assessed by a multi-agent LLM pipeline grounded in the diffusion model's attention mechanism. Experiments across 15 cancer cell lines from three held-out evaluation sets demonstrate consistent and noticeable improvements over competing baselines in sensitivity, drug-likeness, synthesizability, and chemical validity.

---


### 383. [Peacemaker at ATE-IT: Automatic term extraction from Italian text for waste management data using encoder model](https://arxiv.org/abs/2606.01469)

**<font color=#1a73e8>作者：</font>** Mahdi Bakhtiyarzadeh, Hadi Bayrami Asl Tekanlou, Jafar Razmara  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The development of automatic term extraction has become increasingly important in modern technology. Automatic term extraction can be found in virtually every search engine that is currently available to users. Recent advancements have provided promising results for the extraction of automatic terms; however, accurate labeling is difficult because of several factors, such as the limited number of annotated documents available for training and the complexity of extracting multi-word expressions due to shifts in the domain. In this paper, we will present a low-cost and interpretable method of automatic term extraction, developed specifically for Task A of the ATE Shared Task. This new method utilizes fine-tuning extraction strategies that can run on a small amount of computational resources. We evaluated our automated system using both type-level and micro-level measures of precision, recall, and F1-score to measure both complementary aspects of the extraction performance. According to the experimental results, our proposed approach achieves consistent and balanced performance compared to other teams. Even though the technique itself is relatively straightforward, it serves as a good starting point for low-resource models. Overall, the findings point toward the possibility of significant future advancements (in model expansion) with higher-level performance still able to retain their ability to be interpreted.

---


### 384. [A Minimalist Brain-Computer Musical Interface for Real-Time Emotion-Driven Sonification: System Design and Preliminary Evaluation](https://arxiv.org/abs/2606.01473)

**<font color=#1a73e8>作者：</font>** Pablo A. Monroy-D'Croz, Rafael Ramirez-Melendez, Julian Cespedes-Guevara  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a minimalist brain-computer Musical Interface (BCMI) that functions as a real-time affective sonification system, translating prefrontal EEG activity into adaptive music. Emotional valence is estimated from frontal alpha asymmetry (AF7/AF8) and mapped to musical features such as mode, tempo, rhythmic density, and pitch register through a stochastic generative algorithm. The system integrates wireless EEG acquisition, real-time Python signal processing, and Ableton Live-based music generation synchronized via Lab Streaming Layer. An experiment with 22 participants investigated whether intentional emotional self-induction could modulate the BCMI neurofeedback signal. Linear mixed-effects analyses found no significant effects of target emotion or time, indicating that the frontal alpha asymmetry signal did not reliably distinguish instructed emotional states. Individual differences, including musical training and acting experience, explained more variance than the experimental manipulation, which accounted for only 0.40\% of total signal variance. These findings highlight the challenges of using frontal alpha asymmetry as a voluntary control signal for closed-loop emotion regulation and suggest methodological directions for future BCMI research.

---


### 385. [Sparse Autoencoders for Interpretable Emotion Control in Text-to-Speech](https://arxiv.org/abs/2606.01479)

**<font color=#1a73e8>作者：</font>** Hongfei Du, Jiacheng Shi, Sidi Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Integrating large language models (LLMs) into text-to-speech (TTS) systems has improved speech expressiveness, yet interpretable emotional control remains challenging. Existing approaches primarily rely on external conditioning or global activation steering, offering limited insight into the internal representations underlying emotional control. In this work, we analyze emotion-related variation in the semantic hidden states of LLM-based TTS models using sparse autoencoders (SAEs) to identify sparse latent features. Our analysis shows that emotional variation is distributed across multiple sparse latent features, while intervening on a small subset enables interpretable emotion control. Building on this observation, we introduce a feature-level intervention framework for bidirectional emotion induction and suppression without modifying backbone parameters. We further show that distinct latent features are associated with specific acoustic attributes (e.g., pitch), suggesting that emotional expression arises from coordinated latent contributions rather than a single global shift. Empirically, steering these sparse latent features achieves comparable or superior emotion induction and suppression performance relative to global steering and existing TTS baselines.

---


### 386. [SafeGen-Bench: Benchmarking Safety in Image-Conditioned Text-to-Video Generation](https://arxiv.org/abs/2606.01481)

**<font color=#1a73e8>作者：</font>** Yingzi Ma, Xiaogeng Liu, Yawen Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid advancements in text-to-image diffusion models, generative video models (T2V models) like Sora can now produce short synthetic videos from a text prompt or an initial image. However, synthetic video generation -- especially when guided by an initial image -- often poses risks, including the potential creation of illegal, politically sensitive, or unethical content. Existing benchmarks have started to consider the safety of generated videos, but they primarily focus on testing models with malicious text prompts, ignoring the scenario where text prompt and image combination may still lead to harmful video content. In practice, this is a common and challenging issue: videos generated from safe text and image inputs can nonetheless convey harmful information. To bridge this gap, we introduce SafeGen-Bench, a benchmark specifically designed to evaluate the safety of conditional T2V models. Our benchmark defines 10 malicious categories, concentrating on risks related to both temporal sequences and depicted behaviors. SafeGen-Bench consists of carefully selected start frames from diverse image and video sources, paired with corresponding text prompts to simulate realistic inputs. We evaluate a variety of conditional T2V models on SafeGen-Bench, and the results indicate that current models struggle to consistently avoid generating malicious content with unsafety scores reaching up to 44.5, especially under conditions requiring high quality. Furthermore, we assess the effectiveness of both text-based and image-based guardrails on our benchmark, finding that unimodal guardrails alone were insufficient to provide a robust defense, with an 80\% failure rate across seven malicious categories. We hope that SafeGen-Bench will foster the development of safer and more controllable conditional T2V models.

---


### 387. [MURMUR: An Efficient Inference System for Long-Form ASR](https://arxiv.org/abs/2606.01483)

**<font color=#1a73e8>作者：</font>** Wei-Tzu Lee, Keisuke Kamahori, Baris Kasikci  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-form automatic speech recognition (ASR) requires both high accuracy and low latency, but existing systems force a trade-off between the two. Chunk-based pipelines process audio in parallel windows for low latency, but lose cross-chunk context and need brittle heuristics to align speakers and timestamps at boundaries. Long-context ASR models resolve everything in a single pass for better accuracy, but are an order of magnitude slower. We propose Murmur, an inference system that overcomes this trade-off by operating at two levels. At the inter-chunk level, we revisit the chunk-based pipeline for modern long-context ASR, treating chunk size as a tunable hyperparameter, and show that intermediate chunk sizes strike a good balance of accuracy and latency. At the intra-chunk level, we exploit attention sparsity through a sliding window KV cache eviction policy applied to both output and speech tokens. On AMI-IHM, Murmur matches single-pass accuracy while reducing latency by 4.2x, with further gains from token eviction at less than 1% relative tcpWER degradation. The code of Murmur is available at this https URL.

---


### 388. [Perception First: A Frontier Native-Video Model with Self-Consistency for Implicit Video Question Answering](https://arxiv.org/abs/2606.01485)

**<font color=#1a73e8>作者：</font>** Ali Alavi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe our submission to the VRR Challenge @ CVPR 2026, built on the \emph{ImplicitQA} / \emph{VRR-QA} benchmark~\cite{implicitqa}: multiple-choice video question answering in which answers are deliberately \emph{not} observable in any single frame and must be inferred from spatial layout, motion, depth, viewpoint, causality, and social context across discontinuous frames of creative video. We conduct a systematic, training-free study spanning open-source Video-LMMs (Qwen2.5-VL~\cite{qwen25vl}, Qwen3-VL~\cite{qwen3vl}, InternVL3, Gemma-3, and the RL-tuned video reasoners Video-R1~\cite{videor1} and VideoChat-R1.5~\cite{videochatr15}) and a battery of inference-time strategies (chain-of-thought, question decomposition, describe-then-reason cascades, audio transcripts, spatial state prompting, self-consistency~\cite{selfconsistency}, multi-model ensembling, and category routing). Our central finding is that this benchmark is \emph{perception-bound rather than reasoning-bound}: reasoning-side augmentations are neutral-to-harmful, whereas base-model perceptual capability and lightweight test-time denoising are the only reliable levers. A per-category error analysis localizes the difficulty to low-level perception -- relative depth, viewpoint, and counting are the hardest categories, while causal and social reasoning are nearly solved -- and a prompt that explicitly injects monocular depth cues to attack the weakest category \emph{lowers} test accuracy by $5.8$ points, confirming that the model needs a better \emph{percept}, not a better \emph{procedure}.

---


### 389. [Splatshot: 3D Face Avatar Generation from a Single Unconstrained Photo](https://arxiv.org/abs/2606.01493)

**<font color=#1a73e8>作者：</font>** Hao Liang, Zhixuan Ge, Soumendu Majee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing a photorealistic 3D face avatar from a single unconstrained photograph is challenging: feed-forward 3D Gaussian Splatting (3DGS) models degrade on out-of-distribution inputs, while pretrained diffusion models produce high-fidelity images but lack multi-view consistency. We observe that these paradigms are fundamentally complementary: explicit 3D representations guarantee geometric consistency, whereas 2D diffusion priors ensure photorealism. Building on this, we propose SplatShot, a training-free framework that couples these representations directly within the denoising process. Given a base 3DGS face model and a single reference image, we jointly denoise all target views using a per-step 3D feedback loop. At each timestep, we predict clean images from the noisy latents, refit the 3DGS to these multi-view predictions, and back-propagate the photometric discrepancy between the 3DGS re-renderings and 2D predictions into the noise estimate. This steers the sampling trajectory toward strictly 3D-coherent, identity-faithful outputs. Experiments on diverse in-the-wild images demonstrate that SplatShot produces 3D avatars with superior identity preservation, photorealism, and multi-view consistency.

---


### 390. [ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector Disagree](https://arxiv.org/abs/2606.01494)

**<font color=#1a73e8>作者：</font>** Vincent Koc, Patrick Erichsen, Jacob Tomlinson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills extend AI agents with reusable instructions, tools, scripts, references, and workflows, establishing a security boundary distinct from both model safety and traditional package-malware detection. ClawHub Security Signals is a sanitized dataset of 67,453 latest public OpenClaw skill versions. Each row pairs redacted this http URL content and sanitized bundled files where present with a final ClawScan registry verdict and evidence from three scanner families: VirusTotal, static heuristic analysis, and NVIDIA SkillSpector.
Rather than estimating malicious-skill prevalence, we study scanner disagreement. The three scanners rarely flag the same skills: any pair overlaps on at most 10.4% of their combined positives, only 0.69% of skills are flagged by all three, and 81.9% of flagged skills are identified by a single scanner. The disagreement is structured by attack surface. SkillSpector, which raises semantic agentic-risk advisories rather than malware-reputation signals, is positive for 19,209 of 25,504 suspicious rows (75.3%) but only 14 of 206 malicious rows (6.8%). The malicious-verdict region shows the inverse profile: 150 of 206 malicious rows (72.8%) are VirusTotal-positive, consistent with bundled-code malware evidence.
These results show that agent-skill security requires layered governance, not single-scanner allow/block decisions. The corpus is released as a sanitized silver-standard dataset: labels are the registry's automated verdicts, not human-annotated ground truth, and the release represents an early, versioned snapshot intended to support the community while a human-annotated subset is developed. Further research is encouraged, including models tailored for skill-security triage.

---


### 391. [CART: Context-Anchored Recurrent Transformer -- A Parameter-Efficient Architecture with Learned Stability](https://arxiv.org/abs/2606.01495)

**<font color=#1a73e8>作者：</font>** Chad A. Capps  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present CART (Context-Anchored Recurrent Transformer), a parameter-efficient language model that reuses a single shared core block R times across depth. Unlike prior looped transformers that recompute key-value tensors at every iteration, CART computes K and V once from a multi-layer prelude and has the recurrent core cross-attend to those frozen tensors via multi-head latent attention. A learned Linear Time-Invariant (LTI) gate keeps the recurrence stable: its spectral radius settles in a narrow band (rho in [0.79, 0.83]) across all 36 fully-trained configurations.
We evaluate CART on single consumer GPUs in two stages: a 64-configuration screen at 3,000 steps, then 36 configurations (P=6, R in {6,8,10}, three seeds) trained for 30,500 steps (~1B tokens). Two patterns hold across widths d in {256,512,768,1024}: prelude depth P dominates loop count R, and the Stage-1 ranking of R reverses at full training (R=6 becomes best at d>=512). At the binding d=1024 parameter-parity test, CART does not beat a parameter-matched dense baseline, losing by 1-2% at stored-parameter parity and by ~10% at effective-parameter parity. Diagnostic ablations split the effective-parameter gap into ~5% from weight sharing and a residual ~5% from the heterogeneous prelude/anchor/core/coda framing; the recurrent-core machinery (hyper-connections, LTI gate, loop-index embedding) is individually vestigial. Variable-R inference degrades on both sides of the trained R, a negative result for test-time depth scaling under this recipe.

---


### 392. [On the Limits of Token Reduction for Efficient Unified Vision Language Training](https://arxiv.org/abs/2606.01503)

**<font color=#1a73e8>作者：</font>** Siyi Chen, Weiming Zhuang, Jingtao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified vision-language models (VLMs) integrate visual understanding and visual generation within a single autoregressive backbone, but their joint training is computationally expensive and largely overlooked from an efficiency perspective. In this work, we study the feasibility and limits of token-reduction-based acceleration for unified VLM training. Through a systematic analysis of layerwise attention allocation, we uncover a fundamental asymmetry: visual understanding exhibits substantial late-layer visual redundancy, whereas visual generation maintains persistent dependence on image tokens across depth. Guided by this observation, we design task-specific accelerators that selectively reduce image-token computation for each objective. While these methods achieve significant efficiency gains in isolated settings, we observe a consistent synergy loss under unified training -- task-specific token dropping necessitates divergent parameter pathways and eliminates the mutual performance gains typically observed in joint optimization. Our findings suggest that efficient unified modeling requires preserving shared cross-task structures, highlighting the need for synergy-aware acceleration strategies. Project page: this https URL.

---


### 393. [MotionDreamer: Universal Skeletal Motion Generation for 3D Rigged Shapes](https://arxiv.org/abs/2606.01518)

**<font color=#1a73e8>作者：</font>** Ye Tao, Yuxin Yao, Kendong Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion generation for rigged shapes is vital for scalable 4D asset production. However, template-based methods are limited by specific topologies and fail to generalize across diverse morphologies. Conversely, per-case optimization is computationally expensive, susceptible to local optima, and highly sensitive to viewpoint-induced ambiguities. In this paper, we present MotionDreamer, a diffusion-based framework designed for category-agnostic skeletal animation generation from 2D video guidance. To overcome the scarcity of high-quality training data, we have curated a large-scale dynamic dataset comprising approximately 20,000 diverse 3D models, each featuring complete textures, skeletal rigging, and a wide array of comprehensive animation sequences. To bridge the kinematic gap between 2D visual motion cues and heterogeneous 3D skeletal structures, we propose a structural-semantic injection mechanism. Our model integrates texture and semantic attributes directly into skeletal joint representations. This allows it to map perceived visual dynamics to specific joint hierarchies and their functional roles. This enables MotionDreamer to synthesize high-fidelity animations that maintain anatomical consistency across a vast range of unseen categories, from existing biological species to fantastical beings. Extensive experiments demonstrate that our approach significantly outperforms existing methods, setting a new state-of-the-art benchmark for robust and efficient 4D asset generation. The code will be made publicly available upon acceptance.

---


### 394. [TERRA: Task-Embedded Reasoning and Representation Architecture for Cross-Domain Applications](https://arxiv.org/abs/2606.01520)

**<font color=#1a73e8>作者：</font>** Shayan Shokri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A single action-conditioned latent predictive architecture can in principle be trained on the structured state of a driving scene, a robot workspace, or a financial order book. The ingredients for doing so within any one domain already exist and are individually validated: masked-latent prediction, action-conditioned latent world models, discrete action tokenization, and joint-embedding prediction on voxelized state. What is not established, and what TERRA addresses, is the transfer question: when does a representation or predictor learned in one structured-state domain carry over to a structurally analogous but otherwise unrelated domain, and by how much. We give this question a formal treatment. We model each domain as a controlled Markov process on a graded latent grid, factor any instantiation into thin domain adapters and a shared domain-invariant core, and identify a cross-domain correspondence with an approximate Markov decision process homomorphism whose quality is measured by a lax bisimulation discrepancy and, for domains lacking a shared coordinate system, by a Gromov-Wasserstein distance between their action-conditioned transition operators. Under a Lipschitz predictor we derive a transfer bound that separates source-model error from structural mismatch, grows geometrically in the prediction horizon, and is certified from below by the Gromov-Wasserstein distance; we then connect latent error to decision regret through the Lipschitz value property of bisimulation metrics. The resulting Structured-State Transfer Hypothesis is stated as a falsifiable claim with a preregistered experimental program, centered on a transfer test from driving scenes to order books, including conditions under which it is refuted. We present no empirical results: this is a research proposal that converts a widely repeated intuition into testable theory.

---


### 395. [Fast Generalization after Interpolation via Critically Damped Momentum Optimization](https://arxiv.org/abs/2606.01521)

**<font color=#1a73e8>作者：</font>** Luca Muscarnera, Silas Ruhrberg Estévez, Yuanzhang Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central problem in machine learning is that models can achieve near-perfect training performance while generalizing substantially less well to unseen examples. This gap is especially acute in high-dimensional, low-sample regimes, where many interpolating solutions exist and optimization must implicitly select among minima with different generalization properties. Following recent theoretical advances on optimization dynamics near the interpolation threshold, we note that the two-regime structure of risk minimization, with loss minimization followed by complexity minimization, motivates a biphasic optimization schedule. We thus theoretically demonstrate that GROKtimizer, a biphasic strategy that combines rapid convergence to interpolation with Critically Damped Momentum (CDM)-based post-interpolation norm minimization, offers a natural solution for selecting low-norm interpolating solutions. Under a local quadratic model of the post-interpolation basin, GROKtimizer provides a quadratic speedup over classical gradient descent, with provable optimality among first-order optimizers. To showcase the applicability of our method, we evaluate GROKtimizer on several synthetic benchmarks common in the classical grokking literature and on various real-world datasets. Finally, we reconcile our findings with the flat-minima hypothesis, highlighting the importance of post-interpolation dynamics in the construction of high-quality, generalizing models.

---


### 396. [Semi-Supervised Hyperbolic Hierarchical Clustering with Set-Level Structural Priors](https://arxiv.org/abs/2606.01525)

**<font color=#1a73e8>作者：</font>** Junjing Zheng, Xinyu Zhang, Xiangfeng Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-supervised hierarchical clustering aims to learn a tree structure consistent with data patterns and user-provided supervision. Supervision is usually given as leaf-level relations, such as pairwise must-link/cannot-link constraints or triplet-wise must-link-before constraints. Although useful for regulating local sample relations, such supervision does not directly indicate which samples should form coherent subtrees. Consequently, the non-leaf structure of the learned tree may deviate from the hierarchical organization preferred by ground-truth labels. To address this limitation, we propose a semi-supervised hyperbolic hierarchical clustering method with set-level structural priors. The main contribution is to introduce sets as basic modeling units for hierarchy learning. Each set denotes samples expected to cohere within a subtree and is induced from leaf-level supervision together with a learned constraint-consistent similarity structure. These sets act as soft structural priors for subtree-level supervision, allowing supervision to guide non-leaf hierarchy formation beyond local leaf-level relations. Specifically, we first learn constraint-consistent embeddings to obtain a reliable set partition, then construct constraint-induced sets and estimate inter-set similarities to form set-level structural priors. Finally, these priors are incorporated into a hyperbolic hierarchy objective for continuous tree optimization. Experiments on eleven benchmark datasets and ablation studies show that the proposed method consistently improves label consistency over representative hierarchical clustering baselines while also enhancing similarity-based tree quality.

---


### 397. [Near-Optimal Pure Machine Unlearning for Smooth Strongly Convex Losses](https://arxiv.org/abs/2606.01527)

**<font color=#1a73e8>作者：</font>** Matthew Regehr, Gautam Kamath, Andrew Lowy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning is motivated by legal and user-facing requirements to remove the influence of individuals' data from trained models, such as the right to be forgotten. Prior work has developed algorithms and error bounds for unlearning in smooth strongly convex stochastic optimization, but the fundamental statistical cost of unlearning has remained unclear. We nearly resolve this problem by proving upper and lower bounds on the excess population risk of approximate $\varepsilon$-unlearning; our bounds are tight up to a condition-number factor. For mean estimation over the unit ball, our upper and lower bounds match. The optimal rate is the usual statistical error plus an unlearning penalty that interpolates between the retraining-from-scratch rate and an exponentially smaller term as $\varepsilon/d$ grows, where $d$ is the dimension of the model. In particular, when $\varepsilon \gg d$, our $\varepsilon$-unlearning algorithm offers an exponential accuracy improvement over retraining the model from scratch and differentially private baselines. On the other hand, when $\varepsilon \le d$, retraining from scratch is optimal.

---


### 398. [Joint Agent Memory and Exploration Learning via Novelty Signals](https://arxiv.org/abs/2606.01528)

**<font color=#1a73e8>作者：</font>** Shizuo Tian, Xiaohong Weng, Rui Kong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In open-ended environments, exploration is fundamental for autonomous agents, yet current language model agents struggle with this. Effective exploration requires memory, but retaining raw interaction histories is computationally expensive over long trajectories. While latent memory offers a solution to compress interaction histories, its training lacks reliable supervisory signals. We introduce \textbf{J}oint \textbf{A}gent \textbf{M}emory and \textbf{E}xploration \textbf{L}earning (\textbf{JAMEL}), a framework that trains agentic memory and exploration policy together through novelty-driven interaction. We observe that memory and exploration form a mutually dependent loop: sustained exploration requires memory to distinguish exhausted behaviors from unseen ones, while novelty-seeking interaction provides the supervision needed to make memory useful for future exploration. By utilizing deterministic and persistent novelty signals such as code coverage in the GUI domain, we provide natural, annotation-free supervision for the memory module. Empirical evaluations demonstrate that \ours successfully generalizes to unseen environments. Its exploration capability outperforms open-weight baselines and rivals the exploration depth of a closed-source model while reducing token consumption. Our code and model are open-sourced at this https URL.

---


### 399. [Rethinking the Role of Positional Encoding: Sliding-Window Transformers without PE Remain Turing Complete](https://arxiv.org/abs/2606.01532)

**<font color=#1a73e8>作者：</font>** Qian Li, Xinyu Mao, Shang-Hua Teng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Positional encoding (PE) is widely viewed as necessary for transformers to process ordered sequences: without them, the next-token map appears permutation-invariant in its context tokens. This intuition underlies all prior universality results, which rely on positional information to prove that transformers with chain-of-thought can perform arbitrary computation, i.e., they are Turing complete. We revisit this belief in the regime most relevant to long-form reasoning, where generation proceeds through a finite sliding context window. Our opening perception is that the window mechanism itself (mildly) breaks the permutation symmetry. To distill and precisely capture the degree of this added expressiveness, we introduce an abstract autoregressive model, the HIST model, in which each update depends only on constant-size internal state and the token-count histogram within the current window. We prove that this HIST model is Turing complete by showing that the evolution of the window can reveal the token that has just left the window, which suffices to simulate Turing-complete Post machines. We then construct a sliding-window transformer over a constant-size token alphabet, without PE, and show that it can simulate the HIST model. Our result demonstrates that positional encodings are not indispensable for transformers to perform universal computation: The window sliding itself already breaks permutation symmetry and captures sufficient positional information.

---


### 400. [Multi-Agent Computer Use](https://arxiv.org/abs/2606.01533)

**<font color=#1a73e8>作者：</font>** Jing Yu Koh, Ruslan Salakhutdinov, Daniel Fried  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Computer use agents (CUAs) today are primarily deployed as single serial agents. This setup is suboptimal for complex long-horizon tasks that benefit from task decomposition, parallel execution, and consistent re-planning based on new information. In this paper, we argue that we should instead move towards evaluating and building multi-agent computer use (MACU) systems. These systems, which emphasize planning and parallel execution, alleviate many of the shortcomings of single-agent CUAs. We propose a general multi-agent setup in which a manager model decomposes computer use tasks as a directed acyclic graph (DAG), encoding relevant dependencies and goals for subagents. At each iteration, the manager dispatches parallel CUA subagents to carry out nodes on the ready frontier of the DAG, and continuously revises the DAG (adding, canceling, or rewriting nodes) as new findings arrive from subagents. This design treats the partially observable environment of computer use as a first class challenge: information that downstream agents may not be able to re-observe are retained and passed forward through the manager and DAG structure. We demonstrate that MACU consistently improves over strong single-agent baselines by $3.4-25.5\%$ on desktop (OSWorld) and web navigation (Online-Mind2Web, WebTailBench, Odysseys) benchmarks, exhibits more favorable test-time scaling, and solves complex long-horizon tasks where single-agent CUAs get stuck. On Odysseys, a long-horizon web navigation benchmark, MACU improves average task completion wall-clock time by ${\sim} 1.5 \times$, demonstrating its efficacy in speeding up traditionally slow CUA pipelines. Our findings highlight that multi-agent coordination is a promising axis for scaling computer use agents to work productively for longer and more effectively. We release all code and interactive visualizations at this https URL.

---


> [!TIP]
> 当前位于：**351-400**（第 8/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
