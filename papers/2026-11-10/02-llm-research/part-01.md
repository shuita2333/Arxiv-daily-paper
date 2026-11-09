# 🧠 大模型相关研究 | 2026年11月10日

> 本类共 **174** 篇论文：已确认 **163** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-174](./part-04.md)

---

### 1. [Rethinking Data Selection as Distribution Matching on Semantic Manifolds](https://arxiv.org/abs/2611.08495)

**<font color=#1a73e8>作者：</font>** Peng Sun, Yi Yang, Mingshuo Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instruction tuning of large language models and large vision language models relies on massive training data, which incurs substantial computational and storage costs. Meanwhile, training data often contains redundancy, noise, and low quality samples. Existing data selection methods mostly rely on diversity, importance, or a combination of both, without explicitly constraining the distributional consistency between the selected subset and the full data in the embedding space. We propose QMAC, a quality aware multiband characteristic function matching method that formulates data selection as a joint optimization problem of distribution matching and quality filtering. QMAC matches the empirical characteristic functions of the selected subset and the full data across multiple frequency scales, capturing both global semantic coverage and local perturbations, while using task related quality scores to filter noisy and low quality samples. We systematically evaluate QMAC on 4 data types, 8 target models, and 44 benchmarks. Experimental results show that QMAC outperforms existing data selection baselines on standard image-text instruction data, substantially surpasses random selection on standard text instruction, image-text reasoning, and text reasoning data, and exceeds full data training in multiple model and budget combinations. The code will be made publicly available upon acceptance of the paper.

---


### 2. [Emergent Low-Dimensional Topological Dynamics Dictate Generalization and Escape Mechanics in Billion-Parameter Neural Networks](https://arxiv.org/abs/2611.08502)

**<font color=#1a73e8>作者：</font>** Dongqing Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The remarkable generalization of modern over-parameterized neural networks defies classical statistical learning bounds. Here we establish that optimization trajectories in billion-parameter models do not sample the ambient dimension $\mathbb{R}^N$ homogeneously; instead, they are dynamically constrained to a low-dimensional execution submanifold $\mathcal{M}_{\text{exec}}$ (with empirically observed effective dimension $d_{\text{eff}} \le 12$). By equipping the parameter space with a regularized Hessian metric $g_{ij} = \nabla_i \nabla_j L + \epsilon \delta_{ij}$ and analyzing stochastic Langevin diffusion on loss sublevel sets, we derive a rigorous Topological Generalization Bound grounded in projected subspace persistent homology. Furthermore, by linking Morse index transitions to Betti number annihilation ($\beta_1 \to 0$), we formulate an exact mathematical mechanism for exponential escape from strict saddles under anisotropic noise. We validate our framework across 80+ architectures (ResNets, Vision Transformers, and 7B LLMs). To bridge theoretical topology with computational feasibility, we resolve the curse of dimensionality by computing projected persistent homology proxies via randomized Lanczos iterations restricted strictly within active Hessian subspaces. Building upon this mathematical foundation, we introduce Topological-Adaptive Optimization (Top-SGD and Top-AdamW)---a family of wrapper algorithms that dynamically modulate learning rates using active curvature signatures. Extensive benchmarks demonstrate a 14.1\% reduction in total wall-clock training time on ImageNet with all computational and memory overheads fully accounted for. Code is publicly available at this https URL.

---


### 3. [Does Country Matter? Evaluating Geographic Sensitivity of Large Language Models in Zero-Shot Chronic Kidney Disease Screening](https://arxiv.org/abs/2611.08507)

**<font color=#1a73e8>作者：</font>** Sirajam Munira, Muhammad Ashad Kabir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show strong zero-shot reasoning capabilities, yet their sensitivity to prompt context raises questions about reliability in deployment. This study investigates whether geographic context embedded in prompts influences LLM-based chronic kidney disease (CKD) screening, independent of any change in patient features. Using a community-based CKD dataset from Bangladesh (284 participants with 112 CKD and 172 non-CKD), we systematically varied the country attribute across 25 global contexts while holding all clinical inputs constant, and evaluated two open-weight LLMs (Qwen3 8B and Mistral 7B). Experiments were conducted on a common-correct subset of 156 participants for whom both models produced correct baseline predictions. Results show that non-CKD predictions were highly stable across geographic contexts, with both models maintaining consistent non-CKD predictions in nearly all settings. In contrast, CKD-positive predictions were considerably more sensitive. For Qwen3, CKD prediction dropped from a baseline of 65 to as low as 50 across country contexts, while Mistral showed smaller but non-negligible variation. Country contexts did not group according to known epidemiological or healthcare similarities; instead, groupings appear to reflect how country tokens are internally represented within each model. These findings demonstrate that geographic tokens can systematically shift clinical screening outcomes despite identical patient inputs, with implications for the deployment of LLM-based decision support in diverse healthcare settings.

---


### 4. [What Are LLM Agents Actually Learning on Low-Budget Molecular Optimization Benchmarks?](https://arxiv.org/abs/2611.08522)

**<font color=#1a73e8>作者：</font>** Jiayu Qin, Zhengquan Luo, Changyou Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work reports large gains for LLM agents on low-budget molecular optimization. We measure the contributions of online optimization, retrievable task information, and permissive oracle landscapes. On PMO at 50 oracle calls, a GPT-4o mini agent's sum AUC falls from 14.44 to 4.85 after task names and curated reference compounds are hidden. An identity-blinded condition that states only the oracle form (e.g., similarity to a hidden reference) scores 5.39, while a deterministic retrieval-only baseline with no LLM reaches 12.16 (84% of the full agent). A full 23-task 2x2 ablation and a three-seed replication on eight tasks support this interpretation. On a protein-targeted benchmark with an AutoDock Vina composite oracle, a single-edit random walk is a strong lower bound; across three seeds it obtains composite 0.636 +/- 0.008 and docking improvement -1.11 +/- 0.04 kcal/mol. As a positive control, a retrieval-free population agent exceeds REINVENT at a matched 50-call AUC budget, with its strongest result at 100 calls. These results motivate two inexpensive sanity checks: retrieval-safe PMO prompts and a random-walk floor for docking-based optimization.

---


### 5. [Subliminal Learning in Vision-Language Models](https://arxiv.org/abs/2611.08538)

**<font color=#1a73e8>作者：</font>** Arman Hatami, Romina Aalishah, Ilya E. Monosov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subliminal learning is a phenomenon in large language models (LLMs) where a teacher passes a hidden preference to a student through training data unrelated to that preference. We study whether subliminal learning also occurs in vision-language models (VLMs). We finetune a teacher VLM to prefer a specific animal or facial attribute and use a control teacher from the same base model. Both teachers generate numbers for an unrelated visual task involving geometric shapes. Two students initialized from the same base VLM are finetuned on the same images, using numbers generated by either the biased or control teacher. Across VLMs ranging from 2B to 7B parameters, we find that both animal and facial preferences can transfer through this unrelated task. Students trained on biased-teacher outputs select the target more often than control students, with a difference of up to $\sim$10 percentage points in the animal preference task. Transfer can become stronger with more training data and varies with the target preference, model, and how the numbers are generated. Beyond preferences, we show that the biased student's explanations use more of the same words and phrases as the biased teacher's explanations than those of the control student, even when all three models select the same image. These results matter for training VLMs and show that training on unrelated data may change both a VLM's image preferences and how it explains its choices, and that transfer can become stronger with more training samples.

---


### 6. [How Small Can We Go? Calibrating Activation-Cache Compression for SAE Training](https://arxiv.org/abs/2611.08551)

**<font color=#1a73e8>作者：</font>** Abraham Yeung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To train a sparse autoencoder (SAE), you need a massive cache of model activations. We look into the effects that compression has on an SAE in two ways: we keep the original fp32-trained SAE and pass the compressed cache into the same SAE to see how many feature activations stay the same (the frozen-SAE test), and we retrain an SAE on the compressed cache and see how many of the original features still exist (the retraining test). We found that in the retraining test, there is no clear scale for retained features. On a GPT-2 cache, rounding everything to fp16 keeps 60.6% of features, but changing one value in a million by the smallest step fp32 allows (a change eight orders of magnitude smaller) keeps only 70.5%. Meanwhile, changing the random seed keeps 23.0%. For the frozen-SAE test, the frozen SAE's correlation with the original increases in order of how precise the codecs are, but plain $L_2$ distance gives nearly the same ordering. We also see the same frozen reading correspond to different percentages retained at different sites. This leaves the question of the right measurement. We build one by calibrating: retraining on identical bytes sets the ceiling, and a reseed sets the floor. We then measure the effect of each compressed codec against its own site's floor. With TopK SAEs on GPT-2 small and Pythia-1.4B at research-scale budgets, naïve per-token int4 loses more features than a reseed everywhere we tested, as do PCA and random projection on GPT-2. Standardizing each channel before quantizing brings int4 back above the floor in terms of retained features, at the same raw file size. At our smallest budget, a bf16 forward pass, which some pipelines use to save memory, loses slightly more features than rotated 8-bit storage. Calibrating a site costs four training runs and two evaluation passes.

