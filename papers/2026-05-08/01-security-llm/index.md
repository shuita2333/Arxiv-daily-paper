# 🔐 大模型安全相关研究 | 2026年05月08日

> 本类共 **9** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Membership Inference Attacks for Retrieval Based In-Context Learning for Document Question Answering](https://arxiv.org/abs/2605.04116)

**<font color=#1a73e8>作者：</font>** Tejas Kulkarni, Antti Koskela, Laith Zumot  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We show that remotely hosted applications employing in-context learning when augmented with a retrieval function to select in-context examples can be vulnerable to membership-inference attacks even when the service provider and users are separate parties. We propose two black-box membership inference attacks that exploit query text prefixes to distinguish member from non-member inputs. The first attack uses a reference model to estimate an otherwise unavailable loss metric. The second attack improves upon it by eliminating the reference model and instead computing a membership statistic through a simple but novel weighted-averaging scheme. Our comprehensive empirical evaluations consider a stricter case in which the adversary has a paraphrased version of the text in the queries and show that our attacks can exhibit stronger resilience to paraphrasing and outperform three prior attacks in many cases with small number of prefixes. We also adapt an existing ensemble prompting defense to our setting, demonstrating that it substantially mitigates the privacy leakage caused by our second attack.

---


### 2. [Laundering AI Authority with Adversarial Examples](https://arxiv.org/abs/2605.04261)

**<font color=#1a73e8>作者：</font>** Jie Zhang, Pura Peetathawatchai, Florian Tramèr 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly deployed as trusted authorities -- fact-checking images on social media, comparing products, and moderating content. Users implicitly trust that these systems perceive the same visual content as they do. We show that adversarial examples break this assumption, enabling \emph{AI authority laundering}: an attacker subtly perturbs an image so that the VLM produces confident and authoritative responses about the \emph{wrong} input. Unlike jailbreaks or prompt injections, our attacks do not compromise model alignment; the attack operates entirely at the perceptual level. We demonstrate that standard attacks against publicly available CLIP models transfer reliably to production VLMs -- including GPT-5.4, Claude Opus~4.6, Gemini~3, and Grok~4.2. Across four attack surfaces, we show that authority laundering can amplify misinformation, disparage individuals, evade content moderation, and manipulate product recommendations. Our attacks have high success rates: In hundreds of attacks targeting identity manipulation and NSFW evasion, we measure success rates of $22 - 100\%$ across six models. No novel attack algorithm is required: basic techniques known for over a decade suffice, establishing a lower bound on attacker capability that should concern defenders. Our results demonstrate that visual adversarial robustness is now a practical -- and still largely unsolved -- safety problem.

---


### 3. [Misrouter: Exploiting Routing Mechanisms for Input-Only Attacks on Mixture-of-Experts LLMs](https://arxiv.org/abs/2605.04446)

**<font color=#1a73e8>作者：</font>** Zekun Fei, Zihao Wang, Weijie Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures have emerged as a leading paradigm for scaling large language models through sparse, routing-based computation. However, this design introduces a new attack surface: the routing mechanism that determines which experts process each input. Prior work shows that manipulating routing can bypass safety alignment, but existing attacks require model modification and thus apply only to locally deployed models. By contrast, real-world LLM services are remotely hosted and accessible only through input queries. This raises a fundamental question: can MoE routing be exploited through input-only attacks to induce stronger unsafe behaviors in real-world services? Our key insight is to optimize attacks in a white-box setting on open-source surrogate MoE models and transfer the resulting adversarial inputs to public API services within the same model family. This setting presents three main challenges: routing can be influenced only indirectly through input perturbations, routing control and output generation are tightly coupled, and even a successful safety bypass may still produce low-quality responses. To address these challenges, we propose Misrouter, an input-only attack framework that jointly targets routing behavior and expert functionality. Misrouter identifies weakly aligned experts that are willing to produce target harmful content by analyzing expert activations under harmful queries paired with unsafe continuations. It then optimizes adversarial inputs to steer routing toward these experts and away from strongly aligned ones. It further biases routing toward highly capable general-purpose experts identified from benign question-answering tasks. Finally, because routing and output objectives can conflict, Misrouter uses a two-phase optimization strategy that first steers routing and then optimizes harmful outputs while preserving routing stability.

---


### 4. [Pen-Strategist: A Reasoning Framework for Penetration Testing Strategy Formation and Analysis](https://arxiv.org/abs/2605.04499)

**<font color=#1a73e8>作者：</font>** Yasod Ginige, Pasindu Marasinghe, Sajal Jain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber threats are rapidly increasing, expanding their impact from large-scale enterprises to government services and individual users, making robust security systems increasingly essential. However, a significant shortage of skilled cybersecurity professionals exacerbates this challenge. While recent research has explored automating tasks such as penetration testing using LLM-based agents, existing frameworks often perform poorly due to limited capability in strategy formulation, domain-specific reasoning, and accurate action and tool selection. To overcome these limitations, we propose Pen-Strategist framework, consisting of a novel domain-specific reasoning model that derives pentesting strategies via logical reasoning and a classifier that converts the strategies into actionable steps. First, we construct a reasoning dataset containing logical explanations for both strategy derivation and step selection in pentesting scenarios. We then fine-tune a Qwen-3-14B model for strategy generation using reinforcement learning. Evaluation on the test split of the dataset demonstrates a 87% improvement in strategy derivation performance compared to the baseline. Furthermore, we integrate the fine-tuned Pen-Strategist model into existing automated pentesting frameworks, such as PentestGPT, and evaluate its performance on vulnerable machines, achieving a 47.5% improvement in subtask completion while surpassing the baseline GPT-5. Further experiments on the CTFKnow benchmark show an 18% performance gain over the base model. For step prediction, we train a semantic-based CNN classifier, which outperforms commercial LLMs by 28% and enhances execution stability. Finally, we conduct a user study to qualitatively assess the generated strategies, and Pen-Strategist demonstrates superior performance compared to the Claude-4.6-Sonnet.

---


### 5. [Sparse Tokens Suffice: Jailbreaking Audio Language Models via Token-Aware Gradient Optimization](https://arxiv.org/abs/2605.04700)

**<font color=#1a73e8>作者：</font>** Zheng Fang, Xiaosen Wang, Shenyi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Jailbreak attacks on audio language models (ALMs) optimize audio perturbations to elicit unsafe generations, and they typically update the entire waveform densely throughout optimization. In this work, we investigate the necessity of such dense optimization by analyzing the structure of token-aligned gradients in ALMs. We find that gradient energy is highly non-uniform across audio tokens, indicating that only a small subset of token-aligned audio regions dominates the optimization signal. Motivated by this observation, we propose Token-Aware Gradient Optimization (TAGO), which enables sparse jailbreak optimization by retaining only waveform gradients aligned with audio tokens that have high gradient energy, while masking the remaining gradients at each iteration. Across three ALMs, TAGO outperforms baselines, and substantial sparsification preserves strong attack success rates (e.g. on Qwen3-Omni, $\mathrm{ASR}_{l}$ remains at 86% with a token retention ratio of 0.25, compared to 87% with full token retention). These results demonstrate that dense waveform updates are largely redundant, and we advocate that future audio jailbreak and safety alignment research should further leverage this heterogeneous token-level gradient structure.

---


### 6. [A Pragmatic Comparison of Cryptographic Computation Technologies for Machine Learning](https://arxiv.org/abs/2605.04858)

**<font color=#1a73e8>作者：</font>** Marcus Taubert, Adam Skuta, Thomas Loruenser  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As security demands increase, the importance of secure computation technologies grows, yet these technologies can often seem overwhelming to practitioners. Furthermore, many approaches focus only on a single technology, potentially overlooking superior alternatives. This work aims to address the issue of selecting the right technology for secure computation by presenting a comparative analysis of two highly relevant cryptographic methods and their software implementations, with a particular focus on machine learning. Firstly, we provide a theoretical summary and comparison of the secure computation paradigms of secure multi-party computation (SMPC) and fully homomorphic encryption (FHE). We outline the advantages and limitations of the protocols, as well as the relevant open-source software implementations. Secondly, we present the results of extensive benchmarking of the main software frameworks identified for machine learning operations and models. Regarding the current state of the art in FHE, we observe that it outperforms SMPC for regressions. Additionally it may be faster for simple dense networks using GPUs or Hybrid Models. Conversely, SMPC showed superior performance for complex models such as CNNs. Our results should pave the way for more technology-agnostic benchmarking of secure computation technologies for machine learning, providing guidance for practitioners looking to adopt these technologies.

---


### 7. [You Snooze, You Lose: Automatic Safety Alignment Restoration through Neural Weight Translation](https://arxiv.org/abs/2605.04992)

**<font color=#1a73e8>作者：</font>** Marco Arazzi, Vignesh Kumar Kembu, Antonino Nocera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The open-source ecosystem has accelerated the democratization of Large Language Models (LLMs) through the public distribution of specialized Low-Rank Adaptation (LoRA) modules. However, integrating these third-party adapters often induces catastrophic forgetting of the base model's foundational safety alignment. Restoring these guardrails via fine-tuning on safety data introduces an opposing failure mode: the severe degradation of the specialized domain knowledge the adapter was originally designed to provide. To overcome this zero-resource challenge, we propose Neural Weight Translation (NeWTral), a framework that directly maps unsafe, domain-specific adapters onto a safe alignment manifold while rigorously preserving their core expertise. NeWTral operates as a non-linear translation module pre-trained on a diverse corpus of unsafe-to-safe adapter pairs. By executing this mapping entirely within the parameter space, NeWTral utilizes an adaptive Mixture of Experts (MoE) routing strategy to autonomously blend high-fidelity surgical translators and aggressive alignment experts. We evaluate our framework across four architectural families (Llama, Mistral, Qwen, and Gemma) at scales up to 72B parameters across eight diverse scientific and professional domains. Our results demonstrate that the MoE variant achieves a radical reduction in the average Attack Success Rate (ASR), dropping from 70% in unsafe experts to just 13%, while maintaining an exceptional 90\% average knowledge fidelity. Much like the crowdsourced adapters it remedies, the NeWTral module is designed as a standalone, downloadable asset that allows practitioners to restore safety alignment instantly without requiring access to original training data or hardware-intensive retraining.

---


### 8. [Agentic Vulnerability Reasoning on Windows COM Binaries](https://arxiv.org/abs/2605.05000)

**<font color=#1a73e8>作者：</font>** Hwiwon Lee, Jongseong Kim, Lingming Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Windows Component Object Model (COM) services run with elevated privileges and are widely accessible to authenticated users, making race conditions in these binaries a critical surface for local privilege escalation. We present SLYP, an end-to-end agentic pipeline that discovers race condition vulnerabilities in COM binaries and generates debugger-verified proof-of-concept (PoC) code. SLYP exposes binary exploration, COM inspection, and dynamic debugging as reusable tool interfaces, giving agents the static context, COM activation metadata, and debugger feedback needed to move from vulnerability discovery to verified PoC generation. On a benchmark of 20 COM objects covering 40 vulnerability cases, SLYP achieves 0.973 F1, outperforming production coding agents by up to 0.208 F1 and the state-of-the-art static analyzer by 3.3x in bug discovery. For PoC generation, production coding agents in their default setup (without our COM inspection and dynamic debugging tools) verify essentially no cases on either frontier model, whereas SLYP's interactive toolsets enable it to autonomously synthesize working PoCs for 67.5% of cases on the strongest configuration. Deployed on production Windows services, SLYP discovers 28 previously unknown vulnerabilities across nine COM services, all confirmed by the Microsoft Security Response Center (MSRC) with 16 CVEs assigned and $140,000 in bounties. Furthermore, SLYP is designed with generalizable binary analysis and debugging interfaces, making it readily applicable to other commercial off-the-shelf (COTS) binaries beyond Windows COM services.

---


### 9. [SoK: Robustness in Large Language Models against Jailbreak Attacks](https://arxiv.org/abs/2605.05058)

**<font color=#1a73e8>作者：</font>** Feiyue Xu, Hongsheng Hu, Chaoxiang He 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have achieved remarkable success but remain highly susceptible to jailbreak attacks, in which adversarial prompts coerce models into generating harmful, unethical, or policy-violating outputs. Such attacks pose real-world risks, eroding safety, trust, and regulatory compliance in high-stakes applications. Although a variety of attack and defense methods have been proposed, existing evaluation practices are inadequate, often relying on narrow metrics like attack success rate that fail to capture the multidimensional nature of LLM security. In this paper, we present a systematic taxonomy of jailbreak attacks and defenses and introduce Security Cube, a unified, multi-dimensional framework for comprehensive evaluation of these techniques. We provide detailed comparison tables of existing attacks and defenses, highlighting key insights and open challenges across the literature. Leveraging Security Cube, we conduct benchmark studies on 13 representative attacks and 5 defenses, establishing a clear view of the current landscape encompassing jailbreak attacks, defenses, automated judges, and LLM vulnerabilities. Based on these evaluations, we distill critical findings, identify unresolved problems, and outline promising research directions for enhancing LLM robustness against jailbreak attacks. Our analysis aims to pave the way towards more robust, interpretable, and trustworthy LLM systems. Our code is available at Code.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