---


### 7. [Seeing Is Not Knowing: The Epistemic Limits of LLM-Based Mental Health Inference from Youth Social Media Conversations](https://arxiv.org/abs/2611.08565)

**<font color=#1a73e8>作者：</font>** Xiaohan Ding, Mengting Tu, Andrew H. Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Adolescents increasingly use social media for private conversations, sharing experiences and seeking support. These interactions generate digital traces, prompting efforts to infer mental health and psychosocial states. As large language models become more capable of reasoning about conversations and interpersonal dynamics, a fundamental question remains nonetheless: what can models actually "know" about an individual's psychological experience from what they are able to "see"? We evaluated ten reasoning LLMs using donated Instagram Direct Messages from 80 adolescents with a history of depression or suicidal thoughts and behaviors, comparing predictions with self-reports and analyzing 204 reasoning traces. Models performed better when inferring more observable states than participants' subjective appraisals of social experience, such as perceived social support. Beyond prediction accuracy, our findings highlight the epistemic limits of digital traces for AI design and evaluation: what can be observed, what can reasonably be inferred, and what requires people's own accounts.

---


### 8. [NormGym: Evaluating Normative Competence through Social Interaction](https://arxiv.org/abs/2611.08613)

**<font color=#1a73e8>作者：</font>** Binze Li, Zihuan Zhang, Seokhyun Baek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Normative competence, the ability to infer socially enforced expectations from interaction and adjust behavior accordingly, is essential for agents operating in unfamiliar human communities. Yet existing evaluations largely test whether agents can recognize or apply norms they may already know, rather than whether they can acquire previously unknown norms from social interaction. We introduce NormGym, an interactive benchmark for normative competence in which a newcomer must infer a hidden, arbitrary norm while pursuing its own task in a multi-agent community. Success requires distinguishing what is possible from what is permitted, inferring the norm from observed behavior and sanctions, and applying it in new situations. NormGym contains diverse norms and distinct environments, allowing systematic evaluation of current agents, including large language model (LLM) agents. We find that normative competence remains challenging: the strongest evaluated LLM achieves a joint task-and-compliance success rate of 55.3%. Our analysis reveals that models can sometimes revise their behavior following sanctions for their own actions, but struggle to use other agents' behavior and the sanctions they receive to infer the underlying norm. We further find that fine-tuning models may be insufficient to improve normative competence. These results suggest that current models lack a robust, transferable capability for acquiring normative knowledge through social interaction.

---


### 9. [LLM-Based Feature Extraction for Multi-Criteria Inventory Classification](https://arxiv.org/abs/2611.08626)

**<font color=#1a73e8>作者：</font>** Humza Akhtar, Rami Pinto  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> E-commerce supply chains generate large volumes of customer feedback and operational data that remain underutilized in inventory management. Traditional inventory classification techniques such as ABC analysis rely primarily on annual dollar usage, while multi-criteria inventory classification (MCIC) methods extend this but still depend on structured quantitative data and do not utilize unstructured information available in modern supply chains. This paper proposes an LLM-based feature extraction approach that transforms unstructured sources such as customer reviews into quantitative features using vector embeddings and LLM-generated evaluation criteria. The enriched feature set is incorporated into an MCIC framework based on the Hadi-Vencheh model. Experimental results show measurable reclassification effects when customer sentiment signals are included, demonstrating that integrating unstructured data into MCIC can enhance inventory prioritization.

---


### 10. [Benchmarking Machine Learning for Chaotic Three-Body Dynamics in Astrophysics](https://arxiv.org/abs/2611.08634)

**<font color=#1a73e8>作者：</font>** Sheng Wan, Pavan Vynatheya, Duo Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) and generative AI have recently made impressive progress in understanding physics. We explore a hierarchy of prediction problems stemming from chaotic three-body systems and benchmark existing ML approaches, including general-purpose prediction algorithms and those that build on top of foundational physics models. We first simulate the trajectories of triple systems near the critical boundary of stable/unstable initial conditions. We then design a hierarchy of learning tasks, focusing mainly on two broad problems: stability prediction and trajectory prediction. The former classifies whether a given triple system has diverged or not up to a specific horizon, while the latter predicts the exact trajectory, both given suitable input features. We benchmark a range of ML approaches, from simple regression methods to state-of-the-art foundational physics models, across these tasks, and compare them against astrophysical methods such as the Mardling-Aarseth stability criterion. Our experiments reveal a clear order of task difficulties in chaotic three-body dynamics: early dynamics enable strong stability prediction, while precise long-horizon trajectory forecasting remains difficult. Code and dataset are publicly available at this https URL.

---


### 11. [Forcing a Letter Suppresses Refusal: Mechanistic Evidence from WMDP](https://arxiv.org/abs/2611.08639)

**<font color=#1a73e8>作者：</font>** Stepan Epifantsev, Anna Antipova, Oleg Chernikov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety benchmarks for large language models (LLMs) commonly use multiple-choice question (MCQ) format. However, prior studies documented that MCQ format reduces refusal rates, which may significantly affect the safety behavior of the model. We provide a first mechanistic explanation of this effect on the Weapons of Mass Destruction Proxy (WMDP) dataset across two models - Llama-3.1-8B and Qwen3-8B. First, we use the tuned lens technique to show that when processing MCQ the model commits to an answer-letter token very quickly, which is in contrast to the gradual refusal build-up in open-ended formats. Additionally, we observe that activations on the MCQ format lie roughly 3x further from the refusal direction, compared with their open-ended counterparts. Moreover, ablating the attention heads that carry the MCQ format answer increases the refusal, which is a direct evidence that the MCQ answer-selection competes with refusal. These findings indicate that MCQ safety scores primarily measure knowledge capabilities and do not assess the safety-mechanisms.

---


### 12. [Aspect-wise Pairwise Tournaments for Test-Time Selection](https://arxiv.org/abs/2611.08640)

**<font color=#1a73e8>作者：</font>** Hannah Guan, Yilun Du  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling test-time compute has proven highly effective at improving LLM reasoning. A popular method is best-of-n sampling, where a model generates many candidate solutions and one is selected. This motivates the question: how can we select the best candidate? When humans make choices, we find it more natural to compare two options than judge each in isolation. Additionally, when the options become complex, we like to judge the options one aspect at a time, such as comparing two job candidates on experience, communication, etc. In the test-time setting, candidate solutions should be judged in the same way. Here we introduce Aspect-wise Pairwise Tournaments (APT), which verifies by comparison and compares by aspect. Each matchup of a single elimination tournament is decided by a vote over multiple off-the-shelf aspect verifiers, each expressing a pairwise preference along its own aspect. Across five domains and three generator LLMs, APT improves over binary multi-aspect approval, self-consistency and reward model verification, with the largest gains on open-ended tasks. We find that both components matter; neither binary approval over the same aspects nor a generic pairwise judge at a matched budget matches APT. Because aspects are specified in natural language, APT also lets users steer selection toward properties they care about, better aligning with user preferences without needing to regenerate solutions. No component is trained, so APT transfers to new domains by simply rewriting prompts.

---


### 13. [Decision Context: Persistent Behavioral Learning for AI Agents](https://arxiv.org/abs/2611.08644)

**<font color=#1a73e8>作者：</font>** Nima Vahdat, Pashootan Vaezipoor  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents do not learn from corrections across sessions. A user fixes the same mistake at the start of every conversation. Existing agent memory systems primarily handle facts, such as preferences, entities, and conversational history, rather than procedural knowledge.
We present Forge Decision Context (forge_dc), a system that captures behavioral signals from human corrections and self-assessed tool-call failures, compiles them into imperative RULE directives, and injects them at the decision points where they apply. We evaluate forge_dc alongside four predecessor approaches on DC-Bench, a new benchmark of 71 scenarios across nine behavioral dimensions, built from real executed agent traces in a deterministic mocked-tool environment. forge_dc reaches 95% compliance, up from 55% with naive retrieval, while injecting approximately 10 times fewer tokens per query.
Across the five-stage progression, the strongest systems represent behavioral memory as explicit directives and deliver it at the decision points where it applies. The results identify representation, activation, and placement as central design choices for persistent behavioral learning.

---


### 14. [IWIBench: Evaluating Gradient-Free Model Driven Intra-weight Injection](https://arxiv.org/abs/2611.08647)

**<font color=#1a73e8>作者：</font>** Chris von Csefalvay, Pranav Doma, Achyuthan Unni Krishnan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intra-weight injection lets one model change another model's behaviour by editing its weights directly, without gradients. Such edits can range from altering lexical associations to enforcing output formats or updating factual knowledge. Despite growing interest in these approaches, there has been no systematic way to evaluate how well models perform them. We introduce IWIBench, which measures a large editor model's ability to modify the weights of a smaller target model (typically Gemma 3 4B IT) to achieve one of ten classical text-editing objectives while preserving its other capabilities. Editors are limited to four tools for reading and writing weights, with bounded tensor access and a fixed budget for generating and inspecting rollouts. A validator applies each proposed patch in a clean environment and compares the edited model against the unmodified target. Evaluating frontier closed- and open-weight models reveals sharply diverging capabilities, both across models and across tasks. A small number of models, most notably Astra and GPT-6.1 Sol, perform far ahead of the rest. The recency of this ability (little of it is evident in GPT-5.6 Sol, for instance), together with qualitative analysis, suggests it has been acquired through recent training. Tasks also vary widely: structured response resisted every attempt, and answer-length control yielded only one successful solution, whereas alias acquisition and recoding proved most amenable. Success in one task family correlated poorly with success in others, indicating an early and uneven capability frontier. We discuss strategies that editors repeatedly adopted and conclude with an outlook on intra-weight injection as an emerging but already potent approach to gradient-free behaviour modification.

---


### 15. [VoluCompose: Constructing Compact Volumetric Visual Representations for Medical Image Understanding](https://arxiv.org/abs/2611.08649)

**<font color=#1a73e8>作者：</font>** Zanting Ye, Yunrui Lin, Shengyuan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision--language models can interpret volumetric images, but processing full volumes is costly because hundreds of slices produce long, redundant visual-token sequences. Existing compression methods often couple content selection with budget determination. We observe that neighboring slices share visual features and that attention concentration varies across visual encoders. We propose VoluCompose, a training-free, model-agnostic framework that separates what visual content to retain from how many tokens to allocate. Its hyperbolic token composition module groups contiguous slices into ordered support units and uses the Lorentz distance to account for feature magnitude and direction during token allocation, anchor selection, and refinement. Its capacity control module uses visual-encoder attention entropy to allocate more tokens when attention is more dispersed. We evaluate VoluCompose on two tasks across three datasets and four backbones. Across nine calibrated settings, VoluCompose attains the highest mean quality--retention hypervolume among the compared methods. It achieves a mean relative quality of 121.68\% against the uncompressed references while retaining 22.78% of visual tokens on average. Compression remains robust even at a 10% token budget. Across settings, the lowest ROUGE-L ratio to the uncompressed reference is 96.4\% for VoluCompose. The corresponding minima for the compression baselines range from 15.0% to 70.5%. Code is available at this https URL.

---


### 16. [Turkish Multimodal Video Fact-Checking: A New Dataset and a Comparison of Zero-Shot Agentic and Fine-Tuned Systems](https://arxiv.org/abs/2611.08651)

**<font color=#1a73e8>作者：</font>** Azra Açıl  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-based misinformation spreads rapidly on social media, but almost all existing fact-checking systems focus exclusively on English text. Tools for low-resource languages such as Turkish are severely limited. In this work, we present TeViD (Turkish Video Fact-checking Dataset), to the best of our knowledge the first multimodal video fact-checking dataset for Turkish. We compiled the dataset from articles published by this http URL, an IFCN-certified organisation, and enriched it with translated Snopes articles and synthetic examples to reduce class imbalance. Building on TeViD, we develop two verification pipelines that share the same open-source base model. First, in 3MFact-TR (Pipeline 1), we adapt the multi-role 3MFact framework to Turkish with the Qwen2.5-7B large language model and the Qwen2-VL-7B vision-language model, and add three modules of our own: a semantic inconsistency checker, a 5W1H question manager, and a bilingual evidence retriever that excludes fact-checking sites to prevent leakage. Second, as our Fine-Tuned Model (Pipeline 2), we fine-tune a single Qwen2.5-7B with Low-Rank Adaptation (LoRA) to produce closed-book verdicts from the claim and the video's textual description. We report accuracy, macro F1, True class F1, and True class recall for both systems, together with ablation studies.

---


### 17. [Pdb or Not to Be: Comparing Debugging Interfaces With Pass$_{X}$@$k$](https://arxiv.org/abs/2611.08666)

**<font color=#1a73e8>作者：</font>** Ryan Magnuson, Ellie Kitanidis, Ariel Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive debuggers are indispensable to human software development, yet coding agents overwhelmingly rely on edit-execute-observe loops, using common bash tools, test scripts, and print statements to debug via repeated shell commands. Stepping through a debugger provides live access to runtime state, which may enable different problem-solving capabilities. However, prior work typically introduces the debugger as an additional tool or through a new subagent, making its individual contribution difficult to isolate from the associated scaffold changes. To address this, we compare a debugger-only agent against a bash-only agent on all 500 SWE-bench Verified instances, holding the rest of the scaffold fixed. We evaluate both architectures on two models, GPT-OSS-120B and Nemotron-3-Ultra-550B, with three independent runs per architecture $\times$ model configuration. Crucially, to distinguish interface specialization from expanded coverage under repeated sampling, we introduce pass$_X$@$k$, a cross-agent pass@$k$ that provides an unbiased estimator of the probability that at least one of $k$ agents is successful. Although the bash and debugger agents solve partially disjoint subsets of the benchmark in any single pair of runs, our pass$_X$@$2$ estimator reveals that this is largely due to run-to-run variance rather than tool complementarity. Across both models, we find that two bash rollouts outperform the combination of one bash and one debugger rollout. Our findings highlight the importance of accounting for stochastic variance in evaluating agent and tool diversity, and we hope that pass$_X$@$k$ will serve as a useful framework for the community.

---


### 18. [ChainFlow: Few-Step Latent Flow Matching for Speculative Decoding](https://arxiv.org/abs/2611.08669)

**<font color=#1a73e8>作者：</font>** Selim Aktas, Yusuf Erdem Erdem, Ahmed Zeer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding has become a standard way to accelerate LLM inference: a lightweight drafter proposes tokens that the target verifies in one parallel pass. Existing drafters face trade-offs that limits their speedups: autoregressive drafters generate tokens one at a time, so drafting cost grows with draft length, while diffusion drafters generate tokens in parallel but predict each position independently, ignoring inter-token dependencies. We introduce ChainFlow, a new speculative decoding paradigm and the first flow-matching drafter conditioned on the target's hidden states. ChainFlow treats drafting as a short transport over hidden states, needing one or two flow steps instead of the many denoising steps of generation from noise. A variational autoencoder compresses these states so drafting cost barely grows with target size, lightweight feedback heads restore inter-token dependencies, and tree drafting raises acceptance. On Qwen3.5 models, at matched drafter size and training data, ChainFlow outperforms EAGLE-3 and DFlash in vLLM by 39% and 11%, respectively. These gains further widen as drafters are adapted to new languages sequentially. Our ablations cover drafter design and concurrent serving, and we open-source our code and drafter models.

---


### 19. [Compression of Emotion in Language Model Representations](https://arxiv.org/abs/2611.08683)

**<font color=#1a73e8>作者：</font>** Laya Iyer, Sanmi Koyejo, Chen Shani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been evaluated on their ability to identify emotions expressed in text and produce fluent emotional language. However, output predictions alone do not reveal how fine-grained emotion distinctions are organized internally. We study seven LLMs on GoEmotions, an English Reddit dataset annotated with 27 fine-grained emotion categories plus neutral. We compare model predictions and emotion-prompted final-token representations with the 28 GoEmotions categories and with coarser emotion-family and sentiment groupings.
We find a consistent pattern of $\textit{overcompression}$ relative to the fine-grained GoEmotions taxonomy. Under the tested KMeans protocol, when we cluster their hidden representations without using emotion labels, the clearest split is into two groups that largely separate positive from negative emotion. Coarser emotion groupings are also recovered with fewer clusters than the full 28-category taxonomy. Yet linear probes retain substantial fine-grained predictive information. These results suggest that fine-grained emotion information remains accessible even though broader affective structure more strongly organizes the unsupervised geometry.

---


### 20. [Cancellation Is Not Enough: What Retries Leave Behind in an Overloaded LLM Engine](https://arxiv.org/abs/2611.08684)

**<font color=#1a73e8>作者：</font>** Xindan Zhang, Fei Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clients and proxies in front of an LLM engine retry calls that time out. After a transient overload, these retries can keep the engine from recovering even when calls arrive below its capacity. Since the engine may keep computing for clients that have left, propagating cancellation looks like the natural remedy. In this paper, we test it on vLLM with overload experiments on three open models, and with scheduler traces of one that follow each client attempt to the execution it creates in the engine. We find that with retries on, cancellation alone did not restore service in any run, and only 12-38% of the calls that arrived after the overload were delivered. The traces suggest why: retries that vLLM ran typically started prefill less than half a second before they timed out. Executions that vLLM later aborted took 79-85% of the prompt tokens it computed, and vLLM's prompt-token counter missed a third to half of all computed prompt tokens. A retry budget restored service by shedding retries but left many of the overload's calls undelivered. Request coalescing delivered every call from the overload onward, some late, unless cancellation had already aborted the running execution. Overload controls should thus be judged by the executions that retries add and the calls that clients receive.

---


### 21. [Dual-Stream LLM-Guided Reward Design for Reject-Inference-Aware Reinforcement Learning in E-Commerce Payment Fraud Detection](https://arxiv.org/abs/2611.08706)

**<font color=#1a73e8>作者：</font>** Bo Qu, Zhurong Wang, Frank Zahradnik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Production fraud-detection models learn from a censored slice of their own traffic: transactions a legacy system blocked never receive fraud labels, so models train on a biased, approved-only distribution. We extend LLM-guided reward design, the framework of Qu et al. (2025) in which an LLM evolves the reward of a two-step REINFORCE fraud-blocking policy, to attack this reject-inference problem inside the reward. A single LLM designs a dual-stream reward: stream 1 applies the standard dollar-weighted precision objective to labeled transactions; stream 2 scores legacy-blocked, unlabeled transactions by contrasting the newest gradient-boosted risk signal against the legacy scores that drove the original block. Rather than prescribe which signals matter, we expose a superset of evidence and let the LLM decide for itself which to use, guided by evaluation feedback alone; because it writes the reward as code, that choice is directly auditable. On a held-out four-month out-of-time test, the dual-stream agent beats the prior labeled-only agent at every target recall, by +4.7, +2.4 and +3.0 points of dollar-weighted precision at 80%, 85% and 90% recall, and the production baseline by +6.8 points on average. The resulting policy is architecturally identical to that of Qu et al. (2025) and adds no inference cost.

---


### 22. [RL-ATTACK: A Generalized Black-Box Adversarial Attack on Language Models via Reinforcement Learning](https://arxiv.org/abs/2611.08711)

**<font color=#1a73e8>作者：</font>** Taikun Chen, Yue Zhang, Wei Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit vulnerabilities to adversarial perturbations that can induce unintended responses. These vulnerabilities can be identified via intentional attacks and subsequently used to improve model safety. In black-box settings where gradients are inaccessible, existing methods tend to guess adversarial transformations using external knowledge, ignoring the information provided by the target model. To mitigate this, we propose a trainable black-box framework based on reinforcement learning, which learns from the target model to generate tailored adversarial transformations. We demonstrate that our approach achieves lower post-attack accuracy, greater query efficiency and better semantic preservation on both natural language inference and generative Q&A tasks. On natural language inference, it drives post-attack accuracy to 2% within 20 queries. Against generative language models, our trained attacker consistently achieves lower post-attack accuracy than the untrained attacker and wins in 4 out of 6 settings when compared to a strong optimization-based baseline. We further experiment with multiple reward designs and training settings, and we find that no design or setting is consistently dominant. Our code is available at this https URL.

---


### 23. [Patching the Blind Spots: Reversible LLM Rule Overlay for Frozen Fraud Detectors](https://arxiv.org/abs/2611.08714)

**<font color=#1a73e8>作者：</font>** Bo Qu, Zhurong Wang, Frank Zahradnik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In industrial tabular fraud classification, gradient-boosted trees remain state-of-the-art, but even a well-trained model has blind spots, and retraining the deployed model is not always safe. We propose a framework that patches such a model without modifying it: LLMs propose rules anchored on features the model underweights by SHAP, and the resulting noisy pool is screened for empirical support and calibrated into an additive, reversible log-lift overlay that runs at the production cut-off. Single-LLM benefit is high-variance and inverts between datasets, so we pool three diverse backbones by equal-weight logit averaging, trading peak gain for a bounded worst case. On a real-world e-commerce fraud detector trained on selection-biased data, continued training regresses even when carefully tuned, whereas the overlay gains on average +2.26% recall at equal precision ($\Delta$R@P) and +1.60% precision at equal recall ($\Delta$P@R) over production cut-offs spanning 30-57% precision and 23-63% recall. On a public benchmark of seven designed bias-shift variants it raises $\Delta$P@R on every variant and keeps $\Delta$R@P near neutral. Each amendment is a readable predicate naming the fraud pattern it covers.

---


### 24. [Memory-Aware Multi-Agent Architecture with LLM-based Orchestration for Conversational Recommendation](https://arxiv.org/abs/2611.08718)

**<font color=#1a73e8>作者：</font>** Emilly Pitman de Castro, Vanessa Silva, Gustavo Kanno 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational recommender systems often treat user sessions in isolation, limiting their ability to capture how user intent evolves over time. While large language models (LLMs) have improved semantic understanding, they are typically used as isolated components, without addressing how memory, retrieval, and decision-making should be integrated at the system level. In this work, we propose a memory-aware multi-agent architecture for conversational recommendation, in which LLMs act as orchestration layers that coordinate intent refinement, query construction, and interaction flow. A key design principle is the integration of long-term memory as a first-class component, influencing both routing decisions and semantic query formation. We evaluate the system through cross-session memory experiments, multi-turn conversational simulations, and supervisor-driven interaction studies on the Amazon Reviews dataset. Results show that memory-enabled interactions recover up to 63\% of the gap toward explicit-query scenarios and prevent semantic degradation in extended dialogues. In addition, supervisory orchestration increases user acceptance by +28.9 percentage points, highlighting the importance of structured orchestration in guiding interaction and output quality. We also observe an exposure bottleneck between retrieved candidates and displayed recommendations. While LLM-reranking does not improve Hit@K, it consistently enhances semantic consistency and diversity. To capture these effects, we introduce the Semantic Consistency Score (SCS), a complementary evaluation measure. Overall, the results emphasize the importance of system-level design choices, suggesting that effective conversational recommendation benefits from explicit memory integration, orchestration, and evaluation beyond traditional ranking metrics.

---


### 25. [Divide, Diagnose, and Compose: Optimizing Agentic Pipelines and Harnesses](https://arxiv.org/abs/2611.08723)

**<font color=#1a73e8>作者：</font>** Divij Handa, Christopher Tensmeyer, Jihyung Kil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Building agentic pipelines that achieve high task performance while keeping cost and latency low requires jointly optimizing heterogeneous and coupled design choices, including prompts, topology, model selection, and tool policies. Manually searching this combinatorial design space is expensive and time-consuming, while existing automated optimizers typically operate within a predefined subset of this space, modify the pipeline monolithically, or provide little structured evidence for pipeline changes. To mitigate these challenges, we introduce the Decomposed Credit-Assignment Framework (DeCAF), which adapts the design space to the given benchmark and pipeline, optimizes each dimension separately, and generates reasoning traces for every decision. Given a task specification, benchmark examples, and a seed pipeline, DeCAF identifies relevant optimization dimensions and generates diverse experimental hypotheses for each. Independent coding-agent sessions then optimize each dimension under a restricted edit scope, jointly evaluating performance, inference cost, and latency while recording all hypotheses, edits, and outcomes of each experiment. A final synthesis session combines compatible findings across all dimensions and uses a component-level trajectory evaluator, which derives role-specific rubrics from each agent's instructions, to localize underperforming components and guide cross-dimension revisions. Across a diverse suite of agentic benchmarks, DeCAF improves average task performance by 2.58 percentage points, while reducing inference cost by 4.30% and end-to-end latency by 42.45% compared to the best overall baseline.

---


### 26. [Structuring Survey Histories for LLM Digital Twins: A Controlled Study of Background, Decision Procedure, and Evaluation Profiles](https://arxiv.org/abs/2611.08730)

**<font color=#1a73e8>作者：</font>** Iris Ye, Tianze Deng, Ozan Candogan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based digital twins aim to predict how individuals would respond in new settings from representations of their prior responses. Existing evidence that compression of survey histories need not reduce predictive accuracy suggests that representation structure, rather than information volume alone, may be an important design choice. We study BDE, a fixed representation that organizes each respondent's survey history into Background, Decision procedure, and Evaluation. We evaluate it on Twin-2K-500 (Toubia et al., 2025) by predicting each respondent's held-out answers on 17 tasks. In a paired evaluation with 100 respondents, a fully inferred BDE profile improves overall accuracy over the raw survey transcript by 1.27 percentage points (pp) on gpt-5.4-nano (p < 0.01) and 1.19 pp on gpt-5.4-mini (p < 0.001). Three analyses then examine the schema, extraction depth, and component composition. Against a length-matched free-form profile written from the same transcript by the same extractor, BDE improves pricing accuracy on both simulators (2.15 pp on nano, p < 0.01; 1.38 pp on mini, p < 0.05), while its overall advantage is significant only on nano (1.05 pp, p < 0.05). Allowing deeper inference during extraction yields no statistically significant gain on either simulator. By contrast, adding Evaluation to a Background--Decision procedure profile improves overall accuracy by 1.44 pp on nano (p < 0.001) and 1.22 pp on mini (p < 0.001). These results indicate that the advantage over raw transcripts is not explained by compression or length alone, and attribute it primarily to profile composition rather than deeper extraction.

---


### 27. [AlterNet: Adaptive-Depth Mixture-of-Experts with Learned Halting for Elastic Inference](https://arxiv.org/abs/2611.08741)

**<font color=#1a73e8>作者：</font>** Alexander Kastius  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most LLM architectures have fixed compute demands determined at training time. We propose a novel architecture that combines the Mixture-of-Experts architecture with shallow experts and a novel dynamic-depth system to make the extent of a forward pass dynamically adjustable. Our approach lets the model automatically determine the compute needed for a given task, paired with a system to scale it down after training without retraining when the execution environment demands faster or cheaper inference. To achieve this, we introduce an iterative computation mechanism, sequence-level depth-based routing steered by a halting mechanism within the experts, a depth encoding that lets the model track its progress in the chain, and a regularization mechanism that incentivizes the model to use allocated compute efficiently. We present initial benchmarks and discuss future research directions.

---


### 28. [AtariBench: Evaluating Spatiotemporal Reasoning of Vision-Language Models in Atari Gameplay](https://arxiv.org/abs/2611.08755)

**<font color=#1a73e8>作者：</font>** Mingjia Huo, Yao Fu, Bo Chang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have achieved strong performance on static visual understanding benchmarks, yet their ability to act in dynamic environments remains less well understood. We introduce AtariBench, a controlled benchmark that evaluates VLMs across 20 Atari 2600 games, requiring models to make sequential decisions from high-temporal-resolution gameplay streams. By decoupling fast in-game dynamics from wall-clock inference speed, AtariBench focuses on whether models can perceive rapid visual state changes, reason over spatiotemporal dynamics, and ground actions in the current observation. Our experiments reveal substantial limitations in state-of-the-art VLMs: models often fail to infer object motion and direction, exhibit brittle sequential decision-making, and over-rely on textual interaction history despite newly appended visual feedback. We further introduce a separability analysis to identify which in-game scores provide reliable signals of model competence, and use the benchmark to study how memory design and prompting strategies affect performance. Overall, AtariBench exposes a persistent gap between passive visual perception and active decision-making, providing a lightweight and rigorous testbed for developing VLMs that can reason and act in dynamic environments.

---


### 29. [Conflux: Preventing Privilege Escalation with Principal Contexts and System-Level Evaluation](https://arxiv.org/abs/2611.08768)

**<font color=#1a73e8>作者：</font>** Raya Buckley, Christian Schroeder de Witt  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents combine information from multiple principals while acting externally. We formalise privilege escalation (PE) as the system-level security objective: an action may proceed only if every principal that influenced it would allow it. Model-level defences remain probabilistic, so enforcement must sit outside model judgement. We present Conflux, a principal-context defence. Its kernel, ITES, derives authority from provenance and the organisation's existing access-control system and intersects the permissions of every influencing principal. We prove a conditional authority-confinement theorem: under complete mediation, no-laundering provenance, a known non-empty decision context, fresh permission checks, and action binding, the kernel admits no action that escalates privilege with respect to any recorded influencing principal. The theorem covers the represented value-influence fragment; control influence from tool, branch, recipient, or plan-step selection remains a refinement obligation. Conflux extends the kernel with independent policy ports, argument-aware authorisation, disclosure, consent, delegation, restriction, and exposure planning. We describe two system- level evaluators. SLED is a black-box evaluator: it exhaustively explores a declared finite model of a defence up to a bound. SLED-V is a white-box evaluator: it checks a serialisable intermediate representation against security and provenance properties. The evidence is bounded and partial. The appendix reports retained AgentDojo, SLED, and SLED-V results, including the limits of those runs. No result in this paper is an unbounded deployment guarantee.

---


### 30. [Jacobian-Causal Memory Control for Persistent Memory in Language Model Systems](https://arxiv.org/abs/2611.08779)

**<font color=#1a73e8>作者：</font>** Marvin Danig  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent-memory systems choose not only which records are retrieved but which prior information can alter current inference. We propose Jacobian-causal memory control (JCMC), which represents each authorized memory intervention by a predicted influence signature in a shared behavioral measurement space, selects interventions against a target effect and side-effect budget, and compares predicted with observed effects before retaining or rolling back the intervention. Under explicit smoothness and bounded-estimation assumptions, we prove a quadratic local-approximation bound, characterize the target effects reachable by a set of signatures, bound selection regret under signature error, and bound non-additive interactions between simultaneous memories. The paper reports no benchmark measurements; it defines a paired counterfactual estimator and an evaluation protocol comparing JCMC with relevance, graph, and policy-filtered retrieval baselines. The central claim is narrowed or falsified if those simpler baselines match effect targeting, side-effect control, and rollback utility under equal model, memory, policy, and cost budgets.

---


### 31. [Learning from How Users Interpret: Personalizing Recommendation Explanation Order](https://arxiv.org/abs/2611.08785)

**<font color=#1a73e8>作者：</font>** Deo Munduku, Elsa Negre  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Personalized explanations typically adapt their content or presentation based on preferences, interaction histories, or other user characteristics. We examine whether regularities inferred from prior textual interpretations can support personalization of explanation organization. In a controlled within participant study with 122 participants, prior interpretations were represented along three dimensions: information selection, relative salience, and relational organization. The relational dimension was partially operationalized through co mobilization. These representations were aggregated into fixed historical profiles and used to organize otherwise identical explanation sentences. Participants encountered four organization procedures: the OWN historical profile, the DONOR historical profile, a population profile called POP, and a language model procedure using the historical profile called PROFILE LLM. Post exposure objective comprehension was the primary outcome. OWN achieved 86.5 percent correct responses, compared with 66.0 percent for DONOR, 63.9 percent for POP, and 73.0 percent for PROFILE LLM. Mixed effects analyses showed higher comprehension with OWN than with each alternative procedure. No reliable overall condition effect was detected for recommendation acceptance. These findings indicate that historical profiles derived from prior interpretations can provide an actionable signal for personalizing explanation order while keeping explanatory content and wording fixed.

---


### 32. [MotionDecipher: LLM-Assisted Clinical Interpretation of Human Motion Signals for Efficient Gait Analysis](https://arxiv.org/abs/2611.08795)

**<font color=#1a73e8>作者：</font>** Mingrui Ma, Tian Tan, Jinsi Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Clinical gait and motion analysis is widely used to guide targeted interventions for patients with neurological disorders, the outcome of which is typically a report with descriptions of joint movements and forces. Current practices rely on experts' manual effort, which is labor-intensive and time-consuming. Recent advancements in Large Language Models (LLMs) provide opportunities to address this problem, but translating human motion into clinical gait descriptions remains challenging because the quality of the context directly affects LLMs' reasoning capability over continuous motion signals. To tackle this, we introduce MotionDecipher, a novel framework bridging the semantic gap between motion data and clinical interpretations. Specifically, we made 3 key advancements: 1) a Human Motion Tokenizer that converts motion signals into domain-specific tokens for time- and frequency-informed gait interpretation; 2) a Meta Feature Selector that transforms tokens into Structured Representations; and 3) a Hybrid Context Constructor to determine the optimal demonstration-based prompt for In-Context Learning. We evaluated MotionDecipher on data collected at an accredited gait lab from 122 patients and 46 controls. Results show that MotionDecipher achieves 0.91 BERTScore (13% over GPT-5), while expert evaluation ranks MotionDecipher highest in Correctness, Completeness, and Conciseness compared to baselines, highlighting its promise for efficient gait analysis.

---


### 33. [On the Few-Shot Adaptation of Vision-Language Models: A Few Gradient Signs Are All You Need](https://arxiv.org/abs/2611.08800)

**<font color=#1a73e8>作者：</font>** Nairouz Mrabah, Ismail Ben Ayed, Mahdi S. Hosseini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The limited supervision available for the few-shot adaptation of vision-language models makes gradient estimation particularly noisy. We find that the gradient magnitudes are severely miscalibrated, while the signs of a small top-magnitude subset remain informative. This motivates SignSparseSGD and DynSignSparseSGD, two state-free optimizers that use gradient magnitudes only to select where to update and fixed-magnitude signs to decide how to update. The static variant fixes the support after the first minibatch. The dynamic variant refreshes it at every step. Across 11 datasets, three CLIP backbones, and five shot levels, the proposed methods are competitive with or outperform parameter-efficient and optimization-based baselines on average, while exhibiting markedly lower sensitivity to long training schedules. They introduce no task-specific modules, maintain no first- or second-moment optimizer states, and use one shared configuration across datasets, backbones, and shot levels. Our code is included in the supplementary materials and will be released upon publication.

---


### 34. [I Think, Therefore I Attack: Evaluating Thought Injection Attacks on Reasoning Agents](https://arxiv.org/abs/2611.08811)

**<font color=#1a73e8>作者：</font>** Parth Illendula, Garik Livingston, Zain Shamsi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) are one of the key components of current agentic systems. LRMs augment their output with an explicit chain-of-thought reasoning stage, introducing a new attack surface for thought injection, in which untrusted text resembling the model's own deliberation is fed back to the model. We present a two-part study of this attack, performed against the prevailing large, production class open-weight models (e.g., GLM-5.3, MiniMax-M2.5, Qwen3.8-Flash-Next). We first evaluate the effectiveness of static thought-injection prompts under different styles as well as tagged and untagged conditions and find that the effects of thinking tags and payload styles are all properties of the specific target model. In the second study, we exploit this model-specificity in a containerized agentic cyber range, using indirect injection prompts styled in the form of the target model's own reasoning traces to achieve attack success rates (ASR) up to 50% on operational objectives such as reverse-shell exfiltration and repository backdooring. We also find that the same malicious objective in standard prompt injection user voice never succeeds, and thinking tags suppress the agent's tendency to disclose the injection. Our results show that imitating a reasoning model's own thought style is effective for this style of attack, and that tag stripping is an unreliable defense.

---


### 35. [What Matters for LLM Persona Simulation: Signal Form in Cold-Start E-Commerce Advertising](https://arxiv.org/abs/2611.08840)

**<font color=#1a73e8>作者：</font>** Jiwoo Choi, In Ik Lee, Woo Sung Seo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating advertising performance in cold-start settings is challenging because historical logs are unavailable before launch. Large language models (LLMs) offer a potential alternative by simulating persona-conditioned user responses, but it remains unclear which design choices actually drive LLM-based persona simulation. Using real Google Ads e-commerce campaign data across five demographic segments, we identify three signal-form dimensions that affect simulation quality: (i) a demographic anchor without noisy rich attributes, (ii) a relative qualitative banner-blindness signal rather than quantitative anchors, and (iii) prompt phrasing. On this campaign, our method attains an MAE of 24.9 and a MAPE of 26.1%, a 51.3% lower MAE than the best tested non-LLM baseline and 77.3% lower than an LLM configuration using explicit CTR anchors. Systematic ablations show that minimal demographic descriptions achieve lower mean error than richer persona configurations, while relative qualitative cues substantially outperform the tested quantitative anchors. We additionally compare these configurations with direct-prior and rule-based baselines and with alternative LLM configurations.

---


### 36. [When F1 Is Not Enough: Auditing Codebooks for LLM-Assisted Annotation](https://arxiv.org/abs/2611.08846)

**<font color=#1a73e8>作者：</font>** Yuehong Cassandra Tai, Qunhua Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for text annotation in social science, but standard performance metrics do not explain why errors occur. Low F1 may reflect limitations of the annotation system, defects in the written codebook, or inconsistency in reference labels. We propose a pre-deployment codebook audit for LLM-assisted annotation. The audit uses class-specific metrics and confusion matrices to identify problematic classes and boundaries, structured document-level review to attribute error sources, and targeted codebook revision followed by held-out evaluation. We apply the audit to two published multi-class codebooks from distinct domains. In both applications, the audit identifies under-specified or conflicting coding rules, and targeted revisions reduce the diagnosed errors on held-out data. Analyses with two LLM annotators show that some problematic boundaries and codebook revisions transfer across models, whereas other revision effects are annotator-specific. The results show that LLM annotation errors can help identify weaknesses in the written measurement instrument, not only in the model. Codebook auditing complements prompting, retrieval, and fine-tuning by clarifying whether persistent errors call for model improvement, codebook revision, or renewed scrutiny of reference labels.

---


### 37. ["I had nobody to turn to": Why LGBTQ+ People Choose (Not) to Use AI Chatbots for Personal Health and Relationship Advice](https://arxiv.org/abs/2611.08854)

**<font color=#1a73e8>作者：</font>** Jacob Hobbs, Ashray Gupta, Dennis Ulmer 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While there is an abundance of research into large language model (LLM) biases against LGBTQ+ communities, far less research has examined how and why LGBTQ+ people choose to make use of AI chatbots. In this work, we examine how LGBTQ+ people choose (not) to use AI chatbots across three domains in which LGBTQ+ users have unique needs: relationship support, mental health support, and gender or sexual health support. We surveyed 73 people (60 LGBTQ+; 13 non-LGBTQ+) on how they interact with AI chatbots and find that participants' access to external resources, privacy concerns, and perceptions of chatbot capabilities shape whether and how they choose to make use of AI chatbots. For instance, some LGBTQ+ participants felt that chatbots might actually be less biased against LGBTQ+ people than the people they know offline. We also find that LGBTQ+ participants report using AI chatbots less frequently than non-LGBTQ+ participants across 15 specific personal health and relationship advice scenarios, citing concerns about AI sycophancy and adverse cognitive side-effects. Recognizing AI chatbots as vital (albeit imperfect) resources for LGBTQ+ people, we recommend researchers consider systemic issues that drive users to AI chatbots and design technologies (AI or otherwise) that prioritize privacy, anonymity, and real human connection.

---


### 38. [Learning Whom to Trust About the Unseen: Source Credibility and Reliability Transfer in Language Models](https://arxiv.org/abs/2611.08855)

**<font color=#1a73e8>作者：</font>** Ruijia Guan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A source who has been right before deserves attention, but about what? We ask how far a demonstrated record of reliability travels in language models when the new claim cannot be checked, and whether the answer depends on the kind of claim. Three behavioral studies across six models approach the question from three angles. Study 1 adapts the Einstein-effect paradigm and finds that models, unlike the human sample, favor a spiritual leader over a scientist for the same obscure statement, and that the preference largely reverses when the statement is reworded in the vocabulary of physics. Study 2 adapts a paradigm in which a trusted expert calls a scientific or religious explanation unknown or a mystery; models reproduce the human domain asymmetry in exaggerated form. Study 3, the central test, gives two fictional informants different records on checkable river forecasts and then has them endorse matched claims about hidden natural and spiritual causes of the same village events. Most models carry the record to natural causes and barely at all to spiritual ones; one model transfers it weakly to either. Telling the model that the reliable informant forecasts by spiritual guidance rather than by measurement lowers that informant's influence on natural claims in every model and produces no comparable gain on spiritual claims in any. Demonstrated reliability thus has a scope in these models, and the account a source gives of how they came to be reliable can narrow it. Whether this reflects a judgment about relevance or the low prior credence of spiritual claims is the question the design leaves open, and we outline the experiment that would settle it.

---


### 39. [Mind the Divergence: Divergence-Guided Reliability-Aware Fusion and Adaptive LLM Prompting for Conversational Emotion Recognition](https://arxiv.org/abs/2611.08860)

**<font color=#1a73e8>作者：</font>** Jingwen Wang, Jiao Li, Yuhang Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal emotion recognition in conversations (MERC) integrates textual, acoustic, and visual cues to identify utterance-level emotions. However, existing approaches generally do not explicitly adapt multimodal processing to the degree of inter-modal predictive disagreement. In real conversations, semantic incongruity, concealed emotion, noisy observations, and ambiguity can affect modality-specific emotional evidence differently, while the reliability of individual modalities varies across samples. Rather than identifying each source of inconsistency separately, we model their common consequence for emotion recognition as predictive disagreement among unimodal emotion distributions over the same emotion-label set. Such disagreement makes indiscriminate fusion prone to propagating unreliable or competing evidence. Inspired by the Brunswik Lens Model, we propose MiD-ERC, a divergence-centric framework that quantifies inter-modal predictive disagreement using a normalized divergence score and estimates sample-specific modality reliability. MiD-ERC uses these signals to coordinate divergence-guided cross-modal gating, divergence-modulated reliability weighting, and divergence-conditioned adaptive LLM prompting. The framework is trained end-to-end using only standard emotion annotations, without requiring additional conflict labels, auxiliary data construction, or external retrieval modules. Experiments on IEMOCAP and MELD demonstrate that MiD-ERC achieves state-of-the-art performance, with particularly pronounced improvements on high-divergence samples.

---


### 40. [Reconstructing LLM Lineage Trees via Fine-Tuning Path Inference](https://arxiv.org/abs/2611.08866)

**<font color=#1a73e8>作者：</font>** Sota Ogawa, Shojiro Yamabe, Daiki Nishiyama 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuned (FT) derivatives of large language models (LLMs) are now released in large numbers, yet their provenance relies on self-reports and cannot be verified. Misattributed lineage leaves a verifier unable to audit outsourced fine-tuning, confirm license compliance of derived models, or trace vulnerabilities that a parent passes to its children. All three require the direction of derivation, not merely its presence. Existing output-only methods are limited to pairwise derivation tests or undirected lineage estimation, while recovering a directed tree requires white-box access to model weights. We formalize the problem of reconstructing a directed model tree, including internal nodes, under gray-box access, where only teacher-forced log-likelihoods are observed and weights are never inspected. Fine-tuning raises the log-likelihood of the training data, and a child inherits this increase from its parent. Building on this property, we define an asymmetric per-task log-likelihood deviation between any two models as a trace of fine-tuning history, and derive from it an edge weight for each ordered pair of models. We propose TRACE-Edge, which exactly solves for the maximum spanning directed tree under these edge weights, with neither hyperparameters nor tree-structure constraints. We evaluate it on five configurations totaling 25 model trees built from three base models and seven tasks. TRACE-Edge achieves a parent-match accuracy of 0.74 when probed with the fine-tuning examples, and on average outperforms an output-similarity baseline even with held-out probes drawn from the same distribution as the training data.

---


### 41. [GeoJeV: Unified Spatial Probability for Training-Free Efficient Evidence Acquisition in Ultra-High-Resolution Remote Sensing](https://arxiv.org/abs/2611.08879)

**<font color=#1a73e8>作者：</font>** Xinyi Niu, Lingfeng Chen, Jiehua Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultra-high-resolution (UHR) remote sensing imagery provides rich spatial details but poses challenges for accurate and efficient multimodal understanding. Existing evidence acquisition methods selectively explore relevant image regions, yet largely rely on generative multimodal large language models (MLLMs) for intermediate search control. However, reinforcement learning from human feedback (RLHF) primarily aligns these models with human-preferred responses rather than explicitly optimizing region-level relevance judgments, while repeated autoregressive decoding introduces additional computational overhead. To address these limitations, we propose GeoJeV, a training-free method that formulates evidence acquisition as spatial probability-driven decision making. At each evaluated region, a frozen JeV model produces a probability distribution over candidate regions. Specifically, Region Rank prioritizes candidate regions, Sparse Branch adaptively determines branching width through sparse probability support, and Depth Gate controls refinement depth based on branch sparsity and distribution concentration. By coordinating search priority, branching width, and refinement depth through a shared distribution, GeoJeV reduces reliance on RLHF-aligned generation and eliminates intermediate decoding. Experiments on LRS-GRO, MME-RealWorld-RS, and LRS-VQA achieve accuracies of 60.59%, 52.79%, and 34.32%, respectively. Across the three benchmarks, GeoJeV improves the average accuracy of Qwen3-VL-8B by +5.32pp with only 1.12 additional seconds per question, while achieving a 7.8-fold inference speedup over the recent method.

---


### 42. [Richness Is Not Evenness: Ordered Renyi Crossings under Self-Training](https://arxiv.org/abs/2611.08892)

**<font color=#1a73e8>作者：</font>** Pranjal Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recursive self-training of language models, a setting studied in model collapse, can reduce vocabulary while making frequent words, mostly function words, less dominant. We fine-tune English GPT-2 on its own output for nine generations, vary the training-data sampling temperature, and measure every model with one fixed sampler. As training temperature rises, Renyi entropy changes turn from loss to gain at distinct temperatures: min-entropy first, then collision entropy, Shannon entropy and observed richness. Between the outer crossings, word types fall while the most-common word becomes less dominant. Untruncated training at T = 1 lies in this interval: at 13,000 words, generation 9 has 24% fewer types than generation 0 yet collision entropy is 0.91 bits higher. The ordering persists with a finer grid, different measurement samplers, a fixed word budget and five fresh training seeds. Min-entropy again crosses before richness in four further settings (in Hindi only at interpolated roots) and in 12 of 13 distinct measurements under eight text representations. Next-token identities and a categorical simulation isolate decoding and sampling effects; the crossing order remains empirical. Fine-tuning on human text can produce the same split while likelihood improves, and no single order's sign reliably identifies worse likelihood across the tested settings. We recommend reporting entropy profiles at stated budgets with an independent quality measure.

---


### 43. [From Procedures to Permissions: Learning Precise Subagent Authorization from Agent Skills](https://arxiv.org/abs/2611.08905)

**<font color=#1a73e8>作者：</font>** Wenkai Yu, Ning Ding, Wentao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As language agents tackle increasingly complex tasks, they increasingly rely on multiple agents to coordinate specialized work, requiring decisions not only about what each subagent should do but also which tools and workspace resources it should access. Existing agent systems provide mechanisms for controlling tools and execution environments, but do not directly specify the resources required by each delegated subtask. Moreover, task outcomes and execution trajectories alone provide limited supervision for determining whether a subagent has received appropriate permissions. We observe that Agent Skills encode procedural knowledge describing the operations, tools, and files required at each step, providing a natural source of supervision for authorization. Building on this observation, we synthesize tasks and step-by-step procedures from Skills, execute them through subagent delegation in interactive environments, and use verified trajectories to construct training data for task execution and authorization. On ClawArena-Team, our method improves tool permission precision by 13.4 percentage points and workspace permission precision by 24.1 percentage points, while increasing overall task success by 11.6 percentage points for Qwen3.5-35B-A3B. On Terminal-Bench 2.1 and SkillsBench, our method remains competitive with existing agent data synthesis approaches. These results show that the procedural knowledge embedded in Agent Skills provides a source of supervision for precise subagent orchestration that task outcomes alone cannot provide.

---


### 44. [Toward LLM Self-Play Under Data Scarcity: Effectiveness, Generalizability, and Trustworthiness](https://arxiv.org/abs/2611.08908)

**<font color=#1a73e8>作者：</font>** Zhiyin Yu, Yuchen Mou, Bingzhe Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid development of large language models (LLMs) has been driven largely by scaling model size and human-curated training data, yet this paradigm is increasingly constrained by data scarcity and diminishing returns from human supervision. Self-play offers a promising pathway for autonomous data generation and improvement, but current frameworks remain unsatisfactory due to a lack of a data-centric perspective, limited cross-domain generalization, and growing trustworthiness and security concerns. In this paper, we argue that real-world LLM self-play systems should achieve effectiveness, generalizability, and trustworthiness under data scarcity. To address these challenges, we outline three blue-sky research directions for future self-play systems: (1) data-centric self-play for effective experience generation, (2) generalizable self-play for open-world and unverifiable tasks, and (3) trustworthy self-play for reliable self-evolution. We further discuss research opportunities and solutions within each direction. This paradigm shift will establish a sustainable and safe AI ecosystem by transforming finite human knowledge into inexhaustible high-quality experience through self-play architectures.

---


### 45. [Frame: Form-Restricted Authoring with Model-Based Evaluation](https://arxiv.org/abs/2611.08921)

**<font color=#1a73e8>作者：</font>** Nan Jiang, Mohammed Mohsin Hussain, Onkar Tiwari 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many professional reports reuse the structure of prior editions while updating the content. We formalize this setting as form-restricted report generation: given a sample report and new grounding documents, generate a report that preserves the sample's form while accurately reflecting the new evidence. We introduce FRAME, a benchmark of 120 EDGAR- and arXiv-derived instances across Financial Quarterly, Financial Annual, Academic Simple, and Academic Complex categories, built with a temporal three-snapshot pipeline. We evaluate outputs with three human-validated metrics: structural similarity via semantic tree-edit distance, coverage via information unit recall, and faithfulness via claim-level grounding verification. Across five LLMs, open-source models nearly match proprietary models on structure but lag on coverage and faithfulness; all models perform better on financial than academic reports, and performance declines with longer outputs and more complex grounding.

---


### 46. [ResQAdam: Residual-Preserving Adaptive Optimization for Memory-Efficient Quantization Aware Training](https://arxiv.org/abs/2611.08924)

**<font color=#1a73e8>作者：</font>** Liqun Ma, Shengkun Tang, Liangyu Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization-aware training (QAT) is the most reliable way to obtain accurate low-bit large language models (LLMs), but training with AdamW keeps two dense FP32 states for every weight matrix. We find that low-rank memory-efficient optimizers such as GaLore and LDAdam degrade substantially in QAT. A considerable part of the QAT momentum lies outside its top-r singular subspace, and projection-based methods discard this part at every step. We further observe that this residual remains useful when only its sign is kept. Based on these observations, we propose ResQAdam. It keeps a single BF16 momentum, applies Adam only to the r x r coordinates of the principal subspace, and adds a normalized sign update computed from the residual. We evaluate ResQAdam with two from-scratch QAT methods and three QAT fine-tuning pipelines, with weights quantized down to 2 bits. It reduces optimizer-state memory by 71% to 74% relative to AdamW, stays close to AdamW in most settings, and lowers training throughput by less than 2%.

---


### 47. [ODD+LLM: Specifying LLM-Agent Behavior for Reproducible Social Simulation](https://arxiv.org/abs/2611.08932)

**<font color=#1a73e8>作者：</font>** Justin Downes, Robby Milletich, Newel Hirst  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The ODD protocol is the de facto standard for describing agent-based models, but it lacks vocabulary for the components that determine LLM-agent behavior: prompt assembly, memory serialization, parsing, and retry logic. We propose ODD+LLM, a backward-compatible extension adding five documentation blocks grounded in the CoALA cognitive-architecture framework. To show that the gap matters, we conduct a multiverse analysis [Steegen et al., 2016] of a published LLM naming-game simulation, varying six specification choices a reimplementer must make. Variants that are defensible readings of the paper stay within statistical noise of our baseline reconstruction. Missing one instruction that the paper states but is easy to overlook (that the model answers as an outside observer rather than as a player) raises the share of runs settling on the convention agents individually favor from 0.35 to 1.00 and makes convergence three times faster, in a reimplementation that uses a different model from the original. We complement the demonstration with a reconstruction-sufficiency review of 28 published LLM-agent simulations, finding that the details of how prompts are built and how model outputs are parsed are undetermined in 77% of cases, and that no paper fully specifies its main LLM call. ODD+LLM gives the field a standard home for information it already produces but currently scatters across code repositories, supplementary files, and undocumented defaults.

---


### 48. [Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents](https://arxiv.org/abs/2611.08946)

**<font color=#1a73e8>作者：</font>** Jingdong Zhang, Jionghao Wang, Zhengming Yu 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier language models are increasingly deployed as agents, and how well an agent performs depends not only on its model but also on its harness: the prompts, tools, memory, and control loop through which the model acts. When an agent is applied to a new problem, a natural question is whether it can use the feedback of the task to improve the way it works, and not merely its answer. Most existing benchmarks keep the agent's harness fixed and score the solution it produces, or target large-scale model training. We introduce Flex-RSI, a benchmark for the recursive self-improvement of agents on vision and robotics tasks under a fixed budget. In each round, an executor improves the task solution, which is kept only if it scores higher on held-out validation data, and an improver then revises the harness, including the executor and itself. Every run starts from the same general-purpose harness, and the final solution is scored on hidden test data. Evaluating closed-source and open-weight models on tasks spanning perception, reasoning, robot action, 3D reconstruction, visual creation, and infrastructure, we find that self-improvement helps most when the agent builds its own solution, that feedback recording only success or failure holds back open-weight models, and that open-weight models fall furthest behind where outputs must pass strict checks of physical stability or exact correctness. Paired runs further show that editing the harness itself contributes to the gains.

---


### 49. [AIM: Adaptive Interaction in Multi-Agent Debate for Multimodal LLM Inference](https://arxiv.org/abs/2611.08950)

**<font color=#1a73e8>作者：</font>** Wei Fan, JinYi Yoon, Bo Ji  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Debate (MAD) improves reasoning on multimodal tasks, but its accuracy and token efficiency depend on how agents interact during debate. A largely overlooked design choice is which interaction modalities agents use to exchange evidence. Existing methods rely on fixed text- or graph-based interaction, which fails to convey fine-grained multimodal evidence and thus degrades accuracy while inflating token cost due to verbose descriptions. To address this, we propose Adaptive Interaction in Multi-Agent Debate (AIM), an adaptive routing framework that dynamically selects the optimal modality combination for inter-agent interaction in multimodal MAD. Beyond text and graph, AIM introduces task-dependent modality interaction, where agents exchange targeted regions of interest from the task-specific multimodal input, such as image regions, audio segments, or spatio-temporal video clips. To determine the best combination for each instance, AIM first generates a structured baseline response and extracts interpretable routing features that capture which evidence the instance requires, how confident the baseline agent is, and how much new evidence each modality would add beyond the baseline response. A lightweight router then uses these routing features to select a modality combination that avoids both under-fusion (i.e., agents miss decisive evidence) and over-fusion (i.e., redundant modalities inflate token cost) risks. Across eight benchmarks spanning three multimodal task families, \name achieves the highest accuracy. Combining modalities improves accuracy by up to 6.4\% over the best single-modality baseline, and adapting the combination per instance adds up to 4.2\% over the most accurate fixed combination of each benchmark with up to 53.4\% fewer tokens.

---


### 50. [Using an LLM to Tackle Difficult Cases in NER for Nepali Tweets](https://arxiv.org/abs/2611.08967)

**<font color=#1a73e8>作者：</font>** Claire Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Named entity recognition (NER) is challenging for social media data in a low-resource language. LLMs often lag behind pretrained language models (PLMs) in NER performance, but they show promise in handling cases that PLMs struggle with. Using a dataset of Nepali tweets, we split the test set into "easy" and "hard" cases using token probabilities from a fine-tuned pretrained language model (PLM). We then evaluate an LLM on the hard test cases using 16 different prompt configurations. We find that selecting examples based on semantic similarity and increasing the number of examples improves F1 score by almost 10 points from the baseline configuration. Although the LLM underperforms the PLM on the full and easy test sets, it surpasses the PLM on the hard test set, resulting in an improved score when the two models are combined.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-174](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
